init 5 python:
    config.label_overrides["morning_shower_label"] = "morning_shower_enhanced_label"

    def apply_towel_outfit(person):
        towel_outfit = Outfit("Towel")
        towel_outfit.add_dress(towel.get_copy()) #TODO: Decide if we want a head towel here, maybe just for mom or just for Lily
        person.apply_outfit(towel_outfit)
        return

label morning_shower_enhanced_label(): #TODO: make a similar event for your Aunt's place.
    # You wake up and go to take a shower, lily or your mom are already in there.
    "You wake up in the morning uncharacteristically early feeling refreshed and energized. You decide to take an early shower to kickstart the day."
    $ the_person = get_random_from_list(people_in_mc_home() + [None]) #Checks all the rooms in player's home
    if the_person is None or the_person.has_queued_event("sleeping_walk_in_label"):
        #You run into nobody, gain some extra energy. TODO: One of the girls comes to join you.
        "You head to the bathroom and start the shower. You step in and let the water just flow over you, carrying away your worries for the day."
        "After a few long, relaxing minutes it's time to get out. You start the day feeling energized."
        $ mc.change_energy(20)
        return

    "You head to the bathroom, but hear the shower already running inside when you arrive."

    menu:
        "Skip your shower":
            "With the bathroom occupied you decide to get some extra sleep instead."

        "Knock on the door":
            # She says she'll be "out in a minute", or invites you in. Give her a shower outfit.
            "You knock on the door a couple of times and wait for a response."
            if the_person.effective_sluttiness(["bare_tits","bare_pussy"]) > 30:
                the_person "It's open, come on in!"
                $ home_shower.show_background()
                $ the_person.apply_outfit(Outfit("Nude"))
                $ the_person.draw_person(position = "back_peek")
                "You open the door and see [the_person.possessive_title] in the shower."
                call girl_shower_enter_enhanced(the_person) from _call_girl_shower_enter_enhanced_1
            else:
                the_person "Just a second!"
                call girl_shower_leave_enhanced(the_person) from _call_girl_shower_leave_enhanced_1

        "Peek Inside":
            $ home_shower.show_background()
            $ apply_towel_outfit(the_person)
            $ the_person.draw_person(position = "walking_away")
            "You see [the_person.possessive_title] is standing in front of a mirror, getting ready for a shower, undressing herself."

            $ the_person.strip_outfit(position = "walking_away", exclude_feet = False)

            "Now completely nude, she gets into the shower."
            "You see the water running down her chest."
            $ the_person.draw_person(position = "stand3", emotion = "happy")
            "[the_person.possessive_title] turns around, with the water now going on her back and firm ass."
            if the_person.has_large_tits():
                "You can't help but admire [the_person.possessive_title]'s great body and [the_person.tits_description]."
                "Just as this thought flashes through your mind, she starts rubbing her boobs."
            else:
                "You can't help but admire [the_person.possessive_title]'s slim body and [the_person.tits_description]."
                "Just as this thought flashes through your mind, she starts rubbing her breasts, pinching her small nipples."
            $ mc.change_locked_clarity(10)
            $ the_person.change_arousal(renpy.random.randint(10,50))
            if the_person.effective_sluttiness() >=50 or the_person.get_opinion_score("masturbating") > 0 or the_person.arousal > 35:
                call morning_shower_masturbation() from _call_morning_shower_masturbation_enhanced

            menu:
                "Go Inside":
                    if the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) <= 20:
                        $ the_person.draw_person(emotion = "angry")
                        the_person "What the fuck [the_person.mc_title]! Can't you see it's occupied?"
                        mc.name "The door was unlocked, I thought you might have already been finished."
                        the_person "Knock next time, okay? I'll be done in a minute."
                        "She shoos you out of the room, seeming more upset about being interrupted than being seen naked."
                        $ hall.show_background()
                        $ clear_scene()
                        $ the_person.change_stats(love = -2, happiness = -2)
                        call girl_shower_leave_enhanced(the_person) from _call_girl_shower_leave_enhanced_4
                    else:
                        "She looks up at you, slightly startled, and turns her body away from you."
                        the_person "Oh, [the_person.mc_title]!"
                        mc.name "I'm just here to have a shower."
                        the_person "I should be finished soon, if you don't mind waiting."
                        $ the_person.update_outfit_taboos()
                        call girl_shower_enter_enhanced(the_person) from _call_girl_shower_enter_enhanced_2

                "Walk away":
                    pass

        "Barge in":
            # Locked, unless the girl is slutty enough that you wouldn't mind (TODO: add a "make changes to the house" option where you can't lock the door so you can barge in on lily.)
            if the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) < 10:
                "You try and open the door, but find it locked."
                the_person "One second!"
                call girl_shower_leave_enhanced(the_person) from _call_girl_shower_leave_enhanced_2
            elif the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) <= 20:
                $ home_shower.show_background()
                #She's angry that you've barged in on her (but she doesn't mind enough to have locked the door).
                $ the_person.apply_outfit(Outfit("Nude"))
                #$ the_person.outfit = Outfit("Nude") #changed v0.24.1
                $ the_person.draw_person(emotion = "angry")
                $ mc.change_locked_clarity(10)
                "You open the door. [the_person.possessive_title] is standing naked in the shower. She spins around and yells in surprise."
                the_person "[the_person.mc_title]! I'm already in here, what are you doing?"
                mc.name "The door was unlocked, I thought you might have already been finished."
                the_person "Knock next time, okay? I'll be done in a minute."
                "She shoos you out of the room, seeming more upset about being interrupted than being seen naked."
                $ hall.show_background()
                $ clear_scene()
                $ the_person.change_stats(love = -1, slut = 2)
                call girl_shower_leave_enhanced(the_person) from _call_girl_shower_leave_enhanced_3
            else:
                $ home_shower.show_background()
                $ the_person.apply_outfit(Outfit("Nude"))
                $ the_person.draw_person(position = "back_peek")
                "You open the door and see [the_person.possessive_title] in the shower."
                "She looks up at you, slightly startled, and turns her body away from you."
                the_person "Oh, [the_person.mc_title]!"
                mc.name "I'm just here to have a shower."
                the_person "I should be finished soon, if you don't mind waiting."
                $ the_person.update_outfit_taboos()
                call girl_shower_enter_enhanced(the_person) from _call_girl_shower_enter_enhanced_3

    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    $ clear_scene()
    return

