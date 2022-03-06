
init -1 python:
    def pigment_serum_on_apply(person, the_serum, add_to_log):
        skin_styles = [x[0] for x in list_of_skins]
        skin_styles.remove(person.skin)
        new_skin = get_random_from_list(skin_styles)
        return person.match_skin(new_skin)

    def add_pigment_alteration_serum():
        pigment_serum_trait = SerumTraitMod(name = "Pigment Trait",
            desc = "Causes instantaneous alterations in the subject's pigment distribution causing noticeable changes in skin color",
<<<<<<< HEAD
            positive_slug = "Changes the subject's skin color, +$5 Value",
            negative_slug = "+125 Serum Research",
=======
            positive_slug = "Changes the subject's skin color",
            negative_slug = "",
>>>>>>> 6e6cb5b2a2e133ad3fbdb0a9cee754ecc1301374
            research_added = 125,
            base_side_effect_chance = 20,
            on_apply = pigment_serum_on_apply,
            requires = clinical_testing,
            tier = 3,
            research_needed = 500,
            clarity_cost = 2500,
<<<<<<< HEAD
            mental_aspect = 0, physical_aspect = 7, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 3)
=======
            mental_aspect = 2, physical_aspect = 6, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 3
        )
>>>>>>> 6e6cb5b2a2e133ad3fbdb0a9cee754ecc1301374


label serum_mod_pigment_serum_trait(stack):
    python:
        add_pigment_alteration_serum()
        execute_hijack_call(stack)
    return
