﻿init:
    python:
        Ophelia_blowjob = Position(name = "Special Blowjob", slut_requirement = 30, slut_cap = 90, requires_hard = True, requires_large_tits = False,
            position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
            girl_arousal = 4, girl_energy = 8,
            guy_arousal = 20, guy_energy = 3,
            connections = [],
            intro = "intro_Ophelia_blowjob",
            scenes = ["scene_Ophelia_blowjob_1","scene_Ophelia_blowjob_2"],
            outro = "outro_Ophelia_blowjob",
            transition_default = "transition_default_Ophelia_blowjob",
            strip_description = "strip_Ophelia_blowjob", strip_ask_description = "strip_ask_Ophelia_blowjob",
            orgasm_description = "orgasm_Ophelia_blowjob",
            taboo_break_description = "taboo_break_Ophelia_blowjob",
            verb = "mouth fuck",
            opinion_tags = ["giving blowjobs", "dinking cum"], record_class = "Blowjobs",
            default_animation = idle_wiggle_animation, modifier_animations = {"blowjob":blowjob_bob},
            associated_taboo = "sucking_cock")


label intro_Ophelia_blowjob(the_girl, the_location, the_object):
    "You unzip your pants and pull your underwear down far enough to let your hard cock out."
    the_girl.char "Mmm, it looks so hard! Let me take care of that for you..."
    "[the_girl.possessive_title] drops to her knees in front of you. She runs her hands along your hips, then leans foward and slides her lips over the tip of your dick."
    $ Ophelia_blowjob.current_modifier = "blowjob"
    $ Ophelia_blowjob.redraw_scene(the_girl)
    "She teases and licks at the tip, but you know this girl is just toying with you."
    "[the_girl.title] looks up at you, and without breaking eye contact, her lips drag down the side of your length until she completely bottoms out"
    "Her eyes are filled with pride and mischief as her tongue swirls around your cock she bobs her head up and down on your length."
    "You take a deep breath and get yourself ready for a wild ride."
    return

label taboo_break_Ophelia_blowjob(the_girl, the_location, the_object):
    $ the_girl.call_dialogue(Ophelia_blowjob.associated_taboo+"_taboo_break") #Personality dialogue includes all associated "convince me" dialogue
    if the_girl.effective_sluttiness(Ophelia_blowjob.associated_taboo) > Ophelia_blowjob.slut_cap:
        #She's eager to try this
        "[the_girl.possessive_title] kneels down in front of you, eyes locked on your hard cock."
        $ Ophelia_blowjob.current_modifier = "blowjob"
        $ Ophelia_blowjob.redraw_scene(the_girl)
        "She leans in, turning her head to the side to run her tongue down the bottom of your shaft."
        "She licks your balls briefly, then works back up to the tip and slides it past her lips."
        "You sigh happily as you feel [the_girl.title]'s warm mouth envelop your cock."
        "She wastes no time picking up speed, happily bobbing her head up and down over your sensitive tip."

    else:
        "[the_girl.possessive_title] hesitantly gets onto her knees, eyes locked on your hard cock."
        "She gently holds onto your shaft with one hand and brings the tip closer to her lips."
        "She looks up at you just before the moment of truth, locking eyes as she opens her lips and slides the tip of your cock past them."
        $ Ophelia_blowjob.current_modifier = "blowjob"
        $ Ophelia_blowjob.redraw_scene(the_girl)

        "You sigh happily as you feel [the_girl.title]'s warm mouth envelop your cock."
        "She moves slowly at first, gently working her head up and down over your sensitive tip."
    return

