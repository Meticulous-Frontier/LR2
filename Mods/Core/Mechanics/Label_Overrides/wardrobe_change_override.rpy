# override the ask to change wardrobe dialog with the new menu style
init 5 python:
    config.label_overrides["wardrobe_change_label"] = "wardrobe_change_label_enhanced"

    def build_wardrobe_change_menu():
        return ["Choose", ["Add an outfit", "add"], ["Delete an outfit", "delete"], ["Wear an outfit right now", "wear"], ["Back", "back"]]

label wardrobe_change_label_enhanced(the_person):
    if "build_menu_items" in globals():
        call screen main_choice_display(build_menu_items([build_wardrobe_change_menu()]))
    else:
        call screen main_choice_display([build_wardrobe_change_menu()])

    $ picked_option = _return

    if picked_option == "add":
        mc.name "[the_person.title], I've got something I'd like you to wear for me."
        $ renpy.scene("Active")
        call screen outfit_select_manager()
        $ the_person.draw_person()
        if _return == "No Return":
            mc.name "On second thought, never mind."
            return

        $ new_outfit = _return
        menu:
            "Save as a full outfit":
                $ outfit_type = "full"
            "Save as an underwear set" if new_outfit.is_suitable_underwear_set():
                $ outfit_type = "under"
            "Save as an underwear set (disabled)" if not new_outfit.is_suitable_underwear_set():
                pass
            "Save as an over wear set" if new_outfit.is_suitable_overwear_set():
                $ outfit_type = "over"
            "Save as an over wear set (disabled)" if not new_outfit.is_suitable_overwear_set():
                pass
            "Forget it":
                $ outfit_type = "none"

        if outfit_type != "none":
            if the_person.judge_outfit(new_outfit, as_underwear = outfit_type == "under", as_overwear = outfit_type == "over"):
                $ the_person.add_outfit(new_outfit,outfit_type)
                $ the_person.call_dialogue("clothing_accept")
            else:
                $ the_person.call_dialogue("clothing_reject")
        $ del new_outfit

    elif picked_option == "delete":
        mc.name "[the_person.title], lets have a talk about what you've been wearing."
        $ renpy.scene("Active")
        call screen outfit_delete_manager(the_person.wardrobe)
        $ the_person.review_outfit(dialogue = False)
        $ the_person.draw_person()

    elif picked_option == "wear":
        mc.name "[the_person.title], I want you to get changed for me."
        $ renpy.scene("Active")
        call screen girl_outfit_select_manager(the_person.wardrobe, show_sets = True, slut_limit = the_person.effective_sluttiness() + 20)
        if _return != "None":
            $ the_person.set_outfit(_return)
            if the_person.update_outfit_taboos():
                "[the_person.title] seems nervous wearing her new outfit in front of you, but quickly warms up to it."
            the_person.char "Is this better?"
        else:
            $ the_person.review_outfit(dialogue = False)
        $ the_person.draw_person()
    return
