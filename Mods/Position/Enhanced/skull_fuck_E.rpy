# Enhanced version of skull fuck orgasm by BadRabbit

init 5 python:
    config.label_overrides["orgasm_skull_fuck"] = "orgasm_skull_fuck_enhanced"

label orgasm_skull_fuck_enhanced(the_girl, the_location, the_object):
    $ skull_fuck.current_modifier = "blowjob"
    $ skull_fuck.redraw_scene(the_girl)
    "You're happily fucking [the_girl.possessive_title]'s warm, wet throat when you notice her closer her eyes."
    "Her thighs quiver and her hands drop instinctively to her crotch. She begins to rub her pussy furiously, driving herself to orgasm."
    mc.name "Cum for me you dirty slut!"
    if the_girl.sex_skills["Oral"] > 3:
        "[the_girl.possessive_title] keeps her mouth wide open for you, even as she twitches and writhes through her climax."
        "You fuck her tight throat until she finishes twitching."
    else:
        "[the_girl.possessive_title] gags on your cock as you push her down onto it."
        "Her body tightens up as she climaxes, and you make sure to take advantage of her tight throat by fucking it hard."

    if the_girl.get_opinion_score("being submissive") > 0:
        if the_girl.sluttiness > the_girl.core_sluttiness and the_girl.core_sluttiness < skull_fuck.slut_cap:
            $ the_girl.change_slut_core(the_girl.get_opinion_score("being submissive")) #If she likes being submissive this makes her cum and become sluttier super hard.

        $ the_girl.change_obedience(2*the_girl.get_opinion_score("being submissive"))
        if the_girl.outfit.vagina_visible():
            "You can see that [the_girl.title]'s pussy is dripping wet as she cums."
        else:
            $ top_piece = the_girl.outfit.get_lower_top_layer()
            if top_piece.underwear:
                "[the_girl.title]'s dripping wet pussy has managed to soak through her underwear, leaving a wet mark on her [top_piece.display_name]."
            else:
                "[the_girl.title] clenches her thighs together and rides out her orgasm."
            $ top_piece = None
        $ skull_fuck.current_modifier = None
        $ skull_fuck.redraw_scene(the_girl)

    else:
        $ skull_fuck.current_modifier = None
        $ skull_fuck.redraw_scene(the_girl)
        $ the_girl.change_obedience(1)
        $ the_girl.change_happiness(-2)

    "Watching [the_girl.title]'s body writhe as she climaxes from your cock encourages you to go faster."
    "You clamp down on her head and slam yourself in and out of her throat."
    return
