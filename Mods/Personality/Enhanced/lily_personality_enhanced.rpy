init 5 python:
    config.label_overrides["lily_sex_accept"] = "lily_sex_accept_enhanced"

label lily_sex_accept_enhanced(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            the_person "You're definitely my brother, I was thinking the same thing."
        else:
            the_person "You want to do that with your little sister [the_person.mc_title]? Well, you're lucky I'm just as perverted."
    else:
        if mc.business.event_triggers_dict.get("family_threesome", False):
            the_person "Okay, let's do it, next time we should include Mom, okay?"
        else:
            the_person "Okay, let's do it. Just make sure Mom never finds out, okay?"
    return
