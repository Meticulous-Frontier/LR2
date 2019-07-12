init -1 python:
    
    # Overwrites the room / location class to support comparison by name ( not formalName )
    class ModRoom(Room): # Sub- Class of Room that allows comparison so that it is easier to keep them updated without needing new saves.

        def __cmp__(self,other): ##This and __hash__ are defined so that I can use "if Room in List" and have it find identical actions that are different instances.
            if type(other) is ModRoom:
                if self.name == other.name:
                    return 0
                else:
                    if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                        return -1
                    else:
                        return 1
            else:
                if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                    return -1
                else:
                    return 1

        def __hash__(self):
            return hash((self.name))

    
    def change_scene_display(the_location): #Switch displayed location and background image
        renpy.scene("Active")
        renpy.show(the_location.name, what=the_location.background_image)
        return   

    def assign_room_label(room, label_name): # Call labels through renpy.call(room.labels[0]) or through a for loop.
        if label_name not in room.labels:    # NOTE: This can be considered a useless function OR a shortcut to calling labels without having to go through Actions.
            room.labels.append(label_name)
        return "Label added"

    Room.assign_room_label = assign_room_label

    def create_room_label_list(): #Assigns room.labels = [] to all rooms in list_of_places. So they can have labels assigned to them.
        for room in list_of_places: # NOTE: Going to be using the Room.actions list instead because I was too focused on trying to make something unessescary work when I created this.
            if hasattr(room, "labels") == False:
                room.labels = []


    def format_rooms(list_of_rooms, flavor = ""): # This can be kept as it formats rooms in a list for menu display.
        tuple_list = []
        for room in list_of_rooms:
            tuple_string = flavor + room.formalName
            tuple_list.append([tuple_string, room])
        return tuple_list

    def advance_time():
        renpy.call("advance_time")
        return

    def is_public():
        if mc.location.public == True:
            return True
        else:
            return False

    def is_accessable():
        if mc.location.accessable == True:
            return True
        else:
            return False

    def is_day(day_name):
        if dayname in day_names:
            return day % 7 == day_names.index(dayname)
        return False

    def is_time(time_name):
        if time_name in time_names:
            return time_of_day == time_names.index(time_name)
        return False
