#Extra Serum trait side effects. (Original by Computant)
init 2 python:

    ## uncontrollable_arousal_side_effect_functions ##
    def uncontrollable_arousal_side_effect_on_apply(the_person, the_serum, add_to_log):
        the_person.change_slut(20, add_to_log = add_to_log)

    def uncontrollable_arousal_side_effect_on_remove(the_person, the_serum, add_to_log):
        the_person.change_slut(-20, add_to_log = add_to_log)

    ## tryptamine_side_effect_functions ##
    def tryptamine_side_effect_on_apply(the_person, the_serum, add_to_log):
        the_person.change_obedience(10, add_to_log = add_to_log)

    def tryptamine_side_effect_on_remove(the_person, the_serum, add_to_log):
        the_person.change_obedience(-10, add_to_log = add_to_log)

    ## oxytocin_side_effect_functions ##
    def oxytocin_side_effect_on_turn(the_person, the_serum, add_to_log):
        the_person.change_love(1, max_modified_to = 40, add_to_log = False)

    uncontrollable_arousal_side_effect = SerumTrait(name = "Uncontrollable Arousal",
        desc = "An unintended interaction produces a sudden and noticeable spike in the recipient's promiscuity, making them more agreeable to lewd interactions.",
        positive_slug = "+20 Sluttiness for duration",
        negative_slug = "-$25 Value",
        on_apply = uncontrollable_arousal_side_effect_on_apply,
        on_remove = uncontrollable_arousal_side_effect_on_remove,
        is_side_effect = True,
        mental_aspect = 7, physical_aspect = 0, sexual_aspect = 9, medical_aspect = 0, flaws_aspect = 1, attention = 3)

    tryptamine_side_effect = SerumTrait(name = "Tryptamine Induction",
        desc = "An unintended interaction produces a sudden and noticeable degradation of the subject's free will, making them suspectable to suggestion for the duration.",
        positive_slug = "+10 Obedience for duration",
        negative_slug = "-$25 Value",
        on_apply = tryptamine_side_effect_on_apply,
        on_remove = tryptamine_side_effect_on_remove,
        is_side_effect = True,
        mental_aspect = 7, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 2)

    oxytocin_side_effect = SerumTrait(name = "Oxytocin Increment",
        desc = "An unintended interaction produces a sudden and lasting emotional connection to a person, but only when they have no deep connection already.",
        positive_slug = "Permanent +1 Love/Turn when Love < 40",
        negative_slug = "-$25 Value",
        on_turn = oxytocin_side_effect_on_turn,
        is_side_effect = True,
        mental_aspect = 2, physical_aspect = 0, sexual_aspect = 1, medical_aspect = 0, flaws_aspect = 1, attention = 1)

    if "list_of_side_effects" in globals():
        list_of_side_effects.append(uncontrollable_arousal_side_effect)
        list_of_side_effects.append(tryptamine_side_effect)
        list_of_side_effects.append(oxytocin_side_effect)
