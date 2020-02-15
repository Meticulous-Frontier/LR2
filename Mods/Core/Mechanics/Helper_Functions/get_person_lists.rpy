init -1 python:
    def all_people_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        all_people = []
        for location in list_of_places:
            for person in location.people:
                if person not in excluded_people:
                    all_people.append(person)
        return all_people

    def get_random_person_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        all_people = all_people_in_the_game(excluded_people)
        return get_random_from_list(all_people)

    def known_people_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        known_people = []
        for location in list_of_places:
            known_people += known_people_at_location(location, excluded_people)
        return known_people

    def get_random_known_person_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        known_people = known_people_in_the_game(excluded_people)
        return get_random_from_list(known_people)

    def known_people_at_location(location, excluded_people = []):
        known_people = []
        for person in location.people:
            if person not in excluded_people:
                if person.mc_title != "Stranger":
                    known_people.append(person)
        return known_people

    def unknown_people_at_location(location, excluded_people = []):
        unknown_people = []
        for person in location.people:
            if person not in excluded_people:
                if person.mc_title == "Stranger":
                    unknown_people.append(person)
        return unknown_people

    def people_in_mc_home():
        return hall.people + bedroom.people + lily_bedroom.people + mom_bedroom.people + kitchen.people

    def people_in_role(role):
        all_people = all_people_in_the_game([mc])
        return [x for x in all_people if role in x.special_role]

    # returns a single employee when number of employees == 1
    # returns a tuple of employees when number of employees > 1
    def get_random_employees(number_of_employees, exclude_list = None, **employee_args):
        result = set([])
        list_of_possible_people = mc.business.get_requirement_employee_list(exclude_list = exclude_list, **employee_args)
        for i in range(number_of_employees):
            person = get_random_from_list(list_of_possible_people)
            result.add(person)
            list_of_possible_people.remove(person)

        if number_of_employees == 1:
            return list(result)[0]

        return tuple(result)