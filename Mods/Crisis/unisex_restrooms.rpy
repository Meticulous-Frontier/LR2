#This is a crisis series for changing company restrooms to unisex. As the girls in the company get sluttier and sluttier, the crisis changes to reflect the corrupted nature.
#At first, you may only over hear conversations. Then girls talking about sexual fantasies, then gloryhole options.

init -1 python:
    unisex_restroom_mod_weight = 8

init 1301 python:

    def unisex_bathroom_creation_requirement():
        if mc.business.unisex_restroom_unlocks.get("unisex_policy_avail",0) == 1:
            return True
        return False

    def unisex_bathroom_policy_unlock(unlock):
        mc.business.unisex_restroom_unlocks["unisex_policy_unlock"] = unlock

    Unisex_bathroom_creation_policy = Policy(name = "Make Restrooms Unisex",
        desc = "Some basic remodeling and a change of signs will make all company restrooms unisex.",
        cost = 1000,
        requirement =  unisex_bathroom_creation_requirement,
        on_buy_function = unisex_bathroom_policy_unlock,
        extra_arguments = { "unlock" : 1})
    organisation_policies_list.append(Unisex_bathroom_creation_policy)

    def unisex_restroom_fantasy_actout_requirement(the_person):
        if mc.business.is_open_for_business(): #Only trigger if people are in the office.
            if mc.is_at_work(): #Check to see if the main character is at work
                return True
        return False

    def unisex_restroom_gloryhole_wait_requirement():
        if mc.business.is_open_for_business():
            if __builtin__.len(mc.business.get_employee_list()) > 3:
                return True
            else:
                return "You should hire more employees"
        else:
            return "The business isn't open!"
        return False

    unisex_restroom_fantasy_actout = Action("Actout dream fantasy", unisex_restroom_fantasy_actout_requirement, "unisex_restroom_fantasy_actout_label", event_duration = 5)
    unisex_restroom_gloryhole_wait = Action("Wait by the glory hole", unisex_restroom_gloryhole_wait_requirement, "unisex_restroom_gloryhole_wait_label")

init 2 python:
    def unisex_restroom_crisis_requirement():
        if __builtin__.len(mc.business.get_employee_list()) > 5: #Have at least 6 employees.
            if mc.business.is_open_for_business(): #Only trigger if people are in the office.
                if mc.is_at_work(): #Check to see if the main character is at work
                    return True
        return False

    def gloryhole_get_response(person):    #this function creates a weight list of possible outcomes for the glory hole responses.
        gloryhole_list = []
        if person.sluttiness < 20: #They get pissed and refuse to do anything
            gloryhole_list.append("Refuse")
        else:
            gloryhole_list.append("Handjob")
            # actions based on sluttiness
            if person.sluttiness > 35:
                gloryhole_list.append("Blowjob")
            if person.sluttiness > 60:
                gloryhole_list.append("Vaginal")
                gloryhole_list.append("JoinMe")
            if person.sluttiness > 85:
                gloryhole_list.append("Anal")


        # actions based on fetishes (will always be added regardless of sluttiness)
        if person.has_role(cum_internal_role) or person.has_role(cum_external_role):
            gloryhole_list.append("Blowjob")
        if person.has_role(vaginal_fetish_role):
            gloryhole_list.append("Vaginal")
        if person.has_role(anal_fetish_role):
            gloryhole_list.append("Anal")

        return get_random_from_list(gloryhole_list)

    def get_anon_person(person):        #This function returns an anonymous version of a character.
        anon_person = person.char.copy()
        anon_person.name = "?????"

        return anon_person

    unisex_restroom_crisis_action = ActionMod("Unisex Restroom", unisex_restroom_crisis_requirement,"unisex_restroom_action_label",
        menu_tooltip = "Change company restrooms the unisex and enjoy the results.", category="Business", is_crisis = True, crisis_weight = unisex_restroom_mod_weight)

label unisex_restroom_action_label():
    if mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0) == 0:  #unisex restroom not yet created. Go to suggestion label
        call unisex_restroom_overhear_label() from _call_unisex_restroom_over_call_1
        return

    if mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0) < 6:
        $ ran_num = mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0)
        $ unisex_bathroom_policy_unlock(ran_num + 1)
    else:
        $ ran_num = renpy.random.randint(1, mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0))

    if ran_num == 1:
        call unisex_restroom_door_greet_label() from _call_unisex_restroom_greet_call_1
    if ran_num == 2:
        call unisex_restroom_sexy_overhear_label() from _call_unisex_restroom_over_call_2
    if ran_num == 3:
        call unisex_restroom_fantasy_overhear_label() from _call_unisex_restroom_over_call_3
    if ran_num >= 4:
        if mc.business.unisex_restroom_unlocks.get("unisex_restroom_gloryhole", 0) == 0:  #If not already, unlock the glory hole
            call unisex_restroom_unlock_gloryhole_label() from _call_unisex_restroom_gloryhole_unlock_1
        else:
            call unisex_restroom_gloryhole_option_label() from _call_unisex_restroom_gloryhole_option_1

    return

