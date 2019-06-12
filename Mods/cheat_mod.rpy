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


        # if editing_target.skin == "white":
        #     editing_target.body_images = white_skin
        # elif editing_target.skin == "tan":
        #     editing_target.body_images = tan_skin
        # elif editing_target.skin == "black":
        #     editing_target.body_images = black_skin
        editing_target.expression_images = Expression("default", editing_target.skin, editing_target.face_style)
        editing_target.draw_person()
        return

init python:
    config.overlay_screens = ["keybind"]
    config.console = True # Enables the console, can be set to False.

screen keybind():
    key "z" action ToggleScreen("cheat_menu")
    key "Z" action ToggleScreen("cheat_menu")


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
    default available_naming = {
        "Title": ["title"],
        "Player's Title": ["mc_title"],
        "Possesive Title": ["possessive_title"],
        "First Name": ["name"],
        "Last Name": ["last_name"]
        }

    default available_personalities = {}
    if available_personalities == {}:
        $ for x in list_of_personalities: available_personalities[x.personality_type_prefix] = x

    default available_faces = [x for x in list_of_faces]

    default list_of_bodies = [white_skin, tan_skin, black_skin] #Assemble the cloth items into a list. Revisit this later if a default list is created
    default available_skin = {
        "White": ["white", list_of_bodies[0]],
        "Tan": ["tan", list_of_bodies[1]],
        "Black": ["black", list_of_bodies[2]]
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
                xysize (1100, 200)
                grid 5 1:
                    xfill True
                    vbox:
                        textbutton "Name Options for [editing_target.name]":
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
                    grid 3 1:
                        xfill True
                        yfill True
                        vbox:
                            textbutton "Personality":
                                style "textbutton_no_padding_highlight"
                                text_style "serum_text_style"
                                xfill True

                                action ToggleScreenVariable("personality_options")

                            if personality_options:
                                viewport:
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        for x in available_personalities:
                                            if hasattr(editing_target, "personality"):
                                                textbutton "Type" + ": " + str(x):
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
                            textbutton "Face Type":
                                style "textbutton_no_padding_highlight"
                                text_style "serum_text_style"
                                xfill True

                                action ToggleScreenVariable("face_options")

                            if face_options:
                                viewport:
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        for x in available_faces:
                                            if hasattr(editing_target, "face_style"):
                                                textbutton "Type" + ": " + str(x):
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
                            textbutton "Skin Type":
                                style "textbutton_no_padding_highlight"
                                text_style "serum_text_style"
                                xfill True

                                action ToggleScreenVariable("skin_options")

                            if skin_options:
                                viewport:
                                    mousewheel True
                                    draggable True
                                    vbox:
                                        for x in available_skin:
                                            if hasattr(editing_target, "skin"):
                                                textbutton x + ": " + str(available_skin[x][0]):
                                                    xfill True
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"

                                                    if editing_target.skin == available_skin[x][0]:
                                                        background "#4f7ad6"
                                                        hover_background "#4f7ad6"

                                                    action [
                                                        Function(setattr, editing_target, "skin", available_skin[x][0]),
                                                        Function(setattr, editing_target, "body_images", available_skin[x][1]),
                                                        Function(cheat_appearance)
                                                    ]

                                                    alternate [
                                                        Function(setattr, editing_target, "skin", available_skin[x][0]),
                                                        Function(setattr, editing_target, "body_images", available_skin[x][1]),
                                                        Function(cheat_appearance)
                                                    ]
                        # vbox:
                        #     textbutton "Body Type":
                        #         style "textbutton_no_padding_highlight"
                        #         text_style "serum_text_style"
                        #         xfill True
                        #
                        #         action ToggleScreenVariable("body_options")
                        #
                        #     if body_options:
                        #         viewport:
                        #             mousewheel True
                        #             draggable True
                        #             vbox:
                        #                 for x in list_of_body_types:
                        #                     if hasattr(editing_target, "body_type"):
                        #                         textbutton x + ": " + str(available_skin[x][0]):
                        #                             xfill True
                        #                             style "textbutton_no_padding_highlight"
                        #                             text_style "serum_text_style"
                        #
                        #                             if editing_target.skin == available_skin[x][0]:
                        #                                 background "#4f7ad6"
                        #                                 hover_background "#4f7ad6"
                        #
                        #                             action [
                        #                                 Function(setattr, editing_target, "skin", available_skin[x][0]),
                        #                                 Function(setattr, editing_target, "body_images", available_skin[x][1]),
                        #                                 Function(cheat_appearance)
                        #                             ]
                        #
                        #                             alternate [
                        #                                 Function(setattr, editing_target, "skin", available_skin[x][0]),
                        #                                 Function(setattr, editing_target, "body_images", available_skin[x][1]),
                        #                                 Function(cheat_appearance)
                        #                             ]
