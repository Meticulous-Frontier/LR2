label introvert_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 85:
        the_person "Oh fuck, you look so much bigger than any of the toys I've fit inside my ass before..."
        mc.name "Don't worry, I'll stretch you out just fine."
        "The thought seems to turn her on more than scare her."
    elif the_person.love >= 60:
        the_person "I can't believe we're doing this... Do you think you'll even fit?"
        mc.name "I'll fit, but you might not be walking right for a few days."
        the_person "Haha, sure thing..."
        the_person "... You're kidding, right?"
        mc.name "Let's find out."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Fuck, you must really like it tight. We've never even fucked and you're going right for my asshole!"
            the_person "Are you even sure it's going to fit?"
            mc.name "I'll make it fit, but you might not be walking right for a few days."
            the_person "Oh fuck..."
        else:
            the_person "Oh my god, you're actually going to do it! Fuck, I hope you even fit!"
            mc.name "Don't worry, I'll stretch out your ass like I've stretched out all your other holes."
    return

label relaxed_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "[the_person.title] takes a few deep breaths."
        the_person "Whew, I think I'm ready!"
        the_person "Fuck me in the ass [the_person.mc_title]! Stretch me out and ruin me!"
    elif the_person.love >= 60:
        the_person "I can't believe we're doing this... Do you think you'll even fit?"
        mc.name "I'll fit, but you might not be walking right for a few days."
        the_person "Haha, sure thing..."
        the_person "... You're kidding, right?"
        mc.name "Let's find out."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Fuck, you must really like it tight. We've never even fucked and you're going right for my asshole!"
            the_person "Are you even sure it's going to fit?"
            mc.name "I'll make it fit, but you might not be walking right for a few days."
            the_person "Oh fuck..."
        else:
            the_person "Oh my god, you're actually going to do it! Fuck, I hope you even fit!"
            mc.name "Don't worry, I'll stretch out your ass like I've stretched out all your other holes."
    return

label reserved_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "She takes a few deep breaths."
        the_person "I'm ready if you are [the_person.mc_title]. Come and fuck my ass."
    elif the_person.love >= 60:
        the_person "This is really something you want to do then [the_person.mc_title]?"
        mc.name "Yeah, it is."
        the_person "Okay then. It wouldn't be my first pick, but we can give it a try."
        the_person "I don't know if you'll even fit though. Your penis is quite large."
        mc.name "You'll stretch out more than you think."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Oh lord, what happened to me?"
            the_person "I thought I was a respectable lady, now I'm about to get fucked in the ass..."
            the_person "We've never even had sex before and now I'm doing anal!"
            #TODO: "At least my vagina still belongs to my SO... At least I still have that one thing."
        else:
            the_person "I'm not sure about this [the_person.mc_title]... I'm not even sure if you can fit inside me there!"
            mc.name "I can stretch you out, don't worry about that."
            the_person "Oh lord, what happened to me..."
            the_person "I used to think I was a respectable lady, now I'm about to get fucked in the ass..."
        mc.name "Relax, you'll be fine and this isn't the end of the world. Who knows, you might even enjoy yourself."
        the_person "I doubt it. Come on then, there's no point stalling any longer."
    return

label wild_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75 and the_person.sex_record.get("Anal Sex", 0) > 3:
        the_person "Oh god, it always surprises me how big your cock is! You're going to tear my ass in half with that monster!"
        "She seems more turned on by the idea than worried."
        mc.name "Don't worry, you'll be stretched out soon enough."
    elif the_person.love >= 60:
        the_person "So you really want to do this? It might be a little hard to fit all of your cock inside me..."
        mc.name "Don't worry about that, I'll have you stretched out soon enough."
        the_person "Fuck, just try and make sure you don't break me permanently!"
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you, I don't even know if I can fit your cock in my ass!"
            mc.name "I'll make it fit, but you might not be walking right for a few days."
            the_person "Oh fuck..."
        else:
            "She closes her eyes and talks quietly to herself."
            the_person "Whew, deep breathes [the_person.fname]. You can do this..."
            mc.name "Are you okay?"
            the_person "Yeah, of course. I'm just... a little nervous. Fuck, I don't normally feel like this."
            "She laughs and shakes her head."
            the_person "Not that I normally do, you know, this. I don't know what's gotten into me."
            mc.name "Hopefully me, soon."
            the_person "No time like the present then. Do it, before I chicken out!"
    return