label morning_shower_masturbation():
    "The warmth of the water and her caresses seem to turn [the_person.possessive_title] on."
    $ the_person.draw_person(position = "missionary")
    "She sits on the shower floor, spreads her legs and begins to masturbate with her hand."
    while the_person.arousal < 100:
        $ ran_num = renpy.random.randint(0,4)
        if ran_num == 0:
            "[the_person.possessive_title] rubs her clit and her moans grow louder."
        elif ran_num == 1:
            "As she gets more and more turned on, her hand is moving faster and faster."
        elif ran_num == 2:
            "She pushes three fingers inside, making a deep guttural noise."
            the_person "Ahh, yes. Fuck me hard and deep."
        elif ran_num == 3:
            if the_person.get_opinion_score("anal sex") > 0:
                "She slow pushes a finger in her rectum..."
                the_person "Mmmm, yes, make me your little anal slut."
            else:
                "[the_person.possessive_title] moves two fingers along her labia, quietly moaning with pleasure."
        else:
            if the_person.get_opinion_score("being submissive") > 0:
                "[the_person.possessive_title] pinches her nipples hard, wincing from excitement and pain."
            else:
                if the_person.has_large_tits():
                    "With one hand she softly squeezes her [the_person.tits_description]."
                else:
                    "With one hand she squeezes her [the_person.tits_description]."
        $ the_person.change_arousal(renpy.random.randint(20,35))
        $ mc.change_locked_clarity(10)
    the_person "Shit, I'm cumming!"
    $ the_person.run_orgasm()
    $ the_person.draw_person(position = "missionary", emotion = "orgasm")
    "You see [the_person.possessive_title]'s body shiver as she reaches orgasm."
    the_person "Wow, that was intense. Need to be quieter or someone might just hear me."
    $ the_person.draw_person(position = "walking_away")
    "She gets up and returns to washing her body."
    "You see her love juices mixing with the water dripping on the floor."
    $ the_person.reset_arousal()
    return

label girl_shower_leave_enhanced(the_person):
    "After a short pause the shower stops and you hear movement on the other side of the door."
    $ apply_towel_outfit(the_person)
    $ the_person.draw_person()
    "The bathroom door opens and [the_person.possessive_title] steps out from the steamy room in a towel."
    $ mc.change_locked_clarity(5)
    if the_person is mom:
        the_person "There you go [the_person.mc_title], go right ahead."
        "She gives you a quick kiss and steps past you."
    else:
        the_person "There, it's all yours. I might have used up all of the hot water."
        "She steps past you and heads to her room."
    return


