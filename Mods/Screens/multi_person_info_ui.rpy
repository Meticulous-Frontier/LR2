#Used to display stats for multi people while you're talking to them, takes an array of Actor objects.
init 2 python:
    def multi_person_info_ui_get_formatted_tooltip(person):
        tooltip = ""
        if mc.business.get_employee_title(person) != "None":
            tooltip += "Job: " + mc.business.get_employee_title(person) + "\n"
        for role in [x.role_name for x in person.special_role if not x.hidden]:
            tooltip += role + "\n"
        tooltip += "Love: " + str(person.love) + "\n"
        tooltip += "Age: " + str(person.age) + "\n"
        tooltip += "Height: " + height_to_string(person.height) + "\n"
        tooltip += "Cup size: " + str(person.tits) + "\n"
        tooltip += "Weight: " + get_person_weight_string(person)
        return tooltip

screen multi_person_info_ui(actors):
    layer "Active"
    frame:
        background Frame("gui/topbox.png")
        xsize 1100
        ysize 180
        yalign 0.0
        xalign 0.5
        xanchor 0.5

        hbox:
            xanchor 0.5
            xalign 0.5
            spacing 10
            xsize 1000
            xoffset 50

            for actor in sorted(actors, key=lambda a: a.sort_order):
                vbox:
                    hbox:
                        textbutton "{image=question_mark_small}":
                            yoffset 12
                            ysize 28
                            tooltip multi_person_info_ui_get_formatted_tooltip(actor.person)
                            action NullAction()
                            sensitive True

                        if actor.person.title:
                            text actor.person.title style "menu_text_style" size 30 ysize 30
                        else:
                            text "???" style "menu_text_style" font actor.person.char.what_args["font"] color actor.person.char.what_args["color"] size 30

                        if actor.person.serum_effects:
                            textbutton "{image=serum_vial} +[actor.person.suggestibility]%":
                                yoffset 6
                                ysize 24
                                text_style "menu_text_style"
                                tooltip person_info_ui_get_serum_info_tooltip(actor.person)
                                action NullAction()
                                sensitive True

                    if actor.person.arousal > 0:
                        textbutton "Arousal: [actor.person.arousal]/[actor.person.max_arousal] (+" + get_red_heart(__builtin__.int(actor.person.arousal/4)) + ")":
                            ysize 23
                            yoffset -10
                            text_style "menu_text_style"
                            tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                            action NullAction()
                            sensitive True
                    else:
                        textbutton "Arousal: 0%":
                            ysize 23
                            yoffset -10
                            text_style "menu_text_style"
                            tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                            action NullAction()
                            sensitive True

                    textbutton "Energy: [actor.person.energy]/[actor.person.max_energy] {image=gui/extra_images/energy_token.png}":
                        ysize 23
                        yoffset -10
                        text_style "menu_text_style"
                        tooltip "Energy is spent while having sex, with more energy spent on positions that give the man more pleasure. Some energy comes back each turn, and a lot of energy comes back over night."
                        action NullAction()
                        sensitive True

                    textbutton "Happiness: [actor.person.happiness]":
                        ysize 23
                        yoffset -10
                        text_style "menu_text_style"
                        tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                        action NullAction()
                        sensitive True

                    hbox:
                        textbutton "Sluttiness: " + get_heart_image_list(actor.person):
                            ysize 23
                            yoffset -10
                            text_style "menu_text_style"
                            tooltip "The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness (" + get_red_heart(20) + ") is easier to raise but drops slowly over time. Core sluttiness (" + get_gold_heart(20) + ") is permanent, but only increases slowly unless a girl is suggestible."
                            action NullAction()
                            sensitive True

                        if any(x[0] > 0 or x[0] < 0 for x in actor.person.situational_sluttiness.itervalues()):
                            textbutton "{image=question_mark_small}":
                                yoffset 4
                                ysize 23
                                tooltip person_info_ui_get_formatted_tooltip(actor.person)
                                action NullAction()
                                sensitive True

                    hbox:
                        textbutton "Obedience: [actor.person.obedience] - " + get_obedience_plaintext(actor.person.obedience):
                            ysize 23
                            yoffset -10
                            text_style "menu_text_style"
                            tooltip "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."
                            action NullAction()
                            sensitive True

                        if any(x[0] > 0 or x[0] < 0 for x in actor.person.situational_obedience.itervalues()):
                            textbutton "{image=question_mark_small}":
                                yoffset 4
                                ysize 23
                                tooltip person_info_ui_get_formatted_obedience_tooltip(actor.person)
                                action NullAction()
                                sensitive True
