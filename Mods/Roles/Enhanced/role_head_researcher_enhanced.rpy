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
    test_forbidden_research_trait_list = []  #Use this to specify any other serums that would be problematic to research in the test room.
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
        if mc.business.event_triggers_dict.get("head_researcher_cure_disease_name", None) is not None:
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
        if alexia in mc.business.market_team:
            return alexia
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
        start_sluttiness = test_person.sluttiness
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

    def make_trait_research_list():
        research_trait_list = []
        for trait in list_of_traits:
            if trait.tier > 3:
                pass
            elif not trait.researched:
                pass
            elif "Production" in trait.exclude_tags or "Dye" in trait.exclude_tags or "Weight Modification" in trait.exclude_tags or "Pregnancy" in trait.exclude_tags or "Height Modification" in trait.exclude_tags or "Nanobots" in trait.exclude_tags:
                pass
            elif trait in test_forbidden_research_trait_list:
                pass
            else:
                research_trait_list.append(trait)
        return research_trait_list


#Requirement Functions
init -1 python:
    def head_researcher_suggest_testing_room_requirement():
        if mc.business.research_tier >= 1:
            if mc.business.days_since_event("tier_1_serum_unlock_day", set_if_none = True) > TIER_2_TIME_DELAY:
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
            if not mc.is_at_work():
                return "Only in the office"
            if not mc.business.is_open_for_business():
                return "Only during business hours"
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
        if mc.business.is_open_for_business() and mc.business.head_researcher is not None: #Only trigger if people are in the office.
            if mc.business.head_researcher.days_since_event("obedience_event") >= TIER_2_TIME_DELAY and mc.business.head_researcher.obedience >= 160:
                if len(mc.business.market_team) > 0:
                    return True
        return False

    def head_researcher_cure_discovery_market_patent_requirement(the_person):
        if mc.business.is_open_for_business():
            if the_person.is_at_work():
                return True #Only while she is at work
        return False

    def head_researcher_cure_discovery_patent_sold_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.head_researcher is not None:
            if mc.business.head_researcher.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def head_researcher_cure_discovery_patent_kept_requirement():
        if mc.business.is_open_for_business() and mc.business.head_researcher is not None:
            if mc.business.head_researcher.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def head_researcher_cure_finish_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.head_researcher is not None:
            return True
        return False

#Action definitions
    head_researcher_suggest_testing_room = Action("Testing room request", head_researcher_suggest_testing_room_requirement, "head_researcher_suggest_testing_room_label")
    head_researcher_testing_room_intro = Action("Testing Room Intro", head_researcher_testing_room_intro_requirement, "head_researcher_testing_room_intro_label")
    head_researcher_serum_trait_test = Action("Test a Serum Trait {image=gui/heart/Time_Advance.png}", head_researcher_serum_trait_test_requirement, "head_researcher_serum_trait_test_label",
        menu_tooltip = "Perform intensive serum trait test with the help of your head researcher on an employee.", priority = 5)
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
    $ the_person.set_event_day("obedience_event")
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
    if the_person is None:
        return #Bad end
    if mc.location != rd_division:
        $ mc.start_text_convo(the_person)
        the_person "Hey, I need to see you in the lab ASAP!"
        mc.name "On my way!"
        $ mc.end_text_convo()
        "You quickly head to the lab."
        $ mc.change_location(rd_division)
    $ the_person.set_event_day("obedience_event")
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
        mc.name "Noted. I'll talk to her when I can."
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
        the_target = None
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
    if the_person is None:
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
    $ the_disease = head_researcher_cure_discovery_disease_name()
    "You get a notification on your phone and you check it. It's from the Red Cross?"
    "Red Cross""Thank you for donating your patent for [the_disease]!"
    "Red Cross""With this donation, we promise we will work to the best of our abilities to get this cure into the hands of everyone who needs it, worldwide."
    "Donated? What the hell? You didn't donate that!"
    if the_person is None:
        "Suddenly, you realize what must have happened. After clearing out her desk, the old head researcher must have donated the patent she discovered!"
        "Well, maybe you should have considered selling the patent. Either way, that business opportunity is now gone."
        $ del the_disease
        return
    else:
        "Suddenly, you realize what must have happened. [the_person.title], not happy with your intention to keep the patent, must have secretly donated the rights to it."
    "You call her up."
    $ the_person.set_event_day("obedience_event")
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
    $ mc.change_location(ceo_office)
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
    $ mc.business.set_event_day("serum_trait_test")
    $ the_person.add_unique_on_room_enter_event(head_researcher_strip_tease)
    $ the_person.set_event_day("obedience_event")
    return

label head_researcher_serum_trait_test_label(the_person):
    mc.name "There is a serum trait that I would like to study."
    the_person "Okay."
    call serum_research_select_tester_label(the_person) from _select_research_tester_01
    $ the_tester = _return
    $ clear_scene()
    $ scene_manager = Scene()
    "You head down to the testing room. After a few minutes, [the_person.possessive_title] returns with today's test subject."
    $ scene_manager.add_actor(the_person, display_transform = character_left_flipped, z_order = 10)
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
    if "suggest" in test_positive_flags:
        the_person "Alright, we have one more part to the test, however, this part is optional."
        the_person "Research indicates that this particular serum may be more effective if the person has an orgasm after receiving a dose."
        the_tester "An... orgasm?"
        if the_person.sluttiness < 40:
            the_person "Yes. [the_person.mc_title] and I can step out of the room and give you some privacy if you would like to participate in this portion."
            if the_tester.sluttiness < 20 and the_person.obedience < 120:
                the_tester "I think I'd rather opt out of this portion."
                the_person "Certainly."
            elif the_tester.sluttiness < 20:
                the_tester "I guess I could do that... Could you wait outside please?"
                the_person "Certainly. When you are done, just hit the call light there on bed."
                the_tester "Okay."
                $ scene_manager.remove_actor(the_tester)
                "You step outside of the testing room with [the_person.possessive_title]."
                the_person "I'm going to go and file the results. Can you check back with her when she finishes?"
                mc.name "Certainly."
                $ scene_manager.remove_actor(the_person)
                "[the_person.title] steps away, leaving you alone outside the testing room door... while [the_tester.possessive_title] is masturbating inside..."
                call serum_tester_masturbate_privately_label(the_tester) from _test_serum_private_masturbation_label_01

                call serum_tester_trance_label(the_tester) from _serum_test_trance_finish_01
            else:
                the_tester "Oh... umm... can [the_tester.mc_title] stay?"
                "[the_person.possessive_title] seems surprised."
                the_person "Well, sure? I suppose that would still be okay..."
                the_person "I'll, umm... just go file the results we have."
                if the_person.is_girlfriend():
                    the_person "Don't worry [the_person.mc_title]... I understand. This is for science. Do you what you need to do."
                $ scene_manager.remove_actor(the_person)
                "[the_person.title] grabs her things and leaves you with [the_tester.title], alone."
                call serum_tester_suggest_help_label(the_tester) from _serum_test_trance_fuck_01
        elif the_person.sluttiness < 80:
            the_person "Yes. I'll step out, but if you would like, [the_person.mc_title] can give you a hand."
            "[the_person.title] flashes you a quick smile and a wink."
            if the_tester.sluttiness < 20:
                the_tester "Ah geeze... does he have to stay in?"
                "Before she can respond, you step in."
                mc.name "Yes. Atleast one of us needs to be here in case there are any unexpected side effects."
                the_tester "Ah... okay... I guess I can do that, if it would really help out."
                the_person "It would! Just give me one moment and I'll gather my things and go..."
                "[the_person.possessive_title] quickly gathers her things and leaves you alone with [the_tester.title]."
                $ scene_manager.remove_actor(the_person)
                mc.name "Alright, just pretend like I'm not here."
                the_tester "Okay, try not to look too close..."
                call serum_tester_masturbation_show_label(the_tester) from _serum_test_masturbation_show_01
                call serum_tester_trance_label(the_tester) from _serum_test_trance_finish_02
            else:
                the_tester "Oh! I suppose that sounds nice. If that is what you need for the test."
                mc.name "We do."
                the_person "In fact, we have found some of the effects are actually stronger if a partner is there to give the orgasm."
                "Damn. What a wingman."
                the_tester "Okay! An orgasm for science sounds okay by me!"
                the_person "Just give me one moment and I'll gather my things and go..."
                "[the_person.possessive_title] quickly gathers her things and leaves you alone with [the_tester.title]. She gives you a wink on her way out."
                $ scene_manager.remove_actor(the_person)
                call serum_tester_suggest_help_label(the_tester) from _serum_test_trance_fuck_02
        else:   #She is slutty and angles for a threesome
            the_person "Yes. And if you like, either myself or [the_person.mc_title] can give you a hand... or both of us..."
            the_tester "Both of you? Oh my..."
            if the_tester.sluttiness < 20:
                the_tester "No no, that is crazy. I can just do it myself."
                the_person "Okay. I'll go file the results, but [the_person.mc_title] will still need to stay to observe."
                the_tester "He does? Why?"
                mc.name "Atleast one of us needs to be here in case there are any unexpected side effects."
                the_tester "Ah... okay... I guess I can do that, if it would really help out."
                the_person "It would! Just give me one moment and I'll gather my things and go..."
                "[the_person.possessive_title] quickly gathers her things and leaves you alone with [the_tester.title]."
                $ scene_manager.remove_actor(the_person)
                mc.name "Alright, just pretend like I'm not here."
                the_tester "Okay, try not to look too close..."
                call serum_tester_masturbation_show_label(the_tester) from _serum_test_masturbation_show_02
                call serum_tester_trance_label(the_tester) from _serum_test_trance_finish_03
            elif not willing_to_threesome(the_person, the_tester):  #She's atleast somewhat slutty but not willing to threesome.
                the_tester "I don't think I need both of you. [the_tester.mc_title] can help?"
                mc.name "Of course, I'd be glad to."
                the_tester "Okay! An orgasm for science sounds okay by me!"
                the_person "Just give me one moment and I'll gather my things and go..."
                "[the_person.possessive_title] quickly gathers her things and leaves you alone with [the_tester.title]. She gives you a wink on her way out."
                $ scene_manager.remove_actor(the_person)
                call serum_tester_suggest_help_label(the_tester) from _serum_test_trance_fuck_03
            else:
                the_tester "That sounds amazing..."
                the_person "It might be hard to stop at one orgasm though."
                "[the_person.title] looks over at you, thoughtfully."
                the_person "Have we tested this after giving someone multiple orgasms yet?"
                mc.name "Does it matter? We're about to."
                call start_threesome(the_person, the_tester, start_position = Threesome_standing_embrace, position_locked = True) from _serum_tester_threesome_treat_01
                "When you finish, you remember there being something you were supposed to do... but you forget what."
                the_person "I... I need to go file these results... and get a cup of coffee!"
                "Slowly, [the_person.title] gets up, gathers her stuff, and leaves the room."
                $ scene_manager.remove_actor(the_person)
                $ scene_manager.update_actor(the_tester, position = "sitting")
                "[the_tester.possessive_title] sits down on the medical bed, recovering."

    else:
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

    elif ("slut" in test_positive_flags or "arousal" in test_positive_flags) and the_tester.sluttiness >= 30:
        the_tester "Hey umm... I was just wondering... that serum has left me feeling kind of needy."
        the_tester "I'm not saying you have to but, it would be really nice if you could help me get off before you go."
        mc.name "You want me to help you orgasm?"
        the_tester "I mean, I could masturbate too... but it would be nice if you could spare the time."
        menu:
            "Help her out":
                mc.name "Okay, I can help you out. I don't want to leave you hanging, and being aroused might make it hard for you to concentrate on work."
                the_tester "Oh, thanks! That is a relief."
                "With her being under the effects of a serum, it might be a good change to push her limits a little, also."
                call serum_tester_suggest_help_label(the_tester) from _serum_test_trance_fuck_04
            "Let her masturbate":
                mc.name "I'm sorry, I can't help out right now. But the room is yours for the rest of this time block."
                mc.name "If you need to relieve some tension, feel free. I wouldn't want you to be too distracted when you back to work."
                the_tester "Ah, okay. Thank you!"
                $ scene_manager.clear_scene()
                "You step out of the room, leaving [the_tester.title] to take care of herself. Your work here has increased your mastery of [the_serum_trait.name]!"
                $ mc.business.set_event_day("serum_trait_test")
                $ the_tester.have_orgasm()
                call advance_time from _call_advance_time_mastery_research_02
                return "Advance Time"
    else:
        the_tester "Well, hopefully you got the data you needed. Can I get back to work?"
        mc.name "Yes. Thank you for you help, [the_tester.title]."
    $ scene_manager.clear_scene()
    "[the_tester.title] steps out of the room also. Your work here has increased your mastery of [the_serum_trait.name]!"
    $ mc.business.set_event_day("serum_trait_test")
    call advance_time from _call_advance_time_mastery_research_01
    return "Advance Time"

