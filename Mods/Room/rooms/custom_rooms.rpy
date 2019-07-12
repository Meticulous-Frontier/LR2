# Business Basement Rooms is a proof of concept on best practises for adding rooms to the game via the Room Manager.
# Requires the Room Manager.rpy to be present for it to work as intended.
# Adds a basement section accessable via the business lobby.

# name,formalName,connections,background_image,objects,people,actions,public,map_pos, tutorial_label = None, visible = True)
init -1 python:
    business_basement = [] # List of rooms that are supposed to be in the basement.
    
    def update_custom_rooms(room): # Replaces the room in the list with the updated version.
        room_update = find_in_list(lambda x: x.name == room.name, list_of_places)

        # did not find a room to update
        if not room_update:
            return

        # renpy.say("", "Update room " + room_update.name)

        room_update.formalName = room.formalName
        
        room_update.map_pos = room.map_pos
        room_update.background_image = room.background_image
        
        room_update.visible = room.visible
        room_update.accessable = room.accessable

        room_update.connections = room.connections

        room_update.objects = room.objects
        room_update.objects.append(Object("stand",["Stand"], sluttiness_modifier = 0, obedience_modifier = -5)) #Add a standing position that you can always use.

        # update available actions in room
        room_update.actions = room.actions
        
        if room_update.tutorial_label != room.tutorial_label:        
            room_update.tutorial_label = room.tutorial_label
            room_update.trigger_tutorial = True

        # old saves don't have hide_in_known_housemap
        if hasattr(room_update, "hide_in_known_housemap"): # Deal with this somehow else. Thought ModRooms should have the attribute as True by default?
            room_update.hide_in_known_housemap = room.hide_in_known_housemap

        return

init 5  python:
    add_label_hijack("normal_start", "activate_custom_rooms")
    add_label_hijack("after_load", "update_custom_rooms")

label activate_custom_rooms(stack):
    
    call store_m_division_basement() from _store_m_division_basement_1
    call store_p_division_basement() from _store_p_division_basement_1
    call store_rd_division_basement() from _store_rd_division_basement_1
    call store_office_basement() from _store_office_basement_1
    call store_downtown_bar() from _call_store_downtown_bar_1
   
    $ execute_hijack_call(stack)
    return

label update_custom_rooms(stack):
    # use this code to add only a new missing room
    # if not find_in_list(lambda x: x.name == "downtown_bar", list_of_places):
    #     call update_downtown_bar() from _call_update_downtown_bar

    call store_m_division_basement() from _store_m_division_basement_2
    call store_p_division_basement() from _store_p_division_basement_2
    call store_rd_division_basement() from _store_rd_division_basement_2
    call store_office_basement() from _store_office_basement_2
    call store_downtown_bar() from _call_store_downtown_bar_2
    
    $ execute_hijack_call(stack)
    return


    
label store_m_division_basement():
    # Marketing Division Basement - Security Room | security_room_actions.rpy
    $ m_division_basement_objects = [
        make_desk(),
        make_chair(),
        make_floor()
    ]

    $ m_division_basement = Room("security", "Security Room", [m_division], room_background_image("Security_Background.jpg"), m_division_basement_objects,[],[security_overview_action], False, [12,2], None, True)
    
    $ update_custom_rooms(m_division_basement) 
    return

label store_p_division_basement():
    # Production Division Basement - Machinery Room | machinery_room_actions.rpy

    $ p_division_basement_objects = [
        make_table()
    ]

    $ p_division_basement = Room("machinery", "Machinery Room", [p_division], office_background, p_division_basement_objects, [], [], False, [10,5], None, True)
    
    $ update_custom_rooms(p_division_basement) 
    return
    
label store_rd_division_basement():
    # Research Division Basement - Biotechnology Lab | biotech_room_actions.rpy
    $ rd_division_basement_objects = [
        make_chair(),
        make_floor(),
        make_desk(),
        make_table()
    ]

    $ rd_division_basement = Room("biotech", "Biotechnology Lab", [rd_division], room_background_image("Biotech_Background.jpg"), rd_division_basement_objects, [], [biotech_lab_action], False, [13,4], None, True)    
    
    $ update_custom_rooms(rd_division_basement)
    return

label store_office_basement():
    # Main Office Basement - Dungeon | dungeon_room_actions.rpy
    $ office_basement_objects = [
        make_bdsmbed(),
        make_pillory(),
        make_woodhorse()
    ]
    $ office_basement = Room("dungeon", "Dungeon", [office], bar_background, office_basement_objects, [],[dungeon_action], False,[10,2], None, True)
    
    $ update_custom_rooms(office_basement) 
    return

label store_downtown_bar():
    # Downtown Bar - The Downtown Distillery | downtown_bar_actions.rpy
    # This bar gets updated when a save game is loaded, regardsless of its existance

    python:
        downtown_bar_objects = [
            make_desk(),
            make_chair(),
            make_floor()
        ]
        downtown_bar = Room("bar", "The Downtown Distillery", [downtown], bar_background, downtown_bar_objects,[], [downtown_bar_action], True, [6,5], None, True)

    # Make sure it is in the list_of_places (and no duplicate)
    # List of places gets stored, so will the bar when appended here
    if downtown_bar not in list_of_places: 
        $ list_of_places.append(downtown_bar)
    
    # This refreshes the properties of the existing bar, e.g move the position of the Room on the map, objects, actions, connections, background etc.
    $ update_custom_rooms(downtown_bar) 

    return
