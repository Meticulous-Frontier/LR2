init -1 python:
    ###Mod Options Test
    mod_option_test_choice = "0"
    SB_fetish_mod_init = False

init 1 python:
    ###     object handle       Displayed Menu Name     Menu Label - MUST MATCH LABEL OF MOD OPTIONS MENU (See below)
    SB_mod_options = ["SB Mod Options","SB_mod_options_menu"]
    ### append object handle to mod_options_list. Array is declared at -1, append must be at 0+
    mod_options_list.append(SB_mod_options)
    ### Alternativey could do the following
    ### mod_options_list.append(["Mod options test2","mod_options_test_menu2"])
init 2 python:
    def SB_fetish_mod_init_requirement():
        if SB_fetish_mod_init == False:
            return True
        return False

    SB_fetish_mod_init_action = Action("Add Starbuck's Content Mod", SB_fetish_mod_init_requirement, "SB_fetish_mod_init_label",
        menu_tooltip = "Activates the mod")
    mod_list.append(SB_fetish_mod_init_action)

label SB_fetish_mod_init_label():
    call SB_unique_people_create() from SB_MOD_INIT_001
    $ SB_fetish_mod_init = True
    return


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
            ###Returns to PC menu
            $ renpy.jump("pc_loop")
    #"You have chosen option [mod_option_test_choice]"
    ###Loop the menu
    $ renpy.jump("SB_mod_options_menu")
