# Pheremone Therapy Serum by Starbuck

init -1 python:
    def ovulation_function_on_turn(the_person, add_to_log):
        if get_slut_tier(the_person) < 5:
            if renpy.random.randint(0,100) <50:  #chance to increase core sluttiness
                the_person.change_slut_core    (1, add_to_log)
            the_person.change_slut_temp(2, add_to_log)

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_ovulation_serum_trait(stack):
    python:
        ovulation_ther = SerumTraitMod(name = "Hormonal Ovulation",
                desc = "Reproduces hormones naturally occuring during ovulation to make females more receptive to sex. Increases sluttiness over time.",
                positive_slug = "+(0-2) Sluttiness/Turn, +$40 Value",
                negative_slug = "+200 Serum Research",
                value_added = 40,
                research_added = 200,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = ovulation_function_on_turn,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 3,
                start_researched =  False,
                research_needed = 1500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        execute_hijack_call(stack)
    return
