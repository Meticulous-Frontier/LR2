init:
    python:
        SB_reverse_cowgirl = Position("Reverse Cowgirl",60,100,"doggy","Lay","Vagina","Vaginal",22,18,[],
        "intro_SB_reverse_cowgirl",
        ["scene_SB_reverse_cowgirl_1","scene_SB_reverse_cowgirl_2"],
        "outro_SB_reverse_cowgirl",
        "transition_default_SB_reverse_cowgirl",
        "strip_SB_reverse_cowgirl", "strip_ask_SB_reverse_cowgirl",
        "orgasm_SB_reverse_cowgirl",
        opinion_tags = ["taking control","vaginal sex"])
        list_of_girl_positions.append(SB_reverse_cowgirl)
        #list_of_positions.append(SB_reverse_cowgirl)   ###20,120 for testing purprose only###

init 1:
    python:
        missionary.link_positions(SB_reverse_cowgirl,"transition_missionary_SB_reverse_cowgirl")
        SB_reverse_cowgirl.link_positions(doggy,"transition_SB_reverse_cowgirl_doggy")

#init 1:
#    python:
#        #Here is where you would put connections if they existed.

label intro_SB_reverse_cowgirl(the_person, the_location, the_object, the_round):
    mc.name "[the_person.title], why don't you ride me for a bit?"
    "You lay down on the [the_object.name], and [the_person.title] gets on top, facing away from you."
    "She reaches between her legs and wraps her hand around your cock. She slowly guides it into her slit and then slides the length of it inside her."
    return

label scene_SB_reverse_cowgirl_1(the_person, the_location, the_object, the_round):
    # CHOICE CONCEPT: She fucks you, skill based lists#
    "You lay back on the [the_object.name] while [the_person.title] works your cock in and out of her."
    if the_person.arousal > 80:
        "You can clearly see her arousal everytime she bounces up and down on top of you, her juices are beginning to run down the inside of her thighs."
    else:
        "You watch in rapture as her tight pussy lips grip your shaft with every bounce."
    if SB_get_fetish(the_person) == "Vaginal Fetish":   #Fetish serum, highly skilled and loves sex
        the_person.char "Oh [the_person.mc_title], I love how full I feel when you fuck me... god I wish we could do this everyday!"
        "[the_person.title] gives you a few quick, shallow dips then pull off you almost completely, leaving just your tip inside her."
        "She swirls her hips a couple times then impales herself on your again. [the_person.title] works her hips relentlessly on top of you as she pleases herself on your erection."
        "After constant exposure to the serums you've designed, it is clear by the way she fucks you with wild abandon that you've turned her into your slut."
        "She give you a few more vigorous thrusts, then sheathes you entirely as deep as she can get you."
        "[the_person.title] stops moving her hips for a few seconds, but you can feel her contracting and relaxing the muscles around her pelvis, her cunt milking you without even having to move her hips."
        mc.name "Oh my god [the_person.title], that feels amazing..."
        if the_person.arousal > 130:
            "[the_person.title] looks back at you with passion in her eyes while the contractions of her pussy around you suddenly strengthen. Her eyes start to glaze as she orgasms again."
            the_person.char "[the_person.mc_title]! I'm cumming again! Cum for me... I need you to cum for me now!!!"
            "Her pleading and the intense pleasure her cunt is giving you is pushing you to orgasm soon."
            $ mc.change_arousal(50)
            return
        "Her sexual expertise is incredibly pleasing for both of you."
        $ the_person.change_arousal(10)
        $ mc.change_arousal(7)
    elif the_person.sex_skills["Vaginal"] > 2: #She has some skill
        "[the_person.title] slows her pace for a bit, working your erection with her body with purpose."
        "She makes a couple shallow dips, then then sheathes you entirely."

    else:
        "[the_person.title] works her hips up and down on you as best as she can."
        "She makes a couple shallow dips, then then sheathes you entirely."




    return

