# Enhance Morning Breakfast with multi person rendering and updated dialog

init 5 python:
    config.label_overrides["family_morning_breakfast_label"] = "family_morning_breakfast_enhanced_label"

label family_morning_breakfast_enhanced_label():
    python:
        mom_slutty = False
        sis_slutty = False
        if mom.sluttiness > 40:
            mom_slutty = True
            mom.outfit = mom.wardrobe.get_random_appropriate_underwear(mom.sluttiness)

        if lily.sluttiness > 40:
            sis_slutty = True
            lily.outfit = lily.wardrobe.get_random_appropriate_underwear(lily.sluttiness)

        #Make sure we're in our bedroom when the event starts.
        mc.change_location(bedroom)
        # initialize scene manager for multi person scene
        scene_manager = Scene()

    "In the morning you're awoken by a knock on your bedroom door."
    mc.name "Uh, come in?!"
    "Feeling a little groggy, you sit up in bed."
    if mom.love > lily.love:
        $ scene_manager.add_actor(mom)
        "[mom.possessive_title] cracks open the door and leans in."
        mom.char "I'm making some breakfast for you and [lily.name]. Come on down if you'd like some."
        mc.name "Thanks [mom.title], I'll be down in a minute."
        $ scene_manager.update_actor(mom, emotion = "happy")
        "She flashes you a smile and closes the door."
        $ scene_manager.remove_actor(mom)
    else:
        $ scene_manager.add_actor(lily)
        "[lily.possessive_title] cracks your door open and leans in. She seems just as tired as you are."
        lily.char "Hey, I think Mom's making a family breakfast for us."
        mc.name "Thanks for letting me know [lily.title], I'll be down in a minute."
        "She nods and closes your door as she leaves."
        $ scene_manager.remove_actor(lily)
    
    "You get up, get dressed, and head for the kitchen."
    $ mc.change_location(kitchen)
    $ scene_manager.add_actor(mom, position = "walking_away", character_placement = character_left_flipped)

    if mom_slutty:
        if mom.outfit.vagina_visible():
            "[mom.possessive_title] is in front of the stove naked, humming as she scrambles a pan full of eggs."
        elif mom.outfit.tits_visible():
            "[mom.possessive_title] is standing in front of the stove topless, humming as she scrambles a pan full of eggs."
        else:
            "[mom.possessive_title] is just in her underwear in front of the stove, humming as she scrambles a pan full of eggs."
    else:
        "[mom.possessive_title] is at the stove and humming to herself as she scrambles a pan full of eggs."

    $ scene_manager.update_actor(mom, position = "back_peek")

    mom.char "Good morning [mom.mc_title]. I'm almost ready to serve, hopefully your [lily.name] will be here soon."
    lily.char "I'm coming!"

    $ scene_manager.add_actor(lily)

    if sis_slutty:
        if lily.outfit.vagina_visible():
            "[lily.possessive_title] comes into the room naked. She gives a dramatic yawn before sitting down at the kitchen table."
        elif lily.outfit.tits_visible():
            "[lily.possessive_title] walks topless into the kitchen. Yawning dramatically before sitting down at the table."
        else:
            "[lily.possessive_title] walks into the room only wearing her underwear. She gives a dramatic yawn before sitting down at the kitchen table."
    else:
        "[lily.possessive_title] comes into the room and gives a dramatic yawn before sitting down at the kitchen table."
    $ scene_manager.update_actor(lily, position = "sitting")
    
    if mom_slutty and sis_slutty:
        #You have breakfast with both of them stripped down like it's no big thing.
        lily.char "Hope I'm not too late."
        $ scene_manager.update_actor(mom, position = "walking_away")
        "Your mother takes the pan off the stove and begins to slide the contents off onto three plates."
        mom.char "No, just on time."
        $ scene_manager.update_actor(mom, position = "stand3")
        "She turns around and hands one plate to you and one plate to [lily.title]."
        lily.char "Thanks Mom, you're the best!"
        $ scene_manager.update_actor(mom, position = "sitting")
        mom.char "No problem, I'm just happy to spend my morning relaxing with my two favourite people!"
        "You enjoy a relaxing breakfast bonding with your mother and lily. [mom.possessive_title] seems particularly happy she gets to spend time with you."
        "Neither [lily.title] or [mom.possessive_title] seem to think it's strange to relax in their underwear."
        $ lily.change_stats(love = 3, slut_temp = 3)
        $ mom.change_stats(love = 3, slut_temp = 3, happiness = 10)
        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    elif mom_slutty and not sis_slutty:
        #Lily thinks her mom is embarassing and weird but Mom pulls rank.
        lily.char "Oh my god Mom, what are you wearing?"
        $ scene_manager.update_actor(mom, position = "back_peek")
        mom.char "What? It's the weekend and it's just the three of us. I didn't think anyone would mind if I was a little more casual."
        $ scene_manager.update_actor(lily, position = "sitting")

        if mom.outfit.vagina_visible():
            lily.char "Mom, I don't think you know what casual means. Could you at least put on some panties or something?"
        elif mom.outfit.tits_visible():
            lily.char "Mom, I don't think you know what casual means. I mean, couldn't you at least put on a bra?"
        else:
            lily.char "Mom, you're prancing around the kitchen in your underwear. In front of your son and daughter. That's weird."
            "[lily.title] looks at you."
            lily.char "Right [lily.mc_title], that's weird?"

        if mom.obedience > 115:
            $ scene_manager.update_actor(mom, position = "stand3")
            mom.char "What do you think [mom.mc_title], do you think it's \"weird\" for your mother to want to be comfortable in her own house?"
            menu:
                "Side with Mom.":
                    mc.name "I think Mom's right [lily.title]. It's nothing we haven't seen before, she's just trying to relax on her days off."
                    $ mom.change_obedience(-5)
                    $ lily.change_obedience(5)
                    "[lily.title] looks at the two of you like you're crazy then sighs dramatically."
                    lily.char "Fine, but this is really weird, okay?"
                    $ scene_manager.update_actor(mom, position = "sitting")
                    "[mom.possessive_title] dishes out three portions and sits down at the table with you. [lily.title] eventaully gets use to her mothers outfit and joins in on your conversation."
                    $ lily.change_slut_temp(5)
                    $ mom.change_happiness(10)


                "Side with [lily.title].":
                    mc.name "I actually think [lily.title] is right, this is a little weird. Could you go put something on, for our sakes?"
                    $ lily.change_stats(obedience = -2, slut_temp = 2)
                    $ mom.change_stats(obedience = 5, slut_temp = 5)
                    mom.char "Oh you two, you're so silly. Fine, I'll be back in a moment. [lily.title], could you watch the eggs?"
                    $ scene_manager.remove_actor(mom)
                    $ scene_manager.update_actor(lily, position = "walking_away", character_placement = character_left_flipped)
                    "Your mother leaves to get dressed. [lily.possessive_title] ends up serving out breakfast for all three of you."
                    $ scene_manager.update_actor(lily, position = "sitting")
                    $ mom.outfit = mom.planned_outfit.get_copy()
                    lily.char "She's been so weird lately. I don't know what's going on with her..."
                    $ scene_manager.add_actor(mom, position = "sitting", character_placement = character_right)
                    $ lily.change_happiness(5)
                    $ mom.change_happiness(5)
                    "When [mom.possessive_title] gets back she sits down at the table and the three of you enjoy your breakfast together."

        else:
            #She likes what she likes
            mom.char "Well luckily I'm your mother and it doesn't matter what you think. I'm going to wear what makes me comfortable."
            "She takes the pan off the stove and slides the scrambled eggs out equally onto three plates."
            $ scene_manager.update_actor(mom, position = "stand3")
            mom.char "Now, would you like some breakfast or not?"
            "[lily.title] sighs dramatically."
            lily.char "Fine, but this is really weird, okay?"
            $ lily.change_slut_temp(5)
            $ mom.change_happiness(10)
            $ scene_manager.update_actor(mom, position = "sitting")
            "[mom.possessive_title] gives everyone a plate and sits down. [lily.title] eventually gets used to her mothers outfit and joins in on your conversation."
            "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."


    elif sis_slutty and not mom_slutty:
        #MOm thinks lilly is way too underdressed and sends her back to get dressed.
        "Your mother turns around and gasps."
        $ scene_manager.update_actor(mom, position = "stand3", emotion="angry")
        mom.char "[lily.name]! What are you wearing?"
        lily.char "What do you mean? I just got up, I haven't had time to pick out an outfit yet."
        mom.char "You shouldn't be running around the house naked. Go put some clothes on young lady."
        $ scene_manager.update_actor(lily, emotion = "angry")
        "[lily.possessive_title] scoffs and rolls her eyes."
        lily.char "Come on Mom, you're being ridiculous. This is my house too, I should be able to wear whatever I want!"
        "[mom.possessive_title] and [lily.name] lock eyes, engaged in a subtle battle of wills."
        if lily.obedience > mom.obedience:
            $ scene_manager.update_actor(mom, position = "walking_away", emotion = None)
            "[mom.possessive_title] sighs loudly and turns back to the stove."
            mom.char "Fine! You're so stubborn [lily.name], I don't know how I survive around here!"
            $ lily.change_stats(obedience = -2, happiness = 10, slut_temp = 3)
            $ mom.change_obedience(10)
            $ scene_manager.update_actor(lily, emotion = "happy")
            "[lily.possessive_title] looks at you, obviously pleased with herself, and winks."

        else:
            "[lily.title] finally sighs loudly and looks away. She pushes her chair back and stands up in defeat."
            $ scene_manager.update_actor(lily, position = "stand4")
            lily.char "Fine! I'll go put on some stupid clothes so my stupid mother doesn't keep worrying."
            $ scene_manager.update_actor(lily, position = "walking_away")
            "[lily.title] sulks out of the kitchen."
            $ scene_manager.remove_actor(lily)
            $ scene_manager.update_actor(mom, position = "walking_away", emotion = "sad")
            mom.char "I don't know how I manage to survive with you two around!"
            $ lily.outfit = lily.planned_outfit.get_copy()
            $ lily.change_stats(obedience = 10, happiness = -5)
            $ mom.change_obedience(-2)
            $ scene_manager.add_actor(lily, position = "sitting")
            "[lily.possessive_title] is back by the time Mom starts to plate breakfast. She sits down and starts to eat without saying anything."
            $ scene_manager.update_actor(mom, position = "sitting")

        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    else:
        #Neither of them are particularly slutty, so it's just a normal breakfast.
        lily.char "So what's the occasion Mom?"
        $ scene_manager.update_actor(mom, position = "stand3")
        "[mom.possessive_title] takes the pan off the stove and scoops the scrambled eggs out equally onto three waiting plates."
        mom.char "Nothing special, I just thought we could have a nice quiet weekend breakfast together."
        "She slides one plate in front of you and one plate in front of [lily.possessive_title], then turns around to get her own before sitting down to join you."
        $ scene_manager.update_actor(mom, position = "sitting")
        mom.char "Go ahead, eat up!"
        $ lily.change_love(3)
        $ mom.change_stats(love = 3, happiness = 5)
        "You enjoy a relaxing breakfast bonding with [mom.possessive_title] and [lily.name]. [mom.possessive_title] seems particularly happy she gets to spend time with you."
        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    python:
        renpy.scene("Active")
        mom.review_outfit(show_review_message = False)
        lily.review_outfit(show_review_message = False)
    return