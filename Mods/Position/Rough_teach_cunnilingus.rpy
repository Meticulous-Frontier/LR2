#Original file by Badrabbit
init python:
        teach_oral = Position("Teach Oral", slut_requirement = -20, slut_cap = 60, requires_hard = False, requires_large_tits = False,
            position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Oral",
            girl_arousal = 30, girl_energy = 3,
            guy_arousal = 3, guy_energy = 20,
            connections = [],
            intro = "intro_teach_oral",
            scenes = ["scene_teach_oral_1","scene_teach_oral_2"],
            outro = "outro_teach_oral",
            transition_default = "transition_default_teach_oral",
            strip_description = "strip_teach_oral", strip_ask_description = "strip_ask_teach_oral",
            orgasm_description = "orgasm_teach_oral",
            taboo_break_description = "taboo_break_oral",
            verb = "lick",
            opinion_tags = ["getting head", "taking control"], record_class = "Cunnilingus",
            associated_taboo = "licking_pussy")

# init 1:
#     python:
#         teach_oral.link_positions(other, "transition_label") #If there are transitions they go here

label intro_teach_oral(the_girl, the_location, the_object):
    $ the_girl.draw_person (position = "sitting")
    "[the_girl.possessive_title] sits down."
    the_girl.char "Now, kneel down between my legs."
    "You kneel down as instructed."
    the_girl.char "Good boy."
    $ the_girl.change_arousal (10)
    "She spreads her legs for you, giving you access to her pussy and leans back."
    $ teach_oral.redraw_scene(the_girl) #Draw her sitting down.
    if cousin.event_triggers_dict.get("teach_level", -1) == 0: # First Time (always)
        the_girl.char "I'm going to teach you how to eat pussy, [the_girl.mc_title]."
        the_girl.char "Now everyone is different but I take being a teacher seriously so I'll show you everything you need to know and some more besides."
        the_girl.char "Now, most of the time you'll want to get the girl warmed up a bit first."
        the_girl.char "First, kiss along this leg from my knee inwards."
        "She points at one of her legs and you do as instructed."
        the_girl.char "Now this leg."
        "Again, you do as you are told."
        the_girl.char "Now lick me here."
        "She points to the side of her pussy."
        the_girl.char "keep doing that..."
        the_girl.char "Now the other side..."
        the_girl.char "Now using your hands stroke up the outsides of my legs."
        the_girl.char "Start at my ankles and move up."
        the_girl.char "Then down and now the insides."
        the_girl.char "Change sides with licking."
        "You do as you are told moving your hands and licking as you are instructed."
        "She reaches down and spreads the folds of her vagina."
        the_girl.char "I'm already wet, [the_girl.mc_title]."
        "She runs a finger through her own slit and shivers. She places it in her mouth."
        "She returns her hand to her pussy."
        the_girl.char "Let me show you. This is my clit. Think of it like a small dick."
        the_girl.char "Or should that be an average sized dick for you, micro-boy?"
        the_girl.char "Anyway, it is very sensitive when it is erect. Can you see how it is poking out from under its hood?"
        "You can see her clit a few inches away from your face."
        the_girl.char "When a girl gets excited, you can stimulate the clit with your tongue and lips to bring her over the edge."
        the_girl.char "BUT, for most girls, after she cums her clit will be too sensitive to do anything more with for a while. That said all cunts are different, so you'll need to figure out if that's the case or not."
        the_girl.char "Think you can handle that, Micro?"
        mc.name "Okay."
        "[the_girl.possessive_title] moves her fingers slightly."
        the_girl.char "And these are the pussy lips."
        "[the_girl.possessive_title] spreads the lips with her fingers."
        the_girl.char "This is my pussy - vagina to be specific about it. Generally don't put anything in there until it's got a bit wetter."
        the_girl.char "Now, [the_girl.mc_title], I'm going to teach you how to make me cum with your mouth. First, I want you to kind of kiss me around my clit, but don't touch it yet."
        "You do as you are told."
        the_girl.char "Now this is important so pay attention - variation - mixing things up is not bad but when I get close to coming just keep doing whatever it was that you were. Do NOT change what you are doing."
        the_girl.char "Got it? When I get close do not change what you are doing."
        mc.name "OK."
        the_girl.char  "Now stick your tongue inside of my pussy. Right. Yep. Just like that. Now move your lips up to my clit and suck it into your mouth like you're giving me a blowjob."
        "She arches her back and entwines her fingers in your hair. Apparently, whatever you did you did it right. You keep it up and she responds by grinding her pussy into your face."
        $ the_girl.change_arousal (10)
        $ the_girl.call_dialogue("sex_responses_oral")
        the_girl.char  "Why am I not suprised? I tell you to imagine you're sucking a cock and you're a natural at it. Anyway..."
        $ cousin.event_triggers_dict["teach_level"] = 1
    elif cousin.event_triggers_dict.get("teach_level", -1) == 1 or cousin.event_triggers_dict.get("teach_level", -1) == 2:#basics
        the_girl.char "I think that you need to work on the basics some more - tongue work - to help build up your tongue so that's what we're doing today, [the_girl.mc_title]."
        the_girl.char "Think of an ice cream."
        the_girl.char "Remember - when I get close do not change what you are doing."
        $ cousin.event_triggers_dict["teach_level"] = 2
    elif cousin.event_triggers_dict.get("teach_level", -1) == 3:
        the_girl.char "Today we're going to use your fingers."
        the_girl.char "Remember DON'T just stick them straight in. You need to warm me up a bit first."
        the_girl.char "Anything that you would do with your tongue you can do with you finger but it generally won't feel as good."
        the_girl.char "Now start playing with my clit with your fingers."
        if mc.sex_skills["Foreplay"] < 2:
            "You do as instructed, or at least you try to."
            the_girl.char "FUCK. Really? You're bad at that as well? I supose it makes sense."
        else:
            "You do as instructed."
        the_girl.char "The one exception to that is insertion - your fingers can go longer than a tongue can."
        if mc.sex_skills["Foreplay"] < 2:
            the_girl.char "FUCK. Really? You're bad at that as well? I supose it makes sense."
            "You do as instructed, or at least you try to."
            "She continues for some time."
        else:
            the_girl.char "Now keep playing with my clit - keep doing it."
            "You do as instructed."
            "You continue for some time."
        $ the_girl.change_arousal (40)
        the_girl.char "Alright, now gently put one of your fingers in and feel how wet I am. GENTLY remember."
        "You put your right index finger forward and inserted it into her pussy. It feels soft, warm, and slippery."
        if the_person.has_taboo("vaginal_sex"):
            the_girl.char "Alright, I want you to gently fuck me with your finger - in and out."
            the_girl.char "It's the closest you'll ever get to actually fucking me so try not to get too excited and blow your load."
            the_girl.char "How does that feel?"
            mc.name "Warm. Smooth."
        else:
            the_girl.char "Alright, I want you to fuck me with your finger."
            the_girl.char "It can't be any worse than that poor excuse for a cock that you've got."
            the_girl.char "Try not to get too excited and blow your load early, Micro."
        the_girl.char "OK. Good."
        #the_girl.char "Imagine how that is going to feel when you finally get to stick your thick dick in me."
        #"Yeah..."
    elif cousin.event_triggers_dict.get("teach_level", -1) == 4:
        the_girl.char "Rimming."
        the_girl.char "Don't worry, I'm plenty clean."
        the_girl.char "Some girls like ass stuff so rimming will be enjoyable for them. Others are less keen."
        the_girl.char "Some girls naturally take charge - which you had better get used to - I can't imagine anyone taking any shit from you, limp dick."
        the_girl.char "For us it's more a power thing - about you being humiliated rather than the way it feels."
        the_girl.char "If a girl likes rimming for the feeling then the technique's going to be the same for what else we've done and are going to do."
        the_girl.char "If it's because she enjoys putting you in your proper place then you'll want to put on a big show of how inferior you are - which let's face it shouldn't be too difficult for you."
        the_girl.char "Got it?"
        mc.name "Yeh - OK."
        the_girl.char "Also, eating ass alone probably isn't going to do it for anyone so you need other stuff - we spoke about fingers last time?"
        the_girl.char "Finally, although I'm clean, not everyone is as perfect as me, so be careful going ass to vag."

    elif cousin.event_triggers_dict.get("teach_level", -1) ==5:
        the_girl.char "Look at me"
        the_girl.char "OK. Now gimme your hand."
        the_girl.char "Now this might be quite advanced for your retard brain so try to keep up."
        the_girl.char "I will lick and suck your fingers and you do the same thing to my pussy."
        the_girl.char "Give me your hand."
        "You give [the_girl.title] your hand."
        the_girl.char "Now move in closer."
        "You move slightly closer to her pussy between her legs."
        "She hooks her legs around your shoulders and pulls your head to her cunt."
        the_girl.char "Now let's try. First a big lick."
        "She licks your fingers with a big lick. You lick her cunt with a big lick."
        the_girl.char "Good. Now a butterfly flutter."
        "She flutters her tongue and you do the same."
        the_girl.char "Good."
        the_girl.char "I'm such an excellent teacher even your little brain was able to keep up."
        $ cousin.event_triggers_dict["teach_level"] = 5
    elif cousin.event_triggers_dict.get("teach_level", -1) >= 6:
        the_girl.char "This seems to work best for you so we'll try it again. Gimme your hand."
        the_girl.char "Now remember you copy what I do."
        "[the_girl.possessive_title] pulls your head to her clit wuth one hand. With the other she takes your hand and puts it in her mouth."
        "She flutters her tongue on your fingers and you do the same on her clit."
        the_girl.char "Good - you managed to keep that in your head."
    else:
        "Gone wrong"
    $ teach_oral.redraw_scene(the_girl) #Draw her sitting down.
    $ cousin.event_triggers_dict["oral_chance"] += 5

    return

