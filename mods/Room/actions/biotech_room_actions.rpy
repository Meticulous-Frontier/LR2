init -1 python:
    biotech_actions = []
    gene_modifications = []

init 3 python:

    def biotech_lab_requirement():
        return True

    biotech_action = Action("Do things in the lab", biotech_lab_requirement, "biotechs",
        menu_tooltip = "Do stuff")
    rd_division_basement.actions.append(biotech_action)

    def gene_modification_requirement():
        return True

    gene_modification = Action("Do genetic modifications", gene_modification_requirement, "gene_modifications",
        menu_tooltip = "Do stuff with genes or cosmetic alterations")
    biotech_actions.append(gene_modification)

    def clone_person_requirement():
        return True

    clone_person = Action("Clone a person", clone_person_requirement, "clone_person",
        menu_tooltip = "Create a near identical clone of the targeted person")
    gene_modifications.append(clone_person)

label biotechs():
    python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            biotech_options = []
            for act in biotech_actions:
                biotech_options.append(act)
            biotech_options.append("Back")
            act_choice = call_formated_action_choice(biotech_options)

            if act_choice == "Back":
                renpy.jump("game_loop")
            else:
                act_choice.call_action()

label gene_modifications():
    python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            gene_modification_options = []
            for act in gene_modifications:
                gene_modification_options.append(act)
            gene_modification_options.append("Back")
            act_choice = call_formated_action_choice(gene_modification_options)

            if act_choice == "Back":
                renpy.jump("biotechs")
            else:
                act_choice.call_action()


label clone_person():
    python: # First we select which employee we want

            tuple_list = format_person_list(all_people_in_the_game(), draw_hearts = True) #The list of people to show. e.g mc.location.people
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

            if person_choice == "Back":
                renpy.jump("gene_modifications") # Where to go if you hit "Back".

    $ the_person = person_choice
    $ the_person.draw_person(emotion = "default")
    "Do you wish to clone [the_person.name]?"
    menu:
        "Yes":
            "Give the clone a name"
            $ clone_name = str(renpy.input("Name: ", the_person.name))
            "Give the clone a last name"
            $ clone_last_name = str(renpy.input("Last name: ", the_person.last_name))
        "No":
            return

    $ clone = create_random_person(name = clone_name, last_name = clone_last_name, age = the_person.age, body_type = the_person.body_type, face_style = the_person.face_style, tits = the_person.tits, height = the_person.height, hair_colour = the_person.hair_colour, hair_style = the_person.hair_style, skin = the_person.skin, eyes = the_person.eyes, job = None,
        personality = the_person.personality, custom_font = None, name_color = None, dial_color = None, starting_wardrobe = the_person.wardrobe, stat_array = None, skill_array = None, sex_array = None,
        start_sluttiness = the_person.sluttiness, start_obedience = the_person.obedience, start_happiness = the_person.happiness, start_love = the_person.love, start_home = None)

    $ clone.schedule[0] = rd_division_basement
    $ clone.schedule[1] = rd_division_basement
    $ clone.schedule[2] = rd_division_basement
    $ clone.schedule[3] = rd_division_basement
    $ clone.schedule[4] = rd_division_basement

    $ rd_division_basement.add_person(clone) #Create rooms for the clones to inhabit until a schedule is given (through being hired or player input)
    "[clone_name] [clone_last_name] created..."
    return