label girl_shower_enter_enhanced(the_person):
    menu:
        "Wait and watch her shower":
            "You nod and head to the sink to brush your teeth. You lean on the sink and watch [the_person.title] while you brush."
            if the_person.effective_sluttiness() > 40 - (5 * (the_person.get_opinion_score("showing her tits")+the_person.get_opinion_score("showing her ass"))):
                $ the_person.discover_opinion("showing her tits")
                $ the_person.discover_opinion("showing her ass")
                "She notices you watching, but doesn't seem to mind the attention."
                $ the_person.change_slut(1+(the_person.get_opinion_score("showing her tits")+the_person.get_opinion_score("showing her ass")))
            else:
                the_person "It's strange to shower with someone else in the room."
                mc.name "Nothing to worry about, we're all family here, right?"
                "She shrugs and nods, but you notice she's always trying to shield her body from your view."
                $ the_person.change_slut(1)
                $ the_person.change_obedience(1)
            $ the_person.update_outfit_taboos()
            $ mc.change_locked_clarity(10)
            "Soon enough she's finished. She steps out and grabs a towel, but leaves the shower running for you."

            $ apply_towel_outfit(the_person)
            $ the_person.draw_person()
            the_person "There you go. Enjoy!"
            $ clear_scene()
            "She steps past you and leaves. You get into the shower and enjoy the relaxing water yourself."
            $ mc.change_energy(20)

        "Join her in the shower" if the_person.obedience >= 120:
            mc.name "How about I just jump in, I can get your back and we'll both save some time."
            if the_person.effective_sluttiness() > 40:
                the_person "Sure, if you're okay with that. I will put you to work though."
                "She gives you a warm smile and invites you in with her."
            else:
                the_person "I'm not sure..."
                mc.name "I've got work to get to today, so I'm getting in that shower."
                "[the_person.possessive_title] nods meekly."
                the_person "Okay."

            "You strip down and get in the shower with [the_person.title]. The space isn't very big, so she puts her back to you."
            "You're left with her ass inches from your crotch, and when she leans over to pick up the shampoo she grinds up against you."
            $ mc.change_locked_clarity(20)
            the_person "Oops, sorry about that."
            "Your cock, already swollen, hardens in response, and now even stood up the tip brushes against [the_person.possessive_title]'s ass."
            if the_person.effective_sluttiness("touching_body") <= 40:
                the_person "I think I'm just about done, so you can take care of this..."
                "She wiggles her butt and strokes your tip against her cheeks."
                $ mc.change_locked_clarity(10)
                $ the_person.change_slut(1 + the_person.get_opinion_score("showing her ass"))
                "She steps out of the shower and grabs a towel."
                $ apply_towel_outfit(the_person)
                $ the_person.draw_person()
                the_person "See you next time."
                $ clear_scene()
                "She leaves the room and you finish your shower alone, feeling refreshed by the water."
                $ mc.change_location(bedroom)

            # elif the_person.effective_sluttiness() <= 60: #TODO: Add a "hot dog" position and make it a starting position for this.
            #     "She wiggles her butt and strokes your tip against her cheeks."
            #     the_person "Do you need some help with this? How about you just... use my butt?"
            #     $ the_person.draw_person("walking_away")
            #     "She rubs up against you while you talk, stroking your shaft with her wet, slippery ass."
            #     menu:
            #         "Jerk off with her ass":
            #
            #         "Just have a shower":


            else:
                the_person "What is this?"
                "She wiggles her butt and strokes your tip against her cheeks."
                $ mc.change_locked_clarity(10)
                the_person "Well we need to take care of this, don't we..."
                "She turns around and faces you. It might be the hot water, but her face is flush."
                $ the_person.change_slut(2)
                menu:
                    "Fuck her" if not the_person.has_taboo("vaginal_sex"): # only show sex option if you had sex before
                        $ mc.change_location(home_shower)
                        call fuck_person(the_person, skip_intro = True) from _call_fuck_person_shower_enhanced_1
                        $ the_report = _return

                        $ apply_towel_outfit(the_person)
                        $ the_person.draw_person()
                        "When you're finished [the_person.title] steps out of the shower and grabs a towel. She dries herself off, then wraps herself in it and turns to you."
                        if the_report.get("girl orgasms",0)>0:
                            the_person "Well that's a good way to start the day. See you later."
                        elif the_report.get("guy orgasms",0)>0:
                            the_person "Well I hope you enjoyed your start to the day. See you later."
                        else:
                            the_person "Well maybe we can pick this up some other time. See you later."

                        $ clear_scene()
                        "She leaves the room and you finish your shower alone, feeling refreshed by the water."
                        $ mc.change_location(bedroom)

                    "Just have a shower":
                        mc.name "Maybe some other time, I've got to hurry up though."
                        "She pouts and nods."
                        $ the_person.change_obedience(1)
                        the_person "Alright, up to you."

            $ mc.change_energy(20)


        "Join her in the shower\n{color=#ff0000}{size=18}Requires: 120 Obedience{/size}{/color} (disabled)" if the_person.obedience < 120:
            pass

    return
