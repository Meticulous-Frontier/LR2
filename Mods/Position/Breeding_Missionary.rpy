#A special variant of missionary, specifically for breeding. Leaves MC with no choice but to cum inside. Girl encourages through the encounter for him to fill her up.
init:
    python:
        breeding_missionary = Position(name = "Breeding Missionary", slut_requirement = 50, slut_cap = 100, requires_hard = True, requires_large_tits = False,
            position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
            girl_arousal = 16, girl_energy = 8,
            guy_arousal = 15, guy_energy = 10,
            connections = [],
            intro = "intro_breeding_missionary",
            scenes = ["scene_breeding_missionary_1","scene_breeding_missionary_2"],
            outro = "outro_breeding_missionary",
            transition_default = "transition_default_breeding_missionary",
            strip_description = "strip_breeding_missionary", strip_ask_description = "strip_ask_breeding_missionary",
            orgasm_description = "orgasm_breeding_missionary",
            taboo_break_description = "taboo_break_breeding_missionary",
            opinion_tags = ["missionary style sex","vaginal sex"], record_class = "Vaginal Sex",
            default_animation = missionary_bob,
            associated_taboo = "vaginal_sex")
        #list_of_positions.append(breeding_missionary) #For testing


label intro_breeding_missionary(the_girl, the_location, the_object):
    "You run your hands along [the_girl.title]'s hips, feeling the shape of her body."
    #TODO next line only if the girl is already pregnant. change this statement after 29.1 to match the pregnancy condition
    if the_girl.knows_pregnant():
        mc.name "I want to practice putting another baby inside you. Let's pretend like we are trying to make another one."
        the_person.char "Mmm, sounds nice. Okay I'm up for a little roleplaying."
    else:
        mc.name "Lie down now. It's time for me to put a baby inside you."
    "She nods meekly and lies down on the [the_object.name], waiting while you climb on top of her."
    if mc.condom:
        the_person.char "Why are you wearing that thing? Let's get that off of you."
        "She reaches down and pulls off your condom."
        the_person.char "You aren't getting anyone pregnant wearing that silly thing!"
        $ mc.condom = False
    "[the_girl.possessive_title] wraps her arms around you and holds you close as you line your cock up with her pussy. She sighs happily into your ear as you slide into her."
    "When you are deep inside her, you feel her legs lightly wrap around your back, holding you in place for a second."
    the_person.char "Make sure you are this deep when you cum, ok [the_person.mc_title]?"
    return

label taboo_break_breeding_missionary(the_girl, the_location, the_object):
    "You run your hands along [the_girl.title]'s hips, feeling the shape of her body."
    mc.name "Lie down now. It's time for me to put a baby inside you."
    the_person.char "Oh god... are we really doing this? I mean... we've never even had sex before."
    mc.name "Don't worry, we'll have the next 9 months, while your belly swell and your tits get big with milk, to make up for lost time and fuck each other's brains out before the baby gets here."
    $ the_person.change_arousal(10)
    the_person.char "Oh fuck that sounds amazing. You better "
    "She nods meekly and lies down on the [the_object.name], waiting while you climb on top of her."
    if mc.condom:
        the_person.char "Why are you wearing that thing? Let's get that off of you."
        "She reaches down and pulls off your condom."
        the_person.char "You aren't getting anyone pregnant wearing that silly thing!"
        $ mc.condom = False
    "[the_girl.possessive_title] wraps her arms around you and holds you close as you line your cock up with her pussy. She sighs happily into your ear as you slide into her."
    "When you are deep inside her, you feel her legs lightly wrap around your back, holding you in place for a second."
    the_person.char "Make sure you are this deep when you cum, ok [the_person.mc_title]?"
    return

