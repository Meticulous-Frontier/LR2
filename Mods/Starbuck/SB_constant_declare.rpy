init -3 python:
    FETISH_DEBUG_MODE = False #A basic cheat mode, makes it easy to test fetish serums
    FETISH_OPINION_MAX = 2
    FETISH_SEX_SKILL_MAX = 5
    FETISH_SKILL_RAISE_CHANCE = 50
    FETISH_DEVELOPMENT_CHANCE = 50
    FETISH_BASIC_OPINION_LIST = ["giving handjobs", "being fingered", "kissing", "masturbating", "big dicks"]
    FETISH_ANAL_OPINION_LIST = ["anal sex", "doggy style sex", "showing her ass", "sex standing up", "anal creampies" ]
    FETISH_ORAL_OPINION_LIST = ["giving blowjobs", "getting head", "drinking cum"]
    FETISH_VAGINAL_OPINION_LIST = ["missionary style sex", "creampies", "sex standing up", "vaginal sex", "doggy style sex", "being fingered"]
    FETISH_CUM_OPINION_LIST = ["drinking cum", "creampies", "anal creampies", "cum facials", "being covered in cum", "bareback sex"]
    #suggestion add exhibitionist fetish and move some of the basic fetishes to this one
    FETISH_EXHIBITION_OPINION_LIST = ["not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "public sex", "lingerie", "skimpy outfits", "skimpy uniforms" ]
    #relation fetishes (impact relationship with people) still need to workout how to make this happen
    FETISH_RELATION_OPTION_LIST = ["cheating on men", "incest"]
    # these fetishes could be used for 'slave' / 'dominatrix'
    FETISH_BDSM_OPTION_LIST = ["being submissive", "taking control"]

    FETISH_EVENT_TARGET = None
    #global FETISH_VAGINAL_EVENT_INUSE, FETISH_ANAL_EVENT_INUSE
    FETISH_VAGINAL_EVENT_INUSE = False
    FETISH_ANAL_EVENT_INUSE = False
    FETISH_CUM_EVENT_INUSE = False
    FETISH_RESEARCH_PERCENT = 1     #1 = 100%
    FETISH_RESEARCH_BASE_TIER = 1        #Default = 1
    FETISH_RESEARCH_MID_TIER = 1          #Default = 2
    FETISH_RESEARCH_FINAL_TIER = 2      #Default = 3
    FETISH_PRODUCTION_COST = 20     #Default 100
    FETISH_OPINION_VALUE = 2       #To work on balance issues#
    SB_MOD_RANDOM_EVENT_CHANCE = 20
    SB_MOD_DEFAULT_RANDOM_EVENT_CHANCE = 20
    SB_MOD_MC_AROUSAL_MULT = 1.0     #Default arousal multiplier for the MC
    SB_MOD_MC_AROUSAL_1ST_MULT = 0.9     #Arousal multiplier after the first upgrade
    SB_MOD_MC_AROUSAL_2ND_MULT = 0.8     #Arousal multiplier after second upgrade

    if FETISH_DEBUG_MODE:
        FETISH_RESEARCH_PERCENT = .01     #1 = 100%
        FETISH_RESEARCH_BASE_TIER = 0        #Default = 1
        FETISH_RESEARCH_MID_TIER = 0          #Default = 2
        FETISH_RESEARCH_FINAL_TIER = 0      #Default = 3
        FETISH_PRODUCTION_COST = 5     #Default 100
        FETISH_OPINION_VALUE = 10       #To work on balance issues#
        FETISH_SKILL_RAISE_CHANCE = 100
        FETISH_DEVELOPMENT_CHANCE = 100

    def SB_CALCULATE_RANDOM_EVENT_RATE():
        global SB_MOD_RANDOM_EVENT_CHANCE
        SB_MOD_RANDOM_EVENT_CHANCE = SB_MOD_DEFAULT_RANDOM_EVENT_CHANCE
        return

    def SB_SET_RANDOM_EVENT_CHANCE(chance_percent):
        global SB_MOD_RANDOM_EVENT_CHANCE
        SB_MOD_RANDOM_EVENT_CHANCE = chance_percent
        return
