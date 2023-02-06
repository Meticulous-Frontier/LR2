init 5 python:
    add_label_hijack("normal_start", "activate_goal_mod_core")
    add_label_hijack("after_load", "update_goal_mod_core")

init 2 python:
    def daily_profit_count_function(the_goal, profit):
        the_goal.arg_dict["count"] = profit # To make "progress" show
        if profit >= the_goal.arg_dict["required"]:
            return True
        return False

    def daily_profit_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"]  = 100
        the_goal.arg_dict["required"]  += (50 * the_difficulty)
        if the_difficulty > 4:
            the_goal.arg_dict["required"]  += (100 * the_difficulty)
        if the_difficulty > 8:
            the_goal.arg_dict["required"]  += (150 * the_difficulty)
        if the_goal.arg_dict["required"] > 5000:
            the_goal.arg_dict["required"]  = 5000

    # def side_money_count_function(the_goal, count):
    #     the_goal.arg_dict["count"] += count
    #     if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
    #         return True
    #     return False

    # def side_money_difficulty_function(the_goal, the_difficulty):
    #     the_goal.arg_dict["required"]  = 100
    #     the_goal.arg_dict["required"]  += (50 * the_difficulty)
    #     if the_difficulty > 8:
    #         the_goal.arg_dict["required"]  += (100 * the_difficulty)
    #     if the_goal.arg_dict["required"] > 3000:
    #         the_goal.arg_dict["required"]  = 3000

    def HR_interview_count_function(the_goal, the_person):
        the_goal.arg_dict["count"] += 1
        if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
            return True
        return False

    def HR_interview_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] = __builtin__.int(1 + (the_difficulty / 5))
        if the_goal.arg_dict["required"] > 5:
            the_goal.arg_dict["required"]  = 5

    def ass_cum_count_function(the_goal, the_person):
        if not the_person in the_goal.arg_dict["people"]:
            the_goal.arg_dict["people"].append(the_person)
            the_goal.arg_dict["count"] += 1
            if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
                return True
        return False

    def ass_cum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/4)
        return

    def threesome_count_function(the_goal, the_person_one, the_person_two):
        the_goal.arg_dict["count"] += 1
        if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
            return True
        return False

    def threesome_difficulty_function(the_goal, the_difficulty): #For now this difficulty does not scale
        the_goal.arg_dict["required"] = 1
        return

    def give_serum_count_function(the_goal, the_person):
        if the_person in mc.business.get_employee_list() + [mom, lily, aunt, cousin]:
            return False

        the_goal.arg_dict["count"] += 1
        if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
            return True
        return False

    def give_serum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/3)
        return

    def face_cum_count_function(the_goal, the_person):
        if not the_person in the_goal.arg_dict["people"]:
            the_goal.arg_dict["people"].append(the_person)
            the_goal.arg_dict["count"] += 1
            if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
                return True
        return False

    def face_cum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/4)
        return

    def tits_cum_count_function(the_goal, the_person):
        if not the_person in the_goal.arg_dict["people"]:
            the_goal.arg_dict["people"].append(the_person)
            the_goal.arg_dict["count"] += 1
            if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
                return True
        return False

    def tits_cum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/6)  #Unlocked goal, so we make it slightly easier than other similar ones.
        return


    daily_profit_goal = Goal("Daily Profit", "Profitability is always a concern when running a business. Have your business make at least a certain amount in one day.", "daily_profit", "Business", always_valid_goal_function, daily_profit_count_function,
    {"count": 0, "required": 50},
    difficulty_scale_function = daily_profit_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    # side_money_goal = Goal("Side Hustles", "Earn money from ways other than through pharmaceuticals.", "side_money", "Business", always_valid_goal_function, side_money_count_function,
    # {"count": 0, "required": 100},
    # difficulty_scale_function = side_money_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    HR_interview_goal = Goal("HR meetings", "Use the HR director to conduct meetings with employees.", "HR_opinion_improvement", "MC", always_valid_goal_function, HR_interview_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = HR_interview_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    ass_cum_goal = Goal("Anal Seeding", "There's nothing like dumping a load in a tight asshole. Cum inside a few different asses.", "sex_cum_ass", "MC", always_valid_goal_function, ass_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = ass_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    threesome_goal = Goal("Have a Threesome", "You don't need a million dollars to do two girls at the same time.", "threesome", "MC", always_valid_goal_function, threesome_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = threesome_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    give_serum_goal = Goal("Try This Serum", "Successfully give a serum to a person who is not an employee or family member.", "give_random_serum", "MC", always_valid_goal_function, give_serum_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = give_serum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    face_cum_goal = Goal("Paint the Town White", "Show the world that various girls belong to you, by cumming all over their faces.", "sex_cum_on_face", "MC", always_valid_goal_function, face_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = face_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    tits_cum_goal = Goal("Frosted Cupcakes", "Mark you territoy. Cum on multiple girl's tits.", "sex_cum_on_tits", "MC", always_valid_goal_function, tits_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = tits_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    sex_goals.append(face_cum_goal)
    sex_goals.append(ass_cum_goal)
    sex_goals.append(threesome_goal)
    stat_goals.append(daily_profit_goal)
    # stat_goals.append(side_money_goal)
    work_goals.append(give_serum_goal)
    work_goals.append(HR_interview_goal)

    def update_goal_enabled_states_for_list(option_list, goal_list):
        for goal in goal_list: # add new goals to existing games
            if goal not in option_list:
                option_list.add(goal)

        for goal in option_list:
            if not goal.enabled: # remove disabled, when in list
                found = find_in_list(lambda x: x.hash() == goal.hash(), goal_list)
                if found:
                    goal_list.remove(found)
            else: # add enabled, when not in list
                found = find_in_list(lambda x: x.hash() == goal.hash(), goal_list)
                if not found:
                    goal_list.append(goal)


    def update_goal_enabled_states():
        update_goal_enabled_states_for_list(stat_goals_options_list, stat_goals)
        update_goal_enabled_states_for_list(work_goals_options_list, work_goals)
        update_goal_enabled_states_for_list(sex_goals_options_list, sex_goals)
        return

label activate_goal_mod_core(stack):
    python:
        stat_goals_options_list = set(stat_goals)
        work_goals_options_list = set(work_goals)
        sex_goals_options_list = set(sex_goals)

        update_goal_enabled_states()
        # execute after stack has run
        execute_hijack_call(stack)
    return

label update_goal_mod_core(stack):
    python:
        unmodded = False
        try:
            stat_goals_options_list
        except NameError:
            unmodded = True

        # extra check to validate that serum mod list exists correctly
        if not unmodded and not isinstance(stat_goals_options_list, set):
            unmodded = True

        if unmodded:
            stat_goals_options_list = set(stat_goals)
            work_goals_options_list = set(work_goals)
            sex_goals_options_list = set(sex_goals)

        update_goal_enabled_states()
        # execute after stack has run
        execute_hijack_call(stack)

    return
