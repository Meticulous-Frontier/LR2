init 10 python:
    def lily_story_love_list():
        love_story_list = []
        if not lily_can_give_serum():
            love_story_list.append("[lily.name] may talk to you about earning some money soon!")
            return love_story_list
        else:
            love_story_list.append("[lily.name] agreed to help you test your serums.")

        if lily.is_girlfriend():
            love_story_list.append("[lily.name] has agreed to be your girlfriend!")
        elif lily.love < 60:
            love_story_list.append("[lily.name] minimum love of 60 to consider being your girlfriend.")
            return love_story_list
        elif not mom.event_triggers_dict.get("sister_girlfriend_ask_blessing", False):
            love_story_list.append("Work on getting [mom.title] to accept your relationship.")
            return love_story_list
        else:
            love_story_list.append("You might be able to convince [lily.name] to be your girlfriend if you try.")
            return love_story_list

        love_story_list.append("There is nothing more in this story line at this time.")
        return love_story_list

    def lily_story_lust_list():
        lust_story_list = []

        if not lily_can_give_serum():
            lust_story_list.append("Work on [lily.name]'s love story first.")
            return lust_story_list

        #Insta start
        if lily.sluttiness < 20:
            lust_story_list.append("Get [lily.name] to 20 sluttiness.")
            return lust_story_list
        elif lily_started_insta_story():
            lust_story_list.append("You helped [lily.name] take pictures for InstaPic.")
        else:
            lust_story_list.append("Try entering [lily.name]'s room when she is alone there.")
            return lust_story_list

        #Stripping
        if lily_will_strip():
            lust_story_list.append("[lily.name] offered to strip for you for extra cash!")
        elif lily.sluttiness < 30:
            lust_story_list.append("Raise [lily.name]'s sluttiness to at least 30 to continue this story.")
            return lust_story_list
        elif lily_get_serums_tested() < 4:
            story_string = "Have [lily.name] test " + str(4 - lily_get_serums_tested()) + " more serums."
            lust_story_list.append(story_string)
            return lust_story_list


        lust_story_list.append("There is nothing more in this story line at this time.")

        return lust_story_list

    def lily_story_teamup_list():
        teamup_story_list = []
        if erica_get_is_doing_insta_sessions():
            teamup_story_list.append([erica,"Help [erica.title] take insta pics with [lily.title] every Saturday night in [lily.title]'s room!"])
        elif not erica_is_looking_for_work():
            teamup_story_list.append([erica,"Try progressing [erica.title]'s story."])
        elif lily.event_triggers_dict.get("sister_instathot_pic_count", 0) == 0:
            teamup_story_list.append([erica,"Try advancing [lily.title]'s storyline."])
        else:
            teamup_story_list.append([erica,"Try talking to [lily.title] and [erica.title] about money issues."])

        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            teamup_story_list.append([mom,"You've slept with [lily.title] and [mom.title] at the same time!"])
        elif lily_mom_topless_pics_complete():
            teamup_story_list.append([mom,"You've convinced [lily.title] and [mom.title] to take topless InstaPics!"])
        elif lily_mom_insta_started():
            teamup_story_list.append([mom,"You've convinced [lily.title] and [mom.title] to take InstaPics together."])
        else:
            teamup_story_list.append([mom,"Getting [lily.title] and [mom.title] together seems impossible... but is it?"])

        if kaya_has_finished_intro():
            teamup_story_list.append([kaya,"The [lily.title] and [kaya.title] teamup is in progress but not yet written."])

        return teamup_story_list

    def lily_story_other_list():
        story_other_list = []
        if lily_can_give_serum():
            story_other_list.append("[lily.title] will test your serums for $50")
        if lily_will_strip():
            story_other_list.append("[lily.title] will strip for you for $100")
        if lily_started_insta_story():
            story_other_list.append("You can help [lily.title] take pictures for her InstaPic account.")
        return story_other_list




#Use this for lily based wrappers to make coding above stuff easier.
init 9 python:
    def lily_progress_screen_activation():
        lily.event_triggers_dict["story_dict"] = True
        lily.story_character_description = "Your younger sister. Attends classes at the local universtiy and often hard up for cash."
        lily.story_love_list = lily_story_love_list
        lily.story_lust_list = lily_story_lust_list
        lily.story_teamup_list = lily_story_teamup_list
        lily.story_other_list = lily_story_other_list

    def lily_can_give_serum():
        return mc.business.event_triggers_dict.get("sister_serum_test", False)

    def lily_get_serums_tested():
        return mc.business.event_triggers_dict.get("sister_serum_test_count", 0)

    def lily_will_strip():
        return mc.business.event_triggers_dict.get("sister_strip", False)   #Why vren uses mc.business for this?

    def lily_started_insta_story():
        return lily.event_triggers_dict.get("insta_intro_finished", False)

    def lily_mom_insta_started():
        return mom.event_triggers_dict.get("mom_instathot_pic_count", 0) > 0

    def lily_mom_topless_pics_complete():
        return lily.event_triggers_dict.get("sister_instathot_mom_shirtless_covered_count", 0) > 0
