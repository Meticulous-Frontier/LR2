init 5 python:
    add_label_hijack("normal_start", "updated_room_background")
    add_label_hijack("after_load", "updated_room_background")

    #Harem/girlfriend/affair
    gf_token_small_image = im.Scale(Image(get_file_handle("girlfriend.png")), 18, 18)
    renpy.image("gf_token_small", gf_token_small_image)
    
    paramour_token_small_image = im.Scale(Image(get_file_handle("paramour.png")), 18, 18)
    renpy.image("paramour_token_small", paramour_token_small_image)
    
    harem_token_small_image = im.Scale(Image(get_file_handle("harem.png")), 18, 18)
    renpy.image("harem_token_small", harem_token_small_image)

    # scaled images
    taboo_break_image = im.Scale(Image(get_file_handle("taboo_lock_alt.png")), 16, 22)
    renpy.image("taboo_break", taboo_break_image)
    thumbs_up_image = im.Scale(Image(get_file_handle("thumbs_up_small.png")), 16, 22)
    renpy.image("thumbs_up", thumbs_up_image)
    thumbs_down_image = im.Scale(Image(get_file_handle("thumbs_down_small.png")), 16, 22)
    renpy.image("thumbs_down", thumbs_down_image)

    energy_token_small_image = im.Scale(Image(get_file_handle("energy_token.png")), 18, 18)
    renpy.image("energy_token_small", energy_token_small_image)

    arousal_token_small_image = im.Scale(Image(get_file_handle("arousal_token.png")), 18, 18)
    renpy.image("arousal_token_small", arousal_token_small_image)

    red_heart_token_small_image = im.Scale(Image(get_file_handle("heart/red_heart.png")), 18, 18)
    renpy.image("red_heart_token_small", red_heart_token_small_image)

    lust_eye_token_small_image = im.Scale(Image(get_file_handle("lust_eye.png")), 18, 18)
    renpy.image("lust_eye_token_small", lust_eye_token_small_image)

    feeding_bottle_token_small_image = im.Scale(Image(get_file_handle("feeding_bottle.png")), 18, 18)
    renpy.image("feeding_bottle_token_small", feeding_bottle_token_small_image)

    happy_small_image = im.Scale(Image(get_file_handle("happy.png")), 18, 18)
    renpy.image("happy_token_small", happy_small_image)

    underwear_small_image = im.Scale(Image(get_file_handle("underwear_token.png")), 18, 18)
    renpy.image("underwear_token_small", underwear_small_image)

    padlock_small_image = im.Scale(Image(get_file_handle("padlock.png")), 18, 18)
    renpy.image("padlock_token_small", padlock_small_image)

    question_mark_small_image = im.Scale(Image(get_file_handle("question.png")), 18, 18)
    renpy.image("question_mark_small", question_mark_small_image)

    infraction_token_small_image = im.Scale(Image(get_file_handle("infraction_token.png")), 18, 18)
    renpy.image("infraction_token_small", infraction_token_small_image)

    speech_bubble_small_image = im.Scale(Image(get_file_handle("speech_bubble.png")), 18, 18)
    renpy.image("speech_bubble_token_small", speech_bubble_small_image)

    speech_bubble_exclamation_small_image = im.Scale(Image(get_file_handle("speech_bubble_exclamation.png")), 18, 18)
    renpy.image("speech_bubble_exclamation_token_small", speech_bubble_exclamation_small_image)

    vial_token_small_image = im.Scale(Image(get_file_handle("vial.png")), 18, 18)
    renpy.image("vial_token_small", vial_token_small_image)

    vial_image = Image(get_file_handle("vial.png"))
    dna_image = Image(get_file_handle("dna.png"))
    question_image = Image(get_file_handle("question.png"))
    home_image = Image(get_file_handle("home_marker.png"))
    #padlock_image = Image(get_file_handle("padlock.png"))

    under_construction_image = Image(get_file_handle("under_construction.png"))

    empty_image = Image(get_file_handle("empty_holder.png"))