label scene_Ophelia_blowjob_1(the_girl, the_location, the_object):
    $ Ophelia_blowjob.current_modifier = "blowjob"
    $ Ophelia_blowjob.redraw_scene(the_girl)

    "[the_girl.title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out."
    "Her mouth moves an incredible distance with each stroke as she repeatedly throats you. Her gag immunity serving her well as she services your erection."
    menu:
        "Talk dirty to her.":
            mc.name "That feels great [the_girl.title]. You look good on your knees, sucking my cock."
            "She slides your cock out of her mouth to speak."
            the_girl.char "Mmm, and you feel so good in my mouth. You're so big I can barely manage."
            $ the_girl.discover_opinion("giving blowjobs")
            "She rubs her cheek against your wet shaft."
            the_girl.char "Don't forget to warn me when you cum. I like it all over my face, remember?."
            "She slips you back into her mouth and resumes blowing you."

        "Stay quiet.": #TODO change this
            "You rest your hand on her head, guiding her as she sucks you off."
            if the_girl.get_opinion_score("masturbating") > 0:
                if the_girl.outfit.vagina_available():
                    "[the_girl.title] puts a hand between her legs and starts to touch herself while she she blows you."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating"))
                    $ the_girl.discover_opinion("masturbating")
                    if the_girl.arousal > 60:
                        "Her moans are muffled by your cock when she slides a finger into her pussy and starts to finger herself."
                    else:
                        "She rubs her clit with her middle finger, making little circles around the sensitive nub."
                else:
                    if the_girl.arousal > 60:
                        "[the_girl.title] puts a hand between her legs and eagerly rubs at her crotch through her clothing."
                    else:
                        "[the_girl.title] puts a hand between her legs and rubs at her crotch absentmindedly."

            else:
                "[the_girl.title] keeps up a steady pace, bobbing her head back and forth and running your cock in and out of her soft mouth."
    return

label scene_Ophelia_blowjob_2(the_girl, the_location, the_object):
    $ Ophelia_blowjob.current_modifier = None
    $ Ophelia_blowjob.redraw_scene(the_girl)

    "[the_girl.title] pulls your cock out of her her mouth and leans in even closer. She runs her tongue along the bottom of your shaft, pausing at the top to kiss the tip a few times."
    the_girl.char "Feels good, doesn't it?"
    mc.name "Yeah, it does. You are an amazing cocksucker."
    "[the_girl.possessive_title] smiles and keeps working her tongue over your cock. She licks it bottom to top, then sucks on the tip, then licks it from the top back to the bottom."
    $ Ophelia_blowjob.current_modifier = "blowjob"
    $ Ophelia_blowjob.redraw_scene(the_girl)
    "Without warning, she does the move. With her mouth open and her tongue extended, she throats you."
    "Her tongue reaches out and starts lapping at your testicles while her throat contracts around the head. She lets out a throaty moan that feels like it is massaging your entire groin."
    "You close your eyes and just focus on enjoying the nearly overwhelming sensations."

    return

label outro_Ophelia_blowjob(the_girl, the_location, the_object):
    $ Ophelia_blowjob.current_modifier = "blowjob"
    $ Ophelia_blowjob.redraw_scene(the_girl)
    "The warm mouth of [the_girl.title] drives you to your orgasm. One last pass down her velvet throat is enough to push you past the point of no return."
    mc.name "Fuck, here I come!"
    "She pulls back, your cock slipping out of [the_girl.possessive_title]'s mouth with a satisfyingly wet pop. She strokes you with her hand while she points you at her face."
    the_girl.char "Do it! Cum all over me!!!"
    $ Ophelia_blowjob.current_modifier = None
    $ Ophelia_blowjob.redraw_scene(the_girl)
    "[the_girl.title] sticks out her tongue for you and holds still, eager to take your hot load."
    $ the_girl.cum_on_face()
    $ Ophelia_blowjob.redraw_scene(the_girl)
    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
    "You take a deep breath to steady yourself once you've finished cumming. [the_girl.title] looks up at you from her knees, face covered in your semen."
    $ the_girl.call_dialogue("cum_face")
    "Before you even start to recover, she starts to rub your seed into the skin of her face with two fingers."
    return


label transition_default_Ophelia_blowjob(the_girl, the_location, the_object):
    $ Ophelia_blowjob.current_modifier = "blowjob"
    $ Ophelia_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] gets onto her knees in front of you and takes your hard cock in her hands. She strokes it tentatively a few times, then leans in and slides the tip into her mouth."
    the_girl.char "Mmm, its time for me to take care of you."
    return

label strip_Ophelia_blowjob(the_girl, the_clothing, the_location, the_object):
    $ Ophelia_blowjob.current_modifier = None
    $ Ophelia_blowjob.redraw_scene(the_girl)

    "[the_girl.title] pops off your cock and looks up at you."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing)
    "[the_girl.possessive_title] stands and strips off her [the_clothing.name]. She drops it to the ground, then gets back on her knees and slides your cock inside her mouth."
    $ Ophelia_blowjob.current_modifier = "blowjob"
    $ Ophelia_blowjob.redraw_scene(the_girl)
    return

