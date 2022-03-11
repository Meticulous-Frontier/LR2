init 1310 python:
    def introvert_titles(person):
        valid_titles = []
        valid_titles.append(person.formal_address + " " + person.last_name)
        if person.love > 20:
            valid_titles.append(person.name)
        if person.sluttiness > 40:
            valid_titles.append("Baby Girl")
        if person.sluttiness > 60:
            valid_titles.append("Lollipop")

        return valid_titles

    def introvert_player_titles(person):
        valid_titles = []
        valid_titles.append("Mr. " + mc.last_name)
        if person.has_breeding_fetish():
            valid_titles.append("Daddy")
        return valid_titles

    introvert_personality.titles_function = introvert_titles
    introvert_personality.player_titles_function = introvert_player_titles
