init -1 python:
    ###Mod Options Test
    SB_fetish_mod_init = False

label SB_fetish_mod_init_label():
    call SB_unique_people_create() from SB_MOD_INIT_001
    $ SB_fetish_mod_init = True
    return

# TODO: Add difficulty configuration
label SB_mod_options_menu():
    "This is a test of the SB mod options menu. A menu should be displayed after this."
    menu:
        "Sex Shop Investment Returns":
            "This mod changes how much return on investment you get from the sex shop, for difficulty purposes."
            menu:
                "Lucrative (Easy)":
                    $starbuck.shop_difficulty_value = 2.0
                    "Shop returns are now lucrative."
                "Average (Normal)":
                    $starbuck.shop_difficulty_value = 1.0
                    "Shop returns are now normal."
                "Poor (Hard)":
                    $starbuck.shop_difficulty_value = 0.5
                    "Shop returns are now poor."
        "Return":
            pass
    
    return
