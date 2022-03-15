init 5 python:
    add_label_hijack("normal_start", "activate_myrabelle_mod_core")
    add_label_hijack("after_load", "update_myrabelle_mod_core")


label activate_myrabelle_mod_core(stack):
    python:
        #This function only runs on initial new game start
        myrabelle_mod_initialization() #Usually we only create new girls on initial start up. However, this will make them incompatible with existing savegames.

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_myrabelle_mod_core(stack):
    python:
        # This function runs when loading an existing save game. If you want to make your person appear in existing savegames, use this function to check if she exists and then run the init for her if she doesn't.
        if "myra" not in globals():
            myrabelle_mod_initialization()
        execute_hijack_call(stack)
    return
