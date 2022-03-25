init 5 python:
    config.label_overrides["horny_at_work_crisis_label"] = "horny_at_work_crisis_enhanced_label"

    def horny_at_work_get_licker(helpful_people):
        licker = None
        for person in helpful_people:
            person.change_obedience(3)
            person.change_slut(1)
            if person.has_cum_fetish() and licker is None:
                licker = person
            if person.get_opinion_score("being submissive") > 0 and person.get_opinion_score("drinking cum") > 0 and licker is None:
                licker = person #The list was randomized, so even if you have multiple people who meet this criteria this should still end up random.
        return licker

    def horny_at_work_strip_down(person):
        for clothing in person.outfit.get_half_off_to_vagina_list():
            scene_manager.draw_animated_removal(person, clothing, half_off_instead = True)
            if person.outfit.vagina_available():
                renpy.say(None,"You pull her " + clothing.display_name + " out of the way so you can get to her pussy.")
            else:
                renpy.say(None,"You pull her " + clothing.display_name + " out of the way.")
        return

    def horny_at_work_get_people_sets():
        unhappy_people = [] #They're surprised/shocked/disgusted that you're doing this.
        neutral_people = [] #They're neither surprised that you're doing this, nor willing to come help out.
        masturbating_people = []
        helpful_people = [] #They're happy to come over and help you take care of your "needs"
        for person in mc.location.people:
            person.discover_opinion("public sex")
            if person.sluttiness < (30 - person.get_opinion_score("public sex")*10):
                unhappy_people.append(person)

            elif person.obedience > (130 - (person.get_opinion_score("being submissive")*10)):
                helpful_people.append(person)

            else:
                neutral_people.append(person)

        for person in neutral_people:
            if person.get_opinion_score("masturbating") > 0 and person.sluttiness >= 40:
                masturbating_people.append(person)

        renpy.random.shuffle(unhappy_people)
        renpy.random.shuffle(neutral_people)
        renpy.random.shuffle(masturbating_people)
        renpy.random.shuffle(helpful_people)
        return (unhappy_people, neutral_people, masturbating_people, helpful_people)

