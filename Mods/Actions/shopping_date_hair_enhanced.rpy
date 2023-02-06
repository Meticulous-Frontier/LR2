init 5 python:
    config.label_overrides["shopping_date_hair"] = "shopping_date_hair_enhanced"


label shopping_date_hair_enhanced(the_person):
    mc.name "How about we get your hair done? I think there's a salon in here somewhere."
    if the_person.has_role(girlfriend_role) or the_person.has_role(affair_role):
        "She runs her fingers through her hair."
        the_person "Do you think it's time for a change?"
        mc.name "Maybe. Let's take a look."
    elif the_person.has_role(sister_role):
        the_person "Why, don't you think my hair looks cute?"
        mc.name "Can't hurt to try a new style, right?"
        "She runs her fingers through her hair and thinks for a few seconds."
        the_person "I guess... Alright, we can take a look."
    elif the_person.has_role(mother_role):
        the_person "Oh, I don't like to spend money on things like that. I'm happy with my hair nice and plain."
        mc.name "Come on, if it's money that's the issue I can pay for it. You should treat yourself once in a while."
        "She runs her fingers through her hair and thinks for a moment."
        the_person "Well... I suppose it couldn't hurt to look."
    else: #In theory this shouldn't come up right now, but maybe it will in the future.
        the_person "Don't you like my hair?"
        mc.name "Sure, but a new style could be nice too, right?"
        "She runs her fingers through her hair, then shrugs and nods."
        the_person "Alright, we can take a look."

    "You and [the_person.possessive_title] walk to the salon."

    if day % 7 == 6: # closed on sundays
        "As you walk up to the salon, you notice that it is closed."
        mc.name "Seems we are out of luck."
        the_person "I guess you will have to take me another time."
        return

    if ophelia_get_chocolate_gift_unlock():
        $ salon_manager.draw_person()
        salon_manager "Hello [salon_manager.mc_title], nice to see you again."
        mc.name "Hello [salon_manager.fname], this is [the_person.fname], she wants to change up her style."
        salon_manager "No problem, here is our catalog, don't worry [the_person.fname], I will make you look spectacular."
    else:
        "The receptionist smiles as you come and offers you a style magazine to look through."

    python:
        clear_scene()
        hair_style_check = the_person.hair_style.get_copy()
        pubes_style_check = the_person.pubes_style.get_copy()

    call screen hair_creator(the_person, hair_style_check, pubes_style_check)
    call salon_checkout() from _call_salon_checkout_shopping_date_hair

    $ the_person.draw_person()

    if hair_style_check != the_person.hair_style:
        the_person "Well, what do you think?"
        "She gives a little turn so you can get a good look."
        menu:
            "It's cute":
                mc.name "It's a cute look."
                $ the_person.change_love(1)

            "It's sexy":
                mc.name "You look pretty hot."
                $ the_person.change_slut(1, 30)

            "It's what I wanted":
                mc.name "It's just what I wanted."
                $ the_person.change_obedience(1)

        "You leave the salon together. [the_person.possessive_title] keeps looking at her new style in her phone camera."

    elif hair_style_check.colour != the_person.hair_style.colour:
        the_person "Well, what do you think?"
        "She gives a little turn so you can get a good look."
        menu:
            "It's cute":
                mc.name "It's a cute look."
                $ the_person.change_love(1)

            "It's sexy":
                mc.name "You look pretty hot."
                $ the_person.change_slut(1, 30)

            "It's what I wanted":
                mc.name "It's just what I wanted."
                $ the_person.change_obedience(1)

        "You leave the salon together. [the_person.possessive_title] keeps looking at her new dye in her phone camera."

    elif pubes_style_check != the_person.pubes_style or pubes_style_check.colour != the_person.pubes_style.colour:
        the_person "Will you be checking out my new styling later?"
        mc.name "At least I will have a reason to take of your panties."

        "While you leave the salon together, she grabs your arm and holds you tight."
    else:
        the_person "Pity we couldn't find anything nice."
        mc.name "Don't worry, I like you just the way you are."

        "You leave the salon together."

    python:
        clear_scene()
        del hair_style_check
        del pubes_style_check
    return
