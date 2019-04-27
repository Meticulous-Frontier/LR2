init -1 python: # Declare variables to use

    # Create the room(s) I want to use.
    mall_salon = Room("salon", "Hair Salon", [], room_background_image("Salon_Background.png"), [], [], [], True, [0.4,0.3], None, True)
    business_salon = Room("salon", "Hair Salon", [], room_background_image("Salon_Background.png"), [], [], [], True, [], None, False)

    # Note that the class Room have a bunch of useful variables already for restricting access, adding objects etc.

init 2 python: # Room creation

    # Wardrobe for employees in the salon
    salon_wardrobe = wardrobe_from_xml("Salon_Wardrobe")


    # Always check if the room or action is somehow added already before proceeding.
    # I want the Elevator to be accessable.
    if mall_salon not in mod_rooms_mall:
        mod_rooms_mall.append(mall_salon)

    # I want to enter it from the mall.
    if mall_salon not in mod_rooms_append:
        mod_rooms_append.append(mall_salon)

    if object not in mall_salon.objects:
        mall_salon.add_object(make_floor())
        mall_salon.add_object(make_wall())
        mall_salon.add_object(make_chair())
        mall_salon.add_object(make_desk())
        mall_salon.add_object(make_table())
        mall_salon.add_object(make_window())


