init 2 python:
    missionary.scenes.append("scene_missionary_3_enhanced")

label scene_missionary_3_enhanced(the_girl, the_location, the_object):
    #Girl asks you to indulge her fetishes if she has any. Otherwise generally encourages you.
    "[the_girl.possessive_title] leans forward a bit and begins to kiss your neck. Her lips peck up your neck and then she whispers in your ear."
    if the_girl.has_breeding_fetish():
        the_girl "I want you to cum inside me... push as deep as you can and unload!"
    elif the_girl.has_cum_fetish():
        the_girl "I can't wait to feel your cum... cum deep, or pull out and cum all over me... I just want your cum!"
    elif mc.condom:
        the_girl "You feel so good... I can feel you so deep. I love it!"
    elif the_girl.wants_creampie():
        the_girl "You feel so good inside me bare like this. It's okay if you want to cum inside me... I kind of want it too!"
    else:
        the_girl "Your cock feels so good... I can't wait until you pull out and cum all over me!"
    "Encouraged by her words, you speed up, fucking her faster. She runs her hand through your hair and starts to moan at your increased pace."
    menu:
        "Give her everything you've got":
            if the_girl.is_girlfriend():
                mc.name "That's it, you little minx. God I love fucking your tight cunt..."
            elif the_girl.is_affair():
                mc.name "Take it, slut. No man in your life fucks you the way I do."
            elif the_girl.is_single():
                mc.name "You are such a good little slut. God your cunt is so tight and slick."
            else:
                $ so_title = SO_relationship_to_title(the_girl.relationship)
                mc.name "Take it bitch. God your cunt is so tight, so slick. I bet your [so_title] doesn't fuck you as good as I do."
            "[the_girl.possessive_title] clings to you as you fuck her, harder, faster, stronger."
            "You continue at what seems like an impossible pace for as long as you can."
            the_girl "Oh god [the_girl.mc_title]! OH fuck yes!"
            "She is moaning your name right in your ear, and it's really turning you on."
            $ the_girl.change_arousal(10)
            $ mc.change_arousal(10)
        "Tease her":
            the_girl "That's it... oh god [the_girl.mc_title]!"
            "Her body is clinging to you as you start to speed up, but you change up, pushing deep inside her and holding it there."
            the_girl "Oh my god... keep... keep going!"
            "She tries to buck her hips against you, but your weight is pinning her against the [the_object.name]."
            mc.name "You didn't say the magic word."
            if the_girl.arousal > 80:
                the_girl "Please... I'm so close... just a little more!"
            else:
                the_girl "It feels good... just... keep going! Please!"
            mc.name "I'm not sure if you really mean it."
            the_girl "Fuck me please! Fuck me hard and don't stop until I'm cumming my brains out!"
            "Instead of answering, you ease up the pressure and begin to fuck her earnestly again. Her eyes close and she moans as you continue."
            $ the_girl.change_obedience(2)

    return
