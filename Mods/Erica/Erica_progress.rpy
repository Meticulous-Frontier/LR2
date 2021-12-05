init 10 python:

    def erica_story_love_list():
        love_story_list = []
        if erica_get_is_doing_yoga_sessions() and erica_get_is_doing_insta_sessions():
            love_story_list.append("You helped [erica.title] earn some extra money doing Instapic and Yoga.")
        elif erica_get_is_doing_yoga_sessions():
            love_story_list.append("You helped [erica.title] earn some extra money doing Yoga.")
            love_story_list.append("Try working with [lily.title] to help [erica.title] earn some extra money.")
            return love_story_list
        elif erica_get_is_doing_insta_sessions():
            love_story_list.append("You helped [erica.title] earn some extra money doing Instapic with [lily.title].")
            love_story_list.append("Try working with your HR Director to help [erica.title] earn some extra money.")
            return love_story_list
        elif erica_is_looking_for_work():
            love_story_list.append("[erica.title] is looking for some part time work.")
            love_story_list.append("Try working with your HR director or [lily.title] to help her find some extra work!")
            return love_story_list
        elif erica.love <20:
            love_story_list.append("Try increasing [erica.title]'s love score.")
            return love_story_list
        else:
            love_story_list.append("Try getting to know [erica.title] better.")
            return love_story_list

        if erica_pre_insta_blowjob_complete():
            love_story_list.append("[erica.title] showed her appreciation by giving you a blowjob before an Instapic session!")
        elif erica.love <= 40:
            love_story_list.append("Try increasing her love to continue this story.")
            return love_story_list
        elif not erica.is_willing(blowjob):
            love_story_list.append("[erica.title] needs to be willing to give you a blowjob. Make sure her sluttiness is high enough and she doesn't hate that act!")
            return love_story_list
        else:
            love_story_list.append("Make sure to be there to take pics for [erica.title] and [lily.title]'s next Instapic session.")
            return love_story_list

        if erica_post_yoga_fuck_complete():
            love_story_list.append("You couldn't stop watching [erica.title] during your company yoga. She loved it and you fucked her after against your office wall.")
        elif erica.love <= 60:
            love_story_list.append("Try increasing her love to continue this story.")
            return love_story_list
        elif not erica.is_willing(against_wall):
            love_story_list.append("[erica.title] needs to be willing to fuck you against the wall. Make sure her sluttiness is high enough and she doesn't hate that act!")
            return love_story_list
        else:
            love_story_list.append("Make sure to attend company yoga on Tuesday morning to continue this story.")
            return love_story_list

        love_story_list.append("There is nothing more in this story line at this time.")
        return love_story_list

    def erica_story_lust_list():
        lust_story_list = []

        if erica_has_given_morning_handjob():
            lust_story_list.append("[erica.title] woke you up with a handjob after spending the night with [lily.title].")
            lust_story_list.append("Talk to her if you want her to wake you up more or less often.")
        elif not erica.is_willing(cowgirl_handjob, ignore_taboo = True):
            lust_story_list.append("[erica.title] needs to be willing to give a handjob to continue this story. Try raising her sluttiness and check her opinions.")
            return lust_story_list
        elif not erica_get_is_doing_insta_sessions():
            lust_story_list.append("Try advancing [erica.title]'s love story to unlock this.")
            return lust_story_list
        else:
            lust_story_list.append("[erica.title] may try sneaking into your room some morning...")
            return lust_story_list

        if erica.event_triggers_dict.get("erica_progress", 0) > 1:
            lust_story_list.append("You worked out with [erica.title] and had some fun in the gym locker room afterwords.")
        elif erica.event_triggers_dict.get("erica_progress", 0) == 1:
            lust_story_list.append("Try working out with [erica.title] sometime.")
            return lust_story_list
        elif mc.max_energy < 120:
            lust_story_list.append("[erica.title] prefers athletic guys. Try raising your maximum energy.")
            return lust_story_list
        elif erica.sluttiness < 40:
            lust_story_list.append("Try raising [erica.title]'s sluttiness to continue this story.")
            return lust_story_list

        if erica.event_triggers_dict.get("erica_progress", 0) >= 4:
            lust_story_list.append("You won a bet with [erica.title] in a race, then fucked her at her place.")
        elif erica.event_triggers_dict.get("erica_progress", 0) == 3:
            lust_story_list.append("You've challenged [erica.title] to a race. To the victor go the spoils!")
            return lust_story_list
        elif erica.sluttiness < 60:
            lust_story_list.append("Try raising [erica.title]'s sluttiness to continue this story.")
            return lust_story_list
        elif mc.max_energy < 140:
            lust_story_list.append("[erica.title] prefers athletic guys. Try raising your maximum energy.")
            return lust_story_list
        else:
            lust_story_list.append("Try challenging [erica.title] to a race.")
            return lust_story_list

        lust_story_list.append("There is nothing more in this story line at this time.")

        return lust_story_list

    def erica_story_teamup_list():
        teamup_story_list = []
        #Yoga
        if erica_get_is_doing_yoga_sessions():
            teamup_story_list.append([sarah,"Watch [erica.title] do yoga with [sarah.title] every Tuesday morning at the office!"])
        elif erica.event_triggers_dict.get("yoga_quest_started", False) == False:
            teamup_story_list.append([sarah,"Try progressing [erica.title]'s story."])
        elif len(erica_get_yoga_class_list()) < 4:
            teamup_story_list.append([sarah,"Help [sarah.title] convince employees to like or love yoga."])
        else:
            teamup_story_list.append([sarah,"Talk to [erica.title] about hosting a company yoga class."])

        #Insta
        if erica_get_is_doing_insta_sessions():
            teamup_story_list.append([lily,"Help [erica.title] take insta pics with [lily.title] every Saturday night in [lily.title]'s room!"])
        elif not erica_is_looking_for_work():
            teamup_story_list.append([erica,"Try progressing [erica.title]'s story."])
        elif lily.event_triggers_dict.get("sister_instathot_pic_count", 0) == 0:
            teamup_story_list.append([lily,"Try advancing [lily.title]'s storyline."])
        else:
            teamup_story_list.append([lily,"Try talking to [lily.title] and [erica.title] about money issues."])
        return teamup_story_list

    def erica_story_other_list():
        other_info_list = []
        if erica.event_triggers_dict.get("erica_progress", 0) > 1:
            other_info_list.append("[erica.title] likes to workout with you at the gym, especially what happens after...")
        if erica.event_triggers_dict.get("erica_progress", 0) >= 4:
            other_info_list.append("You are always welcome at [erica.title]'s house at night.")
        if erica_fetish_is_kicked_off_team() and not erica_fetish_rejoin_team():
            other_info_list.append("[erica.title] got kicked off the track team for getting pregnant! Try talking to [nora.title].")
        if erica_fetish_rejoin_team():
            other_info_list.append("You helped [erica.title] rejoin the track team after knocking her up.")

        return other_info_list
