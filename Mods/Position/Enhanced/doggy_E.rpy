init 5 python:
    config.label_overrides["transition_default_doggy"] = "transition_default_doggy_enhanced"

label transition_default_doggy_enhanced(the_girl, the_location, the_object):
    if the_person.has_taboo("vaginal_sex"):
        if the_girl.effective_sluttiness(doggy.associated_taboo) > doggy.slut_cap or the_girl.get_opinion_score("showing her ass") > 0:
            $ the_girl.draw_person(position = "back_peek", the_animation = ass_bob)
            "She stands facing away from you and jiggles her butt playfully."
            mc.name "Get on your knees, I want to get a look at this ass."
            the_girl.char "This big fat ass? You finally want to take a closer look?"
            mc.name "I said on your knees."
            $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
            "She gets onto the [the_object.name] and points her butt in your direction. She lowers her shoulders and works her hips for you."
        else:
            $ the_girl.draw_person(position = "kneeling1")
            mc.name "Get on your knees."
            mc.name "Good girl, now spin around and show me that ass."
            "She nods and turns around."
            $ the_girl.draw_person(position = "doggy")
            mc.name "Nice. Now shake it for me."
            the_girl.char "Like... this?"
            $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.4)
            "[the_girl.title] works her hips and jiggles her ass for you."
            mc.name "Getting there, a little faster now."
            $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
            "She speeds up."

        the_girl.char "Is that what you wanted?"
        "You slap your cock down on her ass and drag it down between her legs, ending with your tip resting against her pussy."
        mc.name "No, this is what I really want."
        $ the_girl.call_dialogue(doggy.associated_taboo+"_taboo_break")
        "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you push forward."
        "After a moment of resistance your cock spreads her pussy open and you slide smoothly inside of her."
        the_girl.char "Oh god.... Ah...."
        "You give her short thrusts, each time going a little bit deeper. Soon you're working your full length in and out of her wet hole."
        $ the_girl.break_taboo("vaginal_sex")
    else:
        "[the_girl.title] gets on her hands and knees as you kneel behind her. You bounce your hard shaft on her ass a couple of times before lining yourself up with her cunt."
        "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return
