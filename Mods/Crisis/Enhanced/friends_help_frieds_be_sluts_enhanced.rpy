init 5 python:
    config.label_overrides["friends_help_friends_be_sluts_label"] = "friends_help_friends_be_sluts_enhanced_label"

    def get_friends_relationship_with_actor_not_girlfriend_or_paramour():
        relations = town_relationships.get_business_relationships(["Friend","Best Friend"])
        func = Person.has_role

        relationship = get_random_from_list([x for x in relations if \
            (not func(x.person_a, [girlfriend_role, affair_role]) and not func(x.person_b, [girlfriend_role, affair_role])) \
            or (not func(x.person_a, [girlfriend_role, affair_role]) and func(x.person_b, [girlfriend_role, affair_role])) \
            or (func(x.person_a, [girlfriend_role, affair_role]) and not func(x.person_b, [girlfriend_role, affair_role]))
        ])
        if relationship is None:
            return (None, None)

        if relationship.person_a.has_role([girlfriend_role, affair_role]) \
            or relationship.person_a.effective_sluttiness() > relationship.person_b.effective_sluttiness():
            person_one = relationship.person_a
            person_two = relationship.person_b
        else:
            person_one = relationship.person_b
            person_two = relationship.person_a

        return (person_one, person_two)

label friends_help_friends_be_sluts_enhanced_label():
    #A slutty girl helps her less slutty friend be more slutty.

    $ (person_one, person_two) = get_friends_relationship_with_actor_not_girlfriend_or_paramour()
    if not (isinstance(person_one, Person) and isinstance(person_two, Person)):
        return

    $ mc.change_location(lobby)
    $ mc.location.show_background()
    $ scene_manager = Scene()

    if person_one.effective_sluttiness() < 30: #If our slutty person isn't very slutty in the first place.
        "You decide to take a walk, both to stretch your legs and to make sure your staff are staying on task."
        "When you peek in the break room you see [person_one.title] and [person_two.title] chatting with each other as they make coffee."
        $ scene_manager.add_actor(person_one, position = "walking_away")
        $ scene_manager.add_actor(person_two, position = "walking_away", display_transform = character_center_flipped)
        menu:
            "Stop to listen":
                person_one "... Following so far? Then he takes your..."
                "You can't quite hear what they're talking about. [person_two.title] gasps and blushes."
                person_two "No! Does that even..."
                person_one "It feels amazing! Or so I've been told."
                $ scene_manager.update_actor(person_two, position = "back_peek", emotion = "sad")
                "[person_two.title] shakes her head in disbelief and turns away. When she notices you in the doorway she gasps and stammers."
                person_two "[person_two.mc_title], we were just... I was just... How much did you hear of that?"
                $ scene_manager.update_actor(person_one, position = "back_peek")
                $ scene_manager.update_actor(person_two, position = "stand2", emotion = "default")
                person_two "Oh no, this is so embarrassing!"
                $ scene_manager.update_actor(person_two, position = "stand3")
                person_one "[person_two.title], relax. Sorry [person_one.mc_title], we were just chatting about some girl stuff."
                person_one "She doesn't have much experience, so I was just explaining..."
                $ scene_manager.update_actor(person_two, position = "stand5")
                person_two "[person_one.title]! [person_two.mc_title] doesn't need to hear about this."
                mc.name "This isn't highschool, I'm not going to punish you for being bad girls and talking about sex."
                $ scene_manager.update_actor(person_two, position = "stand2")
                person_one "Well maybe she wants to be punished a little. Maybe a quick spanking?"
                "[person_one.possessive_title] slaps [person_two.title]'s butt."
                $ scene_manager.update_actor(person_two, position = "walking_away")
                person_two "Hey! That's... Come on [person_one.title], we should get back to work. Goodbye [person_two.mc_title]."
                $ scene_manager.remove_actor(person_two)
                "She hurries out of the room, blushing."
                $ person_one.change_slut(2)
                person_one "She's so cute when she's embarrassed. See you around [person_two.mc_title]."
            "Ignore them":
                "You leave them to their discussion and circle back to your desk."

    elif person_one.effective_sluttiness() < 60: #Our sluttiest is moderately slutty
        "You decide to take a walk, both to stretch your legs and to make sure your staff are staying on task."
        "You're passing by the break room when an unusual noise catches your attention. It sounds like distant and passionate feminine moaning."
        $ scene_manager.add_actor(person_one, position = "walking_away")
        $ scene_manager.add_actor(person_two, position = "walking_away", display_transform = character_center_flipped)
        "Intrigued, you peek your head in and see [person_one.title] and [person_two.title]. They are staring intently at [person_one.title]'s phone while they stand next to the coffee machine."
        menu:
            "Investigate":
                if person_two.effective_sluttiness() < 30: #But the other girl is low sluttiness.
                    # The sluttier is showing her friend some porn. She panics/is embarrassed when you walk in and see what it is
                    "You clear your throat and [person_two.title] yelps and spins around."
                    $ scene_manager.update_actor(person_two, position = "stand2")
                    $ scene_manager.update_actor(person_one, position = "back_peek")
                    person_two "[person_two.mc_title]! I was... We were..."
                    "[person_one.title] rolls her eyes and speaks up."
                    $ scene_manager.update_actor(person_one, position = "stand3")
                    person_one "I was just showing [person_two.title] a video I found last night. I thought she might be into it."
                    person_one "Do you want to see?"
                    $ scene_manager.update_actor(person_two, position = "stand5", emotion = "angry")
                    person_two "[person_one.title]! I'm sorry [person_two.mc_title], I know this isn't what we should be doing here."
                    mc.name "Why would I care? You're taking a break and relaxing the way you want to."
                    $ mc.change_locked_clarity(5)
                    $ scene_manager.update_actor(person_two, position = "stand2", emotion = "default")
                    "The moans from the phone grow louder. You notice [person_one.possessive_title] has turned her attention back to the screen."
                    mc.name "[person_one.title] seems to have the right idea."
                    $ scene_manager.update_actor(person_one, emotion = "happy")
                    person_one "Yeah, just relax [person_two.title]. You said you had something you wanted to show me too, right?"
                    "She hands the phone to [person_two.title], who looks at you and takes it hesitantly."
                    person_two "You're sure?"
                    mc.name "Of course I'm sure, but if I'm making you self conscious I'll give you some privacy."
                    $ scene_manager.update_actor(person_two, emotion = "happy")
                    mc.name "Once you're done your break I expect to see you both back at work."
                    $ person_two.change_slut(2)
                    $ person_two.change_obedience(2)
                    $ mc.change_locked_clarity(5)
                    "You leave the room, and a few seconds later you can hear them resume watching porn together."


                else: #And her friend is pretty slutty too.
                    # You catch them watching some porn on break, the less slutty is slightly worried about you seeing but neither mind a ton.
                    "You clear your throat and both girls look up."
                    $ scene_manager.update_actor(person_two, position = "back_peek")
                    person_one "Oh, hey [person_one.mc_title]."
                    $ scene_manager.update_actor(person_one, position = "back_peek")
                    person_two "Hi [person_two.mc_title], we were just taking our break together."
                    "The moaning on the phone grows louder and [person_two.title] seems suddenly self conscious."
                    $ scene_manager.update_actor(person_two, position = "stand2")
                    person_two "I hope you don't mind that we're watching... [person_one.title] just wanted to show me something quickly."
                    mc.name "I certainly don't mind."
                    $ scene_manager.update_actor(person_one, position = "stand3", emotion = "happy")
                    person_one "I told you it was fine. I found this last night and thought it was so hot. Do you want to take a look [person_one.mc_title]."
                    "She holds her phone up for you to see. You lean in close and join the ladies watching porn on [person_one.title]'s phone."
                    $ scene_manager.update_actor(person_one, position = "stand5", emotion = "default")
                    # Discover something new about her sexuality
                    $ person_one.discover_opinion(person_one.get_random_opinion(include_known = True, include_sexy = True, include_normal = False, only_positive = True))
                    $ person_one.discover_opinion(person_one.get_random_opinion(include_known = True, include_sexy = True, include_normal = False, only_positive = True))
                    $ person_one.change_love(1)
                    $ person_two.change_slut(1 + person_two.get_opinion_score("public sex"))
                    $ person_two.change_love(1)
                    $ mc.change_locked_clarity(10)
                    "After a few minutes the video ends and you've discovered a few things about [person_one.title]'s sexual preferences."
                    $ scene_manager.update_actor(person_one, position = "stand3")
                    person_two "You're right [person_one.title], that was hot. Can you send that to me for later?"
                    $ scene_manager.update_actor(person_one, emotion = "happy")
                    person_one "Sure thing. We should be getting to work before [person_one.mc_title] gets too distracted though."
                    $ mc.change_locked_clarity(5)
                    "Her eyes drift conspicuously down your body to the noticeable bulge in your pants."
                    $ scene_manager.update_actor(person_two, emotion = "sad")
                    person_two "Uh, right. Talk to you later [person_two.mc_title]."
                    "You watch them walk out then get back to work."

            "Ignore them":
                "You leave them to their discussion and circle back to your desk."


    else:
        "You decide to take a walk, both to stretch your legs and to make sure your staff are staying on task."
        "When you pass by the break room you overhear [person_one.title] and [person_two.title] chatting at the coffee machine."
        $ scene_manager.add_actor(person_one, position = "stand2")
        $ scene_manager.add_actor(person_two, position = "stand3", display_transform = character_center_flipped)
        menu:
            "Investigate":
                "You stop at the door and listen for a moment."
                if person_two.effective_sluttiness() < 20:
                    # The sluttier girl is talking about how horny she's feeling today when you walk in. Her friend seems embarrassed to be hearing about it.
                    # The sluttier girl then spanks/plays with the less slutty girls ass for your benefit.
                    # When you walk in the sluttier girl makes some passes at you that her friend apologizes for, but that you reenforce.
                    person_one "I can't wait to get home, I've been feeling so worked up all day I just want to get naked and have some me time."
                    person_one "I got a new vibrator and it's mind blowing. I want to be riding it all day long now."
                    $ scene_manager.update_actor(person_two, emotion = "angry")
                    person_two "[person_one.title], you're such a slut!"
                    $ scene_manager.update_actor(person_one, emotion = "happy")
                    person_one "Oh come on, so are you. Wouldn't you like to be at home right now with a vibe pressed up against your clit?"
                    $ scene_manager.update_actor(person_two, emotion = "happy")
                    $ mc.change_locked_clarity(10)
                    "[person_two.title] laughs and shrugs, then suddenly tenses up and starts to blush when she notices you at the door."
                    $ scene_manager.update_actor(person_two, emotion = "sad")
                    person_two "Uh, hello [person_two.mc_title]. I was just... Uhh..."
                    $ scene_manager.update_actor(person_one, emotion = "default")
                    person_one "Hey [person_one.mc_title], don't mind her, she's just horny and thinking about her vibrator at home."
                    $ scene_manager.update_actor(person_two, emotion = "angry")
                    person_two "Shut up, [person_two.mc_title] doesn't want to hear about this."
                    $ mc.change_locked_clarity(10)
                    person_one "Sure he does, men love to hear about slutty, horny women. Right [person_one.mc_title]?"
                    person_two "I'm so sorry [person_two.mc_title], she doesn't know what she's saying."
                    mc.name "I think she does, because I agree, especially when they're as beautiful as you two."
                    $ scene_manager.update_actor(person_two, emotion = "happy")
                    $ scene_manager.update_actor(person_one, position = "stand3", emotion = "happy")
                    person_one "See? Come on, we should probably get back to work. Nice seeing you [person_one.mc_title]."
                    person_two "Uh... See you around."
                    $ scene_manager.update_actor(person_one, position = "walking_away")
                    $ scene_manager.update_actor(person_two, position = "walking_away")
                    "They head for the door. [person_one.title] pauses and waits for [person_two.title] to pass her."
                    $ scene_manager.update_actor(person_one, position = "back_peek")
                    $ mc.change_locked_clarity(10)
                    "She looks at you and winks, then gives her friend a hard slap on the ass."
                    person_one "After you!"
                    $ scene_manager.remove_actor(person_two)
                    person_two "Ah! You..."
                    $ scene_manager.remove_actor(person_one)
                    "You hear them chatting and laughing as they head back to work."
                    $ person_one.change_obedience(1)
                    $ person_two.change_slut(2)
                    $ person_two.change_obedience(2)

                elif person_two.effective_sluttiness() < 40:
                    # The sluttier girl is talking about the less slutty girls tits when you walk in. She wants you to give a comparison, the less slutty girl begrudgingly agrees
                    # Note: At high love she hints that she's doing this as a favour to you.
                    if rank_tits(person_one.tits) < rank_tits(person_two.tits):
                        # The slutty girl wants smaller, perkier tits.
                        person_two "Look at them though, they're the perfect shape. Mine just don't have the same perk yours do."
                        person_one "But they're so nice and big, I'd kill to have them like that. I bet they're nice and soft, too."
                        $ mc.change_locked_clarity(10)
                        person_two "Want to give them a feel? I... Oh, hey [person_one.mc_title]."

                    else:
                        # The slutty girl wants larger tits.
                        person_two "Look at those puppies, they're the perfect size. I'd kill for a pair of tits like yours."
                        person_one "They're big, but yours look perkier. I know lots of guys who are into that."
                        $ mc.change_locked_clarity(10)
                        person_two "I still just want to grab yours by the handful and... Oh, hey [person_one.mc_title]."
                    "[person_one.possessive_title] notices you at the door."
                    $ scene_manager.update_actor(person_two, emotion = "sad")
                    person_two "Ah, hi... We were just getting back to work, right [person_one.title]?"
                    person_one "Yeah, in a moment. [person_one.mc_title], you're just who we need right now to settle this for us."
                    mc.name "Settle what?"
                    person_one "[person_two.title] won't admit she's got the better tits of the two of us. Talk some sense into her for me."
                    $ scene_manager.update_actor(person_two, emotion = "default")
                    $ mc.change_locked_clarity(10)
                    person_two "Oh god, what are you getting us into."
                    menu:
                        "[person_one.title] has nicer tits": #She's already slutty, but gets a love boost
                            "You take a moment to consider, then nod towards [person_one.title]."
                            if rank_tits(person_one.tits) < rank_tits(person_two.tits):
                                mc.name "I've got to give it to [person_one.title]. I like them perky."
                            else:
                                mc.name "I've got to give it to [person_one.title]. I like them big."
                            $ person_one.change_happiness(5)
                            $ person_one.change_love(1 + person_one.get_opinion_score("showing her tits"))
                            $ scene_manager.update_actor(person_two, emotion = "sad")
                            person_two "See? Now that we've settled that, can we get back to work. It feels weird to be talking about our breasts with our boss."
                            $ scene_manager.update_actor(person_one, emotion = "happy")
                            person_one "I suppose. Thanks for the help [person_one.mc_title]."

                        "[person_two.title] has nicer tits": # She gets a sluttiness boost along with a small love boost.
                            if rank_tits(person_one.tits) > rank_tits(person_two.tits):
                                mc.name "I've got to give it to [person_two.title]. I like them perky."
                            else:
                                mc.name "I've got to give it to [person_two.title]. I like them big."
                            $ scene_manager.update_actor(person_one, emotion = "happy")
                            person_one "Exactly! You're just going to have to accept that you're smoking hot [person_two.title]."
                            $ person_two.change_slut(2 + person_one.get_opinion_score("showing her tits"))
                            $ person_two.change_love(1 + person_one.get_opinion_score("showing her tits"))
                            $ scene_manager.update_actor(person_two, emotion = "happy")
                            person_two "Fine, I guess my tits are pretty nice. Shouldn't we be getting back to work."
                            person_one "I suppose. Thanks for the help [person_one.mc_title]."
                            "She gives you a smile and a wink, then leaves the room with [person_two.title]."

                        "I'm going to need a closer look" if not person_one.outfit.tits_visible() or not person_two.outfit.tits_visible(): #Requires high obedience, sluttiness, or a uniform policy for the less slutty girl.
                            mc.name "Hmm. It's a close call, I'm going to need to take a moment for this and get a better look."
                            $ scene_manager.update_actor(person_one, emotion = "happy")
                            if person_one.outfit.tits_visible():
                                # If her tits are already out then it must be her friend who has a shirt on.
                                "[person_one.title] thrusts her chest forward and displays her tits proudly."
                                person_one "Well, here are mine. Come on [person_two.title], whip 'em out!"
                            else:
                                person_one "Of course."
                                $ scene_manager.strip_to_tits(person = person_one, prefer_half_off = True)

                                if person_two.outfit.tits_visible():
                                    $ person_one.break_taboo("bare_tits")
                                    person_one "There, what do you think now [person_one.mc_title]?"
                            $ mc.change_locked_clarity(10)

                            if not person_two.outfit.tits_visible():
                                $ scene_manager.update_actor(person_two, emotion = "angry")
                                person_two "Oh my god, are we really doing this?"
                                person_one "Come on, cut loose a little! It's just a little friendly competition, right?"
                                $ scene_manager.update_actor(person_two, emotion = "default")
                                $ strip_list = person_two.outfit.get_half_off_to_tits_list()
                                $ half_off_instead = True
                                if not strip_list:
                                    $ half_off_instead = False
                                    $ strip_list = person_two.outfit.get_tit_strip_list()

                                $ the_item = strip_list[0]
                                #$ the_item = person_two.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                                if person_two.get_opinion_score("showing her tits") > 0:
                                    $ person_two.discover_opinion("showing her tits")
                                    "[person_two.title] bites her lip and giggles."
                                    person_two "Fine! I can't believe I'm doing this!"
                                    if half_off_instead:
                                        "She starts to strip down, eagerly pulling her [the_item.display_name] up."
                                    else:
                                        "She starts to strip down, eagerly pulling off her [the_item.display_name]."
                                    $ person_two.change_slut(person_two.discover_opinion("showing her tits"))
                                elif person_two.obedience >= 120:
                                    person_two "Do you really want me to do this [person_two.mc_title]?"
                                    mc.name "I do, now show them to us."
                                    if half_off_instead:
                                        "She nods meekly and starts to pull her [the_item.display_name] up."
                                    else:
                                        "She nods meekly and starts to strip down, starting with her [the_item.display_name]."
                                    $ person_two.change_obedience(1)

                                elif corporate_enforced_nudity_policy.is_active() or maximal_arousal_uniform_policy.is_active():
                                    "[person_two.title] hesitates for a second."
                                    mc.name "Just consider this a temporary change to your uniform, [person_two.title]. I could have you walking around topless all day if I wanted to."
                                    person_two "Fine, I guess I did agree to that..."
                                    if half_off_instead:
                                        "She starts to pull her [the_item.display_name] up."
                                    else:
                                        "She starts to strip down, starting with her [the_item.display_name]."
                                    $ person_two.change_obedience(1)
                                else:
                                    $ scene_manager.update_actor(person_two, emotion = "angry")
                                    person_two "I can't do this, [person_one.title]! You're crazy!"
                                    "[person_one.title] jiggles her tits."
                                    person_one "Look at me, I'm doing it! Here, let me help you."
                                    $ scene_manager.update_actor(person_two, emotion = "sad")
                                    $ scene_manager.update_actor(person_one, display_transform = character_center(.10), z_order = - 10)
                                    "[person_one.title] moves behind [person_two.title] and starts to dress her down, starting with her [the_item.name]."
                                $ del the_item

                                $ scene_manager.strip_actor_strip_list(person_two, strip_list, half_off_instead = half_off_instead)
                                $ scene_manager.update_actor(person_one, display_transform = character_right)

                                $ del strip_list

                                if person_two.get_opinion_score("showing her tits") > 0:
                                    "When she has her tits out she crosses her arms in front of her in a small attempt to preserve her modesty."
                                    person_one "[person_one.mc_title] can't see them if you keep them covered up. Here..."
                                    "[person_one.title] takes her friend's hands and move them to her hips, then cups them and gives them a squeeze in front of you."
                                else:
                                    "When she has her tits out she puts her hands on her hips and smiles at you, exposed and ready for your inspection."
                                    $ scene_manager.update_actor(person_one, position = "stand4", emotion = "happy")
                                    person_one "That's it, look at these puppies [person_one.mc_title]..."
                                    "She gets behind her friend and cups her breasts, giving them a squeeze."

                                $ person_two.break_taboo("bare_tits")
                                $ scene_manager.update_actor(person_one, position = "stand2", emotion = "default")
                                person_two "Hey, go easy on them! Well then [person_two.mc_title], who's your pick? Me or [person_one.title]?"

                            $ mc.change_locked_clarity(10)
                            menu:
                                "[person_one.title] has nicer tits": #She's already slutty, but gets a love boost
                                    "You take a moment to consider both of their naked racks, then nod towards [person_one.title]."
                                    if rank_tits(person_one.tits) < rank_tits(person_two.tits):
                                        mc.name "I've got to give it to [person_one.title]. I like them perky."
                                    else:
                                        mc.name "I've got to give it to [person_one.title]. I like them big."

                                    $ person_one.change_happiness(5)
                                    $ person_one.change_love(1 + person_one.get_opinion_score("showing her tits"))
                                    $ person_two.change_slut(1 + person_two.get_opinion_score("showing her tits"))

                                    $ scene_manager.update_actor(person_two, emotion = "sad")
                                    person_two "So I got naked just to lose, huh?"
                                    $ scene_manager.update_actor(person_one, emotion = "happy")
                                    person_one "I guess you did, but at least you get to see some nice tits."
                                    "She jiggles her chest at her friend, who laughs and waves her off."
                                    person_two "Uh huh. Come on, you've had your fun. We need to get back to work."

                                "[person_two.title] has nicer tits": # She gets a sluttiness boost along with a small love boost.
                                    if rank_tits(person_one.tits) > rank_tits(person_two.tits):
                                        mc.name "I've got to give it to [person_two.title]. I like them perky."
                                    else:
                                        mc.name "I've got to give it to [person_two.title]. I like them big."
                                    $ scene_manager.update_actor(person_two, emotion = "happy")
                                    person_two "Well, at least I didn't get naked just to lose."
                                    $ person_two.change_slut(1 + person_one.get_opinion_score("showing her tits"))
                                    $ person_two.change_love(1 + person_one.get_opinion_score("showing her tits"))
                                    $ scene_manager.update_actor(person_one, emotion = "happy")
                                    person_one "You've got some award winning tits on you, you should be proud of them!"
                                    person_two "I feel like [person_two.mc_title] was the real winner here. Come on, we should be getting back to work."
                            $ scene_manager.update_actor(person_two, position = "walking_away")
                            person_one "Yeah, you're probably right."
                            $ scene_manager.update_actor(person_one, position = "walking_away")
                            $ scene_manager.remove_actor(person_two)
                            "[person_one.title] gives you a smile and a wink, then leaves the room with [person_two.title]."
                            $ scene_manager.remove_actor(person_one)

                        "Punish them for inappropriate behaviour" if office_punishment.is_active():
                            mc.name "[person_one.title], [person_two.title], this is completely inappropriate, even if you're on your break."
                            mc.name "I don't have any choice but to record this for disciplinary action later."
                            $ person_one.add_infraction(Infraction.inappropriate_behaviour_factory())
                            $ person_two.add_infraction(Infraction.inappropriate_behaviour_factory())
                            $ scene_manager.update_actor(person_one, emotion = "sad")
                            person_one "Really? I..."
                            $ scene_manager.update_actor(person_two, emotion = "sad")
                            person_two "Don't get us in any more trouble [person_one.title]. Sorry [person_two.mc_title], we'll get back to work right away."
                            person_one "Ugh, whatever. Come on [person_two.title], let's go."
                            $ scene_manager.update_actor(person_one, position = "walking_away")
                            $ scene_manager.update_actor(person_two, position = "walking_away")
                            "They turn and leave the room together."


                else: #She wants to suck your dick, but is embarrassed about it.
                    "They're talking quietly with each other, occasionally glancing in your direction. When [person_two.title] sees you watching she looks away quickly."
                    "[person_one.title] grabs her friend's hand and they walk over to you together."
                    person_one "[person_one.mc_title], could me and [person_two.title] talk to you privately for a moment?"
                    mc.name "Sure, follow me to my office."
                    $ ceo_office.show_background()

                    if person_two.effective_sluttiness("sucking_cock") < 50: #She's embarrassed, but wants to do it
                        person_two "It's nothing important, it could probably wait until later. In fact, never mind at all."
                        person_one "[person_two.title], I know you want to do this. Don't chicken out now."
                        mc.name "I can spare a moment. Close the door."
                        "[person_one.title] closes the door, then stands behind [person_two.title]."
                        mc.name "So, what can I help you two with?"
                        $ scene_manager.update_actor(person_two, emotion = "sad")
                        person_two "I... I mean, we... Uh..."
                        person_one "She's very nervous, let me help her out."
                        if person_two.sex_record.get("Blowjobs", 0) == 0:
                            person_one "[person_two.title] has always wanted to suck your cock, but was too scared to ask."
                        else:
                            person_two "[person_one.title] really liked sucking your cock and wants to do it again, but was too scared to ask."
                        $ scene_manager.update_actor(person_two, emotion = "default")
                        $ mc.change_locked_clarity(20)
                        if person_two.get_opinion_score("giving blowjobs") < 0:
                            $ person_two.discover_opinion("giving blowjobs")
                            person_two "I actually don't like giving blowjobs, but [person_one.title] says it's an important skill for a woman to have."
                        else:
                            "[person_two.possessive_title] nods, blushing intensely."
                            person_two "I swear I don't normally do things like this..."

                    else: #She's a major slut herself and wants to get some dick down her throat.
                        person_two "It won't take long, I promise."
                        mc.name "I can spare a moment. Close the door."
                        "[person_one.title] closes the door, then stands behind [person_two.title]."
                        mc.name "So, what can I help you two with?"
                        person_two "I was talking to [person_one.title] and we started talking about your cock..."
                        $ mc.change_locked_clarity(20)
                        if person_two.sex_record.get("Blowjobs", 0) > 0:
                            person_two "It brought back some good memories, so I was hoping you'd let me suck you off."
                        else:
                            person_two "I haven't had it in my mouth before, and I really want to. Would you let me suck you off?"

                    menu:
                        "Let [person_two.title] give you a blowjob":
                            mc.name "I'm not about to say no to an offer like that."
                            $ scene_manager.update_actor(person_two, emotion = "happy")
                            if girlfriend_role in person_one.special_role or affair_role in person_one.special_role:
                                person_one "I didn't think you would sweetheart."
                                "[person_one.title] leans over your desk and gives you a kiss, then whispers in your ear."
                                person_one "A little gift from me. You two have fun."
                                $ scene_manager.update_actor(person_one, position = "walking_away")
                                "She smiles and steps out of the room, leaving you and [person_two.title] alone."
                                $ scene_manager.remove_actor(person_one)

                            else:
                                person_one "I didn't think you would. You two enjoy yourselves."
                                "She gives [person_two.title] a smack on the ass as she leaves the room."
                                $ scene_manager.update_actor(person_one, position= "walking_away")
                                person_one "Go get him girl."
                                $ scene_manager.remove_actor(person_one)

                            $ scene_manager.clear_scene()
                            $ person_two.draw_person()
                            $ person_two.change_stats(arousal = 50)
                            "You motion [person_two.title] to get down on her knees, while you unzip and take out your already swollen member."
                            $ person_two.draw_person(position = "blowjob")
                            "She opens her mouth and slides your penis between her moist lips."
                            $ person_two.break_taboo("sucking_cock")
                            call fuck_person(person_two, start_position = blowjob, skip_intro = True, position_locked = True, self_strip = False, affair_ask_after = True) from _call_fuck_person_friends_help_friends_be_sluts_enhanced
                            $ the_report = _return
                            if the_report.get("guy orgasms", 0) > 0:
                                "You sit down in your office chair, thoroughly drained. [person_two.title] smiles, seemingly proud of her work."
                                mc.name "So, was that everything you wanted it to be?"
                                person_two "It was fun, I can't wait to tell [person_one.title] all about it."

                            else:
                                "You sit down in your office chair and sigh."
                                person_two "I'm sorry, I'm not doing a good job, am I?"
                                mc.name "You were doing fine, I'm just not in the mood. You should get back to work."
                                $ person_two.change_happiness(-5)
                            $ person_two.review_outfit(dialogue = False)
                            $ scene_manager.update_actor(person_two, position= "walking_away")
                            "[person_two.possessive_title] takes a moment to get herself tidied up, then steps out of your office."

                        "Decline her offer":
                            mc.name "I'm flattered, but I'm not in the mood right now."
                            person_two "Of course, sorry I even brought it up [person_two.mc_title]!"
                            $ scene_manager.update_actor(person_two, position = "walking_away")
                            "She hurries out of your office. [person_one.title] shakes her head and sighs."
                            $ scene_manager.remove_actor(person_two)
                            $ scene_manager.update_actor(person_one, emotion = "angry")
                            person_one "Really? I bring you a cute girl to suck your dick and you're not in the mood? I'll never understand men..."
                            $ scene_manager.update_actor(person_one, "walking_away")
                            "She shrugs and leaves your office, following her friend."
                            $ scene_manager.remove_actor(person_one)

                        "Punish them for inappropriate behaviour" if office_punishment.is_active():
                            mc.name "[person_one.title], [person_two.title], I expected better from both of you."
                            mc.name "This is completely inappropriate, I'm going to have to write both of you up for this."
                            $ person_one.add_infraction(Infraction.inappropriate_behaviour_factory())
                            $ person_two.add_infraction(Infraction.inappropriate_behaviour_factory())
                            person_two "I... Of course, I'm sorry I even brought it up [person_two.mc_title]!"
                            $ scene_manager.update_actor(person_two, position = "walking_away")
                            "She hurries out of your office. [person_one.title] sighs and rolls her eyes."
                            $ scene_manager.remove_actor(person_two)
                            $ scene_manager.update_actor(person_one, emotion = "angry")
                            person_one "Really? I bring you a cute girl to suck your dick and you decide you need to punish both of us? What more do you want?"
                            mc.name "I'm sorry, but rules are rules. You didn't leave me much of a choice."
                            person_one "Whatever, I need to go make sure [person_one.title] is fine."
                            $ scene_manager.update_actor(person_one, position = "walking_away")
                            "She turns and leaves your office, following after her friend."

            "Ignore them":
                "You leave them to their discussion and circle back to your desk."

    python:
        scene_manager.clear_scene()
        del person_one
        del person_two
        clear_scene()
    return
