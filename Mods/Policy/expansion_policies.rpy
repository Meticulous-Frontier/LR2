init 6 python:
    add_label_hijack("normal_start", "store_expansion_policies")
    add_label_hijack("after_load", "store_expansion_policies")

init 1300 python:
    expansion_policies_list = []

init -1 python:

    def purchase_room_requirement(): #Would like to see if the room has already been purchased, but that shouldn't be nescessary on new saves.
        return True


label store_expansion_policies(stack):

    python:
        purchase_machinery_room_policy = Policy(
            name = "[p_division_basement.formalName]", # NOTE: Do not use e.g "[room.formalName] as it breaks the hash check"
            cost = 20000,
            desc = "Gives you access to the [p_division_basement.formalName] where you can further increase the productivity of your business.",
            requirement = purchase_room_requirement,
            on_buy_function = purchase_room_on_buy_function,
            on_buy_arguments = {"room": p_division_basement})

        if purchase_machinery_room_policy not in expansion_policies_list:
            expansion_policies_list.append(purchase_machinery_room_policy)

        purchase_biotech_lab_room_policy = Policy(
            name = "[rd_division_basement.formalName]",
            cost = 20000,
            desc = "Gives you access to the [rd_division_basement.formalName] where you can clone people or do genetic manipulations in order to change appearance.",
            requirement = purchase_room_requirement,
            on_buy_function = purchase_room_on_buy_function,
            on_buy_arguments = {"room": rd_division_basement}
        )

        if purchase_biotech_lab_room_policy not in expansion_policies_list:
            expansion_policies_list.append(purchase_biotech_lab_room_policy)

        purchase_security_room_policy = Policy(
            name = "[m_division_basement.formalName]",
            cost = 20000,
            desc = "Gives you access to the [m_division_basement.formalName] where you can oversee your employees, investigate their opinions and home location.",
            requirement = purchase_room_requirement,
            on_buy_function = purchase_room_on_buy_function,
            on_buy_arguments = {"room": m_division_basement}
        )

        if purchase_security_room_policy not in expansion_policies_list:
            expansion_policies_list.append(purchase_security_room_policy)

        purchase_dungeon_room_policy = Policy(
            name = "[office_basement.formalName]",
            cost = 5000,
            desc = "Gives you access to the [office_basement.formalName] where *undecided*",
            requirement = purchase_room_requirement,
            on_buy_function = purchase_room_on_buy_function,
            on_buy_arguments = {"room": office_basement}
        )

        if purchase_dungeon_room_policy not in expansion_policies_list:
            expansion_policies_list.append(purchase_dungeon_room_policy)

        # purchase_biotech_lab_room_policy = Policy(
        #     name = ,
        #     cost = ,
        #     desc = ,
        #     requirement = ,
        #     on_buy_function = ,
        #     on_buy_arguments = {"room": }
        # )


        if ["Expansion Rooms", expansion_policies_list] not in policy_selection_screen_categories:
            policy_selection_screen_categories.append(["Expansion Rooms", expansion_policies_list]) # NOTE: Put this at the bottom so it gets appended after all policies have been created.

    $ execute_hijack_call(stack)
    return
