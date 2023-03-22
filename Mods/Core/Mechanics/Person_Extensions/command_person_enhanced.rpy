
init 2 python:
    def make_onlyfans_together_requirement(person):
        if person.obedience < 150:
            return "Requires: 150 Obedience"
        if not the_person.has_role(onlyfans_role):
            return "No OnlyFans Account"
        return True

    def bend_over_your_desk_requirement(person):
        if not the_person.is_employee():
            return False
        if mc.business.event_triggers_dict.get("employee_over_desk_unlock", False):
            if person.obedience < 130:
                return "Requires: 130 Obedience"
            else:
                return True
        return False

    # extend the bugfix build_command_person_actions_menu function
    def build_command_person_actions_menu2(the_person):
        result = build_command_person_actions_menu(the_person)
        make_onlyfans_together_action = Action("Make a OnlyFans video together", requirement = make_onlyfans_together_requirement, effect = "make_onlyfans_together_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Order " + the_person.title + " to make a OnlyFans video together with you.", priority = -5)
        bend_over_your_desk_action = Action("Bend her over her desk", requirement = bend_over_your_desk_requirement, effect = "bend_over_your_desk_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Order " + the_person.title + " to bend over her desk so you can enjoy her ass.", priority = -5)
        result.insert(7, make_onlyfans_together_action)
        result.insert(7, bend_over_your_desk_action)
        return result

    # this only works when we can enhance the menu from the bugfix
    if "build_command_person_actions_menu" in globals():
        config.label_overrides["command_person"] = "command_person_enhanced"

label command_person_enhanced(the_person):
    mc.name "[the_person.title], I want you to do something for me."
    the_person "Yes [the_person.mc_title]?"

    if mod_installed:
        call screen enhanced_main_choice_display(build_menu_items([build_command_person_actions_menu2(the_person)]))
    else:
        call screen main_choice_display([build_command_person_actions_menu2(the_person)])

    if _return != "Return":
        $ _return.call_action()
    return

label make_onlyfans_together_label(the_person):
    mc.name "Hey, aren't you a content creator on OnlyFans?"
    the_person "Yeah, I am."
    mc.name "Let's make a video together. I bet I can help you pull in a ton of views."
    if the_person.effective_sluttiness() < 60:
        the_person "I'm not sure that is a good idea..."
        mc.name "Why not? I mean, you're already on there, what's wrong with me dicking you down?"
        the_person "I... okay, I guess we can do that..."
    else:
        the_person "Sure! Just make sure you finish. My customers pay way better if there's a good cumshot, okay?"
        mc.name "I aim to please."
    "You find a private area with [the_person.possessive_title] where you won't be disturbed."
    call fuck_person(the_person, private = True, condition = make_condition_onlyfans_recording()) from _call_fuck_person_make_onlyfans_command_01
    "You hand [the_person.possessive_title]'s phone back to her."
    mc.name "If you want to make another video sometime, just let me know."
    the_person "Sure thing!"
    $ the_person.apply_planned_outfit()
    $ clear_scene
    return

