init 5 python:
    add_label_hijack("normal_start", "activate_strip_club_set_uniforms_label")
    add_label_hijack("after_load", "activate_strip_club_set_uniforms_label")

    def strip_club_set_uniforms_requirement():
        if get_strip_club_foreclosed_stage() >= 5:
            return True
        return False

    strip_club_set_uniforms_action = Action("Manage Stripclub Uniforms",strip_club_set_uniforms_requirement,"strip_club_set_uniforms_label")

init 2:
    screen strip_club_outfit_manager(target_wardrobe): # Brings up a list of the players current saved outfits, returns the selected outfit or None.

        default outfit_categories = {"Full": ["FullSets", "full", "get_outfit_list"], "Overwear": ["OverwearSets", "over", "get_overwear_sets_list"], "Underwear": ["UnderwearSets", "under", "get_underwear_sets_list"]} #NOTE: Key is display name, [0] is XML's category type, [1] is outfit type, [2] is function to retrive [0]
        default import_mode = {"Import": [], "Assign": []}
        add "Paper_Background.png"
        modal True
        zorder 100
        default preview_outfit = None
        default targeted_outfit = None
        default import_wardrobes = {} # Holds the wardrobes you want to be able to import into or select #NOTE: Make sure it is a list inside of a list [[]]
        python:
            import_wardrobes["Your Wardrobe"] = [[mc.designed_wardrobe]]
            import_wardrobes["Strippers"] = [[stripclub_wardrobe]]
            import_wardrobes["Waitresses"] = [[waitress_wardrobe]]
            import_wardrobes["Manager"] = [[manager_wardrobe]]
            import_wardrobes["Mistress"] = [[mistress_wardrobe]]
            import_wardrobes["BDSM performers"] = [[BDSM_performer_wardrobe]]

        python:
            temp_wardrobe = Wardrobe("Temporary Wardrobe")
            for category in import_wardrobes:
                for wardrobes in import_wardrobes[category][0]:
                    for outfit in wardrobes.outfits + mc.designed_wardrobe.outfits:
                        if outfit not in temp_wardrobe.outfits:
                            temp_wardrobe.outfits.append(outfit)

                    for outfit in wardrobes.overwear_sets + mc.designed_wardrobe.overwear_sets:
                        if outfit not in temp_wardrobe.overwear_sets:
                            temp_wardrobe.overwear_sets.append(outfit)

                    for outfit in wardrobes.underwear_sets + mc.designed_wardrobe.underwear_sets:
                        if outfit not in temp_wardrobe.underwear_sets:
                            temp_wardrobe.underwear_sets.append(outfit)

            wardrobe = temp_wardrobe

        grid __builtin__.len(outfit_categories) 1:
            for category in sorted(outfit_categories): # NOTE: Dictionary is not sorted. Don't know the best way to make it so.
                vbox:
                    xsize 480
                    frame:
                        text category style "serum_text_style" xalign 0.5
                        xfill True
                    viewport:
                        ysize 880
                        if __builtin__.len(getattr(wardrobe, outfit_categories[category][2])()) > 7:
                            scrollbars "vertical"
                        mousewheel True
                        vbox:
                            if __builtin__.len(getattr(wardrobe, outfit_categories[category][2])()) > 0: #Don't show a frame if it is empty
                                frame:
                                    vbox:
                                        for outfit in sorted(getattr(wardrobe, outfit_categories[category][2])(), key = lambda outfit: (outfit.slut_requirement, outfit.name)):  # Not sure if there's any good reason to sort XML lists since the default way it works is to place the newest outfit at the bottom which is predictable.
                                            $ effective_slut_score = calculate_outfit_slut_score(wardrobe, outfit)
                                            frame:
                                                vbox:
                                                    id str(outfit)
                                                    xfill True
                                                    textbutton outfit.name + "\n" + get_heart_image_list_cloth(effective_slut_score, 1):
                                                        xfill True
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "serum_text_style"
                                                        action [
                                                            Show("outfit_creator", None, outfit.get_copy(), target_wardrobe, outfit_type = outfit_categories[category][1]), # Bring the outfit into the outfit_creator for editing when left clicked
                                                            Hide(renpy.current_screen().screen_name)
                                                            ]
                                                        hovered Show("mannequin", None, outfit)

                                                    textbutton ("Assign to:"):
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "serum_text_style"
                                                        xfill True
                                                        action ToggleScreenVariable("targeted_outfit", renpy.get_widget(renpy.current_screen(), str(outfit)), None)

                                                    if targeted_outfit == renpy.get_widget(renpy.current_screen(), str(outfit)):
                                                        frame:
                                                            vbox:
                                                                for wardrobes in sorted(import_wardrobes):
                                                                    textbutton str(wardrobes):
                                                                        style "textbutton_no_padding_highlight"
                                                                        text_style "serum_text_style"
                                                                        xfill True

                                                                        if not import_wardrobes_has_outfit_with_name(import_wardrobes[wardrobes][0], outfit.name):
                                                                            action [
                                                                                Function(import_add_outfit_to_wardrobes, import_wardrobes[wardrobes][0], outfit, outfit_type = outfit_categories[category][1]),
                                                                                Function(renpy.notify, ("Outfit assigned to " + wardrobes)),
                                                                                ]
                                                                        else:
                                                                            if import_wardrobes_has_outfit_with_name(import_wardrobes[wardrobes][0], outfit.name):
                                                                                background "#3ffc45"
                                                                            action [
                                                                                Function(import_remove_outfit_from_wardrobes, import_wardrobes[wardrobes][0], outfit),
                                                                                Function(renpy.notify, "Outfit removed from " + wardrobes)
                                                                                ]

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.92]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return("No Return"), Hide("mannequin")]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"

label activate_strip_club_set_uniforms_label(stack):
    python:
        strip_club.add_action(strip_club_set_uniforms_action)
        execute_hijack_call(stack)
    return

label strip_club_set_uniforms_label():

    call screen strip_club_outfit_manager(mc.designed_wardrobe)

    return