label scene_SB_reverse_cowgirl_2(the_person, the_location, the_object, the_round):
    # CHOICE CONCEPT: She bottoms out and grinds on you for a bit. Spank or finger her
    "[the_person.title] bounces up and down a few times on your cock, then and you holds you deep inside her."
    "Instead of bouncing up and down, she starts to grind herself back and forth."
    the_person.char "Mmmm, [the_person.mc_title], its so big... I feel so full!"
    "[the_person.title]'s shapely ass looks amazing on display in front of you. You grasp one of her pliant cheeks in your hand as she grinds."
    menu:
        "Spank it":
            "You bring your hand off [the_person.title]'s ass and give it a firm slap"
            the_person.char "Oh!"
            "You enjoy the way her tight ass jiggles and spank it again."
            if the_person.get_opinion_score("showing her ass") > 0:
                $ the_person.discover_opinion("showing her ass")
                the_person.char "You're gonna leave a mark, [the_person.mc_title]! Then everyone who sees it will know what a slut I am!"
                "She wiggles her hips back and forth, giving you an enticing moving target. You give her irresistable ass another spank."
                $ the_person.change_arousal(the_person.get_opinion_score("showing her ass") * 5)
                "[the_person.title] moans as you give her a few more swats. A bright red handprint is beginning to form on her cheeks."
            elif SB_get_fetish(the_person) == "Vaginal Fetish":
                "You give her irresistable ass another spank. [the_person.title] times her thrust with your hand smacking her booty, swallowing your dick whole with her greedy cunt when you spank her."
                the_person.char "Mmmm. I've been bad [the_person.mc_title], I can't get your dick off my mind!"
                "You spank her again. She bottoms out on top of you in time with your smack again. She greatly enjoys the sensation of getting filled up and spanked at the same time."
                $ the_person.change_arousal(5)
            else:
                the_person.char "Do you like that, [the_person.mc_title]? Ah!"
                "[the_person.title] is enjoying herself. You give her accommodating ass another squeeze and then spank it again."
                "You can feel [the_person.title]'s pussy quivering as she grinds herself back into you."
                $ the_person.change_arousal(5)
            "You leave a hand planted on [the_person.title]'s butt while she fucks you, squeezing it and giving it the occasional slap."

        "Admire her":
            mc.name "Damn [the_person.title],  your ass is amazing!"
            "[the_person.title] wiggles back and forth a few more times, then looks back at you and smiles."
            if the_person.get_opinion_score("taking control") > 0:
                the_person.char "Do you like that, [the_person.mc_title]? Just lay back and let me take care of you..."
                "You run your hands along your hips while she grinds back against you. Her cunt feels amazing wrapped around you."
                if the_person.arousal > 130:
                    the_person.char "Ohh god, I'm gonna cum again! Fuck you should cum too... are you gonna cum soon?"
                    "[the_person.title]'s pussy spasms again in orgasm. The combination of her orgasm and the view of her ass is incredibly arousing."
                    $ mc.change_arousal(10)
                    $ the_person.change_happiness(2)
                else:
                    $ the_person.change_arousal(5)
                    the_person.char "Ohh, you make me so wet. I want to make you feel good too... Do you wanna cum soon?"
                if the_person.get_opinion_score("creampies") > 0:
                    "[the_person.title] reaches back between her legs and cups your balls."
                    the_person.char "Mmm you feel so full... I want you to fill me up! I can't wait to milk all that cum out of you!"
                else:
                    "[the_person.title] grabs your ankles to steady herself."
                    the_person.char "You should... I love it when you cum. I want to make you cum!"
            else:
                the_person.char "I'm glad you like it, [the_person.mc_title]. I love it when you fuck me, but sometimes it feels good to be on top once a while too..."
                if the_person.get_opinion_score("masturbating") > 0:
                    "[the_person.title] reaches down with one hand and begins to rub her clit as she grinds back against you."
                    $ the_person.discover_opinion("masturbating")
                    $ the_person.change_arousal(the_person.get_opinion_score("masturbating" * 5))
                "You grab [the_person.title]'s ass cheeks with both hands. Her smooth skin feels supple in your hands." ###TODO
            "After some time spent grinding, [the_person.title] resumes her bouncing motion on top of you."

    return