label serum_research_select_tester_label(the_person):
    $ the_tester = get_random_from_list(mc.business.get_requirement_employee_list(exclude_list = [the_person]))
    if the_person.obedience < 120:
        mc.name "Get me a random tester and we'll get this started."
        the_person "Right away."
        return the_tester
    elif the_person.obedience < 140:
        mc.name "What if there is someone specific that I want to test a serum on?"
        the_person "Someone specific? That would invalidate the data."
        "She thinks about it for a moment."
        the_person "No, I'm sorry. It need to be a completely random participant."
        "You can tell there is no convincing her otherwise."
        mc.name "Fine. Get me a random tester and we can get this started."
        the_person "Yes sir."
        return the_tester
    elif the_person.obedience < 160:
        mc.name "What if there is someone specific I want to test a serum on?"
        the_person "Someone specific? I mean, usually these tests are done blind..."
        mc.name "Usually?"
        the_person "Well, having someone in mind already could lend a bias to the data collected..."
        if mc.charisma >= 5:
            mc.name "Sure, but regardless of who the tester is, there should be SOME data that we can collect."
            the_person "I suppose, but this seems to be pretty irregular for a pharmaceutical testing environment."
            mc.name "Just pull up the employee list."
            "[the_person.title] sighs, but eventually relents."
            the_person "Yes sir."
        else:
            "You almost have her convinced, but she suddenly changes her mind."
            the_person "No... no... there's a reason procedures are what they are. Let me get someone random."
            mc.name "Fine. Let's get this started."
            return the_tester
    elif the_person.obedience < 180:
        the_person "Let me just call down someone random..."
        mc.name "Random? What if I want someone specific?"
        "[the_person.title] sighs, but relents."
        the_person "Fine. Do you want to decide who we bring down?"
        menu:
            "Random participant":
                the_person "Right..."
                return the_tester
            "Pick the participant":
                mc.name "Of course. Bring up the employee list, I'll choose who we get."
    else:
        the_person "[the_person.mc_title], did you want to choose the participant this time?"
        menu:
            "Random participant":
                the_person "Okay, I'll get someone random then."
                return the_tester
            "Pick the participant":
                mc.name "Of course. Bring up the employee list, I'll choose who we get."
                the_person "Right away sir."
    "[the_person.possessive_title] pulls up the employee list for you."

    call screen enhanced_main_choice_display(build_menu_items([["Call in"] + mc.business.get_requirement_employee_list(exclude_list = [the_person]) + ["Changed my mind"]], draw_hearts_for_people = False))
    $ person_choice = _return
    if person_choice == "Changed my mind":
        the_person "Right, I'll just select someone randomly..."
        return the_tester
    the_person "Okay, I'll call them down."
    return person_choice

label serum_research_tester_response_label(the_tester):
    if the_tester.obedience < 100:
        the_tester "No? Not really? The details were a little vague about what you wanted..."
        mc.name "We want to study the effects of a recently researched serum trait in a restricted, controlled environment."
        the_tester "Umm... I don't know... are you sure it is safe?"
        if mc.int >= 5: #Smart enough we talk our way into it.
            mc.name "Absolutely. None of the serums in this line have produced any significant long term side effects so far, and I'm confident this one is the same way."
            the_tester "I... I guess..."
            "Thankfully you managed to convince her."
            return True
        else:
            mc.name "I... well... there is a reason we are doing these tests..."
            the_tester "You have no idea, do you?"
            mc.name "We are pretty sure there won't be any long term side effects."
            the_tester "Pretty sure? I don't think I want to do this."
        if mc.charisma >= 5:
            mc.name "You are in good hands. The head researcher will be here the whole time, I promise you have nothing to worry about."
            "Her face softens a bit. It seems you may have been able to convince her..."
            the_tester "I guess... let's just get this over with..."
            return True
        else:
            mc.name "I'm here, and the head researcher is here. If anything happens, we'll be able to take immediate action."
            the_tester "Immediate action? You aren't making me feel any better!"
        menu:
            "Offer $100" if mc.business.funds >= 100:
                mc.name "I understand you need more convincing. How about if I pay you a $100 bonus to take part in the test."
                the_tester "Hmm..."
                "She thinks about it for a moment."
                the_tester "Alright. I could really use the money."
                mc.name "Excellent."
                "You setup a funds transfer to [the_tester.title] before the testing begins."
                $ mc.business.change_funds(-100)
                return True
            "Offer $100\n{color=#ff0000}{size=18}Requires: $100{/size}{/color} (disabled)" if mc.business.funds < 100:
                pass
            "Threaten discipline":
                mc.name "I didn't want it to be this way, but we really need this testing done."
                mc.name "Do it or I'll have to reduce your marks on your next review."
                $ the_tester.change_happiness(-10)
                $ the_tester.change_love(-5)
                $ the_tester.change_obedience(2)
                the_tester "Fuck you. Fine, do the stupid test."
                return True
    elif the_tester.obedience < 120:
        the_tester "I don't know... these things seem kind of sketchy to me..."
        "Seems like she is likely going to need some convincing in order to take part."
        menu:
            "Reassure her" if mc.int >= 4:
                mc.name "I understand your concern, but let me rest your mind."
                mc.name "None of the serums in this line have produced any significant long term side effects so far, and I'm confident this one is the same way."
                the_tester "Wow... Okay, I'll do it."
                "Thankfully you managed to convince her."
                $ the_tester.change_obedience(2)
                return True
            "Reassure her\n{color=#ff0000}{size=18}Requires: 4 Intelligence{/size}{/color} (disabled)" if mc.int < 4:
                pass
            "Convince her" if mc.charisma >= 4:
                mc.name "Don't worry, I totally understand your concerns. That is why are taking excessive precautions."
                mc.name "Both myself and the head researcher will be here the whole time, I promise you have nothing to worry about."
                "Her face softens a bit. It seems you may have been able to convince her..."
                the_tester "Okay, that seems okay, as long you are around."
                $ the_tester.change_obedience(2)
                return True
            "Convince her\n{color=#ff0000}{size=18}Requires: 4 Charisma{/size}{/color} (disabled)" if mc.charisma < 4:
                pass
            "Offer $100" if mc.business.funds >= 100:
                mc.name "I understand your hesitation, that is why I have authorized a bonus for the testing process."
                mc.name "If you agree, I'll add $100 to your salary for the day."
                the_tester "Wow. Okay, I could really use the money. I'll do it."
                $ the_tester.change_obedience(2)
                return True
            "Offer $100\n{color=#ff0000}{size=18}Requires: $100{/size}{/color} (disabled)" if mc.business.funds < 100:
                pass
            "Emotional Appeal":
                mc.name "I understand you hesitation. Would you do this a favor to me? This test will really help our understanding of this serum."
                "She looks down at her feet, but after a few moments, she nods."
                the_tester "Okay... but you owe me one."
                mc.name "Certainly."
                return True
    elif the_tester.obedience < 140:
        the_tester "Well... you're the boss, so I guess I don't have much of a choice then?"
        mc.name "Not really, no."
        the_tester "Let's get this over with then."
        return True
    else:
        the_tester "Of course. I'm ready to help out in any way I can."
        mc.name "Excellent."
        return True
    return True

