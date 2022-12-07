# Stephanie story add ons.
init 5 python:
    add_label_hijack("normal_start", "activate_head_researcher_role_enhancement")
    add_label_hijack("after_load", "activate_head_researcher_role_enhancement")

label activate_head_researcher_role_enhancement(stack):
    python:
        head_researcher.add_action(head_researcher_serum_trait_test)
        if not mc.business.event_triggers_dict.get("testing_room_policy_avail",0) == 1:
            mc.business.add_mandatory_crisis(head_researcher_suggest_testing_room)
        execute_hijack_call(stack)
    return

init 1400 python:
    def testing_room_creation_requirement():
        if mc.business.event_triggers_dict.get("testing_room_policy_avail",0) == 1:
            return True
        return "Story Progression"

    def testing_room_policy_unlock(unlock):
        mc.business.event_triggers_dict["testing_room_policy_unlock"] = unlock

    testing_room_creation_policy = Policy(name = "Serum Testing Room",
        desc = "Some medical equipment, a couple windows, and a privacy curtain creates an ideal place to test specific serum traits.",
        cost = 1000,
        requirement =  testing_room_creation_requirement,
        on_buy_function = testing_room_policy_unlock,
        extra_arguments = { "unlock" : 1})
    serum_policies_list.insert(9, testing_room_creation_policy)

    def head_researcher_cure_discovery_disease_name():
        if mc.business.event_triggers_dict.get("head_researcher_cure_disease_name", None) != None:
            return mc.business.event_triggers_dict.get("head_researcher_cure_disease_name", None)
        if mc.business.research_tier == 0:
            return "Rabies"
        elif mc.business.research_tier == 1:
            return "Dengue fever"
        elif mc.business.research_tier == 2:
            return "Crohn's disease"
        else:
            return "Parkinson's disease"

    def head_researcher_cure_get_market_contact():
        contact = get_random_from_list(mc.business.market_team)
        return contact

    def determine_test_serum_flags(the_serum_trait):
        slutty_serum = 0 #positive if it increases, negative if it decreases.
        happy_serum = 0
        arousal_serum = 0
        love_serum = 0
        obedience_serum = 0
        work_serum = 0
        sex_skill_serum = 0
        energy_serum = 0
        suggest_serum = 0

        test_person = create_random_person()
        test_person.serum_tolerance = 5
        test_person.energy = 50
        test_person.arousal = 20


        start_happinesss = test_person.happiness
        start_sluttiness = test_person.effective_sluttiness()
        start_max_arousal = test_person.max_arousal
        start_arousal = test_person.arousal
        start_love = test_person.love
        start_obedience = test_person.obedience
        start_work = test_person.calculate_base_salary()
        start_sex_skill = test_person.sex_skills["Foreplay"] + test_person.sex_skills["Oral"] + test_person.sex_skills["Vaginal"] + test_person.sex_skills["Anal"]
        start_energy = test_person.energy
        start_suggest = test_person.suggestibility

        test_person.give_serum(the_serum_trait.build_test_serum(), add_to_log = False)

        energy_serum = test_person.energy - start_energy
        arousal_serum = test_person.arousal - start_arousal
        happy_serum = test_person.happiness - start_happinesss
        slutty_serum = test_person.sluttiness - start_sluttiness
        love_serum = test_person.love - start_love
        obedience_serum = test_person.obedience - start_obedience
        work_serum = test_person.calculate_base_salary() - start_work
        sex_skill_serum = (test_person.sex_skills["Foreplay"] + test_person.sex_skills["Oral"] + test_person.sex_skills["Vaginal"] + test_person.sex_skills["Anal"]) - start_sex_skill
        suggest_serum = test_person.suggestibility - start_suggest

        test_person.run_turn()
        if slutty_serum == 0:
            slutty_serum = test_person.sluttiness - start_sluttiness
        if happy_serum == 0:
            happy_serum = test_person.happiness - start_happinesss
        if love_serum == 0:
            love_serum = test_person.love - start_love
        if obedience_serum == 0:
            obedience_serum = test_person.obedience - start_obedience



        return ([slutty_serum,
            happy_serum,
            arousal_serum,
            love_serum,
            obedience_serum,
            work_serum,
            sex_skill_serum,
            energy_serum,
            suggest_serum])

