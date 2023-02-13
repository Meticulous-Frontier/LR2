# Enhance hall walk with multi person rendering and updated dialog
init 5 python:
    config.label_overrides["lily_morning_encounter_label"] = "lily_morning_encounter_enhanced_label"

label lily_morning_encounter_enhanced_label():
    # You run into Lily early in the morning as she's going to get some fresh laundry. At low sluttiness she is embarrassed, at high she is completely naked.
    if not lily.is_available:
        return
    python:
        the_person = lily
        comfortable = False
        if the_person.effective_sluttiness() >= 60:
            the_person.apply_outfit(Outfit("Nude"))
        else:
            the_person.apply_outfit(the_person.wardrobe.get_random_appropriate_underwear(the_person.sluttiness, guarantee_output = True))

        if the_person.outfit.wearing_panties() and the_person.outfit.wearing_bra():
            comfortable = True
        elif the_person.outfit.wearing_bra() or the_person.effective_sluttiness("bare_tits") > 40:
            comfortable = True
        elif the_person.outfit.wearing_panties() or the_person.effective_sluttiness("bare_pussy") > 40:
            comfortable = True
        elif the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) > 40:
            comfortable = True

        mc.change_location(hall)
        mc.location.show_background()

    "You wake up in the morning to your alarm. You get dressed and leave your room to get some breakfast."
    $ the_person.draw_person()
    if the_person.outfit.wearing_panties() and the_person.outfit.wearing_bra():
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, wearing nothing but her underwear."
        $ mc.change_locked_clarity(5)
    elif the_person.outfit.wearing_panties():
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, wearing just a tiny pair of panties."
        $ mc.change_locked_clarity(10)
    elif the_person.outfit.wearing_bra():
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, wearing a bra, but surprisingly no panties."
        $ mc.change_locked_clarity(10)
    else:
        $ mc.change_locked_clarity(15)
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, completely naked."

    if the_person.effective_sluttiness("underwear_nudity") < 10:
        #She's startled and embarrassed.
        "[the_person.title] closes her door behind her, then notices you. She gives a startled yell."
        the_person "Ah! [the_person.mc_title], what are you doing here?"
        "She tries to cover herself with her hands and fumbles with her door handle."
        mc.name "I'm just going to get some breakfast. What are you doing?"
        "[the_person.title] gets her door open and hurries back inside. She leans out so all you can see is her head."
        the_person "I was going to get some laundry and thought you were still asleep. Could you, uh, move along?"
        $ the_person.change_slut(2)
        "You shrug and continue on your way."

    elif comfortable == False:
        "[the_person.title] closes her door behind her, then notices you. She turns and jumps slightly in shock, pressing herself against the door."
        the_person "Sorry [the_person.mc_title], you startled me a bit."
        if the_person.outfit.wearing_panties():
            if not the_person.outfit.wearing_bra():
                if the_person.has_large_tits():
                    "She moves her hands up to her [the_person.tits_description], covering them, but also creating some impressive cleavage in the process."
                else:
                    "She covers her [the_person.tits_description] with her hands, but leaves the rest of her body exposed to you."
        else:
            if not the_person.outfit.wearing_bra():
                "She cups one hand on her pussy while stretching the other arm across her breasts."
                if the_person.has_large_tits():
                    "It doesn't quite get the job done leaving them bulging out above and below her arm."
                else:
                    "This mostly takes care of her front, but her ass is still bare."
            else:
                "She cups one hand on her pussy while she splays the other out over her ass."
        "She is pretty well covered, but the idea of being basically naked leaves her looking a bit uneasy."
        $ mc.change_locked_clarity(5)
        mc.name "Yep, early start today. Are you okay?"
        the_person "I just wasn't expecting to run into anyone in the hall at this time of day."
        mc.name "What are you doing anyway?"
        the_person "I'm just up to get some laundry. I put some in last night."
        "She shifts on her feet and nods down the hall."
        the_person "Go ahead, I don't want to distract you."
        menu:
            "Head to the kitchen":
                mc.name "Well, alright I'm going to go get breakfast if you want to join me when you are more presentable."
                "You start to move down the hall again, but not before seeing her start to blush a bit."
                $ the_person.change_stats(love = 1, happiness = 2)
                the_person "Thanks, I'll see you in a bit."
                "You reach the kitchen and head in to prepare breakfast, hearing her make her way to the laundry room a moment later."
            "Ladies first":
                mc.name "No, I insist, ladies first."
                "You take a step back, making an exaggerated gesture down the hall."
                "She looks at your eye imploringly, but you just smile at her until she sighs in resignation."
                the_person "Fine, have it your way."
                "You let [the_person.title] get a step ahead of you so you can look at her ass, but once she is past she swings her hands back to cover herself."
                $ the_person.draw_person(position = "back_peek")
                "She eyes you warily and her gait is a bit stiff, but you keep up the smile and try to avoid staring too much."
                "The view is pleasant, and as you walk together she seems to relax a bit with the idea of being mostly undressed around you."
                $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 30)
                $ the_person.draw_person(position = "walking_away")
                "You reach the door to the kitchen and split up. You linger a second and enjoy the view as [the_person.possessive_title] walks away."
                # Make a bad decision?

    elif the_person.effective_sluttiness("underwear_nudity") < 40:
        #She doesn't mind but doesn't think to tease you further
        "[the_person.title] closes her door behind her, then notices you. She turns and smiles."
        the_person "Morning [the_person.mc_title], I didn't think you'd be up yet."
        mc.name "Yep, early start today. What are you up to?"
        if the_person.outfit.wearing_panties():
            if not the_person.outfit.wearing_bra():
                "She starts to walk alongside you and doesn't seem to mind being topless."
            else:
                "She starts to walk alongside you and doesn't seem to mind being in her underwear."
        else:
            if not the_person.outfit.wearing_bra():
                "She starts to walk alongside you and doesn't seem to mind being naked."
            else:
                "She starts to walk alongside you and doesn't seem to mind that she is only wearing a bra."
        $ mc.change_locked_clarity(5)
        $ the_person.update_outfit_taboos()
        the_person "I'm just up to get some laundry. I put some in last night."
        "You let [the_person.title] get a step ahead of you so you can look at her ass."
        $ the_person.draw_person(position = "walking_away")
        menu:
            "Compliment her":
                #Bonus love and happiness
                mc.name "Well, I'm glad I ran into you. Seeing you is a pretty good way to start my day."
                $ the_person.change_stats(love = 2, happiness = 5)
                the_person "You're just saying that because you get to see me naked, you perv."
                $ the_person.draw_person(position = "back_peek")
                "She peeks back at you and winks."

            "Slap her ass":
                #Bonus sluttiness and obedience
                mc.name "Did you know you look really cute without any clothes on?"
                "You give her a quick slap on the ass from behind. She yelps and jumps forward a step."
                the_person "Ah! Hey, I'm not dressed like this for you, this is my house too you know."
                "She reaches back and rubs her butt where you spanked it."
                the_person "And ew. I'm your sister, you shouldn't be gawking at me."
                mc.name "I'll stop gawking when you stop shaking that ass."
                $ the_person.draw_person(position = "back_peek")
                the_person "You wish this ass was for you."
                $ mc.change_locked_clarity(5)
                "She spanks herself lightly and winks at you."
                $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 30)

        $ the_person.draw_person(position = "walking_away")
        "You reach the door to the kitchen and split up. You wait a second and enjoy the view as [the_person.possessive_title] walks away."

    else: #sluttiness >= 40-55
        #She likes being watched and teases you a little while you walk together.
        "[the_person.title] closes her door behind her, then notices you."
        the_person "Morning [the_person.mc_title], I was wondering if you were going to be up now."
        mc.name "Yep, early start today. What are you up to?"
        the_person "I was just going to get some laundry out of the machine."
        if the_person.outfit.wearing_panties():
            if the_person.outfit.wearing_bra():
                "[the_person.possessive_title] thumbs her underwear playfully."
                $ mc.change_locked_clarity(5)
            else:
                "[the_person.possessive_title] cups her breasts playfully."
                $ mc.change_locked_clarity(10)
        else:
            "[the_person.possessive_title] absentmindedly runs her hands over her hips."
            $ mc.change_locked_clarity(10)

        $ the_person.update_outfit_taboos()
        if mom.effective_sluttiness() > 40:
            the_person "I know you like it when I walk around naked and when I'm doing laundry I have an excuse."
        else:
            the_person "I know you like it when I walk around naked but Mom doesn't. At least when I'm doing laundry I have an excuse."
        "You join her as she starts to walk down the hall."
        $ the_person.draw_person(position = "walking_away")
        menu:
            "Grope her as you walk":
                "You reach behind [the_person.title] and grab her ass while she's walking. She moans softly and leans against you."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")
                else:
                    the_person "[the_person.mc_title], what are you doing? We can't doing anything here..."
                    mc.name "I know, I'm just having a feel. You've got a great ass."
                    "You spank her butt and she moans again. You work your hand down between her legs from behind and run a finger along her slit."
                    the_person "Fuck, please don't get me too wet. I don't want to have to explain that to Mom if she finds us."
                    "You flick your finger over [the_person.possessive_title]'s clit, then slide your hand back and knead her ass some more."
                    $ mc.change_locked_clarity(20)
                $ the_person.change_stats(love = 2)
                "When you reach the kitchen [the_person.title] reluctantly pulls away from you."

            "Put her hand on your cock as you walk":
                "You take [the_person.title]'s left hand and push it against your crotch."
                if the_person.has_taboo("touching_penis"):
                    the_person "Oh my god, what are you doing!"
                    mc.name "I saw you looking at it, I thought you might be curious. Just give it a feel."
                    the_person "I can't believe you... You just made me touch it like that!"
                    mc.name "You liked it though, didn't you? Come on, let's keep walking."
                    "You hold her hand against your crotch as you walk. She looks away awkwardly, but doesn't try and pull away."
                    mc.name "You can touch it for real, if you want."
                    the_person "You're such a pervert, you know that? Tricking me into this..."
                    "Her hand slides up to your waist, then down under your underwear. She wraps her hand around your shaft and rubs it gently."
                    mc.name "Sure thing [the_person.title], I've really tricked you."
                    $ the_person.break_taboo("touching_penis")
                else:
                    the_person "What are you doing?"
                    mc.name "Look at what you do to me when you walk around like this. You're driving me crazy [the_person.title]."
                    "You let go of her hand but it stays planted on your bulge as you walk."
                    the_person "You're such a pervert, you know that? I can't believe you'd even think about me like that..."
                    "Her hand slides up to your waist, then down under your underwear. She wraps her hand around your shaft and rubs it gently."
                    mc.name "Don't pretend like you don't like it. You're just as horny as I am."
                    the_person "Hey, I'm just doing this for you, okay?"
                    mc.name "Sure thing sis. Keep going."

                $ mc.change_locked_clarity(20)
                $ the_person.change_stats(obedience = 3, slut = 1, max_slut = 30)

                "The two of you walk slowly towards the kitchen as [the_person.possessive_title] fondles your dick."
                "When you reach the door to the kitchen she reluctantly pulls her hand out of your pants."
        if the_person.effective_sluttiness() > 40:
            menu:
                "Follow her" if the_person.effective_sluttiness("bare_pussy") > 40:
                    call lily_morning_encounter_follow_up_one_label(the_person) from _call_from_lily_morning_encounter_enhanced_label_1
                "Grab her wrist" if mc.business.event_triggers_dict.get("family_threesome", False) == True:
                    call lily_morning_encounter_follow_up_two_label(the_person) from _call_from_lily_morning_encounter_enhanced_label_2
                "Let her go":
                    $ _return = False

        if _return:
            "Very happy with how your morning has gone so far you head back to your room to start getting ready for the day."
            $ mc.change_location(bedroom)
        else:
            mc.name "Maybe we'll follow up on this later."
            "[the_person.possessive_title]'s face is flush. She nods and heads towards the laundry room. You get to watch her ass shake as she goes."

    $ the_person.apply_outfit(the_person.planned_outfit)
    $ clear_scene()
    return

