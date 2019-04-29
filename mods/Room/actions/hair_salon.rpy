# Mall hair salon mod by Trollden.
# Do whatever you want with it.
# Initialization segment - Start

init 2 python:
    def create_salon_manager():
        # Wardrobe for employees in the salon
        salon_wardrobe = wardrobe_from_xml("Salon_Wardrobe")
        global salon_manager
        salon_manager = create_random_person(age = renpy.random.randint(21,30), body_type = "thin_body", personality = wild_personality, job = "Hair Stylist", starting_wardrobe = salon_wardrobe)

        # We want whoever the salon_manager is to be in the salon during work hours.
        salon_manager.schedule[1] = mall_salon
        salon_manager.schedule[2] = mall_salon
        salon_manager.schedule[3] = mall_salon
        return

    def salon_requirement():
        if time_of_day == 4: # Can be removed
            return "Closed for the night."

        elif day%7 == 6: # Can be removed
            return "Closed on Sundays."

        elif mc.business.funds < 100: # $60 for hair cut, $30 for dye. You wont be spending your last money on haircuts.
            return "Not enough funds."
        else:
            return True
    
    def hair_salon_mod_initialization(self):
        create_salon_manager()
        # Place the character so it is in a room in the world.
        mall_salon.add_person(salon_manager)
        salon_manager.special_role.append(salon_manager_role)   

        # Always check if the room is somehow already added.
        # Enables the elevator.
        if mall_salon not in mod_rooms_mall:
            mod_rooms_mall.append(mall_salon)

        # Always check if the action is somehow already added.
        # Enables the salon_action for the salon.
        if salon_action not in mall_salon.actions:
            mall_salon.actions.append(self.action)

        # I want to enable NPC pathing
        if mall_salon not in list_of_places:
            list_of_places.append(mall_salon)
            mall_salon.link_locations_two_way(mall)
        return


    salon_action = Mod("Schedule a haircut", salon_requirement, "salon_label", initialization = hair_salon_mod_initialization, menu_tooltip = "Change a persons hair style and color.")

# Initilization segment - End

label salon_label():

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
            else:
                renpy.say("","You send a message to " + person_choice.name + " about the appointment.") #Add flavor text to what is about to happen. e.g "You tell the_person to go visit Starbuck for training".
                renpy.say("", "After some time you get a response...")

    call salon_response(person_choice)# What to do if "Back" was not the choice taken.
    jump game_loop # Return to the game_loop or a label that will bring you back to the game loop

label salon_response(person_choice): # How does the_person respond to a company paid haircut?
    $ the_person = person_choice
    $ the_person.draw_person()
    $ hair_style_request = get_random_from_list(hair_styles)
    $ hair_color_request = get_random_hair_colour()

    # Add responses here: Currently just placeholders.

    if the_person.obedience > 120:
        the_person.name "Yes, Sir. I am on my way."
        pass

    elif the_person.sluttiness > 30:
        the_person.name "Yes, Sir. I am on my way."
        pass

    elif the_person.sluttiness > the_person.obedience:
        the_person.name "Yes, Sir. I am on my way."
        pass

    elif the_person.personality.personality_type_prefix == "bimbo":
        the_person.name "I'm a bimbo, cool."
        pass

    elif the_person.happiness < 100 and the_person.love > 20:

        $ the_person.draw_person(emotion = "happy")

        the_person.name "Thanks for the attention, [mc.name]."

        pass

    elif the_person.happiness < 100:
        $ the_person.draw_person(emotion = "sad")
        the_person.name "I'm not in the mood for a haircut right now."
        $ the_person.change_obedience(-2)
        $renpy.scene("Active")
        return
    else:
        the_person.name "Sounds good, I'll be right there [mc.name]."
        pass
    # End of respones

    call hair_style(the_person) # This is the "store" / "salon" part of the mod.



label salon_checkout():



    # Check if any changes was made before leaving.
    if hair_style_check != the_person.hair_style and hair_color_check != the_person.hair_colour: # Both was changed
        $ the_person.change_happiness(+10)

        $ salon_manager.draw_person(emotion = "happy")
        salon_manager.name "That will be $[salon_style_cost] for the haircut and $[salon_dye_cost] for the dye. Who's paying?"

        mc.name "That will be me..."

        $ mc.business.funds -= salon_total_cost
        "You complete the transaction and $[salon_total_cost] has been deducted from the company's card"
        pass

    elif hair_style_check != the_person.hair_style: # Only the hair_style was changed.
        $ the_person.change_happiness(+5)

        $ salon_manager.draw_person(emotion = "happy")
        salon_manager.name "That will be $[salon_style_cost] for the haircut. Who's paying?"

        mc.name "That will be me..."

        $ mc.business.funds -= salon_style_cost
        "You complete the transaction and $[salon_style_cost] has been deducted from the company's card"
        pass

    elif hair_color_check != the_person.hair_colour:
        $ the_person.change_happiness(+5)

        $ salon_manager.draw_person(emotion = "happy")
        salon_manager.name "That will be $[salon_dye_cost] for the dye. Who's paying?"
        mc.name "That will be me..."

        $ mc.business.funds -= salon_dye_cost
        "You complete the transaction and $[salon_dye_cost] has been deducted from the company's card"
        pass

    else:
        $ the_person.change_happiness(-5)
        $ the_person.draw_person(emotion = "angry")

        the_person.name "Did you call me over here for nothing!?"

    return
