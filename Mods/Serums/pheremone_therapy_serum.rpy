# Pheremone Therapy Serum by Starbuck

init -1 python:
    def pheremone_therapy_on_apply(the_person, add_to_log):
        the_person.change_slut_core(15, add_to_log, fire_event = False)
        the_person.change_slut_temp(15, add_to_log)

    def pheremone_therapy_on_remove(the_person, add_to_log):
        the_person.change_slut_core(-15, add_to_log, fire_event = False)
        the_person.change_slut_temp(-15, add_to_log)

    def add_pheromone_therapy_serum():
        pher_ther = SerumTraitMod(name = "Pheromone Therapy",
                desc = "By mimicking pheromones found in closely related animals, this serum can recreate feelings of going into heat in women.",
                positive_slug = "+$40 Value, +15 Sluttiness",
                negative_slug = "+200 Serum Research",
                value_added = 40,
                research_added = 200,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
                on_apply = pheremone_therapy_on_apply,
                on_remove = pheremone_therapy_on_remove,
        #     on_turn = a_function,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 2,
                start_researched =  False,
                research_needed = 800,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )


# any label that starts with serum_mod is added to the serum mod list
label serum_mod_pheremone_therapy_serum_trait(stack):
    python:
        add_pheromone_therapy_serum()
        execute_hijack_call(stack)
    return
