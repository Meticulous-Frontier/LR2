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
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("Cheat") action ToggleScreen("cheat_menu")
            textbutton _("Opinions") action ToggleScreen("opinion_edit_menu")

    screen quick_menu():
        variant "touch"

        zorder 100

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Menu") action ShowMenu()
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Cheat") action ToggleScreen("cheat_menu")
            textbutton _("Opinions") action ToggleScreen("opinion_edit_menu")
