init 2:
    screen set_duties_screen(the_person, allow_changing_duties = True, show_available_duties = True, hide_on_exit = False):
        modal True
        zorder 120
        add "Paper_Background.png"
        default person_portrait = the_person.build_person_portrait()
        default person_job_info = person_info_ui_get_job_title(the_person)
        default visible_roles = ", ".join(info_detail_visible_roles(the_person))
        default available_duties = [x for x in the_person.job.available_duties if x.check_requirement(the_person)]
        default current_duties = the_person.duties
        default add_duties = []
        default remove_duties = []
        default selected_duty = None

        vbox:
            yalign 0.05
            xanchor 0.5
            xalign 0.5
            frame:
                xsize 1540
                ysize 120
                xalign 0.5
                background "#1a45a1aa"
                hbox:
                    imagebutton:
                        idle person_portrait at zoom(.7)
                        xoffset -50
                        yoffset -24
                        xsize 100
                    vbox:
                        xsize (1050 if persistent.pregnancy_pref > 0 else 1650)
                        xalign 0.5 xanchor 0.5
                        text format_titles(the_person) style "menu_text_style" size 30 xalign 0.5 yalign 0.5 yanchor 0.5 color the_person.char.who_args["color"] font the_person.char.what_args["font"]
                        text "Job: [person_job_info]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                        if visible_roles:
                            text "Special Roles: [visible_roles]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

            spacing 20
            hbox:
                xanchor 0.5
                xalign 0.5
                spacing 20
                if show_available_duties:
                    frame:
                        background "#1a45a1aa"
                        xsize 500
                        ysize 700
                        xanchor 0.5
                        xalign 0.5
                        vbox:
                            text "Available Duties" style "serum_text_style_header" size 22
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                vbox:
                                    for a_duty in sorted(list(set(available_duties) - (set(current_duties) - set(remove_duties)) - set(add_duties)), key = lambda x: x.duty_name):
                                        textbutton a_duty.duty_name:
                                            style "textbutton_style" text_style "textbutton_text_style"
                                            action SetScreenVariable("selected_duty", a_duty)
                                            sensitive True
                                            if not a_duty is selected_duty:
                                                background "#000080"

                                            else:
                                                background "#000040"

                                            hover_background "#1a45a1"
                                            insensitive_background "#222222"

                frame:
                    background "#1a45a1aa"
                    xsize 500
                    ysize 700
                    xanchor 0.5
                    xalign 0.5
                    vbox:
                        $ duties_title = "Current Duties (" + str(len(current_duties)-len(remove_duties)+len(add_duties)) + "/" + str(the_person.work_experience) + ")"
                        text duties_title style "serum_text_style_header"
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            vbox:
                                for a_duty in sorted(list(set(current_duties + add_duties) - set(remove_duties)), key = lambda x: x.duty_name):
                                    textbutton a_duty.duty_name:
                                        style "textbutton_style" text_style "textbutton_text_style"

                                        action SetScreenVariable("selected_duty", a_duty)
                                        sensitive True
                                        if not a_duty is selected_duty:
                                            background "#000080"

                                        else:
                                            background "#000040"
                                        hover_background "#1a45a1"
                                        insensitive_background "#222222"
                frame:
                    background "#1a45a1aa"
                    xsize 500
                    ysize 700
                    xanchor 0.5
                    xalign 0.5
                    vbox:
                        xanchor 0.5
                        xalign 0.5
                        if selected_duty is not None:
                            use duty_tooltip(selected_duty):
                                if allow_changing_duties: #Hide the button so we can use this as a display.
                                    if selected_duty in list(set(current_duties) - set(remove_duties)) + add_duties:
                                        if selected_duty in the_person.job.mandatory_duties:
                                            textbutton "Locked - Mandatory Duty":
                                                style "textbutton_style"
                                                text_style "textbutton_text_style"
                                                xanchor 0.5
                                                xalign 0.5
                                                action NullAction()
                                                sensitive False
                                                insensitive_background "#222222"
                                        else:
                                            textbutton "Remove Duty":
                                                style "textbutton_style"
                                                text_style "textbutton_text_style"
                                                xanchor 0.5
                                                xalign 0.5
                                                if selected_duty in add_duties:
                                                    action RemoveFromSet(add_duties, selected_duty)
                                                else:
                                                    action AddToSet(remove_duties, selected_duty)
                                                background "#000080"
                                                hover_background "#1a45a1"
                                                insensitive_background "#222222"

                                    else:
                                        $ button_name = "Add Duty"
                                        $ button_sensitive = selected_duty.check_requirement(the_person)
                                        if button_sensitive is True:
                                            if len(current_duties) - len(remove_duties) + len(add_duties) >= the_person.work_experience:
                                                $ button_sensitive = "Max Duties Reached"
                                        if isinstance(button_sensitive, basestring):
                                            $ button_name += " - " + button_sensitive
                                        textbutton button_name:
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            sensitive button_sensitive is True  #NOTE: button_sensitive can be a string, so we do direct comparison.
                                            xanchor 0.5
                                            xalign 0.5
                                            if selected_duty in remove_duties:
                                                action RemoveFromSet(remove_duties, selected_duty)
                                            else:
                                                action AddToSet(add_duties, selected_duty)
                                            background "#000080"
                                            hover_background "#1a45a1"
                                            insensitive_background "#222222"

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                if hide_on_exit: #Use this when you want ot show this screen from another. Note that you cannot change duties if just hiding/showing. (TODO: Try using run_in_new_context to call the duties_manager label)
                    action Hide("set_duties_screen")
                else:
                    action Return([add_duties, remove_duties])
            textbutton "Return" align [0.5,0.5] style "return_button_style" text_style "return_button_style"

    screen duty_tooltip(the_duty):
        frame:
            background None
            vbox:
                spacing 20
                text the_duty.duty_name style "serum_text_style_header"
                text the_duty.duty_description style "menu_text_style" size 20 text_align 0.0

                transclude
