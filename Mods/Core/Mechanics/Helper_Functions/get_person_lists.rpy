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
