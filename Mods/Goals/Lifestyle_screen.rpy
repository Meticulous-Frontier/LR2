# This file contains the provisions for the lifetstyle coach screen for setting personal goal lists.
init -2 style textbutton_green_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    padding [5,5]
    margin [5,5]
    background "#44BB44"
    insensitive_background "#222222"
    hover_background "#aaaaaa"

screen lifestyle_goal_sheet():
    add "Paper_Background.png"
    modal True
    zorder 100
    vbox:
        xanchor 0.5
        xalign 0.5
        yalign 0.1
        frame:
            background "#1a45a1aa"
            xanchor 0.5
            xalign 0.5
            vbox:
                xsize 770
                text mc.name + " " + mc.last_name style "menu_text_style" size 40
                text "Goal Lists" style "menu_text_style" size 30
                text "Each category requires a minimum of " + str(MIN_GOAL_LiST_LENGTH) + " selections" size 24
        null height 60
        hbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.4
            spacing 40

            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:

                    xsize 500
                    text "Stat Goals" style "menu_text_style" size 32 xalign 0.5
                    text "Current Total: " + str(len(stat_goals)) style "menu_text_style" size 24 xalign 0.5
                    for stat_goal in stat_goals_options_list:
                        hbox:
                            xalign 0.5

                            if stat_goal in stat_goals:
                                textbutton stat_goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_green_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action Function(toggle_goal_avail, stat_goal)
                                    hovered [
                                    None
                                    ]
                            else:
                                textbutton stat_goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action Function(toggle_goal_avail, stat_goal)
                                    hovered [
                                    None
                                    ]
            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:

                    xsize 500
                    text "Work Goals" style "menu_text_style" size 32 xalign 0.5
                    text "Current Total: " + str(len(work_goals)) style "menu_text_style" size 24 xalign 0.5
                    for work_goal in work_goals_options_list:
                        hbox:
                            xalign 0.5
                            if work_goal in work_goals:
                                textbutton work_goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_green_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action Function(toggle_goal_avail, work_goal)
                                    hovered [
                                    None
                                    ]
                            else:
                                textbutton work_goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action Function(toggle_goal_avail, work_goal)
                                    hovered [
                                    None
                                    ]

            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:

                    xsize 500
                    text "Sex Goals" style "menu_text_style" size 32 xalign 0.5
                    text "Current Total: " + str(len(sex_goals)) style "menu_text_style" size 24 xalign 0.5
                    for sex_goal in sex_goals_options_list:
                        hbox:
                            xalign 0.5

                            if sex_goal in sex_goals:
                                textbutton sex_goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_green_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action Function(toggle_goal_avail, sex_goal)
                                    hovered [
                                    None
                                    ]
                            else:
                                textbutton sex_goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action Function(toggle_goal_avail, sex_goal)
                                    hovered [
                                    None
                                    ]


                #$ tooltip = GetTooltip()


    # frame:
    #     background None
    #     anchor [0.5,0.5]
    #     align [0.2,0.88]
    #     xysize [500,125]
    #     imagebutton:
    #         align [0.5,0.5]
    #         auto "gui/button/choice_%s_background.png"
    #         focus_mask "gui/button/choice_idle_background.png"
    #         action Show("mc_character_sheet")
    #     textbutton "Character Sheet" align [0.5,0.5] text_style "return_button_style"

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [Return(True), Hide("serum_tooltip")]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"
