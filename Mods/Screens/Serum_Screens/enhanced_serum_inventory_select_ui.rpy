init 2:
    screen serum_inventory_select_ui(the_inventory, the_person = None): #Used to let the player select a serum from an inventory.
        add "Science_Menu_Background.png"
        frame:
            background "#888888"
            xsize 400
            ysize 1000
            xalign 0.05
            yalign 0.05
            anchor (0.0,0.0)
            vbox:
                frame:
                    background "#000080"
                    xsize 380
                    text "Serum Available" style "serum_text_style_header"

                for serum in the_inventory.serums_held:
                    textbutton serum[0].name + " - " + str(serum[1]) + " Doses":
                        style "textbutton_style"
                        text_style "serum_text_style"
                        xsize 380

                        xalign 0.5
                        xanchor 0.5
                        yalign 0.5
                        yanchor 0.5

                        action [Hide("serum_tooltip"),Return(serum[0])]
                        hovered Show("serum_tooltip",None,serum[0], given_align = (0.9,0.1), given_anchor = (1.0,0.0))

        if the_person:
            frame:
                background None
                anchor [0.5, 0.5]
                align [0.5,0.2]
                use serum_tolerance_indicator(the_person)

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Hide("serum_tooltip"), Return("None")]
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
