style quick_transparent_style:
    background "#00000066"
    padding [40, 5]
    xalign 0.5

style quick_text_style:
    size 28
    outlines [(2,"#222222",0,0)]


init 5:
    ## Quick Menu screen ###########################################################
    ##
    ## The quick menu is displayed in-game to provide easy access to the out-of-game
    ## menus.

    screen quick_menu():

        # Ensure this appears on top of other screens.
        zorder 100

        # Add an in-game quick menu.
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            if okay_to_save:
                textbutton _("Save") action ShowMenu('save')
                if config.has_quicksave:
                    textbutton _("Q.Save") action QuickSave()
            if config.has_quicksave:
                textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("Cheat") action ToggleScreen("cheat_menu")
            textbutton _("Research") action ToggleScreen("serum_cheat_menu")
            textbutton _("Opinions") action ToggleScreen("opinion_edit_menu")

    screen quick_menu():
        variant "touch"

        zorder 100

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") style "quick_transparent_style" text_style "quick_text_style" action Rollback()
            textbutton _("Skip") style "quick_transparent_style" text_style "quick_text_style" action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Menu") style "quick_transparent_style" text_style "quick_text_style" action ShowMenu()
            textbutton _("Auto") style "quick_transparent_style" text_style "quick_text_style" action Preference("auto-forward", "toggle")
            textbutton _("Cheat") style "quick_transparent_style" text_style "quick_text_style" action ToggleScreen("cheat_menu")
            textbutton _("Opinions") style "quick_transparent_style" text_style "quick_text_style" action ToggleScreen("opinion_edit_menu")
