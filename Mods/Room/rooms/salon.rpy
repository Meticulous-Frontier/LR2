init 2 python: # Declare variables to use

     # Note that the class Room have a bunch of useful variables already for restricting access, adding objects etc.

    def salon_requirement():
        if day%7 == 6: # Can be removed
            return "Closed on Sundays."

        elif time_of_day == 0:
            return "Opens in the morning."

        elif time_of_day == 4: # Can be removed
            return "Closed for the night."

        elif mc.business.funds < 100: # $60 for hair cut, $30 for dye. You wont be spending your last money on haircuts.
            return "Requires $90."
        else:
            return True

    def hair_salon_mod_initialization(self):
        # Place the stylist character so it is in a room in the world.
        create_salon_manager()

        salon_manager.special_role.append(salon_manager_role)
        salon_manager.on_room_enter_event_list.append(salon_introduction_action)

        mall_salon.add_person(salon_manager)
        # Add to map
        list_of_places.append(mall_salon)
        mall_salon.link_locations_two_way(mall)
        return

    def salon_introduction_action_requirement(the_person):
        if mc.location == mall_salon:    # only trigger event when in hair salon
            return True
        return False

    salon_action = ActionMod("Schedule a haircut", salon_requirement, "salon_label", initialization = hair_salon_mod_initialization,
        menu_tooltip = "Change a persons hair style and color.", category="Mall")

    salon_introduction_action = Action("Ophelia's Hair Salon", salon_introduction_action_requirement, "hair_salon_greeting", menu_tooltip = "Ophelia's Hair Salon")

    # Create the room(s) I want to use.
    mall_salon = Room("salon", "Hair Salon", [], room_background_image("Salon_Background.jpg"), [make_floor(), make_wall(), make_chair(), make_window()], [], [salon_action], True, [7,2], None, True)
 
label hair_salon_greeting(the_person):
    $ the_person = salon_manager

    show screen person_info_ui(the_person)
    $ the_person.draw_person(emotion = "happy")

    if the_person.mc_title == "Stranger":
        "You enter the hair salon. A beautiful young woman walks up to you and introduces herself."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        the_person.char "Hello there sir! Welcome to the Sweet Pixie Salon!"

        # uses parts of the in-game introduction sequence tailored to SB
        if the_person.title is None:
            mc.name "Hey, there."
            $ title_choice = get_random_title(the_person)
            $ formatted_title = the_person.create_formatted_title(title_choice)
            the_person.char "I am [formatted_title], top stylist and owner."
            $ the_person.set_title(title_choice)
            $ the_person.set_possessive_title(get_random_possessive_title(the_person))
            "She holds her hand out to shake yours."
            the_person.char "And how may I call you?"
            $ title_tuple = []
            $ title_choice = None
            python:
                for title in get_player_titles(the_person):
                    title_tuple.append([title,title])

            $ title_choice = renpy.display_menu(title_tuple,True,"Choice")
            mc.name "[title_choice], nice to meet you."
            $ the_person.set_mc_title(title_choice)

        the_person.char "I've just opened, so what can I do for you today? A wash or a trim? A shave perhaps?"
        mc.name "Nothing like that today, I own a company downtown."
        mc.name "My employees need to look perfect and I want to pay for their expenses, is that possible?"
        the_person.char "No problem, just give me your credit card details and I will charge it whenever you sent someone by."
        "You smile at [the_person.name] and hand over your company credit card."
        the_person.char "Perfect! All done."
    else:
        the_person.char "Hey there, [the_person.mc_title]! Its good to see you!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title] smiles playfully."
            the_person.char "I was just thinking about you. Anything I can do for you today?"
        else:
            the_person.char "Is there anything I can help you with?"

    # readd the event to the room list, so she will keep greeting you when you walk in
    $ salon_manager.on_room_enter_event_list.append(salon_introduction_action)

    $ renpy.scene("Active")
    hide screen person_info_ui
    return
