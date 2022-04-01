init 3:
    # NOTE: Uses seperate mannequin screen and has no real use of the "preview_outfit" Outfit
    # Thinking of adding "Import" directly from this screen as well, but seems redundant.
    # Added the ability enter outfit editor by right clicking an outfit. Needs changes to script.rpy to work as intended. Reason: Easy to edit company wardrobe by entering the Remove an Outfit section and review / edit them from there.
    screen outfit_delete_manager(target_wardrobe, show_sets = True, slut_limit = 9999): ##This screen is used and shared for MC, Company Uniforms and Person. Script.rpy should be calling correct Wardrobe at all times so no default currently needed. NOTE: Script.rpy does not support editing of outfits by default from this screen, but slight additions to it will make it work. Tested. Will propose the change to Vren at later time, pretty much copy paste from different section.
        #add "Paper_Background.png"

        modal True
        zorder 99 #Allow it to be hidden below outfit_creator
        default preview_outfit = None
        default import_selection = False
        default mannequin = the_person

        hbox:
            xalign 0.1
            yalign 0.1
            spacing 20
            frame:
                background "#0a142688"
                xsize 450
                ysize 750


                vbox:
                    frame:
                        background "#000080"
                        xfill True
                        text "Full Outfit Deletion" style "menu_text_title_style" xalign 0.5

                    viewport:

                        if __builtin__.len(target_wardrobe.get_outfit_list()) > 11:
                            scrollbars "vertical"
                        xfill True
                        yfill True
                        mousewheel True
                        vbox:
                            for outfit in sorted(target_wardrobe.get_outfit_list(), key = lambda outfit: outfit.slut_requirement):
                                textbutton "Delete " + outfit.name.replace("_", " ").title() + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1):
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"

                                    xfill True

                                    sensitive (outfit.slut_requirement <= slut_limit)

                                    action [Function(target_wardrobe.remove_outfit,outfit)]

                                    if the_person is not None:
                                        hovered Function(draw_mannequin, the_person, outfit)
                                        alternate Show("outfit_creator", None, outfit.get_copy(), "full", slut_limit, the_person.wardrobe)
                                    else:
                                        hovered Function(draw_average_mannequin, outfit)

            if show_sets:
                frame:
                    background "#0a142688"
                    xsize 450
                    ysize 750
                    vbox:
                        frame:
                            background "#000080"
                            xfill True
                            text "Overwear Deletion" style "menu_text_title_style" xalign 0.5

                        viewport:
                            if __builtin__.len(target_wardrobe.get_overwear_sets_list()) > 11:
                                scrollbars "vertical"
                            xfill True
                            yfill True
                            mousewheel True
                            vbox:
                                for outfit in sorted(target_wardrobe.get_overwear_sets_list(), key = lambda outfit: outfit.slut_requirement):
                                    textbutton "Delete " + outfit.name.replace("_", " ").title() + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1):
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"

                                        xfill True

                                        sensitive (outfit.slut_requirement <= slut_limit)

                                        action [Function(target_wardrobe.remove_outfit,outfit)]
                                        if the_person is not None:
                                            hovered Function(draw_mannequin, the_person, outfit)
                                            alternate Show("outfit_creator", None, outfit.get_copy(), "over", slut_limit, the_person.wardrobe)
                                        else:
                                            hovered Function(draw_average_mannequin, outfit)


                frame:
                    background "#0a142688"
                    xsize 450
                    ysize 750
                    vbox:
                        frame:
                            background "#000080"
                            xfill True
                            text "Underwear Deletion" style "menu_text_title_style" xalign 0.5

                        viewport:
                            if __builtin__.len(target_wardrobe.get_underwear_sets_list()) > 11:
                                scrollbars "vertical"
                            xfill True
                            yfill True
                            mousewheel True
                            vbox:
                                for outfit in sorted(target_wardrobe.get_underwear_sets_list(), key = lambda outfit: outfit.slut_requirement):
                                    textbutton "Delete " + outfit.name.replace("_", " ").title() + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1):
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"

                                        xfill True

                                        sensitive (outfit.slut_requirement <= slut_limit)

                                        action [Function(target_wardrobe.remove_outfit,outfit)]
                                        if the_person is not None:
                                            hovered Function(draw_mannequin, the_person, outfit)
                                            alternate Show("outfit_creator", None, outfit.get_copy(), "under", slut_limit, the_person.wardrobe)
                                        else:
                                            hovered Function(draw_average_mannequin, outfit)

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return("No Return"), Function(hide_mannequin)]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
