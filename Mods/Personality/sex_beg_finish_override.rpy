# Will add a little of stripping to all the sex_beg_finish dialogs
# Original idea by BadRabbit

init 5 python:
    def hijack_beg_finish_labels():
        for lbl in renpy.get_all_labels():
            if lbl.endswith("sex_beg_finish"):
                add_label_hijack(lbl, "sex_beg_finish_enhanced")  

    def remove_clothing_based_on_preference(person):
        if person.get_opinion_score("showing her tits") > person.get_opinion_score("showing her ass"):
            # tits preference
            return person.strip_outfit_to_max_sluttiness(exclude_lower = True, temp_sluttiness_boost = 20)
        elif person.get_opinion_score("showing her tits") < person.get_opinion_score("showing her ass"):
            # vagina/ass preference
            return person.strip_outfit_to_max_sluttiness(exclude_upper = True, temp_sluttiness_boost = 20)
        else:
            # no preference
            return person.strip_outfit_to_max_sluttiness(temp_sluttiness_boost = 20)

    hijack_beg_finish_labels()

# she is desperate to continue and takes off some extra clothes based on her sluttiness.
label sex_beg_finish_enhanced(stack, *args, **kwargs):
    "[the_person.possessive_title] looks at you and..."

    python:
        remove_clothing_based_on_preference(the_person)
        execute_hijack_call(stack)
    return