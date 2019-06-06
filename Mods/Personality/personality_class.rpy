# Replacement for the Personality class the solves some shortcomings of the original implementation
# personalities don't need to be stored in the renpy storage (an instance gets saved when stored with a parent object that is a store object)
# add comparison so python comparison works based on personality_type_prefix

init -1 python:
    class Personality(): #How the character responds to various actions
        def __init__(self, personality_type_prefix, default_prefix = "relaxed",
            common_likes = None, common_dislikes = None, common_sexy_likes = None, common_sexy_dislikes = None,
            titles_function = None, possessive_titles_function = None, player_titles_function = None):

            self.personality_type_prefix = personality_type_prefix
            self.default_prefix = default_prefix

            self.titles_function = titles_function
            self.possessive_titles_function = possessive_titles_function
            self.player_titles_function = player_titles_function

            #These are the labels we will be trying to get our dialogue. If the labels do not exist we will get their defaults instead. A default should _always_ exist, if it does not our debug check will produce an error.
            self.response_label_ending = ["greetings", "sex_responses", "climax_responses", "clothing_accept", "clothing_reject", "clothing_review", "strip_reject", "sex_accept", "sex_obedience_accept", "sex_gentle_reject", "sex_angry_reject",
            "seduction_response", "seduction_accept_crowded", "seduction_accept_alone", "seduction_refuse", "flirt_response", "cum_face", "cum_mouth", "suprised_exclaim", "talk_busy",
            "improved_serum_unlock", "sex_strip", "sex_watch", "being_watched", "work_enter_greeting", "date_seduction"]

            self.response_dict = {}
            for ending in self.response_label_ending:
                if renpy.has_label(self.personality_type_prefix + "_" + ending):
                    self.response_dict[ending] = self.personality_type_prefix + "_" + ending
                else:
                    self.response_dict[ending] = self.default_prefix + "_" + ending

            #Establish our four classes of favoured likes and dislikes. Intensity (ie. love vs like, dislike vs hate) is decided on a person to person basis.
            if common_likes:
                self.common_likes = common_likes
            else:
                self.common_likes = []

            if common_sexy_likes:
                self.common_sexy_likes = common_sexy_likes
            else:
                self.common_sexy_likes = []

            if common_dislikes:
                self.common_dislikes = common_dislikes
            else:
                self.common_dislikes = []

            if common_sexy_dislikes:
                self.common_sexy_dislikes = common_sexy_dislikes
            else:
                self.common_sexy_dislikes = []

        def __cmp__(self,other): ##This and __hash__ are defined so that I can use "if Action in List" and have it find identical actions that are different instances.
            if isinstance(other, Personality):
                if self.personality_type_prefix == other.personality_type_prefix:
                    return 0

            if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                return -1
            else:
                return 1

        def __hash__(self):
            return hash(self.personality_type_prefix)

        def get_dialogue(self, the_person, type, **extra_args):
            renpy.call(self.response_dict[type], the_person, **extra_args)

        def generate_default_opinion(self):
            if renpy.random.randint(1,2) == 1:
                #Positive
                degree = renpy.random.randint(1,2)
                the_key = get_random_from_list(self.common_likes)
                return (the_key,[degree,False])

            else:
                #Negative
                degree = renpy.random.randint(-2,-1)
                the_key = get_random_from_list(self.common_dislikes)
                return (the_key,[degree,False])


        def generate_default_sexy_opinion(self):
            if renpy.random.randint(1,2) == 1:
                #Positive
                degree = renpy.random.randint(1,2)
                the_key = get_random_from_list(self.common_sexy_likes)
                return (the_key,[degree,False])

            else:
                #Negative
                degree = renpy.random.randint(-2,-1)
                the_key = get_random_from_list(self.common_sexy_dislikes)
                return (the_key,[degree,False])

        def get_personality_titles(self, the_person): #This should be a function defined for each
            if self.titles_function:
                return self.titles_function(the_person)
            else:
                return the_person.name

        def get_personality_possessive_titles(self, the_person):
            if self.possessive_titles_function:
                return self.possessive_titles_function(the_person)
            else:
                return the_person.name

        def get_personality_player_titles(self, the_person):
            if self.player_titles_function:
                return self.player_titles_function(the_person)
            else:
                return the_person.name