label lily_morning_encounter_follow_up_one_label(the_person):
    $ mc.change_location(laundry_room)
    $ mc.location.show_background()
    "Not satisfied to let things go there, you follow her into the laundry room."
    the_person "Oh, [the_person.mc_title] I thought you were going to the kitchen."
    mc.name "I was, but I don't think I can leave you like this in good conscience."
    the_person "That is so sweet, I was worried I would have to take care of myself before I could think about school for the day."
    $ the_person.change_stats(happiness = 5, love = 3)
    if the_person.outfit.wearing_panties():
        $ the_person.outfit.strip_to_vagina()
        "As you step towards her she drops her panties off her hips to the floor."
        $ the_person.update_outfit_taboos()
    menu:
        "Continue with your fingers":
            call fuck_person(the_person, private = True, start_object = make_floor(), start_position = standing_finger, skip_intro = False) from _call_lily_morning_encounter_laundryfinger

        "Get a taste of her pussy" if not the_person.has_taboo("licking_pussy"):
            call fuck_person(the_person, private = True, start_object = make_floor(), start_position = cunnilingus, skip_intro = False) from _call_lily_morning_encounter_laundrylick

        "Fuck her" if not the_person.has_taboo("vaginal_sex"): # only show sex option if you had sex before
            call fuck_person(the_person, private = True, start_object = make_floor(), start_position = missionary, skip_intro = False) from _call_lily_morning_encounter_laundryfuck

    the_person "Thanks bro, now get out of here, so I can do my laundry."
    $ clear_scene()
    $ mc.change_location(kitchen)
    $ mc.location.show_background()
    "You walk back to the kitchen to get some breakfast."
    return True

