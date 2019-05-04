## Business Meeting Crisis Mod by Tristimdorion
init -1 python:
    coffee_break_weight = 5

init 2 python:
    def coffee_break_requirement():
        if not mc.business.is_weekend():
            if time_of_day > 1 and time_of_day < 4: # only during morning afternoon or evening
                if len(mc.business.get_requirement_employee_list(slut_required = 0)) >= 3:
                    return True
        return False

    coffee_break_action = ActionMod("Coffee Break Crisis", coffee_break_requirement, "coffee_break_action_description",
        menu_tooltip = "A group of employees is having a coffee break.", category = "Business")
    crisis_list.append([coffee_break_action, coffee_break_weight])

label coffee_break_action_description:
    call coffee_break_action from _call_coffee_break_action_1
    return

label coffee_break_action:
    #Generate list of people with poor obedience
    $ list_of_possible_people = mc.business.get_requirement_employee_list(slut_required = 0)
    $ person_one = get_random_from_list(list_of_possible_people)
    $ list_of_possible_people.remove(person_one)
    $ person_two = get_random_from_list(list_of_possible_people)
    $ list_of_possible_people.remove(person_two)
    $ person_three = get_random_from_list(list_of_possible_people)

    mc.name "As you are walking around the office, you see several employees at the coffee machine. They haven't noticed you, but you can hear what they are saying."
    $ person_one.draw_person(emotion = "default")
    person_one.char "Don't you think [the_person.mc_title] is really good looking."
    $ person_two.draw_person(emotion = "default", character_placement = character_center_flipped) #TODO: Build in better support for multi character drawing.
    person_two.char "I like how his butt flexes in his pants."
    $ person_three.draw_person(emotion = "default", character_placement = character_left_flipped)
    person_three.char "To be honest, I much more prefer the other side."

    $ person_one.draw_person(emotion = "happy")
    $ person_two.draw_person(emotion = "happy")
    $ person_three.draw_person(emotion = "happy")
    "The girls start laughing at [person_three.title]'s last remark."

    person_one.char "That was very funny [person_one.name], but I have to get back to work."
    $ person_one.draw_person(position = "walking_away")
    "[person_three.title] walks off to her workstation."
    # remove person 1 from scene
    $ person_one.clear_scene()

    if person_two.sluttiness > 40:
        #TODO: Make a three some with remaining girls

        person_two.char "Oh, she's such a stickler for rules."
        person_one.char "I don't mind seeing her go."

    else:
        $ person_two.draw_person(character_placement = character_center)
        person_two.char "Yeah, we better get going too."
        $ person_two.draw_person(position = "walking_away")
        $ person_three.draw_person(position = "walking_away")

        "You watch [person_two.title] and [person_three.title] walk away together."

    # remove person 2 from scene
    $ person_two.clear_scene()
    # remove person 3 from scene
    $ person_three.clear_scene()
    return
