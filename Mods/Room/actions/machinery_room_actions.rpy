init 2 python:

    overload_cost = 10000
    machinery_room_overload = 100

    def machinery_room_construct_production_line_requirement():
        production_lines_cost = mc.business.production_lines * 5000
        if time_of_day is 4:
            return "Too late..."
        if not production_line_addition_2_policy.is_owned():
            return "Requires: [production_line_addition_2_policy.name]"

        if mc.business.funds >= production_lines_cost:
            return True
        return "Requires: $" + str(production_lines_cost)

    machinery_room_construct_production_line_action = Action("Create Production Line {image=gui/heart/Time_Advance.png}", machinery_room_construct_production_line_requirement, "machinery_room_construct_production_line_label", menu_tooltip = "...")

    def machinery_room_overload_requirement():
        if time_of_day is 4:
            return "Too late..."

        #overload_cost = (machinery_room_overload % 100) * 1000

        if mc.business.funds >= overload_cost:
            return True
        return "Requires: $[overload_cost]"

    machinery_room_overload_action = Action("Overclock Production Lines {image=gui/heart/Time_Advance.png}", machinery_room_overload_requirement, "machinery_room_overload_label", menu_tooltip = "Increase the capacity of your production lines above the maximum required by safety standards")

label machinery_room_construct_production_line_label():
    python:
        production_line_cost = mc.business.production_lines * 5000

    "[mc.business.name] currently has [mc.business.production_lines] production lines. Expanding and creating a new line will cost [production_line_cost]"

    menu:
        "Purchase Production Line \nCosts: $[production_line_cost]":
            $ add_production_lines(1)
            $ mc.business.change_funds(- production_line_cost)

            "Production lines expanded"
            call advance_time from machinery_room_construct_production_line_label_1

        "Back":
            pass
    return

label machinery_room_overload_label():

    python:

        overload_cost = (machinery_room_overload % 100) * 1000 # First overload will be free, but afterwards scales. Since the room itself costs $20000 that's fine.

    "With the splendor of technical accessibility provided by this facility you can spend both time and funds to increase the productivity of your business."
    "Do you wish to spend $[overload_cost] to increase the maximum capacity by 10%%?"

    menu:
        "Yes \nCosts: $[overload_cost]":
            $ mc.business.change_funds(- overload_cost)

            $ machinery_room_overload += 10

            "The production lines in [p_division.formalName] are now working at [machinery_room_overload]%%"
            call advance_time from machinery_room_overload_label_1
        "No":
            pass

    return
