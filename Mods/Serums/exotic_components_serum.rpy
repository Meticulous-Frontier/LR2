# Exotic Ingredients Serum by RogueKnightUK

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_exotic_components_serum_trait(stack):
    python:
        exotic_components = SerumTraitMod(name = "Exotic Ingredients",
            desc = "Exotic sounding ingredients from unlikely sources ranging from unheard tree saps to rare flower products give the customers the idea that this serum must be very special indeed, and increase it's sale value accordingly. There make is no change to the effects of the serum.",
            positive_slug = "+$40 Value",
            negative_slug = "+100 Serum Research",
            value_added = 40,
            research_added = 100,
            base_side_effect_chance = 1,
            requires = [basic_med_app, improved_serum_prod],
            tier = 1,
            research_needed = 300)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return







