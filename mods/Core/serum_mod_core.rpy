init 5 python:
    add_label_hijack("normal_start", "activate_serum_mod_core")

init 2 python:
    class SerumTraitMod(SerumTrait):
        # store instances of mod
        _instances = set()

        def __init__(self, name, desc, positive_slug = "", negative_slug = "", value_added = 0, research_added = 0, slots_added = 0, production_added = 0,
            duration_added = 0, base_side_effect_chance = 0, on_apply = None, on_remove = None, on_turn = None, on_day = None,
            requires= None, tier = 0, start_researched=False,research_needed=50,exclude_tags=None, is_side_effect = False):

            self.enabled = False
           
            SerumTrait.__init__(self, name,desc, positive_slug, negative_slug, value_added, research_added, slots_added, production_added,
                duration_added, base_side_effect_chance, on_apply, on_remove, on_turn, on_day, requires, tier, start_researched, research_needed, 
                exclude_tags, is_side_effect)

            # store the instance in class static    
            self._instances.add(self)

        def initialize(self):
            serum_mod_list.append(self)
            self.toggle_enabled()

        def toggle_enabled(self):
            self.enabled = not self.enabled
            if self.enabled:
                if not self in list_of_traits:
                    list_of_traits.append(self)
            else:
                if self in list_of_traits:
                    list_of_traits.remove(self)

    def serum_mod_settings_requirement():
        return True

label activate_serum_mod_core(stack):
    # define here using $ so it gets stored in save game
    $ serum_mod_list = []
    python:
        # find all serum mods, and append the creation to the stack
        for game_label in renpy.get_all_labels():
            if game_label.startswith("serum_mod_"):
                stack.append(game_label)

        # initalize configuration from bedroom
        serum_mod_options_action = Action("Serum MOD Settings", serum_mod_settings_requirement, "show_serum_mod_settings", menu_tooltip = "Enable or disable serum")
        bedroom.actions.append(serum_mod_options_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_serum_mod_settings:
    python:
        global active_serum_mod_tier
        tuple_list = []
        for serum_mod in serum_mod_list:
            has_serum_tier = False
            for tier in tuple_list:
                if serum_mod.tier == tier[1].tier:
                    has_serum_tier = True

            if not has_serum_tier:
                tuple_string = "Research Tier: " + str(serum_mod.tier)
                tuple_list.append([tuple_string, serum_mod])

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
            active_serum_mod_tier = category_choice.tier
            renpy.jump("change_serum_mod_tier")
    return

label change_serum_mod_tier:
    python:
        tuple_list = []
        for serum_mod in serum_mod_list:
            if (serum_mod.tier == active_serum_mod_tier):
                tuple_string = serum_mod.name + "\n Active: " + str(serum_mod.enabled)
                tuple_list.append([tuple_string, serum_mod])

        tuple_list = sorted(tuple_list, key=lambda x: x[0])
        tuple_list.append(["Back","Back"])
        serum_mod_choice = renpy.display_menu(tuple_list, True, "Choice")

        if serum_mod_choice == "Back":
            renpy.jump("show_serum_mod_settings")
        else:
            serum_mod_choice.toggle_enabled()
            renpy.jump("change_serum_mod_tier")
    return