#Requirement Functions
init -1 python:
    def head_researcher_suggest_testing_room_requirement():
        if mc.business.research_tier >= 1:
            if mc.business.days_since_event("tier_1_serum_unlock_day") > TIER_2_TIME_DELAY:
                if mc.is_at_work() and mc.business.is_open_for_business():
                    return True
        return False

    def head_researcher_testing_room_intro_requirement(the_person):
        if testing_room_creation_policy.is_active():
            if mc.is_at_work() and mc.business.is_open_for_business():
                return True
        return False

    def head_researcher_serum_trait_test_requirement(the_person):
        if testing_room_creation_policy.is_active():
            if mc.business.days_since_event("serum_trait_test") > TIER_1_TIME_DELAY:
                return True
            else:
                return "Tested serum too recently"
        return False

    def head_researcher_strip_tease_requirement(the_person):
        if the_person.obedience >= 140:
            if the_person.days_since_event("obedience_event") >= TIER_2_TIME_DELAY:
                if mc.is_at_work() and mc.business.is_open_for_business():
                    return True
        return False

    def head_researcher_cure_discovery_intro_requirement():
        if mc.business.is_open_for_business() and mc.business.head_researcher != None: #Only trigger if people are in the office.
            if mc.business.head_researcher.days_since_event("obedience_event") >= TIER_2_TIME_DELAY and mc.business.head_researcher.obedience >= 160:
                return True
        return False

    def head_researcher_cure_discovery_market_patent_requirement(the_person):
        if mc.business.is_open_for_business():
            if the_person.is_at_work():
                return True #Only while she is at work
        return False

    def head_researcher_cure_discovery_patent_sold_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.head_researcher != None:
            if mc.business.head_researcher.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def head_researcher_cure_discovery_patent_kept_requirement():
        if mc.business.is_open_for_business() and mc.business.head_researcher != None:
            if mc.business.head_researcher.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def head_researcher_cure_finish_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.head_researcher != None:
            return True
        return False

#Action definitions
    head_researcher_suggest_testing_room = Action("Testing room reuqest", head_researcher_suggest_testing_room_requirement, "head_researcher_suggest_testing_room_label")
    head_researcher_testing_room_intro = Action("Testing Room Intro", head_researcher_testing_room_intro_requirement, "head_researcher_testing_room_intro_label")
    head_researcher_serum_trait_test = Action("Test a Serum Trait", head_researcher_serum_trait_test_requirement, "head_researcher_serum_trait_test_label",
        menu_tooltip = "Perform intensive serum trait test with the help of your head researcher on an employee.")
    head_researcher_strip_tease = Action("Head Researcher Strip Tease", head_researcher_strip_tease_requirement, "head_researcher_strip_tease_label")
    head_researcher_cure_discovery_intro = Action("Begin Cure Discovery Quest", head_researcher_cure_discovery_intro_requirement, "head_researcher_cure_discovery_intro_label")
    head_researcher_cure_discovery_market_patent = Action("Attempt to sell patent", head_researcher_cure_discovery_market_patent_requirement, "head_researcher_cure_discovery_market_patent_label")
    head_researcher_cure_discovery_patent_sold = Action("Patent Sold", head_researcher_cure_discovery_patent_sold_requirement, "head_researcher_cure_discovery_patent_sold_label")
    head_researcher_cure_discovery_patent_kept = Action("Patent Stolen", head_researcher_cure_discovery_patent_kept_requirement, "head_researcher_cure_discovery_patent_kept_label")
    head_researcher_cure_finish = Action("Cure Reward", head_researcher_cure_finish_requirement, "head_researcher_cure_finish_label")

label head_researcher_suggest_testing_room_label():
    if mc.business.event_triggers_dict.get("testing_room_policy_avail",0) == 1: #We've already run this event.
        return
    $ the_person = mc.business.head_researcher
    if mc.location == mc.business.r_div:
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! Can you meet me down in the lab?"
        mc.name "Sure"
        $ mc.end_text_convo()
        "You walk down to the lab."
        $ mc.change_location(mc.business.r_div)
        $ mc.location.show_background()
    $ the_person.draw_person()
    the_person "Hey! Thanks for coming. I wanted to show you something really quick."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and starts to walk to the far end of the lab. You follow her."
    "When she gets there, she opens a side door and goes down a short hallway, and at the end is a small room, with another small room adjacent room."
    "The two rooms are currently sitting completely unused."
    $ the_person.draw_person()
    the_person "I was thinking about what you said, about testing for changes based on orgasms and interactions with our serums."
    the_person "But the problem is... we don't really have a good place to run the tests at. The lab is great, but it is so open."
    the_person "It might make things uncomfortable and skew results."
    mc.name "You're right."
    the_person "Anyway, I found these two old rooms, that I thought would make a good serum testing site. We could set up a medical exam bed here, and install a window between the two rooms."
    the_person "That way we can research serum effects in a more clinical environment."
    mc.name "That's a great idea. How much would it run?"
    the_person "I priced out some basic medical equipment. A bed, some monitors, etc. I think it could be done for about $1000."
    mc.name "That seems pretty reasonable."
    the_person "Yeah, then we could bring employees here to help test serums once in a while. It would be very handy for newly created traits specifically."
    if mandatory_paid_serum_testing_policy.is_active():
        the_person "With the mandatory testing policy, we'd be able to test it on just about anyone, really."
    else:
        the_person "You might want to consider some type of mandatory testing policy though... for now we would just need to rely on volunteers."
    mc.name "This is a good idea. I'll add it to the to do list, though I can't promise when I'll get around to arranging it."
    the_person "Okay! Thanks for hearing me out."
    $ clear_scene()
    "[the_person.possessive_title] leaves you alone in the small room. A policy has been added to create a designated serum testing room."
    "Once unlocked, you will be able to test and observe the results of serum traits there with your head researcher."
    $ mc.business.event_triggers_dict["testing_room_policy_avail"] = 1
    $ the_person.add_unique_on_room_enter_event(head_researcher_testing_room_intro)
    return

