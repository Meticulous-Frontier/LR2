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

    def demand_panties_requirement(the_person):
        if the_person.vagina_visible() and not the_person.wearing_panties():
            return False
        if not (the_person.obedience >= 120 or the_person.effective_sluttiness() >= 30 or the_person.love >= 30):
            return "Requires: 120 Obedience\nor 30 Sluttiness or 30 Love"
        return True

label demand_panties_label(the_person):
    "You lean over and whisper softly in her ear..."
    mc.name "I want you to give me your panties..."

    if not the_person.wearing_panties():
        the_person "I would love to do that [the_person.mc_title], except that I'm not wearing any..."
        mc.name "Ah, I see, you were expecting something to happen today..."
        return

    if not the_person.can_remove_panties() and the_person.effective_sluttiness() < 60:
        if mc.location.get_person_count() > 1:
            the_person "I could do that [the_person.mc_title], but other people might notice if I start stripping down."
            mc.name "Why don't you stop wearing panties, so I don't have to ask for them?"
            the_person "Maybe next time..."
        else:
            the_person "I'm sorry [the_person.mc_title], but I'm not stripping down, just to give you my panties."
            mc.name "Next time wear something that allows you to take them off without stripping."
        return

    # store outfit and panties
    $ test_outfit = the_person.outfit.get_copy()
    $ the_item = test_outfit.get_panties()
    if the_item.is_extension: #two piece item
        $ the_item = next((x for x in test_outfit.get_upper_ordered() if x.has_extension == the_item), None)
    $ removed_something = False

    if not the_person.can_remove_panties():
        the_person "This might take a minute..."
        if mc.location.get_person_count() > 1:
            "[the_person.possessive_title] takes a quick look around and starts stripping down."
        else:
            "[the_person.possessive_title] starts stripping down, giving you her [the_item.display_name]."
        $ the_person.strip_to_vagina(visible_enough = True)
        the_person "Here you are, anything else I can do for you?"
        $ removed_something = True
    else:
        "[the_person.possessive_title] takes a quick look around and pulls off her [the_item.display_name], placing them in your hand."

    python:
        # remove panties from outfit
        if the_item:
            test_outfit.remove_clothing(the_item)
        # put on outfit without panties
        the_person.apply_outfit(test_outfit)
        the_person.draw_person()
        test_outfit = None
        the_item = None
        the_person.change_stats(obedience = 1, slut = 1, max_slut = 30)

    if removed_something:
        "She quickly puts her clothes back on."
    else:
        the_person "Is this what you were looking for?"
    return
