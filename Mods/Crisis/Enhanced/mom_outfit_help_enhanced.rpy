init 5 python:
    config.label_overrides["mom_outfit_help_crisis_label"] = "mom_outfit_help_crisis_label_enhanced"

    def sister_helps_mom_with_next_day_outfit(mom, sister):
        if sister.effective_sluttiness() >= mom.effective_sluttiness():
            outfit_slut_points = __builtin__.min(__builtin__.int(sister.effective_sluttiness() / 8), 12)
            allow_skimpy = False
            mom.change_stats(slut = 1, max_slut = (30 if sister.effective_sluttiness() >= 30 else sister.effective_sluttiness()))
        else:
            outfit_slut_points = __builtin__.min(__builtin__.int(mom.effective_sluttiness() / 8), 12)
            allow_skimpy = True

        builder = WardrobeBuilder(sister)
        thinks_appropriate = False
        while not thinks_appropriate or outfit_slut_points < 0:
            outfit = mom.personalize_outfit(builder.build_outfit(None, outfit_slut_points), opinion_color = sister.favorite_colour(), coloured_underwear = True, swap_bottoms = True, allow_skimpy = allow_skimpy)
            thinks_appropriate = mom.judge_outfit(outfit)
            outfit_slut_points -= 1
        if thinks_appropriate and outfit:
            return outfit
        return None

