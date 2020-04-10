init -1 python:
    biotech_body_modifications = []

init 3 python:
    def biotech_clone_person_requirement():
        if not time_of_day == 4:
            return True
        else:
            return "Too late."

    biotech_clone_person = Action("Clone a person {image=gui/heart/Time_Advance.png}", biotech_clone_person_requirement, "biotech_clone_person",
        menu_tooltip = "Create a near identical clone of the targeted person")

    def biotech_modify_person_requirement():
        return True

    biotech_modify_person = Action("Modify a person", biotech_modify_person_requirement, "biotech_modify_person",
        menu_tooltip = "Modify the appearance of a person through magic, not science")

    def biotech_change_body_requirement():
        hypothyroidism = find_in_list(lambda x: x.name == hypothyroidism_serum_trait.name, list_of_traits)
        anorexia = find_in_list(lambda x: x.name == anorexia_serum_trait.name, list_of_traits)

        if mc.business.is_trait_researched(hypothyroidism_serum_trait) and mc.business.is_trait_researched(anorexia_serum_trait):
            return True
        else:
            return "Requires: [hypothyroidism_serum_trait.name] and [anorexia_serum_trait.name] researched"

    biotech_change_body = Action("Change body: [person.body_type]", biotech_change_body_requirement, "biotech_change_body",
        menu_tooltip = "Modify [person.title]'s body type.")
    biotech_body_modifications.append(biotech_change_body)

    def biotech_change_skin_requirement():
        if mc.business.is_trait_researched(pigment_serum_trait):
            return True
        else:
            return "Requires: [pigment_serum_trait.name] researched"

    biotech_change_skin = Action("Change skin: [person.skin]", biotech_change_skin_requirement, "biotech_change_skin",
        menu_tooltip = "Modify [person.title]'s skin tone.")
    biotech_body_modifications.append(biotech_change_skin)

    def biotech_change_face_requirement():
        return True

    biotech_change_face = Action("Change face: [person.face_style]", biotech_change_face_requirement, "biotech_change_face",
        menu_tooltip = "Modify [person.title]'s face style.")
    biotech_body_modifications.append(biotech_change_face)

    def biotech_change_breasts_requirement():
        if mc.business.is_trait_researched(breast_enhancement):
            return True
        else:
            return "Requires: [breast_enhancement.name] and [breast_reduction.name]"

    def create_clone(person, clone_name, clone_last_name, clone_age):
        if clone_name is None:
            clone_name = person.name
        if clone_last_name is None:
            clone_last_name = person.last_name
        if clone_age is None:
            clone_age = person.age

        clone = make_person(name = clone_name, last_name = clone_last_name, age = clone_age, body_type = person.body_type, face_style = person.face_style, tits = person.tits, height = person.height, hair_colour = person.hair_colour, hair_style = person.hair_style, skin = person.skin, eyes = person.eyes, job = None,
            personality = person.personality, custom_font = None, name_color = None, dial_color = None, starting_wardrobe = person.wardrobe, stat_array = None, skill_array = None, sex_array = None,
            start_sluttiness = person.sluttiness, start_obedience = person.obedience, start_happiness = person.happiness, start_love = person.love, start_home = None, title = "Clone", possessive_title = "Your creation", mc_title = "Creator", relationship = "Single", kids = 0, force_random = True)

        clone.generate_home()
        clone.set_schedule([0,1,2,3,4], dungeon)

        clone.special_role.append(clone_role)

        dungeon.add_person(clone) #Create rooms for the clones to inhabit until a schedule is given (through being hired or player input)
        return

    biotech_change_breasts = Action("Change breasts: [person.tits]", biotech_change_breasts_requirement, "biotech_change_breasts",
        menu_tooltip = "Modify [person.title]'s cup size.")
    biotech_body_modifications.append(biotech_change_breasts)


label biotech_gene_modifications():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            gene_modification_options = []
            for act in biotech_gene_modifications:
                gene_modification_options.append(act)
            gene_modification_options.append("Back")
            act_choice = call_formated_action_choice(gene_modification_options)
            del gene_modification_options

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()


