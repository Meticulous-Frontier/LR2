#Use these test serums to test the MC serum screen.

init 2 python:
    mc_serum_energy_test = MC_Serum_Trait("Serum: Energy Test", "Low Concentration Sedatives", "energy", [perk_test_energy_01, perk_test_energy_02, perk_test_energy_03], [perk_energy_test_advance_req_01])
    mc_serum_aura_test = MC_Serum_Trait("Serum: Aura Test", "Mood Enhancer", "aura", [perk_test_aura_01, perk_test_aura_02, perk_test_aura_03], [perk_aura_test_advance_req_01])
    mc_serum_cum_test = MC_Serum_Trait("Serum: Cum Test", "Fertility Enhancement", "cum", [perk_test_cum_01, perk_test_cum_02, perk_test_cum_03], [perk_cum_test_advance_req_01])
    mc_serum_physical_test = MC_Serum_Trait("Serum: Physical Test", "Breast Enhancement", "physical", [perk_test_physical_01, perk_test_physical_02, perk_test_physical_03], [perk_physical_test_advance_req_01])

    list_of_mc_traits.append(mc_serum_energy_test)
    list_of_mc_traits.append(mc_serum_aura_test)
    list_of_mc_traits.append(mc_serum_cum_test)
    list_of_mc_traits.append(mc_serum_physical_test)

init 1 python:
    def perk_test_energy_01():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test Energy Perk 1.", bonus_is_temp = True, duration = duration)

    def perk_test_energy_02():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test Energy Perk 2.", bonus_is_temp = True, duration = duration)

    def perk_test_energy_03():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test Energy Perk 3.", bonus_is_temp = True, duration = duration)

    def perk_energy_test_advance_req_01():
        return False

    def perk_test_aura_01():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test aura Perk 1.", bonus_is_temp = True, duration = duration)

    def perk_test_aura_02():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test aura Perk 2.", bonus_is_temp = True, duration = duration)

    def perk_test_aura_03():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test aura Perk 3.", bonus_is_temp = True, duration = duration)

    def perk_aura_test_advance_req_01():
        return False

    def perk_test_cum_01():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test cum Perk 1.", bonus_is_temp = True, duration = duration)

    def perk_test_cum_02():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test cum Perk 2.", bonus_is_temp = True, duration = duration)

    def perk_test_cum_03():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test cum Perk 3.", bonus_is_temp = True, duration = duration)

    def perk_cum_test_advance_req_01():
        return False

    def perk_test_physical_01():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test physical Perk 1.", bonus_is_temp = True, duration = duration)

    def perk_test_physical_02():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test physical Perk 2.", bonus_is_temp = True, duration = duration)

    def perk_test_physical_03():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Test physical Perk 3.", bonus_is_temp = True, duration = duration)

    def perk_physical_test_advance_req_01():
        return False
