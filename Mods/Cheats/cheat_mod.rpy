# I wanted to give it a go at making a mostly modular cheat menu that is easy to configure and also extends itself as options more options e.g faces, personalitites are made available
# I think I have a fairly good idea of how to bypass the quirks regarding lack of lists in certain aspects of the game e.g stats, but it is not quite there yet.

# Adding and removing basic variables works the way I want. Can just throw in a new variable into the list and it just works, which is fine, but for things like skin and body_images (where you need two different inputs to get 1 result)
# it becomes a bit more difficult coming up with good solutions

# Worst case scenario for me right now would be that it's just even easier to keep it up to date at regular intervals
# Going to see if I can add a separate screen for a "crisis master" as in the previous cheat screen, but only if I find a way to make it somewhat build itself on its own
init -2 style cheat_text_style: # General text style used in the serum screens.
    text_align 0.5
    size 18
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    xalign 0.5


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
        #editing_target.expression_images = Expression("default", editing_target.skin, editing_target.face_style)
        editing_target.draw_person()
        return

    def cheat_collapse_menus():
        cs = renpy.current_screen()
        cs.scope["personality_options"] = False
        cs.scope["face_options"] = False
        cs.scope["eye_options"] = False
        cs.scope["skin_options"] = False
        cs.scope["body_options"] = False
        cs.scope["breast_options"] = False
        cs.scope["hair_style_options"] = False
        cs.scope["hair_colour_options"] = False
        cs.scope["pubes_options"] = False
        cs.scope["pubes_color_options"] = False
        cs.scope["font_color_options"] = False
        cs.scope["salary_options"] = False
        for div in cs.scope["divisions"]:
            cs.scope["divisions"][div][1] = False

    def toggle_division_visibility(division):
        cs = renpy.current_screen()
        cs.scope["divisions"][division][1] = not cs.scope["divisions"][division][1]

    def cheat_set_company_salaries(multiplier = 1):
        for person in mc.business.market_team + mc.business.production_team + mc.business.research_team + mc.business.supply_team + mc.business.hr_team:
            person.salary = person.calculate_base_salary() * multiplier

    def cheat_person_font_color(person, color):
        if hasattr(person.char, "color"):
            person.char.color = color
        if hasattr(person.char, "what_color"):
            person.char.what_color = color
        if hasattr(person.char, "what_args"):
            person.char.what_args["color"] = color
        if hasattr(person.char, "who_args"):
            person.char.who_args["color"] = color

        person.set_title(remove_display_tags(person.title))
        person.set_possessive_title(remove_display_tags(person.possessive_title))
        person.set_mc_title(remove_display_tags(person.mc_title))

    def cheat_restore_screen():
        if "the_person" in globals():
            the_person.draw_person()
        else:
            clear_scene()

init python:
    if "keybind1" not in config.overlay_screens:
        config.overlay_screens.append("keybind1")
    config.console = True # Enables the console, can be set to False.

screen keybind1():
    key "x" action [
        ToggleScreen("cheat_menu"),
        Function(cheat_restore_screen)
    ]
    key "X" action [
        ToggleScreen("cheat_menu"),
        Function(cheat_restore_screen)
    ]


