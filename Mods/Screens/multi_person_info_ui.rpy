init -2 python:
    def get_sluttiness_info_tooltip(person):
        tooltip = ""
        positive_effects = ""
        negative_effects = ""
        for situation in person.situational_sluttiness:
            if person.situational_sluttiness[situation][0] > 0: #We purposefully ignore 0 so we don't show null sluttiness modifiers.
                positive_effects += get_coloured_arrow(1)+get_red_heart(person.situational_sluttiness[situation][0])+" - " + person.situational_sluttiness[situation][1] + "\n"
            elif person.situational_sluttiness[situation][0] < 0:
                negative_effects += get_coloured_arrow(-1)+get_red_heart(-person.situational_sluttiness[situation][0])+" - " + person.situational_sluttiness[situation][1] + "\n"
        tooltip += positive_effects + negative_effects
        tooltip += "The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness (" + get_red_heart(20) + ") is easier to raise but drops slowly over time. Core sluttiness (" + get_gold_heart(20) + ") is permanent, but can only be created by using serum to raise suggestability or by making a girl climax."
        return tooltip

    def get_obedience_info_tooltip(person):
        tooltip = ""
        positive_effects = ""
        negative_effects = ""
        for situation in person.situational_obedience:
            if person.situational_obedience[situation][0] > 0:
                positive_effects += get_coloured_arrow(1)+"+"+__builtin__.str(person.situational_obedience[situation][0])+ " Obedience - " + person.situational_obedience[situation][1] + "\n"
            elif person.situational_obedience[situation][0] < 0:
                negative_effects += get_coloured_arrow(1)+""+__builtin__.str(person.situational_obedience[situation][0])+ " Obedience - " + person.situational_obedience[situation][1] + "\n"
        tooltip += positive_effects + negative_effects
        tooltip += "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."
        return tooltip

screen multi_person_info_ui(actors): #Used to display stats for multi people while you're talking to them, takes an array of Actor objects.
    frame:
        background Frame("gui/topbox.png")
        xsize 1100
        ysize 154
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
                    if actor.person.title:
                        text actor.person.title style "menu_text_style" size 32 ysize 32
                    else:
                        text "???" style "menu_text_style" font actor.person.char.what_args["font"] color actor.person.char.what_args["color"] size 32

                    if actor.person.arousal > 0:
                        textbutton "Arousal: [actor.person.arousal]% (+" + get_red_heart(__builtin__.int(actor.person.arousal/4)) + ")":
                            ysize 22
                            text_style "menu_text_style"
                            tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                            action NullAction()
                            sensitive True
                    else:
                        textbutton "Arousal: 0%":
                            ysize 22
                            text_style "menu_text_style"
                            tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                            action NullAction()
                            sensitive True

                    textbutton "Happiness: [actor.person.happiness]":
                        ysize 22
                        text_style "menu_text_style"
                        tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                        action NullAction()
                        sensitive True

                    textbutton "Sluttiness: " + get_heart_image_list(actor.person):
                        ysize 22
                        text_style "menu_text_style"
                        tooltip get_sluttiness_info_tooltip(actor.person)
                        action NullAction()
                        sensitive True

                    textbutton "Obedience: [actor.person.obedience] - " + get_obedience_plaintext(actor.person.obedience):
                        ysize 22
                        text_style "menu_text_style"
                        tooltip get_obedience_info_tooltip(actor.person)
                        action NullAction()
                        sensitive True
