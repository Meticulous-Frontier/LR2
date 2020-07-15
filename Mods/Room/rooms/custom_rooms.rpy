# name, formalName, connections, background_image, objects, people, actions, public, map_pos, tutorial_label = None, visible = True)

init 15 python:
    # Research Division Basement - Biotechnology Lab | biotech_room_actions.rpy
    # rd_division_basement = Room("biotech", "Biotechnology Lab", [], room_background_image("Biotech_Background.jpg"), rd_division_basement_objects, [], [biotech_clone_person, biotech_modify_person], False, [12,5], None, False, lighting_conditions = standard_indoor_lighting)

    # Main Office Basement - Dungeon | dungeon_room_actions.rpy
    dungeon_objects = [
        make_bdsmbed(),
        make_pillory(),
        make_woodhorse(),
        make_floor(),
    ]
    dungeon = Room("dungeon", "Dungeon", [], standard_dungeon_backgrounds[:], dungeon_objects, [], [dungeon_room_appoint_slave_action], False, [4,3], None, False, lighting_conditions = standard_indoor_lighting)

    # Downtown Bar - The Downtown Distillery | downtown_bar_actions.rpy
    # This bar gets updated when a save game is loaded, regardless of its existence
    downtown_bar_objects = [
        make_desk(),
        make_chair(),
        make_floor()
    ]
    downtown_bar = Room("bar", "The Downtown Distillery", [], bar_background, downtown_bar_objects, [], [downtown_bar_drink_action], True, [5,4], None, True, lighting_conditions = standard_indoor_lighting)

    # Hotel Room - The Hotel | No actions at this time.
    # This hotel gets updated when a save game is loaded, regardless of its existence
    downtown_hotel_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
        make_bed()
    ]
    downtown_hotel = Room("hotel", "The Hotel", [], standard_hotel_backgrounds[:], downtown_hotel_objects,[], [], False, [5,5], None, True, lighting_conditions = standard_indoor_lighting)

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

    fancy_restaurant = Room("fancy_restaurant", "Restaurant", [], standard_fancy_restaurant_backgrounds[:], [make_floor(), make_chair(), make_table()], [], [], False, [4,6], None, False, lighting_conditions = standard_indoor_lighting)

    # Stripclub BDSM Room | No actions at this time.
    # This hotel gets updated when a save game is loaded, regardless of its existence
    bdsm_room_objects = [
        make_bdsmbed(),
        make_pillory(),
        make_woodhorse(),
        make_cage(),
        make_chair(),
        make_floor(),
        make_bed()
    ]
    bdsm_room = Room("bdsm_room", "[strip_club.formalName] - BDSM room", [], standard_bdsm_room_backgrounds[:], bdsm_room_objects,[], [], False, [-6,-6], None, False, lighting_conditions = standard_indoor_lighting)

init 5  python:
    add_label_hijack("normal_start", "activate_custom_rooms")
    add_label_hijack("after_load", "update_custom_rooms")

label activate_custom_rooms(stack):
    call store_dungeon() from _store_dungeon_1
    call store_downtown_bar() from _call_store_downtown_bar_1
    call store_downtown_hotel() from _call_store_downtown_hotel_1
    call store_fancy_restaurant() from _call_store_fancy_restaurant_1
    call store_bdsm_room() from _call_store_bdsm_room_1
    call store_purgatory_room() from _call_store_purgatory_room_1

    # initialize dungeon room creation action
    $ add_dungeon_intro_action()

    $ execute_hijack_call(stack)
    return

label update_custom_rooms(stack):
    # use this code to add only a new missing room
    # if not find_in_list(lambda x: x.name == "downtown_bar", list_of_places):
    #     call update_downtown_bar() from _call_update_downtown_bar

    call store_dungeon() from _store_dungeon_2
    call store_downtown_bar() from _call_store_downtown_bar_2
    call store_downtown_hotel() from _call_store_downtown_hotel_2
    call store_fancy_restaurant() from _call_store_fancy_restaurant_2
    call store_bdsm_room() from _call_store_bdsm_room_2
    call store_purgatory_room() from _call_store_purgatory_room_2

    $ execute_hijack_call(stack)
    return

label store_dungeon():
    if dungeon not in list_of_places:
        $ list_of_places.append(dungeon)

    $ dungeon = update_custom_rooms(dungeon)
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

label store_fancy_restaurant():
    if fancy_restaurant not in list_of_places:
        $ list_of_places.append(fancy_restaurant)

    $ fancy_restaurant = update_custom_rooms(fancy_restaurant)
    return

label store_purgatory_room():
    if purgatory not in list_of_places:
        $ list_of_places.append(purgatory)

    $ purgatory = update_custom_rooms(purgatory)
    return

label store_bdsm_room():
    # Make sure it is in the list_of_places (and no duplicate)
    # List of places gets stored, so will the bar when appended here
    if bdsm_room not in list_of_places:
        $ list_of_places.append(bdsm_room)

    # This refreshes the properties of the existing bar, e.g move the position of the Room on the map, objects, actions, connections, background etc.
    $ bdsm_room = update_custom_rooms(bdsm_room)
    return