label taboo_break_oral(the_girl, the_location, the_object):
    "Taboo break none"
    return

label scene_teach_oral_1(the_girl, the_location, the_object):
    if cousin.event_triggers_dict.get("teach_level", -1) == 1:
        the_girl.char "Yes, just like that. Good. Now, use your tongue and lick me from the base of my pussy near my asshole all the way up to my clit."
        "You do as you are told."
    elif cousin.event_triggers_dict.get("teach_level", -1) == 2:
        "You continue to lick at the [the_girl.title]'s clit."
        "[the_girl.title] grabs you by the hair with both hands."
        "She holds your head in place so you can lick her pussy."
        the_girl.char "That's it. Lick it."
        the_girl.char "Slow and steady."
        the_girl.char "Lick... Lick...Lick...Lick..."
        the_girl.char "Keep licking."
        "You lick at [the_girl.possessive_title]'s delicate pussy"
        "She shivers with each touch, obviously enjoying the feeling."
        if the_person.arousal > 70:
            "Her pussy is dripping wet, filling your mouth with the taste of her juices."
        $ the_girl.call_dialogue("sex_responses_oral")
    elif cousin.event_triggers_dict.get("teach_level", -1) == 3: # fingering
        if the_person.arousal > 70:
            "Her pussy is dripping wet, filling your mouth with the taste of her juices."
            the_girl.char "Put in another finger and fuck me with your fingers."
            the_girl.char "Faster! Harder! Keep licking my clit."
            $ the_girl.call_dialogue("sex_responses_oral")
        else:
            the_girl.char "Alright, I want you to fuck me with your finger."
            "You do as instructed."
            the_girl.char "Good boy. Keep doing that."
    elif cousin.event_triggers_dict.get("teach_level", -1) == 4: # rimming
        "[the_girl.possessive_title] reaches down and spreads her ass cheeks."
        the_girl.char "Now get in there and lick my asshole."
        "You do as you are told, gently licking her puckered asshole."
        the_girl.char "Mmm. Now play with my clit with your hand."
        "You reach up and play with her clit at the same time."
        the_girl.char "That's it - keep doing that for a while."
        "You do as instructed."
        the_girl.char "Alright. Now, fuck my ass with your tongue. Imagine it's a little dick - that shouldn't be too hard for you - and fuck my ass with it."
        "You do as instructed."
        the_girl.char "Mmm. Good boy."
        if the_person.has_taboo("anal_sex"):
            the_girl.char "Enjoy it while you can - it's the closest your ever going to get to fucking my ass."
        else:
            the_girl.char "Remember - don't put your dick where you wouldn't put your mouth."
    elif cousin.event_triggers_dict.get("teach_level", -1) == 5 or cousin.event_triggers_dict.get("teach_level", -1) == 6: # fingersuck
        if the_person.arousal > 70:
            "[the_girl.possessive_title]'s' pussy is dripping wet, filling your mouth with the taste of her juices."
            "She firmly licks at your fingers, with a noticeable increase in speed and pressure."
            "You copy her."
            $ the_girl.change_arousal (10)
        else:
            "[the_girl.possessive_title] gently nibbles and sucks on your fingers."
            "You copy her."
            "She moans."
    else:
        "Gone wrong - scene 1"
    $ cousin.event_triggers_dict["oral_chance"] += 5

    return

