init -1 python:
    from lru import lru_cache_function
    from lru import LRUCacheDict

    def all_people_in_the_game(excluded_people = [], excluded_locations = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        all_people = set()
        for location in all_locations_in_the_game(excluded_locations):
            all_people.update([x for x in location.people if not x in excluded_people])
        return list(all_people)

    def all_locations_in_the_game(excluded_locations = []):
        return [x for x in list_of_places if not x in excluded_locations]

    def get_random_person_in_the_game(excluded_people = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        return renpy.random.choice(all_people_in_the_game(excluded_people))

    def get_random_person_in_location(location, excluded_people = []):
        return get_random_from_list([x for x in location.people if not x in excluded_people])

    @lru_cache_function(max_size=1, expiration=5)
    def unique_characters_not_known(): # TODO The check should be standardized, but some people are vanilla, some are different modders or different 'style'.
        not_met_yet_list = []
        if alexia.get_destination(specified_time = 1) == alexia.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(alexia)
        if "ashley" in globals() and ashley.employed_since == -1:
            not_met_yet_list.append(ashley)
        if "candace" in globals() and candace.event_triggers_dict.get("met_at_store", 0) == 0: # She exist but not met yet.
            not_met_yet_list.append(candace)
        if christina.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(christina)
        if "dawn" in globals() and dawn.event_triggers_dict.get("met", 0) == 0:
            not_met_yet_list.append(dawn)
        if emily.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(emily)
        if "erica" in globals() and erica_get_progress() == 0:
            not_met_yet_list.append(erica)
        if cousin.get_destination(specified_time = 1) == cousin.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(cousin)
        if nora.get_destination(specified_time = 1) == nora.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(nora)
        if "salon_manager" in globals() and salon_manager.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(salon_manager)
        if aunt.get_destination(specified_time = 2) == aunt_bedroom: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(aunt)
        if "sarah" in globals() and sarah.event_triggers_dict.get("first_meeting", False) == False: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(sarah)
        if "starbuck" in globals() and starbuck.event_triggers_dict.get("starbuck_intro_complete", False) == False:
            not_met_yet_list.append(starbuck)
        if "camilla" in globals() and camilla.mc_title == 'Stranger':
            not_met_yet_list.append(camilla)
        if "kaya" in globals() and kaya.mc_title == 'Stranger':
            not_met_yet_list.append(kaya)
        if "sakari" in globals() and sakari.mc_title == 'Stranger':
            not_met_yet_list.append(sakari)
        if "ellie" in globals() and ellie.mc_title == 'Stranger':
            not_met_yet_list.append(ellie)
        return not_met_yet_list

    @lru_cache_function(max_size=10, expiration=3)
    def known_people_in_the_game(excluded_people = [], excluded_locations = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        known_people = set()
        excluded = set(excluded_people)
        excluded.update(unique_characters_not_known())
        for location in all_locations_in_the_game(excluded_locations):
            known_people.update(known_people_at_location(location, excluded))
        return list(known_people)

    def known_people_at_location(location, excluded_people = []):
        excluded = set(excluded_people)
        excluded.update(unique_characters_not_known())
        return [x for x in location.people if x.is_available and not x in excluded and x.title and x.mc_title != "Stranger"]

    @lru_cache_function(max_size=3, expiration=3)
    def unknown_people_in_the_game(excluded_people = [], excluded_locations = []):
        unknown_people = set(unique_characters_not_known())
        for location in all_locations_in_the_game(excluded_locations):
            unknown_people.update(unknown_people_at_location(location, excluded_people))
        return list(unknown_people)

    def unknown_people_at_location(location, excluded_people = []):
        return [x for x in location.people if x.is_available and not x in excluded_people and (not x.title or x.mc_title == "Stranger")]

    def people_in_mc_home(excluded_people = []):
        return [x for x in hall.people + bedroom.people + lily_bedroom.people + mom_bedroom.people + kitchen.people if x.is_available and not x in excluded_people]

    def people_in_role(role):
        return [x for x in all_people_in_the_game() if x.has_role(role)]

    # returns a single employee when number of employees == 1
    # returns a tuple of employees when number of employees > 1
    # only returns employees available for events
    def get_random_employees(number_of_employees, exclude_list = None, **employee_args):
        result = set([])
        list_of_possible_people = [x for x in mc.business.get_requirement_employee_list(exclude_list = exclude_list, **employee_args) if x.is_available]
        if len(list_of_possible_people) < number_of_employees:
            if number_of_employees == 1:
                return None

            result.add(None) # build up tuple with correct number of items
            for i in __builtin__.range(1, number_of_employees):
                result.add(i)
            return tuple(result)

        for i in __builtin__.range(number_of_employees):
            person = get_random_from_list(list_of_possible_people)
            result.add(person)
            list_of_possible_people.remove(person)

        if number_of_employees == 1:
            return list(result)[0]

        return tuple(result)