label unisex_restroom_overhear_label():
    "You get up from your work. There is a problem you are having trouble figuring out, so you take a quick walk down the hall to clear your mind a bit."
    if __builtin__.len(mc.business.production_team) > 0:
        $ the_person = get_random_from_list(mc.business.production_team)
    else:
        $ the_person = get_random_from_list(mc.business.get_employee_list())
    "As you pass by the break room, you happen to hear one of your employees complaining to someone else."
    if the_person in mc.business.production_team:
        if the_person.relationship == "Single":
            the_person.char "So I went out with this guy the other day I met on Tinder and we had some lunch together. It went okay, but we got food truck tacos."
        else:
            the_person.char "So I went out on my lunch break the other day to meet up with [the_person.SO_name] for lunch. He found this awesome food truck that has amazing tacos!"
        the_person.char "They tasted great, but when I got back here after lunch I swear I had to run to the bathroom all the way down by HR like five times!"
        the_person.char "I mean, [the_person.mc_title] is the only guy who works here, I wish they would just make both restrooms unisex. Then I wouldn't have to walk clear across the building!"
    else:
        the_person.char "So, the other day I was down in production, trying to find some notes the serums we've been making lately, when suddenly all the coffee I drank that morning hit me."
        the_person.char "I realized the only women's restroom we have in the whole place is all the way back by HR, on the other side of the building!"
        the_person.char "I mean, [the_person.mc_title] is the only guy who works here, I wish they would just make both restrooms unisex. I bet the girls in production would appreciate it too!"

    "The complaint seems... actually fairly reasonable."
    "There are only two restrooms, one men and one women, and they are on opposite sides of the building."
    "It would be a pretty minor investment to convert them into unisex restrooms. Plus, you never know what you might overhear when you happen to be in there..."
    $ mc.business.unisex_restroom_unlocks["unisex_policy_avail"] = 1
    return

label unisex_restroom_door_greet_label():   #You have a chance to learn a couple new opinions
    #TODO change background to restroom
    $ (the_person_one, the_person_two) = get_random_employees(2)

    "During the workday, you get up and head towards the restroom."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person_one, character_placement = character_center_flipped)
    $ scene_manager.add_actor(the_person_two)
    "As you step in the door, you pause for a second when you see [the_person_one.title] and [the_person_two.title] there at the sinks, freshing up."
    "You recently made all the bathrooms in the office unisex, and you aren't quite used to having women in the restroom when you walk in yet."
    "However, the girls seem completely unfazed when you walk through the door."
    the_person_one.char "Oh hey [the_person_one.mc_title]. So anyway..."
    "It seems like they are having a pretty active conversation. Trying not to be awkward, you head into one of the stalls and close the door. They keep talking."
    $ scene_manager.clear_scene()
    $ overhear_topic = the_person_one.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person_one, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person_one.char "... but yeah, I'm not sure he realizes I [text_one] [text_two]"
    if the_person_one.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [the_person_one.title] felt that way."
    "The girls keep talking. They keep bouncing back and forth between multiple topics."
    $ overhear_topic = the_person_two.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person_two, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person_two.char "...But I [text_one] [text_two], so I'm not sure what to do."
    if the_person_two.discover_opinion(overhear_topic):
        "Wow, you can learn all kinds of stuff just hanging out in the bathroom stall, or so it seems..."
    "The girls are still talking but you hear the bathroom door open. Their voices fade away as they exit."

    $ town_relationships.improve_relationship(the_person_one, the_person_two)
    $ del overhear_topic
    $ del text_one
    $ del text_two
    $ del the_person_one
    $ del the_person_two
    return

