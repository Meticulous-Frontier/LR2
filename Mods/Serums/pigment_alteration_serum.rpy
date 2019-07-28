
init -1 python:
    def pigment_serum_on_apply(person, add_to_log):
        skin_styles = [x[0] for x in list_of_skins]
        skin_styles.remove(person.skin)
        new_skin = get_random_from_list(skin_styles)
        return person.match_skin(new_skin)

label serum_mod_pigment_serum_trait(stack):
    python:
        pigment_serum_trait = SerumTraitMod(name = "Pigment Trait",
            desc = "Causes instantanious alterations in the subject's pigment distribution causing noticeable changes in skin color",
            positive_slug = "-$15 Value, Changes the subject's skin color",
            negative_slug = "+125 Serum Research",
            value_added = -15,
            research_added = 125,
            base_side_effect_chance = 20,
            on_apply = pigment_serum_on_apply,
            requires = basic_med_app,
            tier = 1,
            research_needed = 500)

        execute_hijack_call(stack)
    return
