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
        default market_base = the_person.charisma*3 + the_person.market_skill*2 + the_person.focus + 10
        default research_base = the_person.int*3 + the_person.research_skill*2 + the_person.focus + 10
        default prod_base = the_person.focus*3 + the_person.production_skill*2 + the_person.int + 10
        default supply_base = the_person.focus*5 + the_person.supply_skill*3 + the_person.charisma*3 + 20
        default dict_work_skills = get_work_skills()
        default dict_sex_skills = get_sex_skills()
        default dict_main_skills = get_main_skills()
        default master_opinion_dict = dict(the_person.opinions, **the_person.sexy_opinions)
        default relationship_list = sorted(town_relationships.get_relationship_type_list(the_person, visible = True), key = lambda x: x[0].name)
        default visible_roles = info_detail_visible_roles(the_person)

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
                        idle the_person.build_person_portrait() at zoom(.7)
                        xoffset -50
                        yoffset -24
                        xsize 100
                    vbox:
                        xsize (1050 if persistent.pregnancy_pref > 0 else 1650)
                        xalign 0.5 xanchor 0.5
                        text "[the_person.name] [the_person.last_name]" style "menu_text_style" size 30 xalign 0.5 yalign 0.5 yanchor 0.5 color the_person.char.who_args["color"] font the_person.char.what_args["font"]
                        if not mc.business.get_employee_title(the_person) == "None":
                            text "Position: " + mc.business.get_employee_title(the_person) + " ($[the_person.salary]/day)" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5
                        if get_strip_club_foreclosed_stage() >= 5 and the_person.has_role([stripper_role, waitress_role, bdsm_performer_role, manager_role, mistress_role]):
                            text "Position: " + strip_club_get_job_title(the_person) + " ($[the_person.stripper_salary]/day)" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                        if visible_roles:
                            text "Special Roles: " + ", ".join(visible_roles) style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

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
                                    text "Fertility: " + str(__builtin__.round(the_person.fertility_percent, 1)) + "%" style "menu_text_style"
                                if persistent.pregnancy_pref == 2:
                                    $ modified_fertility = the_person.calculate_realistic_fertility()
                                    $ named_chance = the_person.pregnancy_chance_string()
                                    text "Fertility: " + str(__builtin__.round(modified_fertility, 1)) + "% -> " + named_chance style "menu_text_style"
                                    text "Monthly Peak Day: " + str(the_person.ideal_fertile_day + 1) style "menu_text_style"

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
                                        text "Known " + str(day - the_person.event_triggers_dict.get("birth_control_known_day", 0)) + " days ago" size 12 style "menu_text_style"
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
                        text "Sluttiness: [the_person.sluttiness]" style "menu_text_style"
                        text "Obedience: [the_person.obedience] - " + get_obedience_plaintext(the_person.obedience) style "menu_text_style"
                        text "Love: [the_person.love]" style "menu_text_style"
                        text "Personality: " + the_person.personality.base_personality_prefix.capitalize() style "menu_text_style"
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


                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 264
                    vbox:
                        text "Characteristics" style "serum_text_style_header"
                        for skill in dict_main_skills:
                            text dict_main_skills[skill][0] + ": " + str(getattr(the_person, dict_main_skills[skill][1])) style "menu_text_style"
                        text "Age: [the_person.age]" style "menu_text_style"
                        text "Cup size: [the_person.tits]" style "menu_text_style"
                        text "Height: " + height_to_string(the_person.height) style "menu_text_style"
                        text "Hair: " + the_person.hair_colour[0].title() style "menu_text_style"
                        text "Eyes: " + the_person.eyes[0].title() style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 264
                    vbox:
                        text "Work Skills" style "serum_text_style_header"
                        for skill in dict_work_skills:
                            text dict_work_skills[skill][0] + ": " + str(getattr(the_person, dict_work_skills[skill][1])) style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 264
                    vbox:
                        text "Sex Skills" style "serum_text_style_header"
                        for skill in dict_sex_skills:
                            text dict_sex_skills[skill][0] + " Skill: " + str(the_person.sex_skills[dict_sex_skills[skill][0]]) style "menu_text_style"
                        text "Novelty: " + str(the_person.novelty) + "%" style "menu_text_style"

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
                                    text record + ": " + str(the_person.sex_record[record]) style "menu_text_style"

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
                                        text "   " + relationship[0].name + " " + relationship[0].last_name + " [[" + relationship[1] + "]" size 14 style "menu_text_style"
                        else:
                            for relationship in relationship_list:
                                text "   " + relationship[0].name + " " + relationship[0].last_name + " [[" + relationship[1] + "]" size 14 style "menu_text_style"

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
                        text "HR Job: [hr_base]" style "menu_text_style"
                        text "Marketing Job: [market_base]" style "menu_text_style"
                        text "Research Job: [research_base]" style "menu_text_style"
                        text "Production Job: [prod_base]" style "menu_text_style"
                        text "Supply Job: [supply_base]" style "menu_text_style"
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
                                Function(the_person.draw_person, draw_layer="8", wipe_scene = False),
                                Show("story_progress", person = the_person)
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
                                        text serum.name + " : " + str(serum.duration - serum.duration_counter) + " Turns Left" style "menu_text_style"

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
