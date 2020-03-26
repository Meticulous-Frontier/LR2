init 2:
    screen employee_overview(white_list = None, black_list = None, person_select = False): #If select is True it returns the person's name who you click on. If it is false it is a normal overview menu that lets you bring up their detailed info.
        modal True
        zorder 100
        add "Paper_Background.png"
        default division_select = "none"
        default division_name = "All"
        default sort_employees_by = "name"
        default reverse_sort = True
        default sort_attributes = [
            ["Name", "name"],
            ["Salary", "salary"],
            ["Happiness", "happiness"],
            ["Obedience", "obedience"],
            ["Love", "love"],
            ["Sluttiness", "sluttiness"],
            ["Suggest", "suggestibility"],
            ["Charisma", "charisma"],
            ["Intelligence", "int"],
            ["Focus", "focus"],
            ["Research", "research_skill"],
            ["Production", "production_skill"],
            ["Supply", "supply_skill"],
            ["Marketing", "market_skill"],
            ["HR", "hr_skill"]
            ]


        python:
            if not white_list: #If a white list is passed we will only display people that are on the list
                white_list = []
            if not black_list:
                black_list = [] #IF a black list is passed we will not include anyone on the blacklist. Blacklist takes priority


        $ showing_team = []
        $ display_list = []
        $ valid_person_count = 0

        python:
            if division_select == "none":
                showing_team = [] + mc.business.research_team + mc.business.production_team + mc.business.supply_team + mc.business.market_team + mc.business.hr_team
                division_name = "Everyone"
            elif division_select == "r":
                showing_team = mc.business.research_team #ie. take a shallow copy, so we can modify the team without everything exploding.
                division_name = "Research"
            elif division_select == "p":
                showing_team = mc.business.production_team
                division_name = "Production"
            elif division_select == "s":
                showing_team = mc.business.supply_team
                division_name = "Supply Procurement"
            elif division_select == "m":
                showing_team = mc.business.market_team
                division_name = "Marketing"
            elif division_select == "h":
                showing_team = mc.business.hr_team
                division_name = "Human Resources"

            display_list = [person for person in showing_team if (not white_list or person in white_list) and (not black_list or person not in black_list)] #Create our actual display list using people who are either on the white list or not on the black list

        vbox:
            xalign 0.5
            xanchor 0.5
            yalign 0.05
            yanchor 0.0
            spacing 20
            xsize 1860
            frame:
                background "#1a45a1aa"
                xsize 1860
                ysize 60
                if person_select:
                    text "Staff Selection" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_style"
                else:
                    text "Staff Review" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_style"
            frame:
                background "#1a45a1aa"

                hbox:
                    xalign 0.5
                    xanchor 0.5
                    spacing 40
                    $ button_mappings = [["All","none"],["Research","r"],["Production","p"],["Supply","s"],["Marketing","m"],["Human Resources","h"]]
                    for button_map in button_mappings:
                        frame:
                            ysize 60
                            if division_select == button_map[1]:
                                background "#4f7ad6"
                            else:
                                background "#1a45a1"
                            button:
                                action SetScreenVariable("division_select", button_map[1])
                                xsize 200
                                ysize 40
                                text button_map[0] xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 style "textbutton_text_style"

            $ grid_count = 15
            if person_select:
                $ grid_count += 1
            frame:

                yanchor 0.0
                background "#1a45a1aa"
                grid grid_count 1 ysize 30 spacing 10 xfill True:
                    if person_select:
                        text "" style "menu_text_style" xsize 130
                    for attributes in sort_attributes:
                        textbutton attributes[0]:
                            style "textbutton_no_padding_highlight"
                            text_style "textbutton_text_style"
                            xfill True
                            action [
                                SetScreenVariable("sort_employees_by", attributes[1]),
                                ToggleScreenVariable("reverse_sort")
                                ]
                    # textbutton "Name"
                    # textbutton "Salary" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "salary"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Happiness" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "happiness"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Obedience" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "obedience"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Love" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "love"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Sluttiness" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "sluttiness"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Suggest" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "suggestibility"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Charisma" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "charisma"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Int" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "int"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Focus" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "focus"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Research" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "research_skill"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Production " style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "production_skill"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Supply" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "supply_skill"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "Marketing " style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "market_skill"), ToggleScreenVariable("reverse_sort")]
                    # textbutton "HR" style "textbutton_no_padding_highlight" text_style "textbutton_text_style" xsize 120 action [SetScreenVariable("sort_employees_by", "hr_skill"), ToggleScreenVariable("reverse_sort")]

            # text "Position: " + division_name style "menu_text_style" size 24 yalign 0.18 xalign 0.02 xanchor 0.0
            frame:
                ypos -20
                yanchor 0.0
                background "#1a45a1aa"
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    ysize 680
                    grid grid_count len(display_list) spacing 10 xfill True:
                        for person in sorted(display_list, key = lambda person: getattr(person, renpy.current_screen().scope["sort_employees_by"]), reverse = renpy.current_screen().scope["reverse_sort"]):
                            if person_select:
                                textbutton "Select" style "textbutton_style" text_style "menu_text_style" action Return(person) xsize 90 yalign 0.5
                            textbutton person.name + "\n" + person.last_name style "textbutton_style" text_style "menu_text_style" action Show("person_info_detailed",None,person) xsize 120
                            for attributes in sort_attributes[1:]: #Omit name
                                text (str(getattr(person, attributes[1])) if attributes[1] != "salary" else "$" + str(getattr(person, attributes[1])) +"/day") style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5

                            # text "$" + str(person.salary) + "/day"
                            # text str(int(person.happiness)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.obedience)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.love)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.sluttiness)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.suggestibility)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.charisma)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.int)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.focus)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.research_skill)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.production_skill)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.supply_skill)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.market_skill)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5
                            # text str(int(person.hr_skill)) style "menu_text_style" xsize 120 yalign 0.5 xalign 0.5

        if not person_select:
            frame:
                background None
                anchor [0.5,0.5]
                align [0.5,0.94]
                xysize [400,80]
                imagebutton:
                    align [0.5,0.5]
                    idle im.Scale("gui/button/choice_idle_background.png", 400, 80)
                    hover im.Scale("gui/button/choice_hover_background.png", 400, 80)
                    focus_mask im.Scale("gui/button/choice_idle_background.png", 400, 80)
                    action Hide("employee_overview")
                textbutton "Return" align [0.5,0.5] style "return_button_style"
