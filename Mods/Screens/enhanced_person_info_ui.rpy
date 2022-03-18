# Override default person_info_ui screen by VREN to show extra information about character
init -1 python:

    @renpy.pure
    def person_info_ui_format_hearts(value):
        heart_value = __builtin__.abs(value)
        if (heart_value / 4) > 10:
            return get_gold_heart(heart_value / 4)
        return get_red_heart(heart_value)

    def person_info_ui_get_formatted_tooltip(person):
        tooltip = ""
        positive_effects = ""
        negative_effects = ""
        for situation in person.situational_sluttiness:
            if person.situational_sluttiness[situation][0] > 0: #We purposefully ignore 0 so we don't show null sluttiness modifiers.
                positive_effects += get_coloured_arrow(1) + " " + person_info_ui_format_hearts(person.situational_sluttiness[situation][0]) + " - " + person.situational_sluttiness[situation][1] + "\n"
            elif person.situational_sluttiness[situation][0] < 0:
                negative_effects += get_coloured_arrow(-1) + " " + person_info_ui_format_hearts(person.situational_sluttiness[situation][0]) + " - " + person.situational_sluttiness[situation][1] + "\n"
        tooltip += positive_effects + negative_effects
        return tooltip

    def person_info_ui_get_formatted_obedience_tooltip(person):
        tooltip = ""
        positive_effects = ""
        negative_effects = ""
        for situation in person.situational_obedience:
            if person.situational_obedience[situation][0] > 0:
                positive_effects += get_coloured_arrow(1)+"+"+__builtin__.str(person.situational_obedience[situation][0])+ " Obedience - " + person.situational_obedience[situation][1] + "\n"
            elif person.situational_obedience[situation][0] < 0:
                negative_effects += get_coloured_arrow(-1)+""+__builtin__.str(person.situational_obedience[situation][0])+ " Obedience - " + person.situational_obedience[situation][1] + "\n"
        tooltip += positive_effects + negative_effects
        return tooltip

    def person_info_ui_get_serum_info_tooltip(person):
        tooltip = ""
        for serum in person.serum_effects:
            if len(tooltip) > 0:
                tooltip += "\n"
            tooltip += serum.name + " : " + str(serum.duration - serum.duration_counter) + " Turns Left"
        return tooltip

    def person_info_ui_get_job_title(person):
        if person.event_triggers_dict.get("job_known", False):
            return person.job.job_title
        return "Unknown"

init 2:
    screen person_info_ui(person): #Used to display stats for a person while you're talking to them.
        layer "solo" #By making this layer active it is cleared whenever we draw a person or clear them off the screen.

        default job_title = person_info_ui_get_job_title(person)
        default arousal_info = get_arousal_with_token_string(person.arousal, person.max_arousal)
        default energy_info = get_energy_string(person.energy, person.max_energy)
        default happiness_info = str(__builtin__.int(person.happiness))
        default love_info = str(__builtin__.int(person.love))
        default sluttiness_info = get_heart_image_list(person.sluttiness, person.effective_sluttiness())
        default obedience_info = str(person.obedience) + " - " + get_obedience_plaintext(person.obedience)
        default height_info = height_to_string(person.height)
        default weight_info = get_person_weight_string(person)

        frame:
            background im.Alpha("gui/topbox.png", .9)
            xsize 1100
            ysize 200
            yalign 0.0
            xalign 0.5
            xanchor 0.5
            hbox:
                xanchor 0.5
                xalign 0.5
                yalign 0.1
                spacing 100
                vbox:
                    text format_titles(person) style "menu_text_style" size 30

                    text "     Job: [job_title]" style "menu_text_style"

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        xsize 220
                        ysize 100
                        vbox:
                            for role in [x for x in person.special_role if not x.hidden]:
                                text "       - [role.role_name]" style "menu_text_style" size 14

                vbox:
                    yoffset 10
                    textbutton "Arousal: [arousal_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will make a girl happier and may put them into a Trance if their suggestibility is higher than 0."
                        action NullAction()
                        sensitive True

                    textbutton "Energy: [energy_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "Energy is spent while having sex, with more energy spent on positions that give the man more pleasure. Some energy comes back each turn, and a lot of energy comes back over night."
                        action NullAction()
                        sensitive True

                    textbutton "Happiness: [happiness_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                        action NullAction()
                        sensitive True

                    textbutton "Love: [love_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "Girls who love you will be more willing to have sex when you're in private (as long as they aren't family) and be more devoted to you. Girls who hate you will have a lower effective sluttiness regardless of the situation."
                        action NullAction()
                        sensitive True

                    hbox:
                        textbutton "Obedience: [obedience_info]":
                            style "transparent_style"
                            text_style "menu_text_style"
                            tooltip "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."
                            action NullAction()
                            sensitive True

                        if any(x[0] > 0 or x[0] < 0 for x in person.situational_obedience.itervalues()):
                            textbutton "{image=question_mark_small}":
                                yoffset 6
                                style "transparent_style"
                                tooltip person_info_ui_get_formatted_obedience_tooltip(person)
                                action NullAction()
                                sensitive True

                    hbox:
                        textbutton "Sluttiness: [sluttiness_info]":
                            style "transparent_style"
                            text_style "menu_text_style"
                            tooltip "The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness (" + get_red_heart(20) + ") is added to her sluttiness based on effect modifiers {image=question_mark_small}."
                            action NullAction()
                            sensitive True

                        if any(x[0] > 0 or x[0] < 0 for x in person.situational_sluttiness.itervalues()):
                            textbutton "{image=question_mark_small}":
                                yoffset 6
                                style "transparent_style"
                                tooltip person_info_ui_get_formatted_tooltip(person)
                                action NullAction()
                                sensitive True

                vbox:
                    xoffset -40
                    yoffset -8
                    hbox:
                        textbutton "Detailed Information" action Show("person_info_detailed",the_person=person) style "textbutton_style" text_style "textbutton_text_style"
                        if person.serum_effects:
                            textbutton "{image=serum_vial}":
                                yoffset 16
                                style "transparent_style"
                                text_style "menu_text_style"
                                tooltip person_info_ui_get_serum_info_tooltip(person)
                                action NullAction()
                                sensitive True

                        if person.can_clone():
                            textbutton "{image=dna_sequence}":
                                yoffset 16
                                style "transparent_style"
                                text_style "menu_text_style"
                                tooltip "This person can be cloned."
                                action NullAction()
                                sensitive True

                        if person.home in mc.known_home_locations:
                            textbutton "{image=home_marker}":
                                yoffset 16
                                style "transparent_style"
                                text_style "menu_text_style"
                                tooltip "The home address is known."
                                action NullAction()
                                sensitive True

                    textbutton "Suggestibility: [person.suggestibility]%":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "How likely a girl is to slip into a trance when she cums. While in a trance she will be highly suggestible, and you will be able to directly influence her stats, skills, and opinions."
                        action NullAction()
                        sensitive True

                    textbutton "Age: [person.age]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "The age of the girl."
                        action NullAction()
                        sensitive True

                    textbutton "Height: [height_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        if use_imperial_system:
                            tooltip "The length of the girl in feet and inches."
                        else:
                            tooltip "The length of the girl in centimeters."
                        action NullAction()
                        sensitive True

                    textbutton "Cup size: [person.tits]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "The size of the breasts."
                        action NullAction()
                        sensitive True

                    textbutton "Weight: [weight_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        if use_imperial_system:
                            tooltip "The weight of the girl in pounds.\nDetermines the body type."
                        else:
                            tooltip "The weight of the girl in kilograms\nDetermines the body type."
                        action NullAction()
                        sensitive True
