
init -1 python:
    # splits a item_array in even chunks of blok_size
    def split_list_in_blocks(list, blok_size):
        for i in range(0, len(list), blok_size):
            yield list[i:i + blok_size]