label head_researcher_strip_tease_label(the_person):    #140 obedience event
    $ the_person.set_event_day("obedience_event", override = True)
    "You step into the research and development department. There is something on the edge of your mind but you just can't put your finger on it."
    "Something strange is going on. You feel tired. Uninspired. There is no passion in your work."
    $ the_person.draw_person(position = "sitting")
    "You look across the room and see [the_person.title], your head researcher."
    "You have a bit of a realization. You do your best work when you have your moments of post orgasm clarity."
    "The best orgasms give you the best moments of clarity. And for the best orgasms, there needs to be a building effect."
    "As great as it would be to order an employee on her knees to suck you off, you want more than just that."
    "The thrill of a tease... slowly building."
    if the_person.tits_available():
        if the_person.vagina_available():
            mc.name "Hey [the_person.title]."
            the_person "Yes?"
            mc.name "Bend over your desk. I want to see that nice ass of yours."
        else:
            mc.name "Hey [the_person.title]."
            the_person "Yes?"
            mc.name "Take off your bottoms and bend over your desk. I want to see that nice ass of yours."
            the_person "Wow... okay..."
    else:
        mc.name "Hey [the_person.title]."
        the_person "Yes?"
        mc.name "Strip naked and bend over your desk. I want to see that hot little body of yours."
        the_person "Wow... right now?"
        mc.name "Yes now."
    "She is a bit shocked at your demand, but obediently complies."
    $ the_person.strip_full_outfit(position = "standing_doggy")
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "You walk over and sit down at her desk, her ass is right in your face. She looks around the room a bit nervously."
    if the_person.location.get_person_count() >1:
        "She is a bit embarassed, and your other employees in the area are watching to see what happens."
    else:
        "However, the room is empty. Just the two of you are here, for now."
    mc.name "Damn, your ass is amazing. You know that right?"
    if the_person.sluttiness > 40:
        the_person "It doesn't FEEL amazing. But you could probably do something about that if you wanted..."
    else:
        the_person "I guess, are you... about done?"
        mc.name "About done? With what?"
        the_person "Err, I don't know..."
    "You give her ass a playful smack. You enjoy the way her ass jiggles in waves, spreading out from the point of contact."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(10)
    the_person "Mmmf... sir?"
    mc.name "Shh, I just want to enjoy the view for a few minutes, okay?"
    mc.name "You just keep working."
    call employee_lust_build_loop_label(the_person) from _head_researcher_lust_build_unlock_01

    $ blowjob_finish = False
    if get_lust_tier() >= 4 or (get_lust_tier() * 2 > mc.focus):
        $ blowjob_finish = True
    else:
        "You feel reinvigorated, after playing with [the_person.title]. You consider for a moment... should you have her suck you off to finish?"
        menu:
            "Order her to blow you":
                $ blowjob_finish = True
            "Let her go":
                mc.name "Alright, that's enough. Thank you [the_person.title], I appreciate your cooperation."
                the_person "Is that all you wanted? Okay [the_person.mc_title]..."
    if blowjob_finish:
        "You can't take the teasing anymore. It is time for [the_person.title] to finish you off."
        mc.name "Alright that's enough. Time to put your mouth to use. I want to finish now."
        the_person "Yes [the_person.mc_title]."
        $ the_person.draw_person(position = "blowjob")
        "She immediately opens her mouth and takes your length in her mouth. After all the teasing, her soft lips descending on your shaft feels heavenly."
        "[the_person.possessive_title] bobs her head up and down your cock, obediently sucking your cock. After all the teasing, you quickly get ready to cum."
        "You put your hand on the back of her head."
        mc.name "Get ready, I want to cum in your mouth... here it comes!"
        "With a moan you explode, your cock starts to dump its load in her eager mouth."
        $ the_person.cum_in_mouth()
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
        $ the_person.draw_person(position = "blowjob")
        "[the_person.title] doesn't say a word, but finishes milking the last few drops of your cum from your dick, then looks up at you."
        mc.name "That's it. Show me what a good girl your are."
        "[the_person.possessive_title] opens her mouth, your load drips down the sides of her mouth a bit and pooled up in the middle of her tongue."
        mc.name "Good girl. Now swallow."
        "She closes her mouth, then gulps loudly. She licks her lips a couple times, then opens her mouth to show you it is now empty."
        mc.name "Fuck, that was perfect. Thank you [the_person.title]. I really needed that."
        $ the_person.change_obedience(2)
        $ the_person.change_slut(1, 60)
        the_person "Of course. Glad to do it for you, [the_person.mc_title]."
    "You get up and leave [the_person.possessive_title] at her desk."
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    "As you step away, you think about how hot it was, having your head researcher obediently bent over her desk for your viewing pleasure."
    "You bet that your other employees would be willing to do the same thing... the obedient ones anyway."
    "You can now order an employee to bend over her desk and present her ass to you, if she is obedient enough."
    "The more obedient she is, the farther you can take things with her."
    $ mc.business.event_triggers_dict["employee_over_desk_unlock"] = True
    $ mc.business.add_mandatory_crisis(head_researcher_cure_discovery_intro)
    return

