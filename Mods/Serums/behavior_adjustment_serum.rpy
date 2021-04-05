# Pheremone Therapy Serum by Starbuck

init -1 python:
    def get_obedience_tier(person):
        if person.obedience < 80:
            return 0
        elif person.obedience < 100:
            return 1
        elif person.obedience < 120:
            return 2
        elif person.obedience < 140:
            return 3
        elif person.obedience < 160:
            return 4
        return 5

    def behavior_adjustment_on_turn(the_person, add_to_log, fire_event = True):
        if get_obedience_tier(the_person) < 5:
            suggestion_bonus = (get_suggest_tier(the_person) - get_obedience_tier(the_person)) * 10
            if renpy.random.randint(0, 100) < 20 + suggestion_bonus - (the_person.get_opinion_score("taking control") * 5):
                the_person.change_stats(obedience = 1, add_to_log = add_to_log)

    def add_behavior_adjustment_serum():
        behavior_adjustment_ther = SerumTraitMod(name = "Behavior Adjustment",
                desc = "Slowly increases obedience. Strong wills can resist it, but it increases effect based on suggestibility.",
                positive_slug = "Slowly increases obedience based on suggestibility, +$10 Value",
                negative_slug = "+100 Serum Research",
                value_added = 10,
                research_added = 100,
                base_side_effect_chance = 20,
                on_turn = behavior_adjustment_on_turn,
                tier = 1,
                start_researched =  False,
                research_needed = 500,
                clarity_cost = 500
            )

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_behavior_adjustment_serum_trait(stack):
    python:
        add_behavior_adjustment_serum()
        execute_hijack_call(stack)
    return
