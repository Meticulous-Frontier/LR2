
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