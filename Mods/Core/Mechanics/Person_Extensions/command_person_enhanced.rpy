
init 2 python:
    def give_panties_requirement(person):
        if person.obedience < 110:
            return "Requires: 110 Obedience"
        if person.effective_sluttiness() < 30 and person.love < 30:
            return "Requires: 30 Sluttiness or 30 Love"
        return True

    # extend the bugfix build_command_person_actions_menu function
    def build_command_person_actions_menu2(the_person):
        result = build_command_person_actions_menu(the_person)
        give_panties_action = Action("Give me your panties", requirement = give_panties_requirement, effect = "give_panties_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Ask " + the_person.title + " to hand over her panties.", priority = -5)
        result.insert(4, give_panties_action)
        return result

    # this only works when we can enhance the menu from the bugfix
    if "build_command_person_actions_menu" in globals():
        config.label_overrides["command_person"] = "command_person_enhanced"

label command_person_enhanced(the_person):
    mc.name "[the_person.title], I want you to do something for me."
    the_person "Yes [the_person.mc_title]?"

    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items([build_command_person_actions_menu2(the_person)]))
    else:
        call screen main_choice_display([build_command_person_actions_menu2(the_person)])

    if _return != "Return":
        $ _return.call_action()
    return

label give_panties_label(the_person):
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
