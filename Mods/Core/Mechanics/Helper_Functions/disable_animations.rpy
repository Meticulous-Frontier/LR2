
init 20 python:
    add_label_hijack("normal_start", "disable_animations_advisory")

label disable_animations_advisory(stack):
    # disable animations, the MOD doesn't support it, it is buggy and slows down the game / causes crashes.
    python:
        persistent.vren_animation = False
        renpy.save_persistent()
        execute_hijack_call(stack)
    return
