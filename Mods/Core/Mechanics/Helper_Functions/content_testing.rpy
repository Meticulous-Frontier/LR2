#This file is designed to make it possible to wall off pieces of content based on the current status of the player, being either Alpha, Beta, or full content only.
init 5 python:
    def mod_alpha_content_warning():
        renpy.say("","Warning: This content is in alpha and is considered WIP. It may contain game breaking bugs or be incomplete. Please report issues and suggestions on discord, f95zone.to, or on gitgud.io")
        return

    def mod_beta_content_warning(version = -1): #Version is broke. It needs some kind of string dissection to work
        renpy.say("","Warning: This content is in beta. Please report issues and suggestions on discord, f95zone.to, or on gitgud.io")
        return

    def wip_screen_show(version = -1):  #TODO if a label crashes or exits before this gets called, screen will show up indefinitely?
        if "game_version" in globals():
            if version > 0 and version + 1 > game_version and not renpy.get_screen("under_construction_ui"):
                renpy.show_screen(under_construction_ui)
        return

    def wip_screen_clear():
        if renpy.get_screen("under_construction_ui"):
            renpy.hide_screen(under_construction_ui)
        return

    # remove in future versions
    def change_content_setting_requirement():
        return True

    add_label_hijack("normal_start", "add_content_setting_option")
    add_label_hijack("after_load", "add_content_setting_option")

label add_content_setting_option(stack):
    python:
        # remove old alpha/beta selector
        bedroom.remove_action("set_mod_content_settings")
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
