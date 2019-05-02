# Business Basement Rooms is a proof of concept on best practises for adding rooms to the game via the Room Manager.
# Requires the Room Manager.rpy to be present for it to work as intended.
# Adds a basement section accessable via the business lobby.

# name,formalName,connections,background_image,objects,people,actions,public,map_pos, tutorial_label = None, visible = True)
init -1 python:
    business_basement = [] # List of rooms that are supposed to be in the basement.

init 5  python:
    add_label_hijack("normal_start", "store_basement_rooms")
label store_basement_rooms(stack):
    python:
        m_division_basement = Room("security", "Security Room", [], room_background_image("Security_Background.jpg"), [],[],[], False, [], None, False)
        p_division_basement = Room("machinery", "Machinery Room", [], office_background, [], [], [], False, [], None, False)
        rd_division_basement = Room("biotech", "Biotechnology Lab", [], room_background_image("Biotech_Background.jpg"), [], [], [], False, [], None, False)
        office_basement = Room("dungeon", "Dungeon", [], bar_background, [],[],[], False,[], None, False)

    #    room = Room("", "", [], background_image, [], [], [], False, [], None, False)

        business_basement.append(m_division_basement) # I collect the rooms into a list to make appending easier later.
        business_basement.append(p_division_basement)
        business_basement.append(rd_division_basement)
        business_basement.append(office_basement)

    #    for room in business_basement: # These rooms should become accessable through gameplay.
    #        room.accessable = True


    #    for room in business_basement: # I want all of the rooms in the basement to be accessable from the business lobby.
                                       # Modifications and further pathways can be altered later, if I for example want to install a direct elevator into the main office and into the dungeon.
    #        if room not in mod_rooms_lobby:
    #            mod_rooms_lobby.append(room)

        for room in business_basement:
            if object not in room.objects:
                m_division_basement.add_object(make_desk())
                m_division_basement.add_object(make_chair())
                m_division_basement.add_object(make_floor())

                p_division_basement.add_object(make_table())

                rd_division_basement.add_object(make_chair())
                rd_division_basement.add_object(make_floor())
                rd_division_basement.add_object(make_desk())
                rd_division_basement.add_object(make_table())

                office_basement.add_object(make_bed())
    $ execute_hijack_call(stack)
    return
