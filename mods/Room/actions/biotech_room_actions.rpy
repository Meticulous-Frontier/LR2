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

    def modify_person_requirement():
        return True
    modify_person = Action("Modify a person", modify_person_requirement, "modify_person",
        menu_tooltip = "Modify the appearance of a person through magic, not science")
    gene_modifications.append(modify_person)

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
    $ clone_name = None
    $ clone_last_name = None
    $ clone_age = None
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
            jump cloning_process
        "No":
            $renpy.scene("Active")
            jump clone_person
    menu cloning_process:
        "Give the clone a name":
            $ clone_name = str(renpy.input("Name: ", the_person.name))
            $ clone_last_name = str(renpy.input("Last name: ", the_person.last_name))
        "Age":
            $ clone_age = int(renpy.input("Age: ", the_person.age))
            if clone_age < 18:
                $ clone_age = 18



        "Begin production:{image=gui/heart/Time_Advance.png} \n{size=22}Name: [clone_name] [clone_last_name], Age: [clone_age]{/size}":

            if clone_name == None:
                $ clone_name = the_person.name
            if clone_last_name == None:
                $ clone_last_name = the_person.last_name
            if clone_age == None:
                $ clone_age = the_person.age

            $ clone = create_random_person(name = clone_name, last_name = clone_last_name, age = clone_age, body_type = the_person.body_type, face_style = the_person.face_style, tits = the_person.tits, height = the_person.height, hair_colour = the_person.hair_colour, hair_style = the_person.hair_style, skin = the_person.skin, eyes = the_person.eyes, job = None,
                personality = the_person.personality, custom_font = None, name_color = None, dial_color = None, starting_wardrobe = the_person.wardrobe, stat_array = None, skill_array = None, sex_array = None,
                start_sluttiness = the_person.sluttiness, start_obedience = the_person.obedience, start_happiness = the_person.happiness, start_love = the_person.love, start_home = None, title = "Clone", possessive_title = "Your creation", mc_title = "Creator")

            $ clone.schedule[0] = rd_division_basement
            $ clone.schedule[1] = rd_division_basement
            $ clone.schedule[2] = rd_division_basement
            $ clone.schedule[3] = rd_division_basement
            $ clone.schedule[4] = rd_division_basement

            $ rd_division_basement.add_person(clone) #Create rooms for the clones to inhabit until a schedule is given (through being hired or player input)

            "[clone_name] [clone_last_name] created..."
            $ advance_time()
            jump clone_person
        "Back":
            jump clone_person
    jump cloning_process

label modify_person():
    python: # First we select which employee we want

            tuple_list = format_person_list(all_people_in_the_game(), draw_hearts = True) #The list of people to show. e.g mc.location.people
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

            if person_choice == "Back":
                renpy.jump("gene_modifications") # Where to go if you hit "Back".

    $ the_person = person_choice
    $ the_person.draw_person(emotion = "default")
    "Do you wish to modify [the_person.name]?"
    menu:
        "Yes":
            jump modification_process
        "No":
            $renpy.scene("Active")
            jump modify_person

    menu modification_process:
        "Change body: [the_person.body_type]":
            menu modification_body:
                "Thin Body":
                    $ the_person.body_type = "thin_body"
                    $ cheat_redraw_face()
                    $ cheat_redraw_body()

                "Standard Body":
                    $ the_person.body_type = "standard_body"
                    $ cheat_redraw_face()
                    $ cheat_redraw_body()

                "Curvy Body":
                    $ the_person.body_type = "curvy_body"
                    $ cheat_redraw_face()
                    $ cheat_redraw_body()
                "Back":
                    jump modification_process
            jump modification_body
        "Change skin: [the_person.skin]":
            menu modification_skin:
                "White Skin":
                    $ the_person.skin = "white"
                    $ the_person.body_images = white_skin
                    $ cheat_redraw_face()
                    $ cheat_redraw_body()

                "Tan Skin":
                    $ the_person.skin = "tan"
                    $ person_choice.body_images = tan_skin
                    $ cheat_redraw_face()
                    $ cheat_redraw_body()

                "Black Skin":
                    $ the_person.skin = "black"
                    $ person_choice.body_images = black_skin
                    $ cheat_redraw_face()
                    $ cheat_redraw_body()

                "Back":
                    jump modification_process
            jump modification_skin
        "Change face: [the_person.face_style]":
            menu modification_face:
                "Face Style 1":
                    $ the_person.face_style = "Face_1"
                    $ cheat_redraw_face()

                "Face Style 2":
                    $ the_person.face_style = "Face_2"
                    $ cheat_redraw_face()

                "Face Style 3":
                    $ the_person.face_style = "Face_3"
                    $ cheat_redraw_face()

                "Face Style 4":
                    $ the_person.face_style = "Face_4"
                    $ cheat_redraw_face()

                "Face Style 5":
                    $ the_person.face_style = "Face_5"
                    $ cheat_redraw_face()

                "Face Style 6":
                    $ the_person.face_style = "Face_6"
                    $ cheat_redraw_face()

                "Back":
                    jump modification_process
            jump modification_face
        "Change breast size: [the_person.tits]":
            menu modification_tits:
                "Set cup size A":
                    $ the_person.tits = "A"
                    $ the_person.draw_person(the_person)

                "Set cup size AA":
                    $ the_person.tits = "AA"
                    $ the_person.draw_person(the_person)

                "Set cup size B":
                    $ the_person.tits = "B"
                    $ the_person.draw_person(the_person)

                "Set cup size C":
                    $ the_person.tits = "C"
                    $ the_person.draw_person(the_person)

                "Set cup size D":
                    $ the_person.tits = "D"
                    $ the_person.draw_person(the_person)

                "Set cup size DD":
                    $ the_person.tits = "DD"
                    $ the_person.draw_person(the_person)

                "Set cup size DDD":
                    $ the_person.tits = "DDD"
                    $ the_person.draw_person(the_person)

                "Set cup size E":
                    $ the_person.tits = "E"
                    $ the_person.draw_person(the_person)

                "Set cup size F":
                    $ the_person.tits = "F"
                    $ the_person.draw_person(the_person)

                "Set cup size FF":
                    $ the_person.tits = "FF"
                    $ the_person.draw_person(the_person)

                "Back":
                    jump modification_process
            jump modification_tits
        "Back":
            jump modify_person
    jump modification_process
