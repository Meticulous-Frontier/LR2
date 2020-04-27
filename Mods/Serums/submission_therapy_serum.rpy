# Submission Therapy Serum by Starbuck

init -1 python:
    def submission_function_on_apply(the_person, add_to_log):
        the_person.change_slut_core(-15, add_to_log, fire_event = False)
        the_person.change_slut_temp(-15, add_to_log)

    def submission_function_on_remove(the_person, add_to_log):
        the_person.change_slut_core(15, add_to_log, fire_event = False)
        the_person.change_slut_temp(15, add_to_log)

    def submission_function_on_turn(the_person, add_to_log):
        the_person.change_obedience(3, add_to_log)

    def add_submission_serum_trait():
        sub_ther = SerumTraitMod(name = "Submission Therapy",
                desc = "Introduces substances that naturally incline females to obey males, found in many mammals. Reduces feeling in the skin, including erogenous zones.",
                positive_slug = "+3 Obedience/Turn, +$20 Value",
                negative_slug = "-15 Sluttiness, +80 Serum Research",
                value_added = 20,
                research_added = 80,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
                on_apply = submission_function_on_apply,
                on_remove = submission_function_on_remove,
                on_turn = submission_function_on_turn,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 2,
                start_researched =  False,
                research_needed = 800,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )


# any label that starts with serum_mod is added to the serum mod list
label serum_mod_submission_therapy_serum_trait(stack):
    python:
        add_submission_serum_trait()
        execute_hijack_call(stack)
    return
