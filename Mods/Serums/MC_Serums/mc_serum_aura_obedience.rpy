#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_aura_obedience = MC_Serum_Trait("Serum: Aura of Compliance", "Low Concentration Sedatives", "aura", [perk_aura_obedience_small, perk_aura_obedience_med, perk_aura_obedience_large], [perk_aura_obedience_advance_req_01])

    list_of_mc_traits.append(mc_serum_aura_obedience)

init 1 python:  #Associated Perks
    def perk_aura_obedience_small_update():
        for person in get_nearby_people():
            if person.obedience < 150:
                person.change_obedience(1, add_to_log = True)
        return

    def perk_aura_obedience_med_update():
        for person in get_nearby_people():
            if person.obedience < 150:
                person.change_obedience(1, add_to_log = True)
            if person.obedience < 200:
                person.change_obedience(1, add_to_log = True)
        return

    def perk_aura_obedience_large_update():
        for person in get_nearby_people():
            if person.obedience < 150:
                person.change_obedience(1, add_to_log = True)
            if person.obedience < 200:
                person.change_obedience(1, add_to_log = True)
            if person.obedience < 250:
                person.change_obedience(1, add_to_log = True)
        return

    def perk_aura_obedience_small():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Girls near you slowly gain obedience up to 150 and never refuse small favors.", usable = False, update_func = perk_aura_obedience_small_update, bonus_is_temp = True, duration = duration)

    def perk_aura_obedience_med():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Girls near you slowly gain obedience up to 200 and never refuse small or medium favors, and have +10 obedience during sex.", usable = False, update_func = perk_aura_obedience_med_update, bonus_is_temp = True, duration = duration)

    def perk_aura_obedience_large():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "Girls near you slowly gain obedience up to 250 and never refuse any favors, have +20 obedience during sex, and never refuse a sex position based on her opinions.", usable = False, update_func = perk_aura_obedience_large_update, bonus_is_temp = True, duration = duration)

    def perk_aura_obedience_advance_req_01():
        return False
