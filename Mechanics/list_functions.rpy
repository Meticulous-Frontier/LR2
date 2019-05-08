
init -2 python:
    # splits a item_array in even chunks of blok_size
    def split_list_in_blocks(list, blok_size):
        for i in range(0, len(list), blok_size):
            yield list[i:i + blok_size]


    # finds an item in a list, where search(item) == True
    # search as lambda could be a lambda ==> x: x.name == 'searchname'
    def find_in_list(search, list):
        for item in list:
            if search(item):
                return item
        return None

    def simple_list_format(list_to_format, what_to_format, string = ""): # Returns a simple list for use in generic menus. Extensive use in the Biotech Actions.
        tuple_list = []                                                    # NOTE: Needed a generic list setup, this seems to cover most usecases I came across.
        for what_to_format in list_to_format:
            tuple_string = str(string) + str(what_to_format)
            tuple_list.append([tuple_string, what_to_format])
        return tuple_list

    def format_person_list(list_of_people, draw_hearts = False):  # Re-added this incase we dont want to redo all the lists (removed from game in v0.16.1)

        tuple_list = []
        for person in list_of_people:
            tuple_string = format_titles(person)

            if draw_hearts:
                tuple_string += "\n"
                tuple_string += get_heart_image_list(person)

            tuple_list.append([
                tuple_string,person])
        return tuple_list
