init -2 python:
    gym_session_cost = 40

init 2 python:
    #Create Gym Outfits
    gym_clothes = Outfit("Gym Clothes")
    gym_clothes.add_lower(panties.get_copy(),colour_black)
    gym_clothes.add_upper(sports_bra.get_copy(),colour_pink)
    gym_clothes.add_upper(tanktop.get_copy(),colour_pink)
    gym_clothes.add_lower(leggings.get_copy(),colour_pink)
    gym_clothes.add_feet(sneakers.get_copy(),colour_white)

    gym_clothes_sexy = Outfit("Sexy Gym Clothes")
    gym_clothes_sexy.add_lower(tiny_g_string.get_copy(),colour_black)
    gym_clothes_sexy.add_upper(sports_bra.get_copy(),colour_pink)
    gym_clothes_sexy.add_lower(booty_shorts.get_copy(),colour_pink)
    gym_clothes_sexy.add_feet(sneakers.get_copy(),colour_white)

label train_in_gym(person):
    python:
        change_scene_display(gym)
        if person.sluttiness > 40 or person.arousal > 35:
            person.outfit = gym_clothes_sexy.get_copy()
        else:
            person.outfit = gym_clothes.get_copy()
        person.draw_person(emotion="default")
        change = renpy.random.random() * 4 # Maximum change is 4 pounds

    if change < 1:
        "You decide to take a yoga class with [person.possessive_title]."
        person.char "This stretching is good my flexibilty."
        if person.sluttiness > 20:
            $ person.draw_person(emotion="happy")
            "There is a subtle undertone in that remark that makes you smile."
    elif change < 2.5:
        "You and [person.possessive_title] spend a few hours working out."
    else:
        "You put [person.possessive_title] through a vigorous training session."
        if person.sluttiness > 20:
            $ person.draw_person(emotion = "angry")
            person.char "It seems you have plans with my body, [person.mc_title]."
            "If she only knew what dirty things you have her doing in your mind."

    $ body_changed = person.change_weight(-change, 100)
    $ new_weight = get_person_weight_string(person)

    "After the session [person.possessive_title] weighs [new_weight]."

    if body_changed:
        $ person.draw_person(person.body_type)
        $ person.change_stats(happiness = 10, love = 5, arousal = 25, slut_temp = 5)
        if person.sluttiness > 20:
            person.char "Wow, these gym sessions make me feel just great, somehow I get turned on too... would you mind?"
            menu:
                "Have Sex" if mc.current_stamina > 0:
                    mc.name "Lets go to the shower room."
                    person.char "Lead the way, [person.mc_title]."
                    $ change_scene_display(gym_shower)

                    call fuck_person(person) from _call_fuck_person_gym_training

                "Have Sex (disabled)\n {size=22}Requires: Stamina{/size}" if not mc.current_stamina > 0:
                    pass
                "Another Time":
                    mc.name "Sorry [person.title], another time."
                    $ person.change_happiness(-10)
        else:
            person.char "Amazing, these gym session are really paying off."
    person.char "Thank you, [person.mc_title]."
    mc.name "Bye [person.title], see you next time."

    $ person.draw_person(position="walking_away")
    
    $ mc.business.pay(-gym_session_cost)
    "You pay for the gym session and $ [gym_session_cost] has been deducted from the company's credit card."

    $ person.reset_arousal()
    $ person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(gym)
    return