label serum_research_trait_selection_label():
    call screen select_trait_research(make_trait_research_list())
    if _return:
        return _return
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

label serum_tester_suggest_help_label(the_person):
    $ help_choice = None
    "You get up and start to walk over to the testing table."
    mc.name "Have any requests?"
    # First, figure out how she wants MC to help, and decide MC's response
    if the_person.sluttiness < 30:
        the_person "Oh... I don't know... this is so embarassing!"
        mc.name "It's okay, I understand. Why do you just take your bottoms off and I'll use my fingers?"
        if the_person.opinion_score_being_fingered() == -2:
            the_person "To be honest, I hate being fingered..."
            mc.name "I understand, but this isn't just for enjoyment, we are testing the serum effects."
            the_person "Ah... I suppose..."
        else:
            the_person "That sounds good... okay!"
        $ help_choice = "finger"

    elif the_person.sluttiness < 45 and perk_system.has_item_perk("Dildo"):
        the_person "I wish I had one of my toys with me, that would make this easier..."
        "You remember you have a dildo that you could use from the sex store."
        mc.name "Actually, I think I have one. Do you want me to use a dildo to help you orgasm?"
        the_person "Oh! That would be perfect! Would you?"
        "You think about it for a moment."
        menu:
            "Use dildo":
                $ help_choice = "toy"
                mc.name "Yeah, let me do that."
            "Finger her":
                $ help_choice = "finger"
                mc.name "Actually, how about if I just use my fingers?"
                if the_person.opinion_score_being_fingered() == -2:
                    the_person "To be honest, I hate being fingered..."
                    mc.name "I understand, but this isn't just for enjoyment, we are testing the serum effects."
                    the_person "Ah... I suppose..."
                else:
                    the_person "That sounds good too. Okay!"
    elif the_person.sluttiness < 60:

        the_person "Honestly, getting eaten out sounds amazing right now..."
        if the_person.opinion_score_getting_head() == -2:
            the_person "I'm not usually into that, but for some reason it just sounds really nice!"
        mc.name "Hmm."
        "Do you want to go down on [the_person.title]? Or do something else?"
        menu:
            "Eat her out":
                $ help_choice = "oral"
                mc.name "Mmm, I can't wait to taste that sweet pussy of yours."
            "Use dildo" if perk_system.has_item_perk("Dildo"):
                $ help_choice = "toy"
                mc.name "I have another idea."
                "You grab your dildo and show it to her."
                the_person "Oh! That looks like fun too... okay!"
            "Use Dildo\n{color=#ff0000}{size=18}Requires: Dildo{/size}{/color} (disabled)" if not perk_system.has_item_perk("Dildo"):
                pass
            "Finger her":
                $ help_choice = "finger"
                mc.name "Actually, how about if I just use my fingers?"
                if the_person.opinion_score_being_fingered() == -2:
                    the_person "To be honest, I hate being fingered..."
                    mc.name "I understand, but this isn't just for enjoyment, we are testing the serum effects."
                    the_person "Ah... I suppose..."
                else:
                    the_person "That sounds good too. Okay!"
    else:
        "[the_person.title] bites her lip and looks down at your crotch."
        the_person "Can you just fuck me? You big dick sounds amazing right now."
        if the_person.opinion_score_vaginal_sex() == -2:
            the_person "I don't know why though... I usually hate being penetrated that way..."
            mc.name "Could be an effect of the serum?"
            the_person "Yeah, maybe..."
            "It might be worth testing her sudden interest in vaginal sex. Maybe you could make her interest more permanent..."
        else:
            "You had a feeling this little slut would be asking for your cock. The question is, do you give it to her?"
        menu:
            "Fuck her":
                $ help_choice = "fuck"
            "Eat her out":
                $ help_choice = "oral"
                mc.name "How about if I go down on you and lick that sweet pussy of yours."
                if the_person.opinion_score_getting_head() == -2:
                    the_person "Oh! Umm, I'm not usually into that..."
                    mc.name "I understand, but this isn't just for enjoyment, we are testing the serum effects."
                    the_person "Ah... I suppose..."
                else:
                    the_person "Oohhh, that sounds nice too! Okay!"
            "Use dildo" if perk_system.has_item_perk("Dildo"):
                $ help_choice = "toy"
                mc.name "I have another idea."
                "You grab your dildo and show it to her."
                the_person "Oh! That looks like fun too... okay!"
            "Use Dildo\n{color=#ff0000}{size=18}Requires: Dildo{/size}{/color} (disabled)" if not perk_system.has_item_perk("Dildo"):
                pass
            "Finger her":
                $ help_choice = "finger"
                mc.name "Actually, how about if I just use my fingers?"
                if the_person.opinion_score_being_fingered() == -2:
                    the_person "To be honest, I hate being fingered..."
                    mc.name "I understand, but this isn't just for enjoyment, we are testing the serum effects."
                    the_person "Ah... I suppose..."
                else:
                    the_person "That sounds good too. Okay!"

    if help_choice == "finger":
        call serum_tester_finger_aid_label(the_person) from _serum_test_finger_help_01

    elif help_choice == "toy":
        call serum_tester_dildo_aid_label(the_person) from _serum_test_dildo_help_01
    elif help_choice == "oral":
        call serum_tester_oral_aid_label(the_person) from _serum_test_oral_help_01
    elif help_choice == "fuck":
        call serum_tester_fuck_aid_label(the_person) from _serum_test_fuck_help_01

    if the_person.is_in_trance():
        call serum_tester_trance_label(the_person) from _serum_test_trance_followup_01
    return

label serum_tester_trance_label(the_tester):
    mc.name "Alright, sit up on the table there. Let's take a look at you."
    $ scene_manager.update_actor(the_tester, position = "sitting")
    "You grab a small flashlight and wave it in front of her eyes a bit. Her pupils are definitely dialated."
    "She has all the signs of being in a trance. You consider the opportunity."
    call do_training(the_person) from _call_do_training_serum_testing_01
    return

label serum_tester_masturbate_privately_label(the_tester):
    "You quietly put your ear up to the door..."
    the_tester "Ahh.... mmm...."
    "You can hear some muffled moans through the door..."
    $ mc.change_locked_clarity(30)
    if the_tester.sluttiness >= 30:
        the_tester "Oh fuck... that's it [the_tester.mc_title]..."
        $ mc.change_locked_clarity(30)
        "Oh damn... she's fantasizing about you!"
        "You consider stepping inside and helping out... but ultimately, you decide you'd better stick to your agreement to step out."
    else:
        "You decide not to intrude on her masturbation session. It could effect the data from the test, anyway..."
    $ the_tester.have_orgasm(force_trance = True)
    "After several minutes, the light on the outside of the door iluminates, so you step inside."
    $ scene_manager.add_actor(the_tester, position = "sitting")
    "[the_tester.possessive_title] is sitting on the edge of the bed."
    mc.name "Finished?"
    the_tester "I umm... yeah..."
    return

label serum_tester_masturbation_show_label(the_tester):
    if True:
        "[the_tester.possessive_title] almost starts to get undressed, but then stops."
        the_tester "I'm sorry... I just can't... can you just wait outside?"
        mc.name "I suppose. You are helping out, so if that is what you need."
        the_tester "Yes, I'm sorry."
        $ scene_manager.clear_scene()
        "You step outside of the testing room to give [the_tester.title] some privacy."
        call serum_tester_masturbate_privately_label(the_tester) from _temp_label_call_masturbation_show_01
    else:
        pass
        "Sorry, Starbuck still needs to write this."
    return

