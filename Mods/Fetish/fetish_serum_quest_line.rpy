init 2 python:
    def fetish_serum_quest_intro_requirement():
        if day > 14 and time_of_day == 2:
            if mc.is_at_work() and mc.business.head_researcher:
                return True
        return False

    def fetish_serum_quest_intro_followup_requirement():
        if time_of_day == 1 and day%7 == 0:
            if mc.is_at_work():
                return True
        return False

    def fetish_serum_discuss_requirement(the_person):
        if mc.is_at_work() and fetish_serum_unlock_count() > 0:
            return True
        return False

    def fetish_serum_exhibition_requirement():
        if time_of_day == 1 and day%7 == 0:
            if mc.is_at_work():
                return True
        return False

    def fetish_serum_anal_requirement():
        if time_of_day == 1 and day%7 == 0:
            if mc.is_at_work():
                return True
        return False

    def fetish_serum_cum_requirement():
        if time_of_day == 1 and day%7 == 0:
            if mc.is_at_work():
                return True
        return False

    def fetish_serum_breeding_requirement():
        if time_of_day == 1 and day%7 == 0:
            if mc.is_at_work():
                return True
        return False

    def fetish_serum_research_in_progress():
        return mc.business.event_triggers_dict.get("fetish_serum_research_active", False)

    special_fetish_outfit = Outfit("A Special Night")
    special_fetish_outfit.add_upper(lace_bra.get_copy(),colour_pink)
    special_fetish_outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
    special_fetish_outfit.add_feet(high_heels.get_copy(), colour_pink)

    special_fetish_nude_outfit = Outfit("Nude")

init 3 python:
    fetish_serum_quest_intro = Action("Nanobot Discovery", fetish_serum_quest_intro_requirement, "fetish_serum_quest_intro_label")
    fetish_serum_quest_intro_followup = Action("Nanobot Discovery Followup", fetish_serum_quest_intro_followup_requirement, "fetish_serum_quest_intro_followup_label")
    fetish_serum_discuss = Action("Discuss Nanobot Programming", fetish_serum_discuss_requirement, "fetish_serum_discuss_label",
        menu_tooltip = "Discuss creation of new Nanobot programs.")
    fetish_serum_exhibition = Action("Exhibition Program", fetish_serum_exhibition_requirement, "fetish_serum_exhibition_label")
    fetish_serum_anal = Action("Anal Program", fetish_serum_anal_requirement, "fetish_serum_anal_label")
    fetish_serum_cum = Action("Cum Program", fetish_serum_cum_requirement, "fetish_serum_cum_label")
    fetish_serum_breeding = Action("Reproduction Program", fetish_serum_breeding_requirement, "fetish_serum_breeding_label")

label fetish_serum_quest_intro_label():
    $ the_person = mc.business.head_researcher
    "As you are getting ready to sit down for some lunch, your head researcher messages you."
    the_person "Hey, I just got a lead on some new technology that I think would be beneficial. Can I swing by?"
    mc.name "Sure, I'm just sitting down to some lunch, I'm in the office."
    $ the_person.draw_person()
    "A few minutes later, [the_person.title] is standing at your door."
    the_person "Hey [the_person.mc_title]. Mind if I sit down?"
    mc.name "Go ahead."
    $ the_person.draw_person(position = "sitting")
    the_person "Well, I just got off the phone with an old friend. Nerdy guy I kinda had a thing with at the university before I met you."
    the_person "He has been posting a bunch of stuff on Facebook about his work in robotics, and something he posted caught my eye."
    mc.name "Oh?"
    the_person "Yeah, basically, they've managed to make small robot nano bots that are designed to administer drugs in microdoses to specific places in the body."
    mc.name "How could this technology help us?"
    the_person "If we program the nanobots to deliver targeted doses of endorphins and combined them with our suggestability serums, it could change someone's opinions, depending on how we program the bots."
    "You consider briefly the implications of how this technology could help your business. Maybe you could have the bots help girls be more accepting of sexual acts?"
    mc.name "Is this something you would be able to program?"
    "[the_person.possessive_title] shakes her head."
    the_person "No... but ummm, this friend of mine kind of owes me a favor. I was thinking about paying him a visit this weekend. He still lives locally."
    mc.name "Hmm, maybe you could make some kind of deal with him... supply us with these bots? Then maybe set up a basic program we can use for our initial batches."
    mc.name "Eventually we could design new programs, but for initial testing, we could keep it basic."
    the_person "That sounds like a good idea. I'll talk to him, maybe he would be willing to write us the first round of code. What kind of triggers should we put in the first round?"
    mc.name "Well, so far our research has been on making people more... open... to different experiences. Maybe we could base it on some basic sexual acts?"
    if the_person.sluttiness < 20:
        "[the_person.title] crinkles her nose at your suggestions."
        the_person "God, I swear men only want one thing..."
        "She pauses to consider."
        the_person "Though I suppose it DOES make sense to go along with our other research goals."
    elif the_person.sluttiness < 60:
        the_person "That's a good idea. It aligns with our other research goals."
    else:
        the_person "Oh! Yeah we could start small, but if this works we could make people like all kinds of things!"
    mc.name "Exactly what I am thinking."
    "You spend some time going over the details with [the_person.title]. Eventually you have a plan in place."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "Alright, I'll check back with you next week!"
    $ mc.business.mandatory_crises_list.append(fetish_serum_quest_intro_followup)
    $ clear_scene()
    return

