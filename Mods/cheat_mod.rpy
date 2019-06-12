init 2 python:
    def edit_name_func(new_name):

        cs = renpy.current_screen()
        editing_target = cs.scope["editing_target"]
        x = cs.scope["name_type"]

        setattr(editing_target, x, new_name)

        renpy.restart_interaction()

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

    default main_stats_options = True
    default work_skills_options = True
    default sex_skills_options = True

    # Input management variables
    default name_select = False #Determines if the name button is currently taking an input or not

    default editable_characters = [mc, the_person, mc.business]
    default editing_target = None

    # Lists for common skill attributes
    default main_stats = ["charisma", "focus", "int", "arousal", "current_stamina"]
    default work_skills = ["hr_skill", "market_skill", "research_skill", "production_skill", "supply_skill"]
    default relation_stats = ["happiness", "love", "suggestibility", "sluttiness", "core_sluttiness", "obedience"]
    default sex_skills = ["Foreplay", "Oral", "Vaginal", "Anal"] # Sex Skills are stored in dict
    default available_naming = ["title", "mc_title", "possessive_title", "name", "last_name"]

    default name_type = None
    # Lists for player exclusive attributes
    # Lists for person exclusive attributes
    # Lists for business exclusive attributes
    # Lists for other Objects attributes



    frame: # A main frame that all child elements position themselves after, covers the whole screen.
        background None
        yfill True
        xfill True
        if main_screen_showing:
            frame:
                yalign 0.5
                xysize (260,250)
                hbox:
                    vbox:
                        for x in editable_characters:
                            textbutton x.name:
                                xfill True

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
                grid 4 1:
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
                                        if hasattr(editing_target, x):
                                            button:
                                                id "name_select"
                                                margin [2,2]
                                                xfill True
                                                background "#000080"

                                                action [ToggleScreenVariable("name_select"), SetScreenVariable("name_type", x)]

                                                if name_select:
                                                    input default vars(editing_target)[x]:
                                                        changed edit_name_func
                                                        style "serum_text_style"
                                                        yalign 0.5
                                                else:
                                                    text x + ": "+ vars(editing_target)[x]:
                                                        yalign 0.5
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
                                        if hasattr(editing_target, x):
                                            textbutton x + ": " + str(vars(editing_target)[x]):
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"

                                                action [
                                                    Function(setattr, editing_target, x, vars(editing_target)[x] + 1)
                                                ]

                                                alternate [
                                                    Function(setattr, editing_target, x, vars(editing_target)[x] - 1)
                                                ]

                    vbox:
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
                                        if hasattr(editing_target, x):
                                            textbutton x + ": " + str(vars(editing_target)[x]):
                                                xfill True
                                                style "textbutton_no_padding_highlight"
                                                text_style "serum_text_style"

                                                action [
                                                    Function(setattr, editing_target, x, vars(editing_target)[x] + 1)
                                                ]

                                                alternate [
                                                    Function(setattr, editing_target, x, vars(editing_target)[x] - 1)
                                                ]
                    vbox:
                        textbutton "Sex Skills":
                            style "textbutton_no_padding_highlight"
                            text_style "serum_text_style"
                            xfill True

                            action ToggleScreenVariable("sex_skills_options")
                        if sex_skills_options:
                            viewport:
                                mousewheel True
                                draggable True
                                vbox:
                                    for x in sex_skills:
                                        if hasattr(editing_target, "sex_skills"):
                                            if x in editing_target.sex_skills:
                                                textbutton x + ": " + str(vars(editing_target)["sex_skills"][x]):
                                                    xfill True
                                                    style "textbutton_no_padding_highlight"
                                                    text_style "serum_text_style"

                                                    action [
                                                        SetDict(vars(editing_target)["sex_skills"], x, vars(editing_target)["sex_skills"][x] + 1)
                                                    ]

                                                    alternate [
                                                        SetDict(vars(editing_target)["sex_skills"], x, vars(editing_target)["sex_skills"][x] - 1)
                                                    ]
