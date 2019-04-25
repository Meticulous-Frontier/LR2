init -1 python:
    def all_people_in_the_game(excluded_people = None): # Pass excluded_people as array of people [mc, lily]
        all_people = []
        for location in list_of_places:
            for person in location.people:
                if person not in excluded_people:
                    all_people.append(person)
        return all_people

    def get_random_person_in_the_game(excluded_people = None): # Pass excluded_people as array of people [mc, lily]
        all_people = all_people_in_the_game(excluded_people)
        return get_random_from_list(all_people)        