label lily_dual_penetration_taboo_break(the_person):
    if the_person.love > 60:
        the_person "Wait, do you really mean you want to try anal?"
        if the_person.has_taboo("vaginal_sex"):
            mc.name "Yeah, I do. I want to have sex, but you probably don't want me fucking your pussy yet."
            the_person "Ever. That would be actual, full incest [the_person.mc_title]."
            mc.name "Exactly, so we can cheat a little like this."
            "[the_person.possessive_title] seems unsure."
            mc.name "Come on, don't you want to experiment with someone you trust?"
        else:
            mc.name "Yeah, why not? I've already fucked all of your other holes, what's special about this one?"
            the_person "It's not special, I just thought you'd want to fuck my pussy some more. Didn't you enjoy it last time?"
            mc.name "It was great, but I want to experiment a little more. Come on, don't you want to try something new?"
    else:
        the_person "Wait, do you want to try anal?"
        mc.name "Yeah, I do. You've got a cute butt."
        if the_person.has_taboo("vaginal_sex"):
            the_person "You're crazy [the_person.mc_title]! We're related, we shouldn't  be fucking!"
            mc.name "It's not like it's real sex. If you want I can go to town on your pussy though, it looks just as tight."
            the_person "I guess anal isn't as bad as my own brother fucking my pussy..."
        else:
            the_person "What's wrong with my pussy? Didn't you enjoy it last time?"
            mc.name "It was great, I just want to try something new. Come on, you like experimenting, right?"
            the_person "I guess this way I don't have to worry about you pulling out..."
    "She sighs and gives in."
    the_person "Okay, but you need to be gentle with me."
    mc.name "I promise I will. Have you ever tried this before?"
    the_person "With toys a couple of times... Never with a guy."
    mc.name "You'll probably be really tight then. I'll go nice and slow to give you time to stretch out."
    the_person "Okay. Thank you [the_person.mc_title]."
    return

label mom_dual_penetration_taboo_break(the_person):
    if the_person.love > 60:
        the_person "Oh my god, you mean my butt! I... That's not where that goes, [the_person.title]!"
        if the_person.has_taboo("vaginal_sex"):
            mc.name "Should I slide it into your pussy then?"
            the_person "Of course not! You're my son, which means we absolutely should not be having sex."
            mc.name "That's why I want to try anal. I couldn't get you pregnant, so it's not really incest."
            mc.name "I love you so much [the_person.title], I want to try every way possible to be close to each other."
            the_person "I guess it wouldn't really count. It's no different than me using my hand or my breasts, right?"
            mc.name "That's what I'm saying. Have you ever tried this before?"
        else:
            mc.name "Trust me [the_person.title], we can make it work."
            the_person "Isn't my pussy enough? Why do you want to try anal all of a sudden?"
            if the_person.has_taboo("condomless_sex"):
                mc.name "If I'm fucking your pussy I need to wear a condom, but I don't need one if we do it like this."
                the_person "Does it really feel that much better?"
                mc.name "It really does."
                the_person "Okay, for your happiness I'll give it a try."
            else:
                mc.name "If I'm fucking your pussy I might get you pregnant, but with anal that can't happen."
                the_person "Or you could put on a condom."
                mc.name "Those feel like crap though [the_person.title]. I want to feel you wrapped around my cock."
                the_person "Well... Okay, if it would make you happy we can give it a try."
            mc.name "Thank you [the_person.title]. Have you ever done this before?"
        "[the_person.possessive_title] shakes her head sheepishly."
        the_person "No. I never thought I would either."
        mc.name "I'll be as gentle as possible then."
        the_person "Thank you. I love you [the_person.mc_title]."
        mc.name "I love you [the_person.title]."
    else:
        the_person "Whoa! You mean you want to try anal? Right now?"
        if the_person.has_taboo("vaginal_sex"):
            mc.name "Why not? It's not really incest if you can't get pregnant from it, right?"
            the_person "I kind of see what you mean..."
        else:
            if the_person.has_taboo("condomless_sex"):
                mc.name "Why not? If I want to fuck your pussy I need to wear a condom, and they really kill the sensation."
                mc.name "If we do anal I can go in raw and feel you wrapped around me."
            else:
                mc.name "Why not? If I fuck your pussy I might get you pregnant, but that can't happen with anal."
                the_person "Or you could wear a condom."
                mc.name "They really kill the sensation. I want to feel you wrapped around my cock."
        the_person "That does sound nice..."
        mc.name "Have you ever tried anal before?"
        "She shakes her head."
        the_person "No. I've thought about it, but I've never been brave enough to try it."
        mc.name "I'll be as gentle as possible then, so you have time to adjust."
        the_person "It feels so naughty to give my anal virginity to my own son. It's kind of turning me on."
    return
