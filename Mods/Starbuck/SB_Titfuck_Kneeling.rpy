init python:
    SB_Titfuck_Kneeling = Position("Titfuck",   #Name of the position in the sex position selection screen
        25,                                         #Required sluttiness for girl to consider. 20 sluttiness = 1 heart
        60,                                         #Max temporary sluttiness from postions
        "blowjob",                                  #Image name used for the position
        "Kneel",                                    #Description of female pose. Requires room item that accomodates this descriptor: EG, bed for "laying"
        "Tits",                                     #Girl part that must be available to select position. Can be "None", "Tits", or "Vagina"
        "Foreplay",                                 #Skill used to determine how fast arousal is gained each round
        15,                                         #Base female arousal gain per round
        20,                                         #Base male arousal gain per round
        [],                                         #"Connections". Currently unused as far as I can tell. Use link_positions() or Link_positions_two_way() instead
        "intro_SB_Titfuck_Kneeling",                #Name of label describing getting into positions
        ["scene_SB_Titfuck_Kneeling_1","scene_SB_Titfuck_Kneeling_2"],  #List of labels describing the act of the positions
        "outro_SB_Titfuck_Kneeling",                #Label describing when player has orgasm
        "transition_default_SB_Titfuck_Kneeling",   #Label for default transition. I think this is currently unused in game
        "strip_SB_Titfuck_Kneeling",                #Label for if girl decides to take something off
        "strip_ask_SB_Titfuck_Kneeling",            #Label for if girl asks to take something off
        "orgasm_SB_Titfuck_Kneeling",               #Label for if girl orgasms
        opinion_tags = ["giving blowjobs", "showing her tits"])     #Girl has additional arousal gains based on these opinions. See random_lists.rpy for possible likes.
    list_of_girl_positions.append(SB_Titfuck_Kneeling)  #Uncomment this when this position is finished# #This line adds it to the list of positions the girl can choose if she pleases you NOTE:Cannot be selected by player at this time.
    list_of_positions.append(SB_Titfuck_Kneeling) #Use this function if you want the position to be selectable during sexy times by the player.

init 1 python:
    #Use this function to create a two way link between this position and another, so players can go back and forth.
    SB_Titfuck_Kneeling.link_positions_two_way(blowjob, "transition_SB_Titfuck_Kneeling_blowjob", "transition_blowjob_SB_Titfuck_Kneeling")

        #Use this line to create a one way link, so players can go from this position to the one linked
#        SB_Titfuck_Kneeling.link_positions(deepthroat,"transition_SB_Titfuck_Kneeling_deepthroat")

#This label describes getting into position
label intro_SB_Titfuck_Kneeling(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title] eagerly begins opening your pants. She pulls out your cock and gives it a few gentle strokes."
    the_girl.char "How about I take care of this for you?"
    if mc.condom:
        the_girl.char "Why are you wearing this thing? Lets take this off so I can take care of you better..."
        "[the_girl.possessive_title] pulls off your condom."
        $ mc.condom = False
    "[the_girl.possessive_title] looks up at you from her knees. She looks you right in the eyes as she leans forward and slides your cock between her tits."
    "With both hands holding her breasts together, she slowly starts to move her pillowy flesh up and down your erection."

    return

#The first position label
label scene_SB_Titfuck_Kneeling_1(the_girl, the_location, the_object, the_round):

    "[the_girl.possessive_title] sticks her tongue out and licks at the tip of your dick each time she moves her body down."
    "She moans slightly as she pauses to stroke you with her soft, velvet lips. She gets your shaft nice and wet and then continues heaving her chest up and down."
    "The extra lubrication feels great, causing you to let out an appreciative moan."
    if the_girl.sex_skills["Foreplay"] < 2: #Inexperienced.
        "[the_girl.title] is trying her best to pleasure you with her chest, but her inexperience is starting to show."
        "She is pushing her tits together, but she is doing it too hard. It doesn't hurt, but the sensation isn't particularly pleasurable."
        mc.name "Mmm, easy, you aren't trying to strangle it. Tits are soft, your grip should be soft too."
        "[the_girl.title] mutters a quick apology, but lightens up her grip. It feels much better when she resumes stroking you."
    else: #Is experienced
        "[the_girl.title]'s creamy pillows feel amazing wrapped around your erection."
        "[the_girl.possessive_title] lets out a moan. She pinches her nipples while you pound her pillows."

        "She grabs your cock with her hand and then pulls her chest back from around you. She takes the tip of your cock and uses it to tease her nipples."
        the_person.char "Mmm, my nipples are so sensitive."
        "[the_girl.title] raps her chest a few times now with your cock, sending ripples out from the point of impact."

    return

