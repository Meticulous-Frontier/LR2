init 2:
    screen story_progress(the_person, story_dict):
        # show_candidate(the_person)
        add "Paper_Background.png"
        modal True
        zorder 100
        if the_person.draw_person():
            pass
        vbox:
            yalign 0.2
            xalign 0.4
            xanchor 0.5
            spacing 30
            frame:
                background "#1a45a1aa"
                ysize 80
                xsize 1320
                xalign 0.5
                xanchor 0.5
                text "[the_person.name] [the_person.last_name]" style "menu_text_style" size 50 xanchor 0.5 xalign 0.5 color the_person.char.who_args["color"] font the_person.char.what_args["font"]
                text story_dict.get("description", "") style "menu_text_style" size 16 xanchor 0.5 xalign 0.5 yalign 1.0
            hbox:
                xsize 1320
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 420
                    ysize 550
                    vbox:
                        text "Personal Information" style "menu_text_style" size 26 xalign 0.5 xanchor 0.5 #Info about the person: age, height, happiness, obedience, etc.
                        text "Age: [the_person.age]" style "menu_text_style" size 16
                        if the_person.is_employee():
                            text "Required Salary: $[the_person.salary]/day" style "menu_text_style" size 16
                        text "Personality: " + the_person.personality.personality_type_prefix.capitalize() style "menu_text_style" size 16
                        if the_person.is_girlfriend():
                            text "Relationship: [mc.name]'s girlfriend"
                        elif the_person.relationship:
                            text "Relationship: " + the_person.relationship style "menu_text_style" size 16
                            if the_person.relationship != "Single":
                                text "Significant Other: " + the_person.SO_name style "menu_text_style" size 16
                        if the_person.kids > 0:
                            text "Kids: " + str(the_person.kids) style "menu_text_style" size 16
                            text "TODO: kids with MC"
                        text "" style "menu_text_style" size 16
                        text "Happiness: [the_person.happiness]" style "menu_text_style" size 16
                        text "Sluttiness: [the_person.sluttiness] - " + get_gold_heart(the_person.sluttiness) style "menu_text_style" size 16
                        text "Obedience: [the_person.obedience] - " + get_obedience_plaintext(the_person.obedience) style "menu_text_style" size 16
                        text "Suggestibility: [the_person.suggestibility]%" style "menu_text_style" size 16
                        text "Height: " + height_to_string(the_person.height) style "menu_text_style" size 16
                        text "Eye Colour: " + the_person.eyes[0].title() style "menu_text_style" size 16
                        text "Cup size: [the_person.tits]" style "menu_text_style" size 16
                        text "Weight: " + get_person_weight_string(the_person) style "menu_text_style" size 16
                frame:
                    background "#1a45a1aa"
                    xsize 420
                    ysize 550
                    vbox:
                        text "Love Story Progress" style "menu_text_style" size 26 xalign 0.5 xanchor 0.5 #Info about the persons raw stats, work skills, and sex skills
                        for love_text in story_dict.get("love_story", []):
                            text love_text style "menu_text_style" size 16

                frame:
                    #$ master_opinion_dict = dict(the_person.opinions, **the_person.sexy_opinions)
                    background "#1a45a1aa"
                    xsize 420
                    ysize 550
                    vbox:
                        text "Lust Story Progress" style "menu_text_style" size 26 xalign 0.5 xanchor 0.5 #Info about the persons loves, likes, dislikes, and hates
                        for lust_text in story_dict.get("lust_story", []):
                            text lust_text style "menu_text_style" size 16
            hbox:
                xsize 1320
                spacing 60
                frame:
                    background "#1a45a1aa"
                    xsize 630
                    ysize 200
                    vbox:
                        text "Other information" style "menu_text_style" size 30
                        for other_info in story_dict.get("other_info", []):
                            text other_info style "menu_text_style" size 16
                        if the_person.get_fetish_count() == 0:
                            text "No known fetishes" style "menu_text_style" size 16
                        if the_person.has_breeding_fetish():
                            text "Has breeding fetish" style "menu_text_style" size 16
                        if the_person.has_anal_fetish():
                            text "Has anal fetish" style "menu_text_style" size 16
                        if the_person.has_cum_fetish():
                            text "Has cum fetish" style "menu_text_style" size 16
                        if the_person.has_exhibition_fetish():
                            text "Is an exhibitionist" style "menu_text_style" size 16
                        if the_person.is_girlfriend() and not the_person.is_jealous():
                            text "Is polyamory" style "menu_text_style" size 16
                        elif the_person.is_girlfriend():
                            text "Is monogamous" style "menu_text_style" size 16

                frame:
                    background "#1a45a1aa"
                    xsize 630
                    ysize 200
                    vbox:
                        text "Teamups" style "menu_text_style" size 30
                        for teamup_info in story_dict.get("teamup_list", []):
                            text teamup_info style "menu_text_style" size 16
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
                    action Hide("story_progress")
                textbutton "Return" align [0.5,0.5] style "return_button_style"
