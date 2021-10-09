init 1310 python:
    def wild_titles(person):
        valid_titles = []
        valid_titles.append(person.name)
        if person.sluttiness > 40:
            valid_titles.append("Sugar Lips")
        if person.sluttiness > 60:
            valid_titles.append("Bitch")

        return valid_titles

    wild_personality.titles_function = wild_titles