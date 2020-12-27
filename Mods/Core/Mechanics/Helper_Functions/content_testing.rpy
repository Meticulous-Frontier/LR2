#This file is designed to make it possible to wall off pieces of content based on the current status of the player, being either Alpha, Beta, or full content only.
init 5 python:
    def mod_alpha_content_warning(feature = True):
        if not feature:
            renpy.say("","Warning: This content is considered WIP. It may contain game breaking bugs or be incomplete. Please report issues and suggestions on discord, f95zone.to, or on gitgud.io")
        return

    def show_wip_screen(feature = True):  #TODO if a label crashes or exits before this gets called, screen will show up indefinitely?
        if not feature:
            renpy.show_screen("under_construction_ui")
        return

    def hide_wip_screen():
        renpy.hide_screen("under_construction_ui")
        return

    ashley_sisterly_jealousy_feature = False     #   set to True if no longer WIP
    girlfriend_role_sleepover_feature = False    #   set to True if no longer WIP

    add_label_hijack("normal_start", "add_content_setting_option")
    add_label_hijack("after_load", "add_content_setting_option")

label add_content_setting_option(stack):
    python:
        # remove old alpha/beta selector
        bedroom.remove_action("set_mod_content_settings")
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
