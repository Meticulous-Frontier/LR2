init 2 python:
    generic_preference = {}
    generic_preference["Body Type"] = {
        "Thin Body": ["thin_body", 33, 0],
        "Normal Body": ["standard_body", 33, 1],
        "Curvy Body": ["curvy_body", 33, 2]
    }
    generic_preference["Cup Size"] = {
        "AA": ["AA", 4, 0],
        "A": ["A", 8 , 1],
        "B": ["B", 15, 2],
        "C": ["C", 20, 3],
        "D": ["D", 20 , 4],
        "DD": ["DD", 15, 5],
        "DDD": ["DDD", 10, 6],
        "E": ["E", 5, 7],
        "F": ["F", 2, 8],
        "FF": ["FF", 1, 9]
    }
    generic_preference["Skin Color"] = {
        "White": ["white", 33, 0],
        "Tan": ["tan", 33, 1],
        "Dark": ["black", 33, 2]
    }

    # update defaults when not exist
    for pref in generic_preference:
        for x in generic_preference[pref]:
            if not (getattr(persistent, generic_preference[pref][x][0]) or isinstance(getattr(persistent, generic_preference[pref][x][0]), int)):
                setattr(persistent, generic_preference[pref][x][0], generic_preference[pref][x][1])


    def get_random_skin():
        return get_random_from_weighted_list(build_generic_weighted_list("Skin Color"))

    def get_random_body_type():
        return get_random_from_weighted_list(build_generic_weighted_list("Body Type"))

    def get_random_tit():
        return get_random_from_weighted_list(build_generic_weighted_list("Cup Size"))

    def build_generic_weighted_list(pref):
        weighted_list = []
        for x in generic_preference[pref]:
            if getattr(persistent, generic_preference[pref][x][0]) > 0:
                weighted_list.append([generic_preference[pref][x][0], getattr(persistent, generic_preference[pref][x][0])])
        return weighted_list

    def change_generic_preferences_requirement():
        return True

    # remove in future version
    def change_body_type_requirement():
        return True

    # remove in future version
    def change_cup_requirement():
        return True

    # remove in future version
    def change_skin_requirement():
        return True

    change_generic_preferences_action = Action("Change Preferences", change_generic_preferences_requirement, "show_generic_preference_ui", menu_tooltip = "Change the chance of a certain body type / cup size / skin tone will be generated for a random person.")

init 5 python:
    add_label_hijack("normal_start", "activate_generic_preference")
    add_label_hijack("after_load", "activate_generic_preference")

label activate_generic_preference(stack):
    python:
        bedroom.remove_action("show_body_type_preference_ui")
        bedroom.remove_action("show_cup_preference_ui")
        bedroom.remove_action("show_skin_preference_ui")
        bedroom.add_action(change_generic_preferences_action)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_generic_preference_ui():
    $ renpy.call_screen("generic_preference_ui")
    return

init 10 python:
    def switch_preference(pref):
        cs = renpy.current_screen()
        cs.scope["pref_selected"] = pref

screen generic_preference_ui():
    modal True
    zorder 49

    default pref_selected = "Body Type"

    frame: # top frame
        background "#888888"
        xsize 900
        yalign 0.4
        xalign 0.5
        xanchor 0.5

        vbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.3
            spacing 10

            hbox:
                for pref in sorted(generic_preference):
                    textbutton pref:
                        style "textbutton_style"
                        xsize 280
                        sensitive pref != pref_selected
                        action [
                            Function(switch_preference, pref) # If a clothing item is selected and currently being previewed then remove it from preview.
                        ]

            for pref in sorted(generic_preference):
                if pref == pref_selected:
                    vbox:
                        for x in [x[0] for x in sorted(generic_preference[pref].items(), key = lambda x: x[1][2])]:
                            hbox:
                                spacing 5
                                vbox:
                                    xsize 140
                                    ysize 50
                                    yoffset 5
                                    text x style "textbutton_text_style"
                                vbox:
                                    xsize 600
                                    ysize 50
                                    bar value FieldValue(persistent, generic_preference[pref][x][0], 100, step = 1, style = "slider") xsize 600 ysize 45
                                vbox:
                                    xsize 60
                                    ysize 50
                                    yoffset 5
                                    text (str(getattr(persistent, generic_preference[pref][x][0])) + "%" if getattr(persistent, generic_preference[pref][x][0]) > 0 else "None") style "menu_text_style" xsize 100

            hbox:
                xsize 800
                text "{size=16}Warning: setting all values to the same value will result in even chance, for correct percentage make sure they sum close to 100. If you want all random characters to adhere to these value, start a new game after you changed these values." style "warning_text"

            hbox:
                xalign 0.5
                textbutton "Close" action [Return] style "textbutton_style" text_style "textbutton_text_style" tooltip "" text_text_align 0.5 text_xalign 0.5 xysize (155,60)

style warning_text:
    color "B22222"
    size 16
    xalign 0.5