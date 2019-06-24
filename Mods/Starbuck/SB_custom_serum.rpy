
init -1 python:
    def pheremone_therapy_on_apply(the_person, add_to_log):
        the_person.change_slut_core(15, add_to_log, fire_event = False)
        the_person.change_slut_temp(15, add_to_log)

    def pheremone_therapy_on_remove(the_person, add_to_log):
        the_person.change_slut_core(-15, add_to_log, fire_event = False)
        the_person.change_slut_temp(-15, add_to_log)

    def ovulation_function_on_turn(the_person, add_to_log):

        if renpy.random.randint(0,100) <50:  #chance to increase core sluttiness
            the_person.change_slut_core    (1, add_to_log)
        the_person.change_slut_temp(2, add_to_log)

    def constant_stimulation_on_turn(the_person, add_to_log, fire_event = True):
        if renpy.random.randint(0,100) < (the_person.suggestibility - the_person.core_sluttiness) * 5:
            the_person.change_slut_core(1, add_to_log)
            the_person.change_slut_temp(1, add_to_log)

    def dopamine_therapy_on_turn(the_person, add_to_log, fire_event = True):
        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.happiness - 100)) * 5:
            the_person.change_happiness(1, add_to_log)


    def behavior_adjustment_on_turn(the_person, add_to_log, fire_event = True):
        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.obedience - 90)) * 5:
            the_person.change_obedience(1, add_to_log)

    def submission_function_on_apply(the_person, add_to_log):
        the_person.change_slut_core(-15, add_to_log, fire_event = False)
        the_person.change_slut_temp(-15, add_to_log)

    def submission_function_on_remove(the_person, add_to_log):
        the_person.change_slut_core(15, add_to_log, fire_event = False)
        the_person.change_slut_temp(15, add_to_log)

    def submission_function_on_turn(the_person, add_to_log):
        the_person.change_obedience(3, add_to_log)

    def fetish_basic_function_on_turn(the_person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        #the_person.sex_skills["Foreplay"] += 1

        #the_person.sexy_opinions["kissing"] = [2, True]
        if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
            if the_person.sex_skills["Foreplay"] < FETISH_SEX_SKILL_MAX:
                the_person.sex_skills["Foreplay"] += 1

        if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
            SB_random_fetish_key = get_random_from_list( FETISH_BASIC_OPINION_LIST)
            SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
            if SB_random_opinion < FETISH_SEX_SKILL_MAX:
                SB_random_opinion += 1
                the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

    def fetish_exhibition_on_turn(the_person, add_to_log):
        fetish_random_roll_2 = renpy.random.randint(0,100)

        if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
            SB_random_fetish_key = get_random_from_list( FETISH_EXHIBITION_OPINION_LIST)
            SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
            if SB_random_opinion < FETISH_SEX_SKILL_MAX:
                SB_random_opinion += 1
                the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

    def fetish_oral_function_on_turn(the_person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)
        if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
            if the_person.sex_skills["Oral"] < FETISH_SEX_SKILL_MAX:
                the_person.sex_skills["Oral"] += 1

        if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
            SB_random_fetish_key = get_random_from_list( FETISH_ORAL_OPINION_LIST)
            SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
            if SB_random_opinion < 2:
                SB_random_opinion += 1
                the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]


    def fetish_vaginal_function_on_turn(the_person, add_to_log):
        global FETISH_VAGINAL_EVENT_INUSE
        #global FETISH_ANAL_EVENT_INUSE
        #DEBUG Line
        if FETISH_DEBUG_MODE:
            the_person.change_slut_core(15, add_to_log)
            the_person.change_slut_temp(15, add_to_log)
            the_person.change_obedience(15, add_to_log)
            mc.business.funds = 500000


        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)
        if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
            if the_person.sex_skills["Vaginal"] < FETISH_SEX_SKILL_MAX:
                the_person.sex_skills["Vaginal"] += 1


        if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
            SB_random_fetish_key = get_random_from_list( FETISH_VAGINAL_OPINION_LIST)
            SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
            if SB_random_opinion < 2:
                SB_random_opinion += 1
                the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]


        if the_person.sex_skills["Vaginal"] == 5:
            if the_person.get_opinion_score("vaginal sex") == 2:
                if the_person.sluttiness >= 80:
                    if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                        #DEBUG Trigger for vaginal fetish
                        if FETISH_VAGINAL_EVENT_INUSE:
                            the_person.change_slut_core(1, add_to_log = False)
                            the_person.change_slut_temp(1, add_to_log = False)
                        elif the_person == mom:
                            if SB_fetish_mom_vaginal_crisis not in mc.business.mandatory_crises_list:
                                mc.business.mandatory_crises_list.append(SB_fetish_mom_vaginal_crisis)
                                FETISH_VAGINAL_EVENT_INUSE = True
                                SB_SET_RANDOM_EVENT_CHANCE(0)
                        elif the_person == lily:
                            if SB_fetish_lily_vaginal_crisis not in mc.business.mandatory_crises_list:
                                mc.business.mandatory_crises_list.append(SB_fetish_lily_vaginal_crisis)
                                FETISH_VAGINAL_EVENT_INUSE = True
                                SB_SET_RANDOM_EVENT_CHANCE(0)
                        else:
                            if SB_fetish_vaginal_crisis not in mc.business.mandatory_crises_list:
                                SB_fetish_vaginal_crisis.args = [the_person]    # set the current person as action argument
                                mc.business.mandatory_crises_list.append(SB_fetish_vaginal_crisis)
                                FETISH_VAGINAL_EVENT_INUSE = True
                                SB_SET_RANDOM_EVENT_CHANCE(0)
                        #"Vaginal fetish event added"

    def fetish_anal_function_on_turn(the_person, add_to_log):
        global FETISH_ANAL_EVENT_INUSE

        if FETISH_DEBUG_MODE:
            the_person.change_slut_core(15, add_to_log)
            the_person.change_slut_temp(15, add_to_log)
            the_person.change_obedience(15, add_to_log)
            mc.business.funds = 500000

        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)
        if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
            if the_person.sex_skills["Anal"] < FETISH_SEX_SKILL_MAX:
                the_person.sex_skills["Anal"] += 1

        if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
            SB_random_fetish_key = get_random_from_list( FETISH_ANAL_OPINION_LIST)
            SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
            if SB_random_opinion < 2:
                SB_random_opinion += 1
                the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        if the_person.sex_skills["Anal"] >= 5:
            if the_person.get_opinion_score("anal sex") == 2:
                if the_person.sluttiness >= 90:
                    if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                    #"DEBUG Trigger for anal fetish"
                        if FETISH_ANAL_EVENT_INUSE:
                            return
                        elif the_person == lily:
                            if SB_lily_anal_dp_fetish not in mc.business.mandatory_crises_list:
                                mc.business.mandatory_crises_list.append(SB_lily_anal_dp_fetish)
                                FETISH_ANAL_EVENT_INUSE = True
                                SB_SET_RANDOM_EVENT_CHANCE(0)
                            return
                        elif the_person == mom:
                            for mand_event in mc.business.mandatory_crises_list:
                                if mand_event.name == "mom weekly pay":
                                    #renpy.say("","DEBUG: Succesfully located mom event, attempting removal and replacement.")
                                    mc.business.mandatory_crises_list.remove(mand_event)
                                    mc.business.mandatory_crises_list.append(SB_mom_anal_fetish)
                                    FETISH_ANAL_EVENT_INUSE = True
                            return
                        else:
                            if SB_fetish_anal_crisis not in mc.business.mandatory_crises_list:
                                SB_fetish_anal_crisis.args = [the_person]    # set the current person as action argument
                                mc.business.mandatory_crises_list.append(SB_fetish_anal_crisis)
                                FETISH_ANAL_EVENT_INUSE = True
                                SB_SET_RANDOM_EVENT_CHANCE(0)



    def fetish_cum_function_on_turn(the_person, add_to_log):
        global FETISH_CUM_EVENT_INUSE

        if FETISH_DEBUG_MODE:
            the_person.change_slut_core(15, add_to_log)
            the_person.change_slut_temp(15, add_to_log)
            the_person.change_obedience(15, add_to_log)
            mc.business.funds = 500000


        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
            SB_random_fetish_key = get_random_from_list( FETISH_CUM_OPINION_LIST)
            SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
            if SB_random_opinion < 2:
                SB_random_opinion += 1
                the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        if the_person.sex_skills["Oral"] >= 5:
            if SB_get_cum_score(the_person) >= 8:
                if the_person.sluttiness >= 90:
                    # only allow one cum fetish either internal or external
                    if not (SB_check_fetish(the_person, cum_external_role) or SB_check_fetish(the_person, cum_internal_role)):
                        if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                            # renpy.say("", "Evaluate Cum Fetish (In Use: " + str(FETISH_CUM_EVENT_INUSE) + ")")
                            if the_person == lily:
                                if not SB_fetish_lily_cum in mandatory_morning_crises_list:
                                    mandatory_morning_crises_list.append(SB_fetish_lily_cum)
                                if not SB_fetish_lily_cum in mc.business.mandatory_morning_crises_list:
                                    mc.business.mandatory_morning_crises_list.append(SB_fetish_lily_cum)
                            elif FETISH_CUM_EVENT_INUSE:
                                return
                            elif the_person == mom:
                                mc.business.mandatory_crises_list.append(SB_fetish_mom_cum)
                                FETISH_CUM_EVENT_INUSE = True
                            else:
                                # renpy.say("", "Trigger cum fetish " + the_person.name)
                                if SB_fetish_cum_crisis not in mc.business.mandatory_crises_list:
                                    # renpy.say("", "Add trigger to mandatory crisis list " + the_person.name)
                                    SB_fetish_cum_crisis.args = [the_person]
                                    mc.business.mandatory_crises_list.append(SB_fetish_cum_crisis)
                                    FETISH_CUM_EVENT_INUSE = True
                                    SB_SET_RANDOM_EVENT_CHANCE(0)

        ###DEBUGSBEND