label horny_at_work_crisis_enhanced_label():
    $ (the_person, the_cause) = horny_at_work_get_person_and_cause()

    if the_cause == "slutty_outfit":
        $ the_person.draw_person(position = "walking_away")
        "You're at your desk, trying hard to focus. Unfortunately, [the_person.title]'s outfit keeps grabbing your attention."
        "The more you try and ignore her the hornier you get, and it's starting to get in the way of your work."

    elif the_cause == "large_tits":
        $ the_person.draw_person(position = "sitting")
        "You're at your desk, trying hard to focus. Unfortunately, [the_person.title]'s nice, [the_person.tits_description] keep grabbing your attention."
        "The more you try and ignore them the hornier you get, and it's starting to get in the way of work."

    elif the_cause == "vagina_visible":
        $ the_person.draw_person(position = "back_peek")
        "You're at your desk, trying hard to focus. Unfortunately, [the_person.title]'s outfit leaves her sweet little pussy on display and it keeps grabbing your attention."
        "The more you try and ignore it the hornier you get, and it's starting to get in the way of your work."

    elif the_cause == "tits_visible":
        $ the_person.draw_person()
        if the_person.has_large_tits():
            "You're at your desk, trying hard to focus. Unfortunately, [the_person.title]'s [the_person.tits_description] are on prominent display, bouncing pleasantly every time she takes a step."
            "The more you try and ignore them the hornier you get, and it's starting to get in the way of your work."
        else:
            "You're at your desk, trying hard to focus. Unfortunately, [the_person.title]'s [the_person.tits_description] are on display and make your mind wander."
            "The more you try and ignore them the hornier you get, and it's starting to get in the way of your work."

    else:
        "You're at your desk, trying hard to focus. Unfortunately your libido is getting the better of you, and you're getting horny."
        "The more you try and ignore your growing erection the more distracting it becomes, and it's starting to get in the way of your work."


    menu:
        "Ignore it\n{color=#ff0000}{size=18}-10%% Business Efficiency{/size}{/color} (tooltip)Ignore your arousal through sheer willpower. It might save you some embarrassment, but your business efficiency is sure to suffer":
            $ clear_scene()
            "Putting mind over matter into action you redouble your efforts. Time seems to pass slowly and it seems like you're getting no work done at all."
            $ mc.business.change_team_effectiveness(-10)
            "When your erection dies down and you're able to think clearly again you're sure you've made several paperwork mistakes. Sorting this out will take yet more work."

        "Jerk off at your desk (tooltip)With nobody around, what's stopping you?" if not mc.location.people:
            "There's no reason to be self conscious when you're all by yourself inside your own business. You lean back in your chair and unzip your pants."
            call bedroom_masturbation(location_description = "work", edging_available = False, should_advance_time = False) from _call_bedroom_masturbation
            "You tidy up and get back to work, feeling much more focused."

        "Jerk off at your desk, loud and proud (tooltip)Your company, your rules, right?" if mc.location.people:
            $ clear_scene()
            $ scene_manager = Scene()
            # Girls around the room react. If some are particularly obedient and slutty they will offer to help get you off.
            "You wheel your chair back to give yourself some space, then unzip your pants and pull out your cock. You relax and start to jerk yourself off."

            $ unhappy_people, neutral_people, masturbating_people, helpful_people = horny_at_work_get_people_sets()

            if unhappy_people: #There's someone in this list.
                $ active_person = get_random_from_list(unhappy_people) #Someone to lead the unhappy group, if there is more than one person.
                $ clear_scene()

                $ scene_manager.add_group(unhappy_people, position = "sitting")

                if mc.location.get_person_count() == 1: #She's the only person in the room.
                    "It doesn't take long for [active_person.title] to notice what you're doing. When she glances over she does a double take before gasping and yelling out."
                else: #It's more than one person
                    "It doesn't take long for someone to notice what you're doing. When [active_person.title] glances at you she does a double take before gasping and yelling out."
                $ scene_manager.update_actor(active_person, emotion = "angry")
                active_person "Oh my god, what are you doing? [active_person.mc_title], are you insane?!"
                if mc.location.get_person_count() > 1:
                    "The rest of the office girls look up from their work, surprised by the sudden interruption."
                "You lock eyes with her as you stroke your cock."
                mc.name "I'm taking a break and blowing off some steam. If you're uncomfortable you're welcome to leave."

                $ active_person.change_stats(happiness = -30, obedience = -2)

                "She tries to glare at you, but she can't keep her eyes from drifting down to your hard shaft."
                "When it becomes clear you aren't going to stop, let alone apologize, she stands up and storms out of the room."
                $ unhappy_people.remove(active_person)
                $ active_person.change_location(lobby)
                $ scene_manager.remove_actor(active_person)
                if len(unhappy_people) == 0: #She was the only other unhappy person, we're done here
                    pass
                elif len(unhappy_people) == 1:
                    $ renpy.say(None, unhappy_people[0].title + " joins her as she leaves, giving you the same look of disgust as she gets up from her desk.")
                    $ scene_manager.remove_actor(unhappy_people[0])
                else:
                    #There are two or more people. Let's construct a title string!
                    $ renpy.say(None,format_group_of_people(unhappy_people) + " storm out of the room with her, shaking their heads as they leave.")

                python:
                    for unhappy_person in unhappy_people: #Note that the main person was removed from the list so these penalties aren't being applied twice.
                        unhappy_person.change_stats(happiness = -30, obedience = -2)
                        unhappy_person.change_location(lobby) #Move everyone to the lobby so they aren't considered observers for the rest of teh event.
                        scene_manager.remove_actor(unhappy_person)
                    unhappy_person = None
                    clear_scene() #TODO We should have an event for the angry girls coming back (maybe we need a general apology event?)
                    scene_manager.clear_scene()
                    del active_person

            if neutral_people:
                $ scene_manager.add_group(neutral_people, position = "sitting")
                if len(neutral_people) > 1:
                    $ renpy.say(None, format_group_of_people(neutral_people) + " all see you jerking off at your desk, but none of them seem upset or surprised by it.")
                else:
                    $ renpy.say(None, format_group_of_people(neutral_people) + " notices you jerking off, but she doesn't seem upset or surprised by it.")

                if masturbating_people:
                    python:
                        for mast_person in masturbating_people:
                            scene_manager.update_actor(mast_person, position = "missionary", emotion = "happy")
                            scene_manager.strip_actor_strip_list(mast_person, mast_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)

                        if len(masturbating_people) == 1:
                            renpy.say(None, format_group_of_people(masturbating_people) + " even joins in, quietly sliding her hand down to her crotch and rubbing her pussy.")
                        elif len(masturbating_people) == 2:
                            renpy.say(None, format_group_of_people(masturbating_people) + " even join in, both sliding their hands down to their pussies and rubbing them quietly.")
                        else:
                            renpy.say(None, format_group_of_people(masturbating_people) + " all quietly join in as well, quietly sliding hands down to their pussies and joining the group masturbation session.")

            if helpful_people:
                $ active_person = get_random_from_list(helpful_people)
                $ scene_manager.clear_scene()
                $ clear_scene()
                $ active_person.draw_person(emotion = "happy", position = "stand3")
                "[active_person.title] gets up from her desk and comes over, eyes transfixed on your swollen cock."
                active_person "Would you like to use me to take care of that?"
                $ clear_scene()
                $ scene_manager.add_group(helpful_people, position = "stand3", emotion = "happy")
                if len(helpful_people) > 1: #More than one person, so describe them!
                    $ others = [x for x in helpful_people if x not in [active_person]]
                    if len(others) == 1:
                        $ renpy.say(None, format_group_of_people(others) + " gets up and stands behind [active_person.possessive_title], obviously willing to do the same.")
                    elif len(others) == 2:
                        $ renpy.say(None, format_group_of_people(others) + " both get up and stand behind [active_person.possessive_title], obviously willing to do the same.")
                    else:
                        $ renpy.say(None, format_group_of_people(others) + " all get up and stand behind [active_person.possessive_title], obviously willing to do the same.")
                    $ del others
                $ del active_person

                if len(helpful_people) > 1:
                    $ exit_option = "Just have them watch"
                else:
                    $ exit_option = "Just have her watch"

                if "action_mod_list" in globals():
                    call screen enhanced_main_choice_display(build_menu_items([build_helpful_people_menu(helpful_people, exit_option)]))
                else:
                    call screen main_choice_display([build_helpful_people_menu(helpful_people, exit_option)]) #Shows a list of people w/ predictive imaging when you hover

                if not isinstance(_return, Person):
                    $ scene_manager.draw_scene()
                    #Power move, just jerk yourself off as they watch.
                    mc.name "I've got things under control, but I'd like you to stay and watch."
                    "You stroke your cock faster and faster, pulling yourself towards your orgasm."
                    if len(helpful_people) > 1: #Two or more girls
                        "The girls stand by and watch you masturbate. They shift their weight from side to side, rubbing their thighs together in an obvious display of arousal."
                    else:
                        "She stands by and watches as you masturbate, shifting her weight from side to side in an obvious display of arousal."
                    "When you reach the point of no return you lean back in your chair and grunt, firing your load in a long arc until it splatters over the floor."
                    $ ClimaxController.manual_clarity_release()
                    "You catch your breath and sit up."
                    mc.name "Whew. Now you can be helpful by getting that cleaned up for me."

                    $ licker = horny_at_work_get_licker(helpful_people)
                    if licker is not None:
                        $ scene_manager.update_actor(licker, display_transform = character_right, position = "doggy")
                        "Before you even finish the sentence [licker.title] is on her hands and knees, lowering her face to the floor."
                        licker "Right away!"
                        $ licker.change_obedience(2)
                        "She licks your still-warm cum directly off of the floor, drinking it down eagerly."
                        $ scene_manager.update_actor(licker, position = "stand3")
                        $ mc.change_locked_clarity(30)
                        "When she's finished she stands up and wipes her lips with the back of her hand."
                    else:
                        $ licker = get_random_from_list(helpful_people)
                        licker "Let me take care of that, [licker.mc_title]."
                        $ scene_manager.update_actor(licker, position = "doggy", display_transform = character_right, emotion = "happy")
                        $ mc.change_locked_clarity(5)
                        "You watch [licker.title] get on her hands and knees to clean up the mess you made."
                    $ del licker
                    $ scene_manager.update_scene(position = "sitting", emotion = "happy")
                    "The girls go back to their workstations, happy with the distraction you provided them."
                    "You pull your pants up and get back to work, basking in your post-orgasm clarity."

                else:
                    $ active_person = _return
                    $ scene_manager.update_actor(active_person, position = "stand3")
                    "You stand up, pants around your ankles, and motion for [active_person.title] to come over to you."
                    $ clear_scene()
                    call fuck_person(active_person, private = False, skip_intro = True) from _call_fuck_person_horny_at_work_enhanced_1
                    $ the_report = _return
                    $ active_person.review_outfit()
                    $ helpful_people.remove(active_person)
                    $ wants_to_continue = True
                    while mc.energy >= 20 and len(helpful_people) > 0 and wants_to_continue:
                        $ clear_scene
                        $ scene_manager.update_actor(active_person, position = "sitting")
                        if the_report.get("girl orgasms", 0) > 0:
                            "[active_person.title] stumbles back to her desk and collapses into her chair, legs still quivering."
                        else:
                            $ scene_manager.update_actor(active_person, position = "missionary", emotion = "happy")
                            "[active_person.title] goes back to her desk and sits down when you're finished with her. She spreads her legs and starts to touch herself."

                        if len(helpful_people) > 1:
                            "The other girls are still standing next to your desk, and you haven't exhausted yourself quite yet..."
                        else:
                            $ renpy.say(None, helpful_people[0].title + " is still standing next to your desk, and you haven't exhausted yourself quite yet...")

                        $ exit_option = "Finish up"
                        if "action_mod_list" in globals():
                            call screen enhanced_main_choice_display(build_menu_items([build_helpful_people_menu(helpful_people, exit_option)]))
                        else:
                            call screen main_choice_display([build_helpful_people_menu(helpful_people, exit_option)]) #Shows a list of people w/ predictive imaging when you hover

                        if not isinstance(_return, Person):
                            if len(helpful_people) > 1:
                                "You wave the girls back to their desk. They seem disappointed they didn't get a chance to service you."
                            else:
                                "You wave her back to her desk. She seems disappointed that she didn't get a chance to service you."
                            $ wants_to_continue = False

                        else:
                            $ active_person = _return
                            mc.name "[active_person.title], you're next."
                            $ scene_manager.update_actor(active_person, position = "stand3")
                            "She nods and smiles, stepping forward."
                            $ clear_scene()
                            call fuck_person(active_person, private = False, report_log = the_report) from _call_fuck_person_horny_at_work_enhanced_2
                            $ active_person.review_outfit()
                            $ helpful_people.remove(active_person)
                    $ del active_person

                    if the_report.get("guy orgasms",0) == 0:
                        "You've worn yourself out, but you still haven't gotten off. You relax in your office chair and stroke yourself off until you cum."
                        $ ClimaxController.manual_clarity_release()
                        "With that finally taken care of, you get yourself cleaned up and get back to work."
                        "Thanks to your post-orgasm clarity you're able to focus perfectly."
                    elif the_report.get("guy orgasms",0) == 1:
                        "You sit back down in your office chair, feeling satisfied."
                        "After getting yourself cleaned up you're able to focus perfectly again and you get back to work."
                    elif the_report.get("guy orgasms",0) > 1:
                        "You sit back down in your office chair, feeling completely drained, being satisfied multiple times."
                        "After getting yourself cleaned up you're able to focus perfectly again and you get back to work."

            else: #You get yourself off.
                "You pull up some porn and, with a skill trained over many years, you start jerking off."
                if masturbating_people:
                    "Some of the girls get comfortable and start enjoying themselves while watching you."
                    python:
                        scene_manager.clear_scene()
                        scene_manager.add_group(masturbating_people, position = "sitting", emotion = "happy")
                        for mast_person in masturbating_people:
                            scene_manager.update_actor(mast_person, position = "missionary", emotion = "happy")
                            scene_manager.strip_actor_strip_list(mast_person, mast_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)

                "When you're finished you clean up and get back to work with your mind clear and able to focus."
                if masturbating_people:
                    if len(masturbating_people) > 1:
                        "Not long after you're finished you hear girls around the office climax, each one punctuated by a little gasp and moan."
                    else:
                        $ renpy.say(None, "Not long after you hear a gasp and a moan as " + masturbating_people[0].title + " brings herself to climax as well.")
                    $ mc.change_locked_clarity(5*len(masturbating_people))

            python:
                scene_manager.clear_scene()
                for mast_person in masturbating_people:
                    mast_person.apply_planned_outfit()
                clear_scene()
                del unhappy_people
                del neutral_people
                del masturbating_people
                del helpful_people
                mast_person = None

        "Sneak away to the bathroom and jerk off (tooltip)A few minutes in private should fix this right up." if mc.location.people: #If there are people around here's an option to jerk off. There might
            $ clear_scene()
            $ scene_manager = Scene()
            "You're going to need to get this taken care of if you want to get any work done."
            "You get up from your desk and head for the washrooms, attempting to hide your erection from your staff as you go."

            $ active_person = horny_at_work_get_follower()
            if active_person is not None:
                #You were followed.
                $ old_location = mc.location
                $ mc.change_location(work_bathroom)
                $ mc.location.show_background()
                "You relax when you reach the bathroom, but a moment after you enter [active_person.title] opens the door and comes inside too."
                $ active_person.draw_person()
                mc.name "[active_person.title], I..."
                active_person "It's okay. I saw you sneaking away and thought I'd join you. In case you wanted some company..."
                $ mc.change_locked_clarity(5)
                menu:
                    "Let her join you":
                        mc.name "Alright then, get over here."
                        call fuck_person(active_person, private = True) from _call_fuck_person_horny_at_work_enhanced_3
                        $ the_report = _return
                        $ active_person.review_outfit()
                        $ active_person.draw_person()
                        if the_report.get("guy orgasms", 0) == 0:
                            "Despite the fun you had with [active_person.title] you still haven't cum yet."
                            mc.name "You run along, I've still got to deal with this."
                            $ active_person.draw_person(position = "walking_away")
                            "She leaves you alone in the bathroom, and you jerk yourself off to completion."
                            $ clear_scene()
                            $ ClimaxController.manual_clarity_release()
                        else:
                            "You and [active_person.possessive_title] leave the bathroom together."
                        "When you get back to your desk you find you're finally able to focus again."

                    "Tell her to leave":
                        mc.name "If I wanted you to come I would have told you to. I'd like some privacy, please."
                        $ active_person.change_happiness(-5)
                        $ active_person.change_obedience(2)
                        $ active_person.draw_person(emotion = "sad")
                        active_person "I... Oh, I'm sorry [active_person.mc_title], I don't know what I was thinking..."
                        $ active_person.draw_person(position = "walking_away")
                        "She blushes and turns around, leaving quickly."
                        $ clear_scene()
                        call bedroom_masturbation(location_description = "bathroom", edging_available = False, should_advance_time = False) from _call_bedroom_masturbation_1
                        "When you're finished you clean up and get back to work, your mind now crystal clear."

                    "Punish her for inappropriate behaviour" if office_punishment.is_active():
                        mc.name "[the_person.title], this isn't appropriate. I'm going to have to write you up."
                        active_person "I... Oh, I'm sorry [active_person.mc_title], I don't know what I was thinking..."
                        $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())
                        $ active_person.draw_person(position = "walking_away")
                        "She blushes and turns around, leaving quickly."
                        $ clear_scene()
                        "You pull up some porn on your phone and get comfortable, jerking yourself off until you cum."
                        "When you're finished you clean up and get back to work, your mind now crystal clear."

                $ del active_person
                $ mc.change_location(old_location)
                $ mc.location.show_background()
                $ del old_location

            else:
                "Once you have some privacy you pull some porn up on your phone, pull out your dick, and take matters into your own hand."
                call bedroom_masturbation(location_description = "bathroom", edging_available = False, should_advance_time = False) from _call_bedroom_masturbation_2
                "When you're finished you clean up and get back to work, your mind now crystal clear."


        "Ask [the_person.title] to come over (tooltip)She got you turned on, she should be the one to get you off." if the_person is not None:
            mc.name "[the_person.title], I need you to come over here for a moment."
            the_person "Hmm? What do you need?"
            $ the_person.draw_person()
            "She comes over and stands next to your desk. You wheel your chair back and rub your crotch, emphasizing the obvious bulge."
            mc.name "I think we need to have a talk about the way you act when you're in the office. As you can see, it's a little distracting for the male staff: Me."
            if the_person.effective_sluttiness() < (30 - the_person.get_opinion_score("public sex")*10):
                $ the_person.discover_opinion("public sex")
                "She looks away and gasps."
                the_person "Oh my god, [the_person.mc_title]! I can't believe you're doing this right here!"
                $ the_person.change_stats(happiness = -10, love = -5, obedience = -3)
                $ the_person.draw_person(position = "walking_away")
                "Before you can say anything more she turns around and hurries out of the room."
                the_person "I really need to go..."
                "You sigh and give up on your hopes of a quick release."
                $ clear_scene()
                $ mc.business.change_team_effectiveness(-10)

            else:
                $ clear_scene()
                $ scene_manager = Scene()

                if the_person.obedience > 120:
                    the_person "Oh, I'm so sorry. What can I do to help?"
                else:
                    the_person "Oh... What do you want me to do about it?"
                $ mc.change_locked_clarity(5)

                #TODO: Make sure all of this is context aware in some way for other people in the room.
                $ scene_manager.add_group([x for x in mc.location.people if x != the_person], position = "sitting")
                $ scene_manager.add_actor(the_person, display_transform = character_right, position = "stand3")
                menu:
                    "Make her strip while you jerk off": #The basic version if you've picked this path always enabled due to earlier checks, so we don't bother with a failure state
                        mc.name "Well, I'd like you to give me some entertainment while I take care of this. Strip down and give me a little dance."
                        if mc.location.get_person_count() > 1:
                            "[the_person.title] looks around the room, then back to you and whispers."
                            the_person "What about the other people?"
                            mc.name "I'm sure they won't mind, and if they do they can take it up with me. Come on, I need to get back to work."
                            $ mc.change_locked_clarity(5)
                        else:
                            "[the_person.title] looks around the empty room, then back to you and shrugs."

                        the_person "Fine."
                        $ scene_manager.update_actor(the_person, position = "stand2")

                        if mc.location.get_person_count() > 1:
                            "You slide your chair back and turn it to face her. You unzip your pants, grabbing your already-hard cock to stroke it."
                            $ lead_other = get_random_from_list([x for x in mc.location.people if x not in [the_person]])
                            "[lead_other.title] glances over and notices you jerking off at your desk in front of [the_person.title]."
                            if lead_other.effective_sluttiness() < 20:
                                lead_other "Oh my god, [lead_other.mc_title], what are you doing?"
                                the_person "It's okay [lead_other.title], this is my fault. I've gotten [the_person.mc_title] too horny to work."
                                the_person "So I'm going to help him cum."

                            else:
                                lead_other "[the_person.title], what are you doing?"
                                the_person "I've gotten [the_person.mc_title] too excited, so I'm going to help him jerk off."
                            $ mc.change_locked_clarity(10)
                            $ del lead_other

                            the_person "Don't mind us, I'll try and make this quick."
                        else:
                            "You smile and turn your chair to face her. You unzip your pants and grab onto your hard cock, stroking it slowly."

                        $ the_item = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True) #If that fails we need to strip off her top, because she might have a dress style thing on blocking it.
                        while the_item:
                            $ scene_manager.draw_animated_removal(the_person, the_clothing = the_item)
                            "[the_person.title] strips off her [the_item.name] while you watch."
                            $ the_item = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                        $ the_item = None

                        "When [the_person.possessive_title] is finished stripping down she puts her hands on her hips and watches you jerk off."

                        $ mc.change_locked_clarity(10)
                        $ the_person.discover_opinion("not wearing anything")
                        $ the_person.change_slut(the_person.get_opinion_score("not wearing anything")+1)
                        $ the_person.change_obedience(the_person.get_opinion_score("not wearing anything")+1)

                        if the_person.get_opinion_score("not wearing anything") > 0:
                            "She doesn't seem to care about being naked in front of you; if anything she seems to be enjoying the experience."
                            the_person "Do you have a good view?"
                            $  the_person.draw_person(position = "back_peek")
                            "She gives you a quick spin."
                            $ mc.change_locked_clarity(10)
                            $ the_person.draw_person()
                        elif the_person.get_opinion_score("showing her tits") > 0:
                            if the_person.has_large_tits():
                                "She puts an arm under her [the_person.tits_description] and lifts them up for you, leaning forward a little to emphasize their size."
                                the_person "Do you like my tits? I know a lot of men do, they like to have a big pair of juicy titties in their face."

                            else:
                                "She rubs her [the_person.tits_description], thumbing the nipples until they grow hard."
                                the_person "Do you like my tits? I know some women have bigger ones, but I think these are still pretty cute."
                                the_person "They're just the right size to suck on, don't you think?"
                            $ mc.change_locked_clarity(10)

                        elif the_person.get_opinion_score("showing her ass") > 0:
                            "[the_person.title] turns around unprompted and plants her hands on a desk opposite you."
                            $ the_person.draw_person(position = "standing_doggy")
                            the_person "Do you like my ass, [the_person.mc_title]? Do you want to give it a nice hard smack and make it jiggle?"
                            "She works her hips up and down, making her ass cheeks bounce and clap together."
                            $ mc.change_locked_clarity(10)

                        else:
                            the_person "Come on, I want you to cum so we can get back to work."

                        "You stroke yourself faster, enjoying [the_person.title]'s body on display right in front of you. Finally you feel your orgasm approaching."
                        $ ClimaxController.manual_clarity_release()
                        "You lean back in your chair and grunt as you climax, blowing a hot load of cum in an arc onto the floor in front of you."
                        $ the_person.draw_person()
                        the_person "Wow..."
                        "It takes a few moments of deep breathing to recover from the experience."
                        mc.name "Thank you [the_person.title], that's taken care of the problem nicely."
                        "She gives you a quick smile."
                        $ the_person.review_outfit()
                        $ scene_manager.clear_scene()
                        $ clear_scene()
                        "You pull your pants up and get yourself organized, then turn your attention back to your work with a crystal clear mind."


                    "Make her suck you off":
                        mc.name "Well, I need this taken care of so I can get back to work. I want you to get under my desk and suck me off."
                        if the_person.is_willing(blowjob, private = False):
                            if (the_person.get_opinion_score("public sex") > 0 and mc.location.get_person_count() > 1) or the_person.get_opinion_score("giving blowjobs") > 0:
                                the_person "Okay, if that's what you need."
                                "She gets onto her hands and knees, crawling under your desk and nestling herself between your legs."
                                $ mc.change_locked_clarity(10)
                            else:
                                if mc.location.get_person_count() > 1:
                                    the_person "But... What if someone notices?"
                                    mc.name "I'm sure they will be impressed by what a good job you're doing sucking my cock."

                                else:
                                    the_person "Really? I..."

                                mc.name "Come on, I don't have all day. I need to get back to work."
                                "She hesitates, but after a second of thought she sighs and gets onto her hands and knees, crawling under your desk and nestling herself between your legs."
                            $ scene_manager.update_actor(the_person, position = "blowjob")
                            "You unzip your pants and pull them down, letting your hard cock fall out onto [the_person.possessive_title]'s face."
                            "She places her hands on your thighs and slides your cock into her mouth, licking the tip to get it wet before slipping it further back."
                            $ clear_scene()
                            $ the_person.change_arousal(50)
                            call fuck_person(the_person, private = False, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_person_horny_at_work_enhanced_4
                            $ the_report = _return
                            $ the_person.review_outfit()
                            $ scene_manager.update_actor(the_person, position = "stand3")
                            if the_report.get("guy orgasms", 0) == 0:
                                "Frustrated with her service, you let [the_person.title] out from under your desk and finish yourself off with your hand."
                                $ ClimaxController.manual_clarity_release()
                            else:
                                "Fully spent, you let [the_person.title] out from under your desk and get back to work, mind now crystal clear."
                        else:
                            $ scene_manager.update_actor(the_person, emotion = "angry")
                            the_person "What? Oh my god, I couldn't do that!"
                            $ the_person.change_stats(love = -5, happiness = -10, obedience = -3)
                            "She stammers for something more to say before settling on storming out of the room instead."
                            $ clear_scene()
                            "Frustrated, her rejection has at least taken your mind off of your erection and you're able to get back to work eventually."


                    "Make her fuck you":
                        mc.name "I want you to take some responsibility for this. Come over here so I can fuck you."
                        if the_person.is_willing(missionary, private = False):
                            $ desk = mc.location.get_object_with_name("desk") #May be None if there's no desk where you are.
                            if desk is not None:
                                "You grab [the_person.possessive_title] by her hips and lift her up, putting her down on your desk and positioning yourself between her legs."
                            else:
                                $ desk = make_floor() # fallback to floor
                                "You grab [the_person.possessive_title] by her hips and lay her down in front of you, spreading her legs around you."

                            $ mc.change_locked_clarity(10)
                            $ scene_manager.update_actor(the_person, position = "missionary")
                            if mc.location.get_person_count() > 1 and the_person.effective_sluttiness() < (80 - 10*the_person.get_opinion_score("public sex")):
                                the_person "Ah! Wait, what will the other girls think?"
                                mc.name "I'm sure they'll let us know."
                                $ mc.change_locked_clarity(10)
                            elif the_person.relationship != "Single" and affair_role not in the_person.special_role:
                                $ so_title = SO_relationship_to_title(the_person.relationship)
                                the_person "Wait, I have a [so_title]! I shouldn't let you do this!"
                                "Despite her protest she doesn't try to stand back up or get you out from between her thighs."
                                $ mc.change_locked_clarity(10)
                            else:
                                the_person "Ah!"

                            if the_person.outfit.can_half_off_to_vagina():
                                $ horny_at_work_strip_down(the_person)

                            else: #We need to strip her down completely. TODO: We need a way to determine if we can strip someone half down, then pull things aside (ie. pull off pants, pull panties to the side)
                                $ the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True) #Start by stripping off her bottom.
                                while (the_item and not the_person.outfit.vagina_available()):
                                    $ scene_manager.draw_animated_removal(the_person, the_item)
                                    if the_person.outfit.vagina_available():
                                        "You pull off her [the_item.name] and reveal her pussy, ready for you to use."
                                    else:
                                        "You pull off her [the_item.name], getting closer to revealing her pussy for you to use."
                                    $ the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)

                                $ the_item = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove= True) #If that fails we need to strip off her top, because she might have a dress style thing on blocking it.
                                while (the_item and not the_person.outfit.vagina_available()):
                                    $ scene_manager.draw_animated_removal(the_person, the_item)
                                    if the_person.outfit.vagina_available():
                                        "You pull off her [the_item.name] and reveal her pussy, ready for you to use."
                                    else:
                                        "You pull off her [the_item.name], getting closer to revealing her pussy for you to use."
                                    $ the_item = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove= True)

                                $ the_item = None
                            if the_person.outfit.vagina_available():
                                $ mc.change_locked_clarity(20)
                                "You unzip your pants and pull out your hard cock, laying it onto [the_person.title]'s crotch. You rub the shaft against her pussy lips, teasing her with the tip each time."
                                call condom_ask(the_person) from _call_condom_ask_horny_at_work_enhanced
                                if not _return:
                                    "[the_person.title]'s refusal has sucked the wind from your sails. You zip your pants up and let her leave."
                                    "At least you're no longer feeling as horny as you were, and you're able to get back to work."
                                else:
                                    "You pull back a little and line the tip of your dick up with [the_person.title]'s cunt."
                                    "With one smooth thrust you push yourself inside of her. She arches her head back and moans as you bottom out inside of her."
                                    call fuck_person(the_person, private = False, start_position = missionary, start_object = desk, skip_condom = True, skip_intro = True) from _call_fuck_person_horny_at_work_enhanced_5
                                    $ the_report = _return
                                    $ the_person.review_outfit()
                                    $ scene_manager.update_actor(the_person, position = "stand3")

                                    if the_report.get("guy orgasms", 0) == 0:
                                        "You still haven't gotten off, so you stroke your cock until you cum."
                                        $ ClimaxController.manual_clarity_release()
                                        "With that finally taken care of, you get yourself cleaned up and get back to work."
                                        "Thanks to your post-orgasm clarity you're able to focus perfectly."
                                    else:
                                        "You get yourself cleaned up and get back to work. You're able to focus perfectly now thanks to your post-orgasm clarity."

                            else: #We've been thwarted somehow and can't get to her pussy.
                                "Thwarted by her clothing and unable to dress her down any further, you give up and let her go. The shame of your defeat has, thankfully, killed your erection and you're able to get back to work."
                                $ mc.business.change_team_effectiveness(-10)
                            $ del desk

                        else:
                            $ scene_manager.update_actor(the_person, emotion = "angry")
                            the_person "What? Oh my god, I would never let you do that!"
                            $ the_person.change_stats(love = -5, happiness = -10, obedience = -3)
                            "She stammers for something more to say before settling on storming out of the room instead."
                            $ clear_scene()
                            "Her rejection has killed your erection. You return to work frustrated and distracted."
                            $ mc.business.change_team_effectiveness(-10)

                $ scene_manager.clear_scene()
    $ clear_scene()
    return
