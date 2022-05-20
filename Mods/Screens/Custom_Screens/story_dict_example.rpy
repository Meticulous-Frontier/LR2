#### This file gives an example of all the of the required and optional contents of a story dict.
#### Thie file can be copy pasted to give a template of a story dict to give hints for a new character.

init 10 python:
    test_story_dict = {}

    #First, setup the love storyline hints and functions.

    def test_story_20_love_hint():  #Use a requirement style system to return hints as necessary.
        return "Trying talking to her a lot! She likes small talk."

    def test_story_20_love_complete_func():  #Probably some sort of story variable gets set if you completed an event.
        return the_person.love>20

    #### Copy and paste these for the other 4 love story events.

    def test_story_20_lust_hint():
        return "Try flirting! There are multiple ways to increase her sluttiness."

    def test_story_20_lust_complete_func():
        return the_person.sluttiness>20

    #### Copy and paste these for the 4 other lust events.

    def test_story_teamup_1_hint():
        return "Progress [erica.title]'s story to unlock a teamup!"

    def test_story_teamup_1_complete_func():
        return the_person.sluttiness>20


    #### Repeat this for all different teamups.

    def test_story_other_information_func():    #Return a list of strings to be presented in Other Information
        if the_person == mc.business.hr_director:
            return "Is your HR Director"
        return []


    def test_story_build_dict(the_person):

        test_story_dict["description"] = "A long lost childhood friend. Maybe you can spark a flame with her."

        #Build Love Story
        love_story_list = []
        if test_story_20_love_complete_func():
            love_story_list.append("She enjoyed your date at the bar.")
            if test_story_40_love_complete_func():
                love_story_list.append("She enjoyed your second date at the bar.")
                #TODO is there a better way to do this than to just nest 5 if else statements?
            else:
                love_story_list.append(test_story_40_love_hint())
        else:
            love_story_list.append(test_story_20_love_hint())

        test_story_dict["love_story"] = love_story_list

        #Lust story

        lust_story_list = []
        if test_story_20_lust_complete_func():
            lust_story_list.append("She enjoyed when you watched her do yoga at the gym.")
            if test_story_40_lust_complete_func():
                lust_story_list.append("She stole breast enhancing serums and used them!")
                #TODO is there a better way to do this than to just nest 5 if else statements?
            else:
                lust_story_list.append(test_story_40_lust_hint())
        else:
            lust_story_list.append(test_story_20_lust_hint())

        test_story_dict["lust_story"] = lust_story_list

        #Teamup stories

        teamup_story_list = []
        if test_story_teamup_1_complete_func():
            teamup_story_list.append("Watch her do yoga with [erica.title] every Tuesday morning at the office!")
        else:
            teamup_story_list.append(test_story_teamup_1_hint())



        test_story_dict["teamup_list"] = teamup_story_list

        test_story_dict["other_info"] = test_story_other_information_func

        return test_story_dict
