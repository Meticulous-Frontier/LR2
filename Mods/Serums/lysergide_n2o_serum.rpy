# Lysergide N2O Serum by Tristimdorion

init -1 python:
    def lysergide_n2o_trait_on_apply(person, add_to_log):
        if suggestable_role not in person.special_role: # Make it not duplicate itself if it is re- applied before removed
            person.special_role.append(suggestable_role)
        if add_to_log:
            mc.log_event((person.title or person.name) + " is suggestable.", "float_text_blue")
        return

    def lysergide_n2o_trait_on_remove(person, add_to_log):
        # role is also removed after an influence attempt
        if suggestable_role in person.special_role:
            person.special_role.remove(suggestable_role)
            if add_to_log:
                mc.log_event((person.title or person.name) + " is no longer suggestable.", "float_text_blue")
        return

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_lysergide_n2o_serum_trait(stack):
    python:
        lysergide_n2o_serum_trait = SerumTraitMod(name = "Lysergide N2O Trait",
            desc = "Increases target subjects suggestibility, using LSD and Nitrous Oxide components to change the higher brainfunction to become more receptable to suggestions.",
            positive_slug = "+$25 Value, increases suggestibility while active",
            negative_slug = "+200 Serum Research",
            value_added = 25,
            research_added = 200,
            base_side_effect_chance = 50,
            on_apply = lysergide_n2o_trait_on_apply,
            on_remove = lysergide_n2o_trait_on_remove,
            requires = [basic_med_app, suggestion_drugs_trait],
            tier = 2,
            research_needed = 500)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