label biotech_clone_person():
    while True:
        # only known people who are not unique character or clone herself (genetic degradation too high)
        if "bugfix_installed" in globals():
            call screen main_choice_display(build_menu_items([get_sorted_people_list([x for x in known_people_in_the_game([mc] + unique_character_list) if not clone_role in x.special_role], "Clone Person", ["Back"])]))
        else:
            call screen main_choice_display([get_sorted_people_list([x for x in known_people_in_the_game([mc] + unique_character_list) if not clone_role in x.special_role], "Clone Person", ["Back"])])

        if _return == "Back":
            return # Where to go if you hit "Back".
        else:
            call cloning_process(_return) from _call_cloning_process

label cloning_process(person = the_person): # default to the_person when not passed as parameter
    $ person.draw_person(emotion = "default")
    $ clone_name = None
    $ clone_last_name = None
    $ clone_age = None

    while True:
        menu:

            "Give the clone a name":
                $ clone_name = str(renpy.input("Name: ", person.name))
                $ clone_last_name = str(renpy.input("Last name: ", person.last_name))
            "Age":
                $ clone_age = int(renpy.input("Age: ", person.age))
                if clone_age < 18:
                    $ clone_age = 18
            "Begin production: {image=gui/heart/Time_Advance.png}\n{size=22}Name: [clone_name] [clone_last_name], Age: [clone_age]{/size}":
                $ create_clone(person, clone_name, clone_last_name, clone_age)
                "The clone has been created and is now awaiting you in [dungeon.formalName]"
                call advance_time from _call_advance_time_cloning_process
                return
            "Back":
                return

label biotech_modify_person():
    while True:
        if "bugfix_installed" in globals():
            call screen main_choice_display(build_menu_items([get_sorted_people_list(known_people_in_the_game([mc]), "Modify Person", ["Back"])]))
        else:
            call screen main_choice_display([get_sorted_people_list(known_people_in_the_game([mc]), "Modify Person", ["Back"])])

        if _return == "Back":
            return # Where to go if you hit "Back".
        else:
            call modification_process(_return) from _call_modification_process

label modification_process(person = the_person): # when called without specific person use the_person variable
    $ person.draw_person(emotion = "default")
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            body_modification_options = []
            for act in biotech_body_modifications:
                body_modification_options.append(act)
            body_modification_options.append("Back")
            act_choice = call_formated_action_choice(body_modification_options)
            del body_modification_options

        if act_choice == "Back":
            $ renpy.scene("Active")
            return
        else:
            $ act_choice.call_action()
            $ del act_choice

label biotech_change_body():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            body_types = []
            for n in list_of_body_types:
                body_types.append(n)
            body_types.append("Back")
            body_choice = renpy.display_menu(simple_list_format(body_types, n, string = "Body Type: ", ignore = "Back"),True,"Choice")
            del body_types

        if body_choice == "Back":
            return
        else:
            $ person.body_type = body_choice
            $ person.draw_person()
            $ del body_choice

label biotech_change_skin():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            skin_styles = [x[0] for x in list_of_skins]

            skin_styles.append("Back")
            skin_choice = renpy.display_menu(simple_list_format(skin_styles, x[0], string = "Skin Type: ", ignore = "Back"),True,"Choice")
            del skin_styles

        if skin_choice == "Back":
            return

        else:
            $ person.skin = skin_choice
            $ person.match_skin(skin_choice)
            $ person.draw_person()
            $ del skin_choice

label biotech_change_face():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            face_styles = []
            for face in list_of_faces:
                face_styles.append(face)
            face_styles.append("Back")
            face_choice = renpy.display_menu(simple_list_format(face_styles, face, string = "Face Type: ", ignore = "Back"),True,"Choice")
            del face_styles

        if face_choice == "Back":
            return
        else:
            $ person.face_style = face_choice
            $ person.match_skin(person.skin)
            $ person.draw_person()
            $ del face_choice

label biotech_change_breasts():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            cup_sizes = [x[0] for x in list_of_tits]
            cup_sizes.append("Back")
            cup_choice = renpy.display_menu(simple_list_format(cup_sizes, x[0], string = "Cup Size: ", ignore = "Back"),True,"Choice")
            del cup_sizes

        if cup_choice == "Back":
            return
        else:
            $ person.tits = cup_choice
            $ person.draw_person()
            $ del cup_choice
