# Osteomalacia Serum by Tristimdorion

init -1 python:
    def osteomalacia_serum_on_turn(person, add_to_log):
        return person.change_height(amount = -.0133334, chance = 20)

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_osteomalacia_serum_trait(stack):
    python:
        osteomalacia_serum_trait = SerumTraitMod(name = "Osteomalacia Serum",
            desc = "Decrease target subjects height, reduces calcium and vitimine D absorbtion combined with experimental component to slightly change height.",
            positive_slug = "-$15 Value, 20% Chance/Turn to decrease height by 1 inch",
            negative_slug = "+125 Serum Research",
            value_added = -15,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = osteomalacia_serum_on_turn,
            requires = clinical_testing,
            tier = 1,
            research_needed = 500)

        # enable serum and append to mod_list
        osteomalacia_serum_trait.initialize()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return