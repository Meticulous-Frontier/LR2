init 1310 python:
    def relaxed_titles(person):
        valid_titles = []
        valid_titles.append("Mrs. " + person.last_name)
        valid_titles.append(person.name)
        if person.sluttiness > 40:
           valid_titles.append("Chill Bitch")
        if person.sluttiness > 60:
            valid_titles.append("Easy Slut")

        return valid_titles

    relaxed_personality.titles_function = relaxed_titles
