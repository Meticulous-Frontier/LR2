#This file is designed to make it possible to wall off pieces of content based on the current status of the player, being either Alpha, Beta, or full content only.
#Alpha content is designed as things go, and should only be run by active developers and people dedicated to testing and feedback. Alpha content may break existing or previous save games and contain large bugs
#Beta content should be basically finished but needs vet'd by the community. Beta testers should be looking for continuity, spelling, grammar errors, etc.
#Once content has been beta for atleast 1 development cycle, it should be available to the general mod downloaders.
init 5 python:
    add_label_hijack("normal_start", "activate_content_testing")
    add_label_hijack("after_load", "activate_content_testing")

label activate_content_testing(stack):
    if "enable_alpha_mod_content" not in globals():
        $ mod_content_init_settings()
    $ execute_hijack_call(stack)
    return


init -3 python:
    def mod_content_init_settings():
        global enable_alpha_mod_content
        global enable_beta_mod_content
        enable_alpha_mod_content = False
        enable_beta_mod_content = False
        return

    def mod_content_alpha():
        return enable_alpha_mod_content

    def enable_all_alpha_content():
        global enable_alpha_mod_content
        global enable_beta_mod_content
        enable_alpha_mod_content = True
        enable_beta_mod_content = True
        return

    def enable_all_beta_content():
        global enable_alpha_mod_content
        global enable_beta_mod_content
        enable_alpha_mod_content = False
        enable_beta_mod_content = True
        return

    def disable_beta_content():
        global enable_alpha_mod_content
        global enable_beta_mod_content
        enable_alpha_mod_content = False
        enable_beta_mod_content = False
        return

    def change_content_setting_requirement():
        return True

init 5 python:


    def mod_content_beta(version = -1):   #Use a current version number in the call to give the function approximately 1 month beta.
        if enable_beta_mod_content:
            return True
        elif "game_version" in globals():
            if version > 0 and version + 1 > game_version:             #TRIST can we get the mod version from somewhere?
                return True
        return False

    def mod_alpha_content_warning():
        renpy.say("","Warning: This content is in alpha. It may contain game breaking bugs or be incomplete. Please report issues and suggestions on discord, f95zone.to, or on gitgud.io")
        return

    def mod_beta_content_warning(version = -1):
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


    change_content_setting = Action("Enable / Disable Alpha and Beta Content",change_content_setting_requirement, "set_mod_content_settings", menu_tooltip = "Change setting if you are shown Alpha and/or Beta story content.")

    add_label_hijack("normal_start", "add_content_setting_option")
    add_label_hijack("after_load", "add_content_setting_option")

label add_content_setting_option(stack):
    python:
        bedroom.add_action(change_content_setting)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label set_mod_content_settings():
    "Please select if you would like to be shown Alpha and Beta content, just Beta content, or no in testing content."
    "Alpha content is considered work in progress. It may be incomplete, break save games, or crash the game. This is only suggested for mod developers and game testers."
    "Beta content is considered basically finished. Errors should be minimal, but may still exist."
    "If testing content is disabled, neither Alpha or Beta content will be shown. This should be the most stable possible game environment with modded content."
    menu:
        "Enable Alpha and Beta content":
            $ enable_all_alpha_content()
            "Thank you for helping test and develop the mod!"
        "Enable Beta content":
            $ enable_all_beta_content()
            "Thank you for helping test the mod!"
        "Disable content testing":
            $ disable_beta_content()
            "Enjoy the mod!"
    return
