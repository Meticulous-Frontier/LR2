init -1 python:
    color_replacement_list = [
        ["#cf3232", "#cf6347"], # Red => Tomato Red
        ["#d62cff", "#dda0dd"]  # Purple => Plum
    ]

    for x in color_replacement_list:
        if x[0] in readable_color_list:
            idx = readable_color_list.index(x[0])
            readable_color_list[idx] = x[1]

    readable_color_list.append("#fcf7de") # Corn Silk
    readable_color_list.append("#f0defd") # Lavender
    readable_color_list.append("#f2d7b4") # Wheat
    readable_color_list.append("#DAA520") # Golden Rod
    readable_color_list.append("#FFA07A") # Light Salmon
    readable_color_list.append("#FFA500") # Orange
    readable_color_list.append("#D2691E") # Chocolate
    readable_color_list.append("#20B2AA") # Light Sea Green
    readable_color_list.append("#C0C0C0") # Silver

    for replacement in color_replacement_list:
        if replacement[0] in readable_color_list:
            readable_color_list[readable_color_list.index(replacement[0])] = replacement[1]

    def change_person_font_colors(person):
        if not isinstance(person, Person):
            return
        if not (hasattr(person, "char") or hasattr(person.char, "what_args")):
            return

        if person.char.what_args["color"] in [x[0] for x in color_replacement_list]:
            idx = [x[0] for x in color_replacement_list].index(person.char.what_args["color"])
            cheat_person_font_color(person, color_replacement_list[idx][1])
        return

init 5 python:
    add_label_hijack("normal_start", "activate_color_blindness_fix")
    add_label_hijack("after_load", "update_color_blindness_fix")

    def color_blindness_fix_update_people():
        for person in [p for p in  all_people_in_the_game() if p.char.what_args["color"] in [x[0] for x in color_replacement_list]]:
            change_person_font_colors(person)
        return

label activate_color_blindness_fix(stack):
    python:
        color_blindness_fix_update_people()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_color_blindness_fix(stack):
    python:
        color_blindness_fix_update_people()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
