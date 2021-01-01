init 1 python:
    #Requirement functions

    def anal_fetish_employee_intro_requirement():
        return False

    def anal_fetish_family_intro_requirement():
        return False

    def anal_fetish_generic_intro_requirement():
        return False

    def anal_fetish_mom_intro_requirement():
        return False

    def anal_fetish_lily_intro_requirement():
        return False

    def anal_fetish_rebecca_intro_requirement():
        return False

    def anal_fetish_gabrielle_intro_requirement():
        return False

    def anal_fetish_stephanie_intro_requirement():
        return False

    def anal_fetish_alex_intro_requirement():
        return False

    def anal_fetish_nora_intro_requirement():
        return False

    def anal_fetish_emily_intro_requirement():
        return False

    def anal_fetish_christina_intro_requirement():
        return False

    def anal_fetish_starbuck_intro_requirement():
        return False

    def anal_fetish_sarah_intro_requirement():
        return False

    def anal_fetish_ophelia_intro_requirement():
        return False

    def anal_fetish_candace_intro_requirement():
        return False

    def anal_fetish_dawn_intro_requirement():
        return False

    def anal_fetish_erica_intro_requirement():
        return False

    def anal_fetish_ashley_intro_requirement():
        return False

init 2 python: #Other anal fetish related python code





### Function labels

