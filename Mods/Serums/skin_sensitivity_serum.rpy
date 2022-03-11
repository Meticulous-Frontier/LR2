# Skin sensitivity serum original by Kaden

init -1 python:
    def skin_sensitivity_on_apply(the_person, the_serum, add_to_log):
        test_outfit = the_person.outfit.get_copy()
        the_clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True)
        if not the_clothing:
            return # nothing to strip
        test_outfit.remove_clothing(the_clothing)
        if not the_person.judge_outfit(test_outfit, temp_sluttiness_boost = the_person.suggestibility/2):
            return # too slutty
        if the_clothing in the_person.outfit.upper_body and test_outfit.tits_visible() and the_person.has_taboo("bare_tits"):
            return # won't strip to tits
        if the_clothing in the_person.outfit.lower_body and test_outfit.vagina_visible() and the_person.has_taboo("bare_pussy"):
            return # won't strip to vagina
        if test_outfit.underwear_visible() and the_person.has_taboo("underwear_nudity"):
            return # won't strip to underwear

        the_person.planned_outfit = test_outfit
        the_person.apply_outfit(the_person.planned_outfit)
        the_person.draw_animated_removal(the_clothing)
        # always log stripping
        mc.log_event((the_person.title or the_person.create_formatted_title("???")) + ": Removed her " + the_clothing.display_name, "float_text_grey")
        return

    def skin_sensitivity_on_turn(the_person, the_serum, add_to_log):
        if the_person.location.public:
            the_person.change_happiness(-2, add_to_log = add_to_log)
        if the_person.arousal < 50:
            the_person.change_arousal(5, add_to_log = add_to_log)
        return

    def add_skin_sensitivity():
        skin_sensitivity_serum_trait = SerumTraitMod(name = "Skin Sensitivity",
            desc = "Heighten the subjects sense of touch. This can lead to increased arousal, but in public it might be frustrating if their clothes are too restrictive.",
            positive_slug = "+5 Arousal/turn, may cause stripping when administered",
            negative_slug = "-2 Happiness/turn in public",
            research_added = 20,
            base_side_effect_chance = 30,
            on_apply = skin_sensitivity_on_apply,
            on_turn = skin_sensitivity_on_turn,
            requires = [clinical_testing],
            tier = 1,
            research_needed = 800,
            clarity_cost = 1000,
            mental_aspect = 3, physical_aspect = 1, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 2)
        return

label serum_mod_skin_sensitivity_trait(stack):
    python:
        add_skin_sensitivity()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
