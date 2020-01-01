init 5 python:
    add_label_hijack("normal_start", "updated_room_background")
    add_label_hijack("after_load", "updated_room_background")

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

        # Load extra GUI images
        thumbs_up_image = Image(get_file_handle("thumbs_up_small.png"))
        thumbs_down_image = Image(get_file_handle("thumbs_down_small.png"))
        vial_image = Image(get_file_handle("vial.png"))


        # continue on the hijack stack if needed
        execute_hijack_call(stack)

    image thumbs_up = "[thumbs_up_image.filename]"
    image thumbs_down = "[thumbs_down_image.filename]"
    image serum_vial = "[vial_image.filename]"

    return
