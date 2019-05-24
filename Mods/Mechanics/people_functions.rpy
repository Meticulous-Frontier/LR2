init -1 python:
    def all_people_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily]
        all_people = []
        for location in list_of_places:
            for person in location.people:
                if person not in excluded_people:
                    all_people.append(person)
        return all_people

    def get_random_person_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily]
        all_people = all_people_in_the_game(excluded_people)
        return get_random_from_list(all_people)

    def known_people_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily]
        known_people = []
        for location in list_of_places:
            for person in location.people:
                if person not in excluded_people:
                    if person.mc_title != "Stranger":
                        known_people.append(person)
        return known_people

    def get_random_known_person_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily]
        known_people = known_people_in_the_game(excluded_people)
        return get_random_from_list(known_people)
