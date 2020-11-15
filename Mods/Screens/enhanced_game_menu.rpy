init 1 python:
    mod_image = Image(get_file_handle("LR2Mod_idle.png"))
    mod_hover_image = Image(get_file_handle("LR2Mod_hover.png"))

init 2:
    style game_menu_content_frame:
        left_margin 60
        right_margin 30
        top_margin 60

    style navigation_button:
        background None

    screen main_menu():

        # This ensures that any other menu screen is replaced.
        tag menu

        style_prefix "main_menu"

        add gui.main_menu_background

        ## The use statement includes another screen inside this one. The actual
        ## contents of the main menu are in the navigation screen.
        use navigation

        if gui.show_name:

            vbox:
                text "[config.name!t]":
                    style "main_menu_title"

                text "[config.version]":
                    style "main_menu_version"

        imagebutton idle mod_image hover mod_hover_image action OpenURL("https://f95zone.to/threads/lab-rats-2-mods.32881/#post-2102913") xpos 20 ypos 980


    screen game_menu(title, scroll=None):
        # Add the backgrounds.
        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        style_prefix "game_menu"

        frame:
            background None
            style "game_menu_outer_frame"

            hbox:

                # Reserve space for the navigation section.
                frame:
                    style "game_menu_navigation_frame"

                frame:
                    style "game_menu_content_frame"

                    if scroll == "viewport":

                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            side_yfill True

                            vbox:
                                transclude

                    elif scroll == "vpgrid":

                        vpgrid:
                            cols 1
                            yinitial 1.0

                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            side_yfill True

                            transclude

                    else:

                        transclude

        use navigation

        if "stephanie" in globals():
            textbutton _("Back To Game") ypos 990:
                style "return_button"

                action Return()


        label title

        imagebutton idle mod_image hover mod_hover_image action OpenURL("https://f95zone.to/threads/lab-rats-2-mods.32881/#post-2102913") xpos 20 ypos 980

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")
