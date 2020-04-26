init 1310 python:
    def wild_titles(the_person):
        valid_titles = []
        valid_titles.append(the_person.name)
        if the_person.sluttiness > 40:
           valid_titles.append("Crazy Bitch")
        if the_person.sluttiness > 60:
            valid_titles.append("Danger Slut")        

        return valid_titles
