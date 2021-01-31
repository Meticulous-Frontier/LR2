# Contains upgrade modules to policies such as rooms or policies that you want to be toggleable.
# Create them as ModPolicy instead of Policy if you intend for them to be non- standalone aka child elements of a parent policy
init 1310 python:

    def increase_maximum_production(amount):
        global production_max
        production_max += amount

    def overload_production_lines_1_policy_requirement():
        return production_line_addition_1_policy.is_owned()

    overload_production_lines_1_policy = Policy(
        name = "Production Optimization Level 1",
        cost = 10000,
        desc = "Increases the maximum efficiency of the production lines by 10 percent",
        requirement = overload_production_lines_1_policy_requirement,
        on_buy_function = increase_maximum_production,
        extra_arguments = {"amount": 10},
        dependant_policies = production_line_addition_1_policy
    )
    serum_policies_list.append(overload_production_lines_1_policy)

    def overload_production_lines_2_policy_requirement():
        return production_line_addition_2_policy.is_owned()

    overload_production_lines_2_policy = Policy(
        name = "Production Optimization Level 2",
        cost = 20000,
        desc = "Increases the maximum efficiency of the production lines by 10 percent",
        requirement = overload_production_lines_2_policy_requirement,
        on_buy_function = increase_maximum_production,
        extra_arguments = {"amount": 10},
        dependant_policies = production_line_addition_2_policy
    )
    serum_policies_list.append(overload_production_lines_2_policy)

    def mandatory_vibe_policy_requirement():
        return maximal_arousal_uniform_policy.is_owned()

    def mandatory_vibe_policy_on_turn():
        if mc.business.is_open_for_business():
            for person in [x for x in mc.business.get_employee_list() if x.arousal < 30]:
                person.arousal = 30

    mandatory_vibe_policy = Policy(
        name = "Mandatory Vibrator Policy",
        cost = 30000,
        desc = "All employees are required to have a bullet vibrator inserted into their vaginas during work hours, ensuring they are aroused at work all the time.",
        toggleable = True,
        requirement = mandatory_vibe_policy_requirement,
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




    # def body_customizer_policy_requirement():
    #     return rd_division_policy.is_owned()

    # body_customizer_policy = Policy(
    #     name = "Genetic Manipulation Permit",
    #     cost = 15000,
    #     desc = "Allows the modification of DNA on human subjects with the intent of cosmetic changes in the [rd_division.formalName]",
    #     requirement = body_customizer_policy_requirement,
    #     on_buy_function = rd_division.add_action,
    #     extra_arguments = {"act": body_customizer_action},
    #     parent = rd_division_policy

    # body_customizer_action = Action("Modify Person", body_customizer_policy_requirement, "body_customizer_action_label", menu_tooltip = "Bring a person in for modifications")


# label body_customizer_action_label():
#     while True:
#         $ people_list = get_sorted_people_list(known_people_in_the_game(), "Modify Person", ["Back"])

#         call screen enhanced_main_choice_display(build_menu_items([people_list]))
#         $ person_choice = _return
#         $ del people_list

#         if person_choice == "Back":
#             return # Where to go if you hit "Back".
#         else:
#             show screen body_customizer(person_choice)
#     return
