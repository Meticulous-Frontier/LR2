init:
    python:
        SB_anal_cowgirl = Position("Anal Cowgirl",70,95,"cowgirl","Lay","Vagina","Anal",20,20,[],
        "intro_SB_anal_cowgirl",
        ["scene_SB_anal_cowgirl_1","scene_SB_anal_cowgirl_2","scene_SB_anal_cowgirl_3"],
        "outro_SB_anal_cowgirl",
        "transition_default_SB_anal_cowgirl",
        "strip_SB_anal_cowgirl", "strip_ask_SB_anal_cowgirl",
        "orgasm_SB_anal_cowgirl",
        opinion_tags = ["taking control" "anal sex"])
        list_of_girl_positions.append(SB_anal_cowgirl)

#init 1:
#    python:
#        ##Here is where you would put connections if they existed.

label intro_SB_anal_cowgirl(the_girl, the_location, the_object, the_round):
    the_girl.char "Lie down for me, I want to be on top."
    "You lie down on the [the_object.name] and undo your pants. [the_girl.possessive_title] swings a leg over your body and straddles you."
    the_girl.char "I'm gonna put it in my ass. Lets get you lubed up first though..."
    if the_girl.outfit.vagina_visible():
        "She leans back and grinds herself against you. The shaft of your cock rubs against the lips of her pussy."
    else:
        $ blocking_item = the_girl.outift.get_lower_visible()[0]
        "She leans back and grinds herself against you. Underneath her [blocking_item.name] you can feel the lips of her pussy sliding along the length of your shaft."
    "She grinds up against you for several seconds, until your cock glides pleasingly along her wet slit."
    the_girl.char "Ready?"
    if the_girl.sex_skills["Anal"] >= 3:
        "You nod. She grinds forward one last time, then lifts herself up. She reaches back behind her and guides your cock to the entrance of her puckered hole."
        "With a grunt, she slowly lets her body weight sink down on top of you. Her sphincter finally gives way with a pleasing pop, and she slowly sinks down on top of you."
    else:
        "You nod and she lifts herself up. She reaches down with one hand and holds onto your cock to hold it steady."
        "When she has you in place she lowers herself down slowly, sliding you inch by inch into her tight ass."
    if SB_check_fetish(the_girl, anal_fetish_role):
        the_girl.char "OH! Thank god. I needed this so bad."
        "[the_girl.possessive_title] settles in with the familiar feeling of your dick in her ass."
    else:
        the_girl.char "Ah..."
    "After pausing for a second to adjust [the_girl.possessive_title] starts to ride your dick."
    return

label scene_SB_anal_cowgirl_1(the_girl, the_location, the_object, the_round):
    if the_girl.arousal > 50:
        "[the_girl.possessive_title] leans back, putting her hands in line with your feet."
        "In her reclined position you have a perfect view of her drooling pussy. Just below it you can see your cock stretching her nice little asshole."
        if the_girl == mom:
            the_girl.char "Oh god [the_girl.mc_title], you make [the_girl.title] feel so good... You grew up into such good man!"
            mc.name "Mmm, [the_girl.title] your ass is amazing. Its so tight!"
        else:
            the_girl.char "Does that feel good? It feels even bigger when its in my ass like this."
            mc.name "Mmm, [the_girl.title] your ass is amazing. Its so tight!"

    else:
        "[the_girl.possessive_title] leans back, putting her hands in line with your feet, and slows down her rhythm."
        the_girl.char "I need to take it a little slow. I need to get warmed up before I can really take it hard when it's in my ass."
        "You have a perfect view of her pussy. It is just starting to show some early signs of arousal. Just below it you can see your cock stretching her nice little asshole."
        mc.name "Take all the time you need. Your ass is so tight, even completely still it feels amazing."
    "[the_girl.possessive_title] rocks her hips back and forth. Each movement feels like her tight back passage is milking you, begging for you to cum in it."
    return

