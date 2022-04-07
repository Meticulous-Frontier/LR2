# override the ask to change wardrobe dialog with the new menu style
init 5 python:
    config.label_overrides["wardrobe_change_label"] = "wardrobe_change_label_enhanced"

    def build_wardrobe_change_menu():
        return ["Choose", ["Add an outfit", "add"], ["Delete an outfit", "delete"], ["Wear an outfit right now", "wear"], ["Back", "back"]]

    def build_wardrobe_change_save_menu(outfit):
        option_list = []
        option_list.append("Save Outfit As")
        option_list.append(["Full outfit", "full"])
        if outfit.is_suitable_underwear_set():
            option_list.append(["Underwear set", "under"])
        if outfit.is_suitable_overwear_set():
            option_list.append(["Overwear set", "over"])
        option_list.append(["Forget it", "none"])
        return option_list

label wardrobe_change_label_enhanced(the_person):
    call screen enhanced_main_choice_display(build_menu_items([build_wardrobe_change_menu()]))
    $ strip_choice = _return

    if strip_choice == "add":
        mc.name "[the_person.title], I've got something I'd like you to wear for me."
        $ clear_scene()
        call outfit_master_manager(main_selectable = True) from _call_outfit_master_manager_change_enhanced
        $ the_person.draw_person()
        if not _return:
            mc.name "On second thought, never mind."
            return

        if isinstance(_return, list): # Newer versions
            $ new_outfit = _return[1] #Select the outfit from the returned list
        else: #Compatability for older versions.
            $ new_outfit = _return

        call screen enhanced_main_choice_display(build_menu_items([build_wardrobe_change_save_menu(new_outfit)]))
        $ outfit_type = _return

        if outfit_type != "none":
            if the_person.judge_outfit(new_outfit, as_underwear = outfit_type == "under", as_overwear = outfit_type == "over"):
                $ the_person.add_outfit(new_outfit,outfit_type)
                $ the_person.call_dialogue("clothing_accept")
            else:
                $ the_person.call_dialogue("clothing_reject")
        $ del new_outfit

    elif strip_choice == "delete":
        mc.name "[the_person.title], let's have a talk about what you've been wearing."
        $ clear_scene()
        call screen outfit_delete_manager(the_person.wardrobe)
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person()

    elif strip_choice == "wear":
        mc.name "[the_person.title], I want you to get changed for me."
        $ clear_scene()
        call screen girl_outfit_select_manager(the_person.wardrobe, slut_limit = the_person.effective_sluttiness() + 20)
        if _return != "None":
            $ the_person.set_outfit(_return)
            if the_person.update_outfit_taboos():
                "[the_person.title] seems nervous wearing her new outfit in front of you, but quickly warms up to it."
            the_person "Is this better?"
        else:
            $ the_person.apply_planned_outfit()
        $ the_person.draw_person()
    return
