# Assign Division Daily Serum UI
# Based on screen designed by DaMatt

init 2 python:
    config.label_overrides["set_serum_description"] = "set_serum_description_enhanced"

    def get_division_serum_name(division):
        serum = get_division_serum(division)
        if serum:
            return serum.name
        else:
            return "No serum"

    def get_division_serum(division):
        if not hasattr(division[1], division[2]):
            setattr( division[1], division[2], None);
        return getattr(division[1], division[2])

    def set_division_serum(division, serum):
        setattr( division[1], division[2], serum)


label set_serum_description_enhanced:
    call screen assign_division_serum()


init 2:
    screen assign_division_serum():
        add "Science_Menu_Background.png"

        default division_selected = -1
        default division_serums = [
            ["Research", mc.business, "r_serum"],
            ["Production", mc.business, "p_serum"],
            ["Supply", mc.business, "s_serum"],
            ["Marketing", mc.business, "m_serum"],
            ["Human Resources", mc.business, "h_serum"],
            ["Strippers", mc.business, "strippers_serum"],
            ["Waitresses", mc.business, "waitresses_serum"],
            ["BDSM performers", mc.business, "bdsm_performers_serum"],
            ["Manager/Mistress", mc.business, "manager_serum"],
        ]

        vbox:
            xalign 0.5
            xanchor 0.5
            yalign 0.05
            yanchor 0.0
            spacing 20
            frame:
                background "#1a45a1aa"
                xsize 1860
                ysize 60
                text "Assign Daily Serum Dose" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_style"

            hbox:
                vbox:
                    xsize 500
                    yalign 0.0

                    frame:
                        background "#777777"
                        xalign 0.5

                        hbox:
                            xalign 0.5
                            vbox:
                                frame:
                                    xsize 500
                                    ysize 50
                                    background "#000080"
                                    text "Division" style "serum_text_style_header" 

                                viewport:
                                    xsize 500
                                    ysize 700
                                    xalign 0.5
                                    spacing 0

                                    vbox:
                                        for division in range(0,__builtin__.len(division_serums)):
                                            button:
                                                vbox:
                                                    xalign 0.5
                                                    text division_serums[division][0] style "serum_text_style"
                                                    text get_division_serum_name(division_serums[division]) style "serum_text_style" size 14
                                                style "textbutton_style"
                                                if division_selected == division:
                                                    background "#000080"
                                                    hover_background "#0030A0"
                                                else:
                                                    background "#222222"
                                                    hover_background "#333333"
                                                xsize 500
                                                action SetScreenVariable("division_selected", division)

                null width 10

                vbox:
                    xsize 500
                    if division_selected > -1:

                        frame:
                            background "#777777"
                            xalign 0.5

                            hbox:
                                xalign 0.5
                                vbox:
                                    frame:
                                        xsize 500
                                        ysize 50
                                        background "#000080"
                                        text "Assign Serum" style "serum_text_style_header" 

                                    viewport:
                                        scrollbars "vertical"
                                        mousewheel True
                                        xsize 500
                                        ysize 700
                                        xalign 0

                                        vbox:

                                            button:
                                                xsize 500
                                                ysize 80
                                                vbox:
                                                    xalign 0.5
                                                    text "No serum" style "serum_text_style"
                                                style "textbutton_style"
                                                sensitive True
                                                if get_division_serum(division_serums[division_selected]) is None:
                                                    background "#000080"
                                                    hover_background "#0030A0"
                                                else:
                                                    background "#222222"
                                                    hover_background "#333333"
                                                action Function(set_division_serum, division_serums[division_selected], None)

                                            for serum in sorted(mc.business.inventory.serums_held, key = lambda e: e[0].name):
                                                button:
                                                    xsize 500
                                                    vbox:
                                                        xalign 0.5
                                                        text serum[0].name style "serum_text_style"
                                                        text "Available: " + str(serum[1]) style "serum_text_style" size 14
                                                    style "textbutton_style"
                                                    sensitive True
                                                    if get_division_serum(division_serums[division_selected]) == serum[0]:
                                                        background "#000080"
                                                        hover_background "#0030A0"
                                                    else:
                                                        background "#222222"
                                                        hover_background "#333333"
                                                    hovered [
                                                        Show("serum_tooltip", None, serum[0], 0.97, 0.12)
                                                    ]
                                                    unhovered [
                                                        Hide("serum_tooltip")
                                                    ]                                   
                                                    action Function(set_division_serum, division_serums[division_selected], serum[0])

            frame:
                background None
                anchor [0.5,0.5]
                align [0.5,0.55]
                xysize [500,120]
                imagebutton:
                    align [0.5,0.5]
                    auto "gui/button/choice_%s_background.png"
                    focus_mask "gui/button/choice_idle_background.png"
                    action [Hide("assign_division_serum"), Return(), Hide("serum_tooltip")]
                textbutton "Return" align [0.5,0.5] text_style "return_button_style"