label bend_over_your_desk_label(the_person):
    mc.name "[the_person.title], I want you to bend over you desk and work on something on the computer terminal for a while."
    the_person "Oh?"
    mc.name "I'm going to sit behind you and enjoy your body for a bit. You don't mind do you?"
    if the_person.obedience > 180:
        the_person "No, anything you want sir."
        "She eagerly complies, trying to her best to please you."
    elif the_person.sluttiness > 50:
        the_person "I don't mind if you want to do have some fun like that..."
        "She eagerly complies."
    else:
        the_person "Oh my... I suppose..."
        "She hesitates a bit, but obediently complies."
    $ the_person.draw_person(position = "standing_doggy")
    "You sit down in her chair. [the_person.possessive_title]'s ass is directly in front of you for your viewing pleasure as you sit down."
    call employee_lust_build_loop_label(the_person) from _obedience_lust_build_loop_call_02
    if the_person.energy < 30:
        "You are incredibly turned on, but you can tell that [the_person.title] is too tired to continue."
        "[the_person.possessive_title] adjusts her outfit."
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person (position = the_person.idle_pose)
        return
    elif mc.energy < 30:
        "You are incredibly turned on, but you just don't have the energy to continue."
        "[the_person.possessive_title] adjusts her outfit."
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person (position = the_person.idle_pose)
        return
    elif get_lust_tier() >= 4 or (get_lust_tier() * 2 > mc.focus):
        "You are incredibly turned on. You decide to take things with [the_person.title] a step further."
    else:
        "Do you want to take things with [the_person.title] a step further?"

    $ report_log = create_report_log({ "obedience_used": True}) # we already start with obedience used set
    menu:
        "Ask for handjob" if the_person.obedience < 140:
            mc.name "You are so fucking hot. Would you please finish me off? You can use your hand."
            the_person "Okay, I can do that."
            call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = False, skip_intro = False, allow_continue = False, report_log = report_log) from _obedience_lust_loop_handjob_finish_01
        "Demand blowjob" if the_person.is_willing(blowjob, private = False):
            mc.name "That's enough, now I need you to finish me off. Get on your knees and suck me off."
            if the_person.opinion_score_giving_blowjobs() <= -2:
                the_person "I'm sorry, I can't do that... but I can get you off some other way!"
                mc.name "Fine, just do that then."
                the_person "Okay..."
                call get_fucked(the_person, the_goal = "get mc off", private = False, skip_intro = False, allow_continue = False, report_log = report_log) from _obedience_lust_loop_blowjob_finish_01
            else:
                $ the_person.draw_person(position = "blowjob")
                "[the_person.possessive_title] obediently turns and gets down on her knees."
                "You pull your cock out and she opens her mouth, taking you in her mouth obediently."
                call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True, report_log = report_log) from _obedience_lust_loop_blowjob_finish_02
        "Fuck her" if the_person.is_willing(SB_doggy_standing, private = False) and the_person.vagina_available():
            "You stand up and pull your cock out. You rub yourself along her slit for a moment."
            the_person "Ah... sir?"
            mc.name "Just keep working. This will only take a moment."
            call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_desk(), condition = make_condition_computer_work(), skip_intro = True, position_locked = True, report_log = report_log) from _obedience_lust_loop_doggy_finish_01
        "Fuck her ass" if the_person.is_willing(SB_anal_standing, private = False) and the_person.vagina_available():
            "You stand up and pull your cock out. You rub yourself along her slit for a moment."
            the_person "Ah... sir?"
            mc.name "Just keep working. This will only take a moment."
            call fuck_person(the_person, start_position = SB_anal_standing, condition = make_condition_computer_work(), start_object = make_desk(), skip_intro = True, position_locked = True, report_log = report_log) from _obedience_lust_loop_anal_finish_01
        "Leave her alone" if not (get_lust_tier() >= 4 or (get_lust_tier() * 2 > mc.focus)):
            pass
    mc.name "Thank you, [the_person.title]. That was just what I needed."
    if the_person.obedience >= 160:
        "[the_person.possessive_title] starts to clean herself up."
        menu:
            "Stay like that":
                mc.name "What are you doing? Did I say you could clean up?"
                the_person "N... no sir."
                mc.name "I want you to just stay like that for a while. It's a good look for you."
                the_person "Yes [the_person.mc_title]."
                $ the_person.change_obedience(1)
            "Don't say anything":
                "You decide to let her straighten her outfit this time."
                $ the_person.apply_planned_outfit()
    else:
        "[the_person.possessive_title] cleans herself up and adjusts her outfit."
        $ the_person.apply_planned_outfit()
    $ the_person.draw_person (position = the_person.idle_pose)
    return


