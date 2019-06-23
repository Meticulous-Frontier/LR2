init 5 python:
    config.label_overrides["outfit_design_loop"] = "outfit_design_loop_enhanced"

label outfit_design_loop_enhanced:
    menu:
        "Create a new outfit.":
            call create_outfit(None) from _call_create_outfit_enhanced

        "Load an outfit." if mc.designed_wardrobe.get_count() > 0:
            call screen outfit_select_manager(show_export = True, show_sets = True)
            if not _return == "No Return":
                call create_outfit(_return) from _call_create_outfit_1_enhanced

        "Delete an outfit." if mc.designed_wardrobe.get_count() > 0:
            call screen outfit_delete_manager(mc.designed_wardrobe)

        "Back":
            return
    return