label head_researcher_cure_discovery_intro_label():
    $ the_person = mc.business.head_researcher
    $ the_disease = head_researcher_cure_discovery_disease_name()
    $ mc.business.event_triggers_dict["head_researcher_cure_disease_name"] = the_disease
    if the_person == None:
        return #Bad end
    if mc.location != rd_division:
        $ mc.start_text_convo(the_person)
        the_person "Hey, I need to see you in the lab ASAP!"
        mc.name "On my way!"
        $ mc.end_text_convo()
        "You quickly head to the lab."
        $ mc.change_location(rd_division)
        $ mc.location.show_background()
    $ the_person.set_event_day("obedience_event", override = True)
    $ the_person.draw_person()
    the_person "Hey! I need to talk to you about something."
    mc.name "What is it?"
    the_person "I was doing some research for a new serum trait. I was testing the effects on some rats in the lab, when I noticed something incredible."
    the_person "I had some rats that have [the_disease]. After giving them the serum, they showed no signs of the disease in less than 12 hours!"
    mc.name "That's... interesting?"
    the_person "I thought so too, so I ran a bunch more tests. In 99.8 percent of tests I ran, the disease appears to be completely cured!"
    mc.name "Is that something that could be adapted to humans?"
    the_person "This would be the first step in researching a cure! I already filed a patent for the business on the formula."
    mc.name "That's great... but could we realistically manufacture that here?"
    "She considers your question for a moment."
    the_person "Realistically... not really. Not in the numbers that would be needed to have it available to large numbers of people."
    mc.name "Hmm, that's a shame."
    the_person "Maybe you could... I don't know... sell the patent? To a larger pharmaceutical company? One that could make it in the quantity needed to meet worldwide demand?"
    mc.name "That's an interesting idea..."
    menu:
        "Keep the secret for your company":
            mc.name "It might take us some time, but I think we could ramp up production here to meet demand."
            $ the_person.draw_person(emotion = "angry")
            the_person "But sir! That would take... months? Or more?"
            mc.name "So?"
            the_person "Think of all the people out there, suffering right now. Surely it would be better for us to just sell the rights?"
            mc.name "No, I don't think so."
            $ the_person.change_stats(obedience = -10, love = -10, happiness = -20)
            "She really doesn't like your answer. Hopefully you haven't burned any bridges?"
            "As you turn to leave, you can hear her muttering something."
            $ del the_disease
            $ mc.business.add_mandatory_crisis(head_researcher_cure_discovery_patent_kept)
            return
        "Convince me":
            mc.name "Some cash infusion to the company would be great. That's a great idea, [the_person.title]."
    $ the_target = head_researcher_cure_get_market_contact()
    the_person "Personally, I think you should talk to [the_target.name]. You know, over in marketing?"
    mc.name "Oh?"
    if the_target == alexia:
        the_person "She's a recent college graduate and seems to have a good handle on things over there. I bet she could manage it!"
        mc.name "Noted. I'm not sure I'll have time, but I'll talk to her when I can."
    elif the_target == lily or the_person == mom or the_person == cousin or the_person == aunt:
        the_person "Corporate espionage is huge, and a discovery like this could make big waves."
        the_person "You should probably ask someone you can trust to handle this, like someone from your family."
        mc.name "Good idea. I'll talk to her as soon as I can."
    else:
        the_person "Yeah, I think she actually has experience doing something similar at a previous job. I bet she could help out!"
        mc.name "Noted. I'm not sure I'll have the time, but I'll talk to her when I can."
    the_person "If I were you, I'd get on it, quick! Modern day drug research is extremely fast paced. No telling when another lab might replicate our findings..."
    mc.name "Thank you, [the_person.title], for your research and for bringing this to my attention."
    "So... you should talk to [the_target.possessive_title] about selling your patent rights to the cure for [the_disease]."

    python:
        the_target.add_unique_on_talk_event(head_researcher_cure_discovery_market_patent)
        del the_disease
        del the_target
    return

