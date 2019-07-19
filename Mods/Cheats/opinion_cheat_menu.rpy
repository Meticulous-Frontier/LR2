init python:
    if "opinion_edit_menu_keybind" not in config.overlay_screens:
        config.overlay_screens.append("opinion_edit_menu_keybind")

    def update_opinion_score(self, topic, category, value, discover = True):

        score = self.get_opinion_score(topic)

        if score is 2:
            vars(self)[category][topic] = [score - 4, discover]

        else:
            vars(self)[category][topic] = [score + value, discover]

    Person.update_opinion_score = update_opinion_score

    def get_opinion_status(self, topic): #topic is a string matching the topics given in our random list (ie. "the colour blue", "sports"). Returns a tuple containing the score: -2 for hates, -1 for dislikes, 0 for no opinion, 1 for likes, and 2 for loves, and a bool to say if the opinion is known or not.
        if topic in self.opinions:
            return self.opinions[topic][1]

        if topic in self.sexy_opinions:
            return self.sexy_opinions[topic][1]

        return "Not assigned"
    Person.get_opinion_status = get_opinion_status

screen opinion_edit_menu_keybind():
    key "p" action ToggleScreen("opinion_edit_menu")
    key "P" action ToggleScreen("opinion_edit_menu")

screen opinion_edit_menu():

    default categories = {"Sexy Opinion": [sexy_opinions_list, "sexy_opinions"], "Normal Opinions": [opinions_list, "opinions"]}
    default target = the_person

    if target is not None:
        grid len(categories) 1:
            xfill 0.5
            for n in categories:
                frame:
                    vbox:
                        frame:
                            text n style "serum_text_style_header"
                            xfill True
                        viewport:
                            draggable True
                            mousewheel True
                            yfill True
                            vbox:
                                for x in categories[n][0]:
                                    textbutton "[x]\n" +  " Score: " + str(target.get_opinion_score(x)) + " | " + "Discovered: " + str(target.get_opinion_status(x)):
                                        style "textbutton_no_padding_highlight"
                                        text_style "serum_text_style"
                                        xfill True
                                        action Function(target.update_opinion_score, x, categories[n][1], 1)
                                        alternate Function(target.update_opinion_score, x, categories[n][1], 0, False)
