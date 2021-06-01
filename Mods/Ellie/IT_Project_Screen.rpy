init 5 python:
    business_proj_back = Image(get_file_handle("frame.png"))
    nanobot_proj_back = Image(get_file_handle("frame.png"))
    proj_desc_back = Image(get_file_handle("frame.png"))

init 5:
    screen it_project_screen():
        add "IT_Background.png"
        modal True
        zorder 100
        vbox:
            #xanchor 0.5
            #xalign 0.5
            xcenter 960
            yalign 0.2
            # background "#1a45a1aa"
            text "Select a new IT Project" style "menu_text_title_style" size 48 xanchor 0.5 xalign 0.5
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
                        hbox:
                            xalign 0.5
                            textbutton "Routine Maintenence":
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
                                textbutton proj.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action NullAction()
                                    hovered [
                                    Show("IT_tooltip",None,proj)
                                    ]

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
                                textbutton proj.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action NullAction()
                                    hovered [
                                    Show("IT_tooltip",None,proj)
                                    ]

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
                                textbutton proj.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action NullAction()
                                    hovered [
                                    Show("IT_tooltip",None,proj)
                                    ]

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
                                textbutton proj.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action NullAction()
                                    hovered [
                                    Show("IT_tooltip",None,proj)
                                    ]

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
                                textbutton proj.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action NullAction()
                                    hovered [
                                    Show("IT_tooltip",None,proj)
                                    ]

screen IT_tooltip(the_project):
    $ hint_height = 150
    $ window_height = hint_height
    $ proj_desc = the_project.desc
    $ proj_name = the_project.name

    zorder 100
    frame:
        background "#1a45a1aa"
        xcenter 400
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
