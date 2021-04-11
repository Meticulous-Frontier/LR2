init 2:
    screen review_designs_screen():
        add "Science_Menu_Background.png"
        default selected_serum = None

        vbox:
            xalign 0.2
            xanchor 0.5
            yalign 0.5
            frame:
                background "#888888"
                xalign 0.5
                ysize 900
                vbox:
                    frame:
                        background "#000080"
                        xsize 650
                        text "Serum Designs" style "serum_text_style_header"

                    frame:
                        background "#777777"
                        xalign 0.5

                        viewport:
                            scrollbars "vertical"
                            xsize 636
                            mousewheel True
                            hbox:
                                xalign 0.5
                                vbox:
                                    xalign 0.5
                                    for serum_design in mc.business.serum_designs:
                                        $ serum_name = serum_design.name
                                        if serum_design.researched:
                                            $ serum_name += " - {color=#98fb98}Researched{/color}"
                                        else:
                                            $ serum_name += " - " + str(serum_design.current_research) + "/" + str(serum_design.research_needed) + "{color=#cd5c5c} Required{/color}"

                                        textbutton serum_name:
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 400
                                            ysize 50
                                            if serum_design == selected_serum:
                                                action SetScreenVariable("selected_serum", None)
                                            else:
                                                action SetScreenVariable("selected_serum",serum_design)

                                vbox:
                                    xalign 0.5
                                    for serum_design in mc.business.serum_designs:
                                        textbutton "Scrap Design":
                                            action [
                                                Function(mc.business.remove_serum_design, serum_design),
                                                SetScreenVariable("selected_serum", None)
                                            ]
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 230
                                            ysize 50

        if serum_design == selected_serum:
            use serum_tooltip(selected_serum, given_align = (0.9,0.09), given_anchor = (1.0,0.0), allow_edit = True)

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return(), Hide("serum_tooltip")]
            textbutton "Return" align [0.5,0.5] style "return_button_style"