label scene_teach_oral_2(the_girl, the_location, the_object):
    if cousin.event_triggers_dict.get("teach_level", -1) == 1:
        if the_person.arousal > 70:
            the_girl.char  "Better, better, now suck my clit - suck it HARD."
            "She arches her back and entwines her fingers in your hair. Apparently, whatever you did you did it right. You keep it up and she responds by grinding her pussy into your face."
            $ the_girl.change_arousal (15)
        else:
            the_girl.char  "Better, better, now suck my clit - suck it gently."
        $ the_girl.call_dialogue("sex_responses_oral")

    elif cousin.event_triggers_dict.get("teach_level", -1) == 2:
        "[the_girl.title] grabs you by the hair with both hands."
        "She holds your head in place with one hand as she strokes your hair with the other."
        the_girl.char "That's it. Lick my clit."
        "You flick your tongue over [the_girl.possessive_title]'s clit. She gasps and grabs at your shoulders."
        $ the_girl.call_dialogue("sex_responses_oral")
        "You tease the sensitive nub with your tongue, then suck on it gently."
        "She runs her fingers through your hair and sighs, reclining on the [the_object.name]."
    elif cousin.event_triggers_dict.get("teach_level", -1) == 3: # fingering
            the_girl.char "Keep licking, palm up and stroke me gently like you're calling me over."
            "You do as instructed."
            the_girl.char "Good boy. Keep doing that."
    elif cousin.event_triggers_dict.get("teach_level", -1) == 4: # rimming
        "[the_girl.possessive_title] reaches down and spreads her ass cheeks."
        the_girl.char "Fuck my ass with your tongue."
        "You do as instructed."
        the_girl.char "Mmm. Good boy."
    elif cousin.event_triggers_dict.get("teach_level", -1) == 5 or cousin.event_triggers_dict.get("teach_level", -1) == 6: # fingersuck
        if the_person.arousal > 70:
            "[the_girl.possessive_title]'s pussy is dripping wet, filling your mouth with the taste of her juices."
            "She moans and starts sucking hard on your fingers."
            "You copy her."
            $ the_girl.change_arousal (10)
        else:
            "[the_girl.possessive_title]'s moves her mouth around licking gently."
            "You copy her."
    else:
        "Gone wrong - scene 2"
    $ cousin.event_triggers_dict["oral_chance"] += 5
    return



