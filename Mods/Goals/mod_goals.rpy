init 2 python:
    def daily_profit_count_function(the_goal, profit):
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

    def side_money_count_function(the_goal, count):
        the_goal.arg_dict["count"] += count
        if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
            return True
        return False

    def side_money_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"]  = 100
        the_goal.arg_dict["required"]  += (50 * the_difficulty)
        if the_difficulty > 8:
            the_goal.arg_dict["required"]  += (100 * the_difficulty)
        if the_goal.arg_dict["required"] > 3000:
            the_goal.arg_dict["required"]  = 3000

    def HR_interview_count_function(the_goal):
        the_goal.arg_dict["count"] += 1
        if the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]:
            return True
        return False

    def HR_interview_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] = int(1 + (the_difficulty / 5))
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

    daily_profit_goal = Goal("Daily Profit", "Profitibility is always a concern when running a business. Have your business make at least a certain amount in one day.", "daily_profit", "Business", always_valid_goal_function, daily_profit_count_function,
    {"count": 0, "required": 50},
    difficulty_scale_function = daily_profit_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    side_money_goal = Goal("Side Hustles", "Earn money from ways other than through pharmaceuticals.", "side_money", "Business", always_valid_goal_function, side_money_count_function,
    {"count": 0, "required": 100},
    difficulty_scale_function = side_money_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    HR_interview_goal = Goal("HR meetings", "Use the HR director to conduct meetings with employees.", "HR_opinion_improvement", "MC", always_valid_goal_function, HR_interview_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = HR_interview_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    ass_cum_goal = Goal("Anal Seeding", "There's nothing like dumping a load in a tight asshole. Cum inside a few different asses.", "sex_cum_ass", "MC", always_valid_goal_function, ass_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = ass_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    threesome_goal = Goal("Have a Threesome", "You don't need a million dollars to do two girls at the same time.", "threesome", "MC", always_valid_goal_function, threesome_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = threesome_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)