#The second position label
label scene_SB_Titfuck_Kneeling_2(the_girl, the_location, the_object, the_round):
    "You run your hand through [the_girl.title]'s hair while she bounces her mammaries up and down."
    "You move your hand down to her shoulder and grasp it firmly, stopping her motion. You begin to buck your hips, giving her a break from her motions."
    "Her hands move to your ass, and you can feel her gently urging you as you thrust up against her."
    if the_girl.has_large_tits():   #Must have a certain cup size
        "You look down and can barely see the tip of your cock poking up from between [the_girl.title]'s generous chest."
        mc.name "Your tits feel so good. You should play with them while I thrust."
        "She takes her hands and runs them along the sides of her breasts. Her abundance of titflesh feels amazing wrapped around you."
        "[the_girl.title] starts to pinch and pull at her nipples."
        if SB_check_fetish(the_girl, cum_external_role):
            the_person.char "Mmm, your cock is so hot, I can't wait to feel your cum bursting out, all over me."
            "She pinches her nipples hard and pulls on them, causing her to cry out."
            $ the_girl.change_arousal(10)
        else:
            the_person.char "Your cock is so hot, it feels so right up against my body like this."
            "She pinches her nipples hard and pulls on them, causing her to cry out."
            $ the_girl.change_arousal(5)
    else:                           #She has smaller tits
        "Her hands leave your ass and she brings her hands to the sides of her chest, squishing her tits together to try and stimulate you better."
        mc.name "Mmm that's it, push them together like that."
        "You keep thrusting. [the_girl.title] gathers some saliva in her mouth and then spits on the head of your cock."
        the_person.char "Gotta keep things lubricated..."
        "She spits again. You can feel her spit coating your cock and it slides a little smoother between her tits now."
    "You let go of her shoulders. She looks up at you, smiles, and then resumes fucking you with her tits."
    return

#You can make more than 2 position labels. This one is currently unused. To use it, add the label name to the position declaration at the beginning of the file with the other two labels
label scene_SB_Titfuck_Kneeling_3(the_girl, the_location, the_object, the_round):
    "This scene is currently unused."

    return

#This label describes when the player orgasms
label outro_SB_Titfuck_Kneeling(the_girl, the_location, the_object, the_round):
    $ SB_Titfuck_Kneeling.current_modifier = "blowjob"
    $ SB_Titfuck_Kneeling.redraw_scene(the_girl)
    "Little by little the soft, pillowy flesh of [the_girl.possessive_title]'s tits brings you closer to orgasm. You look down and see the hunger in her eyes and it pushes you over the edge."
    mc.name "Fuck, here I come!"
    if SB_check_fetish(the_girl, cum_internal_role):  #She can't help but swallow if she has an internal cum fetish#
        "[the_girl.possessive_title] suddenly leans forward and takes you in her mouth. She gives you a couple quick strokes with her hand"
        "You erupt in orgasm into her greedy mouth. Her pupils dilate as her cum addicted brain registers the presence of your cum in her mouth."
        "[the_girl.possessive_title] is moaning uncontrollably around your spasming cock."
        $ the_girl.cum_in_mouth()                   #See script.rpy. Adds cum clothing item and adds some sluttiness based on likes/dislikes
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)      #Must redraw scene to see cum on the girl
        if the_girl.arousal > 100:                  #She is orgasmic
            "[the_girl.possessive_title]'s legs quiver as she convulses. She is so addicted to your cum, blowing in her mouth has set off another orgasm for her."
            $ the_girl.change_obedience(5*the_girl.get_opinion_score("drinking cum"))           #Feels good to serve MC
        "Once you've had a second to recover, [the_girl.possessive_title] closes her mouth and swallows loudly. It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
        $ SB_cum_fetish_blowjob.current_modifier = None
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
        $ the_girl.call_dialogue("cum_mouth")
        the_girl.char "Mmmm, so tasty [the_girl.mc_title]. I'm sorry, I couldn't pass up an opportunity to swallow your wonderful cum."
    elif SB_check_fetish(the_girl, cum_external_role):  #She has the external cum fetish
        "[the_girl.possessive_title] grabs her tits with both hands and eagerly strokes you with them. You moan as your first wave explodes from your shaft."
        $ the_girl.cum_on_tits()                    #See script.rpy. Adds cum clothing item and adds some sluttiness based on likes/dislikes
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)       #Must redraw scene to see cum on the girl
        "It feels amazing, your second wave spurts so hard it hits her face."
        $ the_girl.cum_on_face()                    #Because cum is messy
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)
        "[the_girl.possessive_title] moans uncontrollably with every spurt"
        if the_girl.arousal > 100:                      #She is orgasmic
            "[the_girl.possessive_title]'s legs quiver as she convulses. She is so addicted to your cum, blowing on her tits and face has set off another orgasm for her."
            $ the_girl.change_obedience(5*the_girl.get_opinion_score("cum facials"))        #Feels good to serve MC
        "Slowly recovering, you look at [the_girl.possessive_title]'s cum covered upper body. Her eyes are closed and she is absentmindedly playing with some of the cum that is starting to run down her cleavage."
        the_girl.char "Yes! Its so hot. It feels so good on my skin..."
    elif the_girl.effective_sluttiness() > 60 or the_girl.get_opinion_score("being covered in cum") > 0:          #No cum fetish, but still slutty
        "[the_girl.possessive_title] smiles wide as your cum splashes onto her body."
        $ the_girl.cum_on_tits()
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)       #Must redraw scene to see cum on the girl
        the_girl.char "Mmm, that's it, cum for me!"
        "Slowly recovering, you look down at [the_girl.possessive_title]'s cum covered chest. She smiles up at you, happy with herself at getting you off."
    else:                                               #Girl is not amused
        "[the_girl.possessive_title] stop when she feels the heat of your cum coming out. She lets your cum spill out and into her cleavage."
        $ the_girl.cum_on_tits()
        $ SB_cum_fetish_blowjob.redraw_scene(the_girl)       #Must redraw scene to see cum on the girl
        "She waits patiently for you to finish, but looks uncomfortable being covered in your cum."
    return

