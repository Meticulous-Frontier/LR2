#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_cum_obedience = MC_Serum_Trait("Serum: Seed of Submission", "Obedience Enhancer", "cum", [perk_cum_obedience_small, perk_cum_obedience_med, perk_cum_obedience_large], [perk_cum_obedience_advance_req_01])

    list_of_mc_traits.append(mc_serum_cum_obedience)

init 1 python:  #Associated Perks
    def perk_cum_obedience_small_on_cum(the_person, the_place):
        if the_person.obedience < 150:
            the_person.change_obedience(5, add_to_log = True)
            if the_person.obedience > 150:
                the_person.obedience = 150
        return

    def perk_cum_obedience_med_on_cum(the_person, the_place):
        if the_person.obedience < 200:
            the_person.change_obedience(10, add_to_log = True)
            if the_person.obedience > 200:
                the_person.obedience = 200
        the_person.increase_opinion_score(the_place, max_value = 0)
        return

    def perk_cum_obedience_large_on_cum(the_person, the_place):
        if the_person.obedience < 250:
            the_person.change_obedience(20, add_to_log = True)
            if the_person.obedience > 250:
                the_person.obedience = 250
        the_person.increase_opinion_score(the_place, max_value = 2)
        if not the_person.is_in_trance():
            the_person.increase_trance(show_dialogue = True, reset_arousal = False, add_to_log = True)
        return

    def perk_cum_obedience_small():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "When exposed to your cum, girls gain up to 5 obedience, to a maximum of 150.", toggle = False, usable = False, cum_func = perk_cum_obedience_small_on_cum, bonus_is_temp = True, duration = duration)

    def perk_cum_obedience_med():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "When exposed to your cum, girls gain up to 10 obedience, to a maximum of 200 and if disliked, her opinion of the cumshot is shifted positively.", toggle = False, usable = False, cum_func = perk_cum_obedience_med_on_cum, bonus_is_temp = True, duration = duration)

    def perk_cum_obedience_large():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "When exposed to your cum, girls gain up to 20 obedience, to a maximum of 250 and her opinion of the cumshot is shifted positively. If she isn't already in a trance, she is put in one.", toggle = False, usable = False, cum_func = perk_cum_obedience_large_on_cum, bonus_is_temp = True, duration = duration)

    def perk_cum_obedience_advance_req_01():
        return False
