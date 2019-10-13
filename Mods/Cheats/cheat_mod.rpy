# I wanted to give it a go at making a mostly modular cheat menu that is easy to configure and also extends itself as options more options e.g faces, personalitites are made available
# I think I have a fairly good idea of how to bypass the quirks regarding lack of lists in certain aspects of the game e.g stats, but it is not quite there yet.

# Adding and removing basic variables works the way I want. Can just throw in a new variable into the list and it just works, which is fine, but for things like skin and body_images (where you need two different inputs to get 1 result)
# it becomes a bit more difficult coming up with good solutions

# Worst case scenario for me right now would be that it's just even easier to keep it up to date at regular intervals
# Going to see if I can add a separate screen for a "crisis master" as in the previous cheat screen, but only if I find a way to make it somewhat build itself on its own

init 2 python:
    def edit_name_func(new_name):

        cs = renpy.current_screen()
        editing_target = cs.scope["editing_target"]
        x = cs.scope["name_type"]

        setattr(editing_target, x, new_name)

        renpy.restart_interaction()

    def cheat_appearance():
        cs = renpy.current_screen()
        editing_target = cs.scope["editing_target"]
        editing_target.expression_images = Expression("default", editing_target.skin, editing_target.face_style)
        editing_target.draw_person()
        return

init python:
    if "keybind1" not in config.overlay_screens:
        config.overlay_screens.append("keybind1")
    config.console = True # Enables the console, can be set to False.

screen keybind1():
    key "x" action ToggleScreen("cheat_menu")
    key "X" action ToggleScreen("cheat_menu")