#This label describes transition from this position to a blowjob
label transition_SB_Titfuck_Kneeling_blowjob(the_girl, the_location, the_object, the_round):
    mc.name "Why don't you suck on me now? I bet those pouty lips of yours would feel amazing around my cock."
    "[the_girl.possessive_title] takes your hard cock in her hands. She strokes it tentatively a few times, then leans in and slides the tip into her mouth."
    mc.name "That's it, that's a good girl."
    return

#This label describes transitions from blowjob to this position
label transition_blowjob_SB_Titfuck_Kneeling(the_girl, the_location, the_object, the_round):
    mc.name "Those tits look great. Why don't you wrap those around my cock for a bit..."
    if mc.condom:
        the_girl.char "Why are you wearing this thing? Lets take this off so I can take care of you better..."
        "[the_girl.possessive_title] pulls off your condom."
        $ mc.condom = False
    "[the_girl.possessive_title] takes your hard cock in her hands. She strokes it tentatively a few times, then leans in and slides your length between her twin peaks." #TODO also figure out way to reference Hooters
    mc.name "That's it, that's a good girl."
    return

#This label describes the girl deciding to take something off
label strip_SB_Titfuck_Kneeling(the_girl, the_clothing, the_location, the_object, the_round):
    "[the_girl.possessive_title] looks up at you."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing)
    "[the_girl.possessive_title] stands and strips off her [the_clothing.name]. She drops it to the ground, then gets back on her knees and slides your cock between her tits."
    $ SB_Titfuck_Kneeling.redraw_scene(the_girl)
    return

#This label describes the girl asking to take something off
label strip_ask_SB_Titfuck_Kneeling(the_girl, the_clothing, the_location, the_object, the_round):
    "[the_girl.possessive_title] looks up at you from her knees."
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_Titfuck_Kneeling.position_tag)
            "[the_girl.possessive_title] stands up and strips out of her [the_clothing.name]. Then she gets back onto her knees and slides your cock back between her tits."

        "Leave it on.":
            mc.name "No, I like how you look with it on."
            the_girl.char "Is it sexy? Does it make you just want to blow your load, looking at me wearing this?"
    return

#This label describes when she orgasms
label orgasm_SB_Titfuck_Kneeling(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title] pauses suddenly. She looks up at you, her face a mixture of pleasure and confusion."
    the_girl.char "I'm... I'm gonna cum!"
    "You place a firm hand on her shoulder and begin to pump your hips."
    mc.name "Cum for me, you dirty little slut, while I fuck your tits!"
    "[the_girl.title]'s tits quiver pleasantly as she orgasms. You fuck her plump mounds, increasing your pleasure as she achieves hers."

    return
