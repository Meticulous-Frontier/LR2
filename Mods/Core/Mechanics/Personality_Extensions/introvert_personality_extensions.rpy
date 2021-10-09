init 1310 python:
    def introvert_titles(person):
        valid_titles = []
        valid_titles.append(person.name)
        if person.sluttiness > 40:
            valid_titles.append("Baby Girl")
        if person.sluttiness > 60:
            valid_titles.append("Lollipop")

        return valid_titles


    introvert_personality.titles_function = introvert_titles