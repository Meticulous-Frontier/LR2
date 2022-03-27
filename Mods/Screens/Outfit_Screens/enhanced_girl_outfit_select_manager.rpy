init 2:
    screen girl_outfit_select_manager(target_wardrobe, show_sets = False, slut_limit = the_person.sluttiness): ##Brings up a list of outfits currently in a girls wardrobe.
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
                        text "Full Outfit Selection" style "menu_text_title_style" xalign 0.5

                    viewport:

                        if __builtin__.len(target_wardrobe.get_outfit_list()) > 11:
                            scrollbars "vertical"
                        xfill True
                        yfill True
                        mousewheel True
                        vbox:
                            for outfit in sorted(target_wardrobe.get_outfit_list(), key = lambda outfit: outfit.slut_requirement):
                                textbutton outfit.name.replace("_", " ").title() + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1):
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"

                                    xfill True

                                    sensitive (outfit.slut_requirement <= slut_limit)

                                    action [Function(hide_mannequin), Return(outfit)]
                                    hovered [Function(draw_mannequin, the_person, outfit)]
                                    alternate Show("outfit_creator", None, outfit.get_copy(), "full", slut_limit, the_person.wardrobe)

            if show_sets:
                frame:
                    background "#0a142688"
                    xsize 450
                    ysize 750
                    vbox:
                        frame:
                            background "#000080"
                            xfill True
                            text "Overwear Selection" style "menu_text_title_style" xalign 0.5

                        viewport:
                            if __builtin__.len(target_wardrobe.get_overwear_sets_list()) > 11:
                                scrollbars "vertical"
                            xfill True
                            yfill True
                            mousewheel True
                            vbox:
                                for outfit in sorted(target_wardrobe.get_overwear_sets_list(), key = lambda outfit: outfit.slut_requirement):
                                    textbutton outfit.name.replace("_", " ").title() + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1):
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"

                                        xfill True

                                        sensitive (outfit.slut_requirement <= slut_limit)

                                        action [Function(hide_mannequin), Return(outfit)]
                                        hovered [Function(draw_mannequin, the_person, outfit)]
                                        alternate Show("outfit_creator", None, outfit.get_copy(), "over", slut_limit, the_person.wardrobe)


                frame:
                    background "#0a142688"
                    xsize 450
                    ysize 750
                    vbox:
                        frame:
                            background "#000080"
                            xfill True
                            text "Underwear Selection" style "menu_text_title_style" xalign 0.5

                        viewport:
                            if __builtin__.len(target_wardrobe.get_underwear_sets_list()) > 11:
                                scrollbars "vertical"
                            xfill True
                            yfill True
                            mousewheel True
                            vbox:
                                for outfit in sorted(target_wardrobe.get_underwear_sets_list(), key = lambda outfit: outfit.slut_requirement):
                                    textbutton outfit.name.replace("_", " ").title() + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1):
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"

                                        xfill True

                                        sensitive (outfit.slut_requirement <= slut_limit)

                                        action [Function(hide_mannequin), Return(outfit)]
                                        hovered [Function(draw_mannequin, the_person, outfit)]
                                        alternate Show("outfit_creator", None, outfit.get_copy(), "under", slut_limit, the_person.wardrobe)

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Function(hide_mannequin), Return("None")]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
