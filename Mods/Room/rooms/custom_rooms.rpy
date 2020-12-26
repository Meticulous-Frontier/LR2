# name, formalName, connections, background_image, objects, people, actions, public, map_pos, tutorial_label = None, visible = True)
init 3 python:
    add_label_hijack("normal_start", "build_custom_rooms")


init 15 python:
    dungeon_objects = [
        make_bdsmbed(),
        make_pillory(),
        make_woodhorse(),
        make_floor(),
    ]
    downtown_bar_objects = [
        make_desk(),
        make_chair(),
        make_floor()
    ]
    downtown_hotel_lobby_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
    ]
    downtown_hotel_room_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
        make_window(),
        make_bed()
    ]
    purgatory_objects = [
        make_floor()
    ]
    bdsm_room_objects = [
        make_pillory(),
        make_woodhorse(),
        make_cage(),
        make_chair(),
        make_floor()
    ]
    ceo_office_objects = [
        make_chair(),
        make_desk(),
        make_wall(),
        make_window(),
        make_floor(),
    ]
    police_jail_objects = [
        Object("cell bars", ["Lean"], sluttiness_modifier = 5, obedience_modifier = 10),
        make_wall(),
        make_bed(),
        make_floor(),
    ]
    gym_shower_objects = [
        make_floor(),
        make_wall(),
        Object("shower door", ["Lean"], sluttiness_modifier = 5, obedience_modifier = 5)
    ]

    def make_swing():
        the_swing = Object("sex swing",["Sit","Low", "Swing"], sluttiness_modifier = 10, obedience_modifier = 10)
        return the_swing

    def make_counter():
        the_counter = Object("counter",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)
        return the_counter


label build_custom_rooms(stack):
    python:
        # Research Division Basement - Biotechnology Lab | biotech_room_actions.rpy
        # rd_division_basement = Room("biotech", "Biotechnology Lab", [], room_background_image("Biotech_Background.jpg"), rd_division_basement_objects, [], [biotech_clone_person, biotech_modify_person], False, [12,5], None, False, lighting_conditions = standard_indoor_lighting)

        # Main Office Basement - Dungeon | dungeon_room_actions.rpy
        dungeon = Room("dungeon", "Dungeon", [], standard_dungeon_backgrounds[:], dungeon_objects, [], [dungeon_room_appoint_slave_action], False, [4,3], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(dungeon)

        # Downtown Bar - The Downtown Distillery | downtown_bar_actions.rpy
        downtown_bar = Room("bar", "The Downtown Distillery", [], bar_background, downtown_bar_objects, [], [downtown_bar_drink_action], True, [5,4], None, True, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(downtown_bar)

        # Hotel Lobby - The Hotel | No actions at this time.
        # room is public, so girls can wander here too
        downtown_hotel = Room("hotel lobby", "The Hotel", [], standard_hotel_backgrounds[:], downtown_hotel_lobby_objects,[], [], True, [5,5], None, True, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(downtown_hotel)

        downtown_hotel_room = Room("hotel room", "The Hotel Room", [], standard_hotel_room_backgrounds[:], downtown_hotel_room_objects,[], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(downtown_hotel_room)

        #Creates a room specifically to keep girls we don't want to be accessible, so they are still updated.
        purgatory = Room("purgatory", "Purgatory", [], None, purgatory_objects, [], [], False, [-5, -5], None, False, True, lighting_conditions = standard_indoor_lighting)
        purgatory.accessible = False

        fancy_restaurant = Room("fancy_restaurant", "Restaurant", [], standard_fancy_restaurant_backgrounds[:], [make_floor(), make_chair(), make_table()], [], [], False, [4,6], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(fancy_restaurant)

        # Stripclub BDSM Room | No actions at this time.
        bdsm_room = Room("bdsm_room", "[strip_club.formalName] - BDSM room", [], standard_bdsm_room_backgrounds[:], bdsm_room_objects,[], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(bdsm_room)

        ceo_office = Room("ceo_office", "CEO Office", [], standard_ceo_office_backgrounds[:], ceo_office_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(ceo_office)

        # room is public so girls are not always visible in the main map
        gym_shower = Room("gym shower", "Gym Shower", [], standard_gym_shower_backgrounds[:], gym_shower_objects, [], [], True, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(gym_shower)

        home_shower = Room("home shower", "Home Shower", [], standard_home_shower_backgrounds[:], gym_shower_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(home_shower)

        mall_salon = Room("salon", "Hair Salon", [], standard_salon_backgrounds[:], [make_floor(), make_wall(), make_chair(), make_window(), make_counter()], [], [], True, [7,2], None, True, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(mall_salon)

        # added police station (and jail) at request of Starbuck
        police_station = Room("police_station", "Police Station", [], standard_police_station_backgrounds[:], ceo_office_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(police_station)

        police_jail = Room("police_jail", "Police Jail", [], standard_police_jail_backgrounds[:], police_jail_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(police_jail)

        work_bathroom = Room("work bathroom", "Work Bathroom", [], bathroom_background, [make_wall(), make_floor()], [], [], False, [0,0], visible = False)
        list_of_places.append(work_bathroom)

        # initialize dungeon room creation action
        add_dungeon_intro_action()

        execute_hijack_call(stack)
    return

init 10 python:
    add_label_hijack("after_load", "update_custom_rooms")

    def fix_duplicate_objects_in_rooms():
        for room in list_of_places:
            unique = list(set(room.objects))
            if len(unique) != len(room.objects):    # mismatch update
                room.objects = unique
        return

    def update_room_visibility():
        remove_list = []
        for i in range(0, len(list_of_places) - 1):
            for j in range(i + 1, len(list_of_places)):
                if not list_of_places[j] in remove_list:
                    if i == j:
                        remove_list.append(list_of_places[j])

        if len(remove_list) > 0:
            for room in remove_list:
                renpy.say("Warning", "Duplicate room " + room.name + ", game is corrupt, your are advised to start a new game.")

        return

label update_custom_rooms(stack):
    python:
        update_room_visibility()
        fix_duplicate_objects_in_rooms()

        execute_hijack_call(stack)
    return
