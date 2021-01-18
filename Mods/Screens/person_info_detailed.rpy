init 2: # Need to allow for None name roles in this screen as well.
    screen person_info_detailed(the_person):
        add "Paper_Background.png"
        modal True
        zorder 100
        default hr_base = the_person.charisma*3 + the_person.hr_skill*2 + the_person.int + 10
        default market_base = the_person.charisma*3 + the_person.market_skill*2 + the_person.focus + 10
        default research_base = the_person.int*3 + the_person.research_skill*2 + the_person.focus + 10
        default prod_base = the_person.focus*3 + the_person.production_skill*2 + the_person.int + 10
        default supply_base = the_person.focus*3 + the_person.supply_skill*2 + the_person.charisma + 10
        default dict_work_skills = get_work_skills()
        default dict_sex_skills = get_sex_skills()
        default dict_main_skills = get_main_skills()
        default master_opinion_dict = dict(the_person.opinions, **the_person.sexy_opinions)

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
                    vbox:
                        xsize (1100 if persistent.pregnancy_pref > 0 else 1700)
                        xalign 0.5 xanchor 0.5
                        text "[the_person.name] [the_person.last_name]" style "menu_text_style" size 30 xalign 0.5 yalign 0.5 yanchor 0.5 color the_person.char.who_args["color"] font the_person.char.what_args["font"]
                        if not mc.business.get_employee_title(the_person) == "None":
                            text "Position: " + mc.business.get_employee_title(the_person) + " ($[the_person.salary]/day)" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5
                        if get_strip_club_foreclosed_stage() >= 5 and the_person.has_role([stripper_role, waitress_role, bdsm_performer_role, manager_role, mistress_role]):
                            text "Position: " + strip_club_get_job_title(the_person) + " ($[the_person.salary]/day)" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                        $ visible_roles = []
                        $ role_string = "Special Roles: "
                        python:
                            for role in [x for x in the_person.special_role if not x.hidden]:
                                visible_roles.append(role.role_name)

                        if visible_roles:
                            $ role_string += ", ".join(visible_roles)
                            text role_string style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                    if isinstance(the_person, Person) and persistent.pregnancy_pref > 0:
                        vbox:
                            xsize 350
                            if the_person.knows_pregnant():
                                text "Pregnant: Yes" style "menu_text_style"
                                if day < the_person.pregnancy_show_day():
                                    text "- Visible Day: " + str(the_person.pregnancy_show_day()) style "menu_text_style"
                                elif day < the_person.get_due_day():
                                    text "- Delivery Day: " + str(the_person.get_due_day()) style "menu_text_style"
                            else:
                                if persistent.pregnancy_pref == 1:
                                    text "Fertility: " + str(__builtin__.round(the_person.fertility_percent, 1)) + "%" style "menu_text_style"
                                if persistent.pregnancy_pref == 2:
                                    $ modified_fertility = the_person.calculate_realistic_fertility()
                                    $ named_chance = the_person.pregnancy_chance_string()
                                    text "Fertility: " + str(__builtin__.round(modified_fertility, 1)) + "% -> " + named_chance style "menu_text_style"
                                    text "Monthly Peak Day: " + str(the_person.ideal_fertile_day) style "menu_text_style"

                        vbox:
                            xsize 350
                            if the_person.knows_pregnant:
                                text "Birth Control: No" style "menu_text_style"
                            elif the_person.event_triggers_dict.get("birth_control_status", None) is None:
                                text "Birth Control: Unknown" style "menu_text_style"
                            else:
                                hbox:
                                    text "Birth Control:" style "menu_text_style"
                                    vbox:
                                        text ("Yes" if the_person.on_birth_control else "No") style "menu_text_style"
                                        text "Known " + str(day - the_person.event_triggers_dict.get("birth_control_known_day", 0)) + " days ago" size 12 style "menu_text_style"

            hbox:
                xsize 1750
                xalign 0.5
                xanchor 0.5
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 260
                    vbox:
                        text "Status and Info" style "menu_text_style" size 22
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 300
                                background None
                                vbox:
                                    text "Happiness: [the_person.happiness]" style "menu_text_style"
                                    text "Sluttiness: [the_person.sluttiness] (Core: [the_person.core_sluttiness])" style "menu_text_style"
                                    text "Obedience: [the_person.obedience] - " + get_obedience_plaintext(the_person.obedience) style "menu_text_style"
                                    text "Age: [the_person.age]" style "menu_text_style"
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
                    ysize 260
                    vbox:
                        text "Characteristics" style "menu_text_style" size 22
                        for skill in dict_main_skills:
                            text dict_main_skills[skill][0] + ": " + str(getattr(the_person, dict_main_skills[skill][1])) style "menu_text_style"
                        text "Love: [the_person.love]" style "menu_text_style"
                        if the_person not in unique_character_list:
                            text "Personality: " + the_person.personality.personality_type_prefix.capitalize() style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 260
                    vbox:
                        text "Work Skills" style "menu_text_style" size 22
                        for skill in dict_work_skills:
                            text dict_work_skills[skill][0] + ": " + str(getattr(the_person, dict_work_skills[skill][1])) style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 260
                    vbox:
                        text "Sex Skills" style "menu_text_style" size 22
                        for skill in dict_sex_skills:
                            text dict_sex_skills[skill][0] + " Skill: " + str(the_person.sex_skills[dict_sex_skills[skill][0]]) style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 260
                    vbox:
                        text "Sex Record" style "menu_text_style" size 22
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 300
                                background None
                                vbox:
                                    for record in sorted(the_person.sex_record):
                                        text record + ": " + str(the_person.sex_record[record]) style "menu_text_style"

            hbox:
                xsize 1750
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Loves" style "menu_text_style" size 22
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 315
                                background None
                                vbox:
                                    for opinion in sorted(master_opinion_dict):
                                        if master_opinion_dict[opinion][0] == 2:
                                            if master_opinion_dict[opinion][1]:
                                                text "   " + opinion.title() style "menu_text_style"
                                            else:
                                                text "   ????" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Likes" style "menu_text_style" size 22
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 315
                                background None
                                vbox:
                                    for opinion in sorted(master_opinion_dict):
                                        if master_opinion_dict[opinion][0] == 1:
                                            if master_opinion_dict[opinion][1]:
                                                text "   " + opinion.title() style "menu_text_style"
                                            else:
                                                text "   ????" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Dislikes" style "menu_text_style" size 22
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 315
                                background None
                                vbox:
                                    for opinion in sorted(master_opinion_dict):
                                        if master_opinion_dict[opinion][0] == -1:
                                            if master_opinion_dict[opinion][1]:
                                                text "   " + opinion.title() style "menu_text_style"
                                            else:
                                                text "   ????" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Hates" style "menu_text_style" size 22
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 315
                                background None
                                vbox:
                                    for opinion in sorted(master_opinion_dict):
                                        if master_opinion_dict[opinion][0] == -2:
                                            if master_opinion_dict[opinion][1]:
                                                text "   " + opinion.title() style "menu_text_style"
                                            else:
                                                text "   ????" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 400
                    vbox:
                        text "Other Relations" style "menu_text_style" size 22
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 315
                                background None
                                vbox:
                                    for relationship in sorted(town_relationships.get_relationship_type_list(the_person, visible = True), key = lambda x: x[0].name):
                                        text "   " + relationship[0].name + " " + relationship[0].last_name + " [[" + relationship[1] + "]" size 14 style "menu_text_style"

            hbox:
                xsize 1750
                xalign 0.5
                xanchor 0.5
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 165
                    vbox:
                        text "HR Job: [hr_base]" style "menu_text_style"
                        text "Marketing Job: [market_base]" style "menu_text_style"
                        text "Research Job: [research_base]" style "menu_text_style"
                        text "Production Job: [prod_base]" style "menu_text_style"
                        text "Supply Job: [supply_base]" style "menu_text_style"
                frame:
                    background None
                    anchor [0.5,1]
                    align [0.5,0]
                    xysize [500,125]
                    xoffset 10
                    yoffset 30
                    imagebutton:
                        align [0.5,0.5]
                        auto "gui/button/choice_%s_background.png"
                        focus_mask "gui/button/choice_idle_background.png"
                        action Hide("person_info_detailed")
                    textbutton "Return" align [0.5,0.5] style "return_button_style"
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 165
                    xoffset 195
                    vbox:
                        text "Currently Affected By:" style "menu_text_style" size 22
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            frame:
                                xsize 300
                                background None
                                vbox:
                                    if not the_person.serum_effects:
                                        text "No active serums." style "menu_text_style"
                                    else:
                                        text "Suggestibility: [the_person.suggestibility]" style "menu_text_style"
                                        for serum in the_person.serum_effects:
                                            text serum.name + " : " + str(serum.duration - serum.duration_counter) + " Turns Left" style "menu_text_style"