label employee_lust_build_loop_label(the_person):
    $ loop_choice = None
    $ ass_lubed = False
    $ fingers_wet = False
    while loop_choice != "finish":
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.possessive_title] is standing in front of you, bent over her desk while you sit right behind her."
        if the_person.vagina_available():
            if the_person.arousal_perc > 75:
                "Her juices are leaking down the inside of her leg. Her lips are puffy with desperate arousal."
                "Her ass jiggles enticingly and her ass sways with every touch."
            elif the_person.arousal_perc > 30:
                "Her pussy is exposed to your view, and a hint of her arousal can be seen on her lips."
                "Her ass jiggles enticingly with every touch."
            else:
                "Her ass and pussy are exposed for you to view. Her ass jiggles with every touch and movement."
        else:
            "Her ass sways enticingly with every touch and movement."
        #Chance to unlock spanking submissive girls here
        if the_person.get_opinion_score("being submissive") > 0 and not the_person.can_be_spanked() and the_person.vagina_available() and renpy.random.randint(0, 100) < 30:
            "Something about [the_person.possessive_title]'s ass in your face and her submissive nature is getting your hormones going."
            "You reach up without warning and give her ass a firm spank."
            "*SLAP*"
            $ spank_factor_increment(the_person)
            the_person "Mnnnf!"
            "She moans, with just a hint of pain in her voice."
            mc.name "[the_person.title], your ass looks amazing when I spank it. You are such a slut. I bet you love it don't you?"
            the_person "Oh god, this is so naughty!"
            "She really seemed to enjoy her spanking. Maybe you should work it into your normal foreplay..."
            $ the_person.unlock_spanking()
        menu:
            "Spank her{color=#FFFF00}-10{/color} {image=gui/extra_images/energy_token.png}" if the_person.can_be_spanked() and the_person.vagina_available():
                $ spank_factor = calc_spank_factor(the_person)
                $ ass_desc = spanking_get_ass_description(the_person)
                $ mc.change_energy(-10)
                "You look at [the_person.possessive_title]'s ass. It is [ass_desc]"
                "*SLAP*"
                "You give her a solid spank. She lets out a little yelp."
                "*SLAP* *SLAP* *SLAP*"
                "You don't let up, giving her a solid spanking, moving back and forth between each cheek."
                if spank_factor > 5: #She loves it.
                    the_person "Oh god [the_person.mc_title]! Give it to me good! Oh god!"
                    "She is really getting into this. With each spank she wiggles her ass, giving you an enticing target."
                    $ the_person.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))
                    $ the_person.change_slut(spank_factor - 5)
                elif spank_factor > 0:
                    the_person "Oh... I'm sorry [the_person.mc_title]! Oh god..."
                    "She keeps her ass still, taking your blows. Her ass makes an enticing target."
                    $ the_person.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))
                    $ the_person.change_obedience(spank_factor)
                elif spank_factor > -5:
                    the_person "Ouch! I'm sorry [the_person.mc_title]! That really hurts..."
                    "With each spank, she flinches a bit."
                    $ the_person.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))
                    $ the_person.change_obedience(-(spank_factor-3))
                else:
                    the_person "Fuck! That hurts! Why are you doing this? Please stop!"
                    "She is trembling. With each spank she flinches and quakes."
                    $ the_person.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))
                    $ the_person.change_obedience(-spank_factor)
                    $ the_person.change_love(spank_factor)
                $ spank_factor_increment(the_person)

            "Pull her bottoms off" if not (the_person.vagina_available() or the_person.vagina_visible()) and (the_person.sluttiness > 30 or the_person.obedience > 140):
                "You decide that it is time to get a better view. You pull at her clothing."
                the_person "Sir... I..."
                mc.name "Shh, just keep working."
                the_person "Fuck... okay..."
                $ the_person.strip_to_vagina(position = "standing_doggy")
                "[the_person.possessive_title]'s ass is now exposed, directly in front of your face for your viewing pleasure as she works at the computer terminal."
                "You run your hands along it and give it a little smack."

            "Grope her ass{color=#FFFF00}-10{/color} {image=gui/extra_images/energy_token.png}":    #The baseline option
                "You reach up and run your hands over her shapely ass as she works."
                $ mc.change_energy(-10)
                if the_person.vagina_available():
                    if the_person.body_is_thin():
                        "[the_person.title]'s tight cheeks are firm and pleasing to the touch. She works hard to keep a fit body and it shows."
                    elif the_person.body_is_average():
                        "[the_person.title]'s shapely ass wobbles a bit as you grope it. You love the feeling of her curves in your hands."
                    elif the_person.body_is_thick():
                        "[the_person.title]'s big bubble butt wobbles excessively as you grope it."
                    elif the_person.body_is_pregnant():
                        "[the_person.title]'s ass wobbles enticingly as you grope it. Her pregnant belly hands underneath her as she enjoys your touches."
                    "You let yourself grope and rub her ass for several seconds as she sighs in pleasure."
                    $ the_person.change_arousal(5)
                else:
                    "[the_person.title]'s curves feel great through her clothing."

            "Order her to twerk" if the_person.energy > 10 and (the_person.sluttiness > 30 or the_person.obedience > 140):
                mc.name "Shake your ass for me. I want to see what this thing can do."
                "[the_person.possessive_title] doesn't say anything, but obediently starts to shake her ass the way you've instructed."
                if the_person.vagina_available():
                    if the_person.body_is_thin():
                        "[the_person.title] shakes her tight little ass up and down for you."
                    elif the_person.body_is_average():
                        "[the_person.title] shakes her shapely ass up and down for you. It wobbles pleasingly as she shakes it."
                    elif the_person.body_is_thick():
                        "[the_person.title] shakes her big ass up and down for you. Her cheeks make large waves as she bounces it up and down."
                    elif the_person.body_is_pregnant():
                        "[the_person.title] shakes her big, pregnant ass up and down for you. This angle really accentuates the curve of her cheeks and bump enticingly."
                    "You can't look away and can only imagine the pleasure it would be bring to have your cock buried inside her while she did this..."
                else:
                    "[the_person.title] twerks her ass up and down for you in an enticing display. You give it a couple light smacks as she moves."
                $ the_person.change_energy(-10)

            "Finger her{color=#FFFF00}-10{/color} {image=gui/extra_images/energy_token.png}" if the_person.vagina_available() and (the_person.sluttiness > 30 or the_person.obedience > 140) and the_person.opinion_score_being_fingered() >= 0:
                "You run your hand along the curve of her hip, then across the top of her ass, then down along her crack."
                $ mc.change_energy(-10)
                "You get to her slit and run your finger along it a few times, then slowly push two fingers into her soft love tunnel."
                $ fingers_wet = True
                the_person "Mmmm..."
                mc.name "Keep working, this is for my enjoyment, not yours."
                the_person "Y... yes sir!"
                "[the_person.possessive_title] tries to muffle her moans as you start to finger her eagerly. Her soft gasps are incredibly arousing."
                $ the_person.change_arousal(15)
                if the_person.arousal_perc > 100:
                    the_person "Oh god... ohhh!"
                    "Her whole body tenses up and she pushes back against you. A shiver runs through her body as she climaxes."
                    $ the_person.call_dialogue("climax_responses_foreplay")
                    $ the_person.have_orgasm(the_position = "standing_doggy", half_arousal = True)
                    $ the_person.change_slut(1, 60)
                    "She quivers with pleasure for a few seconds before her whole body relaxes."
                elif the_person.arousal_perc > 50:
                    "You pull your fingers out for a moment. A long strand of her juices connects your fingers to her soaking wet cunt."
                    mc.name "Wow, you are soaked. I'm glad you are enjoying this as much as I am."
                    "You push your two fingers back inside of her and finger her for a bit longer."
                else:
                    "[the_person.title] lets out a little gasp now and then as she tries to continue working at the computer terminal."
                    "Her body is just starting to get warmed up."

            "Finger her ass{color=#FFFF00}-10{/color} {image=gui/extra_images/energy_token.png}" if the_person.opinion_score_anal_sex() >= 0 and the_person.vagina_available()and (the_person.sluttiness > 40 or the_person.obedience > 150):
                if not ass_lubed:
                    "You decide to stretch her ass hole a bit, but first, you need to get it lubed up."
                    if the_person.arousal_perc > 50: #Use her natural arousal to lube her up.
                        "You take two fingers and push them into her soaking wet cunt, pumping them inside her a few times."
                        "Once they are good and wet, you pull them out, then run them along her puckered hole."

                    else:
                        if fingers_wet:
                            "You bring your fingers up to your mouth. You can taste her cunt on your fingers from when you fingered her earlier."
                            "You slobber on them excessively, then spit a large wad of saliva onto her puckered hole."
                        else:
                            "Your bring your fingers up to your mouth and slobber on them excessively."
                            "You spit a large wad of saliva onto her puckered hole."
                    the_person "S... sir?"
                    mc.name "Shh, I already told you, this is for my benefit. Just keep working."
                    the_person "Yes [the_person.mc_title]..."
                    "Slowly, you push one finger into her puckered back door. There's a bit of resistance, but you manage to get it in."
                    the_person "Aahh.... mmm..."
                    $ ass_lubed = True
                    "You pull your finger out, then spit onto them for more lube. This time, you easily slide both fingers into her bottom."
                else:
                    "Still lubed up from earlier, you easily slide two fingers into [the_person.possessive_title]'s bottom."
                the_person "Oh F..."
                $ mc.change_energy(-10)
                mc.name "Are you still working? You better be."
                the_person "Y... yes sir!"
                "[the_person.possessive_title] tries to muffle her groans as you finger her puckered hole."
                $ the_person.change_arousal(20)
                if the_person.arousal_perc > 100:
                    the_person "Oh god... ohhh!"
                    "Her whole body tenses up and she pushes back against you. A shiver runs through her body as she climaxes."
                    the_person "Your fingers... oh fuck!"
                    $ the_person.have_orgasm(the_position = "standing_doggy", half_arousal = True)
                    $ the_person.change_slut(1, 70)
                    "She quivers with pleasure for a few seconds before her whole body relaxes."
                elif the_person.arousal_perc > 50:
                    "[the_person.possessive_title]'s cunt is leaking juices as you finger her forbidden hole."
                    mc.name "You are such a good slut, you like my fingers in your tight little asshole, don't you?"
                    the_person "Yes [the_person.mc_title]!"
                    "You stroke her depths for a while longer as she tries to work at her terminal."
                else:
                    "[the_person.title] lets out a little gasp now and then as she tries to continue working at the computer terminal."
                    "Her body is warming up quickly from your touch as you stroke her depths a little longer."

            # "Finger her ass and pussy{color=#FFFF00}-10{/color} {image=gui/extra_images/energy_token.png}" if the_person.opinion_score_anal_sex() >= 0 and the_person.vagina_available()and (the_person.sluttiness > 50 or the_person.obedience > 160):
            #     pass
            "Finish":
                $ loop_choice = "finish"

        if loop_choice == "finish":
            "You are done with teasing yourself for now."
        else:
            #Right here we need the option to interact with other people in the room.
            if the_person.vagina_available():
                $ mc.change_locked_clarity(30)
            else:
                $ mc.change_locked_clarity(10)
            if mc.arousal > 90 or mc.energy < 20:
                $ loop_choice = "finish"
                "You decide that it is time to stop teasing yourself."
            if get_lust_tier() >= 4 or (get_lust_tier() * 2 > mc.focus):
                $ loop_choice = "finish"
                "You stare blankly at the ass in front of you. You are painfully turned on and can't focus anymore."
                "The teasing has gone far enough. You need to stop now or move on."
    return
