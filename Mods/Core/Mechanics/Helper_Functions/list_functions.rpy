
init -2 python:
    # splits a item_array in even chunks of blok_size
    def split_list_in_blocks(list, blok_size):
        for i in __builtin__.range(0, __builtin__.len(list), blok_size):
            yield list[i:i + blok_size]

    # splits an item_array in a number of blocks about equal in size (remainders are added to last block)
    def split_list_in_even_blocks(list, blok_count):
        avg = __builtin__.len(list) / float(blok_count)
        result = []
        last = 0.0

        while last < __builtin__.len(list):
            result.append(list[__builtin__.int(last):__builtin__.int(last + avg)])
            last += avg

        return result

    # finds an item in a list, where search(item) == True
    # search as lambda could be a lambda ==> x: x.name == 'searchname'
    def find_in_list(search, list):
        return next((x for x in list if search(x)), None)

    def find_in_set(obj, in_set):
        return next((x for x in in_set if x == obj), None)

    # finds all qualifying items in list and returns them as a smaller list.
    def find_items_in_list(search, list):
        items = [x for x in list if search(x)]
        if items:
            return items
        return None

    def simple_list_format(list_to_format, what_to_format, string = "", ignore = "", attrib = ""): # Returns a simple list for use in generic menus. Extensive use in the Biotech Actions.
        tuple_list = []                                                    # NOTE: Needed a generic list setup, this seems to cover most usecases I came across.
        for what_to_format in list_to_format:
            if what_to_format is not ignore:

                if attrib is not "":
                    tuple_string = str(string) + str(vars(what_to_format)[attrib]) # e.g attrib = "name" for SerumTrait.name to be displayed
                    tuple_list.append([tuple_string, what_to_format])

                else:
                    tuple_string = str(string) + str(what_to_format)
                    tuple_list.append([tuple_string, what_to_format])
            else:
                tuple_string = str(what_to_format)
                tuple_list.append([tuple_string, what_to_format])
        return tuple_list

    def sort_display_list_extra(the_item): #Function to use when sorting lists of actions (and potentially people or strings)
        extra_args = None
        if isinstance(the_item, list): #If it's a list it's actually an item of some sort with extra args. Break those out and continue.
            extra_args = the_item[1]
            the_item = the_item[0]

        if isinstance(the_item, Action):
            if the_item.is_action_enabled(extra_args):
                return the_item.priority
            else:
                return the_item.priority - 1000 #Apply a ranking penalty to disabled items. They will appear in priority order but below enabled events (Unless something has a massive priority).

        elif isinstance(the_item, Person):
            return the_item.name #Order people by name

        else:
            return 0

    # get a sorted list of people to use with main_choice_display
    def get_sorted_people_list(list_of_people, title, back_extension = None, reverse = False):
        list_of_people.sort(key = sort_display_list_extra, reverse = reverse)
        list_of_people.insert(0, title)
        if not back_extension is None:
            list_of_people.extend(["Back"])
        return list_of_people

init -1 python:
        def get_random_from_list(list):
            if list:
                return renpy.random.choice(list)
            return None