#$ wordchoice = renpy.random.choice(['Relax', "Don't panic", 'Stay calm', 'Chill', "It's okay"])
#$ wordchoice2 = renpy.random.choice(['the pill', 'birth control'])
#if the_person.event_triggers_dict.get("preg_knows", False):# The personality reactions but should it not be True instead of False?#
#    the_person.char "[wordchoice], [the_girl.mc_title]. I'm already pregnant remember?"



label outro_teach_oral(the_girl, the_location, the_object): #With low arousal gain this is unlikely to come up much
    "The taste of [the_girl.possessive_title]'s pussy, the sound of her moans, and the subtle twitches of her body drive you crazy."
    "You touch yourself, stroking your hard cock between your legs while you pleasure her."
    "Finally you've gone too far, pushing yourself to climax."
    "You pull your head back and grunt, jerking your cock and blasting out a load of cum onto the floor in front of [the_girl.title]."
    the_girl.char "Really? Just from giving me head? Well, I suppose I am unbearably hot for a nerd like you."
    return

label transition_default_teach_oral(the_girl, the_location, the_object):
    the_girl.char "Alright. Time for your lesson."
    "[the_girl.possessive_title] lies down on the [the_object.name] on her back. She spreads her legs wide."
    "You get down on your knees in front of [the_girl.title]."
    "You move in and start to kiss the inside of her thighs. She starts to twitch from the teasing sensations."
    return

label strip_teach_oral(the_girl, the_clothing, the_location, the_object):
    return

label strip_ask_teach_oral(the_girl, the_clothing, the_location, the_object):
    return

label orgasm_teach_oral(the_girl, the_location, the_object):
    "You notice [the_girl.possessive_title]'s moans becoming louder, and her legs twitching more noticeably on either side of you."
    the_girl.char "That's it. Keep doing that."
    if mc.sex_skills["Oral"] < 4 or the_person.sex_record.get("Cunnilingus", 0) <5:
        "You speed up your efforts, doing your best to drive her towards her orgasm."
        the_girl.char "No. No. NO. NO. Don't speed up. Slow and steady."
        "You slow down doing your best to follow the instructions."
    else:
        pass
    if cousin.event_triggers_dict.get("teach_level", -1) == 3: # fingering
        the_girl.char "That's it. That's it."
        "You keep working her pussy with your mouth and finger until she arches her back"
        the_girl.char "I'm cummmmming!"
        "You keep your lips on her clit and keep working your finger in and out of her pussy. You feel the muscles contracting as if her pussy is trying to draw your finger further inside of her."
    else:
        "She moans and begins to writhe under your tongue."
    $ the_girl.call_dialogue("climax_responses_oral")
    "All at once the tension in her body is unleashed in a series of violent tremors. Her legs wrap around your head for a moment, pulling you against her."
    "The moment passes and she relaxes. For a moment all she can do is look down at you and pant."
    $ cousin.event_triggers_dict["oral_chance"] += 10
    return
