# ACTION MOD CORE by Tristimdorion
# Create a ActionMod class, it has the same parameters as the VREN Action class.
# Attach the ActionMod object to any action list in the game.
# If you need some extra initialization after the game has started pass an initialization function (None is default)
# ActionMod is added to save games when not present, the matching is based on the name property, so make sure it's unique (and don't change it between releases)

### TEMPLATE ###
#init 3 python:
    # def gym_requirement():
    #     if time_of_day == 4: # Can be removed
    #         return "Closed for the night."
    #     elif mc.business.funds < 40: # $40 per session.
    #         return "Not enough money."
    #     else:
    #         return True

    # def gym_initialization(self):
    #     gym.background_image = Image("Mods/mods/Room/images/Gym_Background.jpg") #As long a there is a mall background for the gym, replace it with our gym background
    #     # add gym shower to active places
    #     list_of_places.append(gym_shower)
    #     gym.link_locations_two_way(gym_shower)
    #     gym.actions.append(self)
    #     return

    # train_in_gym_action = ActionMod("Schedule Gym Session {image=gui/heart/Time_Advance.png}", gym_requirement, "select_person_for_gym", initialization = gym_initialization,  menu_tooltip = "Bring a person to the gym to train their body.")

# pre define variable for saving
define action_mod_list = None

init -1 python:
    def is_action_enabled(self, extra_args = None):
        if hasattr(self, "enabled"):
            if not self.enabled:
                return False

        requirement_return = self.check_requirement(extra_args)
        if isinstance(requirement_return, basestring):
            # Any string returned means the action is not enabled
            return False
        else:
            # If it's not a string it must be a bool
            return requirement_return

    def is_disabled_slug_shown(self, extra_args = None): # Returns true if this action is not enabled but should show something when it is disabled.
        if hasattr(self, "enabled"):
            if not self.enabled:
                return False

        requirement_return = self.check_requirement(extra_args)
        if isinstance(requirement_return, basestring):
            return True
        else:
            return False

    # Monkeywrench the action method overrides in the Action class
    Action.is_action_enabled = is_action_enabled
    Action.is_disabled_slug_shown = is_disabled_slug_shown

    # Initialize the randomizer
    renpy.random.seed()

    # BUGFIX MAIN CODE: The action functions are called wrong and the count has wrong indention level, so only 1 role gets checked.
    def valid_role_actions_enhanced(self):
        count = 0
        for role in self.special_role:
            for act in role.actions:
                if act.is_action_enabled(self) or act.is_disabled_slug_shown(self): #We should also check if a non-action disabled slug would be available so that the player can check what the requirement would be.
                    count += 1
        return count

    Person.valid_role_actions = valid_role_actions_enhanced


