#Requirement Functions
init 1 python:
    def cum_fetish_myra_intro_requirement():
        pass
        return False

    def exhibition_fetish_myra_intro_requirement():
        pass
        return False

    def breeding_fetish_myra_intro_requirement():
        pass
        return False

    def anal_fetish_myra_intro_requirement():
        pass
        return False


#Actions
init 2 python:
    cum_fetish_myra_intro = Fetish_Action("Myra Cum Fetish Intro", cum_fetish_myra_intro_requirement, "cum_fetish_myra_intro_label", fetish_type = "cum")
    exhibition_fetish_myra_intro = Fetish_Action("Myra Exhibitionism Fetish Intro", exhibition_fetish_myra_intro_requirement, "exhibition_fetish_myra_intro_label", fetish_type = "exhibition")
    breeding_fetish_myra_intro = Fetish_Action("Myra Breeding Fetish Intro", breeding_fetish_myra_intro_requirement, "breeding_fetish_myra_intro_label", fetish_type = "breeding")
    anal_fetish_myra_intro = Fetish_Action("Myra Anal Fetish Intro", anal_fetish_myra_intro_requirement, "anal_fetish_myra_intro_label", fetish_type = "anal")

label cum_fetish_myra_intro_label():
    $ the_person = myra

    $ add_cum_fetish(the_person)
    return

label exhibition_fetish_myra_intro_label():
    $ the_person = myra
    return


label breeding_fetish_myra_intro_label(the_person):
    $ the_person = myra
    $ the_person.arousal = 40
    "As you walk into [mc.location.name], you notice [the_person.title]. She notices you also and approaches."
    $ the_person.draw_person()
    the_person "Hello [the_person.mc_title]! I'm glad to see you!"
    if the_person.tits_visible():
        "You take a moment to look at her. Her cheeks are flushed, and her exposed nipples look hard as diamond. She is definitely aroused."
    else:
        "You take a moment to look at her. Her cheeks seem flushed... Her nipples are poking against the fabric of her outfit. Is she... Aroused?"
    mc.name "It's good to see you also."
    the_person "Hey, do you think you could help me with something? I have something I need help with that only you can help me with!"
    mc.name "I suppose."
    $ the_person.draw_person(position = "walking_away")
    "You follow [the_person.possessive_title] back to the adults only section of the gaming cafe. You notice her swinging her hips a bit more than usual as you follow her."
    "She stops at one of the computers."
    $ the_person.draw_person()
    the_person "I want to show you something really quick... can I sit on your lap?"
    mc.name "Sure."
    "You sit down at the computer and [the_person.possessive_title] sits on your lap. She sits all the way back, with her ass against your crotch. She wiggles her ass a bit as she pulls up a website."
    the_person "I found this game recently, and I can't stop playing it..."
    "The game screen loads up. The title screen displays proudly: 'Breeding Simulator'"
    "She loads up her save game. When it loads you see her character, a very pregnant woman."
    the_person "God, isn't she beautiful?"
    if the_person.pregnancy_is_visible():
        the_person "Being pregnant is so amazing, all the changes your body goes through..."
    elif the_person.knows_pregnant():
        the_person "I can't wait to look like that... god it looks amazing..."
    else:
        the_person "I want to get knocked up so bad. It looks so amazing..."
    "[the_person.title]'s ass is starting to wiggle back and forth against your crotch. It feels good..."
    the_person "For some reason my hormones have been going crazy lately! It seems like just about the only thing I can think about, getting you to fuck me and cum inside me and knock me up!"
    "You look down and realize that with one hand she has started touching herself."
    


    $ add_breeding_fetish(the_person)
    return

label anal_fetish_myra_intro_label():
    $ the_person = myra

    $ add_anal_fetish(the_person)
    return