init -1 python:
    # override default render backgrounds
    enhanced_office_backgrounds = room_background_image("Main_Office_Background.jpg")
    enhanced_marketing_backgrounds = room_background_image("Marketing_Background.jpg")
    enhanced_production_backgrounds = room_background_image("Production_Background.jpg")
    enhanced_research_backgrounds = room_background_image("RandD_Background.jpg")
    enhanced_lobby_backgrounds = room_background_image("Office_Lobby_Background.jpg")
    # updated (no existing backgrounds)
    standard_sex_store_backgrounds = room_background_image("Sex_Shop_Background.jpg")
    standard_gym_backgrounds = room_background_image("Gym_Background.jpg")
    standard_clothing_store_backgrounds =  room_background_image("Clothing_Store_Background.jpg")
    standard_her_hallway_backgrounds = room_background_image("her_hallway_background.jpg")
    standard_office_store_backgrounds = room_background_image("Office_Store_Background.jpg")
    standard_laundry_room_backgrounds = room_background_image("Laundry_Room_Background.jpg")
    # extra backgrounds
    standard_biotech_backgrounds = room_background_image("Biotech_Background.jpg")
    standard_dungeon_backgrounds = room_background_image("Dungeon_Background.jpg")
    standard_hotel_backgrounds = room_background_image("Hotel_Lobby_Background.jpg")
    standard_hotel_room_backgrounds = room_background_image("Hotel_Room_Background.jpg")
    standard_fancy_restaurant_backgrounds = room_background_image("Fancy_Restaurant_Background.jpg")
    standard_gym_shower_backgrounds = room_background_image("Gym_Shower_Background.jpg")
    standard_salon_backgrounds = room_background_image("Salon_Background.jpg")
    standard_old_home_shower_backgrounds = room_background_image("Home_Shower_Background_Old.jpg")
    standard_home_shower_backgrounds = room_background_image("Home_Shower_Background.jpg")
    standard_bdsm_room_backgrounds = room_background_image("BDSM_Room_Background.jpg")
    standard_ceo_office_backgrounds = room_background_image("CEO_Office_Background.jpg")
    standard_police_station_backgrounds = room_background_image("Police_Station_Background.jpg", darken = False)
    standard_police_jail_backgrounds = room_background_image("Police_Jail_Background.jpg", darken = False)
    standard_coffee_shop_backgrounds = room_background_image("Coffee_Shop_Background.jpg")
    luxury_apartment_backgrounds = room_background_image("Luxury_Apartment_Background.jpg", darken = False)
    university_library_backgrounds = room_background_image("University_Library_Background.jpg")
    university_study_room_backgrounds = room_background_image("Study_Room_Background.jpg")
    # bedroom backgrounds
    standard_bedroom1_background = room_background_image("Generic_Bedroom1_Background.jpg")
    standard_bedroom2_background = room_background_image("Generic_Bedroom2_Background.jpg")
    standard_bedroom3_background = room_background_image("Generic_Bedroom3_Background.jpg")
    standard_bedroom4_background = room_background_image("Generic_Bedroom4_Background.jpg")
    prostitute_bedroom_background = room_background_image("Prostitute_Bedroom_Background.jpg")
    lily_bedroom_background = room_background_image("Lily_Bedroom_Background.jpg")
    cousin_bedroom_background = room_background_image("Cousin_Bedroom_Background.jpg", darken = False)

    def update_rd_div_with_genetics_unlocked():
        if not genetic_modification_policy.is_owned():
            return

        found = find_in_list(lambda x: x.name == "R&D division", list_of_places)
        if found:
            found.background_image = standard_biotech_backgrounds
        return

    def show_lily_room_background(*args, **kwargs):
        bedroom_image = lily_bedroom_background[time_of_day]
        renpy.show("emily_bedroom", what = Image(bedroom_image), layer = "master")
        return

    def show_university_library_background(*args, **kwargs):
        library_image = university_library_backgrounds[time_of_day]
        renpy.show("university_library", what=Image(library_image), layer = "master")
        return

    def show_university_study_room_background(*args, **kwargs):
        library_image = university_study_room_backgrounds[time_of_day]
        renpy.show("university_study_room", what=Image(library_image), layer = "master")
        return

