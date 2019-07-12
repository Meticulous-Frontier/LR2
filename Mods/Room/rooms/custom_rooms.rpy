# Business Basement Rooms is a proof of concept on best practises for adding rooms to the game via the Room Manager.
# Requires the Room Manager.rpy to be present for it to work as intended.
# Adds a basement section accessable via the business lobby.

# name,formalName,connections,background_image,objects,people,actions,public,map_pos, tutorial_label = None, visible = True)
init -1 python:
    business_basement = [] # List of rooms that are supposed to be in the basement.
    
    def update_custom_rooms(room): # Replaces the room in the list with the updated version.
        for i in range(len(list_of_places)):
            if list_of_places[i] == room:
                
                list_of_places[i].formalName = room.formalName
                
                list_of_places[i].map_pos = room.map_pos
                list_of_places[i].background_image = room.background_image
                
                list_of_places[i].visible = room.visible
                list_of_places[i].accessable = room.accessable
                
                if hasattr(list_of_places[i], "hide_in_known_housemap"): # Deal with this somehow else. Thought ModRooms should have the attribute as True by default?
                    list_of_places[i].hide_in_known_housemap = room.hide_in_known_housemap
                
                if hasattr(list_of_places[i], "tutorial_label"):
                    list_of_places[i].tutorial_label = room.tutorial_label
                    renpy.call(room.tutorial_label)
                if hasattr(list_of_places[i], "trigger_tutorial"):
                    list_of_places[i].trigger_tutorial = room.trigger_tutorial
                   
        
        return

init 5  python:
    add_label_hijack("normal_start", "store_custom_rooms")
    add_label_hijack("after_load", "update_custom_rooms")

label update_custom_rooms(stack):

    if "downtown_bar" not in globals(): # After pushing room additions, update this to latest so it gets added on existing saves, or any non- existing global var e.g "just_update_damnit"
        call store_custom_rooms(stack)
    $ execute_hijack_call(stack)
    return



label store_custom_rooms(stack):
    
    # Marketing Division Basement - Security Room | security_room_actions.rpy
    $ m_division_basement_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
        ]

    $ m_division_basement = ModRoom("security", "Security Room", [], room_background_image("Security_Background.jpg"), m_division_basement_objects,[],[], False, [], None, False)
    
    # Production Division Basement - Machinery Room | machinery_room_actions.rpy
    $ p_division_basement_objects = [
        make_table()
        ]

    $ p_division_basement = ModRoom("machinery", "Machinery Room", [], office_background, p_division_basement_objects, [], [], False, [], None, False)
    
    # Research Division Basement - Biotechnology Lab | biotech_room_actions.rpy
    $ rd_division_basement_objects = [
        make_chair(),
        make_floor(),
        make_desk(),
        make_table()
    ]

    $ rd_division_basement = ModRoom("biotech", "Biotechnology Lab", [], room_background_image("Biotech_Background.jpg"), rd_division_basement_objects, [], [], False, [], None, False)
    
    # Main Office Basement - Dungeon | dungeon_room_actions.rpy
    $ office_basement_objects = [
        make_bdsmbed(),
        make_pillory(),
        make_woodhorse()
    ]
    $ office_basement = ModRoom("dungeon", "Dungeon", [], bar_background, office_basement_objects, [],[], False,[], None, False)

    $ business_basement = [ # List of rooms to put in the "basement" of the business
        m_division_basement,
        p_division_basement,
        rd_division_basement,
        office_basement
    ]

    # Downtown Bar - The Downtown Distillery | downtown_bar_actions.rpy
    $ downtown_bar_objects = [
        make_desk(),
        make_chair(),
        make_floor()
    ]
    $ downtown_bar = ModRoom("bar", "The Downtown Distillery", [downtown], bar_background, downtown_bar_objects,[],[], True, [6,5], "downtown_bar_enable_actions", True)
    
    if downtown_bar not in list_of_places: # Make sure it is in the list_of_places.
        $ list_of_places.append(downtown_bar)
    $ update_custom_rooms(downtown_bar) # This refreshes any properties, e.g move the position of the Room on the map.
  
 
    $ execute_hijack_call(stack)
    return
