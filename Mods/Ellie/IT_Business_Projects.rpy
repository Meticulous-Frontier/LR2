init 1 python:  #Multiple init 1 blocks to make organization easier.

    def hr_organized_chaos_project_requirement():
        return True

    def hr_task_manager_project_requirement():
        if len(mc.business.hr_team) >= 3:
            return True
        return "Requires 3 HR employees"

    def supply_inventory_project_requirement():
        return True

    def supply_storage_project_requirement():
        if len(mc.business.supply_team) >= 3:
            return True
        return "Requires 3 supply employees"

    def market_photo_filter_project_requirement():
        return True

    def market_targeted_advertising_project_requirement():
        return True #TODO lock behind modeling policy

    def research_peerless_review_project_requirement():
        return True

    def research_group_discovery_project_requirement():
        return "Unknown Requirement"

    def research_team_building_project_requirement():
        if len(mc.business.research_team) >= 3:
            return True
        return "Requires 3 research employees"

    def production_assembly_line_project_requirement():
        return True

    def production_equipment_selftest_project_requirement():
        if len(mc.business.production_team) >= 3:
            return True
        return "Requires 3 production employees"



init 1 python:
    ## Business IT Projects

    business_IT_project_list = []

    hr_organized_chaos_project = IT_Project(name = "Organized Chaos",
        desc = "Increases the maximum efficiency of the company by 5%.",
        requirement = hr_organized_chaos_project_requirement,
        cost = 0,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = hr_organized_chaos_project_on_apply,
        on_remove_function = hr_organized_chaos_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "HR",
        tier = 10)

    business_IT_project_list.append(hr_organized_chaos_project)

    hr_test_project = IT_Project(name = "Test Project",
        desc = "For Testing.",
        requirement = IT_proj_test_req_text,
        cost = 0,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = hr_organized_chaos_project_on_apply,
        on_remove_function = hr_organized_chaos_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 50,
        category = "HR",
        tier = 5)

    # business_IT_project_list.append(hr_test_project)

    hr_task_manager_project = IT_Project(name = "Task Manager",
        desc = "Requires an HR Director. All HR employees give a maximum efficiency bonus at half the rate of the HR Director.",
        requirement = hr_task_manager_project_requirement,
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
        project_cost = 150,
        category = "HR",
        tier = 20)

    business_IT_project_list.append(hr_task_manager_project)

    supply_inventory_project = IT_Project(name = "JiT Inventory",
        desc = "Just in Time inventory practices help increase efficiency. Increased supply procurement when the company is low on supplies.",
        cost = 0,
        requirement = supply_inventory_project_requirement,
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
        requirement = supply_storage_project_requirement,
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
        project_cost = 150,
        category = "supply",
        tier = 20)

    business_IT_project_list.append(supply_storage_project)

    market_photo_filter_project = IT_Project(name = "Photo Filters",
        desc = "Automated photo filters. Increases the desirability of the subjects used in promotions, increasing product demand. 5% product price increase.",
        cost = 0,
        requirement = market_photo_filter_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = market_photo_filter_project_on_apply,
        on_remove_function = market_photo_filter_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "market",
        tier = 10)

    business_IT_project_list.append(market_photo_filter_project)

    market_targeted_advertising_project = IT_Project(name = "Targeted Adverts", #TODO
        desc = "Know your audience. Refining advertising filters automatically based on the demographics of previous sales. Increases sales by 5%.",
        cost = 0,
        requirement = market_targeted_advertising_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = market_targeted_advertising_project_on_turn,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "market",
        tier = 20)

    business_IT_project_list.append(market_targeted_advertising_project)

    research_peerless_review_project = IT_Project(name = "Peerless Review", #TODO
        desc = "The sensitive nature of the research hinders peer review. Automatic detection and replacement of sensitive terms allows for increased rate of research. Increases research by 5%",
        cost = 0,
        requirement = research_peerless_review_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = research_peerless_review_project_on_turn,
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
        requirement = research_group_discovery_project_requirement,
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
        project_cost = 200,
        category = "research",
        tier = 30)

    business_IT_project_list.append(research_group_discovery_project)

    research_team_building_project = IT_Project(name = "Distributed Research",
        desc = "Distributing research evenly among team members eases workloads, making employees more loyal. Increases researcher obedience.",
        cost = 0,
        requirement = research_team_building_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = research_team_building_project_on_day,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "research",
        tier = 20)

    business_IT_project_list.append(research_team_building_project)

    production_assembly_line_project = IT_Project(name = "Assembly Line",
        desc = "Serums now created via assembly line instead of in small batches. Production increased by 25%, but also uses 25% more supply. Can be toggled.",
        cost = 0,
        requirement = production_assembly_line_project_requirement,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = production_assembly_line_project_on_turn,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "production",
        tier = 10)

    business_IT_project_list.append(production_assembly_line_project)

    production_equipment_selftest_project = IT_Project(name = "Equipment Selftest",
        desc = "Production equipment now runs an end of the day self test. Reduces production staff workload, slightly increasing happiness.",
        cost = 0,
        requirement = production_equipment_selftest_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = production_equipment_selftest_project_on_day,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
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


init -1 python:
    def hr_organized_chaos_project_on_apply():
        mc.business.effectiveness_cap += 5
        if get_HR_director_tag("business_HR_eff_bonus"):
            set_HR_director_tag("business_HR_eff_bonus", get_HR_director_tag("business_HR_eff_bonus") + 5)
        return

    def hr_organized_chaos_project_on_remove():
        mc.business.effectiveness_cap += -5
        if get_HR_director_tag("business_HR_eff_bonus"):
            set_HR_director_tag("business_HR_eff_bonus", get_HR_director_tag("business_HR_eff_bonus") + -5)
        return

    def market_photo_filter_project_on_apply():
        mc.business.add_sales_multiplier("Photo Filters", 1.05)
        return

    def market_photo_filter_project_on_remove():
        mc.business.remove_sales_multiplier("Photo Filters", 1.05)
        return

    def production_equipment_selftest_project_on_day():
        if not mc.business.is_weekend():
            for person in mc.business.production_team:
                person.change_happiness(1)

    def market_targeted_advertising_project_on_turn():
        if not mc.business.is_open_for_business():
            return 0
        sales_inc = 0
        for person in mc.business.market_team:
            sales_inc += marketing_potential_stat(person)
        serum_sale_count = __builtin__.round(sales_inc * 0.05)

        slut_modifier = 0
        serum_value_multiplier = 1.00 #For use with value boosting policies. Multipliers are multiplicative.
        if male_focused_marketing_policy.is_active(): #Increase value by the character's outfit sluttiness if you own that policy.
            sluttiness_multiplier = (slut_modifier/100.0) + 1
            serum_value_multiplier = serum_value_multiplier * (sluttiness_multiplier)

        multipliers_used = {} #Generate a dict with only the current max multipliers of each category.
        for multiplier_source in mc.business.sales_multipliers:
            if not multiplier_source[0] in multipliers_used:
                multipliers_used[multiplier_source[0]] = multiplier_source[1]
            elif multiplier_source[1] > multipliers_used.get(multiplier_source[0]):
                multipliers_used[multiplier_source[0]] = multiplier_source[1]

        for maxed_multiplier in multipliers_used:
            value_change = multipliers_used.get(maxed_multiplier)
            serum_value_multiplier = serum_value_multiplier * value_change

        sorted_by_value = sorted(mc.business.sale_inventory.serums_held, key = lambda serum: serum[0].value) #List of tuples [SerumDesign, count], sorted by the value of each design. Used so most valuable serums are sold first.
        if mc.business.sale_inventory.get_any_serum_count() < serum_sale_count:
            serum_sale_count = mc.business.sale_inventory.get_any_serum_count()

        this_batch_serums_sold = 0
        if serum_sale_count > 0: #ie. we have serum in our inventory to sell, and the capability to sell them.
            for serum in sorted_by_value:
                if serum_sale_count <= serum[1]:
                    #There are enough to satisfy order. Remove, add value to wallet, and break
                    value_sold = serum_sale_count * serum[0].value * serum_value_multiplier
                    if value_sold < 0:
                        value_sold = 0
                    mc.business.funds += value_sold
                    mc.business.sales_made += value_sold
                    mc.business.listener_system.fire_event("serums_sold_value", amount = value_sold)
                    mc.business.serums_sold += serum_sale_count
                    this_batch_serums_sold += serum_sale_count
                    mc.business.sale_inventory.change_serum(serum[0],-serum_sale_count)
                    serum_sale_count = 0
                    break
                else:
                    #There are not enough in this single order, remove _all_ of them, add value, go onto next thing.
                    serum_sale_count += -serum[1] #We were able to sell this number of serum.
                    value_sold = serum[1] * serum[0].value * serum_value_multiplier
                    if value_sold < 0:
                        value_sold = 0
                    mc.business.funds += value_sold
                    mc.business.sales_made += value_sold
                    mc.business.listener_system.fire_event("serums_sold_value", amount = value_sold)
                    mc.business.serums_sold += serum_sale_count
                    this_batch_serums_sold += serum_sale_count
                    mc.business.sale_inventory.change_serum(serum[0],-serum[1]) #Should set serum count to 0.
                    #Don't break, we haven't used up all of the serum count
        return this_batch_serums_sold

    def research_peerless_review_project_on_turn():
        if not mc.business.is_open_for_business():
            return 0
        research_inc = 0
        for person in mc.business.research_team:
            research_inc += research_potential_stat(person)
        research_amount = __builtin__.round(research_inc * 0.05)

        if mc.business.active_research_design is not None:
            the_research = mc.business.active_research_design
            is_researched = the_research.researched # If it was researched before we added any research then we are increasing the mastery level of a trait (does nothing to serum designs)
            mc.business.research_produced += research_amount
            if the_research.add_research(research_amount): #Returns true if the research is completed by this amount'
                if isinstance(the_research, SerumDesign):
                    the_research.generate_side_effects() #The serum will generate any side effects that are needed.
                    mc.business.mandatory_crises_list.append(Action("Research Finished Crisis",serum_creation_crisis_requirement,"serum_creation_crisis_label",the_research)) #Create a serum finished crisis, it will trigger at the end of the round
                    mc.business.add_normal_message("New serum design researched: " + the_research.name)
                    mc.business.active_research_design = None
                elif isinstance(the_research, SerumTrait):
                    if is_researched: #We've researched it already, increase mastery level instead.
                        mc.business.add_normal_message("Serum trait mastery improved: " + the_research.name + ", Now " + str(the_research.mastery_level))
                    else:
                        mc.business.add_normal_message("New serum trait researched: " + the_research.name)
                        mc.business.active_research_design = None #If it's a newly discovered trait clear it so we don't start mastering it without player input.
        return

    def production_assembly_line_project_on_turn():
        if not mc.business.is_open_for_business():
            return 0
        if mc.business.serum_production_array is None:
            return

        prod_inc = 0
        for person in mc.business.production_team:
            prod_inc += production_potential_stat(person)
        production_amount = __builtin__.round(prod_inc * 0.25)

        #Calculate the supplies used from the normal production amount
        supply_hit = production_amount
        if production_amount > mc.business.supply_count:
            mc.business.supply_count = 0
            return 0
        else:
            mc.business.supply_count -= supply_hit

        #Now calculate bonus production
        if production_amount > mc.business.supply_count:
            production_amount = mc.business.supply_count

        for production_line in mc.business.serum_production_array:
            # A production line is a tuple of [SerumDesign, production weight (int), production point progress (int)].
            serum_weight = mc.business.serum_production_array[production_line][1]
            the_serum = mc.business.serum_production_array[production_line][0]

            proportional_production = __builtin__.int((serum_weight/100.0) * production_amount) #Get the closest integer value for the weighted production we put into the serum
            mc.business.production_used += proportional_production #Update our usage stats and subtract supply needed.
            mc.business.supply_count += -proportional_production


            mc.business.serum_production_array[production_line][2] += proportional_production
            serum_prod_cost = the_serum.production_cost
            if serum_prod_cost <= 0:
                serum_prod_cost = 1
            serum_count = mc.business.serum_production_array[production_line][2]//serum_prod_cost #Calculates the number of batches we have made (previously for individual serums, now for entire batches)
            if serum_count > 0:
                mc.business.add_counted_message("Produced " + mc.business.serum_production_array[production_line][0].name,serum_count*mc.business.batch_size) #Give a note to the player on the end of day screen for how many we made.
                mc.business.serum_production_array[production_line][2] -= serum_count * mc.business.serum_production_array[production_line][0].production_cost
                mc.business.inventory.change_serum(mc.business.serum_production_array[production_line][0],serum_count*mc.business.batch_size) #Add the number serums we made to our inventory.
        if mc.business.supply_count < 0:
            mc.business.supply_count = 0
        return production_amount

    def research_team_building_project_on_day():
        if not mc.business.is_weekend():
            for person in mc.business.research_team:
                person.change_obedience(1)

    def hr_test_project_on_turn():
        renpy.say(None, "Test project on turn")
        return

    def hr_test_project_on_day():
        renpy.say(None, "Test Project on Day")
        return

    def hr_test_project_on_move():
        renpy.say(None, "Test Project on Move")
        return
