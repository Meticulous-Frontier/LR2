init 5 python:
    config.label_overrides["flirt_person"] = "flirt_person_enhanced"


label flirt_person_enhanced(the_person): #Tier 1. Raises a character's sluttiness up to a low cap while also raising their love by less than a compliment.
    $ mc.change_energy(-15)
    if the_person.has_role(girlfriend_role):
        mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
        $ the_person.call_dialogue("flirt_response_girlfriend")

    elif the_person.has_role(affair_role):
        mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
        $ the_person.call_dialogue("flirt_response_affair")

    elif the_person.love <= 20:
        #Low Love
        if the_person.outfit.get_full_outfit_slut_score() > 30:
            mc.name "[the_person.title], you're looking nice today. That outfit looks good on you."
        elif the_person.happiness > 120:
            mc.name "[the_person.title], I really like your smile today, it fits with your outfit."
        else:
            mc.name "[the_person.title], are you wearing a new outfit today?"

        $ the_person.call_dialogue("flirt_response_low")

    elif the_person.love <= 40 or the_person.get_opinion_score("kissing") < -1: #20 to 40 or hates kissing
        # Mid Love
        if the_person.outfit.shows_off_her_ass():
            mc.name "You're looking hot today [the_person.title]. That outfit really shows off your cute butt."
        elif the_person.outfit.shows_off_her_tits():
            mc.name "You're looking tasty today [the_person.title]. That outfit really shows off your [the_person.tits_description]."
        else:
            mc.name "You're looking cute today [the_person.title]. That outfit really shows off your body."
        $ the_person.call_dialogue("flirt_response_mid")

    else:
        # High Love
        if the_person.outfit.get_full_outfit_slut_score() > 50:
            if the_person.outfit.shows_off_her_tits():
                mc.name "[the_person.title], your outfit is really showing off your [the_person.tits_description]. What are my chances of getting you out of it?"
            elif the_person.outfit.shows_off_her_ass():
                mc.name "[the_person.title], your outfit is really showing off your perky bottom. What are my chances of getting you out of it?"
            else:
                mc.name "[the_person.title], your outfit is driving me crazy. What are my chances of getting you out of it?"
        elif the_person.outfit.get_underwear_slut_score() > 25:
            if the_person.outfit.shows_off_her_tits():
                mc.name "[the_person.title], any chance you are going to let me play with those [the_person.tits_description]?"
            elif the_person.outfit.shows_off_her_ass():
                mc.name "[the_person.title], any chance you are going to let me spank that beautiful butt?"
            else:
                mc.name "[the_person.title], any chance you are going to show me what you are wearing underneath your clothing?"
        else:
            mc.name "[the_person.title], you are looking good today. Any chance for me to see you naked any time soon?"

        $ the_person.call_dialogue("flirt_response_high")


    python:
        mc.listener_system.fire_event("player_flirt", the_person = the_person)
        change_amount = 1 + the_person.get_opinion_score("flirting")
        if change_amount <= 0:
            change_amount = 1

        the_person.change_stats(happiness = the_person.get_opinion_score("flirting"), arousal = change_amount, slut = change_amount, max_slut = 20, love = 1, max_love = 25)
        the_person.discover_opinion("flirting")
        the_person.apply_serum_study()
    return
