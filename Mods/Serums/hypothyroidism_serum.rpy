# Hypothyroidism Serum by Tristimdorion

init -1 python:
    def hypothyroidism_serum_on_turn(person, the_serum, add_to_log):
        return person.change_weight(amount = 0.5, chance = 50)

    def add_hypothyroidism_serum():
        hypothyroidism_serum_trait = SerumTraitMod(name = "Hypothyroidism Trait",
            desc = "Increase target subject body mass, by reducing hormones from the thyroid gland slowing down metabolism, thus causing weight gain.",
            positive_slug = "50% Chance/Turn to increase body mass by 500 grams, +$5 Value",
            negative_slug = "+125 Serum Research",
            value_added = 5,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = hypothyroidism_serum_on_turn,
            requires = basic_med_app,
            tier = 2,
            research_needed = 500,
            clarity_cost = 1500)

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_hypothyroidism_serum_trait(stack):
    python:
        add_hypothyroidism_serum()
        execute_hijack_call(stack)
    return
