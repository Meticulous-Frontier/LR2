init 1310 python:
    def reserved_titles(the_person):
        valid_titles = []
        valid_titles.append("Mrs. " + the_person.last_name)
        if the_person.love > 30:
            valid_titles.append(the_person.name)
        if the_person.sluttiness > 40:
           valid_titles.append("Serene Bitch")
        if the_person.sluttiness > 60:
            valid_titles.append("Cold Slut")        

        return valid_titles

    def reserved_player_titles(the_person):
        valid_titles = []
        valid_titles.append("Mr. " + mc.last_name)
        if the_person.love > 30:
            valid_titles.append(mc.name)
        return valid_titles