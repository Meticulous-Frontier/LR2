init 2:   #Initial declaration made in init 0
    python:
        tit_fuck.scenes.append("scene_SB_Titfuck_Kneeling_1")
        tit_fuck.scenes.append("scene_SB_Titfuck_Kneeling_2")


#The first position label
label scene_SB_Titfuck_Kneeling_1(the_girl, the_location, the_object):

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
        the_person "Mmm, my nipples are so sensitive."
        "[the_girl.title] raps her chest a few times now with your cock, sending ripples out from the point of impact."

    return

#The second position label
label scene_SB_Titfuck_Kneeling_2(the_girl, the_location, the_object):
    if the_girl.is_bald():
        "You run your hand over [the_girl.title]'s smooth scalp while she bounces her [the_girl.tits_description] up and down."
    else:
        "You run your hand through [the_girl.title]'s hair while she bounces her [the_girl.tits_description] up and down."
    "You move your hand down to her shoulder and grasp it firmly, stopping her motion. You begin to buck your hips, giving her a break from her motions."
    "Her hands move to your ass, and you can feel her gently urging you as you thrust up against her."
    if the_girl.has_large_tits():   #Must have a certain cup size
        "You look down and can barely see the tip of your cock poking up from between [the_girl.title]'s generous chest."
        mc.name "Your tits feel so good. You should play with them while I thrust."
        "She takes her hands and runs them along the sides of her breasts. Her abundance of tit flesh feels amazing wrapped around you."
        "[the_girl.title] starts to pinch and pull at her nipples."
        if the_girl.has_cum_fetish():
            the_person "Mmm, your cock is so hot, I can't wait to feel your cum bursting out, all over me."
            "She pinches her nipples hard and pulls on them, causing her to cry out."
            $ the_girl.change_arousal(10)
        else:
            the_person "Your cock is so hot, it feels so right up against my body like this."
            "She pinches her nipples hard and pulls on them, causing her to cry out."
            $ the_girl.change_arousal(5)
    else:                           #She has smaller tits
        "Her hands leave your ass and she brings her hands to the sides of her chest, squishing her tits together to try and stimulate you better."
        mc.name "Mmm, that's it, push them together like that."
        "You keep thrusting. [the_girl.title] gathers some saliva in her mouth and then spits on the head of your cock."
        the_person "Gotta keep things lubricated..."
        "She spits again. You can feel her spit coating your cock and it slides a little smoother between her tits now."
    "You let go of her shoulders. She looks up at you, smiles, and then resumes fucking you with her tits."
    return
