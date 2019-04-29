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
    $ change_scene_display(gym)
    show screen person_info_ui(person)

    if person.sluttiness > 40 or person.arousal > 35:
        $ person.outfit = gym_clothes_sexy.get_copy()
    else:
        $ person.outfit = gym_clothes.get_copy()
    $ person.draw_person()

    $ change = renpy.random.random() * 4 # Maximum change is 4 kg

    if change < 2:
        "You and [person.name] spend a few hours working out."
    else:
        "You put [person.name] through a vigorous training session."

    $ body_changed = person.change_weight(-change, 100)
    $ new_weight = get_person_weight_string(person)

    "After the training session [person.name] weighs [new_weight] lbs."

    if body_changed:
        $ person.draw_person(person.body_type)
        $ person.change_happiness(+10)
        $ person.change_love(+5)
        $ person.change_arousal(25)
        $ slut_report = person.change_slut_temp(5)
        person.char "Wow, I'm really feeling healthier now, and a little turned on... would you mind?"
        if person.sluttiness > 10:
            menu:
                "Have Sex" if mc.current_stamina > 0:
                    mc.name "Lets go to the shower room."
                    person.char "Lead the way, [mc.name]."
                    $ change_scene_display(gym_shower)

                    call fuck_person(person) from _call_fuck_person_gym_training
                "Have Sex (disabled)\n {size=22}Requires: Stamina{/size}" if not mc.current_stamina > 0:
                    pass
                "Another Time":
                    mc.name "Sorry [person.name], another time."
                    $ person.change_happiness(-10)

    $ person.reset_arousal()
    person.char "Thank you, [mc.name]."
    mc.name "Bye [person.name], see you next time."

    $ mc.business.funds -= 40

    hide screen person_info_ui
    $ person.reset_outfit() #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return