label unisex_restroom_sexy_overhear_label():
    $ (the_person_one, the_person_two) = get_random_employees(2)

    $ discover_identity = False
    $ anon_char_one = get_anon_person(the_person_one)
    #$ anon_char_one.name = "?????"
    $ anon_char_two = get_anon_person(the_person_two)
    #$ anon_char_two.name = "?????"
    "You step into the restroom and walk into one of the stalls."
    "As you are relieving yourself, you hear a couple girls enter the restroom, talking. They seem to be talking about some interesting stuff."
    anon_char_one "I know right? His dick is perfect, and he knows how to use it to."
    anon_char_two "Damn, maybe I should see if he wants to come over for Netflix and chill sometime..."
    "Huh. You wonder who walked in and who they are talking about."
    "You try to focus on the voices and see if you recognize them."
    if renpy.random.randint(0,100) < (25 + (mc.focus * 20)):  #base 25% chance, +20% for every point of focus.
        "As they talk, you pick up on subtle voice inflections and personality. It's [the_person_one.title] and [the_person_two.title]!"
        $ discover_identity = True
    else:
        "You try, but the identity of the girls eludes you for now."
    "They are talking about some pretty... interesting... encounters!"
    if discover_identity:
        $ overhear_topic = the_person_one.get_random_opinion(include_sexy = True, include_normal = False)
        $ text_one = person_opinion_to_string(the_person_one, overhear_topic)[1]
        $ text_two = get_topic_text(overhear_topic)
        the_person_one.char "... but yeah, I'm not sure he realizes I [text_one] [text_two]"
        if the_person_one.discover_opinion(overhear_topic):
            "Oh! You didn't realize that [the_person_one.title] felt that way."
        "The girls keep talking. They keep bouncing back and forth between multiple sexual topics."
        $ overhear_topic = the_person_two.get_random_opinion(include_sexy = True, include_normal = False)
        $ text_one = person_opinion_to_string(the_person_two, overhear_topic)[1]
        $ text_two = get_topic_text(overhear_topic)
        the_person_two.char "...But I [text_one] [text_two], so I'm not sure what to do."
        if the_person_two.discover_opinion(overhear_topic):
            "Wow, you can learn all kinds of stuff just hanging out in the bathroom stall."
    else:
        $ overhear_topic = the_person_one.get_random_opinion(include_sexy = True, include_normal = False)
        $ text_one = person_opinion_to_string(the_person_one, overhear_topic)[1]
        $ text_two = get_topic_text(overhear_topic)
        anon_char_one "... but yeah, I'm not sure he realizes I [text_one] [text_two]"
        "Oh damn! That info might be useful. But who is it!?!"
        "The girls keep talking. They keep bouncing back and forth between multiple sexual topics."
        $ overhear_topic_two = the_person_two.get_random_opinion(include_sexy = True, include_normal = False)
        $ text_one = person_opinion_to_string(the_person_two, overhear_topic)[1]
        $ text_two = get_topic_text(overhear_topic)
        anon_char_two "...But I [text_one] [text_two], so I'm not sure what to do."
        "Wow, you can learn all kinds of stuff just hanging out in the bathroom stall. If only you knew who it was!"
    "You hear the girls finish up and leave the restroom. You wash your hands and leave as well."

    $ town_relationships.improve_relationship(the_person_one, the_person_two)
    $ del the_person_one
    $ del the_person_two
    $ del text_one
    $ del text_two
    $ del anon_char_one
    $ del anon_char_two
    return

