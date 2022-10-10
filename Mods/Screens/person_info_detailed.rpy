init 2: # Need to allow for None name roles in this screen as well.
    python:
        def info_detail_visible_roles(person):
            visible_roles = []
            for role in [x for x in person.special_role if not x.hidden]:
                visible_roles.append(role.role_name)
            return visible_roles

    screen person_info_detailed(the_person):
        add "Paper_Background.png"
        modal True
        zorder 100

        default hr_base = the_person.charisma*3 + the_person.hr_skill*2 + the_person.int + 10
        default market_base = (the_person.charisma*3 + the_person.market_skill*2 + the_person.focus + 10) * 5
        default research_base = the_person.int*3 + the_person.research_skill*2 + the_person.focus + 10
        default prod_base = the_person.focus*3 + the_person.production_skill*2 + the_person.int + 10
        default supply_base = the_person.focus*5 + the_person.supply_skill*3 + the_person.charisma*3 + 20
        default master_opinion_dict = dict(the_person.opinions, **the_person.sexy_opinions)
        default relationship_list = sorted(town_relationships.get_relationship_type_list(the_person, visible = True), key = lambda x: x[0].name)
        default visible_roles = ", ".join(info_detail_visible_roles(the_person))
        default person_portrait = the_person.build_person_portrait()
        default person_job_info = person_info_ui_get_job_title(the_person)
        default fertility_info1 = str(__builtin__.round(the_person.fertility_percent, 1)) + "%"
        default fertility_info2 = str(__builtin__.round(the_person.calculate_realistic_fertility(), 1)) + "% -> " + the_person.pregnancy_chance_string()
        default fertility_peak_day = str(the_person.ideal_fertile_day + 1)
        default known_days = str(day - the_person.event_triggers_dict.get("birth_control_known_day", 0))
        default obedience_info = get_obedience_plaintext(the_person.obedience)
        default personality_info = the_person.personality.base_personality_prefix.capitalize()
        default novelty_info = str(the_person.novelty)
        default height_info = height_to_string(the_person.height)
        if isinstance(the_person.hair_colour, list) and isinstance(the_person.hair_colour[0], basestring):
            default hair_info = the_person.hair_colour[0].title()
        else:
            default hair_info = ""
        if isinstance(the_person.eyes, list) and isinstance(the_person.eyes[0], basestring):
            default eyes_info = the_person.eyes[0].title()
        else:
            default eyes_info = ""
        default desired_salary = the_person.calculate_base_salary()

        vbox:
            spacing 25
            xalign 0.5
            xanchor 0.5
            yalign 0.2
            frame:
                xsize 1750
                ysize 120
                xalign 0.5
                background "#1a45a1aa"
                hbox:
                    imagebutton:
                        idle person_portrait at zoom(.7)
                        xoffset -50
                        yoffset -24
                        xsize 100
                    vbox:
                        xsize (1050 if persistent.pregnancy_pref > 0 else 1650)
                        xalign 0.5 xanchor 0.5
                        text format_titles(the_person) style "menu_text_style" size 30 xalign 0.5 yalign 0.5 yanchor 0.5 color the_person.char.who_args["color"] font the_person.char.what_args["font"]
                        text "Job: [person_job_info]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                        if visible_roles:
                            text "Special Roles: [visible_roles]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                    if isinstance(the_person, Person) and persistent.pregnancy_pref > 0:
                        vbox:
                            xsize 350
                            if the_person.knows_pregnant():
                                text "Pregnant: Yes" style "menu_text_style"
                                if day < the_person.pregnancy_show_day():
                                    text "- Visible Day: " + str(the_person.pregnancy_show_day()) style "menu_text_style"
                                elif day < the_person.get_due_day():
                                    text "- Delivery Day: " + str(the_person.get_due_day()) style "menu_text_style"
                            elif the_person.has_role(clone_role):
                                text "Pregnant: Sterile" style "menu_text_style"
                            else:
                                if persistent.pregnancy_pref == 1:
                                    text "Fertility: [fertility_info1]" style "menu_text_style"
                                if persistent.pregnancy_pref == 2:
                                    text "Fertility: [fertility_info2]" style "menu_text_style"
                                    text "Monthly Peak Day: [fertility_peak_day]" style "menu_text_style"

                        vbox:
                            xsize 350
                            if the_person.has_role(clone_role):
                                pass
                            elif the_person.knows_pregnant():
                                text "Birth Control: No" style "menu_text_style"
                            elif the_person.event_triggers_dict.get("birth_control_status", None) is None:
                                text "Birth Control: Unknown" style "menu_text_style"
                            else:
                                hbox:
                                    text "Birth Control:" style "menu_text_style"
                                    vbox:
                                        text ("Yes" if the_person.on_birth_control else "No") style "menu_text_style"
                                        text "Known [known_days] days ago" size 12 style "menu_text_style"
                            use serum_tolerance_indicator(the_person)

            hbox:
                xsize 1750
                xalign 0.5
                xanchor 0.5
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 264
                    vbox:
                        text "Status and Info" style "serum_text_style_header"
                        text "Happiness: [the_person.happiness]" style "menu_text_style"
                        text "Sluttiness: [the_person.sluttiness]%" style "menu_text_style"
                        text "Obedience: [the_person.obedience] {image=triskelion_token_small} [obedience_info]" style "menu_text_style"
                        text "Love: [the_person.love]" style "menu_text_style"
                        text "Personality: [personality_info]" style "menu_text_style"
                        if the_person.has_role(girlfriend_role):
                            text "Relationship: Girlfriend" style "menu_text_style"
                        else:
                            text "Relationship: [the_person.relationship]" style "menu_text_style"
                        if the_person.relationship != "Single":
                            text "Significant Other: [the_person.SO_name]" style "menu_text_style"
                        elif the_person.has_role(girlfriend_role):
                            text "Significant Other: [mc.name]" style "menu_text_style"
                        if the_person.kids > 0:
                            text "Kids: [the_person.kids]" style "menu_text_style"
                        if the_person.only_normal_employee():
                            text "Salary: $[the_person.salary]/day" style "menu_text_style"
                        if  the_person.is_strip_club_employee():
                            text "Club Salary: $[the_person.stripper_salary]/day" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 264
                    vbox:
                        text "Characteristics" style "serum_text_style_header"
                        text "Intelligence: [the_person.int]" style "menu_text_style"
                        text "Focus: [the_person.focus]" style "menu_text_style"
                        text "Charisma: [the_person.charisma]" style "menu_text_style"
                        text "Age: [the_person.age]" style "menu_text_style"
                        text "Cup size: [the_person.tits]" style "menu_text_style"
                        text "Height: [height_info]" style "menu_text_style"
                        text "Hair: [hair_info]" style "menu_text_style"
                        text "Eyes: [eyes_info]" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 264
                    vbox:
                        text "Work Skills" style "serum_text_style_header"
                        text "Human Resources: [the_person.hr_skill]" style "menu_text_style"
                        text "Marketing: [the_person.market_skill]" style "menu_text_style"
                        text "Research & Development: [the_person.research_skill]" style "menu_text_style"
                        text "Production: [the_person.production_skill]" style "menu_text_style"
                        text "Supply Procurement: [the_person.supply_skill]" style "menu_text_style"
                        text "Work Experience Level: [the_person.work_experience]" style "menu_text_style"
                        if the_person.has_role(employee_role) or the_person.has_role("College Intern"):
                            textbutton "Review Duties: " + str(len(the_person.duties)) + "/" + str(the_person.work_experience):
                                style "textbutton_style"
                                text_style "menu_text_style"
                                action Show("set_duties_screen", the_person = the_person, allow_changing_duties = False, show_available_duties = True, hide_on_exit = True)

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 264
                    vbox:
                        text "Sex Skills" style "serum_text_style_header"
                        text "Foreplay Skill: {}".format(the_person.sex_skills["Foreplay"]) style "menu_text_style"
                        text "Oral Skill: {}".format(the_person.sex_skills["Oral"]) style "menu_text_style"
                        text "Vaginal Skill: {}".format(the_person.sex_skills["Vaginal"]) style "menu_text_style"
                        text "Anal Skill: {}".format(the_person.sex_skills["Anal"]) style "menu_text_style"
                        text "Novelty: [novelty_info]%" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 264
                    vbox:
                        text "Sex Record" style "serum_text_style_header"
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                for record in sorted(the_person.sex_record.keys()):
                                    text "[record]: " + str(the_person.sex_record[record]) style "menu_text_style"

            hbox:
                xsize 1750
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Loves" style "serum_text_style_header"
                        use opinion_list(master_opinion_dict, 2)

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Likes" style "serum_text_style_header"
                        use opinion_list(master_opinion_dict, 1)

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Dislikes" style "serum_text_style_header"
                        use opinion_list(master_opinion_dict, -1)

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Hates" style "serum_text_style_header"
                        use opinion_list(master_opinion_dict, -2)

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Other Relations" style "serum_text_style_header"
                        if len(relationship_list) > 10:
                            viewport:
                                scrollbars "vertical"
                                draggable False
                                mousewheel True
                                vbox:
                                    for relationship in relationship_list:
                                        text "   [relationship[0].name] [relationship[0].last_name] [[[relationship[1]]]" size 14 style "menu_text_style"
                        else:
                            for relationship in relationship_list:
                                text "   [relationship[0].name] [relationship[0].last_name] [[[relationship[1]]]" size 14 style "menu_text_style"

            hbox:
                xsize 1750
                xalign 0.5
                xanchor 0.5
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 185
                    vbox:
                        text "Job Statistics" style "serum_text_style_header"
                        text "HR: [hr_base]% Company Efficiency" style "menu_text_style"
                        text "Marketing: [market_base] Market Reach" style "menu_text_style"
                        text "Research: [research_base] Research Points" style "menu_text_style"
                        text "Production: [prod_base] Production Points" style "menu_text_style"
                        text "Supply: [supply_base] Supply Units" style "menu_text_style"
                        if the_person.only_normal_employee():
                            text "Desired Salary: $[desired_salary]/day" style "menu_text_style"

                frame:
                    background None
                    anchor [0.5,1]
                    align [0.5,0]
                    xysize [1000,125]
                    xoffset 10
                    yoffset 30
                    imagebutton:
                        align [0.0,0.5]
                        auto "gui/button/choice_%s_background.png"
                        focus_mask "gui/button/choice_idle_background.png"
                        action Hide("person_info_detailed")
                    textbutton "Return" align [0.17,0.5] style "return_button_style"

                    if the_person.has_story_dict():
                        imagebutton:
                            align [1.0,0.5]
                            auto "gui/button/choice_%s_background.png"
                            focus_mask "gui/button/choice_idle_background.png"
                            action [
                                Show("story_progress", person = the_person),
                                Function(draw_mannequin, the_person, the_person.outfit)
                            ]
                        textbutton "Story Progress" align [0.87,0.5] style "return_button_style"
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 185
                    xoffset 30
                    vbox:
                        text "Currently Affected By" style "serum_text_style_header"
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                text "Suggestibility: [the_person.suggestibility]%" style "menu_text_style"
                                if not the_person.serum_effects:
                                    text "No active serums" style "menu_text_style"
                                else:
                                    for serum in the_person.serum_effects:
                                        text "[serum.name]: " + str(serum.duration - serum.duration_counter) + " Turns Left" style "menu_text_style"

screen opinion_list(opinion_dict, preference):
    if len([x for x in opinion_dict if opinion_dict[x][0] == preference]) > 10:
        viewport:
            scrollbars "vertical"
            draggable False
            mousewheel True
            vbox:
                use opinion_list_values(opinion_dict, preference)

    else:
        use opinion_list_values(opinion_dict, preference)

screen opinion_list_values(opinion_dict, preference):
    for opinion in sorted(opinion_dict):
        if opinion_dict[opinion][0] == preference:
            if opinion_dict[opinion][1]:
                text "   " + opinion.title() style "menu_text_style"
            else:
                text "   ????" style "menu_text_style"
