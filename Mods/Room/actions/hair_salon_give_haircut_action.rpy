# Mall hair salon mod by Trollden.
# Do whatever you want with it.

init 2 python:
    salon_style_cost = int(60)
    salon_dye_cost = int(30)

    salon_total_cost = salon_style_cost + salon_dye_cost

label salon_label():
    "Select who the appointment is for."
    $ tuple_list = known_people_in_the_game([mc]) + ["Back"]
    call screen person_choice(tuple_list, draw_hearts = True)
    $ person_choice = _return

    if person_choice != "Back":
        "You send a message to [person_choice.name] about the appointment."
        "After some time you get a response..."
        call salon_response(person_choice) from _call_salon_response# What to do if "Back" was not the choice taken.
    return # Where to go if you hit "Back".

label salon_response(person_choice): # How does the_person respond to a company paid haircut?
    $ person = person_choice
    $ person.draw_person()

    python:
        hair_style_check = person.hair_style #If hair_style_check is different than person.hair_style it means a "purchase" has been made.
        hair_color_check = person.hair_colour

    # Add responses here: Currently just placeholders.
    # We don't need repsonse that vary by sluttiness / obedience anymore
    # they are covered by the new title system.
    # so start with the exceptions and run down to the default response.

    if person.personality.personality_type_prefix == "bimbo":
        $ person.draw_person(emotion = "happy")
        person.char "Oh, [person.mc_title], like, I love doing my hair."

    elif person.love > 30:
        $ person.draw_person(emotion = "happy")
        person.char "Thanks for the attention, [person.mc_title]."

    elif person.obedience < 80 or person.happiness < 100:
        $ person.draw_person(emotion = "sad")
        person.char "I'm not in the mood for a haircut right now."
        $ person.change_obedience(-2)
        $ person.change_happiness(-2)
        $renpy.scene("Active")
        return

    elif person.happiness > 120 or person.obedience > 120:
        person.char "Yes, [person.mc_title]. I am on my way."
    else:
        person.char "Sounds good, I'll be right there [person.mc_title]."

    call screen hair_creator(person, hair_style_check, hair_color_check) # This is the "store" / "salon" part of the mod. TODO: Find a different way to check for changes in hair color
    call salon_checkout() from _call_salon_checkout #Will return here if nothing qualifies
    call advance_time from _call_advance_time_hair_salon
    $ renpy.scene("Active")
    return

label salon_checkout():
    # Check if any changes was made before leaving.
    if hair_style_check != person.hair_style and hair_color_check[1] != person.hair_colour[1]: # Both was changed
        $ salon_manager.draw_person(emotion = "happy")
        $ person.change_happiness(+10)
        salon_manager.char "That will be $[salon_style_cost] for the haircut and $[salon_dye_cost] for the dye. Who's paying?"
        mc.name "That will be me..."
        $ mc.business.pay(- salon_total_cost)
        "You complete the transaction and $[salon_total_cost] has been deducted from the company's credit card."
    elif hair_style_check != person.hair_style: # Only the hair_style was changed.
        $ salon_manager.draw_person(emotion = "happy")
        $ person.change_happiness(+5)
        salon_manager.char "That will be $[salon_style_cost] for the haircut. Who's paying?"
        mc.name "That will be me..."
        $ mc.business.pay(- salon_style_cost)
        "You complete the transaction and $[salon_style_cost] has been deducted from the company's credit card."
    elif hair_color_check != person.hair_colour:
        $ salon_manager.draw_person(emotion = "happy")
        $ person.change_happiness(+5)
        salon_manager.char "That will be $[salon_dye_cost] for the dye. Who's paying?"
        mc.name "That will be me..."
        $ mc.business.pay(- salon_dye_cost)
        "You complete the transaction and $[salon_dye_cost] has been deducted from the company's credit card."
    else:
        $ person.change_happiness(-5)
        $ person.draw_person(emotion = "angry")
        if person.happiness < 100:
            person.char "What a waste of my time, [person.mc_title]!"
        else:
            person.char "Did you call me over here for nothing, [person.mc_title]!?"
    return
