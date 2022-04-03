init 1310 python:       # init after VREN personalities, but before our personalities
    def wild_titles(person):
        valid_titles = []
        valid_titles.append(person.formal_address + " " + person.last_name)
        valid_titles.append(person.name)
        if person.sluttiness > 40:
            valid_titles.append("Sugar Lips")
        if person.sluttiness > 60:
            valid_titles.append("Bitch")

        return valid_titles

    def wild_player_titles(person):
        valid_titles = []
        valid_titles.append("Mr. " + mc.last_name)
        valid_titles.append(mc.name)
        if person.has_breeding_fetish():
            valid_titles.append("Stud")
        return valid_titles


    wild_personality.titles_function = wild_titles
    wild_personality.player_titles_function = wild_player_titles
