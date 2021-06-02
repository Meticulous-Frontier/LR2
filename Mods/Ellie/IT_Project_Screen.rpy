init 5 python:
    business_proj_back = Image(get_file_handle("frame.png"))
    nanobot_proj_back = Image(get_file_handle("frame.png"))
    proj_desc_back = Image(get_file_handle("frame.png"))
    prog_bar_left = Image(get_file_handle("left.png"))
    prog_bar_right = Image(get_file_handle("right.png"))
    it_imagebutton_active = Image(get_file_handle("IT_button_a_active.png"))
    it_imagebutton_hover = Image(get_file_handle("IT_button_a_hover.png"))
    it_imagebutton_idle = Image(get_file_handle("IT_button_a_idle.png"))
    it_imagebutton_inactive = Image(get_file_handle("IT_button_a_inactive.png"))
    it_imagebutton_locked = Image(get_file_handle("IT_button_a_locked.png"))




init 5:
    screen it_project_screen():
        add "IT_Background.png"
        modal True
        zorder 100
        use screen_IT_active_project()
        use screen_IT_return_button()
        vbox:
            #xanchor 0.5
            #xalign 0.5
            xcenter 960
            yalign 0.2
            # background "#1a45a1aa"
            text "Manage your IT projects" style "menu_text_title_style" size 48 xanchor 0.5 xalign 0.5
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
                        ysize 300
                        textbutton "Business Project":
                            text_style "menu_text_title_style"
                            text_size 40
                            #xalign 0.5
                            action [Hide("it_project_screen"),
                                    Show("business_project_screen")]
                            # sensitive perk_system.get_ability_clickable(ability_perk)
                            background Frame(business_proj_back, 5,5)
                            insensitive_background "#222222"
                            xalign 0.5
                            yalign 0.4
                            ypadding 30
                            xpadding 30
                            ysize 150
                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 500
                        ysize 300
                        textbutton "Nanobot Project":
                            text_style "menu_text_title_style"
                            text_size 40
                            #xalign 0.5
                            action [Hide("it_project_screen"),
                                    Show("nanobot_project_screen")]
                            # sensitive perk_system.get_ability_clickable(ability_perk)
                            background Frame(business_proj_back, 5,5)
                            insensitive_background "#222222"
                            xalign 0.5
                            yalign 0.4
                            ypadding 30
                            xpadding 30
                            ysize 150

    screen nanobot_project_screen():
        add "IT_Background.png"
        modal True
        zorder 100
        use screen_IT_active_project()
        use screen_IT_return_button()
        vbox:

            xcenter 960
            yalign 0.1
            # background "#1a45a1aa"
            text "Select a New Nanobot Project" style "menu_text_title_style" size 48 xanchor 0.5 xalign 0.5
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

                        xsize 300
                        text "Basic Bots" style "menu_text_title_style" size 32 xalign 0.5
                        for proj in IT_get_basic_bot_projects():
                            hbox:
                                xalign 0.5
                                if proj not in mc.business.IT_projects:
                                    if proj.requirement() == True:
                                        imagebutton:
                                            insensitive it_imagebutton_inactive
                                            idle it_imagebutton_idle
                                            hover it_imagebutton_hover
                                            selected_idle it_imagebutton_active
                                            selected_hover it_imagebutton_hover
                                            action Function (set_active_IT_project, proj)
                                            sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                            if mc.business.IT_project_in_progress != None:
                                                selected proj == mc.business.IT_project_in_progress[0]
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    elif proj.requirement():
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    else:
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]

                                if proj in mc.business.IT_projects:
                                    imagebutton:
                                        insensitive it_imagebutton_inactive
                                        idle it_imagebutton_inactive
                                        hover it_imagebutton_hover
                                        selected proj in mc.business.active_IT_projects
                                        selected_idle it_imagebutton_active
                                        selected_hover it_imagebutton_hover
                                        action Function (IT_toggle_project, proj)
                                        sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                        hovered [
                                            Show("IT_tooltip",None,proj)
                                            ]

                            text proj.name size 28 xanchor 0.5 xalign 0.5 style "textbutton_text_style" ypos -80
                            if mc.business.IT_partial_projects.has_key(proj.identifier):
                                bar:
                                    value mc.business.IT_partial_projects.get(proj.identifier, 0)
                                    range proj.project_cost
                                    xalign 0.5
                                    yalign 0.5
                                    ypos -70
                                    xysize (200, 10)
                            python:
                                supplemental_text = ""
                                if mc.business.IT_project_in_progress != None:
                                    if proj == mc.business.IT_project_in_progress[0]:
                                        supplemental_text = "In Progress"
                                if proj not in mc.business.IT_projects and proj.requirement() != True and proj.requirement():
                                    supplemental_text = "{color=#ff0000}" + proj.requirement() + "{/color}"
                                elif proj not in mc.business.IT_projects and not  proj.requirement():
                                    supplemental_text = "{color=#ff0000} Unknown Req {/color}"

                            text supplemental_text  style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        text "Breeder Bots" style "menu_text_title_style" size 32 xalign 0.5
                        hbox:
                            xalign 0.5
                            textbutton "Button 1":
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()
                        hbox:
                            xalign 0.5
                            textbutton "Button 2":
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        text "Anal Bots" style "menu_text_title_style" size 32 xalign 0.5
                        hbox:
                            xalign 0.5
                            textbutton "Button 1":
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()
                        hbox:
                            xalign 0.5
                            textbutton "Button 2":
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        text "Cum Bots" style "menu_text_title_style" size 32 xalign 0.5
                        hbox:
                            xalign 0.5
                            textbutton "Button 1":
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()
                        hbox:
                            xalign 0.5
                            textbutton "Button 2":
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        text "Exhbitionism Bots" style "menu_text_title_style" size 32 xalign 0.5
                        hbox:
                            xalign 0.5
                            textbutton "Button 1":
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()
                        hbox:
                            xalign 0.5
                            textbutton "Button 2":
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()

    screen business_project_screen():
        add "IT_Background.png"
        modal True
        zorder 100
        use screen_IT_active_project()
        use screen_IT_return_button()
        vbox:

            xcenter 960
            yalign 0.1
            # background "#1a45a1aa"
            text "Select a New Business IT Project" style "menu_text_title_style" size 48 xanchor 0.5 xalign 0.5
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

                        xsize 300

                        text "HR" style "menu_text_title_style" size 32 xalign 0.5
                        for proj in IT_get_HR_projects():
                            hbox:
                                xalign 0.5
                                if proj not in mc.business.IT_projects:
                                    if proj.requirement() == True:
                                        imagebutton:
                                            insensitive it_imagebutton_inactive
                                            idle it_imagebutton_idle
                                            hover it_imagebutton_hover
                                            selected_idle it_imagebutton_active
                                            selected_hover it_imagebutton_hover
                                            action Function (set_active_IT_project, proj)
                                            sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                            if mc.business.IT_project_in_progress != None:
                                                selected proj == mc.business.IT_project_in_progress[0]
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    elif proj.requirement():
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    else:
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]

                                if proj in mc.business.IT_projects:
                                    imagebutton:
                                        insensitive it_imagebutton_inactive
                                        idle it_imagebutton_inactive
                                        hover it_imagebutton_hover
                                        selected proj in mc.business.active_IT_projects
                                        selected_idle it_imagebutton_active
                                        selected_hover it_imagebutton_hover
                                        action Function (IT_toggle_project, proj)
                                        sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                        hovered [
                                            Show("IT_tooltip",None,proj)
                                            ]

                            text proj.name size 28 xanchor 0.5 xalign 0.5 style "textbutton_text_style" ypos -80
                            if mc.business.IT_partial_projects.has_key(proj.identifier):
                                bar:
                                    value mc.business.IT_partial_projects.get(proj.identifier, 0)
                                    range proj.project_cost
                                    xalign 0.5
                                    yalign 0.5
                                    ypos -70
                                    xysize (200, 10)
                            python:
                                supplemental_text = ""
                                if mc.business.IT_project_in_progress != None:
                                    if proj == mc.business.IT_project_in_progress[0]:
                                        supplemental_text = "In Progress"
                                if proj not in mc.business.IT_projects and proj.requirement() != True and proj.requirement():
                                    supplemental_text = "{color=#ff0000}" + proj.requirement() + "{/color}"
                                elif proj not in mc.business.IT_projects and not  proj.requirement():
                                    supplemental_text = "{color=#ff0000} Unknown Req {/color}"

                            text supplemental_text  style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75
                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        text "Supply" style "menu_text_title_style" size 32 xalign 0.5
                        for proj in IT_get_supply_projects():
                            hbox:
                                xalign 0.5
                                if proj not in mc.business.IT_projects:
                                    if proj.requirement() == True:
                                        imagebutton:
                                            insensitive it_imagebutton_inactive
                                            idle it_imagebutton_idle
                                            hover it_imagebutton_hover
                                            selected_idle it_imagebutton_active
                                            selected_hover it_imagebutton_hover
                                            action Function (set_active_IT_project, proj)
                                            sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                            if mc.business.IT_project_in_progress != None:
                                                selected proj == mc.business.IT_project_in_progress[0]
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    elif proj.requirement():
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    else:
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]

                                if proj in mc.business.IT_projects:
                                    imagebutton:
                                        insensitive it_imagebutton_inactive
                                        idle it_imagebutton_inactive
                                        hover it_imagebutton_hover
                                        selected proj in mc.business.active_IT_projects
                                        selected_idle it_imagebutton_active
                                        selected_hover it_imagebutton_hover
                                        action Function (IT_toggle_project, proj)
                                        sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                        hovered [
                                            Show("IT_tooltip",None,proj)
                                            ]

                            text proj.name size 28 xanchor 0.5 xalign 0.5 style "textbutton_text_style" ypos -80
                            if mc.business.IT_partial_projects.has_key(proj.identifier):
                                bar:
                                    value mc.business.IT_partial_projects.get(proj.identifier, 0)
                                    range proj.project_cost
                                    xalign 0.5
                                    yalign 0.5
                                    ypos -70
                                    xysize (200, 10)
                            python:
                                supplemental_text = ""
                                if mc.business.IT_project_in_progress != None:
                                    if proj == mc.business.IT_project_in_progress[0]:
                                        supplemental_text = "In Progress"
                                if proj not in mc.business.IT_projects and proj.requirement() != True and proj.requirement():
                                    supplemental_text = "{color=#ff0000}" + proj.requirement() + "{/color}"
                                elif proj not in mc.business.IT_projects and not proj.requirement():
                                    supplemental_text = "{color=#ff0000} Unknown Req {/color}"

                            text supplemental_text  style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        text "Marketing" style "menu_text_title_style" size 32 xalign 0.5
                        for proj in IT_get_market_projects():
                            hbox:
                                xalign 0.5
                                if proj not in mc.business.IT_projects:
                                    if proj.requirement() == True:
                                        imagebutton:
                                            insensitive it_imagebutton_inactive
                                            idle it_imagebutton_idle
                                            hover it_imagebutton_hover
                                            selected_idle it_imagebutton_active
                                            selected_hover it_imagebutton_hover
                                            action Function (set_active_IT_project, proj)
                                            sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                            if mc.business.IT_project_in_progress != None:
                                                selected proj == mc.business.IT_project_in_progress[0]
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    elif proj.requirement():
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    else:
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]

                                if proj in mc.business.IT_projects:
                                    imagebutton:
                                        insensitive it_imagebutton_inactive
                                        idle it_imagebutton_inactive
                                        hover it_imagebutton_hover
                                        selected proj in mc.business.active_IT_projects
                                        selected_idle it_imagebutton_active
                                        selected_hover it_imagebutton_hover
                                        action Function (IT_toggle_project, proj)
                                        sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                        hovered [
                                            Show("IT_tooltip",None,proj)
                                            ]

                            text proj.name size 28 xanchor 0.5 xalign 0.5 style "textbutton_text_style" ypos -80
                            if mc.business.IT_partial_projects.has_key(proj.identifier):
                                bar:
                                    value mc.business.IT_partial_projects.get(proj.identifier, 0)
                                    range proj.project_cost
                                    xalign 0.5
                                    yalign 0.5
                                    ypos -70
                                    xysize (200, 10)
                            python:
                                supplemental_text = ""
                                if mc.business.IT_project_in_progress != None:
                                    if proj == mc.business.IT_project_in_progress[0]:
                                        supplemental_text = "In Progress"
                                if proj not in mc.business.IT_projects and proj.requirement() != True and proj.requirement():
                                    supplemental_text = "{color=#ff0000}" + proj.requirement() + "{/color}"
                                elif proj not in mc.business.IT_projects and not proj.requirement():
                                    supplemental_text = "{color=#ff0000} Unknown Req {/color}"

                            text supplemental_text  style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        text "Research" style "menu_text_title_style" size 32 xalign 0.5
                        for proj in IT_get_research_projects():
                            hbox:
                                xalign 0.5
                                if proj not in mc.business.IT_projects:
                                    if proj.requirement() == True:
                                        imagebutton:
                                            insensitive it_imagebutton_inactive
                                            idle it_imagebutton_idle
                                            hover it_imagebutton_hover
                                            selected_idle it_imagebutton_active
                                            selected_hover it_imagebutton_hover
                                            action Function (set_active_IT_project, proj)
                                            sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                            if mc.business.IT_project_in_progress != None:
                                                selected proj == mc.business.IT_project_in_progress[0]
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    elif proj.requirement():
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    else:
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]

                                if proj in mc.business.IT_projects:
                                    imagebutton:
                                        insensitive it_imagebutton_inactive
                                        idle it_imagebutton_inactive
                                        hover it_imagebutton_hover
                                        selected proj in mc.business.active_IT_projects
                                        selected_idle it_imagebutton_active
                                        selected_hover it_imagebutton_hover
                                        action Function (IT_toggle_project, proj)
                                        sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                        hovered [
                                            Show("IT_tooltip",None,proj)
                                            ]

                            text proj.name size 28 xanchor 0.5 xalign 0.5 style "textbutton_text_style" ypos -80
                            if mc.business.IT_partial_projects.has_key(proj.identifier):
                                bar:
                                    value mc.business.IT_partial_projects.get(proj.identifier, 0)
                                    range proj.project_cost
                                    xalign 0.5
                                    yalign 0.5
                                    ypos -70
                                    xysize (200, 10)
                            python:
                                supplemental_text = ""
                                if mc.business.IT_project_in_progress != None:
                                    if proj == mc.business.IT_project_in_progress[0]:
                                        supplemental_text = "In Progress"
                                if proj not in mc.business.IT_projects and proj.requirement() != True and proj.requirement():
                                    supplemental_text = "{color=#ff0000}" + proj.requirement() + "{/color}"
                                elif proj not in mc.business.IT_projects and not proj.requirement():
                                    supplemental_text = "{color=#ff0000} Unknown Req {/color}"

                            text supplemental_text  style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        text "Production" style "menu_text_title_style" size 32 xalign 0.5
                        for proj in IT_get_production_projects():
                            hbox:
                                xalign 0.5
                                if proj not in mc.business.IT_projects:
                                    if proj.requirement() == True:
                                        imagebutton:
                                            insensitive it_imagebutton_inactive
                                            idle it_imagebutton_idle
                                            hover it_imagebutton_hover
                                            selected_idle it_imagebutton_active
                                            selected_hover it_imagebutton_hover
                                            action Function (set_active_IT_project, proj)
                                            sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                            if mc.business.IT_project_in_progress != None:
                                                selected proj == mc.business.IT_project_in_progress[0]
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    elif proj.requirement():
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]
                                    else:
                                        imagebutton:
                                            idle it_imagebutton_locked
                                            hover it_imagebutton_locked
                                            hovered [
                                                Show("IT_tooltip",None,proj)
                                                ]

                                if proj in mc.business.IT_projects:
                                    imagebutton:
                                        insensitive it_imagebutton_inactive
                                        idle it_imagebutton_inactive
                                        hover it_imagebutton_hover
                                        selected proj in mc.business.active_IT_projects
                                        selected_idle it_imagebutton_active
                                        selected_hover it_imagebutton_hover
                                        action Function (IT_toggle_project, proj)
                                        sensitive True # (proj.identifier == mc.business.IT_project_in_progress[0])
                                        hovered [
                                            Show("IT_tooltip",None,proj)
                                            ]

                            text proj.name size 28 xanchor 0.5 xalign 0.5 style "textbutton_text_style" ypos -80
                            if mc.business.IT_partial_projects.has_key(proj.identifier):
                                bar:
                                    value mc.business.IT_partial_projects.get(proj.identifier, 0)
                                    range proj.project_cost
                                    xalign 0.5
                                    yalign 0.5
                                    ypos -70
                                    xysize (200, 10)
                            python:
                                supplemental_text = ""
                                if mc.business.IT_project_in_progress != None:
                                    if proj == mc.business.IT_project_in_progress[0]:
                                        supplemental_text = "In Progress"
                                if proj not in mc.business.IT_projects and proj.requirement() != True and proj.requirement():
                                    supplemental_text = "{color=#ff0000}" + proj.requirement() + "{/color}"
                                elif proj not in mc.business.IT_projects and not proj.requirement():
                                    supplemental_text = "{color=#ff0000} Unknown Requirement {/color}"

                            text supplemental_text  style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75
                            # if mc.business.IT_project_in_progress != None:
                            #     if proj == mc.business.IT_project_in_progress[0]:
                            #         text "In Progress" style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75
                            #     else:
                            #         text "" style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75
                            # if proj not in mc.business.IT_projects and proj.requirement() != True and proj.requirement():
                            #     text proj.requirement() style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5 ypos -75 color "#DD0000"

