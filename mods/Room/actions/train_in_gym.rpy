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

label train_in_gym(the_person):
    $ change_scene_display(gym)
    show screen person_info_ui(the_person)

    if the_person.sluttiness > 40 or the_person.arousal > 35:
        $ the_person.outfit = gym_clothes_sexy.get_copy()
    else:
        $ the_person.outfit = gym_clothes.get_copy()
    $ the_person.draw_person()

    $ change = renpy.random.random() * 4 # Maximum change is 4 kg
    $ body_changed = change_person_weight(the_person, -change, 100)
    $ new_weight = get_person_weight_string(the_person)

    "After the training session [the_person.name] weighs [new_weight] kg."

    if body_changed:
        $ the_person.draw_person(the_person.body_type)
        $ the_person.change_happiness(+10)
        $ the_person.change_love(+5)
        $ slut_report = the_person.change_slut_temp(5)
        the_person.char "Wow, i'm really feeling healthier now, and a little turned on...would you mind?"
        if the_person.sluttiness > 10:
            menu:
                "Have Sex" if mc.current_stamina > 0:
                    mc.name "Lets go to the shower room."
                    the_person.char "Lead the way, [mc.name]."
                    $ change_scene_display(gym_shower)

                    call fuck_person(the_person) from _call_fuck_person_gym_training

                    $ the_person.reset_arousal()
                "Have Sex (disabled)" if not mc.current_stamina > 0:
                    pass
                "Another Time":
                    mc.name "Sorry [the_person.name], another time."
                    $ the_person.change_happiness(-10)

    the_person.char "Thank you, [mc.name]."
    mc.name "Bye [the_person.name], see you next time."

    $ mc.business.funds -= 40

    hide screen person_info_ui
    $ the_person.reset_outfit() #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return