label updated_room_background(stack):
    # Load extra GUI images
    image serum_vial = "[vial_image.filename]"
    image question_mark = "[question_image.filename]"
    image dna_sequence = "[dna_image.filename]"
    image home_marker = "[home_image.filename]"

    python:
        # as long as the base game has no nice images, we use these to make navigating a little more fun
        office.background_image = enhanced_office_backgrounds
        m_division.background_image = enhanced_marketing_backgrounds
        p_division.background_image = enhanced_production_backgrounds
        rd_division.background_image = enhanced_research_backgrounds
        lobby.background_image = enhanced_lobby_backgrounds

        mom_office_lobby.background_image = enhanced_lobby_backgrounds
        mom_offices.background_image = enhanced_marketing_backgrounds

        #As long a there is a mall background for these, replace it with our custom background
        sex_store.background_image = standard_sex_store_backgrounds
        gym.background_image = standard_gym_backgrounds
        clothing_store.background_image = standard_clothing_store_backgrounds
        office_store.background_image = standard_office_store_backgrounds
        if "her_hallway" in globals(): # check if room exists
            her_hallway.background_image = standard_her_hallway_backgrounds
        laundry_room = Room("Laundry Room", "Laundry Room", [], standard_laundry_room_backgrounds,[make_bed(), make_wall(), make_floor()],[],[],False,[-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        if not laundry_room in list_of_places:
            list_of_places.append(laundry_room)

        # bedrooms are linked in the person extensions, one time assignment of on of the bedrooms to a person
        prostitute_bedroom = Room("Prostitute Bedroom", "Prostitute Bedroom", [], prostitute_bedroom_background,[make_bed(), make_wall(), make_window(), make_love_rug()],[],[],False,[-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        if not prostitute_bedroom in list_of_places:
            list_of_places.append(prostitute_bedroom)

        generic_bedroom_1 = Room("Generic Bedroom 1", "Bedroom", [], standard_bedroom1_background,[make_bed(), make_wall(), make_window(), make_floor()],[],[],False, [-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        if not generic_bedroom_1 in list_of_places:
            list_of_places.append(generic_bedroom_1)
        generic_bedroom_2 = Room("Generic Bedroom 2", "Bedroom", [], standard_bedroom2_background,[make_bed(), make_wall(), make_window(), make_floor()],[],[],False, [-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        if not generic_bedroom_2 in list_of_places:
            list_of_places.append(generic_bedroom_2)
        generic_bedroom_3 = Room("Generic Bedroom 3", "Bedroom", [], standard_bedroom3_background,[make_bed(), make_wall(), make_window(), make_floor()],[],[],False, [-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        if not generic_bedroom_3 in list_of_places:
            list_of_places.append(generic_bedroom_3)
        generic_bedroom_4 = Room("Generic Bedroom 4", "Bedroom", [], standard_bedroom4_background,[make_bed(), make_wall(), make_window(), make_floor()],[],[],False, [-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        if not generic_bedroom_4 in list_of_places:
            list_of_places.append(generic_bedroom_4)

        # bedroom image replacements
        #lily.home.background_image = lily_bedroom_background
        cousin.home.background_image = cousin_bedroom_background
        #mom.home.background_image = standard_bedroom1_background
        aunt.home.background_image = standard_bedroom4_background

        # student mom (rich uptown snob)
        christina.home.background_image = luxury_apartment_backgrounds
        # instead of changing the role label, just hook a python function before the label
        # to show the correct background for emily study at home
        hook_label("student_study_home", show_lily_room_background)
        hook_label("student_study_university", show_university_library_background)

        # update rd division when genetics are unlocked
        update_rd_div_with_genetics_unlocked()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
