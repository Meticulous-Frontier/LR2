# Hypothyroidism Serum

init -1 python:
    hypothyroidism_serum_mod_init = False

    def hypothyroidism_serum_on_turn(the_person, add_to_log):
        change_person_weight(the_person, .2, 20)
        return

init 2 python:
    def hypothyroidism_serum_mod_init_requirement():
        if hypothyroidism_serum_mod_init == False:
            return True
        return False

    hypothyroidism_serum_mod_init_event = Action("Hypothyroidism Serum Mod Initialization Event",hypothyroidism_serum_mod_init_requirement,"hypothyroidism_serum_mod_init_label")
    mod_list.append(hypothyroidism_serum_mod_init_event)

label hypothyroidism_serum_mod_init_label():
    # "Initiating Hypothyroidism Serum Mod Initialization"
    python:
        hypothyroidism_serum_trait = SerumTrait(name = "Hypothyroidism Serum",
            desc = "Increase target subject body mass, by reducing hormones from the thyroid gland slowing down methabolism, thus causing weight gain.",
            positive_slug = "-$15 Value, 20% Chance/Turn to increase body mass by 200 grams",
            negative_slug = "+125 Serum Research",
            value_added = -15,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = hypothyroidism_serum_on_turn,
            requires = basic_med_app,
            research_needed = 500)

        if hypothyroidism_serum_trait not in list_of_traits:
            list_of_traits.append(hypothyroidism_serum_trait)

        hypothyroidism_serum_mod_init = True
    return
