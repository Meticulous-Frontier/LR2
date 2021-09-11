# Constant Stimulation Serum by Starbuck

init -1 python:
    def get_slut_tier(person):   #returns the heart value of the person
        if person.sluttiness < 25:
            return 0
        elif person.sluttiness < 50:
            return 1
        elif person.sluttiness < 75:
            return 2
        elif person.sluttiness < 100:
            return 3
        elif person.sluttiness < 125:
            return 4
        return 5

    def constant_stimulation_on_turn(the_person, the_serum, add_to_log):
        if get_slut_tier(the_person) < 5:
            suggestion_bonus = (1 + get_suggest_tier(the_person) - get_slut_tier(the_person)) * 10
            if renpy.random.randint(0, 100) < 10 + suggestion_bonus - (the_person.get_opinion_score("taking control") * 5):
                the_person.change_stats(slut = renpy.random.randint(0, 1), add_to_log = add_to_log)

    def add_constant_stimulation_serum():
        constant_stimulation_ther = SerumTraitMod(name = "Constant Stimulation",
                desc = "Slowly increases sluttiness. Strong wills can resist it, but it increases effect based on suggestibility.",
                positive_slug = "Slowly increases sluttiness based on suggestibility, +$15 Value",
                negative_slug = "+100 Serum Research",
                value_added = 15,
                research_added = 100,
                base_side_effect_chance = 50,
                on_turn = constant_stimulation_on_turn,
                tier = 1,
                start_researched =  False,
                research_needed = 500,
                clarity_cost = 500
            )


# any label that starts with serum_mod is added to the serum mod list
label serum_mod_constant_stimulation_serum_trait(stack):
    python:
        add_constant_stimulation_serum()
        execute_hijack_call(stack)
    return
