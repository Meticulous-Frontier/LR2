init 2 python:
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

    ass_cum_goal = Goal("Anal Seeding", "There's nothing like dumping a load in a tight asshole. Cum inside a few different asses.", "sex_cum_ass", "MC", always_valid_goal_function, ass_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = ass_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)


    sex_goals.append(ass_cum_goal)