label serum_tester_finger_aid_label(the_person):
    if the_person.vagina_available() and the_person.vagina_visible():
        "[the_person.title] scoots to the edge of the medical bed and spreads her legs for you as you walk over to her."
    else:
        "[the_person.title] strips off her bottoms as you walk over to her."
        $ scene_manager.strip_to_vagina(the_person)
        "She scoots to the edge of the medical and spreads her legs for you."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "Her cunt is on full display for you."
    $ mc.change_locked_clarity(20)
    "You stand next to her and start to your hands up and down her thighs. She bites her lip and looks you in the eyes."
    mc.name "Alright, here we go."
    "Carefully, you insert one finger up into her slit."
    if the_person.arousal < 25:
        "You go nice and slow, working your finger in and out, as you begin to feel the first indications of her arousal building."
        "It takes a bit, but you can feel her pussy start to get wet as you begin to finger her."
        $ mc.change_locked_clarity(20)
    elif the_person.arousal < 50:
        "Your finger slides in easily, with just a bit of resistance. She was already a bit aroused before the test."
        $ mc.change_locked_clarity(20)
    else:
        "Your finger slides easily into her sopping wet cunt. Apparently she was already aroused and ready for this!"
        $ mc.change_locked_clarity(20)
    if the_person.arousal >= 40:
        "You push a second finger into her eager cunt while she gives a low moan."
    if the_person.arousal >= 80:
        if not the_person.tits_visible() or not the_person.tits_available():
            the_person "Ah! One second... I... I need to do something..."
            "You keep fingering her as she pulls off her top."
            $ scene_manager.strip_to_tits(the_person)
        "You lean forward and start to lick and suck on one of her exposed nipples."
        $ mc.change_locked_clarity(20)
    if the_person.arousal >= 100:
        the_person "Oh fuck! I'm so hot... [the_person.mc_title] I'm sorry, I'm... I'm gonna cum!"
        "Wow, she must have been really pent up! She is getting ready to orgasm already!"
        $ mc.change_locked_clarity(30)

    if the_person.arousal < 20:
        the_person "Ah... go slow please... I need to warm up a bit."
        "You follow her request. You take it nice and slow, exploring her insides with one finger."
        the_person "Mmm yeah... that's it..."
        "She closes her eyes and concentrates on her feelings as her body gets aroused."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal < 40:
        the_person "That's starting to feel so good... keep going..."
        "Her body is definitely responding to your intimate touches. Her cheeks are getting red and her breathing is getting deeper."
        "You finger is sliding in and out of her easily now. You pull out for a moment, then push two fingers inside of her."
        the_person "Ahhh! That's it! So good..."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal < 60:
        the_person "Ahhh... Mmmm..."
        "[the_person.possessive_title] is trying to stifle her moans as they begin to grow more eager."
        "She looks up at you, and when your eyes meet, she can't stifle them anymore."
        the_person "Ahh! Oh [the_person.mc_title], that feels really good!"
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal < 80:
        if not the_person.tits_visible() or not the_person.tits_available():
            the_person "Ah! One second... I... I need to do something..."
            "You keep fingering her as she pulls off her top."
            $ scene_manager.strip_to_tits(the_person)
            "Her tits bounce free, making an enticing target."
        else:
            "You look down at [the_person.title]'s tits. They are jiggling slightly as she starts to move her hips, making an enticing target."
        "You lean forward and lick around one of her stiff nipples. She moans and runs her hand through your hair, holding your mouth to her tit."
        the_person "Ohhh fuck... that is so good..."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
    if the_person.arousal < 100:
        "[the_person.possessive_title] moans and writhes beneath your skillful touching. She is moaning non stop now."
        the_person "Yes! Oh fuck yes... I'm so close..."
        "Her words and her breathing show you just how close she is. You can tell she is in the final stretch."
        "You eagerily finger her, curling your fingers and stroking her g-spot while you suckle and nip at her nipple."
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(30)
    the_person "Yes! Oh YES!"
    $ the_person.have_orgasm(force_trance = True)
    "[the_person.title]'s breathing stops as her hips start to twitch. Her whole body trembles as she begins to orgasm."
    the_person "Ah! Ahhhhh! Oh..."
    "Waves of orgasm rock her body, then begin to get smaller and smaller."
    the_person "Mmm... Ahh..."
    "She seems finished, but you give her nipple one last suckle and feel her whole body twitch in response."
    $ mc.change_locked_clarity(50)
    if the_person.opinion_score_being_fingered() == -2:
        the_person "That was incredible. I never knew it could feel so good!"
        mc.name "Sometimes you learn new things about yourself when you try things with different partners."
        the_person "Yeah..."
        mc.name "So, you think you might like to be fingered again sometime?"
        "She chuckles."
        the_person "Yeah... I think I would..."
        $ the_person.increase_opinion_score("being fingered")
    else:
        the_person "God, it feels so good when you touch me like that..."
        "You can tell that you have made an impression on her. She may be more receptive to being fingered by you in the future."
        $ the_person.increase_opinion_score("being fingered")
    "You remove your fingers from her and clean yourself up a bit while she recovers."
    return

label serum_tester_dildo_aid_label(the_person):
    if the_person.vagina_available() and the_person.vagina_visible():
        "[the_person.title] scoots to the edge of the medical bed and spreads her legs for you as you walk over to her."
    else:
        "[the_person.title] strips off her bottoms as you walk over to her."
        $ scene_manager.strip_to_vagina(the_person)
        "She scoots to the edge of the medical and spreads her legs for you."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "Her cunt is on full display for you."
    $ mc.change_locked_clarity(20)
    "You grab some lubrication from a nearby shelf and spread some on the dildo, getting it ready to penetrate her."
    mc.name "Alright, here we go."
    "Carefully, you slowly start to push the dildo inside of her."
    if the_person.arousal < 25:
        "You go nice and slow. [the_person.possessive_title]'s pussy is tight, and you need to get her worked up a bit more before you fuck her with the dildo outright."
        "It takes a bit, but after a couple strokes you can feel the dildo start to slide in and out easier."
        $ mc.change_locked_clarity(20)
    elif the_person.arousal < 50:
        "There is a little bit of resistance, but the dildo slides into her. She was already a little bit aroused before this test, apparently."
        $ mc.change_locked_clarity(20)
    else:
        "The dildo slides into her soaking wet pussy easily. She must have already been pretty aroused!"
    if the_person.arousal >= 40:
        if not the_person.tits_visible() or not the_person.tits_available():
            the_person "Ah! One second... I... I need to do something..."
            "You leave the dildo inserted as she starts to wiggle out of her top."
            $ scene_manager.strip_to_tits(the_person)
        "With one hand, you start to fuck her with the dildo, with the other you grope her exposed tits."
        $ mc.change_locked_clarity(20)
    if the_person.arousal > 80 and the_person.opinion_score_giving_handjobs() > 0:
        "You feel her hand on your crotch as she pulls the zipper down. She pulls your cock out of your pants."
        the_person "I want to touch it while you do that... can I please?"
        "Her request really turns you on. You nod."
        mc.name "How could I say no?"
        "[the_person.possessive_title]'s soft hand strokes you in time with each thrust you make with the dildo. It feels amazing."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(25)
    if the_person.arousal >= 100:
        the_person "Oh fuck! I'm so hot... [the_person.mc_title] I'm sorry, I'm... I'm gonna cum!"
        "Wow, she must have been really pent up! She is getting ready to orgasm already!"
        "You quickly speed up and start to really bang her with the dildo."
        $ mc.change_locked_clarity(30)

    if the_person.arousal < 20:
        the_person "Ah... fuck... it's so big, take it slow!"
        "You can tell that definitely be for the best. Her body is still adjusting to the size of the dildo, so you give her nice and slow thrusts."
        the_person "Mmm yeah... that's it..."
        "She closes her eyes and concentrates on her feelings as her body gets aroused."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal < 40:
        the_person "That feels good. You can go a little faster now."
        "You gently speed up. The dildo is sliding in and out of her easy now, and her body is adjusted to the size."
        if not the_person.tits_visible() or not the_person.tits_available():
            the_person "Ah! One second... I... I need to do something..."
            "You leave the dildo inserted as she starts to wiggle out of her top."
            $ scene_manager.strip_to_tits(the_person)
        "She takes your free hand and brings it to her chest."
        the_person "...please?"
        "You oblige her and start to grope her tits with one hand, while you fuck her with the dildo in your other hand."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal < 60:
        the_person "Ahhh... Mmmm..."
        "[the_person.possessive_title] is trying to stifle her moans as they begin to grow more eager."
        "She looks up at you, and when your eyes meet, she can't stifle them anymore."
        the_person "Ahh! Oh [the_person.mc_title], it's so big..."
        "Her eyes flicker down to your crotch. You can tell she is wondering if your cock would feel just as good."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal < 80:
        "[the_person.title] is moving her hips in time with your thrusts now. She moans loudly when you pinch her nipple."
        the_person "Oh fuck! Mmm..."
        if the_person.opinion_score_giving_handjobs() > 0:
            "You feel her hand on your zipper and she tugs it down. She starts to pull out your cock."
            mc.name "That isn't part of the test..."
            the_person "I know, but I want to feel your wonderful cock in my hand... please?"
            "Her demeanor is hot, but you know you should probably say no. You are just getting ready to refuse, when you feel her soft hand start to stroke the skin of your cock."
            mc.name "Ahhh, I mean... if that is what you want..."
            the_person "It is... I promise!"
            "You let her pull your cock out of your pants. She strokes it with her hand in time with you as you fuck her with the dildo."
            $ mc.change_arousal (25)
        else:
            "She closes her eyes as she lets her body fully enjoy the feeling of being filled by the sex toy."
        the_person "Ohhh fuck... that's it... mmmm..."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal < 100:
        "[the_person.possessive_title] moans and writhes on the sex toy. She is moaning non stop now."
        the_person "Yes! Oh fuck yes... harder!"
        "Her words and her breathing show you just how close she is. You can tell she is in the final stretch."
        "You start to really bang her with the dildo, and you eagily grope her fantastic tits."
        if the_person.opinion_score_giving_handjobs() > 0:
            "You feel yourself moving your own hips. Her soft hand feels amazing wrapped around your dick."
            "Having [the_person.title] completely exposed in the office and banging her with the dildo is really turning you on."
            $ mc.change_arousal(30)
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(50)
    the_person "Yes! Oh YES! Fuck me!!!"
    $ the_person.have_orgasm(force_trance = True)
    "[the_person.title]'s breathing stops as her hips start to twitch. Her whole body trembles as she begins to orgasm."
    "You watch in awe as her whole body trembles as she cums all over the dildo."
    if the_person.opinion_score_giving_handjobs() > 0:
        "The scene is so arousing, and her soft hand feels so good."
        menu:
            "Cum on her tits":
                $ mc.change_locked_clarity(50)
                "It feels too good. The urge to cover her in your cum is overwhelming."
                "You quickly takeover. You stroke yourself and start to cum, pointing right at her tits."
                $ ClimaxController.manual_clarity_release(climax_type = "tits", the_person = the_person)
                $ the_person.cum_on_tits()
                $ scene_manager.update_actor(the_person, position = "missionary")
                "You coat her tits in your spunk. Deep in the throes of her own orgasm, she doesn't even realize it at first."
            "Keep yourself from cumming" if mc.arousal < 100 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
                "You dig deep and focus. You don't want to dump a load right now."
                "Besides, it might invalidate the test results to cum all over her."
            "Keep yourself from cumming\n{color=#ff0000}{size=18}Too aroused{/size}{/color} (disabled)" if mc.arousal > 100 and not perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
                pass
    the_person "Mmm... Ahh... fuck..."
    if the_person.has_tits_cum():
        "When she finishes, she looks down and realizes the mess you made of her chest."
        if the_person.opinion_score_being_covered_in_cum() == -2:
            the_person "Wow... really?"
            mc.name "I mean, you wanted to touch me... where else was I going to cum?"
            "She sighs."
            the_person "You know, normally I HATE being covered in cum... but for some reason, it was actually kind of nice this time."
            "She rubs some of your cum into her breast, tweaking her nipple. She gives a soft moan."
            mc.name "Well, you look amazing coated in my cum. You should wear it more often."
            "She chuckles for a moment."
            the_person "If you can give me orgasms like that again, I suppose it would only be fair!"
            $ the_person.increase_opinion_score("being covered in cum")
            "Sounds like you made a positive impression on her. She may be more receptive to getting covered in cum by you in the future."
        elif the_person.opinion_score_being_covered_in_cum() == 2:
            the_person "Damn that was hot. God your cum feels so good all over my skin!"
            "[the_person.title] eagerly rubs it into her soft titflesh. You feel your cock twitch as you watch her."
            $ mc.change_locked_clarity(50)
            mc.name "Let's do this again sometime."
            the_person "Definitely!"
        else:
            the_person "You know what, after an orgasm like that, it feels really good to get covered in your cum."
            mc.name "Well, you look amazing too."
            the_person "Do I?"
            "[the_person.title] looks up at you and starts to rub some of your cum into her soft tit flesh."
            "Your cock had started to soften, but you feel it twitch as you watch her."
            $ the_person.increase_opinion_score("being covered in cum")
            $ mc.change_locked_clarity(30)
            mc.name "Let's do this again sometime."
            the_person "I could definitely see myself doing this again in the future."
            "Sounds like you made a positive impression on her. She may be more receptive to getting covered in cum by you in the future."
    else:
        "She seems finished, but you give her nipple one last pinch and feel her whole body twitch in response."
    "You remove the dildo and start to clean it up as she slowly recovers."
    return

