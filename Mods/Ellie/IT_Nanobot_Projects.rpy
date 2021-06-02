init 1 python:
    ## Business IT Projects

    nanobot_IT_project_list = []

    def basic_clarity_reduction_on_apply():
        get_fetish_basic_serum().research_added = 100
        get_fetish_basic_serum().negative_slug = "+100 Serum Research, +" + str(FETISH_PRODUCTION_COST) + " Production Cost"
        return

    def basic_clarity_reduction_on_remove():
        get_fetish_basic_serum().research_added = FETISH_RESEARCH_ADDED
        get_fetish_basic_serum().negative_slug = "+" + str(FETISH_RESEARCH_ADDED) + " Serum Research, +" + str(FETISH_PRODUCTION_COST) + " Production Cost"
        return

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

    nanobot_IT_project_list.append(basic_clarity_reduction_project)




    nanobot_IT_project_list.sort(key = IT_project_sort)

    def IT_get_basic_bot_projects():
        return list(filter(lambda x: x.category == "basic", nanobot_IT_project_list))

    def IT_get_breeder_bot_projects():
        return list(filter(lambda x: x.category == "supply", nanobot_IT_project_list))

    def IT_get_anal_bot_projects():
        return list(filter(lambda x: x.category == "market", nanobot_IT_project_list))

    def IT_get_cum_bot_projects():
        return list(filter(lambda x: x.category == "research", nanobot_IT_project_list))

    def IT_get_exhibition_bot_projects():
        return list(filter(lambda x: x.category == "production", nanobot_IT_project_list))
