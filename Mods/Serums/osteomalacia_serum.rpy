# Osteomalacia Serum by Tristimdorion

init -1 python:
    def osteomalacia_serum_on_turn(person, the_serum, add_to_log):
        return person.change_height(amount = -.01693, chance = 20)

    def add_osteomalacia_serum():
        osteomalacia_serum_trait = SerumTraitMod(name = "Osteomalacia Trait",
            desc = "Decrease target subjects height, reduces calcium and vitamine D absorption combined with experimental component to slightly change height.",
            positive_slug = "20% Chance/Turn to decrease height by 1 cm, +$5 Value",
            negative_slug = "+125 Serum Research",
            value_added = 5,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = osteomalacia_serum_on_turn,
            requires = clinical_testing,
            tier = 3,
            research_needed = 500,
            clarity_cost = 2500
            )


# any label that starts with serum_mod is added to the serum mod list
label serum_mod_osteomalacia_serum_trait(stack):
    python:
        add_osteomalacia_serum()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