label serum_tester_oral_aid_label(the_person):
    if the_person.outfit.full_access():
        "[the_person.title] scoots to the edge of the medical bed and spreads her legs for you as you walk over to her."
    else:
        "[the_person.title] gets naked as you walk over to her."
        $ scene_manager.strip_full_outfit(the_person)
        "She scoots to the edge of the medical and spreads her legs for you."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "Her entire body is on full display for you. She looks up at you and smirks."
    $ mc.change_locked_clarity(30)
    the_person "Are you just going to look?"
    mc.name "For a moment longer. I'll get to work as soon as I'm ready."
    "She smiles shyly but doesn't move to cover herself up from your gaze."
    mc.name "Alright, here we go."
    "You get down on your knees at the edge of the medical bed. She sighs as you start to kiss along the inside of her thigh, working your way up to her crotch."
    if the_person.arousal < 25:
        "[the_person.possessive_title]'s pristine pussy looks amazing. You run your tongue along it a couple times."
        the_person "Ahh... your breath is so warm..."
        "Tentatively, you push your tongue into her warm folds. She gasps as you start to work your tongue along her slit."
        $ mc.change_locked_clarity(20)
    elif the_person.arousal < 50:
        "[the_person.possessive_title]'s pussy looks amazing. Her labia are just starting to show and her juices fill your nose with signs of her arousal."
        "You run your tongue up and down her slit, enjoying her taste from her already aroused state."
        $ mc.change_locked_clarity(20)
    else:
        "[the_person.possessive_title]'s pussy lips are puffy and are flush with obvious signs of arousal. A tiny bit of her juices are beginning to leak out of it."
        "You run your tongue all along her slit, enjoying her copious juices as you begin to eat her out."
    if the_person.arousal >= 80:
        "[the_person.title] is already so aroused, her body is eager and she moans loudly."
        "You decide to make this quick. You push your pinky into her quivering cunt, getting it good and wet, then remove it."
        "Without further delay, you position your hand so your index and middle fingers are at the entrance to her cunt and your pinky is at her puckered asshole."
        if the_person.opinion_score_being_fingered() == -2:
            "She stiffens up when she feels your fingers."
            the_person "Oh hey, no fingers, I'm not into that..."
            mc.name "Shh, it's part of the test."
            the_person "Oh... I guess..."
            "She is too aroused to put up more of a protest."
        elif the_person.opinion_score_anal_sex() == -2:
            "She stiffens up when she feels your fingers."
            the_person "Hey! I don't like butt stuff..."
            mc.name "Shh, it's part of the test."
            the_person "Wha? Why would it be... ahhh..."
            "You get back to work, licking her cunt. She is to aroused to put up more of a protest."
        else:
            "She moans loudly when she feels your fingers push inside of her."
            the_person "Oh fuck... oh my god!"
        $ mc.change_locked_clarity(50)
    elif the_person.arousal >= 40:
        "[the_person.title]'s arousal is obvious. You can tell you can probably get her off pretty quick."
        "You take two fingers and push them into her as you lick her clit."
        if the_person.opinion_score_being_fingered() == -2:
            "She stiffens up when she feels your fingers."
            the_person "Oh hey, no fingers, I'm not into that..."
            mc.name "Shh, it's part of the test."
            the_person "Oh... I guess..."
            "She is too aroused to put up more of a protest."
        else:
            "She moans loudly when she feels your fingers push inside of her."
            the_person "Ohhhhh fuck..."
        $ mc.change_locked_clarity(50)
    if the_person.arousal >= 100:
        the_person "Oh fuck! [the_person.mc_title] I'm sorry, I'm... I'm gonna cum!"
        "Wow, she must have been really pent up! She is getting ready to orgasm already!"
        "You latch onto her clit with your tongue and eagerly bang her holes with your fingers."
        $ mc.change_locked_clarity(50)

    if the_person.arousal < 20:
        the_person "Ah... your tongue feels so good... that's it..."
        "Her body responds to your tongue as you begin to lick her in earnest. You twirl your tongue around the entrance to her vagina, then slowly push it in."
        the_person "Mmm yeah... that's it..."
        "She closes her eyes and concentrates on her feelings as her body gets aroused."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(40)
    if the_person.arousal < 40:
        "You push your tongue inside of her as deep as it will go, then move it in and out a few times."
        "She tastes great, but you know that penetration with your tongue is just the warmup."
        "You move up along her slit, then start to run circles around her clit with your tongue."
        the_person "Ohhh. That's the spot... mmmm..."
        "You take two fingers and push them into her as you lick her clit."
        if the_person.opinion_score_being_fingered() == -2:
            "She stiffens up when she feels your fingers."
            the_person "Oh hey, no fingers, I'm not into that..."
            mc.name "Shh, it's part of the test."
            the_person "Oh... I guess..."
            "She is too aroused to put up more of a protest."
        else:
            "She moans loudly when she feels your fingers push inside of her."
            the_person "Ohhhhh fuck..."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(40)
    if the_person.arousal < 60:
        the_person "Ahhh... Mmmm..."
        "[the_person.possessive_title] is trying to stifle her moans as they begin to grow more eager."
        "Your skillful tongue and fingers are hitting all the right spots, she can't stifle her moans much longer."
        "You gently start to suckle her clit with your mouth, while curling your fingers forward and rubbing her g-spot."
        the_person "Ahh! Oh [the_person.mc_title], that feels so good!"
        "You can feel her body trembling as you continue to eat her out."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal < 80:
        the_person "Oh fuck! Mmm... that is so good!"
        "[the_person.title]'s hips are moving with your finger as you stroke her insides. You lash eargerly at her clit with your tongue."
        "It is time to take things up a notch. You remove your fingers for a moment, then push your pinky inside her sopping wet hole. You get it lubed up, then take it out."
        "Without further delay, you position your hand so your index and middle fingers are at the entrance to her cunt and your pinky is at her puckered asshole."
        if the_person.opinion_score_anal_sex() == -2:
            "She stiffens up when she feels your fingers."
            the_person "Hey! I don't like butt stuff..."
            mc.name "Shh, it's part of the test."
            the_person "Wha? Why would it be... ahhh..."
            "You get back to work, licking her cunt. She is to aroused to put up more of a protest."
        else:
            "She moans loudly when she feels your fingers push inside of her."
            the_person "Oh fuck... oh my god!"
        "You work both her holes with your fingers now as your tongue gets back to work. She is gasping and moaning with every stroke."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(20)
    if the_person.arousal < 100:
        "[the_person.possessive_title] moans and writhes. Her hip movements are so erratic it is starting to get hard to keep your tongue on her clit."
        "You grab her hip with your free hand and pin her to the bed. She whimpers helplessly as you push her down the final stretch."
        the_person "[the_person.mc_title]... [the_person.mc_title]! I'm so close... Oh baby!"
        "You bang her holes aggressively with your fingers, then latch onto her clit with your mouth and suckle hard."
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(50)
    the_person "Yes! Oh YES! Fuck me!!!"
    $ the_person.have_orgasm(force_trance = True)
    "[the_person.title]'s breathing stops as her hips start to twitch. Her whole body trembles as she begins to orgasm."
    if the_person.event_triggers_dict.get("squirts", False) == True:
        "Her pussy squirts fluid as she cums. She cries out incoherently as she loses control of her body."
    else:
        "Her pussy quivers and you feel her insides repeatedly grip your fingers. You imagine how good it would feel if it were your cock her ass was quivering around..."
    the_person "Mmm... Ahh... fuck..."
    "You look up at [the_person.possessive_title]'s face from between her legs, your fingers still deep inside her holes."
    if the_person.opinion_score_getting_head() == -2:
        the_person "God, don't look at me like that! It's so embarassing..."
        mc.name "What is? To cum all over a man's face?"
        the_person "Yeah! I normally hate getting eaten out like that."
        mc.name "Normall?"
        "She sighs."
        the_person "Well... you're pretty good at that. You know?"
        mc.name "I'd be happy to make you cum with my tongue again sometime."
        the_person "Fine... but maybe without that goofy grin at the end!"
        $ the_person.increase_opinion_score("getting head")
    elif the_person.opinion_score_getting_head() == 2:
        the_person "Fuck that was so good. Your tongue feels amazing. I love it when you go down on me like that."
        mc.name "Happy to be of service, ma'am!"
    else:
        the_person "Wow, that was so good. Honestly? I think I'm starting to really like that..."
        mc.name "Getting eaten out?"
        the_person "Yeah..."
        $ the_person.increase_opinion_score("getting head")
    "You give her holes a little stroke with your fingers. She gasps at the sensation."
    if the_person.opinion_score_being_fingered() == -2:
        the_person "I normally hate being fingered, but with your tongue..."
        if the_person.opinion_score_anal_sex() == -2:
            the_person "And then my ass... I... I hate butt stuff... I thought?"
            mc.name "It's okay. It was a new experience. It's okay to discover new things about yourself."
            the_person "Yeah. You might be right."
            $ the_person.increase_opinion_score("being fingered")
            $ the_person.increase_opinion_score("anal sex")
            mc.name "Maybe we could try more foreplay or anal activity again."
            the_person "I... maybe... I could try again. With you atleast!"
            "You can tell that you have made an impression on her. She may be more receptive to being fingered by you and anal activity in the future!"
        else:
            the_person "When I felt you finger my ass though... god it felt so right."
            mc.name "I thought you would like that."
            the_person "I did."
            $ the_person.increase_opinion_score("being fingered")
            $ the_person.increase_opinion_score("anal sex")
            mc.name "We should try that again sometime."
            the_person "Yeah, I think I would like that."
            "You can tell that you have made an impression on her. She may be more receptive to being fingered by you and anal activity in the future!"
    elif the_person.opinion_score_being_fingered() == 2:
        the_person "It was amazing when you started fingering me."
        if the_person.opinion_score_anal_sex() == -2:
            the_person "But... I'm not sure I like it when you finger my umm... butthole..."
            mc.name "Are you sure? It seemed like you liked it."
            the_person "I mean, I guess it did feel good."
            "She sighs, but relents."
            the_person "You know, you might be right. Maybe we could explore more butt stuff sometime."
            $ the_person.increase_opinion_score("anal sex")
            "Sound like you made an impression on her! She may be more open to anal sex in the future."
        elif the_person.opinion_score_anal_sex() == 2:
            the_person "And then my ass too. Fuck you know how to push all my buttons..."
            "She reaches down and runs her hand through your hair. You give her one last thrust into both her holes with your fingers."
            the_person "Ah!... mmm... You might get be started again..."
        else:
            the_person "You know, I've never been big on butt stuff, but it felt amazing when you finished me off..."
            mc.name "Ah, we play around with putting other things in that tight little ass of yours sometime."
            "She chuckles."
            the_person "Honestly? I think I wouldn't mind. With you I think it might even be good."
            $ the_person.increase_opinion_score("anal sex")
            "Sound like you made an impression on her! She may be more open to anal sex in the future."
    elif the_person.opinion_score_anal_sex() == -2:
        the_person "Your fingers felt nice, but when you pushed one into my ass... I don't know..."
        the_person "Honestly, I usually hate butt stuff..."
        mc.name "Usually?"
        the_person "Yeah... it felt really good this time though."
        mc.name "We should toy around with it again sometime. You never know what we might discover together."
        the_person "Ahh... I guess... yeah I might be up for that."
        $ the_person.increase_opinion_score("being fingered")
        $ the_person.increase_opinion_score("anal sex")
        "You can tell that you have made an impression on her. She may be more receptive to being fingered by you and anal activity in the future!"
    else:
        the_person "Damn that was good. You are so good with your hands too."
        the_person "I umm... even like it at the end, when you played with my butt..."
        mc.name "Yeah? I think most women enjoy butt stuff too, but many are just too afraid to experiment with it."
        the_person "Yeah, I think you might be right. I think I'd like to try more experimenting sometime."
        mc.name "Well I would be glad to help!"
        $ the_person.increase_opinion_score("being fingered")
        $ the_person.increase_opinion_score("anal sex")
        "You can tell that you have made an impression on her. She may be more receptive to being fingered by you and anal activity in the future!"

    "You get and wash up a bit in the sink as she lays back and recovers."
    return