label scene_breeding_missionary_1(the_girl, the_location, the_object):
    # CHOICE CONCEPT: talk dirty to her, Tease her nipples.
    # Intro concept. Short difference depending on if she's wet or not.
    if the_girl.arousal > 50:
        "[the_girl.title]'s pussy is nice and wet as you pump your hips and fuck her."
    else:
        "[the_girl.title]'s pussy is still getting wet. You take it slow, giving her time to warm up."

    menu:
        "Play with her tits.":
            if not the_girl.tits_available():
                "You decide you want some quality time with her tits."
                mc.name "Lean forward, I need to get this off you."
                if the_girl.obedience > 120:
                    the_person.char "Yes sir."
                else:
                    the_person.char "Mmm, you wanna play with my tits? Okay."
                "She leans forward and you quickly strip her top off."
                $ the_person.strip_outfit(top_layer_first = True, exclude_lower = True)
            "You lean down and start to kiss at [the_girl.possessive_title]'s tits. She arches her back, presenting them to your lips."
            if the_girl.get_opinion_score("kissing") > 0:
                $ the_girl.discover_opinion("kissing")
                $ the_girl.change_arousal(the_girl.get_opinion_score("kissing"))
            the_girl.char "[the_girl.mc_title]... Oh [the_girl.mc_title] that feels so good."
            "She moans and runs her hands through your hair as you suckle her tits."
            mc.name "Mmm, I can't wait until I knock you up and your milk comes in. I'm going to suck them dry every chance I get!"
            if the_girl.relationship == "Single":
                the_girl.char "Mmm, that's for the baby! But if I have any extra I guess I wouldn't mind if you had some too..."
            else:
                $ so_title = SO_relationship_to_title(the_girl.relationship)
                the_girl.char "That's for the baby! and for my [so_title]!"
                $ del so_title
                mc.name "Yeah, but I'm putting the baby in you. Not him."
                $ the_girl.change_arousal(the_girl.get_opinion_score("cheating on men") * 3)
                the_girl.char "Oh god... yes... yes your are!"

        "Talk dirty to her.":
            mc.name "You feel amazing [the_girl.title]. I'm going to fuck you like this every day and fill you with my seed over and over."
            mc.name "I'm going to knock you up, but I'm not going to stop. I'm going to fuck you over and over, and fill you up over and over, even as your belly gets big."
            the_girl.char "Oh god, I want that so bad! I want to feel your cum inside me again and again..."
            if the_girl.has_large_tits():
                mc.name "Your massive udders are going to get even bigger. When I fuck you milk is going to spray out every time you cum."
            else:
                mc.name "Your tits are going to grow, filling with milk. When I fuck you it's going to spray out every time you cum."
            if the_girl.love > 60:
                the_girl.char "Yes! Make me a mommy! I want to think about you every time I feel it kick and move in my belly."
            else:
                the_girl.char "Careful about making promises! I'm going to hold you to that!"

    "[the_girl.possessive_title] wraps her legs around you and you resume fucking her, pushing yourself as deep as you can with every thrust."

    return

label scene_breeding_missionary_2(the_girl, the_location, the_object):
    "You grab [the_girl.title]'s hands and lift them above her head. You push them against the [the_object.name] and pin [the_girl.title] underneath you."
    the_girl.char "Ah! You've got me held down and there's nothing I can do..."
    mc.name "That's right [the_girl.title]. Your womb is mine for the taking."
    if the_girl.get_opinion_score("being submissive") > 0:
        the_girl.char "Even if I wanted to back out, I couldn't."
        mc.name "We both know you don't want to back out..."
        the_girl.char "... I know..."
        "You stop fucking her for a second. She looks up at you puzzled."
        mc.name "What do you want me to do to you?"
        the_girl.char "You know. You know what I want..."
        "She whimpers. You bark back at her."
        mc.name "No. I don't. You need to tell. What is it that you want?"
        "She squirms below you, her arms pinned behind her. She lets out a whisper."
        the_girl.char "I want you to cum inside me..."
        mc.name "What was that? I thought I knew what you wanted, but now I'm not sure. Maybe I should stop?"
        "You start to pull yourself out of her."
        the_girl.char "No! Don't stop!"
        mc.name "Then what do you want?"
        the_girl.char "I want you to fill me up! I want you to cum so deep not a drop of it escapes. Knock me up! Breed me like an animal!"
        $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
        $ the_girl.discover_opinion("being submissive")
        "You resume fucking her hard and fast. [the_girl.possessive_title] gasps and moans, her hips bucking with pleasure."
        "She tests your grip on her hands and shivers with pleasure when you force them back down and keep her in place."
        the_girl.char "I'm just a fuck toy to you right now... Just a soft wet hole for you to fuck with that big cock... Ah!"
        "[the_girl.title]'s pussy feels great to fuck, but you can't keep this pace up forever. You let go of her hands and slow down."
        "You're both silent for a few seconds, panting for breath."
        the_girl.char "Don't stop..."

    else:
        the_girl.char "Oh! Hello there..."
        mc.name "Spread your legs for me, I want to get nice and deep."
        "She does what you want and spreads her legs. You start to fuck her hard and fast."
        the_girl.char "Fuck me... Oh fuck me harder! Get it in deep!"
        "She pants and moans underneath you. You keep the pace up as long as you can manage, fucking [the_girl.title]'s tight, wet cunt while she's pinned underneath you."
        "You keep up the pace as long as you can manage, but eventually you have to slow down and catch your breath."
        the_girl.char "That was... that felt great, it was so intense."
        "She licks at your ear, then whispers into it."
        the_girl.char "Make sure you get it that deep when you finish..."
    return

