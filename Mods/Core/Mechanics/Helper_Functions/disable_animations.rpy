
init 20 python: 
    add_label_hijack("normal_start", "disable_animations_advisory")

label disable_animations_advisory(stack):
    if persistent.vren_animation:
        "You currently have the game animations enabled, this code is currently unstable and causes issues. The MOD builders recommend that you disable them, if you change your mind, you can change this setting in the game preferences."

        menu:
            "Disable animations (Recommended)":
                $ persistent.vren_animation = False
                $ renpy.save_persistent()
            "Leave animations enabled":
                pass

    $ execute_hijack_call(stack)
    return
