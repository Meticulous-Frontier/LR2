# Business Basement Rooms is a proof of concept on best practices for adding rooms to the game via the Room Manager.
# Requires the Room Manager.rpy to be present for it to work as intended.
# Adds a basement section accessible via the business lobby.

# name,formalName,connections,background_image,objects,people,actions,public,map_pos, tutorial_label = None, visible = True)
init -1 python:
    business_basement = [] # List of rooms that are supposed to be in the basement.

init 15 python:
    # Marketing Division Basement - Security Room | security_room_actions.rpy
    m_division_basement_objects = [
        make_desk(),
        make_chair(),
        make_floor()
    ]
    m_division_basement = Room("security", "Security Room", [], room_background_image("Security_Background.jpg"), m_division_basement_objects,[],[security_overview_action], False, [12,2], None, False)

    # Production Division Basement - Machinery Room | machinery_room_actions.rpy
    p_division_basement_objects = [
        make_table()
    ]
    p_division_basement = Room("machinery", "Machinery Room", [], office_background, p_division_basement_objects, [], [machinery_room_action], False, [11,5], None, False)

    # Research Division Basement - Biotechnology Lab | biotech_room_actions.rpy
    rd_division_basement_objects = [
        make_chair(),
        make_floor(),
        make_desk(),
        make_table()
    ]
    rd_division_basement = Room("biotech", "Biotechnology Lab", [], room_background_image("Biotech_Background.jpg"), rd_division_basement_objects, [], [biotech_lab_action], False, [12,5], None, False)

    # Main Office Basement - Dungeon | dungeon_room_actions.rpy
    office_basement_objects = [
        make_bdsmbed(),
        make_pillory(),
        make_woodhorse()
    ]
    office_basement = Room("dungeon", "Dungeon", [], bar_background, office_basement_objects, [],[dungeon_room_action], False,[11,1], None, False)

    # Downtown Bar - The Downtown Distillery | downtown_bar_actions.rpy
    # This bar gets updated when a save game is loaded, regardless of its existence
    downtown_bar_objects = [
        make_desk(),
        make_chair(),
        make_floor()
    ]
    downtown_bar = Room("bar", "The Downtown Distillery", [], bar_background, downtown_bar_objects,[], [downtown_bar_action], True, [5,4], None, True)

    # Hotel Room - The Hotel | No actions at this time.
    # This hotel gets updated when a save game is loaded, regardless of its existence
    downtown_hotel_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
        make_bed()
    ]
    downtown_hotel = Room("hotel", "The Hotel", [], room_background_image("Hotel_Room_Background.jpg"), downtown_hotel_objects,[], [], False, [5,5], None, True)

    #Creates a room specifically to keep girls we don't want to be accessible, so they are still updated.
    purgatory_objects = [
        make_floor()
    ]

    purgatory = Room("purgatory",
        formalName = "Purgatory",
        connections = [],
        background_image = None,
        objects = purgatory_objects,
        people = [],
        actions = [],
        public = False,
        map_pos = [-5, -5],
        tutorial_label = None,
        visible = False,
        hide_in_known_house_map = True)
    purgatory.accessible = False

init 5  python:
    add_label_hijack("normal_start", "activate_custom_rooms")
    add_label_hijack("after_load", "update_custom_rooms")

label activate_custom_rooms(stack):

    call store_m_division_basement() from _store_m_division_basement_1
    call store_p_division_basement() from _store_p_division_basement_1
    call store_rd_division_basement() from _store_rd_division_basement_1
    call store_office_basement() from _store_office_basement_1
    call store_downtown_bar() from _call_store_downtown_bar_1
    call store_downtown_hotel() from _call_store_downtown_hotel_1
    call store_purgatory_room() from _call_store_purgatory_room_1

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
    call store_downtown_hotel() from _call_store_downtown_hotel_2
    call store_purgatory_room() from _call_store_purgatory_room_2

    $ clean_elevator_action()
    $ execute_hijack_call(stack)
    return

label store_m_division_basement():
    if m_division_basement not in list_of_places:
        #$ m_division_basement.link_locations(m_division)
        $ list_of_places.append(m_division_basement)
    
    $ m_division_basement = update_custom_rooms(m_division_basement)
    return

label store_p_division_basement():
    if p_division_basement not in list_of_places:
        #$ p_division_basement.link_locations(p_division)
        $ list_of_places.append(p_division_basement)
    
    $ p_division_basement = update_custom_rooms(p_division_basement)
    return

label store_rd_division_basement():
    if rd_division_basement not in list_of_places:
        #$ rd_division_basement.link_locations(rd_division)
        $ list_of_places.append(rd_division_basement)
    
    $ rd_division_basement = update_custom_rooms(rd_division_basement)
    return

label store_office_basement():
    if office_basement not in list_of_places:
        #$ office_basement.link_locations(office)
        $ list_of_places.append(office_basement)
    
    $ office_basement = update_custom_rooms(office_basement)
    return

label store_downtown_bar():
    # Make sure it is in the list_of_places (and no duplicate)
    # List of places gets stored, so will the bar when appended here
    if downtown_bar not in list_of_places:
        #$ downtown_bar.link_locations(downtown)
        $ list_of_places.append(downtown_bar)

    # This refreshes the properties of the existing bar, e.g move the position of the Room on the map, objects, actions, connections, background etc.
    $ downtown_bar = update_custom_rooms(downtown_bar)
    return

label store_downtown_hotel():
    # Make sure it is in the list_of_places (and no duplicate)
    # List of places gets stored, so will the bar when appended here
    if downtown_hotel not in list_of_places:
        #$ downtown_hotel.link_locations(downtown)
        $ list_of_places.append(downtown_hotel)

    # This refreshes the properties of the existing bar, e.g move the position of the Room on the map, objects, actions, connections, background etc.
    $ downtown_hotel = update_custom_rooms(downtown_hotel)
    return

label store_purgatory_room():
    if purgatory not in list_of_places:
        $ list_of_places.append(purgatory)

    $ purgatory = update_custom_rooms(purgatory)
    return
