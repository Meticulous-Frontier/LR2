#Blank for now#


init 2 python:
    #def casual_sex_mod_initialization(action_mod):
    def test_init_050():
        people_to_process = [] #Create a list of everyone
        for place in list_of_places:
            for people in place.people:
                people_to_process.append([people,place])

        for (people,place) in people_to_process: #Figure out if person already has an important role
            disqualifying_role = 0
            for role in people.special_role:
                if role == generic_people_role:
                    pass
                else:
                    disqualifying_role = 1
            if disqualifying_role == 0:         #Assign new casual sex roles#
                if people.age < 30:
                    assign_casual_athlete_role(people)
                    #people.special_role.append(casual_athlete_role)
                    #people.personality = athlete_personality
                    #people.schedule[1] = gym
                    #people.schedule[3] = gym

#        for (people,place) in people_to_process: #Figure out if person already has an important role
#            if people.special_role.len() == 0:   #Add new roles only if no current roles exist
#                if people.age < 30:
#                    people.special_role.append(casual_athlete_role)
        return

init 1302 python:
    def assign_casual_athlete_role(the_person):
        the_person.special_role.append(casual_athlete_role)
        local_athlete_personality = Personality("athlete", default_prefix = the_person.personality.personality_type_prefix,
        common_likes = [],
        common_sexy_likes = ["casual sex"],
        common_dislikes = ["relationships"],
        common_sexy_dislikes = [],
        titles_function = athlete_titles, possessive_titles_function = athlete_possessive_titles, player_titles_function = athlete_player_titles)
        the_person.personality = local_athlete_personality
        the_person.schedule[1] = gym
        the_person.schedule[3] = gym

        return

    def remove_casual_athlete_role(the_person):
        the_person.special_role.remove(casual_athlete_role)
        #"relaxed", "reserved", "wild", "introvert", "cougar"
        if the_person.personality.default_prefix == "relaxed":
            the_person.personality = relaxed_personality
        elif the_person.personality.default_prefix == "reserved":
            the_person.personality = reserved_personality
        elif the_person.personality.default_prefix == "wild":
            the_person.personality = wild_personality
        elif the_person.personality.default_prefix == "introvert":
            the_person.personality = introvert_personality
        elif the_person.personality.default_prefix == "cougar":
            the_person.personality = cougar_personality
        else:
            the_person.personality = relaxed_personality  #Catch all for personalities#

        the_person.schedule[1] = None    #Reset their schedule
        the_person.schedule[3] = None















        return