screen cheat_menu():

    # Screen management variables
    default main_screen_showing = True
    default naming_options = False # Extends the name_options viewport
    default time_control_showing = True

    default main_stats_options = True
    default work_skills_options = True
    default sex_stats_options = True
    default relation_options = True
    default face_options = True
    default body_options = True
    default skin_options = True
    default breast_options = True

    default personality_options = True
    default appearance_options = True
    # Input management variables
    default name_select = False #Determines if the name button is currently taking an input or not

    default editable_characters = [mc, the_person, mc.business] # Add unique characters to this list if you want to customize them often
    default editing_target = None

    # Lists for common skill attributes.
    default main_stats = { #The arrays are utilized in this order: key = "DisplayName", [0 = hasattr check], [1 = variable / key], [2 = amount to changed] NOTE: Fields are duplicated incase things change later, less likely that the buttons will need to be re formated
        "Charisma": ["charisma", "charisma", 1],
        "Focus": ["focus", "focus", 1],
        "Intelligence": ["int", "int", 1],

        "Age": ["age", "age", 1],

        "Arousal": ["arousal", "arousal", 10],
        "Stamina": ["current_stamina", "current_stamina", 5],

        "Funds": ["funds", "funds", 100000],
        "Supplies": ["supply_count", "supply_count", 100000],
        "Effectivity": ["team_effectiveness", "team_effectiveness", 1000],
        "Max Effectivity": ["effectiveness_cap", "effectiveness_cap", 1000] # Might add If statement to combine these two as they go hand in hand
        }
    default work_skills = {
        "Human Resources": ["hr_skill", "hr_skill", 1],
        "Marketing": ["market_skill", "market_skill", 1],
        "Researching": ["research_skill", "research_skill", 1],
        "Production": ["production_skill", "production_skill", 1],
        "Supplying": ["supply_skill", "supply_skill", 1],

        "Max Employees": ["max_employee_count", "max_employee_count", 10],
        "Production Lines": ["production_lines", "production_lines", 1],
        "Serum Batch Sizes": ["batch_size", "batch_size", 10],
        "Research Tier": ["research_tier", "research_tier", 1]

        }
    default relation_stats = {
        "Happiness": ["happiness", "happiness", 10],
        "Love": ["love", "love", 10],
        "Suggestibility": ["suggestibility", "suggestibility", 10],
        "Sluttiness": ["sluttiness", "sluttiness", 10],
        "Core Sluttiness": ["core_sluttiness", "core_sluttiness", 10],
        "Obedience": ["obedience", "obedience", 10]
        }
    default sex_stats = { # Sex Skills are stored in a dict
        "Foreplay": ["sex_skills", "Foreplay", 1],
        "Oral": ["sex_skills", "Oral", 1],
        "Vaginal": ["sex_skills", "Vaginal", 1],
        "Anal": ["sex_skills", "Anal", 1]
        }
    default available_naming = { # Consider making it update the respective lists custom titles when it becomes possible
        "Title": ["title"],
        "Player's Title": ["mc_title"],
        "Possesive Title": ["possessive_title"],
        "First Name": ["name"],
        "Last Name": ["last_name"]
        }

    default available_personalities = {}
    if available_personalities == {}:
        $ for x in list_of_personalities: available_personalities[x.personality_type_prefix] = x
        if "list_of_extra_personalities" in globals():
            $ for x in list_of_extra_personalities: available_personalities[x.personality_type_prefix] = x



    default available_faces = [x for x in list_of_faces]
    default available_body_types = [x for x in list_of_body_types]
    default available_breast_sizes = [x[0] for x in list_of_tits]

    default list_of_bodies = [white_skin, tan_skin, black_skin] #Assemble the cloth items into a list. Revisit this later if a default list is created
    default available_skin = { #
        "White": ["skin", "body_images", "white", list_of_bodies[0]],
        "Tan": ["skin", "body_images",  "tan", list_of_bodies[1]],
        "Black": ["skin", "body_images",  "black", list_of_bodies[2]]
        }

    default name_type = None
    # Lists for player exclusive attributes
    # Lists for person exclusive attributes
    # Lists for business exclusive attributes

    # Lists for other Objects attributes



    frame: # A main frame that all child elements position themselves after, covers the whole screen.
        background None
        yfill True
        xfill True
        if time_control_showing: # This section must have fail safes so creating individual buttons as before
            frame:
                xysize (390, 50)
                hbox:
                    # xfill True
                    # yfill True
                    grid 3 1:
                        xfill True
                        yfill True
                        textbutton "D: " + day_names[day%7]:
                            xfill True
                            yfill True
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"

                            action [
                                SetVariable("day", day + 1)
                            ]
                            alternate [
                                SetVariable("day", day - 1)
                            ]

                        textbutton "T: " + time_names[time_of_day]:
                            xfill True
                            yfill True
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"

                            action [
                                If(time_of_day == 4, true = SetVariable("time_of_day", time_of_day - 4), false = SetVariable("time_of_day", time_of_day + 1))
                            ]
                            alternate [
                                If(time_of_day == 0, true = SetVariable("time_of_day", time_of_day + 4), false = SetVariable("time_of_day", time_of_day - 1))
                            ]

                        textbutton "End Day":
                            xfill True

                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"

                            action [
                                SetVariable("time_of_day", 4), Call("advance_time", from_current=True)
                            ]

        if main_screen_showing:
            frame:
                yalign 0.5
                xysize (260,250)
                hbox:
                    vbox:
                        textbutton "Cheat Menu":
                            xfill True
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"
                            action [
                                Hide("cheat_menu")
                            ]
                        viewport:
                            mousewheel True
                            draggable True
                            ysize 125
                            vbox:
                                for x in editable_characters:
                                    if hasattr(x, "name"):
                                        textbutton x.name:
                                            xfill True

                                            if editing_target == x:
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"

                                            sensitive True

                                            hovered [
                                                NullAction()
                                            ]
                                            action [

                                                ToggleScreenVariable("editing_target", x, None)
                                            ]

                                            alternate [
                                                NullAction()
                                            ]


        if editing_target is not None:
            frame:
                xalign 0.5
                xysize (1100, 275)
                grid 5 1:
                    xfill True
                    vbox:
                        textbutton "Name Options":
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"
                            xfill True

                            action ToggleScreenVariable("naming_options")

                        if naming_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for x in available_naming:
                                        if hasattr(editing_target, str(available_naming[x][0])):
                                            button:
                                                id "name_select"
                                                margin [2,2]
                                                xfill True

                                                background "#000080"

                                                if name_type == available_naming[x][0]:
                                                    background "#4f7ad6"
                                                    hover_background "#4f7ad6"

                                                action [ToggleScreenVariable("name_select"), SetScreenVariable("name_type", available_naming[x][0])]

                                                if name_select:
                                                    input default str(vars(editing_target)[available_naming[x][0]]):
                                                        changed edit_name_func
                                                        style "serum_text_style"
                                                        yalign 0.5
                                                        xalign 0.5
                                                        xfill True

                                                else:
                                                    text x + ": "+ str(vars(editing_target)[available_naming[x][0]]):
                                                        yalign 0.5
                                                        yfill True
                                                        style "serum_text_style"
                    vbox:
                        textbutton "Main Stats":
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"
                            xfill True

                            action ToggleScreenVariable("main_stats_options")

                        if main_stats_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for x in main_stats:
                                        if hasattr(editing_target, str(main_stats[x][0])):
                                            textbutton x + ": " + str(vars(editing_target)[main_stats[x][1]]):
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"

                                                action [
                                                    Function(setattr, editing_target, main_stats[x][0], vars(editing_target)[main_stats[x][1]] + main_stats[x][2])
                                                ]

                                                alternate [
                                                    Function(setattr, editing_target, main_stats[x][0], vars(editing_target)[main_stats[x][1]] - main_stats[x][2])
                                                ]

                    vbox:
                            #Make this check if editing_target has any of the attributes in the list instead.
                        textbutton "Work Skills":
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"
                            xfill True

                            action ToggleScreenVariable("work_skills_options")
                        if work_skills_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for x in work_skills:
                                        if hasattr(editing_target, str(work_skills[x][0])):
                                            textbutton x + ": " + str(vars(editing_target)[work_skills[x][1]]):
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"

                                                action [
                                                    Function(setattr, editing_target, work_skills[x][0], vars(editing_target)[work_skills[x][1]] + work_skills[x][2])
                                                ]

                                                alternate [
                                                    Function(setattr, editing_target, work_skills[x][0], vars(editing_target)[work_skills[x][1]] - work_skills[x][2])
                                                ]
                    vbox:
                        textbutton "Sex Skills":
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"
                            xfill True

                            action ToggleScreenVariable("sex_stats_options")

                        if sex_stats_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for x in sex_stats:
                                        if hasattr(editing_target, str(sex_stats[x][0])):
                                            textbutton x + ": " + str(vars(editing_target)[sex_stats[x][0]][sex_stats[x][1]]):
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"

                                                action [
                                                    SetDict(vars(editing_target)[sex_stats[x][0]], sex_stats[x][1], vars(editing_target)[sex_stats[x][0]][sex_stats[x][1]] + sex_stats[x][2])
                                                ]

                                                alternate [
                                                    SetDict(vars(editing_target)[sex_stats[x][0]], sex_stats[x][1], vars(editing_target)[sex_stats[x][0]][sex_stats[x][1]] - sex_stats[x][2])
                                                ]

                    vbox:

                        textbutton "Relations":
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"
                            xfill True

                            action ToggleScreenVariable("relation_options")

                        if relation_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for x in relation_stats:
                                        if hasattr(editing_target, str(relation_stats[x][0])):
                                            textbutton x + ": " + str(vars(editing_target)[relation_stats[x][0]]):
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"

                                                action [
                                                    Function(setattr, editing_target, relation_stats[x][0], vars(editing_target)[relation_stats[x][1]] + relation_stats[x][2])
                                                ]

                                                alternate [
                                                    Function(setattr, editing_target, relation_stats[x][0], vars(editing_target)[relation_stats[x][1]] - relation_stats[x][2])
                                                ]

        if editing_target is not None:
            frame:
                yalign 1.0
                xalign 0.5
                xysize (1100, 200)
                hbox:
                    grid 5 1:
                        xfill True
                        yfill True
                        vbox:
                            if type(editing_target) is not Business and type(editing_target) is not MainCharacter:
                                textbutton "Personality":
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True

                                    action ToggleScreenVariable("personality_options")
                            else:
                                pass
                            if personality_options:
                                viewport:
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        for x in available_personalities:
                                            if hasattr(editing_target, "personality"):
                                                textbutton str(x):
                                                    xfill True
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"


                                                    if editing_target.personality == available_personalities[x]:
                                                        background "#4f7ad6"
                                                        hover_background "#4f7ad6"

                                                    action [
                                                        Function(setattr, editing_target, "personality", available_personalities[x])
                                                    ]

                                                    alternate [
                                                        Function(setattr, editing_target, "personality", available_personalities[x])
                                                    ]



                        vbox:
                            if type(editing_target) is not Business and type(editing_target) is not MainCharacter:
                                hbox:
                                    textbutton "Face Type":
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"

                                        action ToggleScreenVariable("face_options")

                                    textbutton "Hair":
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"
                                        xfill True
                                        action ToggleScreen("cheat_hair_dresser", None, editing_target, editing_target.hair_style, editing_target.hair_colour)
                            else:
                                pass

                            if face_options:
                                viewport:
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        for x in available_faces:
                                            if hasattr(editing_target, "face_style"):
                                                textbutton str(x):
                                                    xfill True
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"

                                                    if editing_target.face_style == x:
                                                        background "#4f7ad6"
                                                        hover_background "#4f7ad6"

                                                    action [
                                                        Function(setattr, editing_target, "face_style", x),
                                                        Function(cheat_appearance)
                                                    ]

                                                    alternate [
                                                        Function(setattr, editing_target, "face_style", x),
                                                        Function(cheat_appearance)
                                                    ]



                        vbox:
                            if type(editing_target) is not Business and type(editing_target) is not MainCharacter:
                                textbutton "Skin Type":
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True

                                    action ToggleScreenVariable("skin_options")
                            else:
                                pass

                            if skin_options:
                                viewport:
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        for x in available_skin:
                                            if hasattr(editing_target, available_skin[x][0] and available_skin[x][1]):
                                                textbutton x:
                                                    xfill True
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"

                                                    if editing_target.skin == available_skin[x][2]:
                                                        background "#4f7ad6"
                                                        hover_background "#4f7ad6"

                                                    action [
                                                        Function(setattr, editing_target, available_skin[x][0], available_skin[x][2]),
                                                        Function(setattr, editing_target, available_skin[x][1], available_skin[x][3]),
                                                        Function(cheat_appearance)
                                                    ]

                                                    alternate [
                                                        Function(setattr, editing_target, available_skin[x][0], available_skin[x][2]),
                                                        Function(setattr, editing_target, available_skin[x][1], available_skin[x][3]),
                                                        Function(cheat_appearance)
                                                    ]



                        vbox:
                            if type(editing_target) is not Business and type(editing_target) is not MainCharacter: #These options will never be relevant to a Business Object, but might want to revisit later once the grand scope of the game is settled down.
                                textbutton "Body Type":
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True

                                    action ToggleScreenVariable("body_options")
                            else:
                                pass

                            if body_options:
                                viewport:
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        for x in available_body_types:
                                            if hasattr(editing_target, "body_type"):
                                                textbutton x:
                                                    xfill True
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"

                                                    if editing_target.body_type == x: # TODO: Take a look at this after you have slept some. Why isn't this working?
                                                       background "4f7ad6"
                                                       hover_background "4f7ad6"

                                                    action [
                                                       Function(setattr, editing_target, "body_type", x),
                                                       Function(cheat_appearance)
                                                    ]

                                                    alternate [
                                                       Function(setattr, editing_target, "body_type", x),
                                                       Function(cheat_appearance)
                                                    ]



                        vbox:
                            if type(editing_target) is not Business and type(editing_target) is not MainCharacter:
                                textbutton "Breast Size":
                                    style "textbutton_no_padding_highlight"
                                    text_style "serum_text_style"
                                    xfill True

                                    action ToggleScreenVariable("breast_options")
                            else:
                                pass

                            if breast_options:
                                viewport:
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        for x in available_breast_sizes:
                                            if hasattr(editing_target, "tits"):
                                                textbutton str(x):
                                                    xfill True
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"

                                                    if editing_target.tits == x:
                                                        background "#4f7ad6"
                                                        hover_background "#4f7ad6"

                                                    action [
                                                        Function(setattr, editing_target, "tits", x),
                                                        Function(cheat_appearance)
                                                    ]

                                                    alternate [
                                                        Function(setattr, editing_target, "tits", x),
                                                        Function(cheat_appearance)
                                                    ]