init 2 python:
    class ActionMod(Action):
        _instances = set()

        # store instances of mod
        def __init__(self, name, requirement, effect, args = None, requirement_args = None, menu_tooltip = "", initialization = None, category="Misc", enabled = True, allow_disable = True, priority = 10, on_enabled_changed = None, options_menu = None, is_crisis = False, is_morning_crisis = False, crisis_weight = None):
            self.initialization = initialization
            self.enabled = enabled
            self.allow_disable = allow_disable
            self.category = category
            self.priority = priority
            self.on_enabled_changed = on_enabled_changed
            self.options_menu = options_menu
            self.is_crisis = is_crisis
            self.is_morning_crisis = is_morning_crisis
            self.crisis_weight = crisis_weight

            Action.__init__(self, name, requirement, effect, args, requirement_args, menu_tooltip)

            ActionMod._instances.add(self)

        def __cmp__(self,other):
            if isinstance(other, Action):
                if self.effect == other.effect:
                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        def __hash__(self):
            return hash(self.effect)

        def initialize(self):
            if not self.initialization is None:
                self.initialization(self)

        def show_options(self):
            if not self.options_menu is None:
                renpy.call(self.options_menu)

        def toggle_enabled(self):
            self.enabled = not self.enabled
            # trigger event
            if not self.on_enabled_changed is None:
                self.on_enabled_changed(self.enabled)

    def action_mod_settings_requirement():
        return True

    # check all ActionMod classes in the game and make sure we have one instance of each and update the action_mod_list
    def append_and_initialize_action_mods():
        # add action_mod instances to list
        if not ActionMod._instances is None:
            # renpy.say("", "There are " + str(len(action_mod_list)) + " mods in save game.")
            for action_mod in sorted(ActionMod._instances, key = lambda x: x.priority):
                if action_mod not in action_mod_list:
                    action_mod_list.append(action_mod)
                    action_mod.initialize()

        # the crisis_list is not stored in save game
        remove_list = []
        for action_mod in action_mod_list:
            if not hasattr(action_mod, "is_crisis"):
                remove_list.append(action_mod)
            elif action_mod.is_crisis:
                if hasattr(action_mod, "is_morning_crisis") and action_mod.is_morning_crisis:
                    if not action_mod in [c[0] for c in morning_crisis_list]:
                        morning_crisis_list.append([action_mod, action_mod.crisis_weight])
                else:
                    if not action_mod in [c[0] for c in crisis_list]:
                        crisis_list.append([action_mod, action_mod.crisis_weight])

        # remove not working stuff
        for action_mod in remove_list:
            action_mod_list.remove(action_mod)

        return

    def try_fix_game_issues():
        # to fix game with old hair colour linked to hair style changed from v0.17 to v0.18
        for person in all_people_in_the_game([mc]):
            if isinstance(person.hair_colour, basestring):
                person.hair_colour = find_in_list(lambda x: x[0] == person.hair_colour, list_of_hairs) or list_of_hairs[0]
            elif not isinstance(person.hair_colour, list) or len(person.hair_colour) != 2:
                person.hair_colour = list_of_hairs[0]
        return

    # mod settings action
    action_mod_options_action = Action("MOD Settings", action_mod_settings_requirement, "show_action_mod_settings", menu_tooltip = "Enable or disable mods")
    action_mod_configuration_action = Action("MOD Configuration", action_mod_settings_requirement, "show_action_mod_configuration", menu_tooltip = "Change configuration for individual MODS")

init 4 python: # NOTE: Having it at 5 was causing errors after I moved things around. Haven't seen any side-effects of it.
    add_label_hijack("normal_start", "activate_action_mod_core")
    add_label_hijack("after_load", "update_action_mod_core")

# as long as VREN doesn't use this, we need to add a dummy label for hijacking purposes
# NOTE: this label gets called after the hijack labels have been triggered
label after_load:
    return

label activate_action_mod_core(stack):
    # initialize variable
    $ action_mod_list = []

    # define here using $ so it gets stored in save game
    python:
        append_and_initialize_action_mods()

        bedroom.actions.append(action_mod_options_action)
        bedroom.actions.append(action_mod_configuration_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

# called after loading a save game
label update_action_mod_core(stack):
    python:
        unmodded = False
        try:
            action_mod_list
        except NameError:
            unmodded = True

        # extra check to validate that action mod list exists correctly
        if not unmodded and not isinstance(action_mod_list, list):
            unmodded = True

    if unmodded:
        # initialize variable
        $ action_mod_list = []

    python:
        append_and_initialize_action_mods()
        if not action_mod_options_action in bedroom.actions:
            bedroom.actions.append(action_mod_options_action)
        if not action_mod_configuration_action in bedroom.actions:
            bedroom.actions.append(action_mod_configuration_action)

        try_fix_game_issues()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_action_mod_settings:
    hide screen main_ui
    hide screen phone_hud_ui
    hide screen business_ui
    call screen mod_configuration_ui
    show screen phone_hud_ui
    show screen business_ui
    show screen main_ui
    return

label show_action_mod_configuration:
    python:
        while True:
            tuple_list = []
            for action_mod in action_mod_list:
                if action_mod.enabled and hasattr(action_mod, "options_menu") and not action_mod.options_menu is None:
                    tuple_string = action_mod.name + " (tooltip)" + action_mod.menu_tooltip
                    tuple_list.append([tuple_string, action_mod])

            tuple_list = sorted(tuple_list, key=lambda x: x[0])
            tuple_list.append(["Back","Back"])
            action_mod_choice = renpy.display_menu(tuple_list, True, "Choice")

            if action_mod_choice == "Back":
                renpy.return_statement()
            else:
                action_mod_choice.show_options()
