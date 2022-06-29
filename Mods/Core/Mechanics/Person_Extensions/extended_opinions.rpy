init 1 python:
    # extend existing opinions
    Person._opinions_list.append("yoga")

    # extend existing sexy opinions
    Person._sexy_opinions_list.append("threesomes")

    # insert opinions (note: used by wardrobe builder)
    Person._opinions_list.insert(7, "boots")
    Person._opinions_list.insert(10, "high heels")
    Person._opinions_list.insert(13, "dresses")

    # insert colours (note: used in colour map of wardrobe builder)
    Person._opinions_list.insert(15, "the colour green")
    Person._opinions_list.insert(15, "the colour purple")
    Person._opinions_list.insert(15, "the colour white")
    Person._opinions_list.insert(15, "the colour orange")
    Person._opinions_list.insert(15, "the colour brown")
