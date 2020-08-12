init 5 python:
    config.label_overrides["mom_outfit_help_crisis_label"] = "mom_outfit_help_crisis_label_enhanced"


label mom_outfit_help_crisis_label_enhanced():
    $ the_person = mom
    # Your mom asks for help planning an outfit for the next day. As a bonus you get to watch her strip down between outfits (peek/don't peek decision given, she doesn't care at high sluttiness)
    if not mom in mc.location.people:
        #She's in a different room, shh calls you in.
        the_person.char "[the_person.mc_title], can you help me with something for a moment?"
        "You hear [the_person.possessive_title] call for you from her bedroom."
        menu:
            "Help [the_person.possessive_title]":
                mc.name "Sure thing, I'll be right there."
                $ mom_bedroom.show_background()
                $ the_person.draw_person()
                "You step into [the_person.possessive_title]. She's standing at the foot of her bed and laying out a few sets of clothing."
                mc.name "Hey Mom, what's up?"

            "Say you're busy":
                mc.name "Sorry [the_person.title], I'm a little busy at the moment."
                the_person.char "Okay, I'll ask your sister."
                $ clear_scene()
                return
    else:
        #She's in the room with you right now (how? no clue, but maybe it'll happen one day!)
        $ the_person.draw_person()
        the_person.char "[the_person.mc_title], could you help me with something for a moment?"
        menu:
            "Help [the_person.possessive_title]":
                mc.name "Sure thing, what's up?"
                "[the_person.possessive_title] goes over to her closet and pulls out a few sets of clothing. She starts to lay them out."

            "Say you're busy":
                mc.name "Sorry Mom, I should really be getting to bed."
                the_person.char "That's okay [the_person.mc_title], I'll ask your sister then."
                $ clear_scene()
                return

    the_person.char "I've got a meeting with an important client tomorrow and I don't know what I should wear."
    the_person.char "Could you give me your opinion?"
    mc.name "Of course, lets take a look!"
    $ first_outfit = the_person.wardrobe.decide_on_outfit(the_person.sluttiness) # A normal outfit for her, made from her wardrobe.
    $ second_outfit = None # Changes her goals based on how you respond to the first one (ie. she tones it down, makes it sluttier, or keeps it the way it is)
    $ third_outfit = None # She asks you to put something together from her wardrobe. If it's reasonable for her she'll add it to her wardrobe.
    $ caught = False #Did you get caught watching her strip

    if the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 30: #She really doesn't want you to see anything
        the_person.char "Okay, I'll need a moment to get changed."
        mc.name "I can just turn around, if that would be faster."
        the_person.char "I'll just be a second. Go on, out."
        $ clear_scene()
        "[the_person.possessive_title] shoos you out of her bedroom. You lean against her door and wait."
        the_person.char "Okay, all done. Come on in!"

    elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
        the_person.char "Okay, I'll need a moment to get changed. Could you just turn around for a second?"
        $ clear_scene()
        "You nod and turn your back to [the_person.possessive_title]. You hear her moving behind you as she starts to get undressed."
        menu:
            "Try and peek":
                # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                $ the_person.draw_person()
                "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."

                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice is not None and not caught:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take off her [strip_choice.display_name]."
                    if renpy.random.randint(0,100) < 10: #you got caught
                        the_person.char "I'll be done in just a second [the_person.mc_title]..."
                        "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                        $ the_person.draw_person(emotion = "angry")
                        $ the_person.change_happiness(-5)
                        $ the_person.change_slut_temp(1+the_person.get_opinion_score("not wearing anything"))
                        the_person.char "[the_person.mc_title], are you watching me change!"
                        mc.name "No, I... The mirror was just sort of there."
                        "She covers herself with her hands and motions for the door."
                        the_person.char "Could you wait outside, please?"
                        $ clear_scene()
                        "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                        the_person.char "Okay, you can come back in."
                        $ caught = True
                    else:
                        menu:
                            "Keep watching.":
                                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                            "Stop peeking.":
                                "You pull your eyes away from the mirror and do your best not to peek."
                                $ clear_scene()
                $ strip_choice = None

                if not caught:
                    "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                    the_person.char "Okay [the_person.mc_title], you can turn around now."

            "Wait until she's done":
                "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                the_person.char "Okay, all done. You can turn around now."

    else: #She's slutty enough that she doesn't care if you watch or not.
        the_person.char "Just give me one second to get dressed [the_person.mc_title]."
        "[the_person.possessive_title] starts to strip down in front of you."
        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        while strip_choice is not None:
            $ the_person.draw_animated_removal(strip_choice)
            "You watch as [the_person.possessive_title] take off her [strip_choice.display_name]."
            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        $ strip_choice = None

        "Once she's stripped naked she grabs her new outfit and starts to put it on."
        if the_person.update_outfit_taboos(): #Some taboo was broken.
            the_person.char "I should probably have told you to look away, but you don't mind, right?"
            the_person.char "It's nothing you haven't seen when you were younger."
            mc.name "I don't mind at all [the_person.title]."
            "She smiles at you and finishes getting dressed again."


    #$ the_person.outfit = first_outfit changed v0.24.1
    $ the_person.apply_outfit(first_outfit, update_taboo = True)
    $ the_person.draw_person()
    the_person.char "Well, what do you think?"
    "You take a moment to think before responding."
    menu:
        "Say it's too revealing":
            mc.name "I don't think it's very appropriate for work Mom. Maybe you should try something a little less... revealing."
            $ the_person.change_slut_temp(-2)
            the_person.char "Maybe you're right. Okay, I'll try something a little more conservative for this next outfit."
            $ second_outfit = the_person.wardrobe.decide_on_outfit(the_person.sluttiness-10, 0) #Note that if we have impossible values for this function it'll keep exanding the threshold until it's possible

        "Say she looks beautiful in it":
            mc.name "You look beautiful Mom, I think it would be perfect."
            $ the_person.change_happiness(5)
            $ the_person.change_love(1)
            "She smiles and blushes."
            the_person.char "You aren't just saying that, are you? I want your real opinion"
            mc.name "It's a great look for you."
            the_person.char "Great! I want to try another outfit before I settle on this one though, if you don't mind."
            $ second_outfit = the_person.wardrobe.decide_on_outfit(the_person.sluttiness, 0)

        "Say it's not revealing enough":
            mc.name "I don't know Mom, it's a little stuffy, isn't it? Maybe you should pick something that's a little more modern and fun."
            $ the_person.change_slut_temp(1+the_person.get_opinion_score("skimpy uniforms"))
            $ the_person.discover_opinion("skimpy uniforms")
            if the_person.get_opinion_score("skimpy uniforms") >= 0:
                the_person.char "Do you think so? Maybe it is a little too conservative."
                "She nods and turns towards her closet."
                the_person.char "Okay, I'll give something else a try then."
            else:
                the_person.char "Oh no, I hate having to dress in those skimpy little outfits everyone wants their secretary in these days."
                "She sighs and shrugs."
                the_person.char "Well, if that's what you think I'll give something else a try."
            $ second_outfit = the_person.wardrobe.decide_on_outfit(the_person.sluttiness+10, 10)


    #Strip choices for the second peek section
    if the_person.effective_sluttiness() + the_person.love < 35 or caught: #She really doesn't want you to see anything
        the_person.char "Okay, I just need to get changed again."
        $ clear_scene()
        "[the_person.possessive_title] shoos you out of the room while she changes into her new outfit."
        the_person.char "Okay, come in!"

    elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
        the_person.char "I'm going to need to get changed again."
        $ clear_scene()
        "You turn around to give her some privacy."
        menu:
            "Try and peek":
                # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                $ the_person.draw_person()
                "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."
                $ caught = False
                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice is not None and not caught:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take off her [strip_choice.display_name]."
                    if renpy.random.randint(0,100) < 10: #you got caught
                        the_person.char "I'll be done in just a second [the_person.mc_title]..."
                        "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                        $ the_person.draw_person(emotion = "angry")
                        $ the_person.change_happiness(-5)
                        $ the_person.change_slut_temp(1+the_person.get_opinion_score("not wearing anything"))
                        the_person.char "[the_person.mc_title], are you watching me change!"
                        mc.name "No, I... The mirror was just sort of there."
                        "She covers herself with her hands and motions for the door."
                        the_person.char "Could you wait outside, please?"
                        $ clear_scene()
                        "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                        the_person.char "Okay, you can come back in."
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
                    the_person.char "Okay [the_person.mc_title], you can turn around now."

            "Wait until she's done":
                "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                the_person.char "Okay, all done. You can turn around now."

    else: #She's slutty enough that she doesn't care if you watch or not.
        the_person.char "It'll just take me a second to get changed."
        "[the_person.possessive_title] starts to strip down in front of you."
        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        while strip_choice is not None:
            $ the_person.draw_animated_removal(strip_choice)
            "You watch as [the_person.possessive_title] take off her [strip_choice.display_name]."
            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

        $ strip_choice = None
        "Once she's stripped naked she grabs another outfit and starts to put it on."

    $ the_person.apply_outfit(second_outfit, update_taboo = True)
    #$ the_person.outfit = second_outfit changed v0.24.1
    $ the_person.draw_person()

    the_person.char "Alright, there we go! Now, do you think this is better or worse than what I was just wearing?"
    $ the_person.draw_person(position = "back_peek")
    "She gives you a few turns, letting you get a look at the full outfit."
    $ the_person.draw_person()
    menu:
        "Suggest the first outfit":
            mc.name "I think you looked best in the first outfit, you should wear that."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = first_outfit
            the_person.char "I think you're right, I'll put it away for tomorrow."

        "Suggest the second outfit":
            mc.name "I think this one suits you better, you should wear it tomorrow."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = second_outfit
            the_person.char "I think you're right, it does look good on me."

        "Suggest your own outfit":
            mc.name "They both look good, but I think I have another idea for something you could wear..."
            "You go to [the_person.possessive_title]'s closet and start to put together an outfit of your own for her."
            $ clear_scene()
            call screen outfit_select_manager(slut_limit = the_person.sluttiness + 10)
            $ third_outfit = _return
            $ the_person.draw_person()

            if third_outfit == "No Return":
                "You try a few different combinations, but you can't come up with anything you think Mom will like."
                mc.name "Sorry Mom, I thought I had an idea but I guess I was wrong."
                the_person.char "That's fine [the_person.mc_title]. I think I'm going to go with the first one anyway."
                $ the_person.change_happiness(5)
                $ the_person.next_day_outfit = first_outfit
            else:
                "You lay the outfit out for [the_person.possessive_title]. She looks it over and nods."
                the_person.char "I'll try it on, but I think I like it!"

                if the_person.effective_sluttiness() + the_person.love < 35 or caught: #She really doesn't want you to see anything
                    $ clear_scene()
                    "[the_person.possessive_title] shoos you out of the room while she changes into her new outfit."
                    the_person.char "Okay, come back!"

                elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
                    the_person.char "I'm just going to get changed one last time, if you could turn around for a second."
                    $ clear_scene()
                    "You turn around to give her some privacy."
                    menu:
                        "Try and peek":
                            # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                            $ the_person.draw_person()
                            "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."
                            $ caught = False
                            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                            while strip_choice is not None and not caught:
                                $ the_person.draw_animated_removal(strip_choice)
                                "You watch as [the_person.possessive_title] take off her [strip_choice.display_name]."
                                if renpy.random.randint(0,100) < 10: #you got caught
                                    the_person.char "I'll be done in just a second [the_person.mc_title]..."
                                    "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                                    $ the_person.draw_person(emotion = "angry")
                                    $ the_person.change_happiness(-5)
                                    $ the_person.change_slut_temp(1+the_person.get_opinion_score("not wearing anything"))
                                    the_person.char "[the_person.mc_title], are you watching me change!"
                                    mc.name "No, I... The mirror was just sort of there."
                                    "She covers herself with her hands and motions for the door."
                                    the_person.char "Could you wait outside, please?"
                                    $ clear_scene()
                                    "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                                    the_person.char "Okay, you can come back in."
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
                                the_person.char "Okay [the_person.mc_title], you can look."

                        "Wait until she's done":
                            "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                            the_person.char "Okay, all done. You can look."

                else: #She's slutty enough that she doesn't care if you watch or not.
                    the_person.char "It'll just take a moment for me to slip into this."
                    "[the_person.possessive_title] starts to strip down in front of you."
                    $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                    while strip_choice is not None:
                        $ the_person.draw_animated_removal(strip_choice)
                        "You watch as [the_person.possessive_title] take off her [strip_choice.display_name]."
                        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                    "Once she's stripped naked she grabs another outfit and starts to put it on."
                    $ strip_choice = None

                $ the_person.apply_outfit(third_outfit, update_taboo = True)
                #$ the_person.outfit = third_outfit changed v0.24.1
                $ the_person.draw_person()
                $ the_person.change_stats(happiness = 5, obedience = 5, love = 1)
                the_person.char "I think you have great fashion sense [the_person.mc_title]! It's settled, I'll wear this tomorrow!"
                $ the_person.add_outfit(third_outfit,"full")
                $ the_person.next_day_outfit = third_outfit

    the_person.char "Thank you so much for the help [the_person.mc_title]. I don't know why but I've been feeling much more unsure about the way I dress lately."
    mc.name "Any time, I'm just glad to help."
    "You leave [the_person.possessive_title] in her room as she starts to pack her clothes away."

    python:
        del first_outfit
        del second_outfit
        del third_outfit
        renpy.scene("Active")
    return
