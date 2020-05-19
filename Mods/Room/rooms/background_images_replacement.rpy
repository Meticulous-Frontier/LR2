init 5 python:
    add_label_hijack("normal_start", "updated_room_background")
    add_label_hijack("after_load", "updated_room_background")

    # scaled images
    taboo_break_image = im.Scale(Image(get_file_handle("taboo_lock_alt.png")), 16, 16)
    renpy.image("taboo_break", taboo_break_image)
    thumbs_up_image = im.Scale(Image(get_file_handle("thumbs_up_small.png")), 18, 18)
    renpy.image("thumbs_up", thumbs_up_image)
    thumbs_down_image = im.Scale(Image(get_file_handle("thumbs_down_small.png")), 18, 18)
    renpy.image("thumbs_down", thumbs_down_image)

    energy_token_small_image = im.Scale(Image(get_file_handle("energy_token.png")), 18, 18)
    renpy.image("energy_token_small", energy_token_small_image)

    arousal_token_small_image = im.Scale(Image(get_file_handle("arousal_token.png")), 18, 18)
    renpy.image("arousal_token_small", arousal_token_small_image)

    question_mark_small_image = im.Scale(Image(get_file_handle("question.png")), 18, 18)
    renpy.image("question_mark_small", question_mark_small_image)

    vial_image = Image(get_file_handle("vial.png"))
    question_image = Image(get_file_handle("question.png"))

label updated_room_background(stack):
    python:
        # as long as the base game has no nice images, we use these to make navigating a little more fun
        office.background_image = room_background_image("Main_Office_Background.jpg")
        m_division.background_image = room_background_image("Marketing_Background.jpg")
        p_division.background_image = room_background_image("Production_Background.jpg")
        rd_division.background_image = room_background_image("RandD_Background.jpg")
        lobby.background_image = room_background_image("Lobby_Background.jpg")

        #As long a there is a mall background for the sex_store, replace it with our custom background (since SB uses this location)
        sex_store.background_image = room_background_image("Sex_Shop_Background.jpg")


        # continue on the hijack stack if needed
        execute_hijack_call(stack)

    # Load extra GUI images
    image serum_vial = "[vial_image.filename]"
    image question_mark = "[question_image.filename]"

    return
