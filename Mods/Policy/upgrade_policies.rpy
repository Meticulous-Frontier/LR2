# Contains upgrade modules to policies such as rooms or policies that you want to be toggleable.
# Create them as ModPolicy instead of Policy if you intend for them to be non- standalone aka child elements of a parent policy

init 1400 python: # Room expansions are init 6, base game policies are init 1300
    add_label_hijack("normal_start", "store_mod_policies")
    add_label_hijack("after_load", "store_mod_policies")

init 10 python:
    def create_production_line_requirement():
        if "production_line_addition_2_policy" in globals(): # In case this gets removed or changed
            return p_division_policy.is_owned() and production_line_addition_2_policy.is_owned()
        else:
            return p_division_policy.is_owned()

    def overload_production_lines_requirement():
        return p_division_policy.is_owned() and ("machinery_room_overload" in globals() and machinery_room_overload >= 100)

    def overload_production_lines_on_buy_function(amount):
        global machinery_room_overload
        machinery_room_overload += amount
        if machinery_room_overload < 100:
            machinery_room_overload = 100

    def mandatory_vibe_policy_requirement():
        return maximal_arousal_uniform_policy.is_owned()

    def mandatory_vibe_action_requirement():
        # Only run while employees are at work. # Action runs if the policy is owned. Is_owned() checks if it is in the mc.business.policy_list
        if mc.business.is_open_for_business():
            policy = get_from_policy_list(mandatory_vibe_policy)
            if policy:
                return policy.is_owned() and policy.enabled
        return False

    def body_customizer_policy_requirement():
        return rd_division_policy.is_owned()

    body_customizer_action = Action("Modify Person", body_customizer_policy_requirement, "body_customizer_action_label", menu_tooltip = "Bring a person in for modifications")
    mandatory_vibe_company_action = ActionMod("Attach vibes to outfits", mandatory_vibe_action_requirement, "mandatory_vibe_company_label", priority = 2, enabled = False, allow_disable = False, category = "Business")

label store_mod_policies(stack = None):

    python: # NOTE: Feel free to rename things and change the costs up.

        body_customizer_policy = ModPolicy(
            name = "Genetic Manipulation Permit",
            cost = 15000,
            desc = "Allows the modification of DNA on human subjects with the intent of cosmetic changes in the [rd_division.formalName]",
            requirement = body_customizer_policy_requirement,
            on_buy_function = rd_division.add_action,
            on_buy_arguments = {"act": body_customizer_action},
            parent = rd_division_policy

        )
        create_production_line_policy = ModPolicy(
            name = "Create Production Line",
            cost = mc.business.production_lines * 5000,
            desc = "Increases the amount of production lines in the [p_division.formalName].\nYou currently have: [mc.business.production_lines]",
            requirement = create_production_line_requirement,
            on_buy_function = add_production_lines, # Find a way to use lists as on_buy_function?
            on_buy_arguments = {"amount": 1},
            alternate_on_buy_arguments = {"amount": -1},
            parent = p_division_policy, # Set the policy you want as a parent here. Clicking the parent in the policy screen will reveal the children ( if any are present )
            upgrade = True,
            refresh = "store_mod_policies" # Set this to the function that creates it
         )

        overload_production_lines_policy = ModPolicy(
            name = "Overload Production Lines",
            cost = (machinery_room_overload % 100) * 1000,
            desc = "Increases the maximum efficiency of the production lines in [p_division.formalName].\nYou currently have: [machinery_room_overload]% Max",
            requirement = overload_production_lines_requirement,
            on_buy_function = overload_production_lines_on_buy_function,
            on_buy_arguments = {"amount": 10},
            alternate_on_buy_arguments = {"amount": -10}, # Arguments sent on a right click. Usually a decrease. Free right now, add a refund / cost to it?
            parent = p_division_policy,
            upgrade = True,
            refresh = "store_mod_policies"
         )

         ###################################################
         # Keep a minimum arousal level for your employees #
         ###################################################

        mandatory_vibe_policy = ModPolicy(
            name = "Attach Bullet Vibrator",
            cost = 5000,
            desc = "Ensures a minimum arousal level for your employees\nEnabled: " + str(mandatory_vibe_action_requirement()),
            requirement = mandatory_vibe_policy_requirement,
            parent = maximal_arousal_uniform_policy,
            refresh = "store_mod_policies"
        )
        if mandatory_vibe_company_action not in advance_time_action_list:
            advance_time_action_list.append(mandatory_vibe_company_action)

          ###################################################

        if not stack is None:
            execute_hijack_call(stack)
    return

label mandatory_vibe_company_label():
    python:
        for person in mc.business.get_employee_list():
            if person.arousal < 30:
                person.arousal = 30
    return

label body_customizer_action_label():
    while True:
        $ people_list = get_sorted_people_list(known_people_in_the_game([mc]), "Modify Person", ["Back"])

        if "build_menu_items" in globals():
            call screen main_choice_display(build_menu_items([people_list]))
        else:
            call screen main_choice_display([people_list])
        $ person_choice = _return
        $ del people_list

        if person_choice == "Back":
            return # Where to go if you hit "Back".
        else:
            show screen body_customizer(person_choice)
    return
