init 2 python:
    def change_body_type_requirement():
        return True

    def get_random_body_type():
        list_of_weighted_body_types = []
        if persistent.thin_body > 0:
            list_of_weighted_body_types.append(["thin_body", persistent.thin_body])
        if persistent.normal_body > 0:
            list_of_weighted_body_types.append(["standard_body", persistent.normal_body])
        if persistent.curvy_body > 0:
            list_of_weighted_body_types.append(["curvy_body", persistent.curvy_body])

        if len(list_of_weighted_body_types) == 0:
            list_of_weighted_body_types.append(["thin_body", 1])
            list_of_weighted_body_types.append(["standard_body", 1])
            list_of_weighted_body_types.append(["curvy_body", 1])

        renpy.notify("Random Body Type: " + str(len(list_of_weighted_body_types)))
        return get_random_from_weighted_list(list_of_weighted_body_types)

    change_body_type_action = Action("Change Body Type Preference", change_body_type_requirement, "show_body_type_preference_ui", menu_tooltip = "Change the chance a certain body type will be generated for a random person.")

init 5 python:
    add_label_hijack("normal_start", "activate_body_type_preference")  
    add_label_hijack("after_load", "update_body_type_preference")

    def set_persistent_body_type_preferences():
        if not (persistent.thin_body or isinstance(persistent.thin_body, int)):
            persistent.thin_body = 75
        if not (persistent.normal_body or isinstance(persistent.normal_body, int)):
            persistent.normal_body = 20
        if not (persistent.curvy_body or isinstance(persistent.curvy_body, int)):
            persistent.curvy_body = 5
        return

label activate_body_type_preference(stack):
    python:
        bedroom.actions.append(change_body_type_action)
        set_persistent_body_type_preferences()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_body_type_preference(stack):
    python:
        if not change_body_type_action in bedroom.actions:
            bedroom.actions.append(change_body_type_action)
        set_persistent_body_type_preferences()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_body_type_preference_ui():
    $ renpy.call_screen("body_type_preference_ui")
    return        

screen body_type_preference_ui():
    modal True
    zorder 49

    default current_thin_body = persistent.thin_body
    default current_normal_body = persistent.normal_body
    default current_curvy_body = persistent.curvy_body

    frame: # top frame
        background "#aaaaaa"
        xsize 900
        ysize 500
        yalign 0.4
        xalign 0.5

        vbox:
            yalign 0
            xalign .5
            text "Body Type Preference" style "textbutton_text_style"

        vbox:
            yalign 0.1
            xalign 0.5
            text "Thin Body" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_thin_body", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_thin_body) + "%" style "menu_text_style"


        vbox:
            yalign 0.3
            xalign 0.5
            text "Normal Body" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_normal_body", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_normal_body) + "%" style "menu_text_style"

        vbox:
            yalign 0.5
            xalign 0.5
            text "Curvy Body" style "textbutton_text_style"
            hbox:
                bar value ScreenVariableValue("current_curvy_body", 100, step = 1) range 100 xsize 800 ysize 45 style style.slider
                yalign 1.0
                text str(current_curvy_body) + "%" style "menu_text_style"

        hbox:
            yalign 0.7
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
                    SetVariable("persistent.thin_body", int(current_thin_body)),
                    SetVariable("persistent.normal_body",int(current_normal_body)), 
                    SetVariable("persistent.curvy_body",int(current_curvy_body)),
                    Return
                ] 

style warning_text:
    color "B22222"
    size 16
    xalign 0.5