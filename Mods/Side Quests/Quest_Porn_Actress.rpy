#Mid game quest. Is available mid game, will help with profitability.
#Requires a couple of employees available for quests atleast 60+ sluttiness.
#Porn video circulates around the company of one of the employees in a porn video. Its a very popular video.
#MC approaches the porn star. Asks her to be moved to marketing.
#Girl is having trouble finding an actor for a new vid, says she will if MC helps her produce her next video.
#Make video
#Video gains popularity based on quality, determined by positions, # female orgasms, and unique cumshots.
#After, she joins marketting. While she is in marketting, gain a bonus to profitability.
#Gain the ability to "Shoot porn video" with her. Can be done once per week and brings in extra cash.
#Once complete, can refer to girl as porn star, slight personality tweek.

# flags
# 1: Quest has been initiated
# 11: MC has seen video.
# 19: MC makes memo not to bother girl about making porn. (Bad End)
# 21: MC talks to girl about video and how good it was, girl asks MC to make a new one within X days (how we time limit this)
# 29: MC does not make video in time. Receives text from girl saying she found another actor but thanks anyway.
# 31: Porn video created, wait a few days to see how popular it is.
# 39: Porn video is a dud. Lose obedience from all girls in the office (They all see it and know how poorly MC performed) (Bad end).
# 41: If popular, girl says she really appreciates it, would be open to using you as an actor in the future. Offers to promote MC.business.name
# 42: If very popular, all girls at office get obedience and sluttiness bonus.
# 49: MC says thats okay, just had fun making video. (Bad End)
# 101: Girl moves to marketing. Gain marketability based on sex video rating. (Good end)
# Any 100 ending adds marketability. Also 40+ can refer to girl as porn star, personality tweak.


label quest_porn_acress_init_label():
    python:
        able_person_list = []
        for person in mc.business.get_employee_list(): #TODO is there a method that grabs ENTIRE employee list?
            if person not in quest_director.unavailable_persons:
                if person.core_sluttiness > 60:
                    able_person_list.append(person)

        quest_porn_acress.quest_event_dict["start_day"] = 9999
        quest_porn_acress.quest_event_dict["target"] = get_random_from_list(able_person_list)
        quest_porn_acress.quest_event_dict["disease_name"]  = quest_cure_discovery_disease_name()
        quest_porn_acress.quest_event_dict["market_contact"] = None
        quest_porn_acress.quest_event_dict["market_day"] = 9999
        quest_porn_acress.set_quest_flag(1)
    return


init 1 python:
    def rate_porn_video(the_report, the_person):  #Takes a sex report and person and returns a score of 1-10 on how good the video isself.
        porn_score = 0
        if len(the_report.get("positions_used", [])) <= 1:  #Max three points for number of positions used
            porn_score += 1
        elif the_report.get("positions_used", []) <= 4:
            porn_score += 2
        else:
            porn_score += 3

        if the_report.get("girl orgasms", 0) <= 4:   #Max 4 points for as many female orgasms
            porn_score += the_report.get("girl orgasms", 0)
        else:
            porn_score += 4
        cum_score = 0   #Max three points based on cum shots.
        if the_person.outfit.has_ass_cum():
            cum_score += 1
        if the_person.outfit.has_mouth_cum():
            cum_score += 1
        if the_person.outfit.has_tits_cum():
            cum_score += 1
        if the_person.outfit.has_stomach_cum():
            cum_score += 1
        if the_person.outfit.has_face_cum():
            cum_score += 1
        if the_person.outfit.has_creampie_cum():
            cum_score += 1
        if cum_score > 3:
            cum_score = 3
        porn_score += cum_score

        return porn_score

#Quest defining functions

    def quest_porn_actress_tracker():

        return

    def quest_porn_actress_start_requirement():

        return
    def quest_porn_actress_cleanup():

        return

#Label requirement functions



#Action declarations


#Quest Labels
label quest_porn_actress_intro_label():
    $ the_target = quest_porn_actress.quest_event_dict.get("target", None)
    $ the_person = get_random_from_list(mc.business.get_employee_list())
    while the_target == the_person:   #If they are same, get a different employee
        $ the_person = get_random_from_list(mc.business.get_employee_list())
    "You get up to stretch your legs for a bit and to check on the different departments, making sure everything is running smoothly."
    "As you pass by the break room, you everhear something."
    the_person.char "Oh my... is that really [the_target.name]? It looks just like her... That's what the other girls are saying!"



    $del the_target
    return
