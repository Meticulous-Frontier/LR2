# Override default person_info_ui screen by VREN to show extra information about character
init 2:
    screen person_info_ui(person): #Used to display stats for a person while you're talking to them.
        $ formatted_tooltip = ""
        $ formatted_obedience_tooltip = ""
        python:
            positive_effects = ""
            negative_effects = ""
            for situation in person.situational_sluttiness:
                if person.situational_sluttiness[situation][0] > 0: #We purposefully ignore 0 so we don't show null sluttiness modifiers.
                    positive_effects += get_coloured_arrow(1)+get_red_heart(person.situational_sluttiness[situation][0])+" - " + person.situational_sluttiness[situation][1] + "\n"
                elif person.situational_sluttiness[situation][0] < 0:
                    negative_effects += get_coloured_arrow(-1)+get_red_heart(-person.situational_sluttiness[situation][0])+" - " + person.situational_sluttiness[situation][1] + "\n"
            formatted_tooltip += positive_effects + negative_effects
            formatted_tooltip += "The higher a girl's sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness (" + get_red_heart(20) + ") is easier to raise but drops slowly over time. Core sluttiness (" + get_gold_heart(20) + ") is permanent, but can only be created by using serum to raise suggestability or by making the girl climax."

            positive_effects = ""
            negative_effects = ""
            for situation in person.situational_obedience:
                if person.situational_obedience[situation][0] > 0:
                    positive_effects += get_coloured_arrow(1)+"+"+__builtin__.str(person.situational_obedience[situation][0])+ " Obedience - " + person.situational_obedience[situation][1] + "\n"
                elif person.situational_obedience[situation][0] < 0:
                    negative_effects += get_coloured_arrow(1)+""+__builtin__.str(person.situational_obedience[situation][0])+ " Obedience - " + person.situational_obedience[situation][1] + "\n"
            formatted_obedience_tooltip += positive_effects + negative_effects
            formatted_obedience_tooltip += "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."

        frame:
            background "gui/topbox.png"
            xsize 1100
            ysize 200
            yalign 0.0
            xalign 0.5
            xanchor 0.5
            hbox:
                xanchor 0.5
                xalign 0.5
                yalign 0.3
                spacing 100
                vbox:
                    if person.title:
                        text person.title style "menu_text_style" size 40
                    else:
                        text "???" style "menu_text_style" font person.char.what_args["font"] color person.char.what_args["color"] size 40
                    
                    if mc.business.get_employee_title(person) == "None":
                        text "     Job: Not employed." style "menu_text_style"
                    else:
                        text "     Job: " + mc.business.get_employee_title(person) style "menu_text_style"

                    for role in person.special_role:
                        if not role.role_name is None:
                            text "       - " + role.role_name style "menu_text_style" size 14

                vbox:
                    if person.arousal > 0:
                        textbutton "Arousal: [person.arousal]% (+" + get_red_heart(__builtin__.int(person.arousal/4)) + ")":
                            ysize 28
                            text_style "menu_text_style"
                            tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                            action NullAction()
                            sensitive True
                    else:
                        textbutton "Arousal: 0%":
                            ysize 28
                            text_style "menu_text_style"
                            tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                            action NullAction()
                            sensitive True

                    textbutton "Happiness: [person.happiness]":
                        ysize 28
                        text_style "menu_text_style"
                        tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                        action NullAction()
                        sensitive True

                    textbutton "Love: [person.love]":
                        ysize 28
                        text_style "menu_text_style"
                        tooltip "Girls who love you will be more willing to have sex when you are in private (as long as they are not family) and be more devoted to you. Girls who hate you will have a lower effective sluttiness regardless of the situation."
                        action NullAction()
                        sensitive True

                    textbutton "Suggestibility: [person.suggestibility]%":
                        ysize 28
                        text_style "menu_text_style"
                        tooltip "How likely this character is to have an increase to her core sluttiness. Every time chunk there is a [person.suggestibility]% chance to change 1 point of temporary sluttiness (" + get_red_heart(5) + ") into core sluttiness (" + get_gold_heart(5) + ") as long as the temporary sluttiness is higher."
                        action NullAction()
                        sensitive True

                    textbutton "Sluttiness: " + get_heart_image_list(person):
                        ysize 28
                        text_style "menu_text_style"
                        tooltip formatted_tooltip
                        action NullAction()
                        sensitive True

                    textbutton "Obedience: [person.obedience] - " + get_obedience_plaintext(person.obedience):
                        ysize 28
                        text_style "menu_text_style"
                        tooltip formatted_obedience_tooltip
                        action NullAction()
                        sensitive True

                vbox:
                    textbutton "Detailed Information" action Show("person_info_detailed",the_person=person) style "textbutton_style" text_style "textbutton_text_style"

                    textbutton "Age: [person.age]":
                        ysize 28
                        text_style "menu_text_style"
                        action NullAction()
                        sensitive True

                    $ person_height = height_to_string(person.height)
                    textbutton "Height: [person_height]":
                        ysize 28
                        text_style "menu_text_style"
                        tooltip "The length of the person in feet and inches."
                        action NullAction()
                        sensitive True

                    textbutton "Cup size: [person.tits]":
                        ysize 28
                        text_style "menu_text_style"
                        action NullAction()
                        sensitive True

                    if hasattr(person, "weight"):
                        $ weight = get_person_weight_string(person)
                        textbutton "Weight: [weight] lbs":
                            ysize 28
                            text_style "menu_text_style"
                            action NullAction()
                            sensitive True
