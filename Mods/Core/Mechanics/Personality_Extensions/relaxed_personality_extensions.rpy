init 1310 python:
    def relaxed_titles(person):
        valid_titles = []
        valid_titles.append(person.formal_address + " " + person.last_name)
        if person.love > 20:
            valid_titles.append(person.name)
        if person.sluttiness > 40:
            valid_titles.append("Candy")
        if person.sluttiness > 60:
            valid_titles.append("Hot Stuff")

        return valid_titles

    def relaxed_player_titles(person):
        valid_titles = []
        valid_titles.append("Mr. " + mc.last_name)
        if person.love > 10:
            valid_titles.append(mc.name)
        if person.has_breeding_fetish():
            valid_titles.append("Bull")
        return valid_titles

    relaxed_personality.titles_function = relaxed_titles
    relaxed_personality.player_titles_function = relaxed_player_titles
