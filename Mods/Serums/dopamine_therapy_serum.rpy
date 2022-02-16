# Dopamine Therapy Serum by Starbuck

init -1 python:
    def dopamine_therapy_on_turn(the_person, the_serum, add_to_log):
        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.happiness - 100)) * 5:
            the_person.change_happiness(1, add_to_log = add_to_log)

    def add_dopamine_therapy_serum():
        dopamine_therapy_ther = SerumTraitMod(name = "Dopamine Therapy",
                desc = "Slowly increases happiness. Increases effect based on suggestibility.",
                positive_slug = "Slowly increases happiness based on suggestibility",
                negative_slug = "",
                research_added = 100,
                base_side_effect_chance = 20,
                on_turn = dopamine_therapy_on_turn,
                tier = 1,
                start_researched =  False,
                research_needed = 500,
                clarity_cost = 500,
                mental_aspect = 3, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 1
            )

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_dopamine_therapy_serum_trait(stack):
    python:
        add_dopamine_therapy_serum()
        execute_hijack_call(stack)
    return
