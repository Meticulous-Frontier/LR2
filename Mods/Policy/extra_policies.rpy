# Contains upgrade modules to policies such as rooms or policies that you want to be toggleable.
# Create them as ModPolicy instead of Policy if you intend for them to be non- standalone aka child elements of a parent policy
init 1310 python:

    # DISABLED FOR NOW, NEEDS NEW IMPLEMENTATION DUE TO CHANGE IN BUSINESS PRODUCTION LINES
    # def increase_maximum_production(amount):
    #     global production_max
    #     production_max += amount

    # def overload_production_lines_1_policy_requirement():
    #     return production_line_addition_1_policy.is_owned()

    # overload_production_lines_1_policy = Policy(
    #     name = "Production Optimization Level 1",
    #     cost = 10000,
    #     desc = "Increases the maximum efficiency of the production lines by 10 percent",
    #     requirement = overload_production_lines_1_policy_requirement,
    #     on_buy_function = increase_maximum_production,
    #     extra_arguments = {"amount": 10},
    #     dependant_policies = production_line_addition_1_policy
    # )
    # serum_policies_list.append(overload_production_lines_1_policy)

    # def overload_production_lines_2_policy_requirement():
    #     return production_line_addition_2_policy.is_owned()

    # overload_production_lines_2_policy = Policy(
    #     name = "Production Optimization Level 2",
    #     cost = 20000,
    #     desc = "Increases the maximum efficiency of the production lines by 10 percent",
    #     requirement = overload_production_lines_2_policy_requirement,
    #     on_buy_function = increase_maximum_production,
    #     extra_arguments = {"amount": 10},
    #     dependant_policies = production_line_addition_2_policy
    # )
    # serum_policies_list.append(overload_production_lines_2_policy)

    creative_colored_uniform_policy = Policy(
        name = "Relaxed Uniform Color Policy",
        cost = 1000,
        desc = "Employees are given some leeway with the colors of their outfits. While active, employees where your uniform pieces but can select their own colors. Reduces happiness penalties for girls who hate work uniforms.",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )
    uniform_policies_list.append(creative_colored_uniform_policy)

    personal_bottoms_uniform_policy = Policy(
        name = "Relaxed Uniform Bottoms Policy",
        cost = 2000,
        desc = "Employees are given some leeway on uniforms. While active, employees may choose to swap pants for a skirt and vice versa.",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )
    uniform_policies_list.append(personal_bottoms_uniform_policy)

    casual_friday_uniform_policy = Policy(
        name = "Casual Friday Uniform Policy",
        cost = 2000,
        desc = "Employees are free to choose their own uniform on Fridays. This would add some variety on Fridays and prevents uniform infractions.",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )
    uniform_policies_list.append(casual_friday_uniform_policy)

    creative_skimpy_uniform_policy = Policy(
        name = "Uniform Self Expression Policy",
        cost = 10000,
        desc = "Employees are given some leeway on uniforms. While active, employees may choose not to wear a piece or two of the uniform as a form of self expression.",
        toggleable = True,
        own_requirement = corporate_enforced_nudity_policy,
        dependant_policies = corporate_enforced_nudity_policy
    )
    uniform_policies_list.append(creative_skimpy_uniform_policy)

    commando_uniform_policy = Policy(
        name = "Uniform Commando Policy",
        cost = 10000,
        desc = "Employees are no longer allowed to wear bra's or panties with their uniforms.",
        toggleable = True,
        own_requirement = corporate_enforced_nudity_policy,
        dependant_policies = corporate_enforced_nudity_policy
    )
    uniform_policies_list.append(commando_uniform_policy)

    def mandatory_vibe_policy_on_turn():
        if mc.business.is_open_for_business():
            for person in [x for x in mc.business.get_employee_list() if x.arousal < 30]:
                person.arousal = 30

    mandatory_vibe_policy = Policy(
        name = "Mandatory Vibrator Policy",
        cost = 30000,
        desc = "All employees are required to have a bullet vibrator inserted into their vaginas during work hours, ensuring they are aroused at work all the time.",
        toggleable = True,
        own_requirement = maximal_arousal_uniform_policy,
        on_turn_function = mandatory_vibe_policy_on_turn
    )
    uniform_policies_list.append(mandatory_vibe_policy)

    def genetic_modification_policy_requirement():
        return mc.business.research_tier >= 2

    def unlock_genetic_modification():
        rd_division.background_image = standard_biotech_backgrounds
        rd_division.add_action(biotech_modify_person)

    genetic_modification_policy = Policy(
        name = "Genetic Modification License",
        cost = 50000,
        desc = "Allows genetic sequencing of human DNA for cosmetic changes. Requires research Tier 2 unlocked.",
        requirement = genetic_modification_policy_requirement,
        on_buy_function = unlock_genetic_modification,
    )
    organisation_policies_list.append(genetic_modification_policy)

    def genetic_manipulation_policy_requirement():
        return mc.business.research_tier >= 3

    def unlock_genetic_manipulation():
        rd_division.add_action(biotech_clone_person)

    genetic_manipulation_policy = Policy(
        name = "Genetic Experimentation License",
        cost = 100000,
        desc = "Unlock full genetic sequencing of human DNA for cloning purposes, the military is very interested in this technology.  Requires research Tier 3 unlocked.",
        requirement = genetic_manipulation_policy_requirement,
        on_buy_function = unlock_genetic_manipulation,
    )
    organisation_policies_list.append(genetic_manipulation_policy)
