init -1 python:
    color_replacement_list = [
        ["#ff2c2c", "#ff6347"], # Red => Tomato Red
        ["#696eff", "#87cefa"], # Blue => Light Sky Blue
        ["#d62cff", "#dda0dd"]  # Purple => Plum
    ]

    readable_color_list.append("#fcf7de") # Corn Silk
    readable_color_list.append("#f0defd") # Lavender
    readable_color_list.append("#f2d7b4") # Wheat

    for replacement in color_replacement_list:
        if replacement[0] in readable_color_list:
            readable_color_list[readable_color_list.index(replacement[0])] = replacement[1]

    def updated_person_colors(person):
        if person.char.what_args["color"] in color_replacement_list[0]:
            idx = color_replacement_list[0].index(person.char.what_args["color"])
            #mc.log_event((person.title or person.name) + ": " + color_replacement_list[idx][0] + " => " + color_replacement_list[idx][1], "float_text_grey")
            if not person.title is None:
                person.title = person.title.replace(color_replacement_list[idx][0], color_replacement_list[idx][1])
            if not person.possessive_title is None:
                person.possessive_title = person.possessive_title.replace(color_replacement_list[idx][0], color_replacement_list[idx][1])
            person.char.what_args["color"] = color_replacement_list[idx][1]
            person.char.who_args["color"] = color_replacement_list[idx][1]
        return

    def color_indicator(variable, max_value = 100): # Gives color indication to a value range split into 5.
        if variable >= max_value / 1.25: # 80%
            return "{color=#24ed27}" + str(variable) +"{/color}"
        if variable >= max_value / 1.67: # 60%
            return "{color=#8edb21}" + str(variable) +"{/color}"
        if variable >= max_value / 2.5: # 40%
            return "{color=#ffec6e}" + str(variable) +"{/color}"
        if variable >= max_value / 5: # 20%
            return "{color=#ed9d4c}" + str(variable) +"{/color}"
        else: # less than 20%
            return "{color=#ff6347}" + str(variable) +"{/color}"

    def rgb_to_hsl(r, g, b):    # r/g/b values in decimal 0-1
        mx = max(r, g, b)
        mn = min(r, g, b)
        dx = mx - mn

        h = 0
        s = 0
        l = (mx + mn) / 2.0

        if dx != 0:
            if l < .5:
                s = dx / (mx + mn)
            else:
                s = dx / (2.0 - mx - mn)

            if r == mx:
                h = (g-b) / dx
            elif (g == mx):
                h = 2.0 + (b - r) / dx
            elif (b == mx):
                h = 4.0 + (r - g) / dx

        h *= 60
        if h < 0:
            h += 360

        return h, s * 100, l * 100

init 5 python:
    add_label_hijack("normal_start", "activate_color_blindness_fix")
    add_label_hijack("after_load", "update_color_blindness_fix")

    def color_blindness_fix_update_people():
        for person in all_people_in_the_game([mc]):
            updated_person_colors(person)
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
