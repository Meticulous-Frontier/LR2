init -3 python:
    FETISH_BASIC_OPINION_LIST = ["giving handjobs", "giving tit fucks", "being fingered", "kissing", "masturbating", "big dicks"]
    FETISH_ANAL_OPINION_LIST = ["anal sex", "doggy style sex", "sex standing up", "anal creampies" ]
    FETISH_ORAL_OPINION_LIST = ["giving blowjobs", "getting head", "drinking cum"]
    FETISH_VAGINAL_OPINION_LIST = ["missionary style sex", "creampies", "sex standing up", "vaginal sex", "doggy style sex"]
    FETISH_CUM_OPINION_LIST = ["drinking cum", "creampies", "anal creampies", "cum facials", "being covered in cum", "bareback sex"]
    #suggestion add exhibitionist fetish and move some of the basic fetishes to this one
    FETISH_EXHIBITION_OPINION_LIST = ["not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "public sex", "lingerie", "skimpy outfits", "skimpy uniforms" ]
    #relation fetishes (impact relationship with people) still need to workout how to make this happen
    FETISH_RELATION_OPTION_LIST = ["cheating on men", "incest"]
    # these fetishes could be used for 'slave' / 'dominatrix'
    FETISH_BDSM_OPTION_LIST = ["being submissive", "taking control"]
    FETISH_BREEDING_OPINION_LIST = ["being submissive", "vaginal sex", "creampies", "bareback sex", "missionary style sex"]

    SB_MOD_MC_AROUSAL_MULT = 1.0     #Default arousal multiplier for the MC
    SB_MOD_MC_AROUSAL_1ST_MULT = 0.9     #Arousal multiplier after the first upgrade
    SB_MOD_MC_AROUSAL_2ND_MULT = 0.8     #Arousal multiplier after second upgrade

    FETISH_VAGINAL_EVENT_LABEL_LIST = [
        "SB_fetish_mom_vaginal_label",
        "SB_fetish_lily_vaginal_label",
        "SB_fetish_vaginal_label",
        "SB_fetish_vaginal_event_label",
    ]

    FETISH_ANAL_EVENT_LABEL_LIST = [
        "SB_lily_anal_dp_fetish_label",
        "SB_mom_anal_pay_label",
        "SB_fetish_anal_label",
        "SB_fetish_anal_label_non_employee",
        "SB_fetish_anal_staylate_event_label",
        "SB_starbuck_anal_intro",
        "SB_stephanie_anal_fetish_label",
    ]

    FETISH_CUM_EVENT_LABEL_LIST = [
        "SB_fetish_mom_cum_label",
        "SB_fetish_lily_cum_label",
        "SB_fetish_cum_label",
        "SB_fetish_cum_non_employee_label",
        "SB_fetish_stephanie_cum_label",
    ]

    FETISH_BREEDING_EVENT_LABEL_LIST = [
        "breeding_fetish_employee_intro_label",
        "breeding_fetish_non_employee_intro_label",
        "breeding_fetish_mom_intro_label",
        "breeding_fetish_lily_intro_label",
        "breeding_fetish_rebecca_intro_label",
        "breeding_fetish_gabrielle_intro_label",
        "breeding_fetish_stephanie_intro_label",
        "breeding_fetish_emily_intro_label",
        "breeding_fetish_christina_intro_label",
        "breeding_fetish_starbuck_intro_label",
        "breeding_fetish_sarah_intro_label",
        "breeding_fetish_ophelia_intro_label",
        "breeding_fetish_erica_intro_label",
        "breeding_fetish_candace_intro_label",
        "breeding_fetish_ashley_intro_label",
    ]

    def SB_FETISH_EVENT_ACTIVE():
        for effect in FETISH_VAGINAL_EVENT_LABEL_LIST + FETISH_ANAL_EVENT_LABEL_LIST + FETISH_CUM_EVENT_LABEL_LIST + FETISH_BREEDING_EVENT_LABEL_LIST:
            if exists_in_mandatory_crisis_list(effect) or exists_in_mandatory_morning_crisis_list(effect):
                return True
        return False