label head_researcher_cure_discovery_market_patent_label(the_person):
    $ the_person.draw_person()
    $ the_disease = head_researcher_cure_discovery_disease_name()
    mc.name "Hello [the_person.title], do you have a moment?"
    the_person "Of course. What can I do for you sir?"
    if the_person == alexia:
        mc.name "We made a big discovery in the research lab, but it is too big for our production department to handle. I was wondering if you could look into selling some patent rights."
        the_person "Oh? I think I could handle something like that. What is the patent for?"
        mc.name "Our research department made a discovery related to a possible treatment for [the_disease]."
    elif the_person == lily or the_person == mom or the_person == cousin or the_person == aunt:
        mc.name "We made a big discovery in the research lab, but it is too big for our production department to handle. I was wondering if you could look into selling some patent rights."
        the_person "Oh? Why... why would you ask me to do that?"
        mc.name "If word gets out that we made this discovery, we might be the target of some bad actors. I need someone I can trust to handle this. Someone from the family."
        the_person "Okay, what is the discovery?"
        mc.name "Our research department made a discovery related to a possible treatment for [the_disease]."
    else:
        mc.name "Well, I heard that you might have some prior experience working with drug patent rights..."
        the_person "Yes sir! At my last job, I worked for a pharmaceutical investment company, buying and selling patent rights to all kinds of different drugs."
        mc.name "Wow, well, that is actually very useful. You see, our research department made a discovery related to a possible treatment for [the_disease]."
    the_person "Oh wow! There's currently some preventative drugs for that, but no known cure."
    mc.name "I know. I wish we had the production and testing capabilities here to take it to market, but unfortunately, we just don't."
    the_person "Aahhh, I see. So you want me to test the waters and see what I can get for the patent rights to the discovery?"
    mc.name "That's exactly right."
    the_person "Okay! I can do that. Give me a couple of days and I'll see what I can find!"
    mc.name "Thank you, [the_person.title]."
    # $ head_researcher_cure_discovery().quest_event_dict["market_day"] = day
    $ del the_disease
    $ the_person.add_unique_on_room_enter_event(head_researcher_cure_discovery_patent_sold)
    return

label head_researcher_cure_discovery_patent_sold_label(the_person):
    $ the_disease = head_researcher_cure_discovery_disease_name()
    if the_person == None:
        return
    the_person "Hey there! I have some good news about that patent for [the_disease]."
    mc.name "Glad to hear it. What is the news?"
    if the_disease == "Rabies":
        the_person "Well, [the_disease] has very few cases annually, so the prospects of a lucrative deal for the patent rights were pretty slim."
        the_person "After negotiating, they were able to sell them for $1500. I hope that is okay."
        $ mc.business.change_funds(1500)
        mc.name "I understand. That is still very helpful. Thank you [the_person.title]."
    elif the_disease == "Dengue fever":
        the_person "Well, [the_disease] really only propagates in poor, tropical areas, due to the way it spreads."
        the_person "While the good this drug can do is great, the profit potential is pretty low. They were able to sell it for $3500. I hope that is okay."
        $ mc.business.change_funds(3500)
        mc.name "Thank you [the_person.title], I just hope the drug can be put to good use."
    elif the_disease == "Crohn's disease":
        the_person "[the_disease] is widespread in the developed world. However, because this treatment has only been shown effective in rats, the over all effectiveness is unknown."
        the_person "After negotiating, they were able to sell the patent for $15000. I hope that is okay."
        $ mc.business.change_funds(15000)
        mc.name "That is still a considerable sum. Thank you [the_person.title]."
    elif the_disease == "Parkinson's disease":
        the_person "[the_disease] is widespread in older populations. However, because this treatment has only been shown effective in rats, the over all effectiveness is unknown."
        the_person "After negotiating, they were able to sell the patent for $50000. I hope that is okay."
        $ mc.business.change_funds(50000)
        mc.name "That is a significant sum. Thank you [the_person.title]."
    else:
        the_person "Well, not much is actually known about [the_disease]. However, with the rapid effects from the compound, I was still able to sell it."
        the_person "After negotiating, I was able to sell the patent for $5000. I hope that is okay."
        $ mc.business.change_funds(5000)
        mc.name "Thank you [the_person.title], I just hope the drug can be put to good use."
    "The patent is sold! And you made a little extra money for the business."
    if mc.business.head_researcher:
        "You might want to check back with your head researcher and let her know the good news."
        $ mc.business.head_researcher.add_unique_on_talk_event(head_researcher_cure_finish)
    else:
        "Unfortunately, you no longer have a head researcher to share the good news with."
    $ del the_disease
    return

