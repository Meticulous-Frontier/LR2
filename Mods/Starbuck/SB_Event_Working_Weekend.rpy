###Scene Idea: Working Weekend
#
#   In this scene, MC is working on the weekend when the business is otherwise closed.
#   Girl comes in to grab something from their locker or workspace and finds player working.
#   If not slutty, girl is just impressed by the MC work ethic.
#   If girl is a little slutty, she may offer to tease MC or give a blowjob
#   If girl is very slutty, girl may take the opportunity to striptease
#
#
###
init -1 python:
    SB_working_weekend_crisis_weight = 5

init 2 python:
    def SB_working_weekend_requirement():
        if mc.business.get_employee_count() > 0:
            if mc.business.is_weekend():
                if mc.is_at_work():
                    return True
        return False

    def person_opinion_to_string(person, topic):
        score = person.get_opinion_score(topic)
        if score <= -2:
            return (score, "actually hate")
        if score == -1:
            return (score, "don't like")
        if score == 0:
            return (score, "have no opinion about")
        if score == 1:
            return (score, "like")
        if score >= 2:
            return (score, "actually love")

    def get_topic_text(topic):
        if topic == "getting head":
            return "when guys lick my pussy"
        if topic == "creampies":
            return "when guys cum inside me"
        if topic == "being covered in cum":
            return "when guys cum all over me"
        if topic == "cum facials":
            return "when guys cum all over my face"
        if topic == "drinking cum":
            return "swallowing cum"
        if topic == "bareback sex":
            return "having sex without a condom."
        if topic == "showing her tits":
            return "showing my tits"
        if topic == "showing her ass":
            return "showing my ass"
        if topic == "lingerie":
            return "wearing lingerie"
        return topic

    def display_topic_opinions(person, topics):


        counter = 0
        for topic in topics:
            (score, opinion) = person_opinion_to_string(person, topic)
            if score != 0:
                display_text = get_topic_text(topic)
                renpy.say(person.char, "I " + opinion + " " + display_text + ".")
                counter += 1
                person.discover_opinion(topic)
        return counter

    SB_working_weekend_crisis = ActionMod("Working Weekend",SB_working_weekend_requirement,"SB_working_weekend_crisis_label",
        menu_tooltip = "While working weekends an employee comes into the office.", category = "Business", is_crisis = True, crisis_weight = SB_working_weekend_crisis_weight)

