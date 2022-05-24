init 5 python:
    add_label_hijack("normal_start", "activate_myrabelle_mod_core")
    add_label_hijack("after_load", "update_myrabelle_mod_core")


label activate_myrabelle_mod_core(stack):
    python:
        #This function only runs on initial new game start
        myrabelle_mod_initialization() #Usually we only create new girls on initial start up. However, this will make them incompatible with existing savegames.
        myra_focus_progression_scene_init()
        myra_alexia_teamup_scene_init()
        # continue on the hijack stack if needed
        if myra_alexia_teamup_scene not in list_of_progression_scenes:
            list_of_progression_scenes.append(myra_alexia_teamup_scene)
        if myra_focus_progression_scene not in list_of_progression_scenes:
            list_of_progression_scenes.append(myra_focus_progression_scene)
        execute_hijack_call(stack)
    return

label update_myrabelle_mod_core(stack):
    python:
        # This function runs when loading an existing save game. If you want to make your person appear in existing savegames, use this function to check if she exists and then run the init for her if she doesn't.
        if "gaming_cafe" not in globals():
            gaming_cafe = Room("gaming_cafe", "Gaming Cafe", [], standard_gaming_cafe_backgrounds, gaming_cafe_objects, [], [gaming_cafe_grind_character_action, gaming_cafe_buy_max_level_token_action, gaming_cafe_adult_swim], False, [6,2], None, False, lighting_conditions = standard_indoor_lighting)
            list_of_places.append(gaming_cafe)

        if "myra" not in globals():
            myrabelle_mod_initialization()
            myra_focus_progression_scene_init()
            myra_alexia_teamup_scene_init()

        if "myra_focus_progression_scene" not in globals():
            myra_focus_progression_scene_init()
        else:
            myra_focus_progression_scene.compile_scenes(myra_focus_progression_scene)

        if "myra_alexia_teamup_scene" not in globals():
            myra_alexia_teamup_scene_init()
        else:
            myra_alexia_teamup_scene.compile_scenes(myra_alexia_teamup_scene)

        if myra_alexia_teamup_scene not in list_of_progression_scenes:
            list_of_progression_scenes.append(myra_alexia_teamup_scene)
        if myra_focus_progression_scene not in list_of_progression_scenes:
            list_of_progression_scenes.append(myra_focus_progression_scene)

        execute_hijack_call(stack)
    return
