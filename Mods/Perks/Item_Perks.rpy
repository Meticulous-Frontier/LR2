init -1 python:
    def male_strapon_on_unlock():
        list_of_positions.append(SB_doggy_anal_dildo_dp)
        doggy.link_positions(SB_doggy_anal_dildo_dp,"transition_doggy_SB_doggy_anal_dildo_dp")
        doggy_anal.link_positions(SB_doggy_anal_dildo_dp,"transition_doggy_anal_SB_doggy_anal_dildo_dp")
        piledriver.link_positions(piledriver_DP,"transition_piledriver_piledriver_DP")
        return

    def male_strapon_save_load():
        if SB_doggy_anal_dildo_dp not in list_of_positions:
            list_of_positions.append(SB_doggy_anal_dildo_dp)
        if SB_doggy_anal_dildo_dp not in doggy.connections:
            doggy.link_positions(SB_doggy_anal_dildo_dp,"transition_doggy_SB_doggy_anal_dildo_dp")
        if SB_doggy_anal_dildo_dp not in doggy_anal.connections:
            doggy_anal.link_positions(SB_doggy_anal_dildo_dp,"transition_doggy_anal_SB_doggy_anal_dildo_dp")
        if piledriver_DP not in piledriver.connections:
            piledriver.link_positions(piledriver_DP,"transition_piledriver_piledriver_DP")
        return

    def male_strapon_unlock(): #This function is wrapper to unlock the male strap on. This is in testing
        item_perk_male_strapon = Item_Perk("A strap on designed to be worn by men. Useful for dual penetration!",
        on_unlock = male_strapon_on_unlock,
        save_load = male_strapon_save_load)

        perk_system.add_item_perk(item_perk_male_strapon, "Male Strapon")

    def dildo_on_unlock():
        standing_finger.link_positions(standing_dildo,"transition_standing_finger_standing_dildo")
        return

    def dildo_save_load():
        if standing_dildo not in standing_finger.connections:
            standing_finger.link_positions(standing_dildo,"transition_standing_finger_standing_dildo")

    def dildo_unlock():
        item_perk_dildo = Item_Perk("A dildo, useful for penetrating any consenting orifice.",
        on_unlock = dildo_on_unlock,
        save_load = dildo_save_load)

        perk_system.add_item_perk(item_perk_dildo, "Dildo")
