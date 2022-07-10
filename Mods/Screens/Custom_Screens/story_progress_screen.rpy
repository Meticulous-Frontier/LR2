init 2:
    screen story_progress(person):
        # show_candidate(person)
        add "Paper_Background.png"
        modal True
        zorder 100

        default mannequin = person
        default preview_outfit = person.outfit

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
                text "[person.name] [person.last_name]" style "menu_text_style" size 50 xanchor 0.5 xalign 0.5 color person.char.who_args["color"] font person.char.what_args["font"]
                text person.story_character_description style "menu_text_style" size 16 xanchor 0.5 xalign 0.5 yalign 1.0
            hbox:
                xsize 1320
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xsize 420
                    ysize 450
                    vbox:
                        text "Personal Information" style "serum_text_style_header" #Info about the person: age, height, happiness, obedience, etc.
                        text "Age: [person.age]" style "menu_text_style" size 16
                        if person.is_employee():
                            text "Required Salary: $[person.salary]/day" style "menu_text_style" size 16
                        text "Personality: " + person.personality.personality_type_prefix.capitalize() style "menu_text_style" size 16
                        if person.is_girlfriend():
                            text "Relationship: [mc.name]'s girlfriend" style "menu_text_style" size 16
                        elif person.relationship:
                            text "Relationship: " + person.relationship style "menu_text_style" size 16
                            if person.relationship != "Single":
                                text "Significant Other: " + person.SO_name style "menu_text_style" size 16
                        if person.kids > 0:
                            text "Kids: " + str(person.kids) style "menu_text_style" size 16
                            text "TODO: kids with MC"
                        text "" style "menu_text_style" size 16
                        text "Happiness: [person.happiness]" style "menu_text_style" size 16
                        text "Sluttiness: [person.sluttiness] - " + get_gold_heart(person.sluttiness) style "menu_text_style" size 16
                        text "Obedience: [person.obedience] {image=triskelion_token_small} " + get_obedience_plaintext(person.obedience) style "menu_text_style" size 16
                        text "Suggestibility: [person.suggestibility]%" style "menu_text_style" size 16
                        text "Height: " + height_to_string(person.height) style "menu_text_style" size 16
                        text "Eye Colour: " + person.eyes[0].title() style "menu_text_style" size 16
                        text "Cup size: [person.tits]" style "menu_text_style" size 16
                        text "Weight: " + get_person_weight_string(person) style "menu_text_style" size 16
                frame:
                    background "#1a45a1aa"
                    xsize 420
                    ysize 450
                    vbox:
                        text "Love Story Progress" style "serum_text_style_header" #Info about the persons raw stats, work skills, and sex skills
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                for love_text in person.story_love_list():
                                    text love_text style "menu_text_style" size 16 text_align 0.0

                frame:
                    #$ master_opinion_dict = dict(person.opinions, **person.sexy_opinions)
                    background "#1a45a1aa"
                    xsize 420
                    ysize 450
                    vbox:
                        text "Lust Story Progress" style "serum_text_style_header" #Info about the persons loves, likes, dislikes, and hates
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                for lust_text in person.story_lust_list():
                                    text lust_text style "menu_text_style" size 16 text_align 0.0
            hbox:
                xsize 1320
                spacing 60
                frame:
                    background "#1a45a1aa"
                    xsize 630
                    ysize 300
                    vbox:
                        text "Other information" style "serum_text_style_header"
                        for other_info in person.story_other_list():
                            text other_info style "menu_text_style" size 16
                        if person.get_fetish_count() == 0:
                            text "No known fetishes" style "menu_text_style" size 16
                        if person.has_breeding_fetish():
                            text "Has breeding fetish" style "menu_text_style" size 16
                        if person.has_anal_fetish():
                            text "Has anal fetish" style "menu_text_style" size 16
                        if person.has_cum_fetish():
                            text "Has cum fetish" style "menu_text_style" size 16
                        if person.has_exhibition_fetish():
                            text "Is an exhibitionist" style "menu_text_style" size 16
                        if person.is_girlfriend() and not person.is_jealous():
                            text "Is polyamory" style "menu_text_style" size 16
                        elif person.is_girlfriend():
                            text "Is monogamous" style "menu_text_style" size 16

                frame:
                    background "#1a45a1aa"
                    xsize 630
                    ysize 300
                    vbox:
                        text "Teamups" style "serum_text_style_header"
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                for teamup_info in [x for x in person.story_teamup_list() if isinstance(x, list) and len(x) == 2]:

                                    if teamup_info[0] != " ":
                                        vbox:
                                            textbutton teamup_info[0].title:
                                                action [
                                                    Function(person.hide_person,draw_layer="8"),
                                                    Function(teamup_info[0].draw_person, draw_layer="8", wipe_scene = False),
                                                    Show("story_progress",person=teamup_info[0])
                                                ]
                                                style "textbutton_style"
                                                text_style "textbutton_text_style"
                                    vbox:
                                        text teamup_info[1] style "menu_text_style" size 16
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
                    action [
                        Function(hide_mannequin),
                        (Hide("story_progress"))
                    ]
                textbutton "Return" align [0.5,0.5] style "return_button_style"
