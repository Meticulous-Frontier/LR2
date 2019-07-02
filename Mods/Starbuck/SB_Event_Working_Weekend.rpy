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

    SB_working_weekend_crisis = ActionMod("Working Weekend",SB_working_weekend_requirement,"SB_working_weekend_crisis_label", 
        menu_tooltip = "While working weekends an employee comes into the office.", category = "Business", is_crisis = True, crisis_weight = SB_working_weekend_crisis_weight)

label SB_working_weekend_crisis_label():
    python:
        the_person = get_random_from_list(mc.business.get_employee_list())

    if the_person is None:
        "Apperently no one can come see you."
        return

    $ SB_LOW_SLUT_VALUE = 30    #Declare constants to tweak later
    $ SB_HIGH_SLUT_VALUE = 70
    $ the_place = mc.business.get_employee_workstation(the_person)
    $ ordered_bottom = the_person.outfit.get_lower_ordered()
    #if len(ordered_bottom) > 0:
        #$ the_clothing = the_person.outfit.get_lower_ordered()[-1] #Get the very top item of clothing.

    "Even though it is the weekend, you find yourself working."
    "Deep in thought, and with the company normally desserted, it takes you by surprise when you see movement out of the corner of your eye."
    "Looking aside, you see [the_person.possessive_title]."
    $ the_person.draw_person()
    "You can tell by the look on her face that [the_person.possessive_title] is also surprised to see you."
    if the_person.sluttiness < SB_LOW_SLUT_VALUE:
        #if she is not slutty at all
        the_person.char "Oh hey there [the_person.mc_title], I didn't expect to see you here! I just stopped by because I forgot something in my desk. Are you... working? You know its the weekend right?"
        "You can tell by the look on her face that she is impressed by your work ethic. You consider the chance to impress on her the values of the company in this one on one situation."
        menu:
            "Stress the importance of obedience.":
                mc.name "It is no accident that this place is accomplishing great things. The work I am trying to do requires many long hours, but also organization and commitment to procedures."
                mc.name "A highly organised workplace is important, especially in a lab setting. I need employees who are able to listen to my instructions and follow them."
                "[the_person.possessive_title] nods in agreement."
                mc.name "You are doing a great job so far, [the_person.title], can I count on you to listen and obey the tasks I set out for you?"
                $ the_person.change_obedience(10)
                the_person.char "Yes, absolutely. I'll do everything I can to make sure this business is successful."

            "Stress the importance of satisfaction.":
                mc.name "I've worked hard to build this place into what it is. Even though it is the weekend, I can't help but come out here and work on improving the business in anyway I can..."
                mc.name "But it can be easy to burn yourself out in this line of business. Pay might not always be great and the hours might be long, but a good attitude is key."
                "[the_person.possessive_title] nods in agreement."
                mc.name "You are doing a great job for me so far, [the_person.title], but take care of yourself, and don't let yourself get burned out."
                $ the_person.change_happiness(10)
                the_person.char "Yes sir, I do enjoy being here."

            "Stress the importance of work hard, play hard.":
                mc.name "Yes, it is true that I work late into the days and even on the weekends, but that doesn't mean that I'm all business."
                mc.name "It is important though, that when you work heard, you can also play hard."
                "[the_person.possessive_title] nods in agreement."
                mc.name "You are doing a great job for me so far, [the_person.title]. Maybe some time we should play hard together?"
                $ the_person.change_slut_temp(10)
                $ the_person.change_slut_core(5)
                the_person.char "Oh! I suppose I might be up for something like that, sometime anyway."

        "After a minute of chit chat, [the_person.possessive_title] eventually says goodbye and walks out of the room."
    elif the_person.sluttiness < SB_HIGH_SLUT_VALUE:
        "Before you can respond, [the_person.possessive_title] pulls up a chair and sits beside you."
        $ the_person.draw_person(position = "sitting")
        the_person.char "Wow, your dedication to this place is pretty incredible... Don't you ever do something... you know, to blow off steam?"
        "[the_person.possessive_title]'s voice takes a bit of a sulty tone at the end of that statement. Is she flirting with you?"
        mc.name "Yes, [the_person.title], of course I do... but... it IS rather boring around here. I'd be grateful for a bit of company while I'm working"
        "[the_person.possessive_title] smiles at you. And was that a wink?"
        the_person.char "Oh! [the_person.mc_title], I was about to go out, but seeing you here still working on the weekend, I'd be glad to stay here with you a bit and give you a bit of a... distraction for a bit."
        "The suggestion in her voice is apparent with the last statement. You briefly consider her offer before making a request..."
        menu:
            "How about a blowjob?\n{size=22}Modifiers: +20 Sluttiness, +5 Obedience{/size}" if mc.current_stamina > 0:
                "[the_person.possessive_title] smiles."
                the_person.char "Oh [the_person.mc_title], you work so hard. Don't worry, I'll take care of you."
                if not the_person.outfit.tits_available():    #If covered up, have her take her top off
                    the_person.char "Here... let me take this off. I bet that will help ease some of your stress."
                    $ the_clothing = the_person.outfit.get_upper_ordered()[-1]
                    "[the_person.possessive_title] takes off her [the_clothing.name]"
                    $ the_person.draw_animated_removal(the_clothing)
                "Your eyes wander down to [the_person.possessive_title]'s tits."
                if the_person.outfit.tits_available():
                    if the_person.get_opinion_score("showing her tits") > 0:
                        "You can see a blush in [the_person.possessive_title]'s cheeks. She likes to show off her [the_person.tits] tits!"
                        $ the_person.discover_opinion("showing her tits")
                        $ the_person.change_slut_core(2)
                        $ the_person.change_slut_temp(5)
                "You back your chair up and move it to the side while [the_person.possessive_title] gets down on her knees in front of you."
                $ the_person.draw_person(position = "blowjob")
                $ the_person.add_situational_slut("seduction_approach",20)
                $ the_person.add_situational_obedience("seduction_approach", 5)
                call sex_description(the_person, blowjob, make_floor(), round = 1, private = True, girl_in_charge = True) from _call_sex_description_SB1
                #while mc.arousal < 100:
                    #Blowjob stuff#
                #    $ SB_round_int = renpy.random.randint(0,100)
                #    if (SB_round_int) < 50:
                #        "While working your "##########################
                #    else:
                #        "that"
                #    $ mc.arousal += (the_person.sex_skills["Oral"] * 4 + 15)
                $ the_person.reset_arousal()
                    #Tidy up our situational modifiers, if any.
                $ the_person.clear_situational_slut("seduction_approach")
                $ the_person.clear_situational_obedience("seduction_approach")
                $ mc.current_stamina += -1
                "Eventually, [the_person.possessive_title] gets up. She says goodbye after giving you a quick kiss"
                return
            "How about a blowjob?\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
                pass
            "Just Talk":
                "You decide to take the opportunity to learn a little more about [the_person.possessive_title]."
                "You chit chat about various things. You decide to probe a little further about her interests."
                $ SB_discover_opinion_count = 0
                menu:
                    "Ask about general opinions":
                            "You decide to ask about her general opinions."
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="flirting")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="sports")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="hiking")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="Mondays")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="Fridays")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="the weekend")

                    "Ask about a work opinions":
                            "You decide to ask about her opinions about work."
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="working")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="work uniforms")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="research work")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="marketing work")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="HR work")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="supply work")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="production work")


                    "Ask about a style opinions":
                            "You decide to ask about her opinions about her personal style."
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="skirts")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="pants")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="the colour blue")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="makeup")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="the colour yellow")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="the colour red")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="the colour pink")
                            $ SB_get_opinion_and_print_text(the_person=the_person, the_opinion="conservative outfits")



                "You chat with [the_person.possessive_title] for a bit longer, but eventually she says goodbye and leaves."

        #IF she is a little slutty,
    else:  #If she is REALLY slutty
        the_person.char "Oh hey [the_person.mc_title]! Are you here all by yourself?"
        "You give her a quick nod as your finish up what you were doing."
        "Seeing that you are here all by yourself, [the_person.possessive_title] grabs a chair and sits close to you."
        $ the_person.draw_person(position = "sitting")
        the_person.char "Wow, your dedication to this place is pretty sexy... would you like to maybe... blow off a little steam?"
        "[the_person.possessive_title] begins to rub your crotch through your pants. You are almost done with your previous task, maybe you could get her to do something while you finish up..."
        menu:
            "Strip for me":
                mc.name "Hey, I'm almost done with this, but I tell you what. Why don't you give me a show while I finish and then maybe when I'm done I'll take you up on that."
                "[the_person.possessive_title] smiles mischieviously at you, before nodding."
                the_person.char "I can do that, [the_person.mc_title]... I hope you like the show!"
                $ the_person.change_slut_temp(5)
                call SB_free_strip_scene(the_person) from _SB_free_strip_scene_3

            "Just Talk":
                $ SEXUAL_TOPIC_COUNTER = 0
                "While her offer is tempting, you decide to take the opportunity to learn a little more about [the_person.possessive_title]"
                mc.name "Sorry, I can't while I'm in the middle of this, but maybe you could stay and talk to me for a little while."
                "[the_person.possessive_title] is clearly disappointed, so you decide to keep the topic of conversation sexual to keep her interested."
                "What do you ask about?"
                menu:
                    "Positions":
                        mc.name "So, how do you feel about different sex positions, [the_person.title]?"
                        "[the_person.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                        the_person.char "Well..."
                        #$ SEXUAL_TOPIC_COUNTER =SB_get_and_print_opinion(the_person, "missionary style sex")
                        if the_person.get_opinion_score("missionary style sex") > 1:
                            the_person.char "I actually LOVE missionary style sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("missionary style sex") > 0:
                            the_person.char "I like missionary style sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("missionary style sex") < -1:
                            the_person.char "I  actually HATE missionary style sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("missionary style sex") < 0:
                            the_person.char "I don't like missionary style sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("missionary style sex")


                        if the_person.get_opinion_score("doggy style sex") > 1:
                            the_person.char "I actually LOVE doggy style sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("doggy style sex") > 0:
                            the_person.char "I like doggy style sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("doggy style sex") < -1:
                            the_person.char "I  actually HATE doggy style sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("doggy style sex") < 0:
                            the_person.char "I don't like doggy style sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("doggy style sex")


                        if the_person.get_opinion_score("sex standing up") > 1:
                            the_person.char "I actually LOVE sex standing up."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("sex standing up") > 0:
                            the_person.char "I likesex standing up."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("sex standing up") < -1:
                            the_person.char "I  actually HATE sex standing up."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("sex standing up") < 0:
                            the_person.char "I don't like sex standing up."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("sex standing up")

                    "Sex types":
                        mc.name "So, how do you feel about different sex types, [the_person.title]?"
                        "[the_person.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                        if the_person.get_opinion_score("vaginal sex") > 1:
                            the_person.char "I actually LOVE vaginal sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("vaginal sex") > 0:
                            the_person.char "I like vaginal sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("vaginal sex") < -1:
                            the_person.char "I actually HATE vaginal sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("vaginal sex") < 0:
                            the_person.char "I don't like vaginal sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("vaginal sex")

                        if the_person.get_opinion_score("anal sex") > 1:
                            the_person.char "I actually LOVE anal sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("anal sex") > 0:
                            the_person.char "I like anal sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("anal sex") < -1:
                            the_person.char "I actually HATE anal sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("anal sex") < 0:
                            the_person.char "I don't like anal sex."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("anal sex")

                        if the_person.get_opinion_score("giving blowjobs") > 1:
                            the_person.char "I actually LOVE giving blowjobs."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("giving blowjobs") > 0:
                            the_person.char "I like giving blowjobs."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("giving blowjobs") < -1:
                            the_person.char "I actually HATE giving blowjobs."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("giving blowjobs") < 0:
                            the_person.char "I don't like giving blowjobs."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("giving blowjobs")

                        if the_person.get_opinion_score("getting head") > 1:
                            the_person.char "I actually LOVE when guys eat me out."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("getting head") > 0:
                            the_person.char "I like when guys eat me out."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("getting head") < -1:
                            the_person.char "I actually HATE when guys eat me out."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("getting head") < 0:
                            the_person.char "I don't like when guys eat me out."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("getting head")


                    "Cum":
                        mc.name "So, how do you feel about cum, [the_person.title]?"
                        "[the_person.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                        if the_person.get_opinion_score("creampies") > 1:
                            the_person.char "I actually LOVE when guys cum inside me."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("creampies") > 0:
                            the_person.char "I like when guys cum inside me."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("creampies") < -1:
                            the_person.char "I actually HATE when guys cum inside me."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("creampies") < 0:
                            the_person.char "I don't like when guys cum inside me."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("creampies")

                        if the_person.get_opinion_score("being covered in cum") > 1:
                            the_person.char "I actually LOVE when guys cum all over me."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being covered in cum") > 0:
                            the_person.char "I like when guys cum all over me."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being covered in cum") < -1:
                            the_person.char "I actually HATE when guys cum all over me."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being covered in cum") < 0:
                            the_person.char "I don't like when guys cum all over me."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("being covered in cum")

                        if the_person.get_opinion_score("cum facials") > 1:
                            the_person.char "I actually LOVE when guys cum all over my face."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("cum facials") > 0:
                            the_person.char "I like when guys cum all over my face."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("cum facials") < -1:
                            the_person.char "I actually HATE when guys cum all over my face."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("cum facials") < 0:
                            the_person.char "I don't like when guys cum all over my face."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("cum facials")

                        if the_person.get_opinion_score("drinking cum") > 1:
                            the_person.char "I actually LOVE swallowing cum."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("drinking cum") > 0:
                            the_person.char "I like swallowing cum."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("drinking cum") < -1:
                            the_person.char "I actually HATE swallowing cum."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("drinking cum") < 0:
                            the_person.char "I don't like swallowing cum."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("drinking cum")

                        if the_person.get_opinion_score("bareback sex") > 1:
                            the_person.char "I actually LOVE the thrill of pregnancy risk though. Shoot it inside me deep!"
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("bareback sex") > 0:
                            the_person.char "I kinda like when guys cum inside me. It feels kinda risky, right?"
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("bareback sex") < -1:
                            the_person.char "I am so scared of getting pregnant."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("bareback sex") < 0:
                            the_person.char "I am a little afraid of getting pregnant, to be honest."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("bareback sex")

                    "Sexy Clothing":
                        mc.name "So, how do you feel about sexy clothing and outfits, [the_person.title]?"
                        "[the_person.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                        if the_person.get_opinion_score("skimpy outfits") > 1:
                            the_person.char "I actually LOVE skimpy outfits."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("skimpy outfits") > 0:
                            the_person.char "I like skimpy outfits."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("skimpy outfits") < -1:
                            the_person.char "I actually HATE skimpy outfits."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("skimpy outfits") < 0:
                            the_person.char "I don't like skimpy outfits."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("skimpy outfits")

                        if the_person.get_opinion_score("skimpy uniforms") > 1:
                            the_person.char "I actually LOVE skimpy uniforms."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("skimpy uniforms") > 0:
                            the_person.char "I like skimpy uniforms."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("skimpy uniforms") < -1:
                            the_person.char "I actually HATE skimpy uniforms."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("skimpy uniforms") < 0:
                            the_person.char "I don't like skimpy uniforms."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("skimpy uniforms")

                        if the_person.get_opinion_score("not wearing underwear") > 1:
                            the_person.char "I actually LOVE not wearing underwear."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("not wearing underwear") > 0:
                            the_person.char "I like not wearing underwear."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("not wearing underwear") < -1:
                            the_person.char "I actually HATE not wearing underwear."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("not wearing underwear") < 0:
                            the_person.char "I don't like not wearing underwear."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("not wearing underwear")

                        if the_person.get_opinion_score("not wearing anything") > 1:
                            the_person.char "I actually LOVE not wearing anything."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("not wearing anything") > 0:
                            the_person.char "I like not wearing anything."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("not wearing anything") < -1:
                            the_person.char "I actually HATE not wearing anything."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("not wearing anything") < 0:
                            the_person.char "I don't like not wearing anything."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("not wearing anything")

                        if the_person.get_opinion_score("showing her tits") > 1:
                            the_person.char "I actually LOVE showing my tits."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("showing her tits") > 0:
                            the_person.char "I like showing my tits."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("showing her tits") < -1:
                            the_person.char "I actually HATE showing my tits."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("showing her tits") < 0:
                            the_person.char "I don't like showing my tits."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("showing her tits")

                        if the_person.get_opinion_score("showing her ass") > 1:
                            the_person.char "I actually LOVE showing my ass."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("showing her ass") > 0:
                            the_person.char "I like showing my ass."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("showing her ass") < -1:
                            the_person.char "I actually HATE showing my ass."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("showing her ass") < 0:
                            the_person.char "I don't like showing my ass."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("showing her ass")

                        if the_person.get_opinion_score("lingerie") > 1:
                            the_person.char "I actually LOVE wearing lingerie."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("lingerie") > 0:
                            the_person.char "I like wearing lingerie."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("lingerie") < -1:
                            the_person.char "I actually HATE wearing lingerie."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("lingerie") < 0:
                            the_person.char "I don't like wearing lingerie."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("lingerie")


                    "Other Kinks":
                        mc.name "So, do you have any kinks, [the_person.title]? Something that might be more fun for me to know about?"
                        "[the_person.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                        if the_person.get_opinion_score("masturbating") > 1:
                            the_person.char "I actually LOVE masturbating."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("masturbating") > 0:
                            the_person.char "I like masturbating."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("masturbating") < -1:
                            the_person.char "I actually HATE masturbating."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("masturbating") < 0:
                            the_person.char "I don't like masturbating."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("masturbating")

                        if the_person.get_opinion_score("giving handjobs") > 1:
                            the_person.char "I actually LOVE giving handjobs."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("giving handjobs") > 0:
                            the_person.char "I like giving handjobs."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("giving handjobs") < -1:
                            the_person.char "I actually HATE giving handjobs."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("giving handjobs") < 0:
                            the_person.char "I don't like giving handjobs."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("giving handjobs")

                        if the_person.get_opinion_score("being fingered") > 1:
                            the_person.char "I actually LOVE being fingered."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being fingered") > 0:
                            the_person.char "I like being fingered."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being fingered") < -1:
                            the_person.char "I actually HATE being fingered."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being fingered") < 0:
                            the_person.char "I don't like being fingered."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("being fingered")

                        if the_person.get_opinion_score("being submissive") > 1:
                            the_person.char "I actually LOVE being submissive."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being submissive") > 0:
                            the_person.char "I like being submissive."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being submissive") < -1:
                            the_person.char "I actually HATE being submissive."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("being submissive") < 0:
                            the_person.char "I don't like being submissive."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("being submissive")

                        if the_person.get_opinion_score("taking control") > 1:
                            the_person.char "I actually LOVE taking control."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("taking control") > 0:
                            the_person.char "I liketaking control."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("taking control") < -1:
                            the_person.char "I actually HATE taking control."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        elif the_person.get_opinion_score("taking control") < 0:
                            the_person.char "I don't like taking control."
                            $ SEXUAL_TOPIC_COUNTER += 1
                        $ the_person.discover_opinion("taking control")

                if SEXUAL_TOPIC_COUNTER == 0:
                    the_person.char "I guess you could say I don't care too much about that."
                elif SEXUAL_TOPIC_COUNTER < 2:
                    the_person.char "So I guess you could say I don't have a lot of strong feelings about that."
                else:
                    the_person.char "So I guess you could say I have a lot of opinions on that."
                "You chat with [the_person.possessive_title] for a little longer. Eventually she says goodbye and heads out."
                return #TODO Make sure this returns correctly
        "You are just finishing up with your work, and now [the_person.possessive_title] is here, naked, in your office."
        $ the_person_two = get_random_from_list(mc.business.get_employee_list())
        if the_person == the_person_two:
            "You're pretty sure she's ready for next step if you are ready."
        elif the_person_two.sluttiness > SB_HIGH_SLUT_VALUE :  #Someone walks in, threesome opportunity#
            "You walk over to [the_person.possessive_title]. She wraps her arms around you as you roughly grab her ass and pick her up. She's grinding herself against you as you carry her over to your desk."
            "[the_person.possessive_title] is just pulling your cock out when you hear a cough from the doorway."
            the_person_two.char "Wow, looks like you guys are getting ready for some fun!"
            $ SB_draw_two_person_scene(person_one = the_person, person_two = the_person_two, two_pos_x = 0.7, one_position = "missionary")
            "You turn and see [the_person_two.possessive_title] standing in the doorway. You aren't sure how long she has been standing there."
            the_person_two.char "This is so sexy... [the_person_two.mc_title], can I join? Please!?! You won't regret it!"
            "Dumbfounded, you can only nod."
            the_person_two.char "Yes! Oh just give me one second!!!"
            "She starts to strip down."
            $ strip_choice = the_person_two.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
            while strip_choice is not None:
                $ the_person_two.outfit.remove_clothing(strip_choice)
                $ SB_draw_two_person_scene(person_one = the_person, person_two = the_person_two, two_pos_x = 0.7, one_position = "missionary")
                "You watch as [the_person_two.possessive_title] take off her [strip_choice.name]."
                $ strip_choice = the_person_two.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
            "Now naked, she walks over to you and [the_person.possessive_title]."
            the_person_two.char "Okay, how do you want to do this?"
            call SB_threesome_description(the_person, the_person_two, SB_threesome_sixty_nine, make_desk(), 0, private = True, girl_in_charge = False) from _SB_EVENT_THREESOME_WEEKEND_SB10
            "Wow, you just had sex with [the_person.possessive_title] and [the_person_two.possessive_title]! You can't believe how lucky you are."
            "Eventually, [the_person_two.possessive_title] gets up."
            $ SB_draw_two_person_scene(person_one = the_person, person_two = the_person_two, two_pos_x = 0.7, one_position = "missionary")
            the_person_two.char "Mmm... wow... I guess I should stop by on the weekend more often..."
            $ SB_draw_two_person_scene(person_one = the_person, person_two = the_person_two, two_pos_x = 0.7, two_position = "walking_away", one_position = "missionary")
            "[the_person_two.possessive_title] turns and starts to walk out."
            if the_person.arousal > 100:  #She  came
                "You get up and make yourself presentable again. [the_person.possessive_title] lays there for a while, recovering from her orgasm."
                $ the_person.change_slut_core(2)
                $ the_person.change_slut_temp(5)
                $ the_person.change_love(5)
            $ mc.current_stamina += -1
            the_person.char "Holy fuck [the_person.mc_title], that was so hot."
            "She eventually gets up and gets herself dressed again. You say goodbye as she leaves the office."
            $ the_person_two.reset_arousal()
            $ the_person.reset_arousal()

            return
        menu:
            "Fuck her on your desk" if mc.current_stamina > 0:
                "You walk over to [the_person.possessive_title]. She wraps her arms around you as you roughly grab her ass and pick her up. She's grinding herself against you as you carry her over to your desk."
                "When her ass runs up against the desk, she reaches down and begins unzipping your pants."
                "She pulls your your dick out and lays back. She lines you up with her pussy and push yourself into her."
                call sex_description(the_person, missionary, make_desk(), 1, private = True) from _call_sex_description_SB15

                if the_person.arousal > 100:  #She  came
                    "You get up and make yourself presentable again. [the_person.possessive_title] lays there for a while, recovering from her orgasm."
                    $ the_person.change_slut_core(2)
                    $ the_person.change_slut_temp(5)
                    $ the_person.change_love(5)
                    $ mc.current_stamina += -1
                else:   #She didn't cum
                    "You get up and make yourself presentable again. [the_person.possessive_title] lays there for a bit, clearly disappointed she didn't orgasm."
                    $ the_person.change_slut_temp(5)
                    $ the_person.change_happiness(-5)
                    $ mc.current_stamina += -1
                "She eventually gets up and gets herself dressed again. You say goodbye as she leaves the office."
                $ the_person.reset_arousal()
            "Fuck her on your desk\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
                pass
            "Thank her for the show":
                mc.name "Thanks for that very pleasant distraction, [the_person.title], but I need to get back to work now."
                "[the_person.possessive_title] can barely hide their disappointment. There's a hint of anger in their voice when they reply."
                the_person.char "Wow, really? After I stripped for you? Okay then, hope you day goes better than mine..."
                $ the_person.change_slut_temp(5)
                $ the_person.change_slut_core(2)
                $ the_person.change_happiness(-5)
                $ the_person.change_love(-15)
                return
        "Eventually, [the_person.possessive_title] gets up. She says goodbye after giving you a peck on the cheek and is soon walking out the door."



    $ renpy.scene("Active")
    return

init 3 python :
    def SB_get_opinion_and_print_text(the_person, the_opinion):
        the_person.discover_opinion(the_opinion)
        if the_person.get_opinion_score(the_opinion) > 1:
            renpy.say (the_person.name, "I actually LOVE " + the_opinion + ".")
            return 1
        elif the_person.get_opinion_score(the_opinion) > 0:
            renpy.say (the_person.name, "I like " + the_opinion + ".")
            return 1
        elif the_person.get_opinion_score(the_opinion) < -1:
            renpy.say (the_person.name, "I actually HATE " + the_opinion + ".")
            return 1
        elif the_person.get_opinion_score(the_opinion) < 0:
            renpy.say (the_person.name, "I don't like " + the_opinion + ".")
            return 1
        return 0
