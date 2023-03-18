# name, formal_name, connections, background_image, objects, people, actions, public, map_pos, tutorial_label = None, visible = True)
init 3 python:
    list_of_instantiation_labels.append("build_custom_rooms")
    add_label_hijack("normal_start", "validate_custom_rooms")
    add_label_hijack("normal_start", "link_unique_character_bedrooms")

init 15 python:
    dungeon_objects = [
        make_bed(),
        make_couch(),
        make_bdsmbed(),
        make_pillory(),
        make_wall(),
        make_floor(),
    ]
    harem_objects =[
        make_bed(),
        make_couch(),
        make_chair(),
        make_wall(),
        make_floor(),
    ]
    downtown_bar_objects = [
        make_desk(),
        make_chair(),
        make_wall(),
        make_floor()
    ]
    downtown_hotel_lobby_objects = [
        make_desk(),
        make_chair(),
        make_wall(),
        make_floor(),
    ]
    downtown_hotel_room_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
        make_window(),
        make_wall(),
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
        make_wall(),
        make_floor(),
        make_bed(),
        make_couch(),
        make_pole(),
        make_stage()
    ]
    ceo_office_objects = [
        make_chair(),
        make_desk(),
        make_wall(),
        make_window(),
        make_floor(),
        make_black_leather_couch(),
    ]
    police_jail_objects = [
        Object("cell bars", ["Lean"], sluttiness_modifier = 0, obedience_modifier = 0),
        make_wall(),
        make_bed(),
        make_floor(),
    ]
    gym_shower_objects = [
        make_floor(),
        make_wall(),
        Object("shower door", ["Lean"], sluttiness_modifier = 0, obedience_modifier = 0),
        make_bench(),
    ]
    coffee_shop_objects = [
        make_floor(),
        make_wall(),
        make_window(),
        Object("counter",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0),
        Object("Booth", ["Sit", "Lay", "Low"], sluttiness_modifier = 0, obedience_modifier = 0),
        make_bench()
    ]

    gaming_cafe_objects = [
        make_floor(),
        make_wall(),
        make_desk(),
        make_chair()
    ]

    def make_swing():
        return Object("sex swing",["Sit","Low","Lay", "Swing"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_counter():
        return Object("counter",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_reception():
        return Object("reception desk",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_dryer():
        return Object("dryer", ["Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_mirror():
        return Object("mirror", ["Lean"])


label build_custom_rooms():
    python:
        # Research Division Basement - Biotechnology Lab | biotech_room_actions.rpy
        # rd_division_basement = Room("biotech", "Biotechnology Lab", [], room_background_image("Biotech_Background.jpg"), rd_division_basement_objects, [], [biotech_clone_person, biotech_modify_person], False, [12,5], None, False, lighting_conditions = standard_indoor_lighting)

        # Main Office Basement - Dungeon | dungeon_room_actions.rpy
        dungeon = Room("dungeon", "Dungeon", [], standard_dungeon_backgrounds, dungeon_objects, [], [dungeon_room_appoint_slave_action], False, [4,3], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(dungeon)
        dungeon.privacy_level = 0

        # TODO: Add actions that can be performed in mansion
        harem_mansion = Room("harem_mansion", "Harem Mansion", [], standard_harem_mansion_backgrounds, harem_objects, [], [], False, [1, 3], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(harem_mansion)
        harem_mansion.privacy_level = 0

        # Downtown Bar - The Downtown Distillery | downtown_bar_actions.rpy
        downtown_bar = Room("bar", "The Downtown Distillery", [], bar_background, downtown_bar_objects, [], [downtown_bar_drink_action], True, [5,4], None, True, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(downtown_bar)
        downtown_bar.privacy_level = 3

        # Hotel Lobby - The Hotel | No actions at this time.
        # room is public, so girls can wander here too
        downtown_hotel = Room("hotel lobby", "The Hotel", [], standard_hotel_backgrounds, downtown_hotel_lobby_objects,[], [], True, [5,5], None, True, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(downtown_hotel)
        downtown_hotel.privacy_level = 3

        downtown_hotel_room = Room("hotel room", "The Hotel Room", [], standard_hotel_room_backgrounds, downtown_hotel_room_objects,[], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(downtown_hotel_room)
        downtown_hotel_room.privacy_level = 0

        #Creates a room specifically to keep girls we don't want to be accessible, so they are still updated.
        purgatory = Room("purgatory", "Hospital", [], None, purgatory_objects, [], [], False, [-5, -5], None, False, True, lighting_conditions = standard_indoor_lighting)
        purgatory.accessible = False
        list_of_places.append(purgatory)
        purgatory.privacy_level = 0

        fancy_restaurant = Room("fancy_restaurant", "Restaurant", [], standard_fancy_restaurant_backgrounds, [make_floor(), make_chair(), make_table()], [], [], False, [4,6], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(fancy_restaurant)
        fancy_restaurant.privacy_level = 3

        # Stripclub BDSM Room | No actions at this time. HACK: Add dungeon action
        bdsm_room = Room("bdsm_room", "[strip_club.formal_name] - BDSM room", [], standard_bdsm_room_backgrounds, bdsm_room_objects,[], [dungeon_room_appoint_slave_action], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(bdsm_room)
        bdsm_room.privacy_level = 0

        ceo_office = Room("ceo_office", "CEO Office", [], standard_ceo_office_backgrounds, ceo_office_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(ceo_office)
        ceo_office.privacy_level = 0

        # room is public so girls are not always visible in the main map
        gym_shower = Room("gym shower", "Gym Shower", [], standard_gym_shower_backgrounds, gym_shower_objects, [], [], True, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(gym_shower)
        gym_shower.privacy_level = 1

        home_shower = Room("home shower", "Home Shower", [], standard_old_home_shower_backgrounds, gym_shower_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(home_shower)
        home_shower.privacy_level = 0

        mall_salon = Room("salon", "Hair Salon", [], standard_salon_backgrounds, [make_floor(), make_wall(), make_chair(), make_window(), make_counter()], [], [], True, [7,2], None, True, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(mall_salon)
        mall_salon.privacy_level = 3

        # special testing room
        testing_room = Room("testing_room", "Test Room", [], testing_room_backgrounds, [make_floor(), make_wall(), make_chair(), make_table(), make_mirror()], [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(testing_room)
        testing_room.privacy_level = 0

        # added police station (and jail) at request of Starbuck
        police_station = Room("police_station", "Police Station", [], standard_police_station_backgrounds, ceo_office_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(police_station)
        police_station.privacy_level = 3

        police_jail = Room("police_jail", "Police Jail", [], standard_police_jail_backgrounds, police_jail_objects, [], [], False, [], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(police_jail)
        police_jail.privacy_level = 3

        #Coffee shop
        coffee_shop = Room("coffee_shop", "Coffee Shop", [], standard_coffee_shop_backgrounds, coffee_shop_objects, [], [coffee_shop_get_coffee_action], True, [7,3], None, True, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(coffee_shop)
        coffee_shop.privacy_level = 3

        gaming_cafe = Room("gaming_cafe", "Gaming Cafe", [], standard_gaming_cafe_backgrounds, gaming_cafe_objects, [], [gaming_cafe_grind_character_action, gaming_cafe_buy_max_level_token_action, gaming_cafe_adult_swim], False, [6,2], None, False, lighting_conditions = standard_indoor_lighting)
        list_of_places.append(gaming_cafe)
        gaming_cafe.privacy_level = 3
    return

label link_unique_character_bedrooms(stack):
    # only executed once, after game-start (prevents duplicate bedroom objects for these characters)
    python:
        lily.bedroom = lily_bedroom
        mom.bedroom = mom_bedroom
        aunt.bedroom = aunt_bedroom
        cousin.bedroom = cousin_bedroom

        execute_hijack_call(stack)
    return

label validate_custom_rooms(stack):
    # extra code run after creation of all rooms
    python:
        # Move electronic store to top location
        electronics_store.map_pos = [7,0]

        # initialize dungeon room creation action
        fix_lobby_objects()

        add_custom_objects()
        update_room_privacy_level()
        fix_duplicate_objects_in_rooms()

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

    def fix_duplicate_room_objects():
        if not lily.bedroom is lily_bedroom:
            lily.bedroom = lily_bedroom
        if not mom.bedroom is mom_bedroom:
            mom.bedroom = mom_bedroom
        if not aunt.bedroom is aunt_bedroom:
            aunt.bedroom = aunt_bedroom
        if not cousin.bedroom is cousin_bedroom:
            cousin.bedroom = cousin_bedroom
        return

    def fix_lobby_objects():
        for room in list_of_places:
            if room == lobby or room == mom_office_lobby:
                found = find_in_list(lambda x: x.name == "desk", room.objects)
                if found:
                    room.objects.remove(found)
                    room.objects.append(make_reception())
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
                renpy.say("Warning", "Duplicate room " + room.name + ", game is corrupt, you are advised to start a new game.")

        return

    def add_custom_objects():
        #add additional objects to existing rooms
        strip_club.add_object( make_pole() )
        downtown.add_object( make_bench() )
        gym.add_object( make_bench() )
        gym_shower.add_object( make_bench() )
        university.add_object( make_bench() )
        # Maybe make this something that the MC pays for. R&D Upgrade
        rd_division.add_object( make_examtable() )

        return

    def fix_missing_rooms():
        # added for save compatibility
        if purgatory not in list_of_places:
            list_of_places.append(purgatory)
        return

    def update_room_privacy_level(): #Set privacy level of vanilla rooms.
        bedroom.privacy_level = 0
        lily_bedroom.privacy_level = 0
        mom_bedroom.privacy_level = 0
        kitchen.privacy_level = 0
        hall.privacy_level = 0
        her_hallway.privacy_level = 0

        lobby.privacy_level = 2
        office.privacy_level = 2
        rd_division.privacy_level = 2
        p_division.privacy_level = 2
        m_division.privacy_level = 2
        work_bathroom.privacy_level = 2

        downtown.privacy_level = 3

        office_store.privacy_level = 3
        clothing_store.privacy_level = 3
        sex_store.privacy_level = 1
        home_store.privacy_level = 3
        gym.privacy_level = 3
        gym_shower.privacy_level = 1
        electronics_store.privacy_level = 3
        mall.privacy_level = 3
        changing_room.privacy_level = 1

        aunt_apartment.privacy_level = 0
        aunt_bedroom.privacy_level = 0
        cousin_bedroom.privacy_level = 0
        university.privacy_level = 3
        strip_club.privacy_level = 1

        mom_office_lobby.privacy_level = 3
        mom_offices.privacy_level = 3

        city_hall.privacy_level = 3
        return

label update_custom_rooms(stack):
    python:
        update_room_visibility()
        add_custom_objects()
        update_room_privacy_level()
        fix_duplicate_objects_in_rooms()
        fix_lobby_objects()
        fix_missing_rooms()
        fix_duplicate_room_objects()

        execute_hijack_call(stack)
    return
