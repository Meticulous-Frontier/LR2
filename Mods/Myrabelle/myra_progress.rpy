init 10 python:

    def myra_story_love_list():
        love_story_list = []
        love_story_list.append("[myra.title] has opened a gaming cafe at the mall. Play games there to restore energy.")
        if not myra_will_grind_with_mc():
            love_story_list.append("Get your character to atleast level 30 to play Guild Quest 2 with [myra.title].")
        else:
            love_story_list.append("[myra.title] enjoys playing Guild Quest 2 with you.")
        if myra_plays_esports():
            love_story_list.append("You learned she is a part of an eSports team.")
        elif myra.love < 20:
            love_story_list.append("Increase [myra.title]'s love to learn more about her.")
            return love_story_list
        else:
            love_story_list.append("Swing by the gaming cafe to learn more about [myra.title].")
            return love_story_list
        if myra_has_failed_tournament():
            love_story_list.append("However, [myra.title] lost her first eSports tournament, badly.")
        elif myra.love < 40:
            love_story_list.append("Increase [myra.title]'s love to learn more about her.")
            return love_story_list
        else:
            love_story_list.append("[myra.title]'s first tournament is on a Sunday.")
            return love_story_list
        if myra_can_sponsor():
            love_story_list.append("She lost a major sponsor as a result.")
        elif myra.love < 60:
            love_story_list.append("Increase [myra.title]'s love to progress her story.")
            return love_story_list
        else:
            love_story_list.append("Stop by the cafe in the evening to learn the repercussions of her loss.")
            return love_story_list
        if myra_has_been_sponsored():
            love_story_list.append("You stepped up and sponsored her eSports team yourself.")
        if not mc.business.has_funds(25000):
            love_story_list.append("You need more money to step up and sponsor her yourself.")
            return love_story_list
        else:
            love_story_list.append("Talk to [myra.title] about sponsoring her team yourself.")
            return love_story_list
        love_story_list.append("This is the end of content in this version. Everything after this in her love story is just outlining.")
        if myra.love < 80:
            love_story_list.append("Increase [myra.title]'s love to progress her story.")
            return love_story_list
        elif myra_focus_progression_scene.get_stage() < 2:
            love_story_list.append("Help [myra.title] train her focus to advance her story.")
            return love_story_list
        elif not myra_has_won_tournament():
            love_story_list.append("Talk to [myra.title] about setting up a new tournament. She is ready!")
            return love_story_list
        if myra_has_won_tournament():
            love_story_list.append("[myra.title] hosted her own tournament and placed third! A huge improvement!")
        if myra_is_expanding_business():
            love_story_list.append("She has used her winnings to begin expanding her business!")
        elif myra.love < 95:
            love_story_list.append("Increase [myra.title]'s love to progress her story.")
            return love_story_list
        else:
            love_story_list.append("Talk to [myra.title] about her winnings.")
            return love_story_list




        love_story_list.append("There is nothing more in this story line at this time.")
        return love_story_list

    def myra_story_lust_list():
        lust_story_list = []
        if myra_distracts_gamers():
            lust_story_list.append("[myra.title] likes to use dirty language and double entendres to distract gaming opponents.")
        elif myra.sluttiness < 20:
            lust_story_list.append("Raise [myra.title]'s sluttiness to advance this story.")
            return lust_story_list
        else:
            lust_story_list.append("Swing by the gaming cafe during business hours to advance this story.")
            return lust_story_list
        if myra_caught_masturbating():
            lust_story_list.append("[myra.title] enjoys sexual video games. You caught her masturbating to one.")
        elif myra.sluttiness < 40:
            lust_story_list.append("Raise [myra.title]'s sluttiness to advance this story.")
            return lust_story_list
        else:
            lust_story_list.append("Swing by the gaming cafe during the evening to advance this story.")
            return lust_story_list
        if myra_lewd_game_fuck_avail():
            lust_story_list.append("[myra.title] enjoys fucking you while acting out positions from a sexual PC game. She is willing every evening at the gaming cafe.")
        elif myra.sluttiness < 60:
            lust_story_list.append("Raise [myra.title]'s sluttiness to advance this story.")
            return lust_story_list
        elif myra.has_taboo("vaginal_sex"):
            lust_story_list.append("Fuck [myra.title] to advance this story.")
            return lust_story_list
        else:
            lust_story_list.append("Swing by the gaming cafe during the evening to advance this story.")
            return lust_story_list
        if myra_lewd_cafe_open():
            lust_story_list.append("She has opened an adults only VIP section at the gaming cafe for sexual PC games.")
        elif myra.sluttiness < 80:
            lust_story_list.append("Raise [myra.title]'s sluttiness to advance this story.")
            return lust_story_list
        elif not myra_is_expanding_business():
            lust_story_list.append("Advance [myra.title]'s love story before advancing this story.")
            return lust_story_list


        lust_story_list.append("There is nothing more in this story line at this time.")

        return lust_story_list

    def myra_story_teamup_list():
        teamup_story_list = []

        #Alexia
        if myra_alexia_teamup_scene.get_stage() == -1:
            teamup_story_list.append([alexia, "[alexia.title] is her good friend. Maybe there will be an opportunity here someday"])
        elif myra_alexia_teamup_scene.get_stage() == 0:
            teamup_story_list.append([alexia, "[alexia.title] meets with her every Friday night. You can rub their backs if you join them."])
        elif myra_alexia_teamup_scene.get_stage() == 1:
            teamup_story_list.append([alexia, "[alexia.title] and [myra.title] compete for you to finger them on Friday nights."])
        elif myra_alexia_teamup_scene.get_stage() == 2:
            teamup_story_list.append([alexia, "[alexia.title] and [myra.title] compete for you to eat them out on Friday nights."])
        elif myra_alexia_teamup_scene.get_stage() == 3:
            teamup_story_list.append([alexia, "[alexia.title] and [myra.title] compete for you to fuck them on Friday nights."])
        elif myra_alexia_teamup_scene.get_stage() == 3:
            teamup_story_list.append([alexia, "[alexia.title] and [myra.title] have a friendly gaming night that always needs in a threesome on Friday nights."])
        return teamup_story_list

    def myra_story_other_list():
        other_info_list = []
        if myra_focus_progression_scene.get_stage() >= 0:
            other_info_list.append("You can help [myra.title] train her focus to get better at gaming in distracting situations.")
            if myra_focus_progression_scene.get_stage() == 0:
                other_info_list.append("You distract her with backrubs during training. Raise her sluttiness to take disitractions further.")
            elif myra_focus_progression_scene.get_stage() == 1:
                other_info_list.append("You distract her by groping her tits during training. Raise her sluttiness to take disitractions further.")
            elif myra_focus_progression_scene.get_stage() == 2:
                other_info_list.append("You distract her by finger her during training. Raise her sluttiness to take disitractions further.")
            elif myra_focus_progression_scene.get_stage() == 3:
                other_info_list.append("You distract her by getting a lapdance during training. Raise her sluttiness to take disitractions further.")
            elif myra_focus_progression_scene.get_stage() == 4:
                other_info_list.append("You distract her by fucking her ass during training.")
        if myra_can_distribute_serum():
            other_info_list.append("Every Wednesday, you can send company energy drinks to [myra.title] for distribution.")
        if myra_wants_bigger_tits() and not myra.has_large_tits():
            other_info_list.append("[myra.title] has asked for help growing bigger tits.")
        elif myra.has_large_tits() and myra_wants_bigger_tits():
            other_info_list.append("[myra.title] is thankful you helped her grow her tits.")
        if myra_finish_blowjob_training():
            other_info_list.append("You helped train [myra.title] how to give amazing head.")
        elif myra_started_blowjob_training():
            other_info_list.append("You are training [myra.title] how to give better head. Check back with her weekly.")
        else:
            other_info_list.append("[myra.title] hates giving head. You should look for some way to show her oral skills are important.")
        if myra_lewd_cafe_open():
            other_info_list.append("[myra.title] has opened an adults only section to the gaming cafe!")

        return other_info_list