label scene_SB_anal_cowgirl_2(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title] speeds up, working her thighs to pump herself up and down your cock."
    "Her ass makes a few lewd squelching noises from her aggressive fucking. Her buttery smooth puckered hole strokes your erection with every pump."
    if the_girl.has_large_tits():
        if the_girl.outfit.tits_visible():
            "Her large, unconstrained tits bounce up and down with each stroke."
            the_girl.char "Fuck, hold onto these!"
            "[the_girl.possessive_title] reaches down and grabs your hands. She brings them up to her tits and plants them there."
            "She moans and grinds your hands into her breasts, then puts her hands on your chest and focuses on fucking you."
        else:
            $ the_clothing = the_girl.outfit.get_upper_visible()[0]
            "Her large tits are barely contained by her [the_clothing.name]. You watch them bounce around as she fucks you vigorously."
            menu:
                "Pull her [the_clothing.name] off.":
                    "You reach up and start to pull at her [the_clothing.name]. She stops fucking you for a moment as she moves her arms to give you better access."
                    mc.name "I want a better look at your tits while you fuck me."
                    $ the_girl.draw_animated_removal(the_clothing, position = SB_anal_cowgirl.position_tag) #Hopefully this copy paste works.
                    "Now free of her [the_clothing.name], [the_girl.possessive_title] resumes fucking you."
                    return
                "Play with her pussy.":
                    "You quickly stick your thumb in your mouth to get it wet, then reach down and start to rub her clit with your thumb as she rides you."
                    if the_girl.get_opinion_score("being fingered"):
                        "[the_girl.possessive_title] moans as you start to play with her."
                        the_girl.char "Oh! That feels good. Makes it easier to handle buttsex when you touch me like that."
                        $ the_girl.change_arousal(5)
                    else:
                        the_girl.char "That feels good... Keep going that makes this easier."
                    "You push a finger up inside her while you continue to use your thumb to rub her love button. As she bounces up and down on your cock you can feel your cock deep inside her ass through the thin vaginal wall."
                    "You stroke yourself a bit through her vagina while she fucks you. It's a very unique feeling, and very pleasurable!"
                    return


    else:
        if the_girl.outfit.tits_visible():
            "She reaches up and grabs onto one of her own small tits, squeezing it while she rides you."
            the_girl.char "Ah!"
            "You decide to get in on the action. You reach up and grab her other breast."
            "She moans as you rub and tweak her breasts. She puts her hands on your chest and focuses on fucking you."
        else:
            $ the_clothing = the_girl.outfit.get_upper_visible()[0]
            "She reaches up and grabs onto one of her small tits through her [the_clothing.name]. She kneeds it through the fabric and moans loudly while she rides you."
            the_girl.char "Ah!"
            menu:
                "Pull her [the_clothing.name] off.":
                    "You reach up and start to pull at her [the_clothing.name]. She stops fucking you for a moment as she moves her arms to give you better access."
                    mc.name "I want a better look at your tits while you fuck me."
                    $ the_girl.draw_animated_removal(the_clothing, position = SB_anal_cowgirl.position_tag) #Hopefully this copy paste works.
                    "Now free of her [the_clothing.name], [the_girl.possessive_title] resumes fucking you."
                    return
                "Play with her pussy.":
                    "You quickly stick your thumb in your mouth to get it wet, then reach down and start to rub her clit with your thumb as she rides you."
                    if the_girl.get_opinion_score("being fingered"):
                        "[the_girl.possessive_title] moans as you start to play with her."
                        the_girl.char "Oh! That feels good. Makes it easier to handle buttsex when you touch me like that."
                        $ the_girl.change_arousal(5)
                    else:
                        the_girl.char "That feels good... Keep going that makes this easier."
                    "You push a finger up inside her while you continue to use your thumb to rub her love button. As she bounces up and down on your cock you can feel your cock deep inside her ass through the thin vaginal wall."
                    "You stroke yourself a bit through her vagina while she fucks you. It's a very unique feeling, and very pleasurable!"
                    return
    "You give her nipple a pinch. You roll it between your finger and thumb."
    if the_girl == mom:
        the_girl.char "[the_girl.mc_title]! [the_girl.title] loves it when you play with her nipples."
    else:
        the_girl.char "Mmm, I love it when you play with my tits!"
    if the_girl.has_large_tits:
        "You give her epic tits another squeeze. They are so full and soft and feel heavy in your hands."
    else:
        "You give her modest tits another squeeze. They are supple yet firm in your hands."
    return

label scene_SB_anal_cowgirl_3(the_girl, the_location, the_object, the_round):
    "You put your hands on [the_girl.possessive_title]'s hips and guide her up and down at a steady pace."
    if the_girl.arousal > 75:
        "Your cock glides in and out of her tight, supple ass. [the_girl.possessive_title] is so excited her pussy is dripping her juices onto you."
    else:
        "Her ass is warm and tight. You glide in and out of her at her pace."
    if SB_check_fetish(the_girl, anal_fetish_role):
        "[the_girl.possessive_title] leans forward. She runs one hand through your hair and the other she puts on your chest."
        the_girl.char "Mmmm, your cock feels so good [the_girl.mc_title]. I crave it, stuffing my tight little asshole constantly." #NOTE: mc_title can be the_girl.mc_title
        "[the_girl.possessive_title] stops rocking her hips for a few minutes. Pausing just to enjoy the exquisite fullness your erection gives her."
    else:
        "With [the_girl.possessive_title] in control you're able to relax and focus entirely on enjoying the feeling."
    return