label unisex_restroom_fantasy_overhear_label():
    $ (the_person_one, the_person_two) = get_random_employees(2)
    if the_person_one.sluttiness < 30: #She's not slutty enough for this.
        call unisex_restroom_sexy_overhear_label() from _call_unisex_restroom_fantasy_redirect_1
        return
    $ discover_identity = False
    $ anon_char_one = get_anon_person(the_person_one)
    #$ anon_char_one.name = "?????"
    $ anon_char_two = get_anon_person(the_person_two)
    #$ anon_char_two.name = "?????"
    "You step into the restroom and walk into one of the stalls."
    "As you are relieving yourself, you hear a couple girls enter the restroom, talking. They seem to be talking about some interesting stuff."
    anon_char_one "I know right? I'm so frustrated right now. Last night I had this crazy dream about [the_person_one.mc_title]."
    anon_char_two "Damn. What kind of dream?"
    if the_person_one.get_opinion_score("public sex") < 0:
        anon_char_one "I'm not usually into like... doing things out in the open..."
    else:
        anon_char_one "Well, you know I've always had this fantasy of have sex like... out in front of other people..."
    "Damn! you like where this conversation is going. You focus and try and figure out who is talking, but it is hard to focus, considering they are talking about sex with you!"
    if renpy.random.randint(0,100) < (25 + (mc.focus * 15)):  #base 25% chance, +15% for every point of focus.
        "As they talk, you pick up on subtle voice inflections and personality. It's [the_person_one.title] and [the_person_two.title]!"
        $ discover_identity = True
    else:
        "You try, but the identity of the girls eludes you for now."
    "She continues to talk about her dream."
    if discover_identity:
        the_person_one.char "I was just at my desk, getting work done, when suddenly my hands were cuffed my desk!"
        the_person_one.char "At first, I got really scared, but then I felt [the_person_one.mc_title]'s strong hands on my hips and he whispers in my ear, 'shh just hold still'."
        the_person_two.char "Damn that's hot..."
        the_person_one.char "I know right? I felt my skirt lifting up and my panties getting pulled down. I couldn't move, I just let him do it!"
        "Wow! Maybe you should pay her a visit later, and act out this fantasy of hers."
        the_person_one.char "When he started fucking me I looked around saw the other girls pointing at me, trying not to watch. It was so hot!"
        the_person_two.char "God, you gotta calm down, now you're getting me worked up!"
        the_person_one.char "I know! But right as I was getting to finish, my alarm went off! I was so pissed. I tried to relieve myself this morning, but I just couldn't get off."
        the_person_two.char "Oh jesus you must be dying right now."
        the_person_one.char "UGH I am. I can't wait to get off work..."
    else:
        anon_char_one "I was just at my desk, getting work done, when suddenly my hands were cuffed my desk!"
        anon_char_one "At first, I got really scared, but then I felt [the_person_one.mc_title]'s strong hands on my hips and he whispers in my ear, 'shh just hold still'."
        anon_char_two "Damn that's hot..."
        anon_char_one "I know right? I felt my skirt lifting up and my panties getting pulled down. I couldn't move, I just let him do it!"
        "Oh god, who is it? You wish you knew who it was so you could act this fantasy out later..."
        anon_char_one "When he started fucking me I looked around saw the other girls pointing at me, trying not to watch. It was so hot!"
        anon_char_two "God, you gotta calm down, now you're getting me worked up!"
        anon_char_one "I know! But right as I was getting to finish, my alarm went off! I was so pissed. I tried to relieve myself this morning, but I just couldn't get off."
        anon_char_two "Oh jesus you must be dying right now."
        anon_char_one "UGH I am. I can't wait to get off work..."
    "The girls finish up and leave the restroom, leaving you alone inside."
    if discover_identity:
        "That was some pretty hot storytelling. You should definitely go see [the_person_one.title] later and act it out maybe?"

    $ town_relationships.improve_relationship(the_person_one, the_person_two)
    # if we don't have the fantasy actout limited time event for the person, add it to the on_talk_event_list.
    if discover_identity and not exists_in_room_enter_list(the_person_one, "unisex_restroom_fantasy_actout_label"):
        $ the_person_one.on_talk_event_list.append(Limited_Time_Action(unisex_restroom_fantasy_actout, 5))
    $ del the_person_one
    $ del the_person_two
    $ del anon_char_one
    $ del anon_char_two
    return

label unisex_restroom_fantasy_actout_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, position = "walking_away")
    "You walk up behind [the_person.title]. She's the one you overheard in the restroom that had a fantasy of getting fucked by you in front of the whole office."
    "Should you try and act it out?"
    menu:
        "Go for it":
            pass
        "Better not":
            "You decide to play it safe for now."
            $ scene_manager.clear_scene()
            return
    "Remembering her words you heard earlier, you walk up behind [the_person.title] and your hands firmly on her hips."
    the_person.char "Huh? Oh, [the_person.mc_title]? What are..."
    mc.name "Shhh, just hold still."
    the_person.char "Why? I don't under... oh my god..."
    "With one hand on her back and one firmly on her hip, you slowly bend [the_person.possessive_title] over her desk."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    $ the_person.change_slut_temp(20)
    the_person.char "Oh god oh god, its happening..."
    $ the_person.change_arousal(30)
    if the_person.outfit.vagina_available():
        "You take your hand off her back and run it down along her ass crack to her cunt. You can feel it is moist and ready for you already!"
    else:
        "You take your hand off her back and start to pull off all the clothing between you and her cunt."
        $ scene_manager.strip_actor_outfit(the_person, exclude_upper = True)
        "Once bare, you run your hand down along her ass crack to her cunt. You can feel it is moist and ready for you already!"
    $ the_person.break_taboo("bare_pussy")
    "You pull your cock out now, then put your hands on her hips. You position your cock at her needy slit."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "Without saying a word, you push yourself into her slick fuckhole. It feels amazing."
    call fuck_person(the_person, start_position = SB_doggy_standing, start_object = mc.location.get_object_with_name("desk"), skip_intro = True, private = False, position_locked = True) from _call_fantasy_actout_1
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person.char "Oh god, it was even better than I thought... oh my god."
        $ the_person.increase_opinion_score("public sex")
        $ the_person.change_happiness(10)
        $ the_person.change_slut_core(3)
    else:
        the_person.char "Fuck... I need to finish so bad! Why can't I just get off today?"
        $ the_person.change_happiness(-10)
        $ the_person.change_love(-5)

    $ the_person.review_outfit()
    return