screen cheat_menu():

    # Screen management variables
    default main_screen_showing = True
    default naming_options = True # Extends the name_options viewport
    default time_control_showing = True

    default main_stats_options = True
    default work_skills_options = True
    default sex_stats_options = True
    default relation_options = True

    default appearance_options = True

    default salary_options = False

    default personality_options = False
    default face_options = False
    default eye_options = False
    default skin_options = False
    default body_options = False
    default breast_options = False
    default hair_style_options = False
    default hair_colour_options = False
    default pubes_options = False
    default pubes_color_options = False
    default font_color_options = False

    default divisions = {
        "Research" : [ mc.business.research_team, False],
        "Production" : [ mc.business.production_team, False],
        "Supply" : [ mc.business.supply_team, False ],
        "Marketing" : [ mc.business.market_team, False ],
        "HR" : [ mc.business.hr_team, False ]
    }


    # Input management variables
    default name_select = False #Determines if the name button is currently taking an input or not

    if "the_person" in globals():
        default editable_characters = [mc, the_person, mc.business] # Add unique characters to this list if you want to customize them often
        default editing_target = the_person # default open the_person cheat menu
    else:
        default editable_characters = [mc, mc.business] # Add unique characters to this list if you want to customize them often
        default editing_target = mc.business

    # Lists for common skill attributes.
    # The arrays are utilized in this order: key = "DisplayName", [0 = hasattr check], [1 = variable / key], [2 = amount to changed], [3 = sort order]
    # NOTE: Fields are duplicated incase things change later, less likely that the buttons will need to be re formated
    default main_stats = {
        "Charisma": ["charisma", "charisma", 1, 0],
        "Focus": ["focus", "focus", 1 , 1],
        "Intelligence": ["int", "int", 1, 2],

        "Age": ["age", "age", 1, 3],
        "Height": ["height", "height", .005, 4],
        "Energy": ["energy", "energy", 10.0, 5],
        "Max Energy": ["max_energy", "max_energy", 10.0, 6],

        "Funds": ["funds", "funds", 10000, 7],
        "Supplies": ["supply_count", "supply_count", 10000, 8],
        "Effectivity": ["team_effectiveness", "team_effectiveness", 10, 9],
        "Max Effectivity": ["effectiveness_cap", "effectiveness_cap", 10, 10] # Might add If statement to combine these two as they go hand in hand
        }
    default work_skills = {
        "HR": ["hr_skill", "hr_skill", 1, 0],
        "Marketing": ["market_skill", "market_skill", 1, 1],
        "Researching": ["research_skill", "research_skill", 1, 2],
        "Production": ["production_skill", "production_skill", 1, 3],
        "Supplying": ["supply_skill", "supply_skill", 1, 4],
        "Salary": ["salary", "salary", 1, 6],

        "Max Employees": ["max_employee_count", "max_employee_count", 5, 5],
        "Production Lines": ["production_lines", "production_lines", 1, 6],
        "Serum Batch Size": ["batch_size", "batch_size", 5, 7],
        "Research Tier": ["research_tier", "research_tier", 1, 8]
        }
    default relation_stats = {
        "Love": ["love", "love", 10, 0],
        "Suggestibility": ["suggestibility", "suggestibility", 10, 1],
        "Obedience": ["obedience", "obedience", 10, 2],
        "Happiness": ["happiness", "happiness", 10, 3],
        "Arousal": ["arousal", "arousal", 10, 4],
        "Sluttiness": ["sluttiness", "sluttiness", 10, 5],
        "Core Sluttiness": ["core_sluttiness", "core_sluttiness", 10, 6]
        }
    default sex_stats = { # Sex Skills are stored in a dict
        "Foreplay": ["sex_skills", "Foreplay", 1, 0],
        "Oral": ["sex_skills", "Oral", 1, 1],
        "Vaginal": ["sex_skills", "Vaginal", 1, 2],
        "Anal": ["sex_skills", "Anal", 1, 3]
        }

    # Consider making it update the respective lists custom titles when it becomes possible
    default available_naming = {
        "Title": ["title"],
        "Player's Title": ["mc_title"],
        "Reference Title": ["possessive_title"],
        "First Name": ["name"],
        "Last Name": ["last_name"]
        }

    default available_personalities = {}
    python:
        if available_personalities == {}:
            for x in list_of_personalities: available_personalities[x.personality_type_prefix] = x
            if "list_of_extra_personalities" in globals():
                for x in list_of_extra_personalities: available_personalities[x.personality_type_prefix] = x

    default available_faces = sorted(list_of_faces, key = lambda x: int(x.split("_")[1]))
    default available_eyes = sorted(list_of_eyes,  key = lambda x: x[0])
    default available_body_types = list_of_body_types
    default available_breast_sizes = [x[0] for x in list_of_tits]
    default available_hair_styles = sorted(hair_styles, key = lambda x: x.name)
    default available_hair_colours = sorted(list_of_hairs, key = lambda x: x[0])
    default available_pubes_styles = sorted(pube_styles, key = lambda x: x.name)

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
                            text_style "cheat_text_style"

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
                            text_style "cheat_text_style"

                            action [
                                If(time_of_day == 4, true = SetVariable("time_of_day", time_of_day - 4), false = SetVariable("time_of_day", time_of_day + 1))
                            ]
                            alternate [
                                If(time_of_day == 0, true = SetVariable("time_of_day", time_of_day + 4), false = SetVariable("time_of_day", time_of_day - 1))
                            ]

                        textbutton "End Day":
                            xfill True

                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"

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
                            text_style "cheat_text_style"
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
                                            text_style "cheat_text_style"

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
                xoffset 400
                yoffset 200
                xysize (1100, 300)
                grid 4 1:
                    xfill True
                    vbox:
                        textbutton "Main Stats":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("main_stats_options")

                        if main_stats_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for (x, i) in sorted(main_stats.items(), key=lambda x:x[1][3]):
                                        if hasattr(editing_target, str(main_stats[x][0])):
                                            hbox:
                                                textbutton " - ":
                                                    xsize 36
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"
                                                    action [
                                                        Function(setattr, editing_target, main_stats[x][0], vars(editing_target)[main_stats[x][1]] - main_stats[x][2])
                                                    ]

                                                if isinstance(vars(editing_target)[main_stats[x][1]], int):
                                                    textbutton x + ": " + str(vars(editing_target)[main_stats[x][1]]):
                                                        xsize 198
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "cheat_text_style"

                                                        action [
                                                            Function(setattr, editing_target, main_stats[x][0], vars(editing_target)[main_stats[x][1]] + main_stats[x][2])
                                                        ]

                                                        alternate [
                                                            Function(setattr, editing_target, main_stats[x][0], vars(editing_target)[main_stats[x][1]] - main_stats[x][2])
                                                        ]
                                                else:
                                                    textbutton x + ": " + str(__builtin__.round(vars(editing_target)[main_stats[x][1]], 3)):
                                                        xsize 198
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "cheat_text_style"

                                                        action [
                                                            Function(setattr, editing_target, main_stats[x][0], vars(editing_target)[main_stats[x][1]] + main_stats[x][2])
                                                        ]

                                                        alternate [
                                                            Function(setattr, editing_target, main_stats[x][0], vars(editing_target)[main_stats[x][1]] - main_stats[x][2])
                                                        ]

                                                textbutton " + ":
                                                    xsize 36
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"
                                                    action [
                                                        Function(setattr, editing_target, main_stats[x][0], vars(editing_target)[main_stats[x][1]] + main_stats[x][2])
                                                    ]

                    vbox:
                            #Make this check if editing_target has any of the attributes in the list instead.
                        textbutton "Work Skills":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("work_skills_options")
                        if work_skills_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for (x, y) in sorted(work_skills.items(), key=lambda x:x[1][3]):
                                        if hasattr(editing_target, str(work_skills[x][0])):
                                            hbox:
                                                textbutton " - ":
                                                    xsize 36
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"
                                                    action [
                                                        Function(setattr, editing_target, work_skills[x][0], vars(editing_target)[work_skills[x][1]] - work_skills[x][2])
                                                    ]

                                                textbutton x + ": " + str(vars(editing_target)[work_skills[x][1]]):
                                                    xsize 198
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"

                                                    action [
                                                        Function(setattr, editing_target, work_skills[x][0], vars(editing_target)[work_skills[x][1]] + work_skills[x][2])
                                                    ]

                                                    alternate [
                                                        Function(setattr, editing_target, work_skills[x][0], vars(editing_target)[work_skills[x][1]] - work_skills[x][2])
                                                    ]

                                                textbutton " + ":
                                                    xsize 36
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"
                                                    action [
                                                        Function(setattr, editing_target, work_skills[x][0], vars(editing_target)[work_skills[x][1]] + work_skills[x][2])
                                                    ]
                    vbox:
                        textbutton "Sex Skills":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("sex_stats_options")

                        if sex_stats_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for (x, y) in sorted(sex_stats.items(), key=lambda x:x[1][3]):
                                        if hasattr(editing_target, str(sex_stats[x][0])):
                                            hbox:
                                                textbutton " - ":
                                                    xsize 36
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"
                                                    action [
                                                        SetDict(vars(editing_target)[sex_stats[x][0]], sex_stats[x][1], vars(editing_target)[sex_stats[x][0]][sex_stats[x][1]] - sex_stats[x][2])
                                                    ]

                                                textbutton x + ": " + str(vars(editing_target)[sex_stats[x][0]][sex_stats[x][1]]):
                                                    xsize 198
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"

                                                    action [
                                                        SetDict(vars(editing_target)[sex_stats[x][0]], sex_stats[x][1], vars(editing_target)[sex_stats[x][0]][sex_stats[x][1]] + sex_stats[x][2])
                                                    ]

                                                    alternate [
                                                        SetDict(vars(editing_target)[sex_stats[x][0]], sex_stats[x][1], vars(editing_target)[sex_stats[x][0]][sex_stats[x][1]] - sex_stats[x][2])
                                                    ]

                                                textbutton " + ":
                                                    xsize 36
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"
                                                    action [
                                                        SetDict(vars(editing_target)[sex_stats[x][0]], sex_stats[x][1], vars(editing_target)[sex_stats[x][0]][sex_stats[x][1]] + sex_stats[x][2])
                                                    ]


                    vbox:

                        textbutton "Relations":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True

                            action ToggleScreenVariable("relation_options")

                        if relation_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for (x, y) in sorted(relation_stats.items(), key=lambda x:x[1][3]):
                                        if hasattr(editing_target, str(relation_stats[x][0])):
                                            hbox:
                                                textbutton " - ":
                                                    xsize 36
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"
                                                    action [
                                                        Function(setattr, editing_target, relation_stats[x][0], vars(editing_target)[relation_stats[x][1]] - relation_stats[x][2])
                                                    ]

                                                textbutton x + ": " + str(vars(editing_target)[relation_stats[x][0]]):
                                                    xsize 198
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"

                                                    action [
                                                        Function(setattr, editing_target, relation_stats[x][0], vars(editing_target)[relation_stats[x][1]] + relation_stats[x][2])
                                                    ]

                                                    alternate [
                                                        Function(setattr, editing_target, relation_stats[x][0], vars(editing_target)[relation_stats[x][1]] - relation_stats[x][2])
                                                    ]

                                                textbutton " + ":
                                                    xsize 36
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "cheat_text_style"
                                                    action [
                                                        Function(setattr, editing_target, relation_stats[x][0], vars(editing_target)[relation_stats[x][1]] + relation_stats[x][2])
                                                    ]

            frame:
                xoffset 0
                yoffset 50
                xysize (390, 330)
                grid 1 1:
                    vbox:
                        textbutton "Name Options":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
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
                                                    input default remove_display_tags(str(vars(editing_target)[available_naming[x][0]])):
                                                        changed edit_name_func
                                                        style "cheat_text_style"
                                                        yalign 0.5
                                                        xalign 0.5
                                                        xfill True

                                                else:
                                                    text x + ": "+ str(vars(editing_target)[available_naming[x][0]]):
                                                        yalign 0.5
                                                        yfill True
                                                        style "cheat_text_style"

        if editing_target and isinstance(editing_target, Business):
            frame:
                xoffset 400
                yoffset 510
                xysize (515, 520)
                hbox:
                    vbox:
                        xsize 250
                        textbutton "Salary":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if salary_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("salary_options")]

                        for div in divisions:
                            textbutton div:
                                style "textbutton_no_padding_highlight"
                                text_style "cheat_text_style"
                                xfill True
                                if divisions[div][1]:
                                    background "#4f7ad6"
                                    hover_background "#4f7ad6"
                                action [Function(cheat_collapse_menus), Function(toggle_division_visibility, div)]

                    vbox:
                        xsize 250
                        if salary_options:
                            for x in range(-4, 5):
                                textbutton "Set to " + str((10 + x) * 10) + "%" :
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"
                                    action [
                                        Function(cheat_set_company_salaries, 1.0 + (x/10.0))
                                    ]
                        for div in divisions:
                            if divisions[div][1]:
                                for person in divisions[div][0]:
                                    textbutton person.name + " " + person.last_name:
                                        xfill True
                                        style "textbutton_no_padding_highlight"
                                        text_style "cheat_text_style"
                                        action [
                                            SetScreenVariable("editing_target", person),
                                            Function(cheat_appearance)
                                        ]

        if editing_target and not isinstance(editing_target, Business) and not isinstance(editing_target, MainCharacter):
            frame:
                xoffset 400
                yoffset 510
                xysize (515, 520)
                hbox:
                    vbox:
                        xsize 250
                        textbutton "Face Type":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if face_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("face_options")]

                        textbutton "Skin Type":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if skin_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("skin_options")]

                        textbutton "Body Type":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if body_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("body_options")]

                        textbutton "Breast Size":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if breast_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("breast_options")]

                        textbutton "Eye Colour":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if eye_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("eye_options")]

                        textbutton "Hair Style":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if hair_style_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("hair_style_options")]

                        textbutton "Hair Colour":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if hair_colour_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("hair_colour_options")]

                        textbutton "Pubes Style":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if pubes_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("pubes_options")]

                        textbutton "Pubes Color":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if pubes_color_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("pubes_color_options")]


                        if hasattr(editing_target, "personality") and editing_target.personality.personality_type_prefix in available_personalities:
                            textbutton "Personality":
                                style "textbutton_no_padding_highlight"
                                text_style "cheat_text_style"
                                xfill True
                                if personality_options:
                                    background "#4f7ad6"
                                    hover_background "#4f7ad6"
                                action [Function(cheat_collapse_menus), ToggleScreenVariable("personality_options")]

                        textbutton "Font Color":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            if font_color_options:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            action [Function(cheat_collapse_menus), ToggleScreenVariable("font_color_options")]

                        frame:
                            background None
                            ysize 24

                        textbutton "Hair Salon":
                            style "textbutton_no_padding_highlight"
                            text_style "cheat_text_style"
                            xfill True
                            action ToggleScreen("hair_creator", None, editing_target, editing_target.hair_style.get_copy(), editing_target.pubes_style.get_copy()) # If the screen doesn't exist it provides an ignorable error. While it removes its standalone functionality, maintaining code twice is a hazzle.


                    vbox:
                        xsize 250
                        if personality_options and hasattr(editing_target, "personality"):
                            for x in sorted(available_personalities, key = lambda x: str(x).lower()):
                                textbutton str(x).title():
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.personality.personality_type_prefix == x:
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "personality", available_personalities[x])
                                    ]

                        if face_options and hasattr(editing_target, "face_style"):
                            for x in available_faces:
                                textbutton str(x).replace("_", " "):
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.face_style == x:
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "face_style", x),
                                        Function(cheat_appearance)
                                    ]

                        if eye_options and hasattr(editing_target, "eyes"):
                            for x in available_eyes:
                                textbutton str(x[0]).title():
                                    xfill True
                                    style "textbutton_no_padding_highlight"
                                    text_style "cheat_text_style"

                                    if editing_target.eyes[0] == x[0]:
                                        background "#4f7ad6"
                                        hover_background "#4f7ad6"

                                    action [
                                        Function(setattr, editing_target, "eyes", x),
                                        Function(cheat_appearance)
                                    ]

                        if skin_options and hasattr(editing_target, "skin"):
                            vbox:
                                for x in available_skin:
                                    textbutton x:
                                        xfill True
                                        style "textbutton_no_padding_highlight"
                                        text_style "cheat_text_style"

                                        if editing_target.skin == available_skin[x][2]:
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"

                                        action [
                                            Function(setattr, editing_target, available_skin[x][0], available_skin[x][2]),
                                            Function(setattr, editing_target, available_skin[x][1], available_skin[x][3]),
                                            Function(cheat_appearance)
                                        ]

                        if body_options and hasattr(editing_target, "body_type"):
                            vbox:
                                for x in available_body_types:
                                    textbutton str(x).replace("_", " ").title():
                                        xfill True
                                        style "textbutton_no_padding_highlight"
                                        text_style "cheat_text_style"

                                        if editing_target.body_type == x:
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"

                                        action [
                                            Function(setattr, editing_target, "body_type", x),
                                            Function(cheat_appearance)
                                        ]

                        if breast_options and hasattr(editing_target, "tits"):
                            vbox:
                                for x in available_breast_sizes:
                                    textbutton str(x):
                                        xfill True
                                        style "textbutton_no_padding_highlight"
                                        text_style "cheat_text_style"

                                        if editing_target.tits == x:
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"

                                        action [
                                            Function(setattr, editing_target, "tits", x),
                                            Function(cheat_appearance)
                                        ]

                        if hair_style_options and hasattr(editing_target, "hair_style" and "hair_colour"):
                            vbox:
                                for x in available_hair_styles:
                                    textbutton str(x.name):
                                        xfill True
                                        style "textbutton_no_padding_highlight"
                                        text_style "cheat_text_style"

                                        if editing_target.hair_style == x:
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"

                                        action [
                                            SetField(editing_target,"hair_style", x),
                                            SetField(editing_target, "hair_style.colour", editing_target.hair_colour[1]),
                                            Function(cheat_appearance)
                                        ]

                        if hair_colour_options and hasattr(editing_target, "hair_style" and "hair_colour"):
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                xsize 500

                                vbox:
                                    for x in available_hair_colours:
                                        textbutton str(x[0]).title():
                                            xfill True
                                            style "textbutton_no_padding_highlight"
                                            text_style "cheat_text_style"

                                            if editing_target.hair_colour[0] == x[0]:
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"

                                            action [
                                                SetField(editing_target, "hair_colour", x),
                                                SetField(editing_target, "hair_style.colour", x[1]),
                                                Function(cheat_appearance)
                                            ]

                        if pubes_options and hasattr(editing_target, "pubes_style"):
                            vbox:
                                for x in available_pubes_styles:
                                    textbutton str(x.name):
                                        xfill True
                                        style "textbutton_no_padding_highlight"
                                        text_style "cheat_text_style"

                                        if editing_target.pubes_style == x:
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"

                                        action [
                                            SetField(editing_target, "pubes_style.colour", editing_target.pubes_colour),
                                            SetField(editing_target, "pubes_style", x),
                                            Function(cheat_appearance)
                                        ]

                        if pubes_color_options and hasattr(editing_target, "pubes_colour"):
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                xsize 500
                                vbox:
                                    for x in list_of_hairs:
                                        $ color = x[1]
                                        $ color[3] = 1
                                        textbutton str(x[0]).title():
                                            xfill True
                                            style "textbutton_no_padding_highlight"
                                            text_style "cheat_text_style"

                                            if editing_target.pubes_colour == color:
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"

                                            action [
                                                SetField(editing_target, "pubes_colour", color),
                                                SetField(editing_target, "pubes_style.colour", color),
                                                Function(cheat_appearance)
                                            ]

                        if font_color_options and hasattr(editing_target, "name"):
                            viewport:
                                mousewheel True
                                scrollbars "vertical"
                                xsize 500

                                vbox:
                                    $ name = getattr(editing_target, "name")
                                    for c in readable_color_list:
                                        textbutton "{color=[c]}" + name + "{/color}":
                                            xfill True
                                            style "textbutton_no_padding_highlight"
                                            text_style "cheat_text_style"

                                            if editing_target.char.what_args["color"] == c:
                                                background "#4f7ad6"
                                                hover_background "#4f7ad6"

                                            action [Function(cheat_person_font_color, editing_target, c)]
