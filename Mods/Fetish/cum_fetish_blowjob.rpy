﻿init python:
    SB_cum_fetish_blowjob = Position(name = "Blowjob", slut_requirement = 40, slut_cap = 100, requires_hard = True, requires_large_tits = False,
        position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
        girl_arousal = 13, girl_energy = 10,
        guy_arousal = 15, guy_energy = 3,
        connections = [],
        intro = "intro_SB_cum_fetish_blowjob",
        scenes = ["scene_SB_cum_fetish_blowjob_1","scene_SB_cum_fetish_blowjob_2"],
        outro = "outro_SB_cum_fetish_blowjob",
        transition_default = "transition_default_SB_cum_fetish_blowjob",
        strip_description = "strip_SB_cum_fetish_blowjob", strip_ask_description = "strip_ask_SB_cum_fetish_blowjob",
        orgasm_description = "orgasm_SB_cum_fetish_blowjob",
        taboo_break_description = "taboo_break_SB_cum_fetish_blowjob",
        verb = "throat",
        opinion_tags = ["giving blowjobs"], record_class = "Blowjobs",
        associated_taboo = "sucking_cock")

    #list_of_girl_positions.append(SB_cum_fetish_blowjob)

#init 1:
#    python:
#        blowjob.link_positions(deepthroat,"transition_blowjob_deepthroat")

label intro_SB_cum_fetish_blowjob(the_girl, the_location, the_object):
    "[the_girl.possessive_title] eagerly begins opening your pants. She pulls out your cock and gives it a few gentle strokes."
    if mc.condom:
        the_girl.char "Why are you wearing this thing? Lets take this off so I can take care of you better..."
        "[the_girl.possessive_title] pulls off your condom."
        $ mc.condom = False
    the_girl.char "How about I take care of this for you?"
    "[the_girl.possessive_title] looks up at your from her knees. She looks you right in the eyes as she leans forward and slides her lips over the tip of your dick."
    $ SB_cum_fetish_blowjob.current_modifier = "blowjob"
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
    return

label scene_SB_cum_fetish_blowjob_1(the_girl, the_location, the_object):
    $ SB_cum_fetish_blowjob.current_modifier = "blowjob"
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
    "She moans slightly as she strokes you with her soft, velvet lips."
    menu:
        "Talk dirty to her":
            mc.name "You are such a good cum slut. You are so eager to suck that cum straight outta me, aren't you?"
            "[the_girl.possessive_title] strokes you a few more times with her skill mouth. She twirls her tongue around the tip a few times before taking a second to respond."
            if the_girl.has_role(cum_internal_role) or the_girl.get_opinion_score("drinking cum") > the_girl.get_opinion_score("cum facials"):
                the_girl.char "Mmm, its been too long since you fed me... I cant wait to feel your cum sliding down my throat..."
                $ the_girl.discover_opinion("drinking cum")
            else:
                the_girl.char "Mmm, I can't wait until I feel it, your balls tighten and that pre-cum twitching... then I'm gonna pull off and stroke you while you cover my face in your hot cum..."
                $ the_girl.discover_opinion("cum facials")
                "She slips you back into her mouth and resumes blowing you."
        "Stay quiet":
            "You rest your hand on her head, guiding her as she sucks you off."
            "With a little encouragement, you pull [the_girl.possessive_title]'s head down a little further with each stroke."
            if the_girl.get_opinion_score("masturbating") > 0:
                if the_girl.outfit.vagina_available():
                    "[the_girl.possessive_title] puts a hand between her legs and starts to touch herself while she she blows you."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating"))
                    $ the_girl.discover_opinion("masturbating")
                    if the_girl.arousal > 60:
                        "Her moans are muffled by your cock when she slides a finger into her pussy and starts to finger herself."
                    else:
                        "She rubs her clit with her middle finger, making little circles around the sensitive nub."
                else:
                    if the_girl.arousal > 60:
                        "[the_girl.possessive_title] puts a hand between her legs and eagerly rubs at her crotch through her clothing."
                    else:
                        "[the_girl.possessive_title] puts a hand between her legs and rubs at her crotch absentmindedly."
            else:
                "[the_girl.possessive_title] keeps up a steady pace, bobbing her head back and forth and running your cock in and out of her soft mouth."

    return

