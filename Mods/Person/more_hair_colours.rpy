# More Hair Colors Mod by Tristimdorion
# Generates extra hair colours when creating random people 

init -1 python:
    # add some new haircolors to the default list (leave out the extreme colors)
    list_of_hairs.append("alt blond")
    list_of_hairs.append("light grey")
    list_of_hairs.append("ash brown")
    list_of_hairs.append("knight red")
    list_of_hairs.append("platinum blonde")
    list_of_hairs.append("golden blonde")
    list_of_hairs.append("strawberry blonde")
    list_of_hairs.append("light auburn")
    list_of_hairs.append("pulp")
    list_of_hairs.append("light brown")

    def update_hair_colour(person):
        if person.hair_colour == "alt blond":
            person.hair_style.colour = [0.882, 0.733, 0.580,1]
        if person.hair_colour == "light grey":
            person.hair_style.colour = [0.866, 0.835, 0.862,1]
        if person.hair_colour == "ash brown":
            person.hair_style.colour = [0.590, 0.473, 0.379,1]
        if person.hair_colour == "knight red":
            person.hair_style.colour = [0.745, 0.117, 0.235,1]
        if person.hair_colour == "platinum blonde":
            person.hair_style.colour = [0.789, 0.746, 0.691,1]
        if person.hair_colour == "golden blonde":
            person.hair_style.colour = [0.895, 0.781, 0.656,1]
        if person.hair_colour == "strawberry blonde":
            person.hair_style.colour = [0.644, 0.418, 0.273,1]
        if person.hair_colour == "light auburn":
            person.hair_style.colour = [0.566, 0.332, 0.238,1]
        if person.hair_colour == "pulp":
            person.hair_style.colour = [0.643, 0.439, 0.541,1]
        if person.hair_colour == "light brown":
            person.hair_style.colour = [0.652, 0.520, 0.414,1]

init 5 python:
    add_label_hijack("normal_start", "update_hair_colours")

label update_hair_colours(stack):
    python:
        people = all_people_in_the_game([mc])
        for person in people:
            update_hair_colour(person)

        execute_hijack_call(stack)
    return