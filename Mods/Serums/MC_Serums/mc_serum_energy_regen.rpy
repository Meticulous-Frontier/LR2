#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_energy_regen = MC_Serum_Trait("Serum: Energy Regeneration", "Caffeine Infusion", "energy", [perk_energy_regen_small, perk_energy_regen_med, perk_energy_regen_large], [perk_energy_regen_advance_req_01])

    list_of_mc_traits.append(mc_serum_energy_regen)

init 1 python:  #Associated Perks
    def perk_energy_regen_small_update():
        mc.change_energy(20)
        return

    def perk_energy_regen_med_update():
        mc.change_energy(50)
        return

    def perk_energy_regen_large_update():
        mc.change_energy(mc.max_energy)
        return

    def perk_energy_regen_small():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "You naturally regenerate a small amount of energy throughout the day.", toggle = False, usable = False, update_func = perk_energy_regen_small_update, bonus_is_temp = True, duration = duration)

    def perk_energy_regen_med():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "You naturally regenerate a moderate amount of energy throughout the day. ", toggle = False, usable = False, update_func = perk_energy_regen_med_update, bonus_is_temp = True, duration = duration)

    def perk_energy_regen_large():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "You naturally regenerate a large amount of energy throughout the day. During sex, only lose erection when low on Energy.", toggle = False, usable = False, update_func = perk_energy_regen_large_update, bonus_is_temp = True, duration = duration)

    def perk_energy_regen_advance_req_01():
        return False
