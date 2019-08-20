init 2:
    screen girl_outfit_select_manager(target_wardrobe, show_sets = True, slut_limit = the_person.sluttiness): ##Brings up a list of outfits currently in a girls wardrobe.
        #add "Paper_Background.png"

        $ hide_ui()
        modal True
        zorder 99 #Allow it to be hidden below outfit_creator
        default preview_outfit = None
        default import_selection = False
        hbox:
            xalign 0.1
            yalign 0.1
            spacing 20
            frame:
                background "#888888"
                xsize 450
                ysize 750


                vbox:
                    frame:
                        background "#000080"
                        xfill True
                        text "Full Outfit Selection" style "serum_text_style"

                    viewport:

                        if len(target_wardrobe.get_outfit_list()) > 11:
                            scrollbars "vertical"
                        xfill True
                        yfill True
                        mousewheel True
                        vbox:
                            for outfit in sorted(target_wardrobe.get_outfit_list(), key = lambda outfit: outfit.slut_requirement):
                                textbutton "" + outfit.name + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1) +"":
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"

                                    xfill True

                                    sensitive (outfit.slut_requirement <= slut_limit)

                                    action [Return(outfit), Hide("mannequin")]
                                    hovered [Function(draw_mannequin, the_person, outfit)]
                                    alternate Show("outfit_creator", None, outfit.get_copy(), the_person.wardrobe)

            if show_sets:
                frame:
                    background "#888888"
                    xsize 450
                    ysize 750
                    vbox:
                        frame:
                            background "#000080"
                            xfill True
                            text "Overwear Selection" style "serum_text_style"

                        viewport:
                            if len(target_wardrobe.get_overwear_sets_list()) > 11:
                                scrollbars "vertical"
                            xfill True
                            yfill True
                            mousewheel True
                            vbox:
                                for outfit in sorted(target_wardrobe.get_overwear_sets_list(), key = lambda outfit: outfit.slut_requirement):
                                    textbutton "" + outfit.name + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1) +"":
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"

                                        xfill True

                                        sensitive (outfit.slut_requirement <= slut_limit)

                                        action [Return(outfit), Hide("mannequin")]
                                        hovered [Function(draw_mannequin, the_person, outfit)]
                                        alternate Show("outfit_creator", None, outfit.get_copy(), the_person.wardrobe)


                frame:
                    background "#888888"
                    xsize 450
                    ysize 750
                    vbox:
                        frame:
                            background "#000080"
                            xfill True
                            text "Underwear Selection" style "serum_text_style"

                        viewport:
                            if len(target_wardrobe.get_underwear_sets_list()) > 11:
                                scrollbars "vertical"
                            xfill True
                            yfill True
                            mousewheel True
                            vbox:
                                for outfit in sorted(target_wardrobe.get_underwear_sets_list(), key = lambda outfit: outfit.slut_requirement):
                                    textbutton "" + outfit.name + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1) +"":
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"

                                        xfill True

                                        sensitive (outfit.slut_requirement <= slut_limit)

                                        action [Return(outfit), Hide("mannequin")]
                                        hovered [Function(draw_mannequin, the_person, outfit)]
                                        alternate Show("outfit_creator", None, outfit.get_copy(), the_person.wardrobe)

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return("None"), Hide("mannequin"), Function(show_ui)]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