label unisex_restroom_unlock_gloryhole_label():
    "You feel the call of nature, so you get up from your work and head to the restroom."
    "The restroom is empty, so you find an empty stall and enter it."
    "Much to your surprise, you discover a small hole cut out. The girls have made a gloryhole!"
    $ mc.business.unisex_restroom_unlocks["unisex_restroom_gloryhole"] = 1
    $ office.add_action(unisex_restroom_gloryhole_wait)
    "Since you are the only man in the company, you have to assume that this was made with you in mind."
    "You finish relieving yourself, and then consider. Should you wait and see if someone comes along? Or maybe try some other time?"
    menu:
        "Wait for a few minutes":
            call unisex_restroom_use_gloryhole_label from _call_use_dat_gloryhole_1
            pass
        "Finish up and maybe try it another time":
            pass
    return

label unisex_restroom_gloryhole_option_label():
    "You step into the restroom and walk into one of the stalls."
    if mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0) < 6:
        "You see that someone has drawn multiple hearts in red lipstick around it."
    else:
        "You see that someone has drawn an open mouth around it in lipstick."
        "Above the hole, someone has drawn a phallus, then the text 'dick goes here plz' with an arrow drawn to the hole."
        "Below, in different handwriting, someone else has written 'cum inside me please!' with another arrow pointed up to the hole."
    "You finish relieving yourself, and then consider. Should you wait and see if someone comes along? Or maybe try some other time?"
    menu:
        "Wait for a few minutes":
            call unisex_restroom_use_gloryhole_label from _call_use_dat_gloryhole_2
        "Finish up and maybe try it another time":
            pass
    return

label unisex_restroom_use_gloryhole_label():
    $ the_person = get_random_employees(1)
    "As you are waiting, you hear someone enter the restroom and walk into the stall next to yours."
    "This is crazy. It could be anybody in there! You hear on the other side the toilet flush as the person finishes relieving herself. You take a deep breath, then go for it."
    "You give yourself a couple of strokes to make sure you are good and hard, then stick your cock through the glory hole."
    $ person_response = gloryhole_get_response(the_person)
    if person_response == "Refuse":
        "The person inside clears her throat, but doesn't say or do anything."
        "Soon, you hear her exit her stall and quickly leave the restroom. Yikes, looks like whoever it was, wasn't very interested!"
        $ the_person.change_slut_temp(4, add_to_log = False)
        $ the_person.change_happiness(-5, add_to_log = False)
    elif person_response == "Handjob":
        call unisex_restroom_gloryhole_handjob_label(the_person) from _call_gloryhole_HJ_response_1
    elif person_response == "Blowjob":
        call unisex_restroom_gloryhole_blowjob_label(the_person) from _call_gloryhole_BJ_response_1
    elif person_response == "Vaginal":
        call unisex_restroom_gloryhole_vaginal_label(the_person) from _call_gloryhole_sex_response_1
    elif person_response == "Anal":
        call unisex_restroom_gloryhole_anal_label(the_person) from _call_gloryhole_anal_response_1
    elif person_response == "JoinMe":
        call unisex_restroom_gloryhole_joinme_label(the_person) from _call_gloryhole_joinme_response_1
    else:
        "Why aren't we catching anything here?"

    return _return

label unisex_restroom_gloryhole_wait_label():
    "You decide you could use a little anonymous action to break up the monotony of the day."
    "You step into the restroom and walk into one of the stalls."
    "You see the glory hole in the stall that has been cutout."
    if mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0) < 6:
        "You see that someone has drawn multiple hearts in red lipstick around it."
    else:
        "You see that someone has drawn an open mouth around it in lipstick."
        "Above the hole, someone has drawn a phallus, then the text 'dick goes here plz' with an arrow drawn to the hole."
        "Below, in different handwriting, someone else has written 'cum inside me please!' with another arrow pointed up to the hole."
    call unisex_restroom_use_gloryhole_label from _call_use_dat_gloryhole_wait_2
    #TODO advance time?

    return

