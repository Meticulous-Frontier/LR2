init 5 python:
    config.label_overrides["meet_person_label"] = "meet_person_enhanced_label"

label meet_person_enhanced_label():
    # You see a women drop some cash out of her purse. YOu can either return it for an introduction+bonus love OR
    # Keep it because it's money and you like money.
    $ the_person = make_person(force_random = True)
    $ the_person.draw_person(position = "walking_away")
    #"This is a test to see if the override worked."
    "While you're wandering a woman hurries past you on the sidewalk, jogging for a bus waiting up the street."
    "A few steps ahead of you she stumbles and trips."
    $ the_person.call_dialogue("surprised_exclaim")
    "She rushes to get back to her feet, unaware that her wallet has slipped out and is sitting on the sidewalk."
    "You crouch down to pick it up. A discreet check reveals there is a sizeable amount of cash inside."
    menu:
        "Return everything":
            $ downtown.add_person(the_person)
            $ the_person.generate_home()
            "You speed up to a jog to catch the woman."
            mc.name "Excuse me! You dropped your wallet!"
            $ the_person.draw_person()
            "She pauses and turns around."
            the_person "What? Oh! Oh my god!"
            "You hold out her wallet for her and she takes it back."
            the_person "Thank you so much, I really need to..."
            "She glances over her shoulder, and the two of you watch as her bus pulls away. She sighs."
            the_person "Well never mind, I guess I have some time. Thank you."
            mc.name "No problem, I'd do it for anyone."

            "She holds out her hand to shake yours."
            $ title_choice = get_random_title(the_person)
            $ the_person.set_title(title_choice)
            $ the_person.set_possessive_title(get_random_possessive_title(the_person))
            the_person "Thank you so much. I'm [the_person.title]."
            call person_introduction(the_person, girl_introduction = False) from _call_person_introduction_1_override
            "You shake her hand. You and [the_person.title] chat while she waits for the next bus to come by."
            $ the_person.change_happiness(10)
            $ the_person.change_love(8)
            "When it does she gives you a quick hug."
            the_person "Thank you again, you've saved my whole day. Maybe we'll see each other again."
            mc.name "I'd like that."
            "She smiles and steps onto the bus, waving briefly from one of the windows."


        "Keep the cash\n{color=#0F0}+$200{/color}":
            $ mc.business.change_funds(200)
            # $ mc.business.listener_system.fire_event("side_money", count = 200)
            "You slip the cash out of the woman's wallet and watch as she rushes to catch her bus."
            $ clear_scene()
            "She gets on and the bus pulls away. When you pass a mailbox you slide the wallet inside - at least she'll get it back."
            $ the_person.remove_person_from_game()


    return
