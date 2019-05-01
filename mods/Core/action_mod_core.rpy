# MOD CORE by Tristimdorion
# Create a Mod class, it has the same parameters as the VREN Action class\
# Attach the mod.action to any action list in the game.
# If you need some extra initialization after the game has started pass an initialization function

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

init -1 python:
    def is_mod_enabled(action_name):
        is_enabled = True
        for mod in action_mod_list:
            if mod.name == action_name:
                is_enabled = mod.enabled
        return is_enabled


    def is_action_enabled(self, extra_args = None):
        is_enabled = is_mod_enabled(self.name)
        if not is_enabled:
            return False

        requirement_return = self.check_requirement(extra_args)
        if isinstance(requirement_return, basestring):
            # Any string returned means the action is not enabled
            return False
        else:
            # If it's not a string it must be a bool
            return requirement_return

    def is_disabled_slug_shown(self, extra_args = None): # Returns true if this action is not enabled but should show something when it is disabled.
        is_enabled = is_mod_enabled(self.name)
        if not is_enabled:
            return False

        requirement_return = self.check_requirement(extra_args)
        if isinstance(requirement_return, basestring):
            return True
        else:
            return False

    # Monkeywrench the action method overrides in the Action class
    Action.is_action_enabled = is_action_enabled
    Action.is_disabled_slug_shown = is_disabled_slug_shown

init 2 python:
    class ActionMod(Action):
        # store instances of mod
        _instances = set()

        def __init__(self, name, requirement, effect, args = None, requirement_args = None, menu_tooltip = None, initialization = None, category="Misc", enabled = True):
            self.initialization = initialization
            self.enabled = enabled
            self.category = category

            Action.__init__(self, name, requirement, effect, args, requirement_args, menu_tooltip)

            # store the instance in class static
            self._instances.add(self)

        def initialize(self):
            if not self.initialization is None:
                self.initialization(self)

        def toggle_enabled(self):
            self.enabled = not self.enabled
        
        def getinstances(self):
            for instance in self._instances:
                yield instance()

    def action_mod_settings_requirement():
        return True

init 5 python:
    add_label_hijack("normal_start", "activate_action_mod_core")

label activate_action_mod_core(stack):
    # define here using $ so it gets stored in save game
    $ action_mod_list = []
    python:
        for action_mod in ActionMod._instances:
            action_mod_list.append(action_mod)
            action_mod.initialize()

        action_mod_options_action = Action("MOD Settings", action_mod_settings_requirement, "show_action_mod_settings", menu_tooltip = "Enable or disable mods")
        bedroom.actions.append(action_mod_options_action)
        
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_action_mod_settings:
    python:
        global active_action_mod_category
        tuple_list = []
        for mod in action_mod_list:
            has_category = False
            for cat in tuple_list:
                if mod.category == cat[1].category:
                    has_category = True

            if not has_category:
                tuple_string = "Category: " + mod.category
                tuple_list.append([tuple_string, mod])

        tuple_list = sorted(tuple_list, key=lambda x: x[0])
        tuple_list.append(["Back","Back"])
        category_choice = renpy.display_menu(tuple_list, True, "Choice")

        if category_choice == "Back":
            act_choice = call_formated_action_choice(mc.location.actions + ["Back"])

            if act_choice == "Back":
                renpy.jump("game_loop")
            else:
                act_choice.call_action()
        else:
            active_action_mod_category = category_choice.category
            renpy.jump("change_mod_category")
    return

label change_mod_category:
    python:
        tuple_list = []
        for action_mod in action_mod_list:
            if (action_mod.category == active_action_mod_category):
                tuple_string = action_mod.name + "\n Active: " + str(action_mod.enabled)
                tuple_list.append([tuple_string, action_mod])

        tuple_list = sorted(tuple_list, key=lambda x: x[0])
        tuple_list.append(["Back","Back"])
        action_mod_choice = renpy.display_menu(tuple_list, True, "Choice")

        if action_mod_choice == "Back":
            renpy.jump("show_action_mod_settings")
        else:
            action_mod_choice.toggle_enabled()
            renpy.jump("change_mod_category")
    return