label unisex_restroom_gloryhole_handjob_label(the_person):
    $ anon_char = get_anon_person(the_person)
    #$ anon_char.name = "?????"
    anon_char "Oh... I can't believe..."
    "The tone of voice on the other side of the wall has you a little bit concerned. Maybe this was a bad idea?"

    if the_person.has_taboo("touching_penis"):
        anon_char "Its so big, do you mind if I touch it?"
        mc.name "Go for it."
        $ the_person.break_taboo("touching_penis", add_to_log = False)
    else:
        "You are just getting ready to pull back you feel a soft hand grasp your member and start to stroke it."

    "You give an appreciative moan as the soft hand starts to slowly work your cock."
    anon_char "Ohhh... its so big..."
    "The hand is warm and soft as it slides up and down your cock. Suddenly you feel it leave you, and you can her the sound of her spitting."
    "A considerably more slippery hand starts to stroke you again. You buck your hips a bit against the sensation."
    "This feels good, you can feel yourself really getting into this. Having no idea who is next door really heightens your arousal."
    "The unknown woman next door rubs her thumb over your tip, spreading your precum over it and then working it back to the shaft."
    "It feels TOO good. You feel yourself start to pant and your balls tighten."
    anon_char "Oh!"
    "The hand never stops stroking you as you start to blow your load. Thank god whoever it is knows how to finish the job!"
    "After you finishes, she gives you a few extra strokes, drawing out any remaining cum. You feel a pair of lips lightly kiss the tip."
    "You slowly pull back. You grab some toilet paper and wipe your cock off."

    # the person is happy and a sluttier (don't log as to preserve anonymity)
    $ the_person.change_slut_temp(1, add_to_log = False)
    $ the_person.change_happiness(2, add_to_log = False)

    $ del anon_char
    return

label unisex_restroom_gloryhole_blowjob_label(the_person):
    $ anon_char = get_anon_person(the_person)
    #$ anon_char.name = "?????"
    anon_char "Oh! Mmmm, yum..."
    "Well that response certainly sounds promising."
    if the_person.has_taboo("touching_penis"):
        anon_char "Look at that thing, its huge..."
        "While talking you feel a soft hand grasp your member, giving at couple of strokes. You hear some movement, but you aren't sure what shes doing."
        $ the_person.break_taboo("touching_penis", add_to_log = False)
    else:
        "You feel a soft hand grasp your member and give it a couple of strokes. You hear movement coming from the stall next to you but you aren't sure what she's doing."

    if the_person.has_taboo("sucking_cock"):
        anon_char "Would you mind, if I gave you a blowjob?"
        mc.name "Not at all, go for it."
        "You feel a kiss on the tip of your cock, then a warm, wet tongue moving around the head."
        $ the_person.break_taboo("sucking_cock", add_to_log = False)
    else:
        "Slowly, you feel a warm, wet tongue circling around the tip of your cock, licking the pre-cum from the tip."

    anon_char "Mmmmmm"
    "A moan rumbles around your dick as the girl on the other side of the wall opens her mouth and slides her mouth down your aching hard on."
    "One of your employees is on the other side. The warm, wet suction of her lips and tongue feels great."
    "It's so hot, not knowing for sure who is on the other side of the wall. You have some guesses, based on her voice, but there's no way to know for sure."
    "The mysterious mouth pulls off your penis for a second and you feel her tongue sliding up and down your full length."
    "It swirls around the tip for a few moments until the anonymous maw in the neighboring stall opens up and greedily sucks on your shaft again."
    "She pushes herself deep, as you feel the tip start to hit the back of her throat, and then begin to slide down it a bit. You swear you feel a tongue on your balls!"
    "Her technique is amazing, you feel yourself getting ready to cum already!"
    "With a moan, you feel yourself pushed too far. It feels like your cock explodes as you begin to dump your load into her gullet."
    anon_char "Oh! Ummmfff.... mmmmmmmm..."
    "She moans in delight as your cream fills her mouth. She eagerly works every last drop from your pulsating prick."
    "You slowly pull back. You grab some toilet paper and wipe your cock off."

    # the person is happy and a sluttier (don't log as to preserve anonymity)
    $ the_person.change_slut_temp(3, add_to_log = False)
    $ the_person.change_happiness(3, add_to_log = False)

    $ del anon_char
    return