label scene_SB_cum_fetish_blowjob_2(the_girl, the_location, the_object):
    $ SB_cum_fetish_blowjob.current_modifier = None
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)

    "[the_girl.possessive_title] pulls your cock out of her her mouth and leans in even closer. She runs her tongue along the bottom of your shaft, pausing at the top to kiss the tip a few times."
    the_girl.char "Mmm, I can't wait until your cock throbs and your sweet, sticky cum is shooting out..."
    mc.name "Of course you can't wait. You are my perfect little cum slut."
    "When [the_girl.possessive_title] opens her mouth and resumes blowing you, you put your hand on the back of her head, intent to push yourself down her throat."
    if the_girl.get_opinion_score("being submissive") > 0:
        "[the_girl.possessive_title] looks up at you. You can see her pupils dilate as you slowly pull her head towards you, until your cock is buried in her throat."
        "[the_girl.possessive_title]'s knees quiver while her throat spasms around your shaft. You hold her deep while her body twitches with pleasure."
        "You let go of her head and she slowly comes up for air."
        the_girl.char "Oh god you taste so good. You can fuck my throat if you want to, just promise me you'll warn me before you cum..."
        if the_girl.has_role(cum_internal_role) or the_girl.get_opinion_score("drinking cum") > the_girl.get_opinion_score("cum facials"):
            the_girl.char "...I want you to cum in my mouth, not down my throat. I want to feel it pool up inside my mouth until I can barely hold it all and taste your amazing cum filling my mouth completely..."
            $ the_girl.discover_opinion("drinking cum")
        else:
            the_girl.char "...I want to wear your cum all over my face, like a good slut! I want to walk around the rest a day with it obvious you've blown your load all over to everyone who sees me..."
            $ the_girl.discover_opinion("cum facials")
        "Turned on by her filthy words, you grab the back of her head with both hands and force your dick right back down her throat."
        "You fuck her face roughly. Her throat makes vulgar suction noises with each thrust, and you can see her throat bulging slightly."
        $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3)
    elif the_girl.is_dominant():
        "[the_girl.possessive_title] grabs your hands in hers. She holds your hands as she looks up at you, making eye contact."
        "With her hands holding yours, she opens her mouth wide and descends on your cock."
        "She bottoms out and her nose is touching your pubic hair. You are balls deep down her throat."
        mc.name "Mmmm, that's it bitch. Take it deep!"
        "Still making eye contact, [the_girl.possessive_title] begins to bob her head up and down, completely deep throating you with every stroke."
        "Every few strokes you can feel the soft rumble of a moan, being stifled by your length she keeps impaling her throat on."
        $ the_girl.discover_opinion("taking control")
        $ the_girl.change_arousal(the_girl.get_opinion_score("taking control") * 3)
    else:
        "[the_girl.possessive_title] turns her eyes up and meets your gaze. She eagerly swallows as your push yourself down her throat, her tongue eagerly licking at the bottom of your shaft."
        mc.name "Fuck that feels good [the_girl.title]."
        "In response she bottoms out on your dick. She rocks her head left and right, grinding her face into your crotch to take as much of your length as possible."
        "She tenses and and relaxes her throat rhythmically, gently massaging your shaft with it."
        "You moan at the intense sensations.You let go of her head and she slowly comes up for air."
        the_girl.char "Oh god you taste so good. Just promise me you'll warn me before you cum..."
        if the_girl.has_role(cum_internal_role) or the_girl.get_opinion_score("drinking cum") > the_girl.get_opinion_score("cum facials"):
            the_girl.char "...I want you to cum in my mouth, not down my throat. I want to feel it pool up inside my mouth until I can barely hold it all and taste your amazing cum filling my mouth completely..."
            $ the_girl.discover_opinion("drinking cum")
        else:
            the_girl.char "...I want to wear your cum all over my face, like a good slut! I want to walk around the rest a day with it obvious you've blown your load all over to everyone who sees me..."
            $ the_girl.discover_opinion("cum facials")
        "You cock twitches in response to her filthy words. She notices and quickly opens her mouth and take you deep again."
    return

