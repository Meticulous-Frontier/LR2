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

    def update_custom_rooms(room): # Replaces the room in the list with the updated version.
        room_update = find_in_list(lambda x: x.name == room.name, list_of_places)

        # did not find a room to update
        if not room_update:
            return

        # renpy.say("", "Update room " + room_update.name)

        room_update.formalName = room.formalName

        room_update.map_pos = room.map_pos
        room_update.background_image = room.background_image

        # room_update.visible = room.visible    DON'T UPDATE VISIBILITY
        room_update.accessable = room.accessable

        # room_update.connections = room.connections    DON'T UPDATE CONNECTIONS

        room_update.objects = room.objects
        room_update.objects.append(Object("stand",["Stand"], sluttiness_modifier = 0, obedience_modifier = -5)) #Add a standing position that you can always use.

        # update available actions in room
        room_update.actions = room.actions

        if room_update.tutorial_label != room.tutorial_label:
            room_update.tutorial_label = room.tutorial_label
            room_update.trigger_tutorial = True

        # old saves don't have hide_in_known_housemap
        if hasattr(room_update, "hide_in_known_housemap"): # Deal with this somehow else. Thought ModRooms should have the attribute as True by default?
            room_update.hide_in_known_housemap = room.hide_in_known_housemap

        return room_update

    def purchase_room_on_buy_function(room):
        room.visible = True

    # Build a location list where the person can be scheduled.
    def build_schedule_location_list(person):
        possible_locations = []

        def add_location(location, add_when_not_visible = False):
            if location.visible or add_when_not_visible:
                if not location in possible_locations:
                    possible_locations.append(location)

        # person home
        add_location(person.home, add_when_not_visible = True)
        # add the mall and all its connections
        add_location(mall)
        for c in mall.connections:
            add_location(c)
        # add employee locations
        if person.is_employee():
            add_location(lobby)
            for c in lobby.connections:
                add_location(c)
        # special character mom and lily locations
        if person in [mom, lily]:
            add_location(hall)
            for c in hall.connections:
                add_location(c)
        # special character aunt and cousing locations
        if person in [aunt, cousin]:
            add_location(aunt_apartment)
            for c in aunt_apartment.connections:
                add_location(c)

        return possible_locations
