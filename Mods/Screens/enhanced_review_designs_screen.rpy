init 2:
    screen review_designs_screen():
        add "Science_Menu_Background.png"
        vbox:
            textbutton "Serum Designs:":
                style "textbutton_style"
                text_style "serum_text_style"
                action [
                NullAction()
                ]
            grid 2 len(mc.business.serum_designs):
                for serum_design in mc.business.serum_designs:
                    if serum_design.researched:
                        textbutton serum_design.name + " - Research Finished":
                            action [
                            ToggleScreen("serum_tooltip",None,serum_design)
                            ]
                            hovered [
                            Show("serum_tooltip",None,serum_design)
                            ]
                            style "textbutton_style"
                            text_style "serum_text_style"
                    else:
                        textbutton serum_design.name + " - " + str(serum_design.current_research) + "/" + str(serum_design.research_needed) + " Research Required":
                            action [
                            ToggleScreen("serum_tooltip", None, serum_design)
                            ]
                            hovered [
                            Show("serum_tooltip",None,serum_design)
                            ]
                            style "textbutton_style"
                            text_style "serum_text_style"

                    textbutton "Scrap Design":
                        action [
                        Function(mc.business.remove_serum_design,serum_design)
                        ]
                        style "textbutton_style"
                        text_style "serum_text_style"

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
