init -1 python:
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
            if not person.follow_mc and not room is destination:
                if person.location == gym:
                    person.apply_gym_outfit()
                elif person.location == university and not person is nora:
                    person.apply_university_outfit()
                else:
                    person.apply_planned_outfit()
            return

        return move_person_wrapper

    Room.move_person = move_person_extended(Room.move_person)

    def show_background_extended(org_func):
        def show_background_wrapper(room):
            org_func(room)
            renpy.with_statement(Dissolve(.5, alpha = False))
            return

        return show_background_wrapper

    Room.show_background = show_background_extended(Room.show_background)

    ########################
    # Added Room Functions #
    ########################
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
        # add the mall and all it's connections
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
        # special character aunt and cousin locations
        if person in [aunt, cousin]:
            add_location(aunt_apartment)
            for c in aunt_apartment.connections:
                add_location(c)

        return possible_locations

    # Adds an action to the room if not already present. Used with PolicyMod.
    def add_action(self, action):
        found = next((x for x in self.actions if x.effect == action.effect), None)
        if not found:
            self.actions.append(action)

    Room.add_action = add_action

    # Remove an action from if present
    def remove_action(self, action):
        found = None
        if isinstance(action, Action):
            found = next((x for x in self.actions if x == action), None)
        elif isinstance(action, basestring):
            found = next((x for x in self.actions if x.effect == action), None)

        if found:
            self.actions.remove(found)

    Room.remove_action = remove_action

    def remove_object(self, the_object):
        if isinstance(the_object, basestring):
            found = ((x for x in self.objects if x.name == the_object), None)
            if found:
                self.objects.remove(found)

        if the_object in self.objects:
            self.objects.remove(the_object)

    Room.remove_object = remove_object

    #Functions to get specific people from a location

    def has_cum_slut(self):
        return get_random_from_list([x for x in self.people if x.has_cum_fetish()])

    def has_anal_slut(self):
        return get_random_from_list([x for x in self.people if x.has_anal_fetish()])

    def has_breeder(self):
        return get_random_from_list([x for x in self.people if x.has_breeding_fetish()])

    def has_exhibitionist(self):
        return get_random_from_list([x for x in self.people if x.has_exhibition_fetish()])

    Room.has_cum_slut = has_cum_slut
    Room.has_anal_slut = has_anal_slut
    Room.has_breeder = has_breeder
    Room.has_exhibitionist = has_exhibitionist

    #Room privacy levels. Useful for public interactions.
    #Levels:
    # 0: Private room. Sex and nudity permitted
    # 1: Public nudity room. Place where nudity would be expected but not overt sexual acts.
    # 2: Business. Use for work rooms, possibly changing permissions based on policies
    # 3: Public. Use for normal public areas. Nudity and sex not expected or permitted

    def get_room_privacy(self):
        if not hasattr(self, "_privacy_int"):
            self._privacy_int = 0
        return self._privacy_int

    def set_room_privacy(self, value):
        self._privacy_int = value

    def del_room_privacy(self):
        del self._privacy_int


    Room.privacy_level = property(get_room_privacy, set_room_privacy, del_room_privacy, "Expected privacy of the room.")

    def is_private(self):
        return self.privacy_level == 0

    Room.is_private = is_private

    def room_average_slut(self):
        if len(self.people) == 0:
            return 0
        sum = 0
        for person in self.people:
            sum += person.sluttiness
        return int(sum / len(self.people))

    Room.room_average_slut = room_average_slut
