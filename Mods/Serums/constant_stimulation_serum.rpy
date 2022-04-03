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
        if renpy.random.randint(0, 100) < (the_person.suggestibility + 10) - the_person.sluttiness:
            the_person.change_slut(1)   #No cap because the condition should cap it for us, gives reward for extremely high suggestibility values also.

    constant_stimulation_ther = SerumTraitMod(name = "Constant Stimulation",
            desc = "Slowly increases sluttiness. Strong wills can resist it, but it increases effect based on suggestibility.",
            positive_slug = "Slowly increases sluttiness based on suggestibility",
            negative_slug = "",
            research_added = 100,
            base_side_effect_chance = 50,
            on_turn = constant_stimulation_on_turn,
            tier = 1,
            start_researched =  False,
            research_needed = 500,
            clarity_cost = 500,
            mental_aspect = 2, physical_aspect = 0, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = 3
        )