label outro_SB_reverse_cowgirl(the_person, the_location, the_object, the_round):
    "[the_person.title]'s sweet cunt milks your cock, the wet friction pushes you past the point of no return."
    mc.name "Ah, I'm going to cum!"
    "[the_person.title] looks back at you and smiles."
    if SB_get_fetish(the_person) == "Internal Cum Fetish":
        "[the_person.title]'s body goes rigid as your cum poors into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
        the_person.char "Oh.. OH! Yes [the_person.mc_title]! Pump it deep! I want it it all inside me!"
        "[the_person.title] revels in having her cum fetish fulfilled."
        $ the_person.cum_in_vagina()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "When you finish, [the_person.title] slowly pulls up off you."
        "You gaze at her shapely ass as a few drips of your seed drip out her pussy and onto [the_object.name]"
    elif SB_get_fetish(the_person) == "External Cum Fetish":
        "[the_person.title] lifts her hips up off of you, your twitching cock suddenly cold and aching to be back inside her."
        "She reaches down between her legs and begins to pump your member with your hand."
        the_person.char "Oh its so good when you spray me with your seed... Do it! Cum all over me!"
        "You don't have time to respond before the first wave of cum erupts from your penis."
        $ the_person.cum_on_ass()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "[the_person.title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
        "[the_person.title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
        the_person.char "Thank you [the_person.mc_title]. Oh my good its so good..."
        "You lay back and take a few moments to enjoy the view. [the_person.title] is massaging your cum into her ass cheeks with both hands."
    elif the_person.get_opinion_score("creampies") > 0:
        the_person.char "Oh god, I can't wait to feel you shoot it up inside me... Cum for me [the_person.mc_title]!"
        "[the_person.title]'s quivering hole feels too good, you can't hold it back anymore."
        "She moans as the first wave of your cum floods her pussy. She rocks her hips back and forth on top of you as you dump your load inside her."
        $ the_person.cum_in_vagina()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "When you finish, [the_person.title] slowly pulls up off you."
        "You gaze at her shapely ass as a few drips of your seed drip out her pussy and onto [the_object.name]"
    elif the_person.get_opinion_score("risking getting pregnant") > 0:
        the_person.char "That's it, shoot your seed in deep! I want to feel you flood my womb!"
        "She stops her up and down movements and pushes herself down onto you, forcing you up inside her as deep a she can."
        "[the_person.title] moans as the first wave of your cum floods her pussy. She holds herself still just as you dump your load deep inside her."
        $ the_person.cum_in_vagina()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "You reach your hands forward and grab her hips, and push yourself up slightly, holding her hips in place."
        the_person.char "Yes! Cum deep! I don't want a single drop to go to waste!"
        "When you finish, [the_person.title] stays still for a few minuntes, keeping you deep inside her."
        "She reaches down between her legs, and then slowly pulls off of you, trying to use her hand to keep any of your seed from spilling out."
    elif the_person.get_opinion_score("being covered in cum") > 0:
        "[the_person.title] lifts her hips up off of you, your twitching cock suddenly cold and aching to be back inside her."
        "She reaches down between her legs and begins to pump your member with your hand."
        the_person.char "Oh my god its so warm. I want to feel you shoot your load all over my ass!"
        "You don't have time to respond before the first wave of cum erupts from your penis."
        $ the_person.cum_on_ass()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "When the last of your cum splashes onto her ass, she stops stroking you."
        the_person.char "Thank you [the_person.mc_title], I love the feeling of your cum on my skin..."
        "You lay back and take a few moments to enjoy the view."
    elif the_person.get_opinion_score("showing her ass") > 0:
        "[the_person.title] lifts her hips up off of you, your twitching cock suddenly cold and aching to be back inside her."
        "She reaches down between her legs and begins to pump your member with your hand."
        the_person.char "I want to feel you shoot your load all over my ass! Its going to feel so hot knowing I've got your load all over my ass..."
        "You don't have time to respond before the first wave of cum erupts from your penis."
        $ the_person.cum_on_ass()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "When the last of your cum splashes onto her ass, she stops stroking you."
        the_person.char "Thank you [the_person.mc_title]. Do I look good? With your sticky seed painted all over my backside?"
        "[the_person.title] shakes her hips side to side for you, showing off her prize. In a couple places your cum starts drip down from her shapely ass."
        "You lay back and take a few moments to enjoy the view."
    elif the_person.sex_skills["Vaginal"] > 5:
        the_person.char "Oh god, it feels to good to pull off now... just shoot it up inside me!"
        if the_person.arousal > 130:
            "[the_person.title] is riding you with wild abandon, as yet another orgasm wracks her body. Too late to stop, you begin cumming at the same time."
        elif the_person.arousal > 100:
            "[the_person.title] is riding you with wild abandon, and an orgasm wracks her body. Too late to stop, you begin cumming at the same time."
        $ the_person.cum_in_vagina()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "[the_person.title]'s expert cunt draws wave after wave of cum from you. For a second you lose the ability to process anything outside the feeling of her velvet pussy wrapped perfectly around your shaft."
        the_person.char "Oh [the_person.mc_title]... I needed that so bad... Let's do that again soon okay?"
    elif the_person.sluttiness < 80:
        "[the_person.title] lifts her hips up off of you, your twitching cock suddenly cold and aching to be back inside her."
        "She reaches down between her legs and begins to pump your member with your hand."
        "You don't have time to respond before the first wave of cum erupts from your penis."
        $ the_person.cum_on_ass()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "When the last of your cum splashes onto her ass, she stops stroking you."
        "You lay back and take a few moments to enjoy the view."
    else:
        the_person.char "It feels to good to pull off now... just shoot it up inside me!"
        if the_person.arousal > 100:
            "[the_person.title] is riding you with wild abandon, and an orgasm wracks her body. Too late to stop, you begin cumming at the same time."
        $ the_person.cum_in_vagina()
        $ SB_reverse_cowgirl.redraw_scene(the_person)
        "You shoot your load up into [the_person.title]. She moans in appreciation as she feels you filling her up."
        "[the_person.title] pulls off you slowly, and you see a few drips of your seed escaping before she gets up."

    return

