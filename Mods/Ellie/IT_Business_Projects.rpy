init 1 python:
    ## Business IT Projects

    business_IT_project_list = []

    hr_organized_chaos_project = IT_Project(name = "Organized Chaos",
        desc = "Inceases the maximum efficiency of the company by 5%.",
        requirement = IT_proj_test_req_text,
        cost = 0,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "HR",
        tier = 30)

    business_IT_project_list.append(hr_organized_chaos_project)

    hr_task_manager_project = IT_Project(name = "Task Manager",
        desc = "Requires an HR Director. All HR employees give a maximum efficiency bonus at half the rate of the HR Director.",
        requirement = IT_proj_test_req_text,
        cost = 0,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "HR",
        tier = 20)

    business_IT_project_list.append(hr_task_manager_project)

    supply_inventory_project = IT_Project(name = "JiT Inventory",
        desc = "Just in Time inventory practices help increase efficiency. Increased supply procurement when the company is low on supplies.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "supply",
        tier = 10)

    business_IT_project_list.append(supply_inventory_project)

    supply_storage_project = IT_Project(name = "Storage Automation",
        desc = "Chemical storage and retrieval automation. Reduces the cost associated with purchasing and storing supplies by 5%.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "supply",
        tier = 20)

    business_IT_project_list.append(supply_storage_project)

    market_photo_filter_project = IT_Project(name = "Photo Filters",
        desc = "Automated photo filters. Increases the desirability of the subjects used in promotions, increasing product demand. 5% product price increase.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "market",
        tier = 10)

    business_IT_project_list.append(market_photo_filter_project)

    market_targeted_advertising_project = IT_Project(name = "Targeted Adverts",
        desc = "Know your audience. Refining advertising filters automatically based on the demographics of previous sales. Increases sales by 5%.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "market",
        tier = 20)

    business_IT_project_list.append(market_targeted_advertising_project)

    research_peerless_review_project = IT_Project(name = "Peerless Review",
        desc = "The sensitive nature of the research hinders peer review. Automatic detection and replacement of sensitive terms allows for increased rate of research. Increases research by 5%",
        cost = 0,
        requirement = IT_proj_test_req_text,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "research",
        tier = 10)

    business_IT_project_list.append(research_peerless_review_project)

    research_group_discovery_project = IT_Project(name = "Group Discovery",
        desc = "Automates sharing of research among team members who work in similar fields. Allows research to be more evenly distributed. Reduces Clarity costs of serum traits by 5%",
        cost = 0,
        requirement = IT_proj_test_req_False,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "research",
        tier = 20)

    business_IT_project_list.append(research_group_discovery_project)

    production_group_discovery_project = IT_Project(name = "Assembly Line",
        desc = "Serums now created via assembly line instead of in small batches. Production increased by 25%, but also uses 25% more supply. Can be toggled.",
        cost = 0,
        requirement = IT_proj_test_req_text,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "production",
        tier = 10)

    business_IT_project_list.append(production_group_discovery_project)

    production_equipment_selftest_project = IT_Project(name = "Equipment Selftest",
        desc = "Production equipment now runs an end of the day self test. Reduces production staff workload, slightly increasing happiness.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "production",
        tier = 20)

    business_IT_project_list.append(production_equipment_selftest_project)

    business_IT_project_list.sort(key = IT_project_sort)


    def IT_get_HR_projects():
        return list(filter(lambda x: x.category == "HR", business_IT_project_list))

    def IT_get_supply_projects():
        return list(filter(lambda x: x.category == "supply", business_IT_project_list))

    def IT_get_market_projects():
        return list(filter(lambda x: x.category == "market", business_IT_project_list))

    def IT_get_research_projects():
        return list(filter(lambda x: x.category == "research", business_IT_project_list))

    def IT_get_production_projects():
        return list(filter(lambda x: x.category == "production", business_IT_project_list))
