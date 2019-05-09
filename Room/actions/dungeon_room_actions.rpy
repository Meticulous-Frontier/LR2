init -1 python:
    dungeon_actions = []
    slave_training_actions = []

init 3 python:

    def dungeon_actions_requirement():
        return True

    dungeon_action = Action("Manage [office_basement.formalName]", dungeon_actions_requirement, "dungeon_action",
        menu_tooltip = "Do things in the [office_basement.formalName]")

    def train_slave_requirement():
        for person in office_basement.people:
            if person.obedience >= 130:
                return True
        return "Need obedient person present. \n Requires: Obedience 130"

    train_slave = Action("Prospect a Slave", train_slave_requirement, "train_slave",
        menu_tooltip = "Choose a person for slave-play training")
    dungeon_actions.append(train_slave)

    def sex_slave_requirement():
        if time_of_day != 4:
            return True
        else:
            return "Too late"
    sex_slave_action = Action("Intercourse {image=gui/heart/Time_Advance.png}", sex_slave_requirement, "sex_slave_label",
        menu_tooltip = "Have sex with [the_person.title]")
    slave_training_actions.append(sex_slave_action)

    def appoint_slave_requirement():
        if the_person.obedience >= 500:
            return True
        else:
            return "Requires: 500 Obedience"
    appoint_slave = Action("Declear Slave {image=gui/heart/Time_Advance.png}", appoint_slave_requirement, "appoint_slave_label",
        menu_tooltip = "Make it official that [the_person.title] is your personal slave.")
    slave_training_actions.append(appoint_slave)
label dungeon_action():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                dungeon_options = []
                for act in dungeon_actions:
                    dungeon_options.append(act)
                dungeon_options.append("Back")
                act_choice = call_formated_action_choice(dungeon_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()

label train_slave():
    while True:
        $ tuple_list = office_basement.people + ["Back"]
        call screen person_choice(tuple_list, draw_hearts = True)
        $ person_choice = _return        

        if person_choice == "Back":
            return # Where to go if you hit "Back".
        else:
            if person_choice.obedience < 130:
                "[the_person.title] needs more obedience first"
            else:
                call train_slave_menu(person_choice)

label train_slave_menu(person_choice = the_person): # default to the person when called from action choice
    $ the_person = person_choice
    $ the_person.draw_person()
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                slave_training_options = []
                for act in slave_training_actions:
                    slave_training_options.append(act)
                slave_training_options.append("Back")
                act_choice = call_formated_action_choice(slave_training_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()

label sex_slave_label():
    call fuck_person(the_person)
    "After some sexual disciplinary actions [the_person.title] becomes a bit more obedient."
    $ the_person.change_obedience(+10)
    $ advance_time()

    return

label appoint_slave_label():
    "You have a nice cermony and you got yourself a slave."
    # the_person.special_role.append(slave_role)
    return