label serum_tester_fuck_aid_label(the_person):
    if the_person.outfit.full_access():
        "[the_person.title] scoots to the edge of the medical bed and spreads her legs for you as you walk over to her."
    else:
        "[the_person.title] gets naked as you walk over to her."
        $ scene_manager.strip_full_outfit(the_person)
        "She scoots to the edge of the medical and spreads her legs for you."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "Her entire body is on full display for you. She looks up at you and smirks."
    $ mc.change_locked_clarity(30)
    the_person "Are you just going to look?"
    mc.name "For a moment longer. Don't worry, you'll get my cock in a moment."
    "She smiles shyly but doesn't move to cover herself up from your gaze."
    "Feeling ready, you take off your clothes. She gasps when your cock springs free."
    the_person "Fuck, what a monster..."
    if the_person.opinion_score_vaginal_sex() == -2:
        the_person "On second thought... I'm not sure that thing is going to fit... maybe we should..."
        mc.name "Nonsense. Don't you worry, we'll take this nice and slow."
        the_person "Ummm, I don't know I... I..."
        mc.name "Shhh..."
        "You put a finger to her lips."
        mc.name "Don't worry. Trust me."
        "Her protests stop, and she nods."
        the_person "Okay... I trust you."
    elif the_person.opinion_score_vaginal_sex() == 2:
        the_person "That thing is going to feel so good. Mmm I can't wait to feel it!"
        $ mc.change_locked_clarity(30)
    else:
        the_person "Are you sure that thing is going to fit?"
        mc.name "Of course. It is biology, your cunt was made to take my cock."
        the_person "Okay... I trust you."
    "You run your fingers along her slit a few times. You consider though."
    "Maybe you should wear a condom? In a clinical setting like this, it might be smart."
    "On the other hand, since she is under the effects of your serums, it might be a good chance to push her boundaries some."
    #In most cases the girl forces condom usage at the start of the session, but MC have opportunities to remove it during sex
    $ mc_condom_desire = False
    $ cum_goal = None
    menu:
        "Put on a condom":
            $ mc_condom_desire = True
            $ mc.condom = True
            mc.name "Hang on, I'm going to put a condom on."
            if the_person.opinion_score_bareback_sex() == -2:
                the_person "Good! I was about to tell you to wrap that thing up."
            elif the_person.opinion_score_bareback_sex() == 2:
                the_person "What? Why? Surely we don't need one of those!"
                mc.name "We need to. The data we get could be skewed if you get exposed to my cum or pre-cum."
                the_person "But... why can't why... like..."
                "She tries to come up with some way around it, but can't."
                the_person "Fine..."
            else:
                the_person "Okay, that is probably for the best, anyway..."
            "You quickly slip the condom on."
        "Try to go bareback":
            $ mc.condom = False
            mc.name "Alright, are you ready?"
            if the_person.opinion_score_bareback_sex() == -2:
                the_person "Whoa! Not yet! You need to wrap that thing up first!"
                mc.name "You mean like, wear a condom?"
                the_person "Of course!"
                mc.name "I can't, it might skew the data if you are exposed to latex."
                the_person "Latex? Really? No way. Wrap it up, or we're done."
                "You relent."
                mc.name "Fine. Give me a second."
                "You quickly grab a condom and slip it on."
                $ mc.condom = True
            elif the_person.opinion_score_bareback_sex() == 2:
                the_person "Mmm, totally! Put it in raw, it feels best that way anyway!"
                "Thankfully she seems into it. This seems like a good opportunity to push her limits a bit..."
                "You suppose you could try and get her to let you cum wherever you want... should you push for a creampie? Or to cover her with it?"
                menu:
                    "Try to creampie her":
                        "You don't say anything to her for now, but you decide to try and fill her up with your cum."
                        $ cum_goal = "creampie"
                    "Try to cover her in cum":
                        "You don't say anything to her for now, but you decide to try and cover her with your cum."
                        $ cum_goal = "cover"
            else:
                the_person "Wait, shouldn't you like... wear a condom or something?"
                mc.name "I can't, it might skew the data if you are exposed to latex."
                the_person "The latex? Seriously?"
                "She seems unconvinced."
                the_person "I don't think I want to do that... can you please just wrap it up?"
                "You relent."
                mc.name "Fine. Give me a second."
                "You quickly grab a condom and slip it on."
                $ mc.condom = True
    mc.name "Alright, here we go."
    $ condom_descrption = "raw"
    if mc.condom:
        $ condom_descrption = "gloved"
    "You put your hands on her hips and pull her to the edge of the medical bed. Her feet go up over your shoulders."
    "You put your hand on your [condom_descrption] cock, lining it up with her cunt, then slowly start to push it inside of her."
    if the_person.arousal < 25:
        "[the_person.possessive_title]'s pussy takes several seconds to penetrate. Her arousal is just starting to build, and you don't want to push things too fast."
        the_person "Ahh... go slow, I need to get warmed up!"
        "You oblige. You give her incredible slow, shallow strokes, but push yourself just a tiny bit deeper with each one."
        "After several strokes, you finally feel yourself push all the way in. You leave your hips in place, finally fully inside of her."

    elif the_person.arousal < 50:
        "[the_person.possessive_title]'s pussy takes a few seconds to penetrate, but you are able to slide in with minimal resistance."
        "She is clearly already a bit aroused, making it easier for you to slide in."
        "Once your are fully inside of her, you stop and enjoy the feeling of having her hot cunt wrapped around your [condom_descrption] dick."
    else:
        "[the_person.possessive_title]'s pussy gives zero resistance as you easily slide in all the way to the hilt."
        "Her pussy is soaking wet, clearly already aroused and ready for action. She moans when you bottom out."
        the_person "Fuck, you are so big... It feels amazing..."
        "You let yourself enjoy her sopping wet cunt for a few moments before you begin to fuck her."
    $ mc.change_locked_clarity(50)

    if the_person.arousal >= 100:
        "As you start to move your hips, [the_person.title] gasps and immediately begins to cry out."
        the_person "Oh fuck! [the_person.mc_title] I'm sorry, I'm... I'm gonna cum!"
        "Wow, she must have been really pent up! She is getting ready to orgasm already!"
        "You don't waste any time. You grab her hips with both hands and start to fuck her as hard as you can."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)

    if the_person.arousal < 20:
        the_person "Ah... you feel so big."
        "Her body is starting to respond to you. You make sure to take it nice and slow, enjoying the feeling of her cunt slowly getting wetter for you."
        the_person "Mmm yeah... that's it..."
        "She closes her eyes and concentrates on her feelings as her body gets aroused."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal < 40:
        "Sensing she is ready, you put your hands on her hips and increase the pace. You hips impact her ass with the sound of a satisfying slaps."
        the_person "Oh [the_person.mc_title]..."
        #If she hates vaginal sex, we focus only on making it as pleasureable as possible for her.
        if the_person.opinion_score_vaginal_sex() == -2:
            "You know that [the_person.possessive_title] normally hates vaginal sex, so you focus on making this as pleasurable as possible for her."
            if the_person.has_large_tits():
                "Her big tits are wobbling enticingly with each thrust. You let go of her hip with one hand and grope one while you fuck her."
            else:
                "Her perky tits shimy slightly with each thrust. You let go of her hip with one hand and grope her while you fuck her."
            the_person "That's nice... mmm..."
        # Otherwise, we can try and push her other limits...
        else:
            if mc.condom and not mc_condom_desire:
                "You are enjoying yourself, but the condom is limiting your pleasure some."
                "Now that you've started, you wonder if you could convince her to let you take it off and fuck her raw..."
                mc.name "Feels amazing, doesn't it?"
                the_person "Yeah..."
                mc.name "You know what would feel even better? If I took that dumb condom off and felt your skin on mine."
                if the_person.opinion_score_bareback_sex() == -2:   #She refuses
                    the_person "No. I know you want to do that but I don't. Leave it on... please?"
                    "She still sounds pretty against it... but by her tone, she might be more willing to go bare when she gets closer to cumming."
                elif the_person.opinion_score_bareback_sex() == 1:  #She accepts
                    the_person "That would feel good... Oh fuck, okay!"
                    "You grab her ankles with your hands and spread her wide open. You pull out and she reaches down and grabs your gloved cock."
                    "She quickly pulls your condom off, then throws it to the side."
                    "She lines you up with her needy hole and you slide inside her, completely bare this time."
                    $ condom_descrption = "raw"
                    $ mc.condom = False
                    $ mc.change_locked_clarity(100)
                    the_person "Oh fuck! You're right..."
                    "It is incredible how hot it is without the stupid condom in the way. You put her legs over your shoulders again and start to fuck her."
                else:
                    "She looks troubled."
                    the_person "I... I don't know... Can you leave it on? I just... I'm not sure..."
                    mc.name "Okay."
                    "She is definitely on the fence now. You bet if you can get her closer to orgasm she will be willing to go for it!"
            elif mc.condom:
                if the_person.opinion_score_bareback_sex() >= 1:
                    the_person "Hang on... I... I want to ask you something."
                    "You stop for a moment. She spreads her legs wide."
                    the_person "Can I... take it off?"
                    mc.name "Take what off? You're already naked."
                    the_person "The condom... I want to feel you... raw!"
                    menu:
                        "Let her take it off":
                            mc.name "I guess, if you really want it that bad."
                            the_person "I do!!!"
                            "You pull out of her. She eagerly reaches down and pulls your condom off, throwing it to the side."
                            "She lines you up with her needy hole and you slide inside her, completely bare this time."
                            $ condom_descrption = "raw"
                            $ mc.condom = False
                            $ mc.change_locked_clarity(100)
                            mc.name "Oh fuck! You're so wet..."
                            "It is incredible how hot it is without the stupid condom in the way. You put her legs over your shoulders again and start to fuck her."
                        "Refuse":
                            mc.name "I'm sorry. The condom stays on."
                            "She whimpers a response, but you can't make it out, since you've already started fucking her again."
                else:
                    "[the_person.title] is really getting into this. You decide to do a little dirty talk."
                    mc.name "Your slutty hole feels so good. I bet we both cum."
                    the_person "Mmm, I hope! It's nice not having to worry about where you finish..."
            else:   #You aren't wearing a condom, which means she must already love bareback sex. Test her limits on cum
                if cum_goal == "creampie":
                    mc.name "Fuck your cunt feels so good. I can't wait to fill you up with my cum."
                    if the_person.opinion_score_creampies() == -2:
                        the_person "Wh... What? No, you can't do that!"
                        mc.name "Why not? It feels amazing, for both of us."
                        the_person "No it doesn't. It make a big mess and leaks out the rest of the day..."
                        mc.name "Exactly."
                        "She doesn't seem convinced, but quiets down."
                        the_person "I... don't know... maybe just once..."
                    elif the_person.opinion_score_creampies() == 2:
                        the_person "Mmm, do it! Fill me up with your hot, sticky cum!"
                        the_person "I want to feel it inside me the rest of the day!"
                        "Wow, she seems really into it."
                    else:
                        the_person "I... I guess it would be okay. Just this once..."
                        mc.name "Okay? It'd be more than okay. It is fucking hot to get creampied, isn't it?"
                        mc.name "Admit it, you can't wait to feel my cock explode inside you, coating your insides with hot cum."
                        "She moans as you fuck her and talk dirty to her."
                        the_person "That does sound nice... Maybe just this once!"
                else:
                    mc.name "God your cunt feels amazing. I bet we both cum. I'm going to pull out and cover you in my cum!"
                    if the_person.opinion_score_being_covered_in_cum() == -2:
                        the_person "What? Don't do that... that's gross!"
                        mc.name "Why not? Where else am I supposed to cum? Do you want me to cum inside of you?"
                        if the_person.opinion_score_creampies() == -2:
                            the_person "No! I just... why can't you just... cum on the table or something?"
                            mc.name "Wow, really? No, I can't. If you want this dick, you gotta handle the finish too."
                            "She sighs, but relents."
                            the_person "Fine... just this once I guess."
                        elif the_person.opinion_score_creampies() == 2:
                            the_person "Yeah! Put that hot cum of yours right where it belongs! Deep in my hungry cunt!"
                            "Damn, seems she's more interested in gettied creampied. Maybe you should consider cumming inside of her instead?"
                            menu:
                                "Plan to creampie her":
                                    mc.name "Wow, you want it in your needy hole huh? Okay fine, I'll fill you up then."
                                    $ cum_goal = "creampie"
                                    the_person "Mmm, yesss..."
                                "Plan cover her in cum":
                                    mc.name "No way, I can't risk that, it'll skew the data collection."
                                    $ cum_goal = "cover"
                                    "She sighs, but relents."
                                    the_person "Ahhh, fine, do what you want I guess..."
                        else:
                            the_person "Ahh, no, I guess not..."
                            "She sighs, but relents."
                            the_person "Fine... just this once I guess."
                    elif the_person.opinion_score_being_covered_in_cum() == 2:
                        the_person "Oh fuck, do it! Pull out and cover in me in your sticky seed!"
                        the_person "I love it when it splashes all over my skin!"
                        "Damn, she seems into that too!"
            "You grab her hips and keep pounding her. The sounds of her moans and your hips slapping against each other fill the room."

        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal < 60:
        the_person "Ahhh... Mmmm..."
        "[the_person.possessive_title] moans grow more eager."
        "You wrap your arms around her legs and pull her ass a little further off the edge of the examination bed."
        "The higher penetration angle makes her moan even louder, and by closing her legs together and putter her feet over your shoulders, her pussy grips your [condom_descrption] cock even tighter."
        the_person "Oh my god... fuck me [the_person.mc_title]!"
        "You oblige her. You hips are moving at an urgent pace."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
        $ mc.change_arousal(20)
    if the_person.arousal < 80:
        the_person "Oh fuck! Mmm... that is so good! I'm getting so close!"
        "[the_person.title]'s whole body is quivering as you pound her."
        if the_person.opinion_score_vaginal_sex() == -2:
            "She really seems to be enjoying herself. You are positive you'll be able to get her off if you keep at it."
            if the_person.has_large_tits():
                "Her big tits are bouncing wildly now as you pound her. You seem to be on the edge of orgasming together."
            else:
                "Her perky tits shimy with every thrust. You can't wait to orgasm together with her."
            the_person "I can't believe how good it feels... oh [the_person.mc_title] don't stop!"
        # Otherwise, we can try and push her other limits...
        else:
            if mc.condom and not mc_condom_desire:
                "It's time to make a move. You decide now is the time to push your luck."
                mc.name "I need to take this stupid condom off. I want to feel it when you quiver and cum all over my cock!"
                mc.name "Don't you want to feel that too?"
                if the_person.opinion_score_bareback_sex() == -2:
                    the_person "I... I guess... you make it sound like a religious experience or something."
                    "You spread her legs wide with your hands and pull out."
                    mc.name "Take it off. I need to feel your pussy wrapped around me!"
                    the_person "Okay..."
                    if the_person.opinion_score_creampies() == -2:
                        the_person "Just promise me you'll pull out when you cum... okay?"
                        mc.name "Alright, I promise."
                        "You probably better not go back on that one, you don't want to push her too far past her usual limits..."
                        $ cum_goal = "cover"
                    elif the_person.opinion_score_creampies() == 2:
                        the_person "Just promise me you'll finish inside of me, okay?"
                        mc.name "Inside you? You don't want me to pull out?"
                        the_person "No. If we're going to do this, I want to get the full experience!"
                        mc.name "Okay..."
                        "You probably better not go back on that one, you don't want to push her too far past her usual limits..."
                        $ cum_goal = "creampie"
                    "She reaches down between your legs and pulls the condom off, throwing it to the side."
                    "She takes your cock in her hand, then points it back at her cunt, taking a deep breath."
                else:  #She accepts
                    the_person "That would feel good... Oh fuck, okay! Let me get it!"
                    "You grab her ankles with your hands and spread her wide open. You pull out and she reaches down and grabs your gloved cock."
                    "She quickly pulls your condom off, then throws it to the side."
                "You slide back inside her, completely bare. You grit your teeth to keep from cumming immediately."
                $ condom_descrption = "raw"
                $ mc.condom = False
                $ mc.change_locked_clarity(100)
                the_person "Oh fuck! You're right... That's amazing!!! I can feel everything... Oh my god!"
                $ the_person.increase_opinion_score("bareback sex")
                "It is incredible how hot it is without the stupid condom in the way, and she seems to agree."
                "You put her legs over your shoulders again and continue to fuck her."
            elif mc.condom:
                if the_person.opinion_score_bareback_sex() >= 1:
                    the_person "Please! I need you take that stupid thing off!"
                    mc.name "The condom?"
                    the_person "Yes! I want to feel your skin! I want to feel every vein and ridge... not some stupid piece of latex!"
                    "Damn, she is really getting desperate."
                    menu:
                        "Let her take it off":
                            mc.name "I guess, if you really want it that bad."
                            the_person "I do!!!"
                            "You pull out of her. She eagerly reaches down and pulls your condom off, throwing it to the side."
                            "She lines you up with her needy hole and you slide inside her, completely bare this time."
                            $ condom_descrption = "raw"
                            $ mc.condom = False
                            $ mc.change_locked_clarity(100)
                            mc.name "Oh fuck! You're so wet..."
                            $ the_person.increase_opinion_score("bareback sex")
                            "It is incredible how hot it is without the stupid condom in the way. You put her legs over your shoulders again and continue to fuck her."
                        "Refuse":
                            mc.name "No. The condom stays on. You need to learn to submit to your partner when they are fucking you like this."
                            "She whimpers a response, but you can't make it out, since you've already started fucking her again."
                            $ the_person.increase_opinion_score("being submissive")
                else:
                    mc.name "Your body is amazing. We should fuck more often."
                    the_person "Mmm, you make me feel so good... I'm not sure I could say no to you... if I even try to!"
                    if the_person.has_large_tits():
                        "Her big tits are bouncing wildly now as you pound her. You seem to be on the edge of orgasming together."
                    else:
                        "Her perky tits shimy with every thrust. You can't wait to orgasm together with her."
            else:
                mc.name "Of fuck I'm getting so close. You are too, aren't you?"
                the_person "Yes! I'm gonna cum all over your big cock!"
                if cum_goal == "creampie":
                    mc.name "I'm gonna push it deep and cum inside you as deep as possible. I'm gonna fill you to the brim with my seed!"
                    if the_person.opinion_score_creampies() == -2:
                        the_person "Oh god, I must be crazy... I think I want it!"
                        mc.name "Of course you want it. It's the most natural thing in the world, to get your pussy loaded with semend!"
                        "She doesn't respond, but seems to be getting into it. You seem to have convinced her!"
                    else:
                        the_person "Yes! Cum inside me and fill me up with cum like the little slut I am!"
                        the_person "I want you shoot it so deep it is still inside me when I go to bed tonight!"
                        "She moans and gasps as you push her closer and closer to orgasm."
                else:
                    mc.name "You want me to pull out and cover in my cum, don't you?"
                    if the_person.opinion_score_being_covered_in_cum() == -2:
                        the_person "I can't believe I'm saying this... but I think I do!"
                        the_person "You cock makes me feel so good... I want to wear your cum too!"
                        mc.name "Oh fuck, you're going to look so hot covered in my sticky seed!"
                        "You seem to have convinced her to take your cumshot."
                    else:
                        the_person "Yes! Pull out and cover me in your wonderful seed!"
                        the_person "That cock makes me feel so good, I can't wait to feel it cover me!"
                if the_person.has_large_tits():
                    "Her big tits are bouncing wildly now as you pound her. You are on the edge of orgasming together."
                else:
                    "Her perky tits shimy with every thrust. You can't wait to orgasm together with her."
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal < 100:
        "[the_person.possessive_title] moans and writhes. She tries to move her hips in time with you, but you are basically picking her up now as you bang her mercilessly."
        the_person "[the_person.mc_title]... [the_person.mc_title]! I'm so close... Oh fuck me baby!"
        "She is right on the edge. You dig deep and somehow manage to fuck her even harder."
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    the_person "Yes! Oh YES! Fuck me!!!"
    $ the_person.have_orgasm(force_trance = True)
    "[the_person.title]'s breathing stops as she cums. Her whole body trembles as she begins to orgasm."
    if the_person.event_triggers_dict.get("squirts", False) == True:
        "Her pussy squirts fluid as she cums. She cries out incoherently as she loses control of her body."
    "Her pussy quivers and grasps at your [condom_descrption] cock, as if begging it to release your cum with her."
    $ mc.change_arousal(20)
    menu:
        "Cum":
            $ mc.change_locked_clarity(50)
            "Feeling her pussy quiver and cum all over your cock is too much. You let yourself go and get ready to finish."
            mc.name "Oh fuck... I'm gonna cum too!"
            if mc.condom:
                "Knowing you've got protection on, you push yourself deep and cum inside of her."
                "The condom swells and accepts your load as you pump it out."
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
                "When you finish, you slowly let go of her legs, setting her down on the examination table."
                "You pull the condom off and throw it in the trash."
            elif cum_goal == "creampie":
                "With your arms wrapped around her legs and her ass several inches off the examination bed, you begin to dump your seed inside of her."
                "Even if she wanted to, there's nothing she could do about it now. She has zero leverage and is barely hanging on to the bed."
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
                $ the_person.cum_in_vagina()
                $ scene_manager.update_actor(the_person, position = "missionary")
                "In the midst of her own orgasm, she just moans as you fill her up with your cum."
                if the_person.opinion_score_creampies() == -2:
                    the_person "Oh my god... I really just let you... it's sooo gooooood!"
                    "When you finally finish, you leave your cock anchored deep inside of her as it will go."
                    mc.name "Fuck, that was incredible. Wasn't it amazing to get filled up like that?"
                    the_person "I... I guess it was..."
                    mc.name "This is just the start. You're going to learn to love it."
                    the_person "I suppose we could try it again sometime..."
                    $ the_person.increase_opinion_score("creampies")
                    "You definitely seem to have shifted her opinion on getting creampied!"
                elif the_person.opinion_score_creampies() == 2:
                    the_person "Yes! Oh fuck keep it deep!"
                    "You feel her hand grab your hip as she tries to pull you even deeper."
                    mc.name "Fuck, your needy cunt is so good. Take it you little slut!"
                    the_person "I am! Oh [the_person.mc_title] give it to me!"
                    "When you finally finish, you leave your cock anchored deep inside of her as it will go."
                    the_person "Oh fuck... that was amazing..."
                else:
                    the_person "Oh my god! I can feel it! I can feel your cum splashing inside of me!"
                    "Her face is blissful as you fill her up. She is really loving it."
                    "When you finally finish, you leave your cock anchored deep inside of her as it will go."
                    the_person "I didn't know it could feel so good! That was incredible!"
                    mc.name "This is just the start. You're going to learn to love it."
                    the_person "I already do! maybe you should just cum inside me everytime from now on..."
                    $ the_person.increase_opinion_score("creampies")
                    "You definitely seem to have shifted her opinion on getting creampied!"
            else:
                "At the last possible second, you set her ass down on the examination bed and pull out."
                "You spread her legs with your hands and she quickly reaches down and strokes your cock, finishing you off."
                mc.name "Oh fuck, here it comes!"
                $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
                $ the_person.cum_on_stomach()
                $ scene_manager.update_actor(the_person, position = "missionary")
                "Her soft hands stroke you off as you finish. You fire off spurt after spurt of cum all over her stomach."
                "She moans with you, finishing the last of her orgasms as you finish yours."
                "When you finish, you look down at [the_person.title], covered in your semen."
                if the_person.opinion_score_being_covered_in_cum() == -2:
                    the_person "Oh my god... it's everywhere..."
                    mc.name "I know. Damn you look amazing."
                    "She chuckles."
                    the_person "I do... don't I?"
                    mc.name "Getting covered in cum isn't as bad as you thought, is it?"
                    the_person "I guess not. I helps that I came so hard though."
                    $ the_person.increase_opinion_score("being covered in cum")
                    "Sounds like she is coming around on the idea of being covered in your cum."
                elif the_person.opinion_score_being_covered_in_cum() == 2:
                    the_person "Oh fuck its so hot... mmmm I love it!"
                    "[the_person.title] runs a finger through your cum, then brings it to her mouth."
                    the_person "Do I look good? Covered in your wonderful cum?"
                    mc.name "Yeah, that is really hot."
                    the_person "Mmm, I just want to lay back for a bit and enjoy this."
                else:
                    the_person "Oh my god! It's so hot... oh my!"
                    mc.name "You look amazing covered in my cum [the_person.title]."
                    the_person "Mmm, I FEEL amazing..."
                    mc.name "Run your fingers through it and play with it."
                    the_person "Mmm... okay..."
                    "She slowly slides her fingers through a pool of cum that is gathering on her belly, spreading it around her soft skin."
                    the_person "Oh fuck... I could get used to this..."
                    $ the_person.increase_opinion_score("being covered in cum")
                    "Sounds like she is really getting off on being covered in your cum!."

        "Keep yourself from cumming" if mc.arousal < 100 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
            "Somehow, against all odds, you dig deep and keep yourself from cumming."
            "Besides, it might invalidate the test results to cum all over her."
        "Keep yourself from cumming\n{color=#ff0000}{size=18}Too aroused{/size}{/color} (disabled)" if mc.arousal > 100 and not perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
            pass

    if the_person.opinion_score_vaginal_sex() == -2:
        the_person "That was incredible... I can't believe I came like that. I never do!"
        mc.name "Seems to me like maybe you just needed to find the right dick."
        the_person "Hmm... you might be right..."
        mc.name "We should probably do it again sometime. Just to find out."
        "She chuckles"
        the_person "We might have to."
        $ the_person.increase_opinion_score("vaginal sex")
        "[the_person.title] seems to have warmed up on the idea of vaginal sex in the future!"
    elif the_person.opinion_score_vaginal_sex() == 2:
        the_person "There's nothing quiet as amazing as a good fuck, is there?"
        mc.name "No, I don't think there is."
        the_person "Mmm, hopefully we can do this again soon."
    else:
        the_person "Wow... that was so intense. I always knew sex was good, but that was... AMAZING."
        mc.name "That's happens when a man who knows how to use his dick has his way with you."
        the_person "I think you're right. Wow..."
        $ the_person.increase_opinion_score("vaginal sex")
        "[the_person.title] seems to have warmed up on the idea of vaginal sex in the future!"

    "You step away and clean up a bit as she lays back and recovers."
    return
