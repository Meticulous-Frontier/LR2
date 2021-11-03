init 6 python:  # init after kaya (relationship setter)
    add_label_hijack("normal_start", "activate_sakari_mod_core")
    add_label_hijack("after_load", "update_sakari_mod_core")


label activate_sakari_mod_core(stack):
    python:
        sakari_mod_initialization()
        $ clothing_store.name = "Sak's Clothing"
        $ clothing_store.formal_name = "Sak's Clothing Store"
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_sakari_mod_core(stack):
    python:
        if "sakari" not in globals():
            sakari_mod_initialization()
            $ clothing_store.name = "Sak's Clothing"
            $ clothing_store.formal_name = "Sak's Clothing Store"
        execute_hijack_call(stack)
    return