label anal_fetish_employee_intro_label():
    "You are just finishing up with business for the day. As you are closing up your workstation, something is bothering you."
    "You couldn't help but notice one of your employees, [the_person.title], has been acting a little bit... different."
    "She seems to be using her ass to try and get attention."
    "Even now, as you walk around he business in your closing rounds, [the_person.possessive_title] bends over her desk when she notices you are nearby."

    $ the_person.draw_person(position = "standing_doggy")
    "She tries to pretend like she doesn't notice you, but you notice subtle shifts in her hips, wiggling a bit as you walk by her."
    "[the_person.possessive_title] has been doses recently with some of your anal enhancing serums. You wonder if she is ready to awaken a new love of anal sex."
    menu:
        "Attempt to train her anal fetish" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
        "Too risky, leave her alone":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            $ fetish_after_hours_unlock()
            $ clear_scene()
            return
    mc.name "Hello [the_person.title]."
    the_person.char "Hey [the_person.mc_title]! Its good to see you!"
    $ the_person.draw_person(position = the_person.idle_pose)
    "She quickly stands up and turns to you. You take a deep breath. Its time to take the plunge."
    mc.name "[the_person.title], are busy today? I have something I could use your help with after we close up."
    the_person "Oh! I suppose I could stay for a bit. Let me just finish this up. Want to meet in your office?"
    "It's clear from the tone of her voice she's hoping for some personal attention."
    mc.name "That sounds perfect. See you there."
    $ clear_scene()
    $ ceo_office.show_background()
    "You head to your office and wait a few minutes. Shortly after you hear a knock at the door."
    $ the_person.draw_person()
    ###Draw the girl###
    mc.name "Come in. Please have a seat."
    $ the_person.draw_person(position = "sitting")
    "As she sits down, she starts to fidgit a bit."
    mc.name "First off, I want you to know that you aren't in trouble. That isn't why I asked you here."
    the_person "Okay..."
    mc.name "I've noticed you've been acting a bit different lately whenever I am around. Bending over, wiggling your hips at me."
    the_person "I... sir its not..."
    if the_person.has_taboo("anal_sex"):
        mc.name "I was wondering if you've ever tried anal before. It's clear that it is something that is on your mind."
    else:
        mc.name "I was wondering if you want a round of anal. It is clear to me that your ass needs some attention."
    "[the_person.title] laughs a little."
    the_person "Oh! I umm... I suppose I would be up for something like that."
    "You stand up and start to walk around the desk toward [the_person.possessive_title]."
    mc.name "You aren't fooling anyone [the_person.title]. Your body langage is practically begging for it."
    mc.name "Now get up and bend over the desk so I can get a good look."
    the_person "Oh my god..."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.vagina_available():
        "You give her ass a smack, admiring the way her cheeks wobble."
    else:
        mc.name "Let's get this out of the way first."
        $ the_person.strip_outfit(exclude_upper = True)
        "Once you've got her clothing out of the way, you give her ass a smack, admiring the way her cheeks wobble."
    $ the_person.change_arousal(15)
    the_person "Mmm... like the view?"
    mc.name "I love it."
    "[the_person.title] moans as you firmly knead her ass for a bit."
    $ the_person.change_arousal(15)
    "You slide your fingers down betwee her cheeks and find her cunt just starting to leak a bit of moisture."
    mc.name "Wow, you really like this kind of attention don't you."
    "[the_perosn.possessive_title] can only moan as you slide two fingers inside her cunt. With your other hand you give her another spank."
    $ the_person.change_arousal(10)
    mc.name "There, that should be good."
    "You remove yor fingers briefly, then bring them up slightly "


    
    menu:
        "Accept":
            mc.name "I suppose I could stay for a bit, let me just finish up a couple things and I'll be right with you."
            the_person.char "Oh! Thanks [the_person.mc_title], I'll be right back! You won't regret this!"
            $ the_person.draw_person(position = "walking_away")
            "You finish up what you were doing and say goodbye to your employees. You are just starting to wonder what [the_person.possessive_title] needs when she comes back into the room."
            $ the_person.apply_outfit(SB_anal_outfit)
            $ the_person.draw_person()
            "[the_person.possessive_title] has changed into some very nice lingerie. You notice as she walks up that she isn't wearing any panties..."
            "She walks up and stands next to you by your desk."
            the_person.char "So, [the_person.mc_title], I don't know why but... I decided recently I really want to try and get better at anal..."
            "You aren't surprised, it's been a while since you started giving her the serum for increased anal enjoyment."
            the_person.char "I went over to the sex shop and bought a new toy... I've been wearing it for a few days now... and I was wondering what you thought?"
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.possessive_title] turns and bends over in front of you, with her hands on your desk."
            "You can see, nestled between her curvaceous ass cheeks, a matching pink jewel on the base of a butt plug."
            the_person.char "I think I'm ready for something a bit more... substantial... don't you think?"
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.get_opinion_score("anal sex") * 10)
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title] tries to push back against you and begins to beg."
            the_person.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
            $ the_person.break_taboo("anal_sex")
            ###Anal Scene, standing variant###
            call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True) from _call_fuck_person_SBA10
            #$ the_person.SB_fetish = "anal sex"
            $ the_person.max_opinion_score("anal sex")
            $ the_person.max_opinion_score("anal creampies")
            "[the_person.possessive_title] takes a few minutes to recover, then turns to you."
            $ the_person.draw_person()
            the_person.char "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately... I just can't stop thinking about you bending me over..."
            "[the_person.possessive_title] blushes and pauses..."
            mc.name "...And doing what, [the_person.title]?"
            "You tease her."
            the_person.char "I can't stop thinking about how full it feels... it feels so right when you push into my ass. It gets me so hot imagining it..."
            "She's been under the influence of your serums for a while now... you wonder if she's developed an anal fetish..."
            $ the_person.add_role(anal_fetish_role)
            $ the_person.update_sex_skill("Anal", 6)
            $ the_person.event_triggers_dict["LastAnalFetish"] = day
            $ add_fuck_doll_collar_to_base_outfit(the_person)
            "[the_person.possessive_title] gets her butt plug. She slowly pushes it back into her ass."
            the_person.char "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            $ the_person.draw_person(position = "walking_away")
            "You wave goodbye to [the_person.possessive_title] and get ready to head home for the night."
        "Refuse":
            the_person.char "I'm sorry to hear that..." #TODO finish this
            $ the_person.change_stats(happiness = -10, obedience = -10)
            "[the_person.possessive_title] quickly sulks off."
        "Too Tired" if mc.energy < 30:     # not enough energy for the player to induce fetish
            "[the_person.possessive_title] is surprised by your answer."
            $ the_person.change_stats(happiness = -5, obedience = -5)
            the_person.char "Oh! I'm sorry... I didn't think about that. Maybe tomorrow then?"
            "[the_person.possessive_title] quickly sulks off."
    $ fetish_after_hours_unlock()
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return

label anal_fetish_family_intro_label():
    return False

label anal_fetish_generic_intro_label():
    return False

label anal_fetish_mom_intro_label():
    return False

label anal_fetish_lily_intro_label():
    return False

label anal_fetish_rebecca_intro_label():
    return False

label anal_fetish_gabrielle_intro_label():
    return False

label anal_fetish_stephanie_intro_label():
    return False

label anal_fetish_alex_intro_label():
    return False

label anal_fetish_nora_intro_label():
    return False

label anal_fetish_emily_intro_label():
    return False

label anal_fetish_christina_intro_label():
    return False

label anal_fetish_starbuck_intro_label():
    return False

label anal_fetish_sarah_intro_label():
    return False

label anal_fetish_ophelia_intro_label():
    return False

label anal_fetish_candace_intro_label():
    return False

label anal_fetish_dawn_intro_label():
    return False

label anal_fetish_erica_intro_label():
    return False

label anal_fetish_ashley_intro_label():
    return False
