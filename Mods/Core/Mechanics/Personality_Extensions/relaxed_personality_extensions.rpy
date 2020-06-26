init 1310 python:
    def relaxed_titles(the_person):
        valid_titles = []
        valid_titles.append("Mrs. " + the_person.last_name)
        valid_titles.append(the_person.name)
        if the_person.sluttiness > 40:
           valid_titles.append("Chill Bitch")
        if the_person.sluttiness > 60:
            valid_titles.append("Easy Slut")

        return valid_titles

    relaxed_personality.titles_function = relaxed_titles
