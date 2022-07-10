init 5 python:
    config.label_overrides["wild_cum_face"] = "wild_cum_face_enhanced"
    config.label_overrides["wild_cum_mouth"] = "wild_cum_mouth_enhanced"
    config.label_overrides["reserved_cum_face"] = "reserved_cum_face_enhanced"
    config.label_overrides["reserved_cum_mouth"] = "reserved_cum_mouth_enhanced"
    config.label_overrides["bimbo_cum_face"] = "bimbo_cum_face_enhanced"
    config.label_overrides["bimbo_cum_mouth"] = "bimbo_cum_mouth_enhanced"
    config.label_overrides["introvert_cum_face"] = "introvert_cum_face_enhanced"
    config.label_overrides["introvert_cum_mouth"] = "introvert_cum_mouth_enhanced"
    config.label_overrides["relaxed_cum_face"] = "relaxed_cum_face_enhanced"
    config.label_overrides["relaxed_cum_mouth"] = "relaxed_cum_mouth_enhanced"
    config.label_overrides["stephanie_cum_face"] = "stephanie_cum_face_enhanced"
    config.label_overrides["stephanie_cum_mouth"] = "stephanie_cum_mouth_enhanced"

label wild_cum_face_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("cum facials") > 0:
            the_person "What do you think? Is this a good look [the_person.mc_title]?"
            "[the_person.title] licks her lips, moving a few drops of your semen that had run down her face with her fingers to her mouth."
        else:
            the_person "I hope you had a good time [the_person.mc_title]. It certainly seems like you did."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("cum facials") > 0:
            the_person "Mmm, that's such a good feeling. Do you think I look cute like this?"
            "[the_person.title] runs her tongue along her lips, then smiles and laughs."
        else:
            the_person "Whew, glad you got that over with. Take a good look while it lasts."
    return

label wild_cum_mouth_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Mmm, thank you [the_person.mc_title]."
        else:
            "[the_person.title]'s face grimaces as she tastes your cum in her mouth."
            the_person "Ugh. There, all taken care of [the_person.mc_title]."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Mmm, you taste great [the_person.mc_title]. Was it nice to watch me take your load in my mouth?"
        else:
            the_person "Ugh, that's such a... unique taste."
    return

label reserved_cum_face_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("cum facials") > 0:
            the_person "Ah, that's always a pleasure, [the_person.mc_title]."
        else:
            the_person "Well that's certainly a lot. I hope that means I did a satisfactory job."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("cum facials") > 0:
            the_person "Oh [the_person.mc_title], what are you doing to me? I'm beginning to like looking like this!"
        else:
            the_person "Oh god [the_person.mc_title], could you imagine if someone saw me like this? I really should go and get cleaned up."
    return

label reserved_cum_mouth_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Mmm, always a pleasure to taste you [the_person.mc_title]. I hope you had a good time."
        else:
            "[the_person.title] puckers her lips, obviously not happy with the taste but too polite to say anything."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.get_opinion_score("drinking cum") > 0:
            the_person "You're making me act like such a slut [the_person.mc_title], what would other women think if they knew what I just did?"
        else:
            the_person "Well, at least there's no mess to clean up. I need to go wash my mouth out after that though."
    return

label bimbo_cum_face_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("cum facials") > 0:
            the_person "Do I look cute covered in your cum, [the_person.mc_title]?"
            "[the_person.title] licks her lips, scooping up a few drops of your semen that dripped down her face with her finger and licking them off."
        else:
            the_person "I hope this means I did a good job."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("cum facials") > 0:
            the_person "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
        else:
            the_person "Fuck me, you really pumped it out, didn't you?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label bimbo_cum_mouth_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Your cum tastes really great [the_person.mc_title], try giving me more next time, I love it."
            "[the_person.title] licks her lips and smiles at you."
        else:
            if the_person.sex_record.get("Cum in Mouth", 0) < 4:
                the_person "Yeez, I don't know if I'll ever, like that stuff."
            else:
                "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
    return

label introvert_cum_face_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("cum facials") > 0:
            "[the_person.title] licks her lips and moves her tongue up to catch a few drops of semen that spilled out of her nose."
        else:
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("cum facials") > 0:
            "[the_person.title] looks you in the eye, then runs her tongue over her lips seductively."
        else:
            "[the_person.title] wipes some of your cum off her face with the back of her hand."
    return

label introvert_cum_mouth_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Mmm. Thank you."
        else:
            the_person "Mmm."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Mmm, you taste great."
        else:
            the_person "Ugh."
    return

label relaxed_cum_face_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("cum facials") > 0:
            the_person "Do I look cute covered in your cum, [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person "I hope this means I did a good job."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("cum facials") > 0:
            the_person "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
        else:
            the_person "Fuck me, you really pumped it out, didn't you?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label relaxed_cum_mouth_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            if the_person.sex_record.get("Cum in Mouth", 0) < 4:
                the_person "Bleh, I don't know if I'll ever get used to that."
            else:
                "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
    return

label stephanie_cum_face_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish():
            the_person "Mmm, that feels nice."
        elif the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("cum facials") > 0 or the_person.get_opinion_score("drinking cum") > 1:
            the_person "Mmm, that feels nice. I bet it would feel even nicer in my mouth next time, [the_person.mc_title]."
        elif the_person.get_opinion_score("drinking cum") > 0:
            the_person "There we go, all taken care of. You can cum in my mouth next time if you want, it would make cleaning up a lot faster."
        else:
            the_person "There we go, all taken care of."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 1:
            if the_person.sex_record.get("Cum in Mouth", 0) > 0:
                the_person "Aww, you should shoot it into my mouth next time. I love how your hot cum tastes."
            else:
                the_person "Aww, you should shoot it into my mouth next time. I love the taste of hot cum."
            "[the_person.title] runs a finger through a puddle of your cum and then licks it clean, smiling at you while she does it."
        elif the_person.get_opinion_score("drinking cum") > 0:
            the_person "Oh man, you really got me covered, didn't you? I wish you would just cum in my mouth so I don't have to worry about getting cleaned up."
        else:
            the_person "Oh man, you really got me covered, didn't you?"
    return

label stephanie_cum_mouth_enhanced(the_person):
    if the_person.has_cum_fetish() or the_person.obedience > 130:
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Oh god, you taste so good. Thank you for the treat [the_person.mc_title]."
        else:
            the_person "Mmm, thank you [the_person.mc_title]."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Mmm, your cum tastes so great [the_person.mc_title], are you sure there isn't any more of it for me?"
            "[the_person.title] licks her lips and sighs happily."
        elif the_person.get_opinion_score("drinking cum") > -1:
            "[the_person.title] licks her lips and smiles at you."
            the_person "Mmm, that was nice."
        else:
            "[the_person.title] licks her lips."
    return
