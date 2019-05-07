init -1 python:
    biotech_actions = []
    gene_modifications = []
    body_modifications = []

init 3 python:

    def biotech_lab_requirement():
        return True

    biotech_action = Action("Do things in the lab", biotech_lab_requirement, "biotechs",
        menu_tooltip = "Do stuff")


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

    def modify_person_requirement():
        return True
    modify_person = Action("Modify a person", modify_person_requirement, "modify_person",
        menu_tooltip = "Modify the appearance of a person through magic, not science")
    gene_modifications.append(modify_person)

    def change_body_requirement():
        return True
    change_body = Action("Change body: [person.body_type]", change_body_requirement, "change_body",
        menu_tooltip = "Modify [person.title]'s body type.")
    body_modifications.append(change_body)

    def change_skin_requirement():
        return True
    change_skin = Action("Change skin: [person.skin]", change_skin_requirement, "change_skin",
        menu_tooltip = "Modify [person.title]'s skin tone.")
    body_modifications.append(change_skin)
    def change_face_requirement():
        return True
    change_face = Action("Change face: [person.face_style]", change_face_requirement, "change_face",
        menu_tooltip = "Modify [person.title]'s face style.")
    body_modifications.append(change_face)
    def change_breasts_requirement():
        return True
    change_breasts = Action("Change breasts: [person.tits]", change_breasts_requirement, "change_breasts",
        menu_tooltip = "Modify [person.title]'s cup size.")
    body_modifications.append(change_breasts)
label biotechs():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                biotech_options = []
                for act in biotech_actions:
                    biotech_options.append(act)
                biotech_options.append("Back")
                act_choice = call_formated_action_choice(biotech_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()

label gene_modifications():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                gene_modification_options = []
                for act in gene_modifications:
                    gene_modification_options.append(act)
                gene_modification_options.append("Back")
                act_choice = call_formated_action_choice(gene_modification_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()


label clone_person():
    $ clone_name = None
    $ clone_last_name = None
    $ clone_age = None

    while True:
        python: # First we select which employee we want

                tuple_list = format_person_list(all_people_in_the_game(), draw_hearts = True) #The list of people to show. e.g mc.location.people
                tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
                person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

        if person_choice == "Back":
            return # Where to go if you hit "Back".
        else:
            $ person = person_choice
            $ person.draw_person(emotion = "default")

            call cloning_process(person)

label cloning_process(person):
    while True:
        menu:

            "Give the clone a name":
                $ clone_name = str(renpy.input("Name: ", person.name))
                $ clone_last_name = str(renpy.input("Last name: ", person.last_name))
            "Age":
                $ clone_age = int(renpy.input("Age: ", person.age))
                if clone_age < 18:
                    $ clone_age = 18



            "Begin production:{image=gui/heart/Time_Advance.png} \n{size=22}Name: [clone_name] [clone_last_name], Age: [clone_age]{/size}":

                if clone_name == None:
                    $ clone_name = person.name
                if clone_last_name == None:
                    $ clone_last_name = person.last_name
                if clone_age == None:
                    $ clone_age = person.age

                $ clone = create_random_person(name = clone_name, last_name = clone_last_name, age = clone_age, body_type = person.body_type, face_style = person.face_style, tits = person.tits, height = person.height, hair_colour = person.hair_colour, hair_style = person.hair_style, skin = person.skin, eyes = person.eyes, job = None,
                    personality = person.personality, custom_font = None, name_color = None, dial_color = None, starting_wardrobe = person.wardrobe, stat_array = None, skill_array = None, sex_array = None,
                    start_sluttiness = person.sluttiness, start_obedience = person.obedience, start_happiness = person.happiness, start_love = person.love, start_home = None, title = "Clone", possessive_title = "Your creation", mc_title = "Creator")

                $ clone.schedule[0] = rd_division_basement
                $ clone.schedule[1] = rd_division_basement
                $ clone.schedule[2] = rd_division_basement
                $ clone.schedule[3] = rd_division_basement
                $ clone.schedule[4] = rd_division_basement

                $ clone.special_role.append(clone_role)

                $ rd_division_basement.add_person(clone) #Create rooms for the clones to inhabit until a schedule is given (through being hired or player input)

                "[clone_name] [clone_last_name] created..."
                $ advance_time()
                return
            "Back":
                return

label modify_person():
    while True:
        python: # First we select which employee we want

                tuple_list = format_person_list(all_people_in_the_game(), draw_hearts = True) #The list of people to show. e.g mc.location.people
                tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
                person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

        if person_choice == "Back":

            return # Where to go if you hit "Back".
        else:
            $ person = person_choice
            $ person.draw_person(emotion = "default")
            call modification_process(person)

label modification_process(person):
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                body_modification_options = []
                for act in body_modifications:
                    body_modification_options.append(act)
                body_modification_options.append("Back")
                act_choice = call_formated_action_choice(body_modification_options)

        if act_choice == "Back":
            $ renpy.scene("Active")
            return
        else:
            $ act_choice.call_action()

label change_body():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                body_types = []
                for n in list_of_body_types:
                    body_types.append(n)
                body_types.append("Back")
                body_choice = renpy.display_menu(simple_list_format(body_types, n, string = "Body Type: "),True,"Choice")

        if body_choice == "Back":
            return
        else:
            $ person.body_type = body_choice
            $ person.draw_person()

label change_skin():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                skin_styles = [x[0] for x in list_of_skins]

                skin_styles.append("Back")
                skin_choice = renpy.display_menu(simple_list_format(skin_styles, x[0], string = "Skin Type: "),True,"Choice")
        if skin_choice == "Back":
            return
        else:
            $ person.skin = skin_choice
            $ person.match_skin(skin_choice)
            $ person.draw_person()

label change_face():

    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                face_styles = []
                for face in list_of_faces:
                    face_styles.append(face)
                face_styles.append("Back")
                face_choice = renpy.display_menu(simple_list_format(face_styles, face, string = "Face Type: "),True,"Choice")

        if face_choice == "Back":
            return
        else:
            $ person.face_style = face_choice
            $ person.match_skin(person.skin)
            $ person.draw_person()

label change_breasts():

    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                cup_sizes = [x[0] for x in list_of_tits]
                cup_sizes.append("Back")
                cup_choice = renpy.display_menu(simple_list_format(cup_sizes, x[0], string = "Cup Size: "),True,"Choice")

        if cup_choice == "Back":
            return
        else:
            $ person.tits = cup_choice
            $ person.draw_person()
