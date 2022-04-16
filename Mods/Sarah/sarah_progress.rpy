init 10 python:
    # sarah_story_dict = {}

    #First, setup the love storyline hints and functions.

    def sarah_story_20_love_hint():
        if sarah.love < 20:
            return "Try increasing [sarah.title]'s Love score."
        if sarah.sluttiness < 20:
            return "Try increasing [sarah.title]'s sluttiness."
        else:
            return "[sarah.title] may ask you out if you are working on a Saturday."

    def sarah_story_20_love_complete_func():
        return sarah.event_triggers_dict.get("drinks_out_progress",0) > 0

    def sarah_story_40_love_hint():
        if sarah_epic_tits_progress() == 1:
            return "Wait and see how her tits look on Monday."
        if sarah.love < 40:
            return "Try increasing [sarah.title]'s Love score."
        if sarah.sluttiness < 40:
            return "Try increasing [sarah.title]'s sluttiness."
        if get_HR_director_tag("business_HR_sexy_meeting", False) != True:
            return "Progress [sarah.title]'s lust story."
        else:
            return "[sarah.title] may ask you out again if you are working on a Saturday."

    def sarah_story_40_love_complete_func():
        return sarah.event_triggers_dict.get("drinks_out_progress",0) > 1

    def sarah_story_60_love_hint():
        if sarah_epic_tits_progress() < 2 and not sarah_epic_tits_progress() == -1:
            return "Progress [sarah.title]'s lust story."
        if strip_club_is_closed():
            return "Progress buying the strip club storyline."
        if sarah.love < 60:
            return "Try increasing [sarah.title]'s Love score."
        if sarah.sluttiness < 50:
            return "Try increasing [sarah.title]'s sluttiness."
        else:
            return "[sarah.title] may ask you out again if you are working on a Saturday."

    def sarah_story_60_love_complete_func():
        return sarah.event_triggers_dict.get("stripclub_progress",0) > 0

    def sarah_story_80_love_hint():
        if sarah.love < 80:
            return "Try increasing [sarah.title]'s Love score."
        if sarah.sluttiness < 60:
            return "Try increasing [sarah.title]'s sluttiness."
        if sarah != mc.business.hr_director:
            return "[sarah.title] must be your HR Director to progress this story."
        else:
            return "[sarah.title] will give you a special service during your Monday morning meeting soon."

    def sarah_story_80_love_complete_func():
        return get_HR_director_unlock("anal lapdance")

    def sarah_story_100_love_hint():
        return "This story is complete for now..."

    def sarah_story_100_love_complete_func():
        return False

    #### Copy and paste these for the other 4 love story events.

    def sarah_story_20_lust_hint():
        if sarah.sluttiness < 20:
            return "Try increasing [sarah.title]'s sluttiness."
        else:
            return "Look for [sarah.title] at the gym on the weekend."

    def sarah_story_20_lust_complete_func():
        return sarah.event_triggers_dict.get("yoga_voyeur",False)

    def sarah_story_40_lust_hint():
        if sarah != mc.business.hr_director:
            return "[sarah.title] must be your HR Director to progress this story."
        if sarah.sluttiness < 40:
            return "Try increasing [sarah.title]'s sluttiness."
        else:
            return "[sarah.title] has a surprise for you during your Monday HR meeting."

    def sarah_story_40_lust_complete_func():
        return get_HR_director_unlock("blowjob")

    def sarah_story_tit_serum_hint():
        if not mc.business.is_trait_researched(breast_enhancement):
            return "Try researching breast enhancement serums to progress this story."
        else:
            return "[sarah.title] seemed very intested in the breast enhancement serums. Wait for her to steal some."

    def sarah_story_tit_serum_complete_func():
        if sarah_epic_tits_progress() < 2 and not sarah_epic_tits_progress() == -1:
            return False
        return True

    def sarah_story_60_lust_hint():
        if sarah.sluttiness < 20:
            return "Try increasing [sarah.title]'s sluttiness."
        else:
            return "Look for [sarah.title] at the gym on the weekend."

    def sarah_story_60_lust_complete_func():
        return sarah.event_triggers_dict.get("gym_tshirt",False)

    def sarah_story_80_lust_hint():
        if sarah.event_triggers_dict.get("initial_threesome_target", None) != None:
            return "Arrange the threesome with the person you chose."
        if sarah.sluttiness < 80:
            return "Try increasing [sarah.title]'s sluttiness."
        if __builtin__.len(get_Sarah_willing_threesome_list()) <= 3:
            return "Not enough possible threesome partners. Try increasing more girl's sluttiness to at least 80."
        else:
            return "Look for [sarah.title] at work on Saturdays."

    def sarah_story_80_lust_complete_func():
        return sarah_threesomes_unlocked()

    def sarah_story_100_lust_complete_func():
        return False

    def sarah_story_100_lust_hint():
        return "This story is complete for now..."

    #### Copy and paste these for the 4 other lust events.

    def sarah_story_teamup_1_hint():
        if erica.event_triggers_dict.get("yoga_quest_started", False) == False:
            return "Try progressing [erica.title]'s story."
        if len(erica_get_yoga_class_list()) < 4:
            return "Help [sarah.title] convince employees to like or love yoga."
        else:
            return "Talk to [erica.title] about hosting a company yoga class."

    def sarah_story_teamup_1_complete_func():
        return erica_get_is_doing_yoga_sessions()

    #### Repeat this for all different teamups.

    def sarah_story_other_information_func():    #Return a list of strings to be presented in Other Information
        other_info_list = []
        if sarah is mc.business.hr_director:
            other_info_list.append("[sarah.title] is your HR Director")
        else:
            other_info_list.append("[sarah.title] needs to be your HR director to progress most story options.")
        if Sarah_has_bigger_tits():
            other_info_list.append("[sarah.title] took serums to make her breasts bigger.")
        if sarah_get_special_titfuck_unlocked():
            other_info_list.append("[sarah.title] gives amazing tit fucks!")
        return other_info_list


    def sarah_story_build_dict():

        sarah_story_dict = {}

        sarah_story_dict["description"] = "A long lost childhood friend. Maybe you can spark a flame with her."

        #Build Love Story
        love_story_list = []
        if sarah_story_20_love_complete_func():
            love_story_list.append("[sarah.title] enjoyed your first date at the bar.")
            if sarah_story_40_love_complete_func():
                love_story_list.append("[sarah.title] enjoyed your second date at the bar.")
                if sarah_story_60_love_complete_func():
                    love_story_list.append("[sarah.title] took you to the strip club.")
                    if sarah_story_80_love_complete_func():
                        love_story_list.append("[sarah.title] gave you her ass during a Monday meeting!")
                        if sarah_story_100_love_complete_func():
                            pass
                        else:
                            love_story_list.append(sarah_story_100_love_hint())
                    else:
                        love_story_list.append(sarah_story_80_love_hint())
                else:
                    love_story_list.append(sarah_story_60_love_hint())
            else:
                love_story_list.append(sarah_story_40_love_hint())
        else:
            love_story_list.append(sarah_story_20_love_hint())

        sarah_story_dict["love_story"] = love_story_list

        #Lust story

        lust_story_list = []
        if sarah_story_20_lust_complete_func():
            lust_story_list.append("[sarah.title] enjoyed when you watched her do yoga at the gym.")
            if sarah_story_40_lust_complete_func():
                lust_story_list.append("[sarah.title] gave you a blowjob in your office!")
                if sarah_story_tit_serum_complete_func():
                    lust_story_list.append("[sarah.title] stole breast enhancing serums and used them!")
                    if sarah_story_60_lust_complete_func():
                        lust_story_list.append("[sarah.title] turned a gym session into a lewd show!")
                        if sarah_story_80_lust_complete_func():
                            lust_story_list.append("[sarah.title] finally had her first threesome.")
                            if sarah_story_100_lust_complete_func():
                                pass
                            else:
                                lust_story_list.append(sarah_story_100_lust_hint())
                        else:
                            lust_story_list.append(sarah_story_80_lust_hint())
                    else:
                        lust_story_list.append(sarah_story_60_lust_hint())
                else:
                    lust_story_list.append(sarah_story_tit_serum_hint())
            else:
                lust_story_list.append(sarah_story_40_lust_hint())
        else:
            lust_story_list.append(sarah_story_20_lust_hint())

        sarah_story_dict["lust_story"] = lust_story_list

        #Teamup stories

        teamup_story_list = []
        if sarah_story_teamup_1_complete_func():
            teamup_story_list.append("Watch [sarah.title] do yoga with [erica.title] every Tuesday morning at the office!")
        else:
            teamup_story_list.append(sarah_story_teamup_1_hint())

        sarah_story_dict["teamup_list"] = teamup_story_list

        sarah_story_dict["other_info"] = sarah_story_other_information_func()

        return sarah_story_dict

    def sarah_story_love_list():
        love_story_list = []
        if sarah_story_20_love_complete_func():
            love_story_list.append("[sarah.title] enjoyed your first date at the bar.")
            if sarah_story_40_love_complete_func():
                love_story_list.append("[sarah.title] enjoyed your second date at the bar.")
                if sarah_story_60_love_complete_func():
                    love_story_list.append("[sarah.title] took you to the strip club.")
                    if sarah_story_80_love_complete_func():
                        love_story_list.append("[sarah.title] gave you her ass during a Monday meeting!")
                        if sarah_story_100_love_complete_func():
                            pass
                        else:
                            love_story_list.append(sarah_story_100_love_hint())
                    else:
                        love_story_list.append(sarah_story_80_love_hint())
                else:
                    love_story_list.append(sarah_story_60_love_hint())
            else:
                love_story_list.append(sarah_story_40_love_hint())
        else:
            love_story_list.append(sarah_story_20_love_hint())
        return love_story_list

    def sarah_story_lust_list():
        lust_story_list = []
        if sarah_story_20_lust_complete_func():
            lust_story_list.append("[sarah.title] enjoyed when you watched her do yoga at the gym.")
            if sarah_story_40_lust_complete_func():
                lust_story_list.append("[sarah.title] gave you a blowjob in your office!")
                if sarah_story_tit_serum_complete_func():
                    lust_story_list.append("[sarah.title] stole breast enhancing serums and used them!")
                    if sarah_story_60_lust_complete_func():
                        lust_story_list.append("[sarah.title] turned a gym session into a lewd show!")
                        if sarah_story_80_lust_complete_func():
                            lust_story_list.append("[sarah.title] finally had her first threesome.")
                            if sarah_story_100_lust_complete_func():
                                pass
                            else:
                                lust_story_list.append(sarah_story_100_lust_hint())
                        else:
                            lust_story_list.append(sarah_story_80_lust_hint())
                    else:
                        lust_story_list.append(sarah_story_60_lust_hint())
                else:
                    lust_story_list.append(sarah_story_tit_serum_hint())
            else:
                lust_story_list.append(sarah_story_40_lust_hint())
        else:
            lust_story_list.append(sarah_story_20_lust_hint())

        return lust_story_list

    def sarah_story_teamup_list():
        teamup_story_list = []
        if sarah_story_teamup_1_complete_func():
            teamup_story_list.append([erica,"Watch [sarah.title] do yoga with [erica.title] every Tuesday morning at the office!"])
        else:
            teamup_story_list.append([erica,sarah_story_teamup_1_hint()])
        return teamup_story_list

    def sarah_story_other_list():
        other_info_list = []
        if sarah is mc.business.hr_director:
            other_info_list.append("[sarah.title] is your HR Director")
        else:
            other_info_list.append("[sarah.title] needs to be your HR director to progress most story options.")
        if Sarah_has_bigger_tits():
            other_info_list.append("[sarah.title] took serums to make her breasts bigger.")
        if sarah_get_special_titfuck_unlocked():
            other_info_list.append("[sarah.title] gives amazing tit fucks!")
        return other_info_list
