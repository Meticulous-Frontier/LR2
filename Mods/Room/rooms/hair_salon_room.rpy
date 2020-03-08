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
        # Wardrobe for employees in the salon
        salon_wardrobe = wardrobe_from_xml("Salon_Wardrobe")

        # Place the stylist character so it is in a room in the world.
        global salon_manager

        salon_manager = make_person(name = "Ophelia", last_name = "von Friseur", height = .9, age = renpy.random.randint(21,30), body_type = "thin_body",
            personality =  None if not "salon_manager_personality" in globals() else salon_manager_personality, job = "Hair Stylist", starting_wardrobe = salon_wardrobe, eyes="light blue", start_sluttiness = 10,
            possessive_title = "My stylist", force_random = True)

        if "salon_manager_role" in globals():
            salon_manager.special_role.append(salon_manager_role)

        if "salon_manager_personality" in globals():
            salon_manager.on_room_enter_event_list.append(salon_introduction_action)

        # create home for salon manager
        salon_manager.generate_home()            

        # We want whoever the salon_manager is to be in the salon during work hours.
        salon_manager.set_schedule([0,4], salon_manager.home)
        salon_manager.set_schedule([1,2,3], mall_salon)

        # Add to mall
        mall_salon.add_person(salon_manager)
        # Add to map
        list_of_places.append(mall_salon)
        mall_salon.link_locations_two_way(mall)
        return

    def salon_introduction_action_requirement(the_person):
        if mc.location == mall_salon:    # only trigger event when in hair salon
            return True
        return False

    salon_action = ActionMod("Schedule a haircut {image=gui/heart/Time_Advance.png}", salon_requirement, "salon_label", initialization = hair_salon_mod_initialization,
        menu_tooltip = "Change a persons hair style and color.", category="Mall")

    salon_introduction_action = Action("Ophelia's Hair Salon", salon_introduction_action_requirement, "salon_manager_greetings", menu_tooltip = "Ophelia's Hair Salon")

    # Create the room(s) I want to use.
    mall_salon = Room("salon", "Hair Salon", [], room_background_image("Salon_Background.jpg"), [make_floor(), make_wall(), make_chair(), make_window()], [], [salon_action], True, [7,2], None, True, lighting_conditions = standard_indoor_lighting)
