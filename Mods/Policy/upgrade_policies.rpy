# Contains upgrade modules to policies such as rooms or policies that you want to be toggleable.
# Create them as ModPolicy instead of Policy if you intend for them to be non- standalone aka child elements of a parent policy
# NOTE: ModPolicy takes a list of on_buy_functions

init 10 python: # Room expansions are init 6
    add_label_hijack("normal_start", "store_mod_policies")
    add_label_hijack("after_load", "store_mod_policies")

init -1 python:


    def create_production_line_requirement():
        if "production_line_addition_2_policy" in globals(): # In case this gets removed or changed
            return purchase_machinery_room_policy.is_owned() and production_line_addition_2_policy.is_owned()
        else:
            return purchase_machinery_room_policy.is_owned()

    def reset_mod_policy(policy): # Makes it so the policy can be purchased again
        if policy in mc.business.policy_list:
            mc.business.policy_list.remove(policy)
        renpy.restart_interaction() # Refresh text



label store_mod_policies(stack = None):

    python:
        create_production_line_policy = ModPolicy(
            name = "Upgrade [p_division_basement.formalName]",
            cost = mc.business.production_lines * 5000,
            desc = "Increases the amount of production lines in the [p_division.formalName].\nYou currently have: [mc.business.production_lines]",
            requirement = create_production_line_requirement,
            on_buy_function = add_production_lines, # Find a way to use lists as on_buy_function
            on_buy_arguments = {"amount": 1}, # Make this less weird and more useful instead. As it is you can only match one argument to each function
            parent = purchase_machinery_room_policy, # Set the policy you want as a parent here. Clicking the parent in the policy screen will reveal the children ( if any are present )
            upgrade = True,
            refresh = "store_mod_policies" # Set this to the function that creates it
         )

    if stack is not None:
        $ execute_hijack_call(stack)
        return
