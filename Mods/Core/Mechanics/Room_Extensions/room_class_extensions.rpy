init -1 python:
    def assign_room_label(room, label_name): # Call labels through renpy.call(room.labels[0]) or through a for loop.
        if label_name not in room.labels:    # NOTE: This can be considered a useless function OR a shortcut to calling labels without having to go through Actions.
            room.labels.append(label_name)
        return "Label added"

    Room.assign_room_label = assign_room_label

    ###########################################
    # Custom Compare Functions For Room Class #
    ###########################################
    def room_compare(self, other):
        if isinstance(self, other.__class__):
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
    Room.hash = room_hash

    def room_eq(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name
        return False

    Room.__eq__ = room_eq

    def room_ne(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name
        return True

    Room.__ne__ = room_ne

    #################################
    # Extend Default Room Functions #
    #################################

    # extend the default move_person function
    def move_person_extended(org_func):
        def move_person_wrapper(room, person, destination):
            # run original function
            org_func(room, person, destination)
            # run extension code
            if not room is destination and destination is gym:  # people change clothes when going to the gym
                person.apply_gym_outfit()
            if not room is destination and destination is university and not person is nora: # people wear university uniform
                person.apply_university_outfit()

        return move_person_wrapper

    Room.move_person = move_person_extended(Room.move_person)


    ########################
    # Added Room Functions #
    ########################
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

        if not room.has_object_with_trait("Stand"): # Was creating a standing object for each room on every save reload
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

    # Adds an action to the room if not already present. Used with PolicyMod.
    def add_action(self, act): 
        if act not in self.actions:
            self.actions.append(act)

    Room.add_action = add_action

    # Remove an action from if present
    def remove_action(self, act):
        if isinstance(act, basestring):
            found = find_in_list(lambda x: x.effect == act, self.actions)
            if found:
                self.actions.remove(found)

        if act in self.actions:
            self.actions.remove(act)

    Room.remove_action = remove_action