screen cheat_hair_dresser(person, old_hair_style, old_hair_colour): ##Pass the person and the variables holding the current hair style
    modal True
    default catagory_selected = "Hair Style"
    default valid_catagories = ["Hair Style"] #Holds the valid list of catagories strings to be shown at the top.

    $ catagories_mapping = {
        "Hair Style": [hair_styles]
    }

    default bar_select = 0 # 0 is nothing selected, 1 is red, 2 is green, 3 is blue, and 4 is alpha

    default selected_colour = "colour" #If secondary we are alterning the patern colour. When changed it updates the colour of the clothing item. Current values are "colour" and "colour_pattern"
    default current_r = person.hair_colour[1][0]
    default current_g = person.hair_colour[1][1]
    default current_b = person.hair_colour[1][2]
    default current_a = person.hair_colour[1][3]

    default selected_hair_colour_name = person.hair_colour[0]
    default selected_hair_colour = person.hair_colour[1]
    default selected_hair_style = person.hair_style

    hbox: #The main divider between the new item adder and the current outfit view.
        xpos 15
        yalign 0.5
        yanchor 0.5
        spacing 15
        frame:
            background "#aaaaaa"
            padding (20,20)
            xysize (880, 1015)
            hbox:
                spacing 15
                vbox: #Catagories select on far left
                    spacing 15
                    for catagory in valid_catagories:
                        textbutton catagory:
                            style "textbutton_style"
                            text_style "textbutton_text_style"
                            if catagory == catagory_selected:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            else:
                                background "#1a45a1"
                                hover_background "#3a65c1"
                            text_align(0.5,0.5)
                            text_anchor(0.5,0.5)
                            xysize (220, 60)
                            action [SetScreenVariable("catagory_selected",catagory),
                                SetScreenVariable("selected_colour", "colour")]

                vbox:
                    spacing 15
                    viewport:
                        ysize 480
                        xminimum 605
                        scrollbars "vertical"
                        mousewheel True
                        frame:
                            xsize 620
                            yminimum 480
                            background "#888888"
                            vbox:
                                if catagory_selected in catagories_mapping:
                                    for hair_style_item in catagories_mapping[catagory_selected][0]:
                                        textbutton hair_style_item.name:
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            background "#1a45a1"
                                            hover_background "#3a65c1"
                                            xfill True
                                            sensitive True
                                            action [
                                                SetScreenVariable("selected_colour", "colour"),
                                                SetScreenVariable("selected_hair_style", hair_style_item),
                                                SetField(hair_style_item, "colour", [current_r, current_g, current_b, current_a]),
                                                SetField(person, "hair_colour[1]", [current_r, current_g, current_b, current_a]),
                                                SetField(person, "hair_style", hair_style_item),
                                                Function(person.draw_person)]

                    frame:
                        #THIS IS WHERE SELECTED ITEM OPTIONS ARE SHOWN
                        xysize (605, 480)
                        background "#888888"
                        vbox:
                            spacing 10
                            if selected_hair_style is not None:
                                text selected_hair_style.name style "textbutton_text_style"

                                hbox:
                                    spacing -5 #We will manually handle spacing so we can have our colour predictor frames
                                    textbutton "Primary Colour":
                                        style "textbutton_style"
                                        text_style "textbutton_text_style"
                                        if selected_colour == "colour":
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                            hover_background "#3a65c1"
                                        sensitive True
                                        action NullAction()

                                    frame:
                                        background Color(rgb=(current_r,current_g,current_b,current_a))
                                        xysize (45,45)
                                        yanchor 0.5
                                        yalign 0.5

                                    textbutton "Dye Hair":
                                        style "textbutton_style"
                                        text_style "textbutton_text_style"
                                        background "#1a45a1"
                                        hover_background "#3a65c1"
                                        sensitive True
                                        xoffset 20
                                        action [
                                            SetField(selected_hair_style, "colour", [current_r, current_g, current_b, current_a]),
                                            SetField(person, "hair_colour", [selected_hair_colour_name, [current_r,current_g,current_b,current_a]]),
                                            SetField(person, "hair_style", selected_hair_style),
                                            Function(person.draw_person)
                                        ]

                                hbox:
                                    spacing 10
                                    vbox:
                                        text "Red" style "textbutton_text_style"
                                        hbox:
                                            if bar_select == 1:
                                                frame:
                                                    input default current_r length 4 changed colour_changed_r allow ".0123456789" style "menu_text_style"
                                                    xsize 70
                                                    ysize 50
                                            else:
                                                button:
                                                    background "#888888"
                                                    action SetScreenVariable("bar_select",1)
                                                    text "%.2f" % current_r style "menu_text_style"
                                                    xsize 70
                                                    ysize 50

                                            bar value ScreenVariableValue("current_r", 1.0)  xsize 120 ysize 45 style style.slider #unhovered #SetScreenVariable("current_r",__builtin__.round(current_r,2))
                                    vbox:
                                        text "Green" style "textbutton_text_style"
                                        hbox:
                                            if bar_select == 2:
                                                frame:
                                                    input default current_g length 4 changed colour_changed_g allow ".0123456789" style "menu_text_style"
                                                    xsize 70
                                                    ysize 50
                                            else:
                                                button:
                                                    background "#888888"
                                                    action SetScreenVariable("bar_select",2)
                                                    text "%.2f" % current_g style "menu_text_style"
                                                    xsize 70
                                                    ysize 50

                                            bar value ScreenVariableValue("current_g", 1.0) xsize 120 ysize 45 style style.slider #unhovered SetScreenVariable("current_g",__builtin__.round(current_g,2))
                                    vbox:
                                        text "Blue" style "textbutton_text_style"
                                        hbox:
                                            if bar_select == 3:
                                                frame:
                                                    input default current_b length 4 changed colour_changed_b allow ".0123456789" style "menu_text_style"
                                                    xsize 70
                                                    ysize 50
                                            else:
                                                button:
                                                    background "#888888"
                                                    action SetScreenVariable("bar_select",3)
                                                    text "%.2f" % current_b style "menu_text_style"
                                                    xsize 70
                                                    ysize 50

                                            bar value ScreenVariableValue("current_b", 1.0) xsize 120 ysize 45 style style.slider #unhovered SetScreenVariable("current_b",__builtin__.round(current_b,2))

                                text "Transparency: " style "menu_text_style"
                                hbox:
                                    spacing 20
                                    button:
                                        if current_a == 1.0:
                                            background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                        text "Normal" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                        xysize (120, 40)
                                        action SetScreenVariable("current_a", 1.0)

                                    button:
                                        if current_a == 0.95:
                                            background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                        text "Sheer" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                        xysize (120, 40)
                                        action SetScreenVariable("current_a", 0.95)

                                    button:
                                        if current_a == 0.8:
                                            background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                        text "Translucent" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                        xysize (120, 40)
                                        action SetScreenVariable("current_a", 0.8)
                                for block_count, hair_colour_list in __builtin__.enumerate(split_list_in_blocks(list_of_hairs, 10)):
                                    hbox:
                                        spacing 5
                                        xalign 0.5
                                        xanchor 0.5
                                        yanchor (block_count * .1)
                                        for count, hair_colour in __builtin__.enumerate(hair_colour_list):
                                            frame:
                                                background "#aaaaaa"
                                                button:
                                                    background Color(rgb=(hair_colour[1][0], hair_colour[1][1], hair_colour[1][2]))
                                                    xysize (40,40)
                                                    sensitive True
                                                    action [
                                                        SetScreenVariable("selected_hair_colour_name", hair_colour[0]),
                                                        SetScreenVariable("selected_hair_colour", hair_colour[1]),
                                                        SetScreenVariable("current_r", hair_colour[1][0]),
                                                        SetScreenVariable("current_g", hair_colour[1][1]),
                                                        SetScreenVariable("current_b", hair_colour[1][2]),
                                                        SetScreenVariable("current_a", hair_colour[1][3]),
                                                        SetField(selected_hair_style, "colour", [hair_colour[1][0], hair_colour[1][1], hair_colour[1][2], hair_colour[1][3]]),
                                                        SetField(person, "hair_colour", hair_colour),
                                                        SetField(person, "hair_style", selected_hair_style),
                                                        Function(person.draw_person)
                                                    ]
                                                    # We use a fixed pallette of hair colours
        vbox:
            spacing 15
            frame:
                xysize (440, 500)
                background "#aaaaaa"
                padding (20,20)
                vbox:
                    spacing 15
                    text "Current Hair Style" style "textbutton_text_style"
                    frame:
                        xfill True
                        yfill True
                        background "#888888"
                        vbox:
                            spacing 5 #TODO: Add a viewport here too.
                            button:
                                background Color(rgb = (selected_hair_colour[0], selected_hair_colour[1], selected_hair_colour[2]))
                                xysize (380, 40)
                                action NullAction()
                                xalign 0.5
                                yalign 0.0
                                text selected_hair_style.name xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 style "outfit_style"




            frame:
                background "#aaaaaa"
                xysize (440, 500)
                padding (20,20)
                vbox:
                    yalign 0.0
                    hbox:
                        yalign 1.0
                        xalign 0.5
                        xanchor 0.5
                        spacing 50
                        textbutton "Save Haircut" action [Hide("cheat_hair_dresser")] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xysize (155,80)
                        textbutton "Abandon Design" action [SetField(person, "hair_colour", old_hair_colour), SetField(person, "hair_style", old_hair_style), Hide("cheat_hair_dresser")] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xysize (185,80)
