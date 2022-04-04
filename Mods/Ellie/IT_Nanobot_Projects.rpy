init 1 python:
    ## Business IT Projects

    nanobot_IT_project_list = []

    ### Project related functions ###

    def basic_clarity_reduction_on_apply():
        get_fetish_basic_serum().research_added = 100
        return

    def basic_clarity_reduction_on_remove():
        get_fetish_basic_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def anal_clarity_reduction_on_apply():
        get_fetish_anal_serum().research_added = 100
        return

    def anal_clarity_reduction_on_remove():
        get_fetish_anal_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def breeder_clarity_reduction_on_apply():
        get_fetish_breeding_serum().research_added = 100
        return

    def breeder_clarity_reduction_on_remove():
        get_fetish_breeding_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def cum_clarity_reduction_on_apply():
        get_fetish_cum_serum().research_added = 100
        return

    def cum_clarity_reduction_on_remove():
        get_fetish_cum_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def exhibition_clarity_reduction_on_apply():
        get_fetish_exhibition_serum().research_added = 100
        return

    def exhibition_clarity_reduction_on_remove():
        get_fetish_exhibition_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def anal_incest_project_on_apply():
        if "incest" not in FETISH_ANAL_OPINION_LIST:
            FETISH_ANAL_OPINION_LIST.append("incest")
        return

    def anal_incest_project_on_remove():
        if "incest" in FETISH_ANAL_OPINION_LIST:
            FETISH_ANAL_OPINION_LIST.remove("incest")
        return

    def breeder_submission_project_on_apply():
        if "being submissive" not in FETISH_BREEDING_OPINION_LIST:
            FETISH_BREEDING_OPINION_LIST.append("being submissive")
        return

    def breeder_submission_project_on_remove():
        if "being submissive" in FETISH_BREEDING_OPINION_LIST:
            FETISH_BREEDING_OPINION_LIST.remove("being submissive")
        return

    def cum_thirst_project_on_apply():
        if "taking control" not in FETISH_CUM_OPINION_LIST:
            FETISH_CUM_OPINION_LIST.append("taking control")
        return

    def cum_thirst_project_on_remove():
        if "taking control" in FETISH_CUM_OPINION_LIST:
            FETISH_CUM_OPINION_LIST.remove("taking control")
        return

    def exhibition_cheating_project_on_apply():
        if "cheating on men" not in FETISH_EXHIBITION_OPINION_LIST:
            FETISH_EXHIBITION_OPINION_LIST.append("cheating on men")
        return

    def exhibition_cheating_project_on_remove():
        if "cheating on men" in FETISH_EXHIBITION_OPINION_LIST:
            FETISH_EXHIBITION_OPINION_LIST.remove("cheating on men")
        return

init 1 python:
    ###Project requirement functions###
    def anal_incest_project_requirement():
        return get_fetish_anal_serum().mastery_level >= 3.0

    def breeder_submission_project_requirement():
        if get_fetish_breeding_serum().mastery_level >= 3.0:
            return True
        return "Low Mastery"

    def cum_thirst_project_requirement():
        return get_fetish_cum_serum().mastery_level >= 3.0

    def exhibition_cheating_project_requirement():
        if get_fetish_exhibition_serum().mastery_level >= 3.0:
            return True
        return "Low Mastery"

init 1 python:

    basic_clarity_reduction_project = IT_Project(name = "Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces clarity requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = basic_clarity_reduction_on_apply,
        on_remove_function = basic_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "basic",
        tier = 10)

    anal_clarity_reduction_project = IT_Project(name = "Anal Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = anal_clarity_reduction_on_apply,
        on_remove_function = anal_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "anal",
        tier = 10)

    anal_incest_project = IT_Project(name = "Familial Anal Adaptation",
        desc = "Members of family may be more willing to accept acts of Anal. Adds Incest to opinions increased by the Anal Proclivity Nanobots.",
        cost = 0,
        requirement = anal_incest_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = anal_incest_project_on_apply,
        on_remove_function = anal_incest_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "anal",
        tier = 20)

    breeder_clarity_reduction_project = IT_Project(name = "Breeding Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = breeder_clarity_reduction_on_apply,
        on_remove_function = breeder_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "breeder",
        tier = 10)

    breeder_submission_project = IT_Project(name = "Submissive Breeder Adaptation",
        desc = "Encourages breeding as an active form of submission. Adds being submissive to the list of opinions increased by Reproduction Proclivity Nanobots.",
        cost = 0,
        requirement = breeder_submission_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = breeder_submission_project_on_apply,
        on_remove_function = breeder_submission_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "breeder",
        tier = 20)

    cum_clarity_reduction_project = IT_Project(name = "Cum Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = cum_clarity_reduction_on_apply,
        on_remove_function = cum_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "cum",
        tier = 10)

    cum_thirst_project = IT_Project(name = "Cum Thirst Adaptation",
        desc = "Exposure to cum causes thirst. Makes girls more likely to seek out situations where they will be exposed to it. Adds taking control to the list of opinions increased by Semen Proclivity Nanobots.",
        cost = 0,
        requirement = cum_thirst_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = cum_thirst_project_on_apply,
        on_remove_function = cum_thirst_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "cum",
        tier = 20)

    exhibition_clarity_reduction_project = IT_Project(name = "Exhibition Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = exhibition_clarity_reduction_on_apply,
        on_remove_function = exhibition_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "exhibition",
        tier = 10)

    exhibition_cheating_project = IT_Project(name = "Risky Behavior Adaptation",
        desc = "Exhibitionism is often encouraged by risky behavior. Adds cheating on men to the list of opinions increased by Social Sexual Proclivity Nanobots.",
        cost = 0,
        requirement = exhibition_cheating_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = exhibition_cheating_project_on_apply,
        on_remove_function = exhibition_cheating_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "exhibition",
        tier = 20)


    nanobot_IT_project_list.append(basic_clarity_reduction_project)
    nanobot_IT_project_list.append(anal_clarity_reduction_project)
    nanobot_IT_project_list.append(anal_incest_project)
    nanobot_IT_project_list.append(breeder_clarity_reduction_project)
    nanobot_IT_project_list.append(breeder_submission_project)
    nanobot_IT_project_list.append(cum_clarity_reduction_project)
    nanobot_IT_project_list.append(cum_thirst_project)
    nanobot_IT_project_list.append(exhibition_clarity_reduction_project)
    nanobot_IT_project_list.append(exhibition_cheating_project)


    nanobot_IT_project_list.sort(key = IT_project_sort)

    def IT_get_basic_bot_projects():
        return list(filter(lambda x: x.category == "basic", nanobot_IT_project_list))

    def IT_get_breeder_bot_projects():
        return list(filter(lambda x: x.category == "breeder", nanobot_IT_project_list))

    def IT_get_anal_bot_projects():
        return list(filter(lambda x: x.category == "anal", nanobot_IT_project_list))

    def IT_get_cum_bot_projects():
        return list(filter(lambda x: x.category == "cum", nanobot_IT_project_list))

    def IT_get_exhibition_bot_projects():
        return list(filter(lambda x: x.category == "exhibition", nanobot_IT_project_list))
