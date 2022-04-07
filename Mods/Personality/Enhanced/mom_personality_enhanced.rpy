init 5 python:
    config.label_overrides["mom_sex_obedience_accept"] = "mom_sex_obedience_accept_enhanced"

label mom_sex_obedience_accept_enhanced(the_person):
    if the_person.sluttiness > 70:
        the_person "I know we shouldn't be doing this. I know I should say no..."
        the_person "But just a little more couldn't hurt, right?"
    else:
        if the_person.obedience > 130:
            the_person "I... We really shouldn't... But I know it would make you so happy. Okay [the_person.mc_title], let's try it"
        else:
            the_person "How does this keep happening [the_person.mc_title]? You know I love you but we shouldn't be doing this..."
            "[the_person.possessive_title] looks away, conflicted."
        if not mc.business.event_triggers_dict.get("family_threesome", False):
            the_person "I... You just have to make sure your sister never knows about this. Nobody can know..."
    return
