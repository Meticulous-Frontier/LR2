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

    mc.name "As you are walking around the office, you see several employees at the coffee machine."
    $ person_one.draw_person(emotion = "default")
    person_one.char "Telling a story."
    $ person_two.draw_person(character_placement = character_center) #TODO: Build in better support for multi character drawing.
    person_two.char "Listening"
    $ person_three.draw_person(character_placement = character_left)
    person_three.char "Listening"

    $ person_two.draw_person(emotion = "happy")
    person_two.char "Starts smiling"

    $ person_three.draw_person(emotion = "happy")
    person_three.char "Starts laughing"

    person_three.char "That was very funny [person_one.name], but I have to get back to work."
    $ person_three.draw_person(position = "walking_away")
    person_two.char "Oh, she's such a stickler for rules."
    $ person_three.reset_placement()

    person_one.char "I don't mind seeing her go."

    $ person_one.reset_placement()
    $ person_two.reset_placement()

    return 