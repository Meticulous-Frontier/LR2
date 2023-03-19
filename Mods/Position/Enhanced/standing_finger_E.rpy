# enhancements for standing fingering
# Original code by BadRabbit


init 5 python:
    standing_finger.outro = "outro_standing_finger_enhanced"

label outro_standing_finger_enhanced(the_girl, the_location, the_object):
    "[the_girl.title] can tell you are getting close. She grinds her butt back into your crotch."
    "Feeling her butt on your crotch and [the_girl.title]'s hot, tight pussy squeezing your fingers is enough to push you that little bit further, past the point of no return."
    "You grasp her tightly with your free hand as you cum, shoving your fingers deep into her cunt and making her gasp in surprise."
    the_girl "Did you just... Cum?"
    mc.name "Yeah."
    if report_log.get("girl orgasms", 0) > 0:
        the_girl "That's only fair I suppose."
    else:
        the_girl "Aww, I thought I was going to get there first. Oh well."

    if the_girl.wants_creampie() or the_girl.has_cum_fetish():
        the_girl "Maybe next time we'll find somewhere else for you to do that."
        if the_girl.get_opinion_score("drinking cum") > 0:
            "[the_girl.title] winks at you as she licks her lips."
        elif the_girl.get_opinion_score("cum facials") > 0:
            "[the_girl.title] strokes her cheek and pouts at you."
        elif the_girl.get_opinion_score("being covered in cum") > 0:
            if the_girl.outfit.tits_available():
                "[the_girl.title] strokes her bare chest with her hand."
            else:
                "[the_girl.title] strokes her neck."
        else:
            "[the_girl.title] winks at you and pouts slightly."

    if the_girl.get_opinion_score("being fingered") < 0:
        the_girl "Now, you've cum, can we do something else?"
        "[the_girl.title] gently pulls your hand up from her [the_girl.pubes_description] pussy."
        if the_girl.sluttiness >= 60:
            "She brings your hand up to her mouth. She slides your fingers, fresh from her cunt, into her mouth."
            "Her tongue wraps around them as she sucks gently on your fingers. She works her hips, grinding her ass against you."
        else:
            "She moans and works her hips back against you, grinding her ass against you."
    elif the_girl.get_opinion_score("being fingered") > 0 or report_log.get("girl orgasms", 0) > 0:
        the_girl "Now, what is it that you were doing?"
        "[the_girl.title] gently holds your arm in place with your hand at her pussy."
        the_girl "You are so good at this."
    else:
        the_girl "Don't forget what you were doing."
    return