label transition_default_SB_reverse_cowgirl(the_person, the_location, the_object, the_round):
    "You lay down on the [the_object.name], and [the_person.title] gets on top, facing away from you."
    "She reaches between her legs and wraps her hand around your cock. She slowly guides it into her slit and then slides the length of it inside her."
    return

label strip_SB_reverse_cowgirl(the_person, the_clothing, the_location, the_object, the_round):
    "[the_person.title] straightens up a bit and peaks back at you."
    $ the_person.call_dialogue("sex_strip")
    $ the_person.draw_animated_removal(the_clothing, position = SB_reverse_cowgirl.position_tag)
    "[the_person.title] struggles out of her [the_clothing.name] and throws it to the side."
    "She resumes working her hips up and down on top of you with a sigh."
    return

label strip_ask_SB_reverse_cowgirl(the_person, the_clothing, the_location, the_object, the_round):
    "[the_person.title] straightens up a bit and peaks back at you."
    the_person.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_person.draw_animated_removal(the_clothing, position = SB_reverse_cowgirl.position_tag)
            "[the_person.title] struggles out of her [the_clothing.name] and throws it to the side."
            "She resumes working her hips up and down on top of you with a sigh."

        "Leave it on.":
            mc.name "No, I like how you look with it on."
            if the_person.sluttiness < 80:
                the_person.char "Do you think I look sexy in it?"
                "She bottoms herself out on top of you and starts to grind her hips into yours."
            elif the_person.sluttiness < 100:
                the_person.char "Does it make me look like a good little slut? All I want to be is your good little slut sir."
                "She pushes her hips back into you and moans happily."
            else:
                the_person.char "Does it make me look like the cum hungry slut that I am? That's all I want to be for you sir, your dirty little cum dumpster!"
                "She grinds her hips back into you and moans ecstatically."
    return

label transition_missionary_SB_reverse_cowgirl(the_person, the_location, the_object, the_round):
    "Looking down at [the_person.title], you decide it's time to change things up a little bit."
    mc.name "Hey, why don't we change it up a bit, do you wanna be on top for a bit?"
    if the_person.get_opinion_score("taking control") > 0:
        the_person.char "Oh! I love being on top. Let's do it!"
        $ the_person.change_arousal(5)
    else:
        the_person.char "Sure, if that's what you want [the_person.mc_title]"
    "You pull off of her and let her, then lay down on your back."
    mc.name "Why don't you ride me reverse cowgirl? Let me watch that amazing ass of yours."
    if the_person.get_opinion_score("showing her ass") > 0:
        the_person.char "Mmm, you wanna watch my booty bounce up and down on you? That sounds hot!"
        $ the_person.change_arousal(5)
        "[the_person.title] winks at you, then climbs on top you, giving her ass a bit of a shake as she climbs on."
    else:
        "[the_person.title] blushes, but soon swings her legs over you with her back facing you."
    $ the_person.draw_person(position = "doggy")
    "[the_person.title] reachs down between her legs and takes hold of your penis. She gives it a couple strokes then lines it up with her slit."
    "She pushes her hips back onto you slowly, until you are fully embedded inside her."
    return

label transition_SB_reverse_cowgirl_doggy(the_person, the_location, the_object, the_round):
    "While the view of her ass is amazing, you decide it is time that you took control of the situation."
    "You grab [the_person.title]'s hips and slowly push her up off you. She looks back at you for a moment in confusion."
    mc.name "Don't worry [the_person.title], I'm just gonna change things up. I'll be back inside you in a second."
    "You slide yourself out then get on your knees behind her."
    if the_person.arousal > 60:
            "You rub the tip of your penis against [the_person.title]'s cunt, feeling how nice and wet she is already. She moans softly when you slide the head of your dick over her clit."
    else:
            "You rub the tip of your penis against [the_person.title]'s cunt, getting ready to slide yourself inside."
    "When you're ready you push forward, slipping your shaft deep inside of [the_person.title]. She gasps and quivers ever so slightly as you start to pump in and out."
    return

label orgasm_SB_reverse_cowgirl(the_person, the_location, the_object, the_round):
    "[the_person.title]'s cunt quivers and spasms around you, and then suddenly tenses up."
    $ the_person.call_dialogue("climax_responses")
    "[the_person.title] stirs her womb with your erection aggressively through her climax"
    "After a couple of seconds [the_person.title] sighs and the tension drains from her body."
    the_person.char "God it feels so good, I wonder if you can last long enough to let me cum again..."
    return
