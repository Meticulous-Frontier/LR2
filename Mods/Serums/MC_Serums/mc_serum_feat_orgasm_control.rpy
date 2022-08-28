#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_feat_orgasm_control = MC_Serum_Trait("Serum: Feat of Orgasm Control", "Pleasure Center Stimulator", "physical", [perk_feat_orgasm_control_small, perk_feat_orgasm_control_med, perk_feat_orgasm_control_large], [perk_feat_orgasm_control_advance_req_01])

    list_of_mc_traits.append(mc_serum_feat_orgasm_control)

init 1 python:  #Associated Perks

    def perk_feat_orgasm_control_on_apply():
        config.label_overrides["climax_check"] = "climax_check_orgasm_control"
        return

    def perk_feat_orgasm_control_on_remove():
        del config.label_overrides["climax_check"]
        return

    def perk_feat_orgasm_control_small():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "During sex, you can hold off orgasm indefinitely, but orgasms cost 20 energy.", toggle = False, usable = False, update_func = perk_feat_orgasm_control_small_update, bonus_is_temp = True, duration = duration)

    def perk_feat_orgasm_control_med():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "During sex, cum early or hold off indefinitely, but orgasms cost 20 energy.", toggle = False, usable = False, update_func = perk_feat_orgasm_control_med_update, bonus_is_temp = True, duration = duration)

    def perk_feat_orgasm_control_large():
        duration = get_mc_serum_duration()
        return Ability_Perk(description = "During sex, cum early or hold off indefinitely, and once per day you can quickly orgasm during a conversation before the other person can react. Orgasms cost 20 energy.", toggle = False, usable = False, update_func = perk_feat_orgasm_control_large_update, bonus_is_temp = True, duration = duration)

    def perk_feat_orgasm_control_advance_req_01():
        return False

label climax_check_orgasm_control():
    $ is_cumming = False
    "Your pleasure is growing. You could cum now, if you decide to."
    menu:
        "Cum now":
            "You focus on the pleasure and let yourself go."
            $ mc.change_energy(-20)
            return True
        "Delay orgasm":
            "You put off your orgasm for a bit longer."
            return False

    return is_cumming
