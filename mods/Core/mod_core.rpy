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
    #     gym.actions.append(self.action)
    #     return

    # train_in_gym_action = Mod("Schedule Gym Session {image=gui/heart/Time_Advance.png}", gym_requirement, "select_person_for_gym", initialization = gym_initialization,  menu_tooltip = "Bring a person to the gym to train their body.")

init -2 python:
    game_mod_list = []

init -1 python:
    def is_mod_enabled(action_name):
        is_enabled = True
        for mod in game_mod_list:
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
    class Mod(renpy.store.object):
        def __init__(self, name, requirement, effect, args = None, requirement_args = None, menu_tooltip = None, initialization = None, category="Misc", enabled = True):
            self.name = name
            self.requirement = requirement
            self.effect = effect
            self.args = args
            self.requirement_args = requirement_args
            self.menu_tooltip = menu_tooltip
            self.initialization = initialization
            self.enabled = enabled
            self.category = category
           
            game_mod_list.append(self)

            self.action = Action(name, requirement, effect, args, requirement_args, menu_tooltip)
        
        def __cmp__(self, other): ##This and __hash__ are defined so that I can use "if Mod in List" and have it find identical actions that are different instances.
            if type(other) is Mod:
                if self.name == other.name and self.requirement == other.requirement and self.effect == other.effect and self.args == other.args:
                    return 0
                else:
                    if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                        return -1
                    else:
                        return 1
            else:
                if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                    return -1
                else:
                    return 1

        def __hash__(self):
            return hash((self.name,self.requirement,self.effect))

        def initialize(self):
            if not self.initialization is None:
                self.initialization(self)

        def toggle_enabled(self):
            self.enabled = not self.enabled

    def mod_settings_requirement():
        return True

init 500 python:
    add_label_hijack("normal_start", "activate_mod_core")

label activate_mod_core:
    python:
        for mod in game_mod_list:
            mod.initialize()

        mod_options_action = Action("Mod Settings", mod_settings_requirement, "show_mod_settings", menu_tooltip = "Enable or disable mods")
        bedroom.actions.append(mod_options_action)
    return

label show_mod_settings:
    python:
        global active_category
        tuple_list = []
        for mod in game_mod_list:
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
            renpy.jump("game_loop")
        else:
            active_category = category_choice.category
            renpy.jump("change_mod_category")
    return

label change_mod_category():
    python:
        tuple_list = []
        for mod in game_mod_list:
            if (mod.category == active_category):
                tuple_string = mod.name + "\n Active: " + str(mod.enabled)
                tuple_list.append([tuple_string, mod])

        tuple_list = sorted(tuple_list, key=lambda x: x[0])
        tuple_list.append(["Back","Back"])
        mod_choice = renpy.display_menu(tuple_list, True, "Choice")

        if mod_choice == "Back":
            renpy.jump("show_mod_settings")
        else:
            mod_choice.toggle_enabled()
            renpy.jump("change_mod_category")
    return