label lily_morning_encounter_follow_up_two_label(the_person):
    python:
        jealous_person = False
        if the_person.sex_record.get("Last Sex Day", 0) < day - 7:
            jealous_person = True
        the_other_person = None
        scene_manager = Scene()
        if renpy.random.randint(0, 1) == 1: # 50% we have a second person (if someone is in the house)
            the_other_person = get_random_from_list(people_in_mc_home(excluded_people = [the_person]))
        jealous_watcher = False
        if the_other_person:
            if the_other_person.effective_sluttiness() < 40:
                the_other_person = None
            elif the_other_person.sex_record.get("Last Sex Day", 0) < day - 7:
                jealous_watcher = True

    "Not satisfied by a little groping you grab [the_person.title] by the wrist and pull her along with you towards the kitchen."
    the_person "Hey, [the_person.mc_title], what do you think you are doing?"
    $ scene_manager.add_actor(the_person, emotion = "angry")
    mc.name "I think we need to continue this before I can go about my day."
    the_person "What, in the kitchen? What about mom?"
    mc.name "She'll have to wait her turn."
    $ mc.change_location(kitchen)
    $ mc.location.show_background()
    if the_other_person and renpy.random.randint(0, 1) == 1: #someone is already there 25%
        the_person "I'm serious, what if sh..."
        $ scene_manager.add_actor(the_other_person, display_transform = character_left_flipped, position = "sitting", emotion = "happy")
        the_other_person "Good morning [the_other_person.mc_title]..."
        if the_other_person.sluttiness < 60:
            the_other_person "... and, [the_person.title], what do you think you are doing walking around naked?"
            the_person "Sorry, [the_other_person.name] I was on my way to get my laundry and [the_person.mc_title] pulled me in here."
        else:
            the_other_person "... and, [the_person.title], walking around naked again I see."
            the_person "Well, since [the_person.mc_title] likes it so much I didn't want to disappoint him."
        the_other_person "Well I can understand that, now [the_other_person.mc_title] what are you doing dragging [the_person.possessive_title] around?"
        mc.name "She got me so excited that I figured she could help me take care of this."
        if jealous_person == True:
            the_other_person "Well, you can hardly blame her for wanting to get your attention."
            if jealous_watcher == True:
                the_other_person "You've been so busy and hardly paid any attention to either of us this week."
                mc.name "Sorry, [the_other_person.title] I don't want you to feel neglected."
                $ scene_manager.update_actor(the_person, emotion = "sad")
                the_person "Hey, I don't want to miss out on quality time with you either."
                mc.name "We could all do something together, that way everyone wins."
            else:
                the_other_person "She mentioned the other day that you've been ignoring her, loneliness can lead to desperation."
                mc.name "I know, I've just been so busy, but I'm ready to remedy that right now."
        else:
            the_other_person "Ah, the insatiability of youth. I sort of miss that."
            if jealous_watcher == True:
                the_other_person "I wouldn't mind some attention myself you know."
                mc.name "Sorry, [the_other_person.title] I can give you my attention now, and let [the_person.title] get on with her day."
                the_person "Yeah, if you want to take care of [the_other_person.name] we can always do something later."
                mc.name "That is very generous of you [the_person.title], but you don't need to leave for me to take care of [the_other_person.title]."
            else:
                the_person "He is just so good, I can't get enough."
                the_other_person "I'll let you two have your fun."
                mc.name "Thanks, [the_other_person.title], but you don't need to be left out."
        the_other_person "What ever will make you happiest [the_other_person.mc_title]."
        the_person "Yeah [the_person.mc_title], tell us what you want to do."
        "It seems like you have full control over what happens next. Who do you want to spend more time with?"
        menu:
            "Just [the_person.title]":
                mc.name "[the_other_person.title] I think I'm just going to focus on [the_person.title], she is the one who started this after all."
                if jealous_watcher == True:
                    the_other_person "If that is what you want to do, just try to make time for me soon too."
                    $ the_other_person.change_stats(happiness = -5, love = -1)
                else:
                    the_other_person "Don't let me get in your way. I'll see you tonight."
                $ scene_manager.remove_actor(the_other_person)
                $ the_other_person = None
            "Just [the_other_person.title]":
                mc.name "Go on, [the_person.title] I'm going to spend some quality time with [the_other_person.title]"
                if jealous_person == True:
                    the_person "Ok, just remember that I'd like to spend time with you soon too."
                    $ the_person.change_stats(happiness = -5, love = -1)
                else:
                    the_person "Ok, you two have fun. I'll see you tonight."
                $ scene_manager.remove_actor(the_person)
                $ the_person = the_other_person
                $ the_other_person = None
            "Both" if willing_to_threesome(the_person, the_other_person):
                mc.name "We're all here, and time as a family is important. [the_person.title] why don't you help me take care of [the_other_person.title]."
                mc.name "First I think there are far too many clothes being worn in this room."
                $ scene_manager.update_actor(the_other_person, position = "stand3")
                $ scene_manager.strip_full_outfit()     # they both undress
                call start_threesome(the_person, the_other_person, start_position = Threesome_double_down) from _call_lily_morning_encounter_threesome_event_kitchen1
            "No one":
                mc.name "This is really tempting, but I just remembered something I have to do today."
                mc.name "If I linger I'm going to be late so we'll have to try again another time."
                if jealous_person == True:
                    the_person "Ok, just remember that I'd like to spend time with you soon."
                    $ the_person.change_stats(happiness = -5, love = -1)
                if jealous_watcher == True:
                    the_other_person "If that is what you want to do, just try to make time for me soon."
                    $ the_other_person.change_stats(happiness = -5, love = -1)
                "It isn't easy abandoning the two of them, so you quickly make your way back to your room to get ready for the day."
                $ mc.change_location(bedroom)
        if not the_other_person:
            mc.name "Now get over here [the_person.title]."
            menu:
                "Get a handjob":
                    call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_lily_morning_encounter_handjob_02

                "Force her to her knees" if the_person.is_willing(blowjob):
                    call fuck_person(the_person, private = False, start_position = blowjob, skip_intro = False, position_locked = True) from _call_lily_morning_encounter_kitchenblow

                "Lay her on the table" if the_person.is_willing(missionary):
                    call fuck_person(the_person, private = False, start_position = missionary, start_object = make_table(), skip_intro = False) from _call_lily_morning_encounter_kitchenfuck

                "Bend her over the table" if the_person.is_willing(spanking):
                    call fuck_person(the_person, start_position = spanking, start_object = make_table(), skip_intro = False, private = False) from _call_lily_morning_encounter_kitchenspank4

            the_person "Thanks bro, I'm going to do my laundry now."
            $ the_person.draw_person(position = "walking_away")
            "You watch as your sister walks to the laundry room."
    else:
        the_person "Very funny, I'm serious."
        mc.name "So am I, we've certainly done more than let her watch us. I'm sure we can do whatever we want wherever we want."
        the_person "I suppose that is true."
        $ scene_manager.update_actor(the_person, position = "stand2")
        the_person "So, [the_person.mc_title] what do you want to do to [the_person.possessive_title]?"
        menu:
            "Ask for a handjob":
                the_person "Okay... I can do that."
                "[the_person.title] quickly pulls down your shorts, setting your erection free."
                if the_person.has_taboo("touching_penis"):
                    "[the_person.possessive_title] begins to falter a bit. You can sense her hesitation to touch you."
                    the_person "Are you sure... this is okay? I feel like we are really crossing a line here..."
                    mc.name "It's okay. It feels so good, don't you want to make me feel good?"
                    the_person "Yes... of course I want to... I just..."
                    "You take her hand in yours. She looks at you and bites her lip. You slowly move her hand down until your cock is resting in her palm."
                    the_person "Oh my god... it's so... warm..."
                    "Her hand starts to stroke you."
                    $ the_person.break_taboo("touching_penis")
                    $ mc.change_arousal(15)
                else:
                    "[the_person.possessive_title] reaches down and takes a light hold of your erection."
                    the_person "Oh god... I don't know why, but it always surprises me how warm it is..."
                    "Her hand starts to stroke you."
                    $ mc.change_arousal(15)
                call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False, ) from _call_lily_morning_encounter_handjob_01

            "Force her to her knees" if the_person.is_willing(blowjob):
                $ scene_manager.update_actor(the_person, position = "kneeling1")
                "You run your hand up her arm to her shoulder and firmly push her down to her knees."
                mc.name "I think you need to get a closer look at the problem, maybe see if you can find a solution."
                "She pulls down your pants allowing your erection to spring free."
                the_person "Wow, [the_person.mc_title], that is certainly a big problem but I think I can handle it."
                $ scene_manager.update_actor(the_person, position = "blowjob")
                "She gently takes you in her hand as she leans in and begins to lick your shaft"
                if the_other_person:
                    $ scene_manager.add_actor(the_other_person, display_transform = character_left_flipped, position = "stand4", emotion = "angry")
                    "Suddenly you hear a gasp from the door behind you."
                    the_other_person "[the_other_person.mc_title], [the_person.title] what do you think you are doing?"
                    mc.name "Oh, hey [the_other_person.title] I was just teaching [the_person.title] a lesson for walking around the house naked."
                    if the_other_person.sluttiness < 80:
                        the_other_person "Again? What a little slut, although I have to admit the view is not bad."
                    else:
                        the_other_person "You can hardly blame her, with a body like that I would walk around naked as much as I could."
                    menu:
                        "Invite [the_other_person.title]" if willing_to_threesome(the_person, the_other_person):
                            mc.name "Your body is nothing to be ashamed of [the_other_person.possessive_title], in fact you could join us if you want."
                            the_other_person "That is such a generous offer. I guess I can change my breakfast plans."
                            mc.name "Well then, you are wearing far too many clothes."
                            $ scene_manager.update_actor(the_other_person, position = "stand3")
                            $ scene_manager.strip_full_outfit()
                            call start_threesome(the_person, the_other_person, start_position = Threesome_double_down) from _call_lily_morning_encounter_threesome_event_kitchen2

                        "Continue with [the_person.title]":
                            mc.name "I can't argue with that, do you want to stay and watch?"
                            the_other_person "Well I was going to make breakfast, but I guess a little show with my meal wouldn't hurt."
                            $ scene_manager.update_actor(the_other_person, position = "sitting", emotion = "happy")
                            call fuck_person(the_person, private = False, start_position = blowjob, skip_intro = True, position_locked = True) from _call_lily_morning_encounter_kitchenblow2
                            $ scene_manager.update_actor(the_person, position = "kneeling1")
                            the_other_person "Thanks for the show."

                else:
                    mc.name "Don't be shy [the_person.title], I know how much you want this."
                    call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _call_lily_morning_encounter_kitchenblow3

            "Lay her on the table" if the_person.is_willing(missionary): # only show sex option if you had sex before
                $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = True)
                $ scene_manager.update_actor(the_person, position = "missionary")
                "Putting your other hand on [the_person.title]'s shoulder you gently guide her to the table and push her back to sit on the top."
                the_person "Oh, [the_person.mc_title] what did you have in mind for me?"
                mc.name "I think you need a good fucking, it is obvious you are horny all the time, walking around naked and teasing me."
                the_person "I can hardly disagree with that, I was hoping something like this would happen."
                "You pull down your pants and step between her legs, slowly running your hard shaft along her wet folds."
                the_person "Mmm, now who is the one teasing."
                if the_other_person:
                    $ scene_manager.add_actor(the_other_person, display_transform = character_left_flipped, position = "stand4", emotion = "angry")
                    "Before you can respond you hear a gasp behind you at the kitchen door."
                    the_other_person "[the_other_person.mc_title], [the_person.title] what are you are doing?"
                    mc.name "Oh, hey [the_other_person.title] I was just about to give [the_person.title] a bit of my attention."
                    if the_other_person.sluttiness < 80:
                        the_other_person "Right here in the middle of the kitchen?"
                    else:
                        the_other_person "Getting an early start today aren't you?"
                    mc.name "Sure, no time like the present."
                    if jealous_person == True:
                        the_other_person "Well, you can hardly blame her for wanting to get your attention."
                        if jealous_watcher == True:
                            the_other_person "You've been too busy to make time for either of us this week."
                        else:
                            the_other_person "She mentioned the other day that you've been ignoring her, loneliness can lead to desperation."
                    else:
                        the_other_person "Ah, the insatiability of youth. I sort of miss that."
                        if jealous_watcher == True:
                            the_other_person "I wouldn't mind some attention myself you know."
                        else:
                            $ scene_manager.update_actor(the_other_person, position = "stand2")
                            the_other_person "I'll let you two have your fun."
                            $ scene_manager.remove_actor(the_other_person)

                    $ kitchen_threesome = False # init variable
                    if jealous_watcher == True:
                        mc.name "Sorry, [the_other_person.title] I can give you my attention now, and let [the_person.title] get on with her day."
                        if jealous_person == True:
                            $ scene_manager.update_actor(the_person, emotion = "sad")
                            the_person "Hey, now I don't what to miss out on time with you again."
                            $ kitchen_threesome = True
                        else:
                            the_person "Are you sure?"
                            menu:
                                "Yes":
                                    mc.name "Go on, [the_person.title] I'm going to spend some quality time with [the_other_person.title]."
                                    the_person "Ok, you two have fun. I'll see you tonight."
                                    $ scene_manager.remove_actor(the_person)
                                    $ the_person = the_other_person

                                "No" if willing_to_threesome(the_person, the_other_person):
                                    mc.name "Actually, I think you could help me take care of [the_other_person.title]."
                                    $ kitchen_threesome = True
                    if kitchen_threesome == True:
                        mc.name "Well then, I guess we need to decide who goes first."
                        $ scene_manager.update_actor(other_person, position = "stand3", emotion = "happy")
                        $ scene_manager.strip_full_outfit()
                        call start_threesome(the_person, the_other_person, start_position = Threesome_double_down) from _call_lily_morning_encounter_threesome_event_kitchen3
                    else:
                        call fuck_person(the_person, private = False, start_position = missionary, start_object = make_table(), skip_intro = False) from _call_lily_morning_encounter_kitchenfuck2
                else:
                    call fuck_person(the_person, private = False, start_position = missionary, start_object = make_table(), skip_intro = True) from _call_lily_morning_encounter_kitchenfuck3

            "Bend her over the table" if the_person.is_willing(spanking):
                "Already hard from the teasing in the hallway you waste no time forcing [the_person.title] over to the table."
                $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = True)
                $ scene_manager.update_actor(the_person, position = "standing_doggy")
                "You push her roughly against it and bend her over getting an even better look at her tight ass."
                the_person "Oh, [the_person.mc_title] what are you going to do to me?"
                mc.name "I think it is time to teach you a lesson. If you are going to keep teasing me there will be consequences."
                if the_person.get_opinion_score("being submissive") > 0:
                    the_person "I'm not sure this is the deterrent you think it is, but I'm not complaining."
                else:
                    the_person "I'm not a big fan of punishments [the_person.mc_title]."
                if the_other_person:
                    $ scene_manager.add_actor(the_other_person, display_transform = character_left_flipped, position = "stand4", emotion = "angry")
                    "Just before you bring your hand down on [the_person.title]'s ass you hear a gasp from behind you."
                    the_other_person "[the_other_person.mc_title], [the_person.title] what is going on?"
                    mc.name "Good morning [the_other_person.title], I found this slut walking down the hallway naked and was about to teach her a lesson."
                    the_other_person "She really has been acting out recently, I guess it is time for someone to discipline her."
                    menu:
                        "Send [the_other_person.title] away":
                            mc.name "Exactly, and since you don't seem capable I guess I'll take care of it."
                            mc.name "You can go."
                            the_other_person "Yes, [the_other_person.mc_title]."
                            $ scene_manager.remove_actor(the_other_person)
                            call fuck_person(the_person, start_position = spanking, start_object = make_table(), skip_intro = False, private = True, position_locked = True) from _call_lily_morning_counter_kitchenspank1

                        "Make [the_other_person.title] stay":
                            mc.name "I know you've been struggling with her discipline, take a seat and I'll show you how it is done."
                            $ scene_manager.update_actor(the_other_person, position = "sitting")
                            the_other_person "Yes, [the_other_person.mc_title]."
                            $ the_other_person.change_obedience(5)
                            call fuck_person(the_person, start_position = spanking, start_object = make_table(), skip_intro = False, private = False, position_locked = True) from _call_lily_morning_encounter_kitchenspank2
                            $ scene_manager.update_actor(the_other_person, position = "sitting")
                            $ scene_manager.update_actor(the_person, position = "stand2")
                            mc.name "You see, it isn't that hard, to make her behave."
                            the_other_person "Indeed, I see your point. I will do better from now on."

                        "Punish [the_other_person.title] instead":
                            mc.name "And you've barely done anything about it."
                            mc.name "I think maybe you need to be punished in her place."
                            $ scene_manager.update_actor(the_other_person, position = "stand2", display_transform = character_right)
                            $ scene_manager.update_actor(the_person, position = "sitting", display_transform = character_left_flipped)
                            the_other_person "If you think that is best [the_other_person.mc_title]."
                            $ the_other_person.change_obedience(10)
                            $ scene_manager.strip_to_vagina(the_other_person, visible_enough = True, prefer_half_off = True)
                            call fuck_person(the_other_person, start_position = spanking, start_object = make_table(), skip_intro = False, private = False, position_locked = True) from _call_lily_morning_encounter_kitchenspank3
                            $ scene_manager.draw_scene()
                            mc.name "I hope this has taught you a lesson and that you will take your responsibilities more seriously now."
                            the_person "Yes [the_person.mc_title]."
                            the_other_person "Yes [the_other_person.mc_title], I will try harder."

                else:
                    call fuck_person(the_person, start_position = spanking, start_object = make_table(), skip_intro = True, private = True, position_locked = True) from _call_lily_morning_encounter_kitchenspank

                    the_person "See you next time bro, I'm going to do my laundry now."
                    $ the_person.draw_person(position = "walking_away")
                    "You watch as your sister walks to the laundry room."

    $ the_other_person = None
    $ scene_manager.clear_scene()
    $ scene_manager = None
    return True