label unisex_restroom_gloryhole_vaginal_label(the_person):
    $ anon_char = get_anon_person(the_person)
    #$ anon_char.name = "?????"
    anon_char "Oh! Just what I needed..."
    #TODO condom check.
    "Sounds like your bathroom stall neighbor is taking the bait."

    if the_person.has_taboo("touching_penis"):
        anon_char "Its so big, do you mind if I touch it?"
        mc.name "Go for it."
        $ the_person.break_taboo("touching_penis", add_to_log = False)
    else:
        "You feel a soft hand grasp your member and give it a couple of strokes. You hear movement coming from the stall next to you but you aren't sure what's they are doing."

    if the_person.has_taboo(["condomless_sex", "vaginal_sex"]):
        anon_char "I really need to feel you cock, but I didn't bring any condoms, do you mind?"
        mc.name "I don't mind, show me what you can do."
        $ the_person.break_taboo("condomless_sex", add_to_log = False)
        $ the_person.break_taboo("vaginal_sex", add_to_log = False)

    "You feel her hand hold you rigidly in place as you begin to slowly feel a hot, wet sleeve enveloping your cock."
    "It feels like she is taking you in her pussy! You let out a moan of appreciation."

    anon_char "Mmmm, its so good when it goes in."
    "You press yourself against the wall to try and push yourself as deep as you can. You are almost balls deep, but the thin wall is in the way."
    "You start to work your hips a bit, testing the limits of how far you can pull back without pulling all the way out of her."
    anon_char "Yes! Mmm that feels good."
    "It's so hot, not knowing for sure who is on the other side of the wall. You have some guesses, based on her voice, but there's no way to know for sure."
    "You're giving whoever it is good hard thrusts now. Once in a while you thrust a little too hard and your hips ram into the stall wall."
    "The mystery cunt you are fucking feels like its getting wetter and wetter. The slippery channel feels so good wrapped around you."
    #TODO determine if she finishes or not. For now she always finishes with MC.
    "Moaning and panting coming from the other stall is getting urgent now. She must be enjoying this as much as your are!"
    anon_char "Oh god don't stop, please don't stop!"
    "Ha! Stopping was never even an option. You can feel her cunt starting to quiver and twitch. It feels TOO good!"
    "You give several more strong thrusts as you pass the point of no return. You moan as you begin to dump your load inside of her."
    anon_char "Yes. Yes! Oh fuck yes!"
    "You cum as deep inside of her as you can manage. You wonder if she is on birth control. Maybe you knocked her up? Who even is it!?!"
    "You pull out. You grab some toilet paper and wipe your cock off."

    # the person is happy and a sluttier (don't log as to preserve anonymity)
    $ the_person.change_slut_temp(5, add_to_log = False)
    $ the_person.change_happiness(5, add_to_log = False)

    $ del anon_char
    return

label unisex_restroom_gloryhole_anal_label(the_person):
    $ anon_char = get_anon_person(the_person)
    #$ anon_char.name = "?????"

    if the_person.has_taboo("touching_penis"):
        anon_char "Its so big, do you mind if I touch it?"
        mc.name "Go for it."
        $ the_person.break_taboo("touching_penis", add_to_log = False)
    else:
        anon_char "Oh! So hard! I know somewhere I can put that..."
        "Sounds like your bathroom stall neighbor likes what she sees."

    "You feel a soft hand grasp your member and give it a couple of strokes. You hear movement coming from the stall next to you but you aren't sure what's they are doing."
    "You here the sound of... was that spitting? Suddenly the hand stroking you is significantly wetter."
    "Similar sounds continue. Whoever it is, she seems to be lubing you up really good with her spit!"
    "It feels like saliva is dripping off your cock now, when you hear more motion coming from the stall."

    if the_person.has_taboo(["condomless_sex", "anal_sex"]):
        anon_char "I really need to feel you cock, but I didn't bring any condoms, do you mind?"
        mc.name "I don't mind, show me what you can do."
        $ the_person.break_taboo("condomless_sex", add_to_log = False)
        $ the_person.break_taboo("anal_sex", add_to_log = False)

    "You feel her hand hold you rigidly in place as you begin to slowly feel a hot, smooth, fleshy vice slowly swallowing your cock."
    "Shit! It feels like she is sticking you in her ass! She gets about halfway then stops for a moment."
    anon_char "Oh god it's so thick..."
    "She slowly keeps descending until she hits the literal wall, separating you from your anonymous butt slut."
    "You press yourself against the wall to try and push yourself as deep as you can. You are almost balls deep, but the damn wall is in the way."
    "You start to thrust a little bit, testing the limits on how far to pull back without pulling out."
    anon_char "Oh fuck its good. Mmmmm"
    "One of your employees is on the other side of that wall, taking your cock in her ass. But who? You have some guesses, based on her voice, but there's no way to know for sure."
    "You are thrusting vigorously now. Her ass is so tight, it's like it it is trying to milk the cum out of you."
    "Moaning and panting coming from the other stall is getting urgent now. She must be enjoying this as much as your are!"
    anon_char "Oh god don't stop, please don't stop!"
    "You feel yourself getting ready to nut. The urge to bury your cum deep in whoever this girl is ass is too strong."
    "Her ass is quivering all around you. Your penetration is making her finish too!"
    anon_char "Yes! Fuck my ass! YES!"
    "You cum as deep inside her ass as you can manage. Your cum spurts deep inside her bowel, farther than your cock can penetrate."
    "You pull out. You grab some toilet paper and wipe your cock off."

    # the person is happy and a sluttier (don't log as to preserve anonymity)
    $ the_person.change_slut_temp(7, add_to_log = False)
    $ the_person.change_happiness(7, add_to_log = False)

    $ del anon_char
    return

label unisex_restroom_gloryhole_joinme_label(the_person):
    $ anon_char = get_anon_person(the_person)
    $ scene_manager = Scene()
    anon_char "Oh! Mmmm, it's so hard."
    "Sounds like she's taking the bait."
    if the_person.has_taboo("touching_penis"):
        anon_char "Do you mind if I touch it?"
        mc.name "Go for it."
        $ the_person.break_taboo("touching_penis", add_to_log = False)

    "You feel a soft hand begin to stroke you. Her delicate fingers feel great wrapped around your erection."
    "She gives you a few good strokes, but then she stops."
    anon_char "Sir, I want to feel you... would you please come over into my stall?"
    menu:
        "Go over":
            "You quickly exit your stall and go into the one next to yours."
            $ scene_manager.add_actor(the_person, position = "kissing")
            "[the_person.title] is waiting for you as you step inside. You lock the stall and she immediately wraps her arms around you."
            the_person.char "Mmm, the glory hole is hot, but I am craving a more personal touch..."
            if not the_person.outfit.vagina_available():
                "You grab her ass for a bit, then start to peel off her clothes."
                $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False, exclude_feet = True, exclude_upper = True)
            "You pin her to the stall wall. She lifts up one leg to give you better access and grabs your cock in her hand."
            $ scene_manager.update_actor(the_person, position = "against_wall")
            $ the_person.break_taboo("condomless_sex")
            $ the_person.break_taboo("vaginal_sex")
            "She lines it up with her slit as you slowly slide into her. She stifles a moan when you finally bottom out."
            call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_gloryhole_joinme_1
            $ scene_manager.update_actor(the_person, position = "against_wall")
            "When you finish, you stand there with her, her leg still in the air for a moment."
            $ scene_manager.update_actor(the_person, position = "stand4")
            "You grab some toilet paper and wipe your dick off before leaving the stall so [the_person.title] can clean up."
            $ scene_manager.clear_scene()
        "Stay like this":  #Defaults to vaginal sex
            mc.name "I don't think that's how this is supposed to work..."
            anon_char "Ohhhh, fine."
            "You aren't sure who is on the other side of the wall but her disappointment is tangible."
            "You hear movement coming from the stall next to you but you aren't sure what's they are doing."
            if the_person.has_taboo(["condomless_sex", "vaginal_sex"]):
                anon_char "I really need to feel you cock, but I didn't bring any condoms, do you mind?"
                mc.name "I don't mind, show me what you can do."
                $ the_person.break_taboo("condomless_sex", add_to_log = False)
                $ the_person.break_taboo("vaginal_sex", add_to_log = False)

            "You feel her hand hold you rigidly in place as you begin to slowly feel a hot, wet sleeve enveloping your cock."
            "It feels like she is taking you in her pussy! You let out a moan of appreciation."
            anon_char "Mmmm, its so good when it goes in."
            "You press yourself against the wall to try and push yourself as deep as you can. You are almost balls deep, but the thin wall is in the way."
            "You start to work your hips a bit, testing the limits of how far you can pull back without pulling all the way out of her."
            anon_char "Yes! Mmm that feels good."
            "It's so hot, not knowing for sure who is on the other side of the wall. You have some guesses, based on her voice, but there's no way to know for sure."
            "You're giving whoever it is good hard thrusts now. Once in a while you thrust a little too hard and your hips ram into the stall wall."
            "The mystery cunt you are fucking feels like its getting wetter and wetter. The slippery channel feels so good wrapped around you."

            "Moaning and panting coming from the other stall is getting urgent now. She must be enjoying this as much as your are!"
            anon_char "Oh god don't stop, please don't stop!"
            "Ha! Stopping was never even an option. You can feel her cunt starting to quiver and twitch. It feels TOO good!"
            "You give several more strong thrusts as you pass the point of no return. You moan as you begin to dump your load inside of her."
            anon_char "Yes. Yes! Oh fuck yes!"
            "You cum as deep inside of her as you can manage. You wonder if she is on birth control. Maybe you knocked her up? Who even is it!?!"
            "You pull out. You grab some toilet paper and wipe your cock off."

            # the person is happy and a sluttier (don't log as to preserve anonymity)
            $ the_person.change_slut_temp(5, add_to_log = False)
            $ the_person.change_happiness(5, add_to_log = False)


    $ del anon_char
    return
