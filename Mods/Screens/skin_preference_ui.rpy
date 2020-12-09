init 2 python:
    def change_skin_requirement():
        return True

    def get_random_skin():
        list_of_weighted_skins = []
        if persistent.white > 0:
            list_of_weighted_skins.append(["white", persistent.white])
        if persistent.black > 0:
            list_of_weighted_skins.append(["black", persistent.black])
        if persistent.tan > 0:
            list_of_weighted_skins.append(["tan", persistent.tan])

        if __builtin__.len(list_of_weighted_skins) == 0:
            list_of_weighted_skins.append(["white", 33])
            list_of_weighted_skins.append(["black", 33])
            list_of_weighted_skins.append(["tan", 33])

        return get_random_from_weighted_list(list_of_weighted_skins)

    change_skin_action = Action("Change Skin Preference", change_skin_requirement, "show_skin_preference_ui", menu_tooltip = "Change the chance a certain skin will be generated for a random person.")

init 5 python:
    add_label_hijack("normal_start", "activate_skin_preference")
    add_label_hijack("after_load", "update_skin_preference")

    def set_persistent_skin_preferences():
        if not (persistent.white or isinstance(persistent.white, int)):
            persistent.white = 33
        if not (persistent.black or isinstance(persistent.black, int)):
            persistent.black = 33
        if not (persistent.tan or isinstance(persistent.tan, int)):
            persistent.tan = 33
        return

label activate_skin_preference(stack):
    python:
        bedroom.add_action(change_skin_action)
        set_persistent_skin_preferences()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_skin_preference(stack):
    python:
        bedroom.add_action(change_skin_action)
        set_persistent_skin_preferences()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_skin_preference_ui():
    $ renpy.call_screen("skin_preference_ui")
    return

screen skin_preference_ui():
    modal True
    zorder 49

    default current_white = persistent.white
    default current_black = persistent.black
    default current_tan = persistent.tan

    frame: # top frame
        background "#aaaaaa"
        xsize 900
        ysize 500
        yalign 0.4
        xalign 0.5

        vbox:
            yalign 0
            xalign .5
            text "Skin Preference" style "textbutton_text_style"

        vbox:
            yalign 0.1
            xalign 0.5
            text "White" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_white", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_white) + "%" style "menu_text_style"

        vbox:
            yalign 0.5
            xalign 0.5
            text "Tan" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_tan", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_tan) + "%" style "menu_text_style"

        vbox:
            yalign 0.3
            xalign 0.5
            text "Dark" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_black", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_black) + "%" style "menu_text_style"

        hbox:
            yalign 0.7
            xalign 0.5
            xsize 800
            text "{size=16}Warning: setting all values to the same value will result in even chance, for correct percentage make sure they sum close to 100. If you want all random characters to adhere to these value, start a new game after you changed these values." style "warning_text"

        hbox:
            yalign 1.0
            xalign 0.5
            xanchor 0.5
            spacing 50
            textbutton "Cancel" action [Return] style "textbutton_style" text_style "textbutton_text_style" tooltip "" text_text_align 0.5 text_xalign 0.5 xysize (155,60)
            textbutton "Save":
                style "textbutton_style"
                text_style "textbutton_text_style"
                tooltip ""
                text_text_align 0.5
                text_xalign 0.5
                xysize (155,60)
                action [
                    SetVariable("persistent.white", __builtin__.int(current_white)),
                    SetVariable("persistent.black", __builtin__.int(current_black)),
                    SetVariable("persistent.tan", __builtin__.int(current_tan)),
                    Return
                ]

style warning_text:
    color "B22222"
    size 16
    xalign 0.5