screen IT_tooltip(the_project):
    $ hint_height = 150
    $ window_height = hint_height
    $ proj_desc = the_project.desc
    $ proj_name = the_project.name

    zorder 100
    frame:
        background "#1a45a1aa"
        xcenter 440
        #xalign 0.1
        ycenter 900
        xsize 760
        ysize window_height

        vbox:
            spacing 5
            frame:
                background Frame(proj_desc_back, 5,5)
                xsize 750
                ysize hint_height - 10
                ypadding 15
                xpadding 30
                vbox:
                    spacing 0
                    text "{size=24}[proj_name]{/size}" style "menu_text_title_style" xalign 0 text_align 0 xpos 2
                    text "{size=18}[proj_desc]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2

screen screen_IT_active_project():
    $ hint_height = 150
    $ window_height = hint_height
    if mc.business.IT_project_in_progress:
        $ proj_desc = mc.business.IT_project_in_progress[0].name
    else:
        $ proj_desc = "Unassigned!"
    zorder 100
    frame:
        background "#1a45a1aa"
        xcenter 1160
        #xalign 0.1
        ycenter 900
        xsize 360
        ysize window_height

        vbox:
            spacing 5
            frame:
                background Frame(proj_desc_back, 5,5)
                xsize 350
                ysize hint_height - 10
                ypadding 15
                xpadding 30
                vbox:
                    spacing 0
                    text "{size=24}Current Project:{/size}" style "menu_text_title_style" xalign 0 text_align 0 xpos 2
                    text "{size=18}[proj_desc]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
                    if proj_desc != "Unassigned!":
                        bar:
                            value mc.business.IT_project_in_progress[1]
                            range mc.business.IT_project_in_progress[0].project_cost
                            xalign 0.5
                            yalign 0.5
                            left_bar prog_bar_left
                            right_bar prog_bar_right
                            xysize (200, 20)

screen screen_IT_return_button():
    frame:
        background None
        anchor [0.5,0.5]
        align [0.88,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [Return(), Hide("it_project_screen"),
                     Hide("IT_tooltip"),
                     Hide("nanobot_project_screen"),
                     Hide("business_project_screen"),
                     Hide("screen_IT_active_project")]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"

screen in_progress_text_box(x,y):
    text "In Progress" style "menu_text_title_style" size 18 xalign x ypos y
