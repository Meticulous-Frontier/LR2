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

    # Hotel Lobby - The Hotel | No actions at this time.
    # This hotel gets updated when a save game is loaded, regardless of its existence
    downtown_hotel_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
    ]
    downtown_hotel = Room("hotel lobby", "The Hotel", [], standard_hotel_backgrounds[:], downtown_hotel_objects,[], [], True, [5,5], None, True, lighting_conditions = standard_indoor_lighting)

    downtown_hotel_room_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
        make_bed()
    ]
    downtown_hotel_room = Room("hotel room", "The Hotel Room", [], standard_hotel_room_backgrounds[:], downtown_hotel_room_objects,[], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)

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
    bdsm_room = Room("bdsm_room", "[strip_club.formalName] - BDSM room", [], standard_bdsm_room_backgrounds[:], bdsm_room_objects,[], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)

    ceo_office_objects = [
        make_chair(),
        make_desk(),
        make_floor(),
    ]

    ceo_office = Room("ceo_office", "CEO Office", [], standard_ceo_office_backgrounds[:], ceo_office_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)

    # room is public so girls are not always visible in the main map
    gym_shower_objects = [
        make_floor(),
        make_wall(),
        Object("shower door", ["Lean"], sluttiness_modifier = 5, obedience_modifier = 5)
    ]
    gym_shower = Room("gym shower", "Gym Shower", [], standard_gym_shower_backgrounds[:], gym_shower_objects, [], [], True, [], None, False, lighting_conditions = standard_indoor_lighting)

    home_shower = Room("home shower", "Home Shower", [], standard_home_shower_backgrounds[:], gym_shower_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)

    # these rooms are updated / created at start or load of game
    room_storage_list = [dungeon, downtown_bar, downtown_hotel, downtown_hotel_room, fancy_restaurant, bdsm_room, purgatory, ceo_office, gym_shower, home_shower]


init 10 python:
    add_label_hijack("normal_start", "activate_custom_rooms")
    add_label_hijack("after_load", "update_custom_rooms")

    def store_custom_rooms():
        for room in room_storage_list:
            if room not in list_of_places:
                list_of_places.append(room)
            else:
                found = find_in_list(lambda x: x.name == room.name, list_of_places)
                if found: # update existing room
                    found.background_image = room.background_image
                    found.objects = room.objects
                    found.public = room.public
                    found.map_pos = room.map_pos
                    found.visible = room.visible
        return       

label activate_custom_rooms(stack):
    python:
        store_custom_rooms()

        # initialize dungeon room creation action
        add_dungeon_intro_action()

        execute_hijack_call(stack)
    return

label update_custom_rooms(stack):
    python:
        store_custom_rooms()
        
        execute_hijack_call(stack)
    return
