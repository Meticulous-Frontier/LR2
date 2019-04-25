# Bulimia Serum

init -1 python:
    bulimia_serum_mod_init = False

    def bulimia_serum_on_turn(the_person, add_to_log):
        change_person_weight(the_person, .2, 20)
        return

init 2 python:
    def bulimia_serum_mod_init_requirement():
        if bulimia_serum_mod_init == False:
            return True
        return False

    bulimia_serum_mod_init_event = Action("Bulimia Serum Mod Initialization Event",bulimia_serum_mod_init_requirement,"bulimia_serum_mod_init_label")
    mod_list.append(bulimia_serum_mod_init_event)

label bulimia_serum_mod_init_label():
    # "Initiating Bulimia Serum Mod Initialization"
    python:
        bulimia_serum_trait = SerumTrait(name = "Bulimia Serum",
            desc = "Increase target subject body mass, using a high testorone serum component that increases cravings for high calorie foods and sugars.",
            positive_slug = "-$15 Value, 20% Chance/Turn to increase body mass by 200 grams",
            negative_slug = "+125 Serum Research",
            value_added = -15,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = bulimia_serum_on_turn,
            requires = basic_med_app,
            research_needed = 500)

        if bulimia_serum_trait not in list_of_traits:
            list_of_traits.append(bulimia_serum_trait)

        bulimia_serum_mod_init = True
    return
