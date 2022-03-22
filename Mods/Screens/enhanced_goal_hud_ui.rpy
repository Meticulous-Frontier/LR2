init 2:
    screen goal_hud_ui():
        frame:
            background "Goal_Frame_1.png"
            yalign 0.5
            xysize (260, 250)
            vbox:
                textbutton "Goal Information" action Show("mc_character_sheet") style "textbutton_style" text_style "menu_text_title_style" text_size 14 xsize 245 text_align 0.5 tooltip "Complete goals to earn experience, and spend experience to improve your stats and skills."
                for goal in [mc.stat_goal,mc.work_goal,mc.sex_goal]:
                    $ goal_info = goal.name + "\n" + goal.get_reported_progress()
                    frame:
                        ysize 60
                        background None
                        bar value goal.get_progress_fraction() range 1.0 xalign 0.5 ysize 50 xfill True
                        textbutton "[goal_info]" style "transparent_style" text_style "menu_text_style" text_size 16 xalign 0.5 yanchor 0.5 yalign 0.5 action NullAction() sensitive True tooltip goal.description
