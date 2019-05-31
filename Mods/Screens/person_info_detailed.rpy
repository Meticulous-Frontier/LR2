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
                vbox:
                    xalign 0.5 xanchor 0.5
                    text "[the_person.name] [the_person.last_name]" style "menu_text_style" size 30 xalign 0.5 yalign 0.5 yanchor 0.5 color the_person.char.who_args["color"] font the_person.char.what_args["font"]
                    if not mc.business.get_employee_title(the_person) == "None":
                        text "Position: " + mc.business.get_employee_title(the_person) + " ($[the_person.salary]/day)" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                    python:
                        role_string = "Special Roles: "
                        if the_person.special_role: # NOTE: This is a temporary workaround to prevent errors due to NoneType Role Name. Will not scale.
                            first = True
                            for role in the_person.special_role:
                                if not role.role_name in [generic_people_role.role_name]: # Hide generic role
                                    if not first:
                                        role_string += ", "
                                    role_string += role.role_name
                                    first = False

                    text role_string style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5
            hbox:
                xsize 1750
                xalign 0.5
                xanchor 0.5
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 250
                    vbox:
                        text "Main Stats" style "menu_text_style" size 22
                        text "Charisma: [the_person.charisma]" style "menu_text_style"
                        text "Intelligence: [the_person.int]" style "menu_text_style"
                        text "Focus: [the_person.focus]" style "menu_text_style"
                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 250
                    vbox:
                        text "Work Skills" style "menu_text_style" size 22
                        text "HR Skill: [the_person.hr_skill]" style "menu_text_style"
                        text "Marketing Skill: [the_person.market_skill]" style "menu_text_style"
                        text "Researching Skill: [the_person.research_skill]" style "menu_text_style"
                        text "Production Skill: [the_person.production_skill]" style "menu_text_style"
                        text "Supply Skill: [the_person.supply_skill]" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 250
                    vbox:
                        text "Sex Skills" style "menu_text_style" size 22
                        text "Foreplay Skill: " + str(the_person.sex_skills["Foreplay"]) style "menu_text_style"
                        text "Oral Skill: " + str(the_person.sex_skills["Oral"]) style "menu_text_style"
                        text "Vaginal Skill: " + str(the_person.sex_skills["Vaginal"]) style "menu_text_style"
                        text "Anal: " + str(the_person.sex_skills["Anal"]) style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 250
                    vbox:
                        text "Current Status" style "menu_text_style" size 22
                        text "Happiness: [the_person.happiness]" style "menu_text_style"
                        text "Suggestibility: [the_person.suggestibility]" style "menu_text_style"
                        text "Sluttiness: [the_person.sluttiness]" style "menu_text_style"
                        text "Obedience: [the_person.obedience] - " + get_obedience_plaintext(the_person.obedience) style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 325
                    ysize 250
                    vbox:
                        text "Currently Affected By:" style "menu_text_style" size 22
                        if not the_person.serum_effects:
                            text "No active serums." style "menu_text_style"

                        for serum in the_person.serum_effects:
                            text serum.name + " : " + str(serum.duration - serum.duration_counter) + " Turns Left" style "menu_text_style"
                        null height 20


            hbox:
                xsize 1750
                spacing 30
                $ master_opinion_dict = dict(the_person.opinions, **the_person.sexy_opinions)
                frame:
                    background "#1a45a1aa"
                    xsize 415
                    ysize 400
                    vbox:
                        text "Loves" style "menu_text_style" size 22
                        for opinion in master_opinion_dict:
                            if master_opinion_dict[opinion][0] == 2:
                                if master_opinion_dict[opinion][1]:
                                    text "   " + opinion.title() style "menu_text_style"
                                else:
                                    text "   ????" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 415
                    ysize 400
                    vbox:
                        text "Likes" style "menu_text_style" size 22
                        for opinion in master_opinion_dict:
                            if master_opinion_dict[opinion][0] == 1:
                                if master_opinion_dict[opinion][1]:
                                    text "   " + opinion.title() style "menu_text_style"
                                else:
                                    text "   ????" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 415
                    ysize 400
                    vbox:
                        text "Dislikes" style "menu_text_style" size 22
                        for opinion in master_opinion_dict:
                            if master_opinion_dict[opinion][0] == -1:
                                if master_opinion_dict[opinion][1]:
                                    text "   " + opinion.title() style "menu_text_style"
                                else:
                                    text "   ????" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 415
                    ysize 400
                    vbox:
                        text "Hates" style "menu_text_style" size 22
                        for opinion in master_opinion_dict:
                            if master_opinion_dict[opinion][0] == -2:
                                if master_opinion_dict[opinion][1]:
                                    text "   " + opinion.title() style "menu_text_style"
                                else:
                                    text "   ????" style "menu_text_style"

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action Hide("person_info_detailed")
            textbutton "Return" align [0.5,0.5] style "return_button_style"
