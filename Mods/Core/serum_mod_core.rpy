# SERUM MOD CORE by Tristimdorion
# Its used for adding new SerumTraits to the game
# Create a SerumTraitMod class, it has the same parameters as the VREN Action class.
# SerumTraitMod is added to save games when not present, the matching is based on the name property, so make sure it's unique (and don't change it between releases)

### TEMPLATE ###
# init -1 python:
#     def anorexia_serum_on_turn(person, add_to_log):
#         return person.change_weight(amount = -.2, chance = 20)       

# # any label that starts with serum_mod is added to the serum mod list
# label serum_mod_anorexia_serum_trait(stack):
#     python:
#         anorexia_serum_trait = SerumTraitMod(name = "Anorexia Serum",
#             desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centers to inhibit hunger and calorie intake.",
#             positive_slug = "-$15 Value, 20% Chance/Turn to reduce body mass by 200 grams",
#             negative_slug = "+125 Serum Research",
#             value_added = -15,
#             research_added = 125,
#             base_side_effect_chance = 20,
#             on_turn = anorexia_serum_on_turn,
#             requires = basic_med_app,
#             tier = 1,
#             research_needed = 500)

#         # enable serum and append to mod_list
#         anorexia_serum_trait.initialize()

#         # continue on the hijack stack if needed
#         execute_hijack_call(stack)
#     return

init 5 python:
    add_label_hijack("normal_start", "activate_serum_mod_core")
    add_label_hijack("after_load", "update_serum_mod_core")

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


        def __cmp__(self,other): 
            if isinstance(other, SerumTrait):
                if self.name == other.name:
                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        def __hash__(self):
            return hash(self.name)


        # check if SerumMod class is already in the game append if needed and update serum_mod_list / list_of_traits list
        def initialize(self):
            for serum_mod in self._instances:
                if not serum_mod in serum_mod_list:
                    serum_mod_list.append(self)
                    self.toggle_enabled()

            remove_list = []
            for serum_mod in serum_mod_list:
                if serum_mod not in self._instances:
                    remove_list.append(serum_mod)

            # remove serum mods not in instance list
            for serum_mod in remove_list:
                if serum_mod in list_of_traits:
                    if serum_mod in list_of_traits:
                        list_of_traits.remove(serum_mod)
                    serum_mod_list.remove(serum_mod)

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

    # find all serum mods, and append the creation to the stack
    def append_serum_mods_to_stack(stack):
        for game_label in renpy.get_all_labels():
            if game_label.startswith("serum_mod_"):
                stack.append(game_label)
        return stack

    # Serum Mod
    serum_mod_options_action = Action("Serum MOD Settings", serum_mod_settings_requirement, "show_serum_mod_settings", menu_tooltip = "Enable or disable serum")

label activate_serum_mod_core(stack):
    $ serum_mod_list = []
    python:
        stack = append_serum_mods_to_stack(stack)

        # initalize configuration from bedroom
        bedroom.actions.append(serum_mod_options_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_serum_mod_core(stack):
    python:
        unmodded = False
        try:
            serum_mod_list
        except NameError:
            unmodded = True

        # extra check to validate that serum mod list exists correctly
        if not unmodded and not isinstance(serum_mod_list, list):
            unmodded = True

    if unmodded:
        $ serum_mod_list = []
        
    python:
        stack = append_serum_mods_to_stack(stack)

        if not serum_mod_options_action in bedroom.actions:
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
            renpy.return_statement()
        else:
            active_serum_mod_tier = category_choice.tier
            renpy.jump("change_serum_mod_tier")
    return

label change_serum_mod_tier:
    python:
        tuple_list = []
        for serum_mod in serum_mod_list:
            if (serum_mod.tier == active_serum_mod_tier):
                tuple_string = serum_mod.name + "\n Active: " + str(serum_mod.enabled) + " (tooltip)" + serum_mod.desc
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