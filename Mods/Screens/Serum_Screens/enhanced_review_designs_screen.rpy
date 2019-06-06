init 2:
    screen review_designs_screen():
        add "Science_Menu_Background.png"
        vbox:
            xalign 0.2
            xanchor 0.5
            yalign 0.1
            frame:
                background "#888888"
                xalign 0.5
                ysize 900
                vbox:
                    xalign 0.5
                    textbutton "Serum Designs":
                        style "textbutton_style"
                        text_style "serum_text_style"
                        xsize 650
                        xalign 0.5
                        action [
                        NullAction()
                        ]

                    frame:
                        background "#777777"
                        xalign 0.5

                        viewport:
                            scrollbars "vertical"
                            xsize 650
                            mousewheel True
                            hbox:
                                xalign 0.5
                                vbox:
                                    xalign 0.5
                                    for serum_design in mc.business.serum_designs:
                                        if serum_design.researched:
                                            textbutton "[serum_design.name] - {color=#98fb98}Researched{/color}":
                                                action [
                                                ToggleScreen("serum_tooltip", None, serum_design)
                                                ]
                                                hovered [
                                                Show("serum_tooltip", None, serum_design)
                                                ]
                                                style "textbutton_style"
                                                text_style "serum_text_style"
                                                xsize 400
                                                ysize 50
                                        else:
                                            textbutton "[serum_design.name]: " + str(serum_design.current_research) + "/" + str(serum_design.research_needed) + "{color=#cd5c5c} Required{/color}":
                                                action [
                                                ToggleScreen("serum_tooltip", None, serum_design)
                                                ]
                                                hovered [
                                                Show("serum_tooltip", None, serum_design)
                                                ]
                                                style "textbutton_style"
                                                text_style "serum_text_style"
                                                xsize 400
                                                ysize 50

                                vbox:
                                    xalign 0.5
                                    for serum_design in mc.business.serum_designs:
                                        textbutton "Scrap Design":
                                            action [
                                            Function(mc.business.remove_serum_design, serum_design)
                                            ]
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 250
                                            ysize 50

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
