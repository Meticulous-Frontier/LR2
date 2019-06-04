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
        # I want to enable NPC pathing
        if mall_salon not in list_of_places:
            # Place the stylist character so it is in a room in the world.
            create_salon_manager()
            salon_manager.special_role.append(salon_manager_role)
            mall_salon.add_person(salon_manager)
            # Add to map
            list_of_places.append(mall_salon)
            mall_salon.link_locations_two_way(mall)
        return

    salon_action = ActionMod("Schedule a haircut", salon_requirement, "salon_label", initialization = hair_salon_mod_initialization,
        menu_tooltip = "Change a persons hair style and color.", category="Mall")

    # Create the room(s) I want to use.
    mall_salon = Room("salon", "Hair Salon", [], room_background_image("Salon_Background.jpg"), [make_floor(), make_wall(), make_chair(), make_window()], [], [salon_action], True, [7,2], None, True)
 