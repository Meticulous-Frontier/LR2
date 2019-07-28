init 5 python:
    add_label_hijack("normal_start", "updated_room_background")  
    add_label_hijack("after_load", "updated_room_background")

label updated_room_background(stack):
    python:
        # as long as the base game has no nice images, we use these to make navigating a little more fun
        office.background_image = Image(room_background_image("Main_Office_Background.jpg"))
        m_division.background_image = Image(room_background_image("Marketing_Background.jpg"))
        p_division.background_image = Image(room_background_image("Production_Background.jpg"))
        rd_division.background_image = Image(room_background_image("RandD_Background.jpg"))
        lobby.background_image = Image(room_background_image("Lobby_Background.jpg"))

        #As long a there is a mall background for the sex_store, replace it with our custom background (since SB uses this location)
        sex_store.background_image = Image(room_background_image("Sex_Shop_Background.jpg")) 

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return