label head_researcher_cure_discovery_patent_kept_label():
    $ the_person = mc.business.head_researcher
    $ the_disease = head_researcher_cure_discovery().quest_event_dict.get("disease_name", "Rabies")
    "You get a notification on your phone and you check it. It's from the Red Cross?"
    "Red Cross""Thank you for donating your patent for [the_disease]!"
    "Red Cross""With this donation, we promise we will work to the best of our abilities to get this cure into the hands of everyone who needs it, worldwide."
    "Donated? What the hell? You didn't donate that!"
    if the_person == None:
        "Suddenly, you realize what must have happened. After clearing out her desk, the old head researcher must have donated the patent she discovered!"
        "Well, maybe you should have considered selling the patent. Either way, that business opportunity is now gone."
        $ del the_disease
        return
    else:
        "Suddenly, you realize what must have happened. [the_person.title], not happy with your intention to keep the patent, must have secretly donated the rights to it."
    "You call her up."
    $ the_person.set_event_day("obedience_event", override = True)
    the_person "Hello?"
    mc.name "Hey. So, I'm guessing you're the one I have to thank for the email I got this morning from the Red Cross?"
    "There is silence on the other end. You think you hear an expletive whispered."
    the_person "I'm not going to lie... yes, that was me. You have to understand! This could help a lot of people!"
    "She sounds very sincere. It's hard to be mad, and maybe this is something that really COULD help a lot of people."
    the_person "Please don't fire me, I love working here, but I just couldn't sit by while something that could help people..."
    mc.name "I'm not firing you, [the_person.title]."
    "She sounds relieved."
    the_person "Oh [the_person.mc_title], I knew you were a reasonable man! I'll make it up to you, I promise!"
    mc.name "Of course you are going to make it up to me. Get to my office, NOW."
    the_person "Yes sir!"
    $ ceo_office.show_background()
    $ the_person.draw_person()
    "You hear a knock. You look up and see [the_person.possessive_title]."
    the_person "You wanted to see me?"
    mc.name "Yes. Come in, and lock the door behind you."
    the_person "Oh my..."
    "[the_person.title] does as you ask. Her voice takes on a sultry tone."
    the_person "So, did you have something in mind? How can I make all of this up to you?"
    mc.name "I do, come around here and get on your knees."
    the_person "Oh god, yes [the_person.mc_title]."
    $ the_person.draw_person(position = "blowjob")
    "You pull your dick out of your pants and put it right on her face."
    mc.name "You know what to do."
    "You could let her just give you a blowjob, but if you push things a little rougher, it would really drive the point home, but her admiration for you would probably decrease."
    "[the_person.title] opens her mouth and takes the tip of your cock in her hot mouth. She gives you a few strokes as you rapidly harden in her mouth."
    call fuck_person(the_person, start_position = blowjob, start_object = mc.location.get_object_with_trait("Kneel"), skip_intro = True, position_locked = True, ignore_taboo = True) from _quest_cure_sex_path_05
    $ the_report = _return
    if skull_fuck in the_report.get("positions_used", []):  #You really roughed her up
        "[the_person.possessive_title] mascara is running from tears caused by being gagged when you roughly fucked her throat."
        mc.name "I know that this story had a happy ending, with the patent going to the Red Cross, but remember, this is my business. Don't do things behind my back again."
        $ the_person.change_stats(obedience = 10, love = -10, slut = 3, max_slut = 70)
        "Her voice is trembling as she responds."
        the_person "Yes... yes sir..."
    elif deepthroat in the_report.get("positions_used", []):  #She took it deep.
        "[the_person.possessive_title] is recovering from taking your cock deep down her throat."
        mc.name "I know this story had a happy ending, with the patent going to the Red Cross, but please don't do things behind my back like that again."
        $ the_person.change_stats(obedience = 5, slut = 2, max_slut = 70)
        the_person "Yes sir, it won't happen again!"
    else: #Just a BJ
        "[the_person.possessive_title] licks her lips, she seems to have enjoyed getting on her knees for you."
        mc.name "Thank you for doing the right thing, but please let me know before you take actions like that again."
        $ the_person.change_stats(love = 3, slut = 1, max_slut = 70)
        the_person "Yes sir."
    mc.name "That'll be all for now."
    $ the_person.draw_person(position = "walking_away")
    "Well, you may have missed a financial opportunity, but at least you got a blowjob out of it!"
    $ del the_disease
    return

label head_researcher_cure_finish_label(the_person):
    $ the_disease = head_researcher_cure_discovery_disease_name()
    the_person "Hello [the_person.mc_title]."
    mc.name "I have some good news. Remember that patent on a [the_disease] drug? It sold."
    the_person "Oh! That's great! Hopefully it will help a lot of people."
    mc.name "I think it will. I appreciate you making that patent when you did. You are exactly the type of person I need running this department."
    the_person "Thank you sir!"
    "She seems to really appreciate your praise."
    $ the_person.change_obedience(3)
    $ the_person.change_happiness(10)
    the_person "Is there anything else you need?"
    return