label outro_SB_anal_cowgirl(the_girl, the_location, the_object, the_round):
    "With each stroke of her hips [the_girl.possessive_title]'s impossibly tight ass brings you closer and closer to cumming. You're finally driven past the point of no return."
    mc.name "Fuck, I'm going to cum!"

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    $ threshold = 120 + (-20 * the_girl.get_opinion_score("creampies")) + (-20 * the_girl.get_opinion_score("anal sex"))
    if the_girl.sluttiness > threshold:
        #She drops down on you as you cum.
        the_girl.char "Yes! Ah!"
        "[the_girl.possessive_title] drops herself down, grinding her hips against yours and pushing your cock as deep into her ass as possible."
        "Her breath catches in her throat when you pulse out your hot load of cum deep inside of her."
        if the_girl.char == mom:
            the_girl.char "That's it baby! Give your cum to [the_girl.title]!"
        else:
            the_girl.char "Oh my god... Give it all to me [the_girl.mc_title]... Fill my ass up!"
        $ cum_in_ass(the_girl)
        $ SB_anal_cowgirl.redraw_scene(the_girl)
        the_girl.char "Oh yes... so full..."
        "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
        "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
        "She rolls off and lies next to you on the [the_object.name]."
    elif the_girl.sluttiness < 70:
        #She always pull off and you cum on her stomach.
        the_girl.char "Oh shit, don't cum in my ass!"
        "[the_girl.possessive_title] jerks up, pulls off your cock, and lowers herself back down."
        "She leans back and uses one hand to push your shaft against the lips of her pussy, grinding against it until you climax."
        the_girl.char "Cum for me [the_girl.mc_title], I want you to cum on me!"
        "You tense up and cum, shooting your thick load up and onto [the_girl.possessive_title]'s stomach. She keeps grinding against your cock until you are completely spent."
        $ the_girl.cum_on_stomach()
        $ SB_anal_cowgirl.redraw_scene(the_girl)

    else:
        #She hesitates and you can decide to pull her down or not.
        "[the_girl.possessive_title] starts to pull up and off of you. She hesistates with the tip of your cock just inside of her ass."
        the_girl.char "I... I really shouldn't let you..."
        "She bites her lip and moans, unsure of what to do."
        menu:
            "Pull her down and cum inside her.":
                "You reach up and grab [the_girl.possessive_title] by the hips. With one confident pull she plunges back onto your cock, gasping with pleasure."
                "The feeling of her tight, warm ass sliding down and engulfing your cock again pushes you over the edge. You pull [the_girl.possessive_title] tight against you and unload inside of her."
                the_girl.char "Ah! Fuck..."
                $ the_girl.change_obedience(3)
                $ cum_in_ass(the_girl)
                $ SB_anal_cowgirl.redraw_scene(the_girl)
                "You give a few half-hearted pumps when you're done, then tap [the_girl.possessive_title] on the ass. She slides off of your dick and collapses beside you."

            "Let her pull off and cum on her stomach.":
                "You stay silent. [the_girl.possessive_title] waits another second, as if waiting to be convinced, then pulls off of your cock."
                "She grinds the lips of her pussy against your shaft as you climax. You fire your hot load over her stomach."
                $ the_girl.cum_on_stomach()
                $ SB_anal_cowgirl.redraw_scene(the_girl)
                the_girl.char "Whew, that was close..."
                "She rolls off and lies next to you on the [the_object.name]."
    return

label transition_default_SB_anal_cowgirl(the_girl, the_location, the_object, the_round):
    "You lie down on [the_object.name]. [the_girl.possessive_title] swings a leg over your waist and straddles you."
    if the_girl.sex_skills["Anal"] >= 3:
        "You nod. She grinds forward one last time, then lifts herself up. She reaches back behind her and guides your cock to the entrance of her puckered hole."
        "With a grunt, she slowly lets her body weight sink down on top of you. Her sphincter finally gives way with a pleasing pop, and she slow sinks down on top of you."
    else:
        "You nod and she lifts herself up. She reaches down with one hand and holds onto your cock to hold it steady."
        "When she has you in place she lowers herself down slowly, sliding you inch by inch into her tight ass."
    the_girl.char "Ah..."
    "After pausing for a second to adjust [the_girl.possessive_title] starts to ride your dick."
    return

label strip_SB_anal_cowgirl(the_girl, the_clothing, the_location, the_object, the_round):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = SB_anal_cowgirl.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
    return

label strip_ask_SB_anal_cowgirl(the_girl, the_clothing, the_location, the_object, the_round):
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_anal_cowgirl.position_tag)
            "[the_girl.possessive_title] slows down her pace while she strips out of her [the_clothing.name]. When she's free of it she puts her hands on your chest and fucks you faster again."

        "Leave it on.":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 70:
                the_girl.char "Yeah? Do I look sexy in it?"
                "She sighs happily while she rides you."
            else:
                the_girl.char "Yeah? Do I look like a good little slut in it? Because that's what I feel like right now!"
                "She sighs happily while she rides your cock hard and fast."
    return

label orgasm_SB_anal_cowgirl(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title] works her hips faster and her breathing grows heavier."
    $ the_girl.call_dialogue("climax_responses")
    the_girl.char "With one last gasp she collapses down against you. Her thighs quiver as she climaxes. Her velvet smooth ass quivers around your erection as she cums."
    "After a second [the_girl.possessive_title] regains control of herself. Her breath is warm against your ear as she whispers to you."
    if SB_check_fetish(the_girl, anal_fetish_role):
        the_girl.char "Everytime you're in my ass, it's like I just can't stop cumming..."
    else:
        the_girl.char "I can't stop now, I want you to make me cum again!"
    "She leans back and starts to ride you faster than ever."
    return
