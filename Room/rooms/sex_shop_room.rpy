init 5 python:
    add_label_hijack("normal_start", "updated_sex_store_background")  
    add_label_hijack("after_load", "updated_sex_store_background")

label updated_sex_store_background(stack):
    python:
        sex_store.background_image = Image(room_background_image("Sex_Shop_Background.jpg")) #As long a there is a mall background for the sex_store, replace it with our custom background

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return