label outro_SB_cum_fetish_blowjob(the_girl, the_location, the_object):
    $ SB_cum_fetish_blowjob.current_modifier = "blowjob"
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
    "Little by little the soft, warm mouth of [the_girl.possessive_title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
    mc.name "Fuck, here I come!"

    if the_girl.has_role(cum_internal_role) or the_girl.get_opinion_score("drinking cum") > the_girl.get_opinion_score("cum facials"):
        "[the_girl.possessive_title] moans and looks you in the eyes. She pulls off until just the  tip of your cock is in her mouth and she begins to stroke out off eagerly."
        "You erupt in orgasm into her greedy mouth. Her pupils dilate as her cum addicted brain registers the presence of your cum in her mouth."
        "[the_girl.possessive_title] is moaning uncontrollably around your twitching cock."
        $ the_girl.cum_in_mouth()
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
        if the_girl.arousal > 100:
            "[the_girl.possessive_title]'s legs quiver as she convulses. She is so addicted to your cum, blowing in her mouth has set off another orgasm for her."
            $ the_girl.change_obedience(5*the_girl.get_opinion_score("drinking cum"))
        "Once you've had a second to recover, [the_girl.possessive_title] closes her mouth and swallows loudly. It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
        $ SB_cum_fetish_blowjob.current_modifier = None
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
        $ the_girl.call_dialogue("cum_mouth")

    else:
        "[the_girl.possessive_title] moans and looks you in the eyes. She pulls off your cock and strokes you eagerly, waiting for the first splash across her face."
        "You erupt in orgasm and shoot your load across her glowing face. Her pupils dilate as her cum addicted brain registers the presence of your cum on her skin."
        "[the_girl.possessive_title] moans uncontrollably with every spurt"
        $ the_girl.discover_opinion("cum facials")
        $ the_girl.cum_on_face()
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
        if the_girl.arousal > 100:
            "[the_girl.possessive_title]'s legs quiver as she convulses. She is so addicted to your cum, blowing on her face has set off another orgasm for her."
            $ the_girl.change_obedience(5*the_girl.get_opinion_score("cum facials"))
        "Slowly recovering, you look at [the_girl.possessive_title]'s cum covered face. Her eyes are closed and she is absentmindedly playing with some of the cum that is starting to run down her neck."
        $ SB_cum_fetish_blowjob.current_modifier = None
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
        the_girl.char "Yes.. its so hot... It feels so good on my skin..."
    return

label transition_default_SB_cum_fetish_blowjob(the_girl, the_location, the_object):
    $ SB_cum_fetish_blowjob.current_modifier = "blowjob"
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
    if mc.condom:
        the_girl.char "Why are you wearing this thing? Lets take this off so I can take care of you better..."
        "[the_girl.possessive_title] pulls off your condom."
        $ mc.condom = False
    "[the_girl.possessive_title] gets onto her knees in front of you and takes your hard cock in her hands. She strokes it tentatively a few times, then leans in and slides the tip into her mouth."
    mc.name "That's it, that's a good girl."
    return

label strip_SB_cum_fetish_blowjob(the_girl, the_clothing, the_location, the_object):
    $ SB_cum_fetish_blowjob.current_modifier = None
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)

    "[the_girl.possessive_title] pops off your cock and looks up at you."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing)
    "[the_girl.possessive_title] stands and strips off her [the_clothing.name]. She drops it to the ground, then gets back on her knees and slides your cock inside her mouth."
    $ SB_cum_fetish_blowjob.current_modifier = "blowjob"
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
    return

