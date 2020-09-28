# Mall hair salon mod by Trollden.
# Do whatever you want with it.

init 2 python:
    salon_style_cost = __builtin__.int(60)
    salon_dye_cost = __builtin__.int(30)

    salon_total_cost = salon_style_cost + salon_dye_cost

label salon_label():
    call screen enhanced_main_choice_display(build_menu_items([get_sorted_people_list(known_people_in_the_game([mc]), "Salon appointment", ["Back"])]))
    $ person_choice = _return

    if person_choice != "Back":
        "You send a message to [person_choice.name] about the appointment."
        "After some time you get a response..."
        call salon_response(person_choice) from _call_salon_response# What to do if "Back" was not the choice taken.
        $ del person_choice
    return # Where to go if you hit "Back".

label salon_response(person_choice): # How does the_person respond to a company paid haircut?
    $ the_person = person_choice
    $ the_person.draw_person()

    # Add responses here: Currently just placeholders.
    # We don't need response that vary by sluttiness / obedience anymore
    # they are covered by the new title system.
    # so start with the exceptions and run down to the default response.

    if the_person.personality.personality_type_prefix == "bimbo":
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Oh, [the_person.mc_title], like, I love doing my hair."

    elif the_person.love > 30:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Thanks for the attention, [the_person.mc_title]."

    elif the_person.obedience < 80 or the_person.happiness < 100:
        $ the_person.draw_person(emotion = "sad")
        the_person.char "I'm not in the mood for a haircut right now."
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-2)
        $renpy.scene("Active")
        return

    elif the_person.happiness > 120 or the_person.obedience > 120:
        the_person.char "Yes, [the_person.mc_title]. I am on my way."
    else:
        the_person.char "Sounds good, I'll be right there [the_person.mc_title]."

    python:
        hair_style_check = the_person.hair_style.get_copy()
        pubes_style_check = the_person.pubes_style.get_copy()

    call screen hair_creator(the_person, hair_style_check, pubes_style_check) # This is the "store" / "salon" part of the mod. TODO: Find a different way to check for changes in hair color
    call salon_checkout() from _call_salon_checkout #Will return here if nothing qualifies
    call advance_time from _call_advance_time_hair_salon
    $ clear_scene()
    return

label salon_checkout():
    # Check if any changes was made before leaving.
    if (hair_style_check != the_person.hair_style and hair_style_check.colour != the_person.hair_style.colour) or (pubes_style_check != the_person.pubes_style and pubes_style_check.colour != the_person.pubes_style.colour): # Both was changed
        $ salon_manager.draw_person(emotion = "happy")
        $ the_person.change_happiness(+10)
        salon_manager.char "That will be $[salon_style_cost] for the haircut and $[salon_dye_cost] for the dye. Who's paying?"
        mc.name "That will be me..."
        $ mc.business.change_funds(- salon_total_cost)
        "You complete the transaction and $[salon_total_cost] has been deducted from the company's credit card."
    elif hair_style_check != the_person.hair_style or pubes_style_check != the_person.pubes_style: # Only the hair_style was changed.
        $ salon_manager.draw_person(emotion = "happy")
        $ the_person.change_happiness(+5)
        salon_manager.char "That will be $[salon_style_cost] for the haircut. Who's paying?"
        mc.name "That will be me..."
        $ mc.business.change_funds(- salon_style_cost)
        "You complete the transaction and $[salon_style_cost] has been deducted from the company's credit card."
    elif hair_style_check.colour != the_person.hair_style.colour or pubes_style_check.colour != the_person.pubes_style.colour:
        $ salon_manager.draw_person(emotion = "happy")
        $ the_person.change_happiness(+5)
        salon_manager.char "That will be $[salon_dye_cost] for the dye. Who's paying?"
        mc.name "That will be me..."
        $ mc.business.change_funds(- salon_dye_cost)
        "You complete the transaction and $[salon_dye_cost] has been deducted from the company's credit card."
    else:
        $ the_person.change_happiness(-5)
        $ the_person.draw_person(emotion = "angry")
        if the_person.happiness < 100:
            the_person.char "What a waste of my time, [the_person.mc_title]!"
        else:
            the_person.char "Did you call me over here for nothing, [the_person.mc_title]!?"
    return