label serum_mod_starbuck_traits(stack):
    python:
        pher_ther = SerumTraitMod(name = "Pheremone Therapy",
                desc = "By mimicing pheremones found in closely related animals, this serum can recreate feelings of going into heat in women.",
                positive_slug = "+$40 Value, +15 Sluttiness",
                negative_slug = "+200 Serum Research",
                value_added = 40,
                research_added = 200,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
                on_apply = pheremone_therapy_on_apply,
                on_remove = pheremone_therapy_on_remove,
        #     on_turn = a_function,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 2,
                start_researched =  False,
                research_needed = 800,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        pher_ther.initialize()

        sub_ther = SerumTraitMod(name = "Submission Therapy",
                desc = "Introduces substances that naturally incline females to obey males, found in many mammals. Reduces feeling in the skin, including erogenous zones.",
                positive_slug = "+3 Obedience/Turn, +$20 Value",
                negative_slug = "-15 Sluttiness, +80 Serum Research",
                value_added = 20,
                research_added = 80,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
                on_apply = submission_function_on_apply,
                on_remove = submission_function_on_remove,
                on_turn = submission_function_on_turn,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 2,
                start_researched =  False,
                research_needed = 800,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        sub_ther.initialize()

        ovulation_ther = SerumTraitMod(name = "Hormonal Ovulation",
                desc = "Reproduces hormones naturally occuring during ovulation to make females more receptive to sex. Increases sluttiness over time.",
                positive_slug = "+(0-2) Sluttiness/Turn, +$40 Value",
                negative_slug = "+200 Serum Research",
                value_added = 40,
                research_added = 200,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = ovulation_function_on_turn,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 3,
                start_researched =  False,
                research_needed = 1500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        ovulation_ther.initialize()

        fetish_basic_ther = SerumTraitMod(name = "Initial Fetish Therapy",
                desc = "Over time, increases general positivity towards basic sexual acts.",
                positive_slug = "Slowly increases sexual opinions, Slowly increases Foreplay skill, +$5 Value",
                negative_slug = "+100 Serum Research, +100 Production Cost",
                value_added = 5,
                research_added = 100 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_basic_function_on_turn,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = FETISH_RESEARCH_BASE_TIER,
                start_researched =  False,
                research_needed = 500 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_basic_ther.initialize()

        fetish_exhibition_ther = SerumTraitMod(name = "Exhibitionism Fetish Therapy",
                desc = "Over time, increases the need to behave in an extravagant way in order to attract attention.",
                positive_slug = "Slowly increases exhibionistic behaviour, +$5 Value",
                negative_slug = "+100 Serum Research, +100 Production Cost",
                value_added = 5,
                research_added = 100 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_exhibition_on_turn,
        #     on_day = a_function,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_BASE_TIER,
                start_researched =  False,
                research_needed = 500 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_exhibition_ther.initialize()

        fetish_oral_ther = SerumTraitMod(name = "Oral Fetish Therapy",
                desc = "Over time, increases general positivity towards Oral Sex.",
                positive_slug = "Slowly increases oral sexual opinions, Slowly increases Oral skill, +$5 Value",
                negative_slug = "+300 Serum Research, +100 Production Cost",
                value_added = 5,
                research_added = 300 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_oral_function_on_turn,
        #     on_day = a_function,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_MID_TIER,
                start_researched =  False,
                research_needed = 1000 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_oral_ther.initialize()

        fetish_vaginal_ther = SerumTraitMod(name = "Vaginal Fetish Therapy",
                desc = "Over time, increases general positivity towards Vaginal Sex.",
                positive_slug = "Slowly increases Vaginal sexual opinions, Slowly increases Vaginal skill, +$5 Value",
                negative_slug = "+300 Serum Research, +100 Production Cost",
                value_added = 5,
                research_added = 300 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_vaginal_function_on_turn,
        #     on_day = a_function,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_MID_TIER,
                start_researched =  False,
                research_needed = 1000 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_vaginal_ther.initialize()

        fetish_anal_ther = SerumTraitMod(name = "Anal Fetish Therapy",
                desc = "Over time, increases general positivity towards Anal Sex.",
                positive_slug = "Slowly increases Anal sexual opinions, Slowly increases Anal skill, +$5 Value",
                negative_slug = "+500 Serum Research, +100 Production Cost",
                value_added = 5,
                research_added = 500 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_anal_function_on_turn,
        #     on_day = a_function,
                requires = [fetish_vaginal_ther],
                tier = FETISH_RESEARCH_FINAL_TIER,
                start_researched =  False,
                research_needed = 3000 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_anal_ther.initialize()

        fetish_cum_ther = SerumTraitMod(name = "Cum Fetish Therapy",
                desc = "Over time, increases general positivity towards Cum.",
                positive_slug = "Slowly increases Cum sexual opinions, +$5 Value",
                negative_slug = "+500 Serum Research, +100 Production Cost",
                value_added = 5,
                research_added = 500 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_cum_function_on_turn,
        #     on_day = a_function,
                requires = [fetish_oral_ther],
                tier = FETISH_RESEARCH_FINAL_TIER,
                start_researched =  False,
                research_needed = 3000 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_cum_ther.initialize()

        constant_stimulation_ther = SerumTraitMod(name = "Constant Stimulation",
                desc = "Slowly increases sluttiness. Strong wills can resist it, but it increases effect based on suggestability.",
                positive_slug = "Slowly increases sluttiness based on suggestability, +$10 Value",
                negative_slug = "+100 Serum Research",
                value_added = 10,
                research_added = 100,
        #     slots_added = a_number,
        #     production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 50,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = constant_stimulation_on_turn,
        #     on_day = a_function,
        #     requires = [fetish_oral_ther],
                tier = 1,
                start_researched =  False,
                research_needed = 500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        constant_stimulation_ther.initialize()

        dopamine_therapy_ther = SerumTraitMod(name = "Dopamine Therapy",
                desc = "Slowly increases happiness. Increases effect based on suggestability.",
                positive_slug = "Slowly increases happiness based on suggestability, +$10 Value",
                negative_slug = "+100 Serum Research",
                value_added = 10,
                research_added = 100,
        #     slots_added = a_number,
        #     production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = dopamine_therapy_on_turn,
        #     on_day = a_function,
        #     requires = [fetish_oral_ther],
                tier = 1,
                start_researched =  False,
                research_needed = 500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        dopamine_therapy_ther.initialize()

        behavior_adjustment_ther = SerumTraitMod(name = "Behavior Adjustment",
                desc = "Slowly increases obedience. Increases effect based on suggestability.",
                positive_slug = "Slowly increases obedience based on suggestability, +$10 Value",
                negative_slug = "+100 Serum Research",
                value_added = 10,
                research_added = 100,
        #     slots_added = a_number,
        #     production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = behavior_adjustment_on_turn,
        #     on_day = a_function,
        #     requires = [fetish_oral_ther],
                tier = 1,
                start_researched =  False,
                research_needed = 500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        behavior_adjustment_ther.initialize()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
