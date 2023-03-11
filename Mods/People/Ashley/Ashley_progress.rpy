init 10 python:
    #Prototypes for an easier way of managing story progress screens. Add an init function to attempt to retain global functionaliy

    def ashley_story_love_list():

        return ashley.love_messages

    def ashley_story_lust_list():
        return ashley.lust_messages

    def ashley_story_obedience_list():
        return ashley.obedience_messages

    def ashley_story_teamup_list():
        return [[stephanie, ashley.teamup_messages[0]], [lily, ashley.teamup_messages[1]]]

    def ashley_story_other_list():
        #Ashley's other story indices:
        # 0 - Her attempting to get MC obedient
        # 1 - Your arrangement with Stephanie
        # 2 - arousal serum quest
        return ashley.other_messages
