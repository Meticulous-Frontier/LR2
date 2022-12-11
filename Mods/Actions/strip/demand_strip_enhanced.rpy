init 10 python:
    def build_demand_strip_menu_enhanced(the_person):
        demand_panties_action = Action("Give me your panties", demand_panties_requirement, "demand_panties_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Ask " + the_person.title + " to hand over her panties.")
        demand_strip_tits_action = Action("Get your tits out", demand_strip_tits_requirement, "demand_strip_tits_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Have her strip down until you can see her tits.")
        demand_strip_underwear_action = Action("Strip to your underwear", demand_strip_underwear_requirement, "demand_strip_underwear_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Have her strip down until she's only in her underwear.")
        demand_strip_naked_action = Action("Get naked", demand_strip_naked_requirement, "demand_strip_naked_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Have her strip until she is completely naked.")

        return ["Strip Command", demand_panties_action, demand_strip_tits_action, demand_strip_underwear_action, demand_strip_naked_action, ["Never mind", "Return"]]
    build_demand_strip_menu = build_demand_strip_menu_enhanced

init 5 python:
    def demand_strip_requirement_enhanced(the_person):
        if (demand_panties_requirement(the_person) is False # If there's nothing to strip, don't show action
            and demand_strip_tits_requirement(the_person) is False
            and demand_strip_underwear_requirement(the_person) is False
            and demand_strip_naked_requirement(the_person) is False
        ):
            return False
        if the_person.obedience < 110:
            return "Requires: 110 Obedience"
        return True
    demand_strip_requirement = demand_strip_requirement_enhanced