label strip_ask_SB_cum_fetish_blowjob(the_girl, the_clothing, the_location, the_object):
    $ SB_cum_fetish_blowjob.current_modifier = None
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)

    "[the_girl.possessive_title] pops off your cock and looks up at you from her knees."
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_cum_fetish_blowjob.position_tag)
            "[the_girl.possessive_title] stands up and strips out of her [the_clothing.name]. Then she gets back onto her knees and slides your cock all the way to the back of her mouth."
            $ SB_cum_fetish_blowjob.current_modifier = "blowjob"
            $ SB_cum_fetish_blowjob.redraw_scene(the_girl)


        "Leave it on":
            mc.name "No, I like how you look with it on."
            the_girl.char "Is it sexy? Does it make you just want to blow your load, looking at me wearing this?"
            $ SB_cum_fetish_blowjob.current_modifier = "blowjob"
            $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
            "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."
    return

label orgasm_SB_cum_fetish_blowjob(the_girl, the_location, the_object):
    $ SB_cum_fetish_blowjob.current_modifier = "blowjob"
    $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] pauses suddenly. You hear her whimper softly - the noise party muffled by your cock."

    "[the_girl.possessive_title] starts to pull back off of your cock. You place a firm hand on the back of her head."
    mc.name "Did I tell you to stop sucking, you dirty little slut?"
    "You push her back down, hard. [the_girl.possessive_title] keeps her mouth open wide and fits you all the way in, quivering as she climaxes."
    mc.name "A cock sleeve like you deserves to have her throat stuffed when she cums."
    if the_girl.get_opinion_score("being submissive") > 0:
        if the_girl.sluttiness > the_girl.core_sluttiness and the_girl.core_sluttiness < SB_cum_fetish_blowjob.slut_cap:
            $ the_girl.change_slut_core(the_girl.get_opinion_score("being submissive")) #If she likes being submissive this makes her cum and become sluttier super hard.
            $ the_girl.change_slut_temp(-the_girl.get_opinion_score("being submissive"))
        $ the_girl.change_obedience(2*the_girl.get_opinion_score("being submissive"))
        "[the_girl.possessive_title] closes her eyes tight. You can feel her throat spasm around your shaft in time with her orgasmic contractions."
        if the_girl.outfit.vagina_visible():
            "You can see that [the_girl.possessive_title]'s pussy is dripping wet as she cums."
        else:
            $ the_item = the_girl.outfit.get_lower_top_layer()
            if the_item and the_item.underwear:
                "[the_girl.possessive_title]'s dripping wet pussy has managed to soak through her underwear, leaving a wet mark on her [the_item.name]."
            else:
                "[the_girl.possessive_title] clenches her thighs together and rides out her orgasm."
            $ del the_item
        $ SB_cum_fetish_blowjob.current_modifier = None
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
        "When she's stopped twitching and moaning you let [the_girl.possessive_title] slide back. She pants loudly, then licks along the length of your cock."
        the_girl.char "That was... incredible... Okay, I came... now its your turn!"
        "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."
    else:
        "[the_girl.possessive_title] closes her eyes as her orgasm peaks. She holds almost perfectly still, your dick still sitting in her mouth, until she's finished."
        $ SB_cum_fetish_blowjob.current_modifier = None
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
        "She pulls off and takes a long, deep breath."
        $ the_girl.change_obedience(1)
        $ the_girl.change_happiness(2)
        the_girl.char "Wow, that was amazing... Okay, I came... now its your turn!"
        "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."

    return

label taboo_break_SB_cum_fetish_blowjob(the_girl, the_location, the_object):
    # TODO: Add custom taboo break
    return