init 1310 python:       # init after VREN personalities, but before our personalities
    def reserved_titles(person):
        valid_titles = []
        valid_titles.append(person.formal_address + " " + person.last_name)
        if person.love > 20:
            valid_titles.append(person.name)
        if person.love > 30:
            valid_titles.append(person.name)
        if person.sluttiness > 40:
            valid_titles.append("Cherry")
        if person.sluttiness > 60:
            valid_titles.append("Whore")

        return valid_titles

    def reserved_player_titles(person):
        valid_titles = []
        valid_titles.append("Mr. " + mc.last_name)
        if person.love > 30:
            valid_titles.append(mc.name)
        if person.has_breeding_fetish():
            valid_titles.append("Bull")
        return valid_titles

    reserved_personality.titles_function = reserved_titles
    reserved_personality.player_titles_function = reserved_player_titles
