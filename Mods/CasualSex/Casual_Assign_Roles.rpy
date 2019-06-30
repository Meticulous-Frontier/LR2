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
                    people.special_role.append(casual_athlete_role)
                    people.personality = athlete_personality
                    people.schedule[1] = gym
                    people.schedule[3] = gym

#        for (people,place) in people_to_process: #Figure out if person already has an important role
#            if people.special_role.len() == 0:   #Add new roles only if no current roles exist
#                if people.age < 30:
#                    people.special_role.append(casual_athlete_role)
        return