#Head researcher testing progression event

label head_researcher_testing_room_intro_label(the_person):
    "In this label, we go with the head researcher to the new serum testing room, where we introduce the idea of an intensive serum trait test."
    $ mc.business.set_event_day("serum_trait_test", override = True)
    $ the_person.add_unique_on_room_enter_event(head_researcher_strip_tease)
    $ the_person.set_event_day("obedience_event", override = True)
    return

label head_researcher_serum_trait_test_label(the_person):
    mc.name "There is a serum trait that I would like to study. Get a random volunteer and meet me in the study room."
    the_person "Okay."
    $ clear_scene()
    $ scene_manager = Scene()
    $ the_tester = get_random_from_list(mc.business.get_requirement_employee_list(obedience_required = 110, exclude_list = [the_person]))
    "You head down to the testing room. After a few minutes, [the_person.possessive_title] returns with today's test subject."
    $ scene_manager.add_actor(the_person, display_transform = character_left_flipped)
    $ scene_manager.add_actor(the_tester, display_transform = character_right)
    mc.name "Hello [the_tester.title]. Are you ready to begin the test?"
    call serum_research_tester_response_label(the_tester) from _research_serum_mastery_01
    "You sit down at the computer and select a serum to be tested."
    call serum_research_trait_selection_label() from _research_serum_mastery_02
    $ the_serum_trait = _return
    the_person "Got it. Let me grab the test sample for that."
    "[the_person.title] walks it over to [the_tester.possessive_title]."
    $ scene_manager.update_actor(the_person, display_transform = character_right, position = "walking_away")
    "She gives her the serum then steps back to her observation station."
    $ scene_manager.add_actor(the_person, display_transform = character_left_flipped, position = the_person.idle_pose)
    the_tester "Okay... here we go!"
    $ the_tester.give_serum(the_serum_trait.build_test_serum(), add_to_log = True)
    "She drinks the serum."
    mc.name "Alright, [the_person.title] is going to run a series of tests with you while we observe the effects."
    the_tester "Alright."
    "[the_person.possessive_title] begins her questions for [the_tester.possessive_title]."
    call serum_research_serum_results_label(the_person, the_tester, the_serum_trait) from _research_serum_master_03
    $ test_positive_flags = _return
    mc.name "Thank you, [the_person.title] and [the_tester.title]. I appreciate your cooperation."
    the_person "Of course. I'm going to file these results in the main lab."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title] steps out, leaving you alone with [the_tester.title] in the testing room."
    $ scene_manager.remove_actor(the_person)

    #Use this section to determine what extra curriculars we want to engage in.
    if ("love" in test_positive_flags and the_tester.love > 30) or the_tester.is_girlfriend():    #She asks MC on a date.
        the_tester "Well, honestly, it was nice just being able spend some time in here with you."
        the_tester "I was wondering... would you want to catch a movie sometime? It would nice to just hang out!"
        mc.name "You want to go on a date?"
        the_tester "Yeah, it could be fun! right? How about Tuesday?"
        if mc.business.event_triggers_dict.get("movie_date_scheduled", False):
            mc.name "I'm sorry, I've already got plans for that evening."
            the_tester "Ah, I see..."
        else:
            menu:
                "Accept Date":
                    mc.name "Sure, I can do Tuesday."
                    $ create_movie_date_action(the_tester)
                    the_tester "Great!"
                    $ the_tester.change_happiness(2)
                "Decline Date":
                    mc.name "I'm sorry, work keeps me too busy, most days I'm just exhausted."
                    the_tester "Ah, its okay. Don't worry about it."
    else:
        the_tester "Well, hopefully you got the data you needed. Can I get back to work?"
        mc.name "Yes. Thank you for you help, [the_tester.title]."
    $ scene_manager.clear_scene()
    "[the_tester.title] steps out of the room also. Your work here has increased your mastery of [the_serum_trait.name]!"
    $ mc.business.set_event_day("serum_trait_test", override = True)
    call advance_time from _call_advance_time_mastery_research_01
    return "Advance Time"

label serum_research_tester_response_label(the_tester):
    the_tester "Well... you're the boss, so I guess I don't have much of a choice then?"
    mc.name "Not really, no."
    the_tester "Let's get this over with then."
    return

label serum_research_trait_selection_label():
    "Note from the Author: I'm working on a screen for this. For now, please accept my apologies and select one of the following:"
    menu:
        "Low Concentration Sedatives":
            return find_serum_by_name("Low Concentration Sedatives")
        "Inhibition Suppression":
            return find_serum_by_name("Inhibition Suppression")
        "Love Potion":
            return find_serum_by_name("Love Potion")
        "Off Label Pharmaceuticals":
            return find_serum_by_name("Off Label Pharmaceuticals")
    return