label fetish_serum_quest_intro_followup_label():
    $ the_person = mc.business.head_researcher
    $ fetish_unlock_basic_serum()
    if mc.location == mc.business.r_div:
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        "You get a text message from [the_person.possessive_title]"
        the_person "Hey! Meet me down in the lab!"
        "You hurry down to the lab."
        $ mc.business.r_div.show_background()
    $ the_person.draw_person()
    the_person "Guess what! I got the first set of those nano bots. He did me a favor and spent all weekend coding the program for our first batch!"
    "You look at her desk. There is a small container filled with what appears to be a silver liquid."
    the_person "All we have to do is added a little bit to a serum, set the program, and it should be good to go!"
    the_person "However, he did give me a warning. He said this tech is still technically top secret, so we absolutely CANNOT advertise what's in it or how they work."
    mc.name "Can we still sell the completed serum?"
    the_person "Yes, but we aren't allowed to tell anyone that they are in it. Kinda shady, but I understand where he is coming from."
    the_person "We'll need to design new serums with the bots, but it shouldn't be particularly difficult. They are basic to add."
    mc.name "Sounds great. We should make sure we observe the effects of these bots as well, to make sure they are effective."
    the_person "Okay! This is exciting stuff!"
    "You have unlocked Sexual Proclivity Nanobots. These can be added to any serum design, and do not take up a trait slot. However, they do increase the production cost."
    "New versions of the nanobots can be unlocked after observing the results of this version. To advance, raise their mastery level to atleast 5.0"
    return

label fetish_serum_discuss_label(the_person):
    if get_fetish_basic_serum().mastery_level < 5.0:
        the_person "Unforunately, I feel like we still don't know enough about the nanobots to consider messing with their programming."
        mc.name "I understand. I'll make it a priority to observe their results more closely."
        "To unlock new nanobots, you need to raise the mastery level of Sexual Proclivity Nanobots to atleast 5.0"
    elif fetish_serum_research_in_progress():
        the_person "I already reached out to my contact. He is going to make a new program based on your specifications this weekend."
        mc.name "Excellent."
    elif fetish_serum_unlock_count() == 1:
        the_person "The nanobots have been working flawlessly, as far as our initial research can tell."
        mc.name "That is excellent news."
        the_person "I actually reached out to my previous contact, about the possibility of writing a new program for us."
        the_person "He has agreed to do it for us, but he is a little strapped for cash right now and has asked for a small payment."
        mc.name "How much?"
        the_person "He is asking for $500. He could have it done by the start of business on Monday."
        mc.name "Hmm..."
        if mc.business.funds < 500:
            "Unfortunately, you don't have the funds to commission this program right now."
            return
        "Do you want to commission a new nanobot program?"
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_01
        if _return:
            $ mc.business.funds += (-500)
        the_person "Anything else I can do for you today?"
    elif fetish_serum_unlock_count() == 2:
        mc.name "I want to discuss commissioning a new program for the nanobots."
        the_person "Hmm. Okay. Unfortunately, my contact told me that their current employer has been getting suspicious."
        the_person "Apparently, some nanobots were discovered where they shouldn't have been, and they are cracking down on access to the source code."
        the_person "He told me he could write us a new program, but he needs to secure some new equipment to do it safely."
        mc.name "How much for the new equipment?"
        the_person "He said $1500 should cover it, including his usual $500 fee."
        mc.name "Hmm..."
        if mc.business.funds < 1500:
            "Unfortunately, you don't have the funds to commission this program right now."
            return
        "Do you want to commission a new nanobot program?"
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_02
        if _return:
            $ mc.business.funds += (-1500)
        the_person "Anything else I can do for you today?"
    elif fetish_serum_unlock_count() == 3:
        mc.name "I want to discuss commissioning a new program for the nanobots."
        "[the_person.possessive_title] grimaces."
        the_person "I figured you might. However, my contact is starting to get spooked."
        the_person "His employer has instituted new measures for source code control. He's scared of getting caught and has significantly increased his commission price."
        mc.name "How much is he asking for?"
        the_person "He won't do it for less than $5000."
        mc.name "Hmm..."
        if mc.business.funds < 5000:
            "Unfortunately, you don't have the funds to commission this program right now."
            return
        "Do you want to commission a new nanobot program?"
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_03
        if _return:
            $ mc.business.funds += (-5000)
        the_person "Anything else I can do for you today?"
    elif fetish_serum_unlock_count() == 4:
        mc.name "I want to discuss commissioning a new program for the nanobots."
        "[the_person.possessive_title] grimaces."
        the_person "I figured you might. However, my contact has some troubling news."
        the_person "His employer has instituted a whitelist for people to get access to the new source code, and my contact isn't on the list."
        the_person "He says he could probably get access, but he needs a significant bribe for the security head."
        mc.name "How much is he asking for?"
        the_person "He won't do it for less than $15000."
        mc.name "Hmm..."
        if mc.business.funds < 15000:
            "Unfortunately, you don't have the funds to commission this program right now."
            return
        "Do you want to commission a new nanobot program?"
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_04
        if _return:
            $ mc.business.funds += (-15000)
        the_person "Anything else I can do for you today?"
    else:
        mc.name "I want to discuss commissioning a new program for the nanobots."
        "[the_person.possessive_title] grimaces."
        the_person "I'm sorry [the_person.mc_title]. My contact has made it clear that at this point they can't work on the program anymore, for any amount of money."
        mc.name "I see."
    return

