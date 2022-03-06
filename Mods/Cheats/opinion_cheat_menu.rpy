init python:
    if "opinion_edit_menu_keybind" not in config.overlay_screens:
        config.overlay_screens.append("opinion_edit_menu_keybind")

    def update_opinion_score(self, topic, category, value, discover = True):

        score = self.get_opinion_score(topic)

        if value > 0 and score >= 2:
            vars(self)[category][topic] = [-2, discover]
        elif value < 0 and score <= -2:
            vars(self)[category][topic] = [2, discover]
        else:
            vars(self)[category][topic] = [score + value, discover]

    Person.update_opinion_score = update_opinion_score

    def remove_opinion(self, topic, category):
        if topic in self.opinions:
            del self.opinions[topic]
        if topic in self.sexy_opinions:
            del self.sexy_opinions[topic]

    Person.remove_opinion = remove_opinion

    def get_opinion_status(self, topic): #topic is a string matching the topics given in our random list (ie. "the colour blue", "sports"). Returns a tuple containing the score: -2 for hates, -1 for dislikes, 0 for no opinion, 1 for likes, and 2 for loves, and a bool to say if the opinion is known or not.
        if topic in self.opinions:
            return self.opinions[topic][1]

        if topic in self.sexy_opinions:
            return self.sexy_opinions[topic][1]

        return "Not assigned"
    Person.get_opinion_status = get_opinion_status

    def cheat_opinion_score_to_string(score):
        if score <= -2:
            return "hates"
        if score == -1:
            return "dislikes"
        if score == 0:
            return "no opinion"
        if score == 1:
            return "likes"
        if score >= 2:
            return "loves"

screen opinion_edit_menu_keybind():
    key "p" action ToggleScreen("opinion_edit_menu")
    key "P" action ToggleScreen("opinion_edit_menu")

screen opinion_edit_menu():

    default categories = {"Sexy Opinion": [sexy_opinions_list, "sexy_opinions"], "Normal Opinions": [opinions_list, "opinions"]}
    if "the_person" in globals():
        default target = the_person
    else:
        default target = None

    if target:
        grid __builtin__.len(categories) 1:
            xfill 0.5
            for n in categories:
                frame:
                    margin (0, 24)
                    vbox:
                        frame:
                            text target.name + " - " + n style "serum_text_style_header"
                            xfill True

                        viewport:
                            draggable True
                            mousewheel True
                            scrollbars "vertical"
                            yfill True
                            vbox:
                                for x in sorted(categories[n][0], key=lambda s: s.lower()):
                                    hbox:
                                        textbutton x.title():
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            xsize 370
                                            padding (4,2)
                                            action Function(target.update_opinion_score, x, categories[n][1], 1)
                                            alternate Function(target.update_opinion_score, x, categories[n][1], 0, False)

                                        textbutton " - ":
                                            padding (0,2)
                                            xsize 36
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            action [
                                                Function(target.update_opinion_score, x, categories[n][1], -1)
                                            ]
                                        textbutton cheat_opinion_score_to_string(target.get_opinion_score(x)).title() + " | " + "Discovered: " + str(target.get_opinion_status(x)):
                                            padding (0,2)
                                            xsize 440
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            action NullAction()
                                        textbutton " + ":
                                            padding (0,2)
                                            xsize 36
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            action [
                                                Function(target.update_opinion_score, x, categories[n][1], 1)
                                            ]
                                        textbutton "{color=#D00}{b}" + " X " + "{/b}{/color}":
                                            padding (0,2)
                                            xsize 44
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            action [
                                                Function(target.remove_opinion, x, categories[n][1])
                                            ]
    else:
            frame:
                background "gui/button/main_choice_idle_background.png"
                anchor [0.5,0.5]
                align [0.5,0.55]
                xysize [600,120]
                textbutton "Interact with girl first" align [0.5,0.5] text_style "serum_text_style_header"
