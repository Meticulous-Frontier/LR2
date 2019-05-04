# Mall hair salon mod by Trollden.
# Do whatever you want with it.
# Initialization segment - Start

init 2 python:
    salon_style_cost = int(60)
    salon_dye_cost = int(30)

    salon_total_cost = salon_style_cost + salon_dye_cost

    def create_salon_manager():
        # Wardrobe for employees in the salon
        salon_wardrobe = wardrobe_from_xml("Salon_Wardrobe")
        global salon_manager
        salon_manager = create_random_person(name = "Ophelia", last_name = "von Friseur", height = .9, age = renpy.random.randint(21,30), body_type = "thin_body",
            personality = wild_personality, job = "Hair Stylist", starting_wardrobe = salon_wardrobe, eyes="blue", start_sluttiness = 10,
            title = "Ophelia", possessive_title = "My stylist", mc_title = mc.name)

        # We want whoever the salon_manager is to be in the salon during work hours.
        salon_manager.schedule[1] = mall_salon
        salon_manager.schedule[2] = mall_salon
        salon_manager.schedule[3] = mall_salon
        return

    def salon_requirement():
        if day%7 == 6: # Can be removed
            return "Closed on Sundays."

        elif time_of_day == 1:
            return "Opens in the morning."

        elif time_of_day == 4: # Can be removed
            return "Closed for the night."

        elif mc.business.funds < 100: # $60 for hair cut, $30 for dye. You wont be spending your last money on haircuts.
            return "Not enough funds."
        else:
            return True

    def hair_salon_mod_initialization(self):
        # Always check if the room is somehow already added.
        # Enables the elevator.
        if mall_salon not in mod_rooms_mall:
            mod_rooms_mall.append(mall_salon)

        # Always check if the action is somehow already added.
        # Enables the salon_action for the salon.
        if salon_action not in mall_salon.actions:
            mall_salon.actions.append(self)

        # I want to enable NPC pathing
        if mall_salon not in list_of_places:
            # Place the character so it is in a room in the world.
            create_salon_manager()
            salon_manager.special_role.append(salon_manager_role)
            mall_salon.add_person(salon_manager)
            # Add to map
            list_of_places.append(mall_salon)
            mall_salon.link_locations_two_way(mall)
        return


    salon_action = ActionMod("Schedule a haircut", salon_requirement, "salon_label", initialization = hair_salon_mod_initialization,
        menu_tooltip = "Change a persons hair style and color.", category="Mall")

# Initilization segment - End

label salon_label():
    $ renpy.scene("Active")

#    python:

#    # Run an update in case of new characters in the world. NOTE: See if Vren make changes to how roles are displayed.
#        for room in list_of_places:                               I want unnamed roles to be invisible.
#            for person in room.people:
#                if salon_patron not in person.special_role:
#                    person.special_role.append(salon_patron)


    "Select who the appointment is for."
    python: # First we select which employee we want
        tuple_list = format_person_list(all_people_in_the_game([mc]), draw_hearts = True)  #The list of people to show. e.g mc.location.people
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

        if person_choice == "Back":
            renpy.jump("game_loop") # Where to go if you hit "Back".
            renpy.scene("Active") # Had a rare occurence of a person being drawn although no choice being made.
        else:
            renpy.say("","You send a message to " + person_choice.name + " about the appointment.") #Add flavor text to what is about to happen. e.g "You tell the_person to go visit Starbuck for training".
            renpy.say("", "After some time you get a response...")

    call salon_response(person_choice)# What to do if "Back" was not the choice taken.
    jump game_loop # Return to the game_loop or a label that will bring you back to the game loop

label salon_response(person_choice): # How does the_person respond to a company paid haircut?
    $ person = person_choice
    $ person.draw_person()

    python:
        hair_style_check = person.hair_style #If hair_style_check is different than person.hair_style it means a "purchase" has been made.
        hair_color_check = person.hair_colour

    # $ hair_style_request = get_random_from_list(hair_styles)
    # $ hair_color_request = get_random_hair_colour()

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

    call screen hair_creator(person) # This is the "store" / "salon" part of the mod. TODO: Find a different way to check for changes in hair color
    $renpy.scene("Active")
    call salon_checkout() #Will return here if nothing qualifies
    $renpy.scene("Active")
    return


label salon_checkout():
    # Check if any changes was made before leaving.
    if hair_style_check != person.hair_style and hair_color_check != person.hair_colour: # Both was changed
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
        $ mc.business.pay (- salon_style_cost)
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
