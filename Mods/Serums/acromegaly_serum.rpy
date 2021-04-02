# Acromegaly Serum by Tristimdorion

init -1 python:
    def acromegaly_serum_on_turn(person, add_to_log):
        return person.change_height(amount = .01693, chance = 20)

    def add_acromegaly_serum():
        acromegaly_serum_trait = SerumTraitMod(name = "Acromegaly Trait",
            desc = "Increase target subjects height, stimulates the pituitary gland to increase growth hormone production and calcium absorption causing slight changes in height.",
            positive_slug = "20% Chance/Turn to increase height by 1 cm, +$5 Value",
            negative_slug = "+125 Serum Research",
            value_added = 5,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = acromegaly_serum_on_turn,
            requires = clinical_testing,
            tier = 3,
            research_needed = 500)
        return

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_acromegaly_serum_trait(stack):
    python:
        add_acromegaly_serum()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
