init -1 python:
    def male_strapon_on_unlock():
        list_of_positions.append(SB_doggy_anal_dildo_dp)
        doggy.link_positions(SB_doggy_anal_dildo_dp,"transition_doggy_SB_doggy_anal_dildo_dp")
        doggy_anal.link_positions(SB_doggy_anal_dildo_dp,"transition_doggy_anal_SB_doggy_anal_dildo_dp")
        return

    def male_strapon_save_load():
        if SB_doggy_anal_dildo_dp not in list_of_positions:
            list_of_positions.append(SB_doggy_anal_dildo_dp)
            doggy.link_positions(SB_doggy_anal_dildo_dp,"transition_doggy_SB_doggy_anal_dildo_dp")
            doggy_anal.link_positions(SB_doggy_anal_dildo_dp,"transition_doggy_anal_SB_doggy_anal_dildo_dp")
        return

    def male_strapon_unlock(): #This function is wrapper to unlock the male strap on. This is in testing
        item_perk_male_strapon = Item_Perk("A strap on designed to be worn by men. Useful for dual penetration!",
        on_unlock = male_strapon_on_unlock,
        save_load = male_strapon_save_load)
        
        perk_system.add_item_perk(item_perk_male_strapon, "Male Strapon")