label fetish_serum_unlock_choice_menu(the_person):
    menu:
        "Exhibitionist Program" if get_fetish_exhibition_serum().tier > 5:
            mc.name "I'd like to commission a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to have sexual activity in front of others."
            "In addition, it would make them more willing to show their body, even out in public."
            the_person "Alright, I'll make up a specification sheet and pass it along to him, along with the payment."
            $ mc.business.mandatory_crises_list.append(fetish_serum_exhibition)
        "Anal Program" if get_fetish_anal_serum().tier > 5:
            mc.name "I'd like to commission a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to have anal sexual activity and be submissive to their partner."
            the_person "Alright, I'll make up a specification sheet and pass it along to him, along with the payment."
            $ mc.business.mandatory_crises_list.append(fetish_serum_anal)
        "Semen Program" if get_fetish_cum_serum().tier > 5:
            mc.name "I'd like to commission a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person enjoy semen exposure."
            the_person "Alright, I'll make up a specification sheet and pass it along to him, along with the payment."
            $ mc.business.mandatory_crises_list.append(fetish_serum_cum)
        "Reproduction Program" if get_fetish_breeding_serum().tier > 5:
            mc.name "I'd like to commission a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to engage in reproduction and acts associated with it."
            the_person "Alright, I'll make up a specification sheet and pass it along to him, along with the payment."
            $ mc.business.mandatory_crises_list.append(fetish_serum_breeding)
        "No":
            mc.name "Not right now, but I'll keep this option in mind."
            return False
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = True
    return True

label fetish_serum_exhibition_label():
    $ the_person = mc.business.head_researcher
    $ fetish_unlock_exhibition_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.location == mc.business.r_div:
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        "You get a text message from [the_person.possessive_title]"
        the_person "Hey! I have details on the new program!"
        "You hurry down to the lab."
        $ mc.business.r_div.show_background()
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will be more willing to show their bodies in public, or commit sexual acts in front of others."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Social Sexual Proclivity Nanobots."
    return

label fetish_serum_anal_label():
    $ the_person = mc.business.head_researcher
    $ fetish_unlock_anal_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.location == mc.business.r_div:
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        "You get a text message from [the_person.possessive_title]"
        the_person "Hey! I have details on the new program!"
        "You hurry down to the lab."
        $ mc.business.r_div.show_background()
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will be more willing to commit acts of sodomy in submission to their partner."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Anal Sexual Proclivity Nanobots."
    return

label fetish_serum_cum_label():
    $ the_person = mc.business.head_researcher
    $ fetish_unlock_cum_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.location == mc.business.r_div:
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        "You get a text message from [the_person.possessive_title]"
        the_person "Hey! I have details on the new program!"
        "You hurry down to the lab."
        $ mc.business.r_div.show_background()
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will have positive reactions to exposure to semen."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Semen Proclivity Nanobots."
    return

label fetish_serum_breeding_label():
    $ the_person = mc.business.head_researcher
    $ fetish_unlock_breeding_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.location == mc.business.r_div:
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        "You get a text message from [the_person.possessive_title]"
        the_person "Hey! I have details on the new program!"
        "You hurry down to the lab."
        $ mc.business.r_div.show_background()
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will have positive reactions to exposure to reproducing and other associated body functions, such as lactation."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Reproduction Proclivity Nanobots."
    return