label serum_research_serum_results_label(the_person, the_tester, the_serum_trait):
    $ serum_trait_result_list = determine_test_serum_flags(the_serum_trait)
    $ positive_flags = []
    $ negative_flags = []
    #The high notes
    the_person "Alright, I have some initial results from our quick study. First are the positive effects."
    if serum_trait_result_list[0] > 0:  #Slutty Serum
        $ positive_flags.append("slut")
        the_person "This serum definitely changes her sexual appetite."
    if serum_trait_result_list[1] > 0:  #Happy Serum
        $ positive_flags.append("happy")
        the_person "She seems to be happier and more satisfied with her life and work situation than at the start."
    if serum_trait_result_list[2] > 0:  #Arousal Serum
        $ positive_flags.append("arousal")
        the_person "She is showing subtle cues and body language associated with arousal."
    if serum_trait_result_list[3] > 0:  #Love Serum
        $ positive_flags.append("love")
        the_person "She actually seems to be showing a more favorable response to questions involving you."
    if serum_trait_result_list[4] > 0:  #obedience Serum
        $ positive_flags.append("obedience")
        the_person "As the test went on, she showed better response and obedience to questions and directions."
    if serum_trait_result_list[5] > 0:  #Work skill Serum
        $ positive_flags.append("work")
        the_person "She is showing greater aptitude for work related tasks than before the serum."
    if serum_trait_result_list[6] > 0:  #sex skill serum
        $ positive_flags.append("sex")
        the_person "She appears to be more able to pick up subtle clues in words and body language associated with sex, possibly making her a better partner."
    if serum_trait_result_list[7] > 0:  #Energy Serum
        $ positive_flags.append("energy")
        the_person "As the test continued, she appeared to be more energetic doing the survey instead of less."
    if serum_trait_result_list[8] > 0:  #Suggest Serum
        $ positive_flags.append("suggest")
        the_person "She seems to be more suspectible to suggestions about her behavior and beliefs."
    if len(positive_flags) == 0:    #No obvious immediate positive effects.
        the_person "Unforunately, I don't think that this serum trait has any positive immediate effects. There is a little bit of variability in the results, but it is hard to make a pattern of."
        the_person "It is likely it has longer term effects in longer laster serum cocktails than in the simple production run we use for these tests."

    the_person "Next, the negative effects."
    if serum_trait_result_list[0] < 0:  #Slutty Serum
        $ negative_flags.append("slut")
        the_person "She seems to have a reduced sex drive."
    if serum_trait_result_list[1] < 0:  #Happy Serum
        $ negative_flags.append("happy")
        the_person "Her demeanor shifted negatively throughout the study, indicating less work and relationship satisfaction."
    if serum_trait_result_list[2] < 0:  #Arousal Serum
        $ negative_flags.append("arousal")
        the_person "She seemed to get less aroused by sexual related questions and cues."
    if serum_trait_result_list[3] < 0:  #Love Serum
        $ negative_flags.append("love")
        the_person "Her opinion of you shifted negatively."
    if serum_trait_result_list[4] < 0:  #obedience Serum
        $ negative_flags.append("obedience")
        the_person "She started to show negative signs of submission to authority during the test."
    if serum_trait_result_list[5] < 0:  #Work skill Serum
        $ negative_flags.append("work")
        the_person "She seems to be less qualifed for her work related tasts while under the effects of this serum."
    if serum_trait_result_list[6] < 0:  #sex skill serum
        $ negative_flags.append("sex")
        the_person "Strangely, she seems to be less in tune to the needs and desires of those around her."
    if serum_trait_result_list[7] < 0:  #Energy Serum
        $ negative_flags.append("energy")
        the_person "She tired out quickly during the testing."
    if serum_trait_result_list[8] < 0:  #Suggest Serum
        $ negative_flags.append("suggest")
        the_person "Her beliefs became more firm throughout the testing, indicating a reduced willingness to change."
    if len(negative_flags) == 0:
        the_person "Thankfully, I don't see any immediate negative effects from the serum."

    if len(positive_flags) > 0 and len(negative_flags) > 0:
        $ the_serum_trait.add_mastery(3)
        $ mc.log_event("Mastery of " + the_serum_trait.name + " increased by 3.", "float_text_blue")
    elif len(positive_flags) > 0 or len(negative_flags) > 0:
        $ the_serum_trait.add_mastery(2)
        $ mc.log_event("Mastery of " + the_serum_trait.name + " increased by 2.", "float_text_blue")
    else:
        $ the_serum_trait.add_mastery(1)
        $ mc.log_event("Mastery of " + the_serum_trait.name + " increased by 1.", "float_text_blue")
    the_tester"Wow, that's crazy."
    return positive_flags
