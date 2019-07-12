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

    def assign_room_label(room, label_name): # Call labels through renpy.call(room.labels[0]) or through a for loop.
        if label_name not in room.labels:    # NOTE: This can be considered a useless function OR a shortcut to calling labels without having to go through Actions.
            room.labels.append(label_name)
        return "Label added"

    Room.assign_room_label = assign_room_label


    # add room compare function
    def room_compare(self, other):
        if isinstance(other, Room):
            if self.name == other.name:
                return 0

        if self.__hash__() < other.__hash__():
            return -1
        else:
            return 1

    Room.__cmp__ = room_compare            

    # add room hash function
    def room_hash(self):
        return hash(self.name)

    Room.__hash__ = room_hash