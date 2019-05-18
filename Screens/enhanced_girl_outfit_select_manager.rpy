init 2:
    screen girl_outfit_select_manager(target_wardrobe, show_sets = True, slut_limit = the_person.sluttiness): ##Brings up a list of outfits currently in a girls wardrobe.
        add "Paper_Background.png"
        modal True
        zorder 99 #Allow it to be hidden below outfit_creator
        default preview_outfit = None
        hbox:
            xalign 0.1
            yalign 0.1
            spacing 20
            frame:
                background "#888888"
                xsize 450
                ysize 750
                hbox:
                    vbox:
                        textbutton "Full Outfits"  action NullAction() style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5
                        viewport:
                            scrollbars "vertical"
                            ysize 750
                            xsize 225
                            mousewheel True
                            vbox:
                                for outfit in target_wardrobe.get_outfit_list():
                                    textbutton "Select "+outfit.name+ "\n(Sluttiness " +str(outfit.slut_requirement) +")" action [Return(outfit), Hide("mannequin")] hovered Show("mannequin", None, outfit) sensitive (outfit.slut_requirement <= slut_limit) alternate Show("outfit_creator", None, outfit.get_copy(), the_person.wardrobe) style "textbutton_style" text_style "outfit_description_style" xsize 210

                    vbox:
                        textbutton "Import Design" action ToggleVariable("import_selection") style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5
                        if import_selection:
                            viewport:
                                scrollbars "vertical"
                                mousewheel True
                                xsize 225
                                ysize 750
                                vbox:
                                    for n in os.listdir("game/wardrobes/"):
                                        textbutton n action [Show("import_outfit_manager", None, target_wardrobe, n)] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5

            if show_sets:
                frame:
                    background "#888888"
                    xsize 450
                    ysize 750
                    viewport:
                        scrollbars "vertical"
                        xsize 450
                        ysize 750
                        mousewheel True
                        vbox:
                            text "Overwear Sets" style "menu_text_style" size 30
                            for outfit in target_wardrobe.get_overwear_sets_list():
                                textbutton "Select "+outfit.name+ "\n(Sluttiness " +str(outfit.get_overwear_slut_score()) +")" action [Return(outfit), Hide("mannequin")] hovered Show("mannequin", None, outfit) sensitive (outfit.slut_requirement <= slut_limit) alternate Show("outfit_creator", None, outfit.get_copy(), the_person.wardrobe) style "textbutton_style" text_style "outfit_description_style" xsize 210

                frame:
                    background "#888888"
                    xsize 450
                    ysize 750
                    viewport:
                        scrollbars "vertical"
                        xsize 450
                        ysize 750
                        mousewheel True
                        vbox:
                            text "Underwear Sets" style "menu_text_style" size 30
                            for outfit in target_wardrobe.get_underwear_sets_list():
                                textbutton "Select "+outfit.name+ "\n(Sluttiness " +str(outfit.get_underwear_slut_score()) +")" action [Return(outfit), Hide("mannequin")] hovered Show("mannequin", None, outfit) sensitive (outfit.slut_requirement <= slut_limit) alternate Show("outfit_creator", None, outfit.get_copy(), the_person.wardrobe) style "textbutton_style" text_style "outfit_description_style" xsize 210

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return("None"), Hide("mannequin")]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
