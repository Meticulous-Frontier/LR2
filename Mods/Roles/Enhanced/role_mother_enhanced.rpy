init 5 python:
    def mom_weekly_pay_requirement(the_person):
        if the_person.is_available and day%7 == 5: #It is the end of the day on friday
            return True
        return False

    def wear_promotion_outfit(person, is_planned = False):
        interview_outfit = person.event_triggers_dict.get("mom_work_promotion_outfit", None)
        if interview_outfit:
            if is_planned:
                person.next_day_outfit = interview_outfit.get_copy()
            person.planned_outfit = interview_outfit.get_copy() # also set it as planned so she doesn't change clothes on interactions
            person.apply_outfit(interview_outfit)
        return

label mom_weekly_pay_tit_fuck_label(the_person):    #Anticipate adding this as an option to Saturday morning payments. This scene not yet in game.
    mc.name "Alright, I'll pay you to let me fuck your tits."
    if (not the_person.has_taboo("touching_body")) or the_person.effective_sluttiness("touching_body") >= 40:
        "[the_person.title] peaks down at your crotch before responding."
        the_person "These tits?"
        "She jiggles her hefty tits for you a couple times."
        $ mc.change_locked_clarity(10)
        "You pull out your wallet and count out her cash while [the_person.possessive_title] gets onto her knees in front of you."
        $ mc.business.change_funds(-200)
        $ the_person.draw_person(position = "blowjob")
        $ the_person.strip_to_tits(position = "blowjob")
        the_person "Remember, not a word to anyone else though. Okay?"
        mc.name "Of course, this is just between you and me... and your tits."
        $ the_person.break_taboo("touching_body")
    else:
        the_person "What? I mean... I could never do that! I'm your mother!"
        "You pull out your wallet and count out the cash while you talk."
        mc.name "Sure you could. It's just me and you here, nobody would ever need to know."
        mc.name "Besides, it's for the family, right? This is just another way to help everyone out. Myself included, I've been real stressed at work lately."
        $ mc.business.change_funds(-200)
        "You lay the cash down on the table. [the_person.possessive_title] hesitates, then meekly reaches for the money."
        the_person "I don't know about this."
        mc.name "Sure you do [the_person.title]. Just get down on your knees and take your tits out. I'll do the rest."
        "She gives you a scowl, but obediently starts to do what she is told."
        $ the_person.draw_person(position = "blowjob")
        $ the_person.strip_to_tits(position = "blowjob")
        $ mc.change_locked_clarity(10)
        "She kneels down in front of you. You unzip your pants and pull your cock out for your mother."
        mc.name "Don't worry, you can just relax and close your eyes if you need to."
        the_person "Let's just get this over with..."
        $ the_person.break_taboo("touching_body")

    "You step closer and slowly slide your cock between [the_person.title]'s fantastic tits. She holds them together as you start to move your hips."
    $the_person.add_situational_obedience("deal", 20, "I'm doing this for the family")
    call fuck_person(the_person, private = True, start_position =tit_fuck, skip_intro = True, position_locked = True) from _call_fuck_jennifer_modded_0102
    $ the_person.clear_situational_obedience("deal")
    $ the_report = _return
    $ the_person.apply_outfit()
    if the_report.get("girl orgasms", 0) > 0:
        "You pull up your pants while [the_person.possessive_title] is on her knees panting, trying to get her breath back."
        mc.name "I didn't know you were going to enjoy that so much. Maybe you should be paying me next time."
        the_person "Ah... I hope we can come to some sort of deal... Ah... In the future..."
    else:
        $ the_person.draw_person()
        "You pull your pants up while [the_person.possessive_title] gets off of her knees and cleans herself up."
    $ the_person.change_obedience(4)
    return
