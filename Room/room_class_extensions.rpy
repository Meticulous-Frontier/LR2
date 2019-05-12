init -1 python:
    def get_strangers(self):
        result = []
        for person in self.people:
            if person.mc_title == "Stranger":
                result.append(person)
        return result

    Room.get_strangers = get_strangers

    def get_known_people(self):
        result = []
        for person in self.people:
            if person.mc_title != "Stranger":
                result.append(person)
        return result

    Room.get_known_people = get_known_people