label strip_ask_Ophelia_blowjob(the_girl, the_clothing, the_location, the_object):
    $ Ophelia_blowjob.current_modifier = None
    $ Ophelia_blowjob.redraw_scene(the_girl)

    "[the_girl.title] pops off your cock and looks up at you from her knees."
    the_girl.char "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = Ophelia_blowjob.position_tag)
            "[the_girl.possessive_title] stands up and strips out of her [the_clothing.name]. Then she gets back onto her knees and slides your cock all the way to the back of her mouth."
            $ Ophelia_blowjob.current_modifier = "blowjob"
            $ Ophelia_blowjob.redraw_scene(the_girl)


        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl.char "Yeah? Do I look sexy in it?"
                $ Ophelia_blowjob.current_modifier = "blowjob"
                "She licks the length of your shaft, then slides your tip into her mouth and starts to blow you again."
            else:
                the_girl.char "Does it make me look like a good little slut? Or is your cock in my mouth enough for that?"
                $ Ophelia_blowjob.current_modifier = "blowjob"
                $ Ophelia_blowjob.redraw_scene(the_girl)
                "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."
    return

label orgasm_Ophelia_blowjob(the_girl, the_location, the_object):
    $ Ophelia_blowjob.current_modifier = "blowjob"
    $ Ophelia_blowjob.redraw_scene(the_girl)
    "[the_girl.title] pauses suddenly. You hear her whimper softly - the noise party muffled by your cock."
    menu:
        "Be rough as she cums":
            "[the_girl.possessive_title] starts to pull back off of your cock. You place a firm hand on the back of her head."
            mc.name "Did I tell you to stop sucking, you dirty little slut?"
            if the_girl.sex_skills["Oral"] > 2:
                "You push her back down, hard. [the_girl.title] keeps her mouth open wide and fits you all the way in, quivering as she climaxes."
            else:
                "You push her back down, hard. [the_girl.title] gags and coughs, but you make sure she gets your cock back into her mouth. She quivers as she climaxes"

            mc.name "A cock sleeve like you deserves to have her throat stuffed when she cums."
            if the_girl.get_opinion_score("being submissive") > 0:
                if the_girl.sluttiness > the_girl.core_sluttiness and the_girl.core_sluttiness < Ophelia_blowjob.slut_cap:
                    $ the_girl.change_slut_core(the_girl.get_opinion_score("being submissive")) #If she likes being submissive this makes her cum and become sluttier super hard.
                    $ the_girl.change_slut_temp(-the_girl.get_opinion_score("being submissive"))
                $ the_girl.change_obedience(2*the_girl.get_opinion_score("being submissive"))
                "[the_girl.possessive_title] closes her eyes tight. You can feel her throat spasm around your shaft in time with her orgasmic contractions."
                if the_girl.outfit.vagina_visible():
                    "You can see that [the_girl.title]'s pussy is dripping wet as she cums."
                else:
                    $ the_item = the_girl.outfit.get_lower_top_layer()
                    if the_item.underwear:
                        "[the_girl.possessive_title]'s dripping wet pussy has managed to soak through her underwear, leaving a wet mark on her [the_item.name]."
                    else:
                        "[the_girl.possessive_title] clenches her thighs together and rides out her orgasm."
                    $ the_item = None
                $ Ophelia_blowjob.current_modifier = None
                $ Ophelia_blowjob.redraw_scene(the_girl)
                "When she's stopped twitching and moaning you let [the_girl.title] slide back. She pants loudly, then licks along the length of your cock."
                the_girl.char "That was... incredible... I want more!"
            else:
                "[the_girl.possessive_title] closes her eyes as her orgasm peaks. She holds almost perfectly still, your dick still sitting in her mouth, until she's finished."
                $ Ophelia_blowjob.current_modifier = None
                $ Ophelia_blowjob.redraw_scene(the_girl)
                "She pulls off and takes a long, deep breath."
                $ the_girl.change_obedience(1)
                $ the_girl.change_happiness(2)
                the_girl.char "Damn, that was crazy! I couldn't breath!"

        "Be gentle as she cums":
            $ Ophelia_blowjob.current_modifier = None
            $ Ophelia_blowjob.redraw_scene(the_girl)
            mc.name "That's it, cum for me [the_girl.title]."
            "[the_girl.possessive_title] pulls off your cock as she climaxes. She nuzzles up against your hot, wet shaft as her body shivers uncontrollably."
            "You stroke her hair and wait until she's over the worst of it."
            $ the_girl.change_happiness(2)
            the_girl.name "Wow... Thanks for waiting, that was really intense."
            "She licks your shaft and looks up at you."
            the_girl.name "Should I get going again?"
            "She doesn't wait for an answer and starts sucking your cock again."
    return
