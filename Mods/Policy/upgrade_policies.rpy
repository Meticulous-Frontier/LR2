# Contains upgrade modules to policies such as rooms or policies that you want to be toggleable.
# Create them as ModPolicy instead of Policy if you intend for them to be non- standalone aka child elements of a parent policy

init 1400 python: # Room expansions are init 6, base game policies are init 1300
    add_label_hijack("normal_start", "store_mod_policies")
    add_label_hijack("after_load", "store_mod_policies")

init 10 python:


    def create_production_line_requirement():
        if "production_line_addition_2_policy" in globals(): # In case this gets removed or changed
            return purchase_machinery_room_policy.is_owned() and production_line_addition_2_policy.is_owned()
        else:
            return purchase_machinery_room_policy.is_owned()

    def overload_production_lines_requirement():
        return purchase_machinery_room_policy.is_owned() and ("machinery_room_overload" in globals() and machinery_room_overload >= 100)

    def overload_production_lines_on_buy_function(amount):
        global machinery_room_overload
        machinery_room_overload += amount
        if machinery_room_overload < 100:
            machinery_room_overload = 100

    def mandatory_vibe_policy_requirement():
        return maximal_arousal_uniform_policy.is_owned()
    def mandatory_vibe_action_requirement():
        return mandatory_vibe_policy.is_owned() and mc.business.is_open_for_business() # Only run while employees are at work. # Action runs if the policy is owned. Is_owned() checks if it is in the mc.business.policy_list


label store_mod_policies(stack = None):

    python:
        create_production_line_policy = ModPolicy(
            name = "Create Production Line",
            cost = mc.business.production_lines * 5000,
            desc = "Increases the amount of production lines in the [p_division.formalName].\nYou currently have: [mc.business.production_lines]",
            requirement = create_production_line_requirement,
            on_buy_function = add_production_lines, # Find a way to use lists as on_buy_function?
            on_buy_arguments = {"amount": 1},
            alternate_on_buy_arguments = {"amount": -1},
            parent = purchase_machinery_room_policy, # Set the policy you want as a parent here. Clicking the parent in the policy screen will reveal the children ( if any are present )
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
            parent = purchase_machinery_room_policy,
            upgrade = True,
            refresh = "store_mod_policies"
         )

         ###################################################
         # Keep a minimum arousal level for your employees #
         ###################################################

        mandatory_vibe_policy = ModPolicy(
            name = "Attach Bullet Viberator",
            cost = 5000,
            desc = "Ensures a minimum arousal level for your employees\nEnabled: " + (str(mandatory_vibe_policy.is_owned()) if "mandatory_vibe_policy" in globals() else "False"),
            requirement = mandatory_vibe_policy_requirement,
            parent = maximal_arousal_uniform_policy,
            refresh = "store_mod_policies"
        )
        mandatory_vibe_company_action = ActionMod("Attach vibes to outfits", mandatory_vibe_action_requirement, "mandatory_vibe_company_label", priority = 2)
        if mandatory_vibe_company_action not in advance_time_action_list:
            advance_time_action_list.append(mandatory_vibe_company_action)

          ###################################################

    if stack is not None:
        $ execute_hijack_call(stack)
        return

label mandatory_vibe_company_label():
    python:
        for person in mc.business.get_employee_list():
            if person.arousal < 30:
                person.arousal = 30
    return
