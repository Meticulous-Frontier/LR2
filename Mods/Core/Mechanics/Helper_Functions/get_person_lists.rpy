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

    def get_random_person_in_location(location, excluded_people = []):
        return get_random_from_list([x for x in location.people if x not in excluded_people])

    def unique_characters_not_known(): # TODO The check should be standardized, but some people are vanilla, some are different modders or different 'style'.
        not_met_yet_list = []
        if alexia.schedule[1] == alexia.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(alexia)
        if ashley.event_triggers_dict.get("intro_complete") == False:
            not_met_yet_list.append(ashley)
        if not "candace" in globals(): # She's not been created yet.
            pass
        elif candace.event_triggers_dict.get("met_at_store") == 0: # She exist but not met yet.
            not_met_yet_list.append(candace)
        if christina.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(christina)
        if dawn.event_triggers_dict.get("met") == 0:
            not_met_yet_list.append(dawn)
        if emily.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(emily)
        if erica.event_triggers_dict.get("erica_progress") == 0:
            not_met_yet_list.append(erica)
        if cousin.schedule[1] == cousin.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(cousin)
        if nora.schedule[1] == nora.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(nora)
        if salon_manager.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(salon_manager)
        if aunt.schedule[2] == aunt_bedroom: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(aunt)
        if sarah.schedule[1] == sarah.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(sarah)
        if not starbuck.event_triggers_dict.get("starbuck_intro_complete"):
            not_met_yet_list.append(starbuck)
        return not_met_yet_list

    def known_people_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        known_people = []
        for location in list_of_places:
            known_people += known_people_at_location(location, excluded_people)
        return known_people

    def get_random_known_person_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        known_people = known_people_in_the_game(excluded_people)
        return get_random_from_list(known_people)

    def known_people_at_location(location, excluded_people = []):
        not_met_yet_list = unique_characters_not_known()
        known_people = []
        for person in [x for x in location.people if not x in excluded_people]:
            if not (person.mc_title == "Stranger" or not person.title) and not person in not_met_yet_list:
                known_people.append(person)
        return known_people

    def unknown_people_in_the_game(excluded_people = []):
        unknown_people = []
        for location in list_of_places:
            unknown_people += unknown_people_at_location(location, excluded_people)
        return unknown_people

    def unknown_people_at_location(location, excluded_people = []):
        unknown_people = []
        for person in [x for x in location.people if not x in excluded_people]:
            if person.mc_title == "Stranger" or not person.title:
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
        if len(list_of_possible_people) < number_of_employees:
            if number_of_employees == 1:
                return None
                
            result.add(None) # build up tuple with correct number of items
            for i in range(1, number_of_employees):
                result.add(i)
            return tuple(result)

        for i in range(number_of_employees):
            person = get_random_from_list(list_of_possible_people)
            result.add(person)
            list_of_possible_people.remove(person)

        if number_of_employees == 1:
            return list(result)[0]

        return tuple(result)