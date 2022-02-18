init 5 python:
    config.label_overrides["student_dinner"] = "student_dinner_enhanced"


label student_dinner_enhanced(the_student, the_mom, first_time):
    #TODO Have a unique dining room background
    python:
        clear_scene()
        scene_manager = Scene()
        christina.home.show_background()
        scene_manager.add_actor(the_student, emotion = "happy")

    if first_time:
        "[the_student.possessive_title] leads you into a finely decorated dining room. She pulls out a chair and motions for you to sit down at the table."
    else:
        "[the_student.possessive_title] leads you into the dining room and pulls out a chair for you."

    the_student "You just have a seat, I'll get everything ready."
    $ scene_manager.update_actor(the_student, position = "sitting")
    "You sit down and wait while [the_student.possessive_title] sets out place mats and cutlery. When she's done she sits down in the seat next to you."
    $ scene_manager.add_actor(the_mom, display_transform = character_left_flipped)
    "After waiting for a few minutes [the_mom.possessive_title] steps out from the kitchen, carrying a tray of roasted chicken and a bottle of wine under her arm."
    "She places the tray down, places the bottle of wine down, and sit down across from you and her daughter."
    $ scene_manager.update_actor(the_mom, display_transform = character_center_flipped, position = "sitting")
    the_mom "Mr.[the_mom.last_name] should be home any minute now, he's probably just held up at the office."
    mc.name "No problem, we can wait a little..."
    $ scene_manager.update_actor(the_mom, position = "walking_away")
    "You're interrupted by the phone ringing. [the_mom.possessive_title] apologies and moves into the kitchen."
    $ scene_manager.hide_actor(the_mom)
    the_mom "Yes... Okay... [the_student.name]'s tutor is over for dinner... I'll tell him... We can talk when you get home..."
    $ scene_manager.show_actor(the_mom, position = "sitting", emotion = "sad")
    "[the_mom.possessive_title] comes back into the room and sits down. She has a tense smile as she reaches for the bottle of wine."
    $ mc.change_locked_clarity(5)
    if first_time:
        the_mom "My husband is going to be at the office for the rest of the night, so we should just get started."
        the_mom "He wanted me to tell you how happy he is with your work."
        "[the_student.possessive_title] sits, uncomfortably quiet, as her mother uncorks the bottle of wine and pours herself a generous amount."
    else:
        the_mom "My husband is going to be at the office later again. He told us to have dinner without him."
        "[the_student.possessive_title] sighs unhappily as her mother uncorks the bottle of wine. She pours herself a generous glass."

    the_mom "Let me pour you both a glass..."
    "You have dinner with [the_student.possessive_title] and [the_mom.possessive_title]."
    "[the_mom.possessive_title] seems tense at first, but after some food and two glasses of wine she is smiling and making pleasant conversation."
    $ scene_manager.update_actor(the_mom, emotion = "happy")
    the_mom "[the_student.name], you made a very good choice when you asked [the_mom.mc_title] to tutor you. He's an absolute pleasure to have around."
    if the_student.love > 40 or the_student.effective_sluttiness() > 30:
        "[the_student.possessive_title] places her hand on your thigh and rubs it for emphasis."
        $ mc.change_locked_clarity(15)
        if the_student.effective_sluttiness() > 50:
            "She carries on the conversation with her mother, but her hand starts to drift higher up."
            $ mc.change_locked_clarity(20)
            "Soon [the_student.possessive_title] is rubbing your bulge under the table, massaging it through your pants."

    if the_mom.effective_sluttiness() > 20:
        $ mc.change_locked_clarity(10)
        "While you are talking you feel a gentle touch on your leg. You glance under the table and see it is [the_mom.possessive_title]'s foot caressing your calf."
        "She turns to you and smiles, keeping up her conversation with her daughter while her foot moves up your leg."
        $ mc.change_locked_clarity(10)
        "Soon enough she is rubbing her soft foot against your inner thigh. The movement brings her dangerously close to brushing your cock."
        "After a few moments of teasing she draws her leg back and slips her foot back in her shoe."

    the_mom "Now, how about I get dessert ready. [the_student.name], please clean the table. Leave my wine, I'll have the rest with dessert."
    $ scene_manager.update_actor(the_student, position = "stand3")
    the_student "Okay Mom."
    $ scene_manager.update_scene(position = "walking_away")
    "Both women stand up. [the_mom.possessive_title] moves into the kitchen, while her daughter collects a stack of dirty dishes before following behind her."
    $ clear_scene()
    # You can already give Emily serum while she's studying, so this is just to corrupt her Mom.
    menu:
        "Add serum to [the_mom.possessive_title]'s wine" if mc.inventory.get_any_serum_count() > 0:
            call give_serum(the_mom) from _call_give_serum_student_dinner_enhanced
            if _return:
                "You stand up and lean over the table, quickly emptying the contents of a small glass vial into [the_mom.possessive_title]'s half finished wine glass."
                "You give the glass a quick swirl, then sit back down and wait for [the_mom.possessive_title] and [the_student.possessive_title] to return."
            else:
                "You reconsider, and instead sit back in your chair and wait for [the_mom.possessive_title] and [the_student.possessive_title] to return."

        "Add serum to [the_mom.possessive_title]'s wine\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.get_any_serum_count() == 0:
            pass
        "Leave her drink alone":
            "You lean back in your chair and relax while you wait for [the_mom.possessive_title] and [the_student.possessive_title] to return."


    "After another minute or two both of them come back from the kitchen, now carrying small bowls of ice cream."
    $ scene_manager.update_actor(the_mom, position = "stand3")
    $ scene_manager.update_actor(the_student, position = "sitting")
    "[the_student.possessive_title] places one bowl down in front of you before sitting back in her chair beside you."
    $ scene_manager.update_actor(the_mom, position = "sitting")
    "[the_mom.possessive_title] sits down and takes a sip from her wine."
    the_mom "I'm glad you were able to join us for the evening [the_mom.mc_title]."
    the_mom "It seems like my husband is always at work, it's nice to have some company."
    menu:
        "Talk about [the_student.possessive_title]":
            mc.name "It's no trouble. It also gives us a perfect opportunity to talk about your daughters education."
            if the_mom.event_triggers_dict.get("student_mom_extra_obedience", False):
                the_mom "Yes, give me an update on how things are going."
                "You give [the_mom.possessive_title] a recap of your work educating [the_student.possessive_title], leaving out anything too explicit."
                $ the_mom.change_happiness(5)
                the_mom "It sounds like you have everything under control. Good work."

            else:
                the_mom "That's a very good idea. Is she giving you any problems?"
                "You glance at [the_student.possessive_title] at your side, then shake your head."
                mc.name "No, she is doing very well. There are some new study techniques that I would like to try though."
                the_mom "Is that so? Well you have my full permission. [the_student.name], I want you to do everything [the_mom.mc_title] tells you to do."
                the_mom "Please treat his instructions as if they were coming from me or your father."
                $ the_student.change_obedience(10)
                the_student "Yes Mom, I promise I will."
                $ the_mom.event_triggers_dict["student_mom_extra_obedience"] = True

        "Flirt with [the_mom.possessive_title]":
            mc.name "The pleasure is all mine. Your daughter is wonderful, I should have known she got it from her mother."
            "[the_mom.possessive_title] laughs and waves you off."
            the_mom "You're too kind."
            "You flirt with [the_mom.possessive_title] as much as you think you can get away with while her daughter is in the room."
            $ the_mom.change_slut(1, 25)
            $ the_mom.change_love(2, max_modified_to = 25)

        "Touch [the_student.possessive_title]" if the_student.effective_sluttiness("touching_body") > 35:
            mc.name "I'm glad to be here. I'm always happy to spend time with you and your daughter."
            "You move a hand to your side, then and onto [the_student.possessive_title]'s thigh, rubbing it gently."
            $ mc.change_locked_clarity(10)
            "You move your hand higher, up her thigh and to her crotch. You can feel her struggling to keep still in front of her mother."

            if the_student.effective_sluttiness() > 50:
                "In response [the_student.possessive_title] moves her hand onto your crotch, the movements hidden by the table."
                $ mc.change_locked_clarity(20)
                "She runs her hand along the bulge of your crotch, stroking you slowly through the fabric."
                the_student "He's been such a strong, firm presence in my life since I met him. I'm really learning a lot."
                $ the_student.change_slut(1, 65)
                $ mc.change_locked_clarity(20)
                "You and [the_student.possessive_title] fondle each other while you eat dessert, doing your best to keep [the_mom.possessive_title] from noticing everything."

            else:
                $ mc.change_locked_clarity(10)
                "You fondle [the_student.possessive_title] as you eat your dessert, doing your best to keep [the_mom.possessive_title] from noticing."

            $ the_student.change_slut(1 + the_student.get_opinion_score("public sex"))
            $ the_student.discover_opinion("public sex")
            "Eventually you finish your ice cream."
            the_mom "[the_student.name], could you clean things up for us?"

    $ scene_manager.update_actor(the_student, position = "walking_away")
    "[the_student.possessive_title] collects up the dishes again when you finished dessert and carries them to the kitchen."
    $ scene_manager.hide_actor(the_student)
    the_mom "It's been wonderful having you over [the_mom.mc_title], but I'm sure you're looking forward to getting home."
    $ scene_manager.update_actor(the_mom, position = "stand3")
    mc.name "The dinner was fantastic. I'm lucky to have such a generous, beautiful host."
    "[the_mom.possessive_title] seems to blush, although it might just be wine taking effect."

    $ her_hallway.show_background()
    $ scene_manager.show_actor(the_student, position = "stand4")
    "[the_mom.possessive_title] and [the_student.possessive_title] walk you to the door to say goodbye."
    the_student "Bye [the_student.mc_title], I hope you'll be by again soon!"

    if the_mom.effective_sluttiness("kissing") > 20 and not the_mom.event_triggers_dict.get("student_mom_door_kiss", 0) == 1: #TODO: Add a check that we haven't triggered the "I'm sorry" event.
        the_mom "[the_student.name], I need to have a private word with [the_mom.mc_title] before he goes."

        $ scene_manager.remove_actor(the_student)
        "[the_student.possessive_title] nods and goes upstairs to her room. [the_mom.possessive_title] waits until she is gone before turning back to you."
        if the_mom.event_triggers_dict.get("student_mom_door_kiss", 0) == 2: #TODO: Add a check that you've also triggered the "I'm sorry event
            # She wants to kiss you, and you've already done it before
            the_mom "I just wanted to say thank you again for coming over..."
            $ scene_manager.update_actor(the_mom, position = "kissing", emotion = "happy", special_modifier = "kissing")
            "She takes a half step closer and leans in. You close the rest of the gap and kiss her."
            $ mc.change_locked_clarity(10)
            "[the_mom.possessive_title] kisses you passionately at the door, rubbing her body against you for a moment."
            "After a long moment she pulls back and breaks the kiss, panting softly."
            $ scene_manager.update_actor(the_mom, special_modifier = None)
            $ the_mom.break_taboo("kissing")
            the_mom "Come again soon, okay? I don't like being lonely..."
            mc.name "I won't be gone long."
            $ scene_manager.update_actor(the_mom, position = "stand3")
            "She watches you from the front door as you leave."

        else:
            # It's the first time
            mc.name "Is something wrong?"
            the_mom "No, nothing is wrong. I wanted to say thank you for tutoring my daughter."
            "She takes a half step closer, putting one of her legs between yours."
            the_mom "And for spending the evening with me, when I would have otherwise been all alone..."
            "She leans close, barely an inch separating you from her. You can smell the faint hint of wine on her breath."
            the_mom "With no one to comfort me..."
            $ scene_manager.update_actor(the_mom, position = "kissing", emotion = "happy", special_modifier = "kissing")
            "[the_mom.possessive_title] closes the gap and kisses you passionately, almost over-eagerly."
            $ mc.change_locked_clarity(10)
            "She presses her body against you and holds the back of your neck. After a long moment she pulls back, panting softly."
            $ scene_manager.update_actor(the_mom, special_modifier = None)
            $ the_mom.change_slut(1, 60)
            $ the_mom.break_taboo("kissing")
            the_mom "Thank you for staying for dinner [the_mom.mc_title]. I hope I see you again soon..."
            $ scene_manager.update_actor(the_mom, position = "stand3")
            "She steps back, trailing a hand along your chest."
            mc.name "I hope so too. Goodnight [the_mom.title]."
            "She watches you from the front door as you leave the house."
            $ add_student_mom_apologize_action(the_mom)

    else:
        the_mom "You're welcome to come again for dinner any time [the_mom.mc_title]. Have a good evening."
        "They watch you from the porch as you leave."





    #TODO: Something like "It's nice to have some company at home..."
    #TODO: Branching options? Let the player select what they want to do?
    #TODO: Something should lead directly into her having the affair role.
    #TODO: Options like "Talk about her daughter.", "Flirt with Christina.".
    #TODO: If she's slutty enough (should be achievable with some minor corruption or serum use, 25-ish) she finds a way to kiss you. The next time you're over she appologises.



    # TODO: This event. YOu stay for dinner. Emily's father is "delayed at the office", so the three of you have dinner together.
    # Christina praises your work and gives you permission to "do whatever you need to do to help her daughter."
    # Mention that she should "get more involved" in her daughters schooling.
    # She also gets a little tipsy and a little hands-y with you when you go to leave.

    $ the_mom.event_triggers_dict["stayed_for_dinner"] += 1
    $ scene_manager.clear_scene()
    return