label SB_working_weekend_crisis_label():
    $ person_one = get_random_employees(1)    

    if person_one is None:
        return

    $ scene_manager = Scene()
    $ the_place = mc.business.get_employee_workstation(person_one)

    "Even though it is the weekend, you find yourself working."
    "Deep in thought, and with the company normally deserted, it takes you by surprise when you see movement out of the corner of your eye."
    "Looking aside, you see [person_one.possessive_title]."

    $ scene_manager.add_actor(person_one, emotion="default")
    $ scene_manager.draw_scene()
    "You can tell by the look on her face that [person_one.possessive_title] is also surprised to see you."
    if person_one.sluttiness < 30:
        #if she is not slutty at all
        person_one.char "Oh hey there [person_one.mc_title], I didn't expect to see you here! I just stopped by because I forgot something in my desk. Are you... working? You know its the weekend right?"
        "You can tell by the look on her face that she is impressed by your work ethic. You consider the chance to impress on her the values of the company in this one on one situation."
        menu:
            "Stress the importance of obedience":
                mc.name "It is no accident that this place is accomplishing great things. The work I am trying to do requires many long hours, but also organization and commitment to procedures."
                mc.name "A highly organized workplace is important, especially in a lab setting. I need employees who are able to listen to my instructions and follow them."
                "[person_one.possessive_title] nods in agreement."
                mc.name "You are doing a great job so far, [person_one.title], can I count on you to listen and obey the tasks I set out for you?"
                $ person_one.change_obedience(10)
                person_one.char "Yes, absolutely. I'll do everything I can to make sure this business is successful."

            "Stress the importance of satisfaction":
                mc.name "I've worked hard to build this place into what it is. Even though it is the weekend, I can't help but come out here and work on improving the business in anyway I can..."
                mc.name "But it can be easy to burn yourself out in this line of business. Pay might not always be great and the hours might be long, but a good attitude is key."
                "[person_one.possessive_title] nods in agreement."
                mc.name "You are doing a great job for me so far, [person_one.title], but take care of yourself, and don't let yourself get burned out."
                $ person_one.change_happiness(10)
                person_one.char "Yes sir, I do enjoy being here."

            "Stress the importance of work hard, play hard":
                mc.name "Yes, it is true that I work late into the days and even on the weekends, but that doesn't mean that I'm all business."
                mc.name "It is important though, that when you work heard, you can also play hard."
                "[person_one.possessive_title] nods in agreement."
                mc.name "You are doing a great job for me so far, [person_one.title]. Maybe some time we should play hard together?"
                $ person_one.change_slut_temp(10)
                $ person_one.change_slut_core(5)
                person_one.char "Oh! I suppose I might be up for something like that, sometime anyway."

        "After a minute of chit chat, [person_one.possessive_title] eventually says goodbye and walks out of the room."
    elif person_one.sluttiness < 70:
        "Before you can respond, [person_one.possessive_title] pulls up a chair and sits beside you."
        $ scene_manager.update_actor(person_one, position = "sitting")
        person_one.char "Wow, your dedication to this place is pretty incredible... Don't you ever do something... you know, to blow off steam?"
        "[person_one.possessive_title]'s voice takes a bit of a sultry tone at the end of that statement. Is she flirting with you?"
        mc.name "Yes, [person_one.title], of course I do... but... it IS rather boring around here. I'd be grateful for a bit of company while I'm working"
        "[person_one.possessive_title] smiles at you. And was that a wink?"
        person_one.char "Oh! [person_one.mc_title], I was about to go out, but seeing you here still working on the weekend, I'd be glad to stay here with you a bit and give you a bit of a... distraction for a bit."
        "The suggestion in her voice is apparent with the last statement. You briefly consider her offer before making a request..."
        menu:
            "How about a blowjob?\n{size=22}Modifiers: +20 Sluttiness, +5 Obedience{/size}":
                "[person_one.possessive_title] smiles."
                person_one.char "Oh [person_one.mc_title], you work so hard. Don't worry, I'll take care of you."
                if not person_one.outfit.tits_available():    #If covered up, have her take her top off
                    person_one.char "Here... let me take this off. I bet that will help ease some of your stress."
                    $ the_clothing = person_one.outfit.get_upper_ordered()[-1]
                    "[person_one.possessive_title] takes off her [the_clothing.name]"
                    $ person_one.draw_animated_removal(the_clothing)
                "Your eyes wander down to [person_one.possessive_title]'s tits."
                if person_one.outfit.tits_available():
                    if person_one.get_opinion_score("showing her tits") > 0:
                        "You can see a blush in [person_one.possessive_title]'s cheeks. She likes to show off her [person_one.tits] tits!"
                        $ person_one.discover_opinion("showing her tits")
                        $ person_one.change_slut_core(2)
                        $ person_one.change_slut_temp(5)
                "You back your chair up and move it to the side while [person_one.possessive_title] gets down on her knees in front of you."
                $ scene_manager.update_actor(person_one, position = "blowjob")
                $ person_one.add_situational_slut("seduction_approach",20)
                $ person_one.add_situational_obedience("seduction_approach", 5)
                call fuck_person(person_one, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_SB1

                $ person_one.clear_situational_slut("seduction_approach")
                $ person_one.clear_situational_obedience("seduction_approach")
                $ person_one.review_outfit(dialogue = False)
                "Eventually, [person_one.possessive_title] gets up. She says goodbye after giving you a quick kiss"
                return
            "Just Talk":
                "You decide to take the opportunity to learn a little more about [person_one.possessive_title]."
                "You chit chat about various things. You decide to probe a little further about her interests."
                $ SB_discover_opinion_count = 0
                menu:
                    "Ask about general opinions":
                        "You decide to ask about her general opinions."
                        $ topic_list = ["flirting", "sports", "hiking", "Mondays", "Fridays", "the weekend"]

                    "Ask about a work opinions":
                        "You decide to ask about her opinions about work."
                        $ topic_list = ["working", "work uniforms", "research work", "marketing work", "HR work", "supply work", "production work"]

                    "Ask about a style opinions":
                        "You decide to ask about her opinions about her personal style."
                        $ topic_list = ["skirts", "pants", "dresses", "boots", "high heels", "makeup", "conservative outfits", "the colour blue", "the colour yellow", "the colour red", "the colour pink", "the colour green", "the colour purple", "the colour white", "the colour black"]

                $ SB_discover_opinion_count = display_topic_opinions(person_one, topic_list)

                "You chat with [person_one.possessive_title] for a bit longer, but eventually she says goodbye and leaves."

        #IF she is a little slutty,
    else:  #If she is REALLY slutty
        person_one.char "Oh hey [person_one.mc_title]! Are you here all by yourself?"
        "You give her a quick nod as your finish up what you were doing."
        "Seeing that you are here all by yourself, [person_one.possessive_title] grabs a chair and sits close to you."
        $ scene_manager.update_actor(person_one, position = "sitting")
        person_one.char "Wow, your dedication to this place is pretty sexy... would you like to maybe... blow off a little steam?"
        "[person_one.possessive_title] begins to rub your crotch through your pants. You are almost done with your previous task, maybe you could get her to do something while you finish up..."
        menu:
            "Strip for me":
                mc.name "Hey, I'm almost done with this, but I tell you what. Why don't you give me a show while I finish and then maybe when I'm done I'll take you up on that."
                "[person_one.possessive_title] smiles mischievously at you, before nodding."
                person_one.char "I can do that, [person_one.mc_title]... I hope you like the show!"
                $ person_one.change_slut_temp(5)
                call SB_free_strip_scene(person_one) from _SB_free_strip_scene_3

            "Just Talk":
                "While her offer is tempting, you decide to take the opportunity to learn a little more about [person_one.possessive_title]"
                mc.name "Sorry, I can't while I'm in the middle of this, but maybe you could stay and talk to me for a little while."
                "[person_one.possessive_title] is clearly disappointed, so you decide to keep the topic of conversation sexual to keep her interested."
                "What do you ask about?"
                menu:
                    "Positions":
                        mc.name "So, how do you feel about different sex positions, [person_one.title]?"
                        "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                        person_one.char "Well..."

                        $ topic_list = ["missionary style sex", "doggy style sex", "sex standing up"]

                    "Sex types":
                        mc.name "So, how do you feel about different sex types, [person_one.title]?"
                        "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."

                        $ topic_list = ["vaginal sex", "anal sex", "giving blowjobs", "getting head"]

                    "Cum":
                        mc.name "So, how do you feel about cum, [person_one.title]?"
                        "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."

                        $ topic_list = ["creampies", "being covered in cum", "cum facials", "drinking cum", "bareback sex"]

                    "Sexy Clothing":
                        mc.name "So, how do you feel about sexy clothing and outfits, [person_one.title]?"
                        "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."

                        $ topic_list = ["skimpy outfits", "skimpy uniforms", "not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "lingerie"]

                    "Other Kinks":
                        mc.name "So, do you have any kinks, [person_one.title]? Something that might be more fun for me to know about?"
                        "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."

                        $ topic_list = ["masturbating", "giving handjobs", "being fingered", "being submissive", "taking control"]

                $ SB_discover_opinion_count = display_topic_opinions(person_one, topic_list)

                if SB_discover_opinion_count == 0:
                    person_one.char "I guess you could say I don't care too much about that."
                elif SB_discover_opinion_count < 2:
                    person_one.char "So I guess you could say I don't have a lot of strong feelings about that."
                else:
                    person_one.char "So I guess you could say I have a lot of opinions on that."
                "You chat with [person_one.possessive_title] for a little longer. Eventually she says goodbye and heads out."
                return #TODO Make sure this returns correctly
        "You are just finishing up with your work, and now [person_one.possessive_title] is here, naked, in your office."
        $ person_two = get_random_employees(1)
        if person_one == person_two:
            "You're pretty sure she's ready for next step if you are ready."
        elif person_two.sluttiness > 70:  #Someone walks in, threesome opportunity#
            "You walk over to [person_one.possessive_title]. She wraps her arms around you as you roughly grab her ass and pick her up. She's grinding herself against you as you carry her over to your desk."
            $ scene_manager.update_actor(person_one, position = "kissing")
            "[person_one.possessive_title] is just pulling your cock out when you hear a cough from the doorway."
            person_two.char "Wow, looks like you guys are getting ready for some fun!"
            $ scene_manager.add_actor(person_two, position = "stand3", character_placement = character_left, emotion = "happy")
            "You turn and see [person_two.possessive_title] standing in the doorway. You aren't sure how long she has been standing there."
            person_two.char "This is so sexy... [person_two.mc_title], can I join? Please!?! You won't regret it!"
            "Dumbfounded, you can only nod."
            person_two.char "Yes! Oh just give me one second!!!"
            "She starts to strip down."
            $ scene_manager.strip_actor_outfit(person_two)
            "Now naked, she walks over to you and [person_one.possessive_title]."
            person_two.char "Okay, how do you want to do this?"
            call start_threesome(person_one, person_two) from _call_start_threesome_SB_working_weekend_crisis
            $ the_report = _return
            #call SB_threesome_description(person_one, person_two, SB_threesome_sixty_nine, make_desk(), 0, private = True, girl_in_charge = False) from _SB_EVENT_THREESOME_WEEKEND_SB10
            "Wow, you just had sex with [person_one.possessive_title] and [person_two.possessive_title]! You can't believe how lucky you are."
            "Eventually, [person_two.possessive_title] gets up."
            person_two.char "Mmm... wow... I guess I should stop by on the weekend more often..."
            $ scene_manager.update_actor(person_two, position = "walking_away", character_placement = character_left)
            "[person_two.possessive_title] turns and starts to walk out."
            $ scene_manager.remove_actor(person_two)
            if the_report.get("girl orgasms", 0) > 0:
                "You get up and make yourself presentable again. [person_one.possessive_title] lays there for a while, recovering from her orgasm."
                $ person_one.change_slut_core(2)
                $ person_one.change_slut_temp(5)
                $ person_one.change_love(5)
            person_one.char "Holy fuck [person_one.mc_title], that was so hot."
            "She eventually gets up and gets herself dressed again. You say goodbye as she leaves the office."
            $ scene_manager.remove_actor(person_one)
            $ person_two.review_outfit(dialogue = False)
            $ person_one.review_outfit(dialogue = False)
            $ scene_manager.clear_scene()
            return
        menu:
            "Fuck her on your desk":
                "You walk over to [person_one.possessive_title]. She wraps her arms around you as you roughly grab her ass and pick her up. She's grinding herself against you as you carry her over to your desk."
                "When her ass runs up against the desk, she reaches down and begins unzipping your pants."
                "She pulls your your dick out and lays back. She lines you up with her pussy and push yourself into her."
                call fuck_person(person_one, start_position = missionary, start_object = make_desk(), skip_intro = True) from _call_sex_description_SB15
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 0:
                    "You get up and make yourself presentable again. [person_one.possessive_title] lays there for a while, recovering from her orgasm."
                    $ person_one.change_slut_core(2)
                    $ person_one.change_slut_temp(5)
                    $ person_one.change_love(5)
                else:   #She didn't cum
                    "You get up and make yourself presentable again. [person_one.possessive_title] lays there for a bit, clearly disappointed she didn't orgasm."
                    $ person_one.change_slut_temp(5)
                    $ person_one.change_happiness(-5)
                "She eventually gets up and gets herself dressed again. You say goodbye as she leaves the office."
            "Thank her for the show":
                mc.name "Thanks for that very pleasant distraction, [person_one.title], but I need to get back to work now."
                "[person_one.possessive_title] can barely hide their disappointment. There's a hint of anger in their voice when they reply."
                person_one.char "Wow, really? After I stripped for you? Okay then, I hope your day goes better than mine..."
                $ person_one.change_slut_temp(5)
                $ person_one.change_slut_core(2)
                $ person_one.change_happiness(-5)
                $ person_one.change_love(-15)

    $ scene_manager.remove_actor(person_one)
    $ scene_manager.clear_scene()
    $ person_one.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
    $ mc.location.show_background()
    return
