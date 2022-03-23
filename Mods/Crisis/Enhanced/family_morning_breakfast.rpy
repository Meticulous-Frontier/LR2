# Enhance Morning Breakfast with multi person rendering and updated dialog

init 5 python:
    config.label_overrides["family_morning_breakfast_label"] = "family_morning_breakfast_enhanced_label"

label family_morning_breakfast_enhanced_label():
    python:
        if mom.effective_sluttiness() > 40:
            mom.apply_outfit(mom.wardrobe.get_random_appropriate_underwear(mom.sluttiness, guarantee_output = True))

        if lily.effective_sluttiness() > 40:
            lily.apply_outfit(lily.wardrobe.get_random_appropriate_underwear(lily.sluttiness, guarantee_output = True))

        #Make sure we're in our bedroom when the event starts.
        mc.change_location(bedroom)
        mc.location.show_background()
        # initialize scene manager for multi person scene
        scene_manager = Scene()

    "You're woken up in the morning by a knock at your door."
    mc.name "Uh, come in."
    "You groan to yourself and sit up in bed."
    if mom.love > lily.love:
        $ scene_manager.add_actor(mom)
        "[mom.possessive_title] cracks open the door and leans in."
        mom "I'm making some breakfast for you and [lily.name]. Come on down if you'd like some."
        mc.name "Thanks [mom.title], I'll be down in a minute."
        $ scene_manager.update_actor(mom, emotion = "happy")
        "She flashes you a smile and closes the door."
        $ scene_manager.hide_actor(mom)
    else:
        $ scene_manager.add_actor(lily)
        "[lily.possessive_title] cracks your door open and leans in. She seems just as tired as you are."
        lily "Hey, I think Mom's making a family breakfast for us."
        mc.name "Thanks for letting me know [lily.title], I'll be down in a minute."
        "She nods and closes your door as she leaves."
        $ scene_manager.hide_actor(lily)

    "You get up, get dressed, and head for the kitchen."
    $ mc.change_location(kitchen)
    $ mc.location.show_background()
    $ scene_manager.show_actor(mom, position = "walking_away", display_transform = character_left_flipped)

    if mom.effective_sluttiness() > 40:
        if mom.outfit.vagina_visible():
            "[mom.possessive_title] is in front of the stove naked, humming as she scrambles a pan full of eggs."
            $ mc.change_locked_clarity(20)
        elif mom.outfit.tits_visible():
            "[mom.possessive_title] is standing in front of the stove topless, humming as she scrambles a pan full of eggs."
            $ mc.change_locked_clarity(10)
        else:
            "[mom.possessive_title] is just in her underwear in front of the stove, humming as she scrambles a pan full of eggs."
            $ mc.change_locked_clarity(5)
    else:
        "[mom.possessive_title] is at the stove and humming to herself as she scrambles a pan full of eggs."

    $ mom.update_outfit_taboos()
    $ scene_manager.update_actor(mom, position = "back_peek")

    mom "Good morning [mom.mc_title]. I'm almost ready to serve, hopefully your [lily.name] will be here soon."
    lily "I'm coming!"

    $ scene_manager.show_actor(lily)

    if lily.effective_sluttiness() > 40:
        if lily.outfit.vagina_visible():
            "[lily.possessive_title] comes into the room naked. She gives a dramatic yawn before sitting down at the kitchen table."
            $ mc.change_locked_clarity(20)
        elif lily.outfit.tits_visible():
            "[lily.possessive_title] walks topless into the kitchen, yawning dramatically before sitting down at the table."
            $ mc.change_locked_clarity(10)
        else:
            "[lily.possessive_title] walks into the room only wearing her underwear. She gives a dramatic yawn before sitting down at the kitchen table."
            $ mc.change_locked_clarity(5)
    else:
        "[lily.possessive_title] comes into the room and gives a dramatic yawn before sitting down at the kitchen table."

    $ lily.update_outfit_taboos()
    $ scene_manager.update_actor(lily, position = "sitting")

    if mom.effective_sluttiness() > 40 and lily.effective_sluttiness() > 40:
        #You have breakfast with both of them stripped down like it's no big thing.
        lily "Hope I'm not too late."
        $ scene_manager.update_actor(mom, position = "walking_away")
        "Your mother takes the pan off the stove and begins to slide the contents off onto three plates."
        mom "No, just on time."
        $ scene_manager.update_actor(mom, position = "stand3")
        "She turns around and hands one plate to you and one plate to [lily.title]."
        if mom.lactation_sources > 0 and mom.tits_available():
            mom "Want a little milk for your coffee, honey?"
            "[mom.title] gives you a quick wink."
            mc.name "Sure mom."
            "[mom.possessive_title] bends over slight over your coffee. She takes one of her breasts in her hand and starts to squeeze."
            "It takes a second, but soon a stream of her milk is pouring out into you coffee."
            mom "Just say when!"
            "You let her continue for a few more moments, until you can see the cream start to circulate around your hot coffee."
            $ mom.change_stats(slut = 1, max_slut = 30, happiness = 5)
            mc.name "That's good!"
        lily "Thanks Mom, you're the best!"
        $ scene_manager.update_actor(mom, position = "sitting")
        mom "No problem, I'm just happy to spend my morning relaxing with my two favorite people!"
        "You enjoy a relaxing breakfast bonding with your mother and lily. [mom.possessive_title] seems particularly happy she gets to spend time with you."
        "Neither [lily.title] or [mom.possessive_title] seem to think it's strange to relax in their underwear."
        $ mc.change_locked_clarity(10)
        $ lily.change_stats(love = 3)
        $ mom.change_stats(love = 3, happiness = 5)
        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            "While no one else seems to be bothered by all the skin in the room, it is starting to take a toll on you."
            "You try to focus on something work related, but instead all you can focus on are [mom.possessive_title]'s heaving tits, across the table from you."
            mom "Honey? Are you feeling okay? You seem a little zoned out..."
            "Next to you, [lily.title] notices your erection and speaks up."
            lily "I'm sure he's fine mom, but us walking around like this has him all worked up. He's hard as a rock!"
            "[lily.possessive_title] reaches down and starts to stroke you."
            mom "Oh! I'm so sorry [mom.mc_title], I didn't even think about that. [lily.name] honey, let's take care of him before the day gets going."
            lily "Good idea mom!"
            menu:
                "Accept their help":
                    mc.name "Oh wow, that would be great!"
                    $ scene_manager.update_actor(mom, position = "stand2")
                    $ scene_manager.update_actor(lily, position = "blowjob")
                    "[mom.possessive_title] gets up and starts walking around the table, while [lily.title] gets on her knees and starts pulling off your pants and underwear."
                    "Your cock springs out of your clothes, nearly smacking [lily.possessive_title] in the face. [mom.title] gets on her knees next to [lily.title]."
                    call start_threesome(lily, mom, start_position = threesome_double_blowjob, position_locked = True) from _threesome_for_breakfast_yum_1
                    $ the_report = _return
                    if the_report.get("guy orgasms", 0) > 0:
                        "You enjoy your post orgasm bliss for a few moments while [mom.possessive_title] and [lily.possessive_title] get up."
                    else:
                        "Finished for now, you decide to put your cock away while [mom.possessive_title] and [lily.possessive_title] get up."
                    $ scene_manager.update_actor(mom, position="stand3", display_transform = character_center_flipped)
                    $ scene_manager.update_actor(lily, position = "stand4", display_transform = character_right)
                    mc.name "Mmm, thanks for breakfast mom!"
                    if the_report.get("guy orgasms", 0) > 0:
                        "[lily.title] laughs and jokes back."
                        lily "Thanks for breakfast, bro!"
                "Refuse":
                    mc.name "That's okay, I have a ton of stuff to get done today. Maybe tonight after dinner?"
                    mom "Okay, if that's what you want [mom.mc_title]."
                    $ scene_manager.update_actor(mom, position="walking_away", display_transform = character_left_flipped)
                    "[mom.possessive_title] gets up and starts to do the dishes."
        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    elif mom.effective_sluttiness() > 40 and not lily.effective_sluttiness() > 40:
        #Lily thinks her mom is embarrassing and weird but Mom pulls rank.
        lily "Oh my god Mom, what are you wearing?"
        $ scene_manager.update_actor(mom, position = "back_peek")
        mom "What? It's the weekend and it's just the three of us. I didn't think anyone would mind if I was a little more casual."
        $ scene_manager.update_actor(lily, position = "sitting")

        if mom.outfit.vagina_visible():
            lily "Mom, I don't think you know what casual means. Could you at least put on some panties or something?"
        elif mom.outfit.tits_visible():
            lily "Mom, I don't think you know what casual means. I mean, couldn't you at least put on a bra?"
        else:
            lily "Mom, you're prancing around the kitchen in your underwear. In front of your son and daughter. That's weird."
            "[lily.title] looks at you."
            lily "Right [lily.mc_title], that's weird?"

        if mom.obedience > 115:
            $ scene_manager.update_actor(mom, position = "stand3")
            mom "What do you think [mom.mc_title], do you think it's \"weird\" for your mother to want to be comfortable in her own house?"
            $ mc.change_locked_clarity(5)
            menu:
                "Side with Mom":
                    mc.name "I think Mom's right, [lily.title]. It's nothing we haven't seen before, she's just trying to relax on her days off."
                    $ mom.change_obedience(-3)
                    $ lily.change_obedience(3)
                    "[lily.title] looks at the two of you like you're crazy, then sighs dramatically."
                    lily "Fine, but this is really weird, okay?"
                    $ scene_manager.update_actor(mom, position = "sitting")
                    "[mom.possessive_title] dishes out three portions and sits down at the table with you. [lily.title] eventually gets used to her mother's outfit and joins in on your conversation."
                    $ lily.change_slut(2)
                    $ mom.change_happiness(5)


                "Side with [lily.title]":
                    mc.name "I actually think [lily.title] is right, this is a little weird. Could you go put something on, for our sakes?"
                    $ lily.change_stats(obedience = -2, slut = 1, max_slut = 30)
                    $ mom.change_stats(happiness = -10, obedience = 2)
                    mom "Oh you two, you're so silly. Fine, I'll be back in a moment. [lily.title], could you watch the eggs?"
                    $ scene_manager.hide_actor(mom)
                    $ scene_manager.update_actor(lily, position = "walking_away", display_transform = character_left_flipped)
                    "Your mother leaves to get dressed. [lily.possessive_title] ends up serving out breakfast for all three of you."
                    $ scene_manager.update_actor(lily, position = "sitting")
                    $ mom.apply_outfit(mom.planned_outfit)
                    lily "She's been so weird lately. I don't know what's going on with her..."
                    $ scene_manager.show_actor(mom, position = "sitting", display_transform = character_right)
                    $ lily.change_happiness(5)
                    $ mom.change_happiness(5)
                    "When [mom.possessive_title] gets back she sits down at the table and the three of you enjoy your breakfast together."

        else:
            #She likes what she likes
            mom "Well luckily I'm your mother and it doesn't matter what you think. I'm going to wear what makes me comfortable."
            "She takes the pan off the stove and slides the scrambled eggs out equally onto three plates."
            $ scene_manager.update_actor(mom, position = "stand3")
            mom "Now, would you like some breakfast or not?"
            "[lily.title] sighs dramatically."
            lily "Fine, but this is really weird, okay?"
            $ lily.change_slut(2)
            $ mom.change_happiness(5)
            $ scene_manager.update_actor(mom, position = "sitting")
            "[mom.possessive_title] gives everyone a plate and sits down. [lily.title] eventually gets used to her mother's outfit and joins in on your conversation."
            "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."


    elif lily.effective_sluttiness() > 40 and not mom.effective_sluttiness() > 40:
        # Mom thinks lily is way too underdressed and sends her back to get dressed.
        "Your mother turns around and gasps."
        $ scene_manager.update_actor(mom, position = "stand3", emotion="angry")
        mom "[lily.name]! What are you wearing?"
        lily "What do you mean? I just got up, I haven't had time to pick out an outfit yet."
        mom "You shouldn't be running around the house naked. Go put some clothes on young lady."
        $ scene_manager.update_actor(lily, emotion = "angry")
        "[lily.possessive_title] scoffs and rolls her eyes."
        lily "Come on Mom, you're being ridiculous. This is my house too, I should be able to wear whatever I want!"
        "[mom.possessive_title] and [lily.name] lock eyes, engaged in a subtle battle of wills."
        if lily.obedience > mom.obedience:
            $ scene_manager.update_actor(mom, position = "walking_away", emotion = None)
            "[mom.possessive_title] sighs loudly and turns back to the stove."
            mom "Fine! You're so stubborn [lily.name], I don't know how I survive around here!"
            $ lily.change_stats(obedience = -2, happiness = 5)
            $ mom.change_obedience(10)
            $ scene_manager.update_actor(lily, emotion = "happy")
            "[lily.possessive_title] looks at you, obviously pleased with herself, and winks."

        else:
            "[lily.title] finally sighs loudly and looks away. She pushes her chair back and stands up in defeat."
            $ scene_manager.update_actor(lily, position = "stand4")
            lily "Fine! I'll go put on some stupid clothes so my stupid mother doesn't keep worrying."
            $ scene_manager.update_actor(lily, position = "walking_away")
            "[lily.title] sulks out of the kitchen."
            $ scene_manager.hide_actor(lily)
            $ scene_manager.update_actor(mom, position = "walking_away", emotion = "sad")
            mom "I don't know how I manage to survive with you two around!"
            $ lily.apply_outfit(lily.planned_outfit)
            $ lily.change_stats(obedience = 5, happiness = -5)
            $ mom.change_obedience(-2)
            $ scene_manager.show_actor(lily, position = "sitting")
            "[lily.possessive_title] is back by the time Mom starts to plate breakfast. She sits down and starts to eat without saying anything."
            $ scene_manager.update_actor(mom, position = "sitting")

        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    else:
        # Neither of them are particularly slutty, so it's just a normal breakfast.
        lily "So what's the occasion Mom?"
        $ scene_manager.update_actor(mom, position = "stand3")
        "[mom.possessive_title] takes the pan off the stove and scoops the scrambled eggs out equally onto three waiting plates."
        mom "Nothing special, I just thought we could have a nice quiet weekend breakfast together."
        "She slides one plate in front of you and one plate in front of [lily.possessive_title], then turns around to get her own before sitting down to join you."
        $ scene_manager.update_actor(mom, position = "sitting")
        mom "Go ahead, eat up!"
        $ lily.change_love(3)
        $ mom.change_stats(love = 3, happiness = 5)
        "You enjoy a relaxing breakfast bonding with [mom.possessive_title] and [lily.name]. [mom.possessive_title] seems particularly happy she gets to spend time with you."
        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    $ scene_manager.clear_scene()
    return "Advance Time"