label mom_outfit_help_crisis_label_enhanced():
    $ the_person = mom
    if not mom.is_available:
        return
    # Your mom asks for help planning an outfit for the next day. As a bonus you get to watch her strip down between outfits (peek/don't peek decision given, she doesn't care at high sluttiness)
    if not mom in mc.location.people:
        #She's in a different room, shh calls you in.
        the_person "[the_person.mc_title], can you help me with something for a moment?"
        "You hear [the_person.possessive_title] call for you from her bedroom."
        menu:
            "Help [the_person.possessive_title]":
                mc.name "Sure thing, I'll be right there."
                $ mom_bedroom.show_background()
                $ the_person.draw_person()
                "You step into [the_person.possessive_title]. She's standing at the foot of her bed and laying out a few sets of clothing."
                mc.name "Hey [the_person.title], what's up?"

            "Say you're busy":
                mc.name "Sorry [the_person.title], I'm a little busy at the moment."
                the_person "Okay, I'll ask your sister."
                $ the_person.next_day_outfit = sister_helps_mom_with_next_day_outfit(the_person, lily)
                $ clear_scene()
                return
    else:
        #She's in the room with you right now (how? no clue, but maybe it'll happen one day!)
        $ the_person.draw_person()
        the_person "[the_person.mc_title], could you help me with something for a moment?"
        menu:
            "Help [the_person.possessive_title]":
                mc.name "Sure thing, what's up?"
                "[the_person.possessive_title] goes over to her closet and pulls out a few sets of clothing. She starts to lay them out."

            "Say you're busy":
                mc.name "Sorry [the_person.title], I should really be getting to bed."
                the_person "That's okay [the_person.mc_title], I'll ask your sister then."
                $ the_person.next_day_outfit = sister_helps_mom_with_next_day_outfit(the_person, lily)
                $ clear_scene()
                return

    the_person "I've got a meeting with an important client tomorrow and I don't know what I should wear."
    the_person "Could you give me your opinion?"
    mc.name "Of course, let's take a look!"
    python:
        builder = WardrobeBuilder(the_person)
        outfit_slut_points = __builtin__.min(__builtin__.int(the_person.effective_sluttiness() / 8), 12)
        first_outfit = builder.personalize_outfit(builder.build_outfit(None, outfit_slut_points))
    # $ first_outfit = the_person.decide_on_outfit() # A normal outfit for her, made from her wardrobe.
    $ second_outfit = None # Changes her goals based on how you respond to the first one (ie. she tones it down, makes it sluttier, or keeps it the way it is)
    $ third_outfit = None # She asks you to put something together from her wardrobe. If it's reasonable for her she'll add it to her wardrobe.
    $ caught = False #Did you get caught watching her strip

    if the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 30: #She really doesn't want you to see anything
        the_person "Okay, I'll need a moment to get changed."
        mc.name "I can just turn around, if that would be faster."
        the_person "I'll just be a second. Go on, out."
        $ clear_scene()
        "[the_person.possessive_title] shoos you out of her bedroom. You lean against her door and wait."
        the_person "Okay, all done. Come on in!"

    elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
        the_person "Okay, I'll need a moment to get changed. Could you just turn around for a second?"
        $ clear_scene()
        "You nod and turn your back to [the_person.possessive_title]. You hear her moving behind you as she starts to get undressed."
        menu:
            "Try and peek":
                # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                $ the_person.draw_person()
                "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."

                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice and not caught:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take's off her [strip_choice.display_name]."
                    $ mc.change_locked_clarity(2)
                    if renpy.random.randint(0,100) < 10: #you got caught
                        the_person "I'll be done in just a second [the_person.mc_title]..."
                        "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                        $ the_person.draw_person(emotion = "angry")
                        $ the_person.change_stats(happiness = -5, slut = 1 + the_person.get_opinion_score("not wearing anything"), max_slut = 20)
                        the_person "[the_person.mc_title], are you watching me change!"
                        mc.name "No, I... The mirror was just sort of there."
                        "She covers herself with her hands and motions for the door."
                        the_person "Could you wait outside, please?"
                        $ clear_scene()
                        "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                        the_person "Okay, you can come back in."
                        $ caught = True
                    else:
                        menu:
                            "Keep watching":
                                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                            "Stop peeking":
                                "You pull your eyes away from the mirror and do your best not to peek."
                                $ clear_scene()
                                $ strip_choice = None

                if not caught:
                    "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                    the_person "Okay [the_person.mc_title], you can turn around now."

            "Wait until she's done":
                "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                the_person "Okay, all done. You can turn around now."

    else: #She's slutty enough that she doesn't care if you watch or not.
        the_person "Just give me one second to get dressed [the_person.mc_title]."
        "[the_person.possessive_title] starts to strip down in front of you."
        $ the_person.strip_outfit(exclude_feet = False)
        $ mc.change_locked_clarity(10)
        "Once she's stripped naked she grabs her new outfit and starts to put it on."
        if the_person.update_outfit_taboos(): #Some taboo was broken.
            the_person "I should probably have told you to look away, but you don't mind, right?"
            the_person "It's nothing you haven't seen when you were younger."
            mc.name "I don't mind at all [the_person.title]."
            "She smiles at you and finishes getting dressed again."

    $ the_person.apply_outfit(first_outfit, update_taboo = True)
    $ the_person.draw_person()
    the_person "Well, what do you think?"
    "You take a moment to think before responding."
    menu:
        "Say it's too revealing":
            mc.name "I don't think it's very appropriate for work [the_person.title]. Maybe you should try something a little less... revealing."
            $ the_person.change_slut(-2)
            the_person "Maybe you're right. Okay, I'll try something a little more conservative for this next outfit."
            $ outfit_slut_points = __builtin__.max(outfit_slut_points - 1, 0)
            $ second_outfit = builder.personalize_outfit(builder.build_outfit(None, outfit_slut_points)) #Note that if we have impossible values for this function it'll keep exanding the threshold until it's possible

        "Say she looks beautiful in it":
            mc.name "You look beautiful [the_person.title], I think it would be perfect."
            $ the_person.change_stats(happiness = 5, love = 1)
            "She smiles and blushes."
            the_person "You aren't just saying that, are you? I want your real opinion"
            mc.name "It's a great look for you."
            the_person "Great! I want to try another outfit before I settle on this one though, if you don't mind."
            $ second_outfit = builder.personalize_outfit(builder.build_outfit(None, outfit_slut_points))

        "Say it's not revealing enough":
            mc.name "I don't know [the_person.title], it's a little stuffy, isn't it? Maybe you should pick something that's a little more modern and fun."
            $ the_person.change_slut(1+the_person.get_opinion_score("skimpy uniforms"))
            $ outfit_slut_points = __builtin__.min(outfit_slut_points + 1, 12)
            $ the_person.discover_opinion("skimpy uniforms")
            if the_person.get_opinion_score("skimpy uniforms") >= 0:
                the_person "Do you think so? Maybe it is a little too conservative."
                "She nods and turns towards her closet."
                the_person "Okay, I'll give something else a try then."
            else:
                the_person "Oh no, I hate having to dress in those skimpy little outfits everyone wants their secretaries in these days."
                "She sighs and shrugs."
                the_person "Well, if that's what you think I'll give something else a try."
            $ second_outfit = builder.personalize_outfit(builder.build_outfit(None, outfit_slut_points))


    #Strip choices for the second peek section
    if the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 35 or caught: #She really doesn't want you to see anything
        the_person "Okay, I just need to get changed again."
        $ clear_scene()
        "[the_person.possessive_title] shoos you out of the room while she changes into her new outfit."
        the_person "Okay, come in!"

    elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
        the_person "I'm going to need to get changed again."
        $ clear_scene()
        "You turn around to give her some privacy."
        menu:
            "Try and peek":
                # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                $ the_person.draw_person()
                "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."
                $ caught = False
                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice and not caught:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take's off her [strip_choice.display_name]."
                    $ mc.change_locked_clarity(2)
                    if renpy.random.randint(0,100) < 10: #you got caught
                        the_person "I'll be done in just a second [the_person.mc_title]..."
                        "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                        $ the_person.draw_person(emotion = "angry")
                        $ the_person.change_stats(happiness = -5, slut = 1 + the_person.get_opinion_score("not wearing anything"), max_slut = 20)
                        the_person "[the_person.mc_title], are you watching me change!"
                        mc.name "No, I... The mirror was just sort of there."
                        "She covers herself with her hands and motions for the door."
                        the_person "Could you wait outside, please?"
                        $ clear_scene()
                        "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                        the_person "Okay, you can come back in."
                        $ caught = True
                    else:
                        menu:
                            "Keep watching":
                                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                            "Stop peeking":
                                "You pull your eyes away from the mirror and do your best not to peek."
                                $ clear_scene()
                                $ strip_choice = None

                if not caught:
                    "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                    the_person "Okay [the_person.mc_title], you can turn around now."

            "Wait until she's done":
                "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                the_person "Okay, all done. You can turn around now."

    else: #She's slutty enough that she doesn't care if you watch or not.
        the_person "It'll just take me a second to get changed."
        "[the_person.possessive_title] starts to strip down in front of you."
        $ the_person.strip_outfit(exclude_feet = False)
        $ mc.change_locked_clarity(10)
        "Once she's stripped naked she grabs another outfit and starts to put it on."

    $ the_person.apply_outfit(second_outfit, update_taboo = True)
    #$ the_person.outfit = second_outfit changed v0.24.1
    $ the_person.draw_person()

    the_person "Alright, there we go! Now, do you think this is better or worse than what I was just wearing?"
    $ the_person.draw_person(position = "back_peek")
    "She gives you a few turns, letting you get a look at the full outfit."
    $ the_person.draw_person()
    menu:
        "Suggest the first outfit":
            mc.name "I think you looked best in the first outfit, you should wear that."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = first_outfit
            the_person "I think you're right, I'll put it away for tomorrow."

        "Suggest the second outfit":
            mc.name "I think this one suits you better, you should wear it tomorrow."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = second_outfit
            the_person "I think you're right, it does look good on me."

        "Suggest your own outfit":
            mc.name "They both look good, but I think I have another idea for something you could wear..."
            "You go to [the_person.possessive_title]'s closet and start to put together an outfit of your own for her."
            $ clear_scene()
            call outfit_master_manager(slut_limit = the_person.sluttiness + 10, show_overwear = False, show_underwear = False) from _call_outfit_master_manager_mom_outfit_help_enhanced
            $ third_outfit = _return
            $ the_person.draw_person()

            if third_outfit is None:
                "You try a few different combinations, but you can't come up with anything you think [the_person.title] will like."
                mc.name "Sorry [the_person.title], I thought I had an idea but I guess I was wrong."
                the_person "That's fine [the_person.mc_title]. Do you want to pick one of my outfits instead?"
                menu:
                    "Suggest the first outfit":
                        mc.name "I think you looked best in the first outfit, you should wear that."
                        "She smiles and nods."
                        $ the_person.change_happiness(2)
                        $ the_person.next_day_outfit = first_outfit
                        the_person "I think you're right, I'll put it away for tomorrow."

                    "Suggest the second outfit":
                        mc.name "I think this one suits you better, you should wear it tomorrow."
                        "She smiles and nods."
                        $ the_person.change_happiness(2)
                        $ the_person.next_day_outfit = second_outfit
                        the_person "I think you're right, it does look good on me."

            else:
                "You lay the outfit out for [the_person.possessive_title]. She looks it over and nods."
                the_person "I'll try it on, but I think I like it!"

                if the_person.effective_sluttiness() + the_person.love < 35 or caught: #She really doesn't want you to see anything
                    $ clear_scene()
                    "[the_person.possessive_title] shoos you out of the room while she changes into her new outfit."
                    the_person "Okay, come back!"

                elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
                    the_person "I'm just going to get changed one last time, if you could turn around for a second."
                    $ clear_scene()
                    "You turn around to give her some privacy."
                    menu:
                        "Try and peek":
                            # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                            $ the_person.draw_person()
                            "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."
                            $ caught = False
                            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                            while strip_choice and not caught:
                                $ the_person.draw_animated_removal(strip_choice)
                                "You watch as [the_person.possessive_title] takes off her [strip_choice.display_name]."
                                $ mc.change_locked_clarity(2)
                                if renpy.random.randint(0,100) < 10: #you got caught
                                    the_person "I'll be done in just a second [the_person.mc_title]..."
                                    "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                                    $ the_person.draw_person(emotion = "angry")
                                    $ the_person.change_stats(happiness = -5, slut = 1 + the_person.get_opinion_score("not wearing anything"), max_slut = 20)
                                    the_person "[the_person.mc_title], are you watching me change!"
                                    mc.name "No, I... The mirror was just sort of there."
                                    "She covers herself with her hands and motions for the door."
                                    the_person "Could you wait outside, please?"
                                    $ clear_scene()
                                    "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                                    the_person "Okay, you can come back in."
                                    $ caught = True
                                else:
                                    menu:
                                        "Keep watching":
                                            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                                        "Stop peeking":
                                            "You pull your eyes away from the mirror and do your best not to peek."
                                            $ clear_scene()
                                            $ strip_choice = None

                            if not caught:
                                "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                                the_person "Okay [the_person.mc_title], you can look."

                        "Wait until she's done":
                            "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                            the_person "Okay, all done. You can look."

                else: #She's slutty enough that she doesn't care if you watch or not.
                    the_person "It'll just take a moment for me to slip into this."
                    "[the_person.possessive_title] starts to strip down in front of you."
                    $ the_person.strip_outfit(exclude_feet = False)
                    $ mc.change_locked_clarity(10)
                    "Once she's stripped naked she grabs another outfit and starts to put it on."

                $ the_person.apply_outfit(third_outfit, update_taboo = True)
                $ the_person.draw_person()
                $ the_person.change_stats(happiness = 5, obedience = 5, love = 1)
                the_person "I think you have great fashion sense [the_person.mc_title]! It's settled, I'll wear this tomorrow!"
                $ the_person.add_outfit(third_outfit,"full")
                $ the_person.next_day_outfit = third_outfit

    the_person "Thank you so much for the help [the_person.mc_title]. I don't know why but I've been feeling much more unsure about the way I dress lately."
    mc.name "Any time, I'm just glad to help."
    if the_person.effective_sluttiness(["touching_penis", "sucking_cock"]) > 50:
        the_person "Is there anything I could do to show you how thankful I am? You are such a helpful son..."
        if mc.energy < 50:
            mc.name "I'm sure you could think of something, but honestly I'm exhausted. I think I'll just head for bed."
            the_person "Of course honey. Have a good night!"
        else:
            mc.name "I don't know [the_person.title]. Did you have anything in mind?"
            the_person "Oh, I wouldn't say I have something specific..."
            "[the_person.possessive_title] starts to take off her outfit. Saving her clothes for tomorrow you guess?"
            $ the_person.strip_outfit(exclude_lower = True)
            $ mc.change_locked_clarity(10)
            if the_person.has_taboo("condomless_sex") and the_person.is_willing(tit_fuck): #Mid sluttiness path.
                "With her tits out, she starts to walk over to you."
                the_person "I'm sure it was hard for you... to watch your mother undress like that... right in front of you..."
                $ the_person.draw_person(position = "kissing")
                "She wraps her arms around you. The heat coming from her chest radiates against you. It feels great."
                "You pull her close as you embrace. Your erection is now rubbing up against her belly..."
                the_person "Oh my... you feel so hard. Why don't you let your mother take care of that for you?"
                "Slowly, [the_person.possessive_title] slides down to her knees. She pulls your zipper down and takes your cock out."
                $ the_person.draw_person(position = "blowjob")
                the_person "You have become such a virile young man..."
                $ mc.change_locked_clarity(20)
                if the_person.is_willing(blowjob) and the_person.get_opinion_score("giving blowjobs") >= the_person.get_opinion_score("giving tit fucks"):
                    "[the_person.possessive_title]'s lips part and she runs the tip of your cock back and forth across her tongue."
                    if the_person.has_taboo("sucking_cock"):
                        the_person "Oh my god... I just can't stop myself. I'm sorry honey, I know I shouldn't be doing this..."
                        the_person "I'll stop if you want me too. You probably think I'm crazy!"
                        mc.name "I don't think you're crazy. This is a great way to say thank you. I can't believe I'm so lucky."
                        the_person "I'm glad to hear that... I just... need to taste it!!!"
                        $ the_person.break_taboo("sucking_cock")
                    "Suddenly, she opens a bit wider and takes your cock into her mouth. Your hands run through her hair as her head starts to bob up and down."
                    call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_person_mom_outfit_help_crisis_01

                else:
                    "You watch in amazement as she wraps your cock between her tits, you erection now enveloped in her creamy cleavage."
                    if the_person.has_taboo("touching_body"):
                        the_person "Oh my god... it's so hot... I just want to make it feel good!"
                        the_person "I'll stop if you want me too. You probably think I'm crazy!"
                        mc.name "I don't think you're crazy. This is a great way to say thank you. I can't believe I'm so lucky."
                        the_person "I'm glad to hear that... I just... want to feel it blow all over me!"
                        $ the_person.break_taboo("touching_body")
                    "[the_person.possessive_title] slowly starts to rock her body up and down, stroking your cock with her tits."
                    call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_person_mom_outfit_help_crisis_02
                mc.name "That was nice... if you ever need any more outfit advice, let me know!"
            elif the_person.is_willing(SB_doggy_standing):
                the_person "I mean... you are such a virile young man... maybe you could think of some way I could thank you..."
                "[the_person.possessive_title] turns around and bends over as she starts to take off what is left of her outfit. She takes her time..."
                $ the_person.strip_outfit(position = "standing_doggy")
                "When she finishes, she stays bent over her bed. Her hips wiggle back and forth a bit, making it obvious what she has in mind..."
                $ mc.change_locked_clarity(20)
                "It's been a long day, but you still got some energy left, so you decide to have your way with her. You pull your dick out and step behind [the_person.possessive_title]."
                call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_bed(), skip_intro = True, position_locked = True) from _call_fuck_person_mom_outfit_help_crisis_03
                "When you finish up, you put your dick away."
                mc.name "That was nice... if you ever need any more outfit advice, let me know!"
            else:
                the_person "How about a nice handjob? I know that you like it when I take care of you."
                $ mc.change_locked_clarity(10)
                "[the_person.possessive_title] gets your cock out of your pants and starts jerking you off."
                call get_fucked(the_person, the_goal = "get mc off", start_position = handjob, start_object = make_floor(), skip_intro = True, prohibit_tags = ["Vaginal", "Anal"]) from _call_get_fucked_person_mom_outfit_help_crisis_01
                "When you are done, you put your cock in your pants."
                mc.name "That was nice... if you ever need any more outfit advice, let me know!"

    $ the_person.draw_person()
    "You leave [the_person.possessive_title] in her room as she starts to pack her clothes away."

    python:
        del first_outfit
        del second_outfit
        del third_outfit
        del builder
        del outfit_slut_points
        clear_scene()
    return