label outro_breeding_missionary(the_girl, the_location, the_object):
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her pussy it's not long before you're pushed past the point of no return."
    mc.name "Here it comes bitch! I'm going to cum now!"
    "[the_girl.possessive_title] wraps her legs around your waist. Even if you wanted to pull out, you couldn't, as she uses her legs to pull you into her."
    "You use your full weight to push your cock deep inside of [the_girl.possessive_title]'s cunt as you climax. She gasps and claws at your back as you pump your seed into her."
    $ the_girl.call_dialogue("cum_vagina")
    $ the_girl.cum_in_vagina()
    $ breeding_missionary.redraw_scene(the_girl)
    "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."
    "She lifts her legs up a bit, tilting her vagina so that your cum will naturally slide deeper inside. She sighs happily."


    return


label transition_default_breeding_missionary(the_girl, the_location, the_object):
    "You run your hands along [the_girl.title]'s hips, feeling the shape of her body."
    #TODO next line only if the girl is already pregnant. change this statement after 29.1 to match the pregnancy condition
    if False:
        mc.name "I want to practice putting another baby inside you. Let's pretend like we are trying to make another one."
        the_person.char "Mmm, sounds nice. Okay I'm up for a little roleplaying."
    else:
        mc.name "Lie down now. It's time for me to put a baby inside you."
    "She nods meekly and lies down on the [the_object.name], waiting while you climb on top of her."
    if mc.condom:
        the_person.char "Why are you wearing that thing? Let's get that off of you."
        "She reaches down and pulls off your condom."
        the_person.char "You aren't getting anyone pregnant wearing that silly thing!"
        $ mc.condom = False
    "[the_girl.possessive_title] wraps her arms around you and holds you close as you line your cock up with her pussy. She sighs happily into your ear as you slide into her."
    "When you are deep inside her, you feel her legs lightly wrap around your back, holding you in place for a second."
    the_person.char "Make sure you are this deep when you cum, ok [the_person.mc_title]?"
    return

label strip_breeding_missionary(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = breeding_missionary.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She sighs happily when you slip back inside of her."
    return

label strip_ask_breeding_missionary(the_girl, the_clothing, the_location, the_object):
    the_girl.char "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.title] pants as you fuck her."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = breeding_missionary.position_tag)
            "You move back kneel for a moment while [the_girl.title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She sighs happily when you get on top of her and slide your cock back inside."

        "Leave it on.":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl.char "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 100:
                the_girl.char "Does it make me look like a good little milf? All I want to be is your breeding stock sir."
                "She pushes her hips against yours and moans happily."
            else:
                the_girl.char "Does it make me look like the cum hungry slut that I am? That's all I want to be for you sir, your dirty little cum dumpster!"
                "She grinds her hips against you and moans ecstatically."
    return

label orgasm_breeding_missionary(the_girl, the_location, the_object):
    "[the_girl.title] turns her head and pants loudly. Suddenly she bucks her hips up against yours and gasps."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "Her pussy is dripping wet as you fuck through her climax. She paws at the [the_object.name], trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down your thrusts to catch your own breath."
    the_girl.char "Don't stop for me[the_girl.mc_title]! I still need your cum inside me."
    return
