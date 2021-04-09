# Metabolizer Serum Trait by Tristimdorion

init -1 python:
    def anorexia_serum_on_turn(person, the_serum, add_to_log):
        return person.change_weight(amount = -0.5, chance = 50)

    def add_anorexia_serum():
        anorexia_serum_trait = SerumTraitMod(name = "Methabolizer Trait",
            desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centers to inhibit hunger and calorie intake.",
            positive_slug = "50% Chance/Turn to reduce body mass by 500 grams, +$5 Value",
            negative_slug = "+125 Serum Research",
            value_added = 5,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = anorexia_serum_on_turn,
            requires = basic_med_app,
            tier = 2,
            research_needed = 500,
            clarity_cost = 2000)


# any label that starts with serum_mod is added to the serum mod list
label serum_mod_anorexia_serum_trait(stack):
    python:
        add_anorexia_serum()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
