init 2 python:
    def change_cup_requirement():
        return True

    def get_random_tit():
        list_of_weighted_cups = []
        if persistent.AA > 0:
            list_of_weighted_cups.append(["AA", persistent.AA])
        if persistent.A > 0:
            list_of_weighted_cups.append(["A", persistent.A])
        if persistent.B > 0:
            list_of_weighted_cups.append(["B", persistent.B])
        if persistent.C > 0:
            list_of_weighted_cups.append(["C", persistent.C])
        if persistent.D > 0:
            list_of_weighted_cups.append(["D", persistent.D])
        if persistent.DD > 0:
            list_of_weighted_cups.append(["DD", persistent.DD])
        if persistent.DDD > 0:
            list_of_weighted_cups.append(["DDD", persistent.DDD])
        if persistent.E > 0:
            list_of_weighted_cups.append(["E", persistent.E])
        if persistent.F > 0:
            list_of_weighted_cups.append(["F", persistent.F])
        if persistent.FF > 0:
            list_of_weighted_cups.append(["FF", persistent.FF])

        if __builtin__.len(list_of_weighted_cups) == 0:
            list_of_weighted_cups.append(["AA", 4])
            list_of_weighted_cups.append(["A", 8])
            list_of_weighted_cups.append(["B", 15])
            list_of_weighted_cups.append(["C", 20])
            list_of_weighted_cups.append(["D", 20])
            list_of_weighted_cups.append(["DD", 15])
            list_of_weighted_cups.append(["DDD", 10])
            list_of_weighted_cups.append(["E", 5])
            list_of_weighted_cups.append(["F", 2])
            list_of_weighted_cups.append(["FF", 1])

        return get_random_from_weighted_list(list_of_weighted_cups)

    change_cup_action = Action("Change Cup Size Preference", change_cup_requirement, "show_cup_preference_ui", menu_tooltip = "Change the chance a certain tit size will be generated for a random person.")

init 5 python:
    add_label_hijack("normal_start", "activate_cup_preference")
    add_label_hijack("after_load", "update_cup_preference")

    def set_persistent_cup_preferences():
        if not (persistent.AA or isinstance(persistent.AA, int)):
            persistent.AA = 4
        if not (persistent.A or isinstance(persistent.A, int)):
            persistent.A = 8
        if not (persistent.B or isinstance(persistent.B, int)):
            persistent.B = 15
        if not (persistent.C or isinstance(persistent.C, int)):
            persistent.C = 20
        if not (persistent.D or isinstance(persistent.D, int)):
            persistent.D = 20
        if not (persistent.DD or isinstance(persistent.DD, int)):
            persistent.DD = 15
        if not (persistent.DDD or isinstance(persistent.DDD, int)):
            persistent.DDD = 10
        if not (persistent.E or isinstance(persistent.E, int)):
            persistent.E = 5
        if not (persistent.F or isinstance(persistent.F, int)):
            persistent.F = 2
        if not (persistent.FF or isinstance(persistent.FF, int)):
            persistent.FF = 1
        return

label activate_cup_preference(stack):
    python:
        bedroom.add_action(change_cup_action)
        set_persistent_cup_preferences()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_cup_preference(stack):
    python:
        bedroom.add_action(change_cup_action)
        set_persistent_cup_preferences()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_cup_preference_ui():
    $ renpy.call_screen("cup_preference_ui")
    return

screen cup_preference_ui():
    modal True
    zorder 49

    default current_AA = persistent.AA
    default current_A = persistent.A
    default current_B = persistent.B
    default current_C = persistent.C
    default current_D = persistent.D
    default current_DD = persistent.DD
    default current_DDD = persistent.DDD
    default current_E = persistent.E
    default current_F = persistent.F
    default current_FF = persistent.FF

    frame: # top frame
        background "#aaaaaa"
        xsize 900
        ysize 900
        yalign 0.6
        xalign 0.5

        vbox:
            yalign 0
            xalign .5
            text "Cup Size Preferences" style "textbutton_text_style"

        vbox:
            yalign 0.015
            xalign 0.5
            text "AA Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_AA", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_AA) + "%" style "menu_text_style"


        vbox:
            yalign 0.115
            xalign 0.5
            text "A Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_A", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_A) + "%" style "menu_text_style"

        vbox:
            yalign 0.215
            xalign 0.5
            text "B Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_B", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_B) + "%" style "menu_text_style"
        vbox:
            yalign 0.315
            xalign 0.5
            text "C Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_C", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_C) + "%" style "menu_text_style"
        vbox:
            yalign 0.415
            xalign 0.5
            text "D Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_D", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_D) + "%" style "menu_text_style"
        vbox:
            yalign 0.515
            xalign 0.5
            text "DD Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_DD", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_DD) + "%" style "menu_text_style"
        vbox:
            yalign 0.615
            xalign 0.5
            text "DDD Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_DDD", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_DDD) + "%" style "menu_text_style"
        vbox:
            yalign 0.715
            xalign 0.5
            text "E Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_E", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_E) + "%" style "menu_text_style"
        vbox:
            yalign 0.715
            xalign 0.5
            text "F Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_F", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_F) + "%" style "menu_text_style"
        vbox:
            yalign 0.815
            xalign 0.5
            text "FF Cup" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_FF", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_FF) + "%" style "menu_text_style"

        hbox:
            yalign 0.95
            xalign 0.5
            xsize 800
            text "{size=16}Warning: setting all values to the same value will result in even chance, for correct percentage make sure they sum to 100. If you want all random characters to adhere to these value, start a new game after you changed these values." style "warning_text"

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
                    SetVariable("persistent.AA", __builtin__.int(current_AA)),
                    SetVariable("persistent.A", __builtin__.int(current_A)),
                    SetVariable("persistent.B", __builtin__.int(current_B)),
                    SetVariable("persistent.C", __builtin__.int(current_C)),
                    SetVariable("persistent.D", __builtin__.int(current_D)),
                    SetVariable("persistent.DD", __builtin__.int(current_DD)),
                    SetVariable("persistent.DDD", __builtin__.int(current_DDD)),
                    SetVariable("persistent.E", __builtin__.int(current_E)),
                    SetVariable("persistent.F", __builtin__.int(current_F)),
                    SetVariable("persistent.FF", __builtin__.int(current_FF)),
                    Return
                ]

style warning_text:
    color "B22222"
    size 16
    xalign 0.5