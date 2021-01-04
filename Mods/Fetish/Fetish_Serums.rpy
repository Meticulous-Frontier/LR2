init -3 python:
    FETISH_BASIC_OPINION_LIST = ["giving handjobs", "giving tit fucks", "being fingered", "kissing", "masturbating", "big dicks", "getting head", "lingerie"]
    FETISH_ANAL_OPINION_LIST = ["anal sex", "doggy style sex", "anal creampies", "being submissive"]
    FETISH_ORAL_OPINION_LIST = []
    FETISH_VAGINAL_OPINION_LIST = []
    FETISH_CUM_OPINION_LIST = ["being covered in cum","drinking cum", "cum facials", "giving blowjobs", "taking control"]
    FETISH_BREEDING_OPINION_LIST = ["bareback sex","vaginal sex", "creampies", "lactation", "missionary style sex"]
    FETISH_EXHIBITION_OPINION_LIST = ["public sex", "not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "skimpy outfits", "skimpy uniforms", "sex standing up" ]
    #relation fetishes (impact relationship with people) still need to workout how to make this happen
    FETISH_RELATION_OPTION_LIST = ["cheating on men", "incest"]
    # these fetishes could be used for 'slave' / 'dominatrix'
    FETISH_BDSM_OPTION_LIST = ["being submissive", "taking control"]


init -2 python:
    def get_suggest_tier(person):   #Returns a value of 0-3 depending on the person's suggestibility.
        if person.suggestibility < 15:
            return 0
        elif person.suggestibility < 35:
            return 1
        elif person.suggestibility < 55:
            return 2
        elif person.suggestibility < 75:
            return 3
        else:
            return 4 #Edge case, has suggestibility not yet in game

    def get_slut_tier(person):   #returns the heart value of the person
        if person.core_sluttiness < 20:
            return 0
        elif person.core_sluttiness < 40:
            return 1
        elif person.core_sluttiness < 60:
            return 2
        elif person.core_sluttiness < 80:
            return 3
        elif person.core_sluttiness < 100:
            return 4
        else:
            return 5


init -1 python:
    def is_fetish_after_hours_available():
        if mc.business.event_triggers_dict.get("fetish_after_hours_available", True) == True:
            return True
        return False

    def fetish_after_hours_lock():
        mc.business.event_triggers_dict["fetish_after_hours_available"] = False
        return

    def fetish_after_hours_unlock():
        mc.business.event_triggers_dict["fetish_after_hours_available"] = True
        return

    def fetish_serum_unlock_count():
        return mc.business.event_triggers_dict.get("fetish_serum_count", 0)


    def start_anal_fetish_quest(the_person):
        return False #For now disable this
        if person is lily:
            add_SB_lily_anal_dp_fetish_event()
            return True
        elif person is mom:
            mom_weekly_pay = exists_in_mandatory_morning_crisis_list("mom_weekly_pay_label")
            if mom_weekly_pay: # replace default mom weekly pay with new event
                # renpy.say("", "Replacing default mom weekly pay event")
                mc.business.mandatory_morning_crises_list.remove(mom_weekly_pay)
                add_mom_anal_fetish_event()
                return True
        elif person is starbuck:
            if starbuck.shop_investment_rate == 6.0:
                add_sb_starbuck_anal_intro_event()
                return True
        elif person is stephanie and person.has_role(head_researcher) and person.personality != bimbo_personality:
            add_stephanie_anal_fetish_action()
            return True
        elif person.is_employee():
            if is_fetish_after_hours_available():
                fetish_after_hours_lock()
                add_sb_fetish_anal_crisis(person)
            return True
        else:
            add_sb_fetish_anal_crisis_non_employee(person)
            return True
        return False

    def start_breeding_fetish_quest(the_person):
        return False #For now disable this
        #Determine who it is, then add the appropriate quest.
        if persistent.pregnancy_pref == 0:
            return False
        if the_person is mom:
            if breeding_fetish_mom_intro not in mc.business.mandatory_morning_crises_list:
                mc.business.mandatory_morning_crises_list.append(breeding_fetish_mom_intro)
                return True
        elif the_person is lily:
            lily.add_unique_on_room_enter_event(breeding_fetish_lily_intro)
            return True
        elif the_person is aunt:
            pass
        elif the_person is cousin:
            pass
        elif the_person is stephanie:
            if breeding_fetish_stephanie_intro not in mc.business.mandatory_morning_crises_list:
                mc.business.mandatory_morning_crises_list.append(breeding_fetish_stephanie_intro)
                return True
        elif the_person is emily:
            pass
        elif the_person is christina:
            pass
        elif the_person is starbuck:
            if breeding_fetish_starbuck_intro not in mc.business.mandatory_morning_crises_list:
                mc.business.mandatory_morning_crises_list.append(breeding_fetish_starbuck_intro)
                return True
        elif the_person is sarah:
            if breeding_fetish_sarah_intro not in mc.business.mandatory_morning_crises_list:
                mc.business.mandatory_morning_crises_list.append(breeding_fetish_sarah_intro)
                return True
        elif the_person is salon_manager:
            pass
        elif the_person is erica:
            pass
        elif "candace" in globals() and the_person is candace:
            candace.add_unique_on_room_enter_event(breeding_fetish_candace_intro)
            return True
        elif the_person is ashley:
            pass
        elif the_person.is_employee():
            if is_fetish_after_hours_available():
                fetish_after_hours_lock()
                breeding_fetish_employee_intro = Action("Employee breeding fetish intro", breeding_fetish_employee_intro_requirement, "breeding_fetish_employee_intro_label", args = the_person)
                mc.business.mandatory_crises_list.append(breeding_fetish_employee_intro)
                return True
        else:
            pass

        return

    def start_cum_fetish_quest(the_person):
        return False #For now disable this
        if the_person is lily:
            add_sb_fetish_lily_cum_event()
            return True
        elif the_person is mom:
            add_sb_fetish_mom_cum_event()
            return True
        elif the_person is stephanie and person.has_role(head_researcher) and person.personality != bimbo_personality:
            add_sb_fetish_stephanie_cum_event()
            return True
        elif the_person.is_employee():
            add_sb_fetish_cum_crisis(person)
            return True
        else:
            add_sb_fetish_cum_crisis_non_employee(person)
            return True
        return False

    def start_exhbition_fetish_quest(the_person):
        return False #None of them are written yet

    def fetish_serum_increase_opinion(opinion_list, max_new_score, the_person, add_to_log = False): #WE purposefully increase a score EVERY time this function is used instead of RNG
        avail_opinions = []
        for opinion in opinion_list:
            if the_person.get_opinion_score(opinion) < max_new_score:
                avail_opinions.append(opinion)
        if len(avail_opinions) > 0:
            the_person.increase_opinion_score(get_random_from_list(avail_opinions), max_value = max_new_score, add_to_log = add_to_log)
            return True #Return true if we increased an opinion
        return False

    def fetish_serum_roll_fetish_chance(opinion_list, person):
        fetish_odds = (get_suggest_tier(person) * 20) #Up to 60 points based on suggestability
        opinion_modifier = 0
        for opinion in opinion_list:
            opinion_modifier += (person.get_opinion_score(opinion) * 20)
        opinion_modifier = opinion_modifier / (len(opinion_list))
        fetish_odds += int(opinion_modifier)
        return fetish_odds


    def fetish_basic_function_on_apply(person, add_to_log):
        fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, get_suggest_tier(person) - 1, person)
        return

    def fetish_anal_function_on_apply(person, add_to_log):
        if fetish_serum_increase_opinion(FETISH_ANAL_OPINION_LIST, get_suggest_tier(person) - 1, person):
            return
        if person.get_opinion_score(FETISH_ANAL_OPINION_LIST[0]) >= 2 and not person.has_started_anal_fetish() and person.core_sluttiness > 60:
            if fetish_serum_roll_fetish_chance(FETISH_ANAL_OPINION_LIST, person) > renpy.random.randint(0,100):
                if start_anal_fetish_quest(person):
                    person.event_triggers_dict["anal_fetish_start"] = True
                    #TODO some kind of test here to indicate to the player that their anal quest has started
                else:
                    #TODO throw some kind of error here to indicate that I haven't created this scenario yet
                    pass
        return

    def fetish_breeding_function_on_apply(person, add_to_log):
        if fetish_serum_increase_opinion(FETISH_BREEDING_OPINION_LIST, get_suggest_tier(person) - 1, person):
            return
        if person.get_opinion_score(FETISH_BREEDING_OPINION_LIST[0]) >= 2 and not person.has_started_breeding_fetish() and person.core_sluttiness > 60:
            if fetish_serum_roll_fetish_chance(FETISH_BREEDING_OPINION_LIST, person) > renpy.random.randint(0,100):
                if start_breeding_fetish_quest(person):
                    person.event_triggers_dict["breeding_fetish_start"] = True
                    #TODO some kind of test here to indicate to the player that their breeding quest has started
                else:
                    #TODO throw some kind of error here to indicate that I haven't created this scenario yet
                    pass

        if persistent.pregnancy_pref == 0:
            return

        if fetish_serum_roll_fetish_chance(FETISH_BREEDING_OPINION_LIST, person) >= 50 and person.on_birth_control:
            person.on_birth_control = False
            person.add_unique_on_talk_event(breeding_fetish_going_off_BC)
        return

    def fetish_cum_function_on_apply(person, add_to_log):
        if fetish_serum_increase_opinion(FETISH_CUM_OPINION_LIST, get_suggest_tier(person) - 1, person):
            return
        if person.get_opinion_score(FETISH_CUM_OPINION_LIST[0]) >= 2 and not person.has_started_cum_fetish() and person.core_sluttiness > 60:
            if fetish_serum_roll_fetish_chance(FETISH_CUM_OPINION_LIST, person) > renpy.random.randint(0,100):
                if start_cum_fetish_quest(person):
                    person.event_triggers_dict["cum_fetish_start"] = True
                    #TODO some kind of test here to indicate to the player that their cum quest has started
                else:
                    #TODO throw some kind of error here to indicate that I haven't created this scenario yet
                    pass
        return

    def fetish_exhibition_function_on_apply(person, add_to_log):
        if fetish_serum_increase_opinion(FETISH_EXHIBITION_OPINION_LIST, get_suggest_tier(person) - 1, person):
            return
        if person.get_opinion_score(FETISH_EXHIBITION_OPINION_LIST[0]) >= 2 and not person.has_started_exhibition_fetish():
            if fetish_serum_roll_fetish_chance(FETISH_EXHIBITION_OPINION_LIST, person) > renpy.random.randint(0,100):
                if start_exhbition_fetish_quest(person):
                    person.event_triggers_dict["exhibition_fetish_start"] = True
                    #TODO some kind of test here to indicate to the player that their exhibitionism quest has started
                else:
                    #TODO throw some kind of error here to indicate that I haven't created this scenario yet
                    pass
        return

    def fetish_anal_function_on_turn(person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)

        tier = get_suggest_tier(person)
        if fetish_random_roll_1 < 10 + (tier * 5):
            person.increase_sex_skill("Anal", 2 + tier)

        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.obedience - 90)) * 3:
            the_person.change_obedience(1, add_to_log)
        return

    def fetish_breeding_function_on_turn(person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)
        tier = get_suggest_tier(person)
        if fetish_random_roll_1 < 10 + (tier * 5):
            person.increase_sex_skill("Vaginal", 2 + tier)
        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.happiness - 100)) * 3:
            the_person.change_happiness(1, add_to_log)

        return

    def fetish_cum_function_on_turn(person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)
        tier = get_suggest_tier(person)
        if fetish_random_roll_1 < 10 + (tier * 5):
            person.increase_sex_skill("Oral", 2 + tier)
        if person.sluttiness < person.suggestibility:
            if renpy.random.randint(0,100) < (30 - (person.suggestibility - person.sluttiness)):
                the_person.change_slut_temp(1, add_to_log)
        return

    def fetish_exhibition_on_turn(person, add_to_log):
        if person.sluttiness < person.suggestibility:
            if renpy.random.randint(0,100) < (30 - (person.suggestibility - person.sluttiness)):
                the_person.change_slut_temp(1, add_to_log)
        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.obedience - 90)) * 3:
            the_person.change_obedience(1, add_to_log)
        return

    def fetish_basic_function_on_turn(person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)

        tier = get_suggest_tier(person)
        if fetish_random_roll_1 < 10 + (tier * 5):
            person.increase_sex_skill("Foreplay", 2 + tier)
        return

    def fetish_unlock_basic_serum():
        found = find_in_list(lambda x: x.name == "Sexual Proclivity Nanobots", list_of_traits)
        if found:
            found.tier = 1
            mc.business.event_triggers_dict["fetish_serum_count"] = 1
        return

    def fetish_unlock_anal_serum():
        found = find_in_list(lambda x: x.name == "Anal Proclivity Nanobots", list_of_traits)
        if found:
            found.tier = 1
            mc.business.event_triggers_dict["fetish_serum_count"] += 1
        return

    def fetish_unlock_exhibition_serum():
        found = find_in_list(lambda x: x.name == "Social Sexual Proclivity Nanobots", list_of_traits)
        if found:
            found.tier = 1
            mc.business.event_triggers_dict["fetish_serum_count"] += 1
        return

    def fetish_unlock_cum_serum():
        found = find_in_list(lambda x: x.name == "Semen Proclivity Nanobots", list_of_traits)
        if found:
            found.tier = 1
            mc.business.event_triggers_dict["fetish_serum_count"] += 1
        return

    def fetish_unlock_breeding_serum():
        found = find_in_list(lambda x: x.name == "Reproduction Proclivity Nanobots", list_of_traits)
        if found:
            found.tier = 1
            mc.business.event_triggers_dict["fetish_serum_count"] += 1
        return


    def add_fetish_serum_traits():
        FETISH_PRODUCTION_COST = 20    #Default 100

        fetish_basic_ther = SerumTraitMod(name = "Sexual Proclivity Nanobots",
                desc = "Targetted endorphin emitters increase general positive sexual responses based on suggestability.",
                positive_slug = "Increases sexual opinions, Slowly increases Foreplay skill",
                negative_slug = "+10 Serum Research, +20 Production Cost",
                value_added = 0,
                research_added = 10,
                slots_added = 1,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 0,
                on_apply = fetish_basic_function_on_apply,
                on_turn = fetish_basic_function_on_turn,
                tier = 99,
                start_researched =  True,
                research_needed = 400,
                exclude_tags = ["Nanobots"]
            )

        fetish_exhibition_ther = SerumTraitMod(name = "Social Sexual Proclivity Nanobots",
                desc = "Targetted endorphin emitters increase general positive opinions of public sexual encounters based on suggestability.",
                positive_slug = "Increases exhibitionistic behavior, Slow increases sluttiness",
                negative_slug = "+10 Serum Research, +20 Production Cost",
                value_added = 0,
                research_added = 10,
                slots_added = 1,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 0,
                on_apply = fetish_exhibition_function_on_apply,
                on_turn = fetish_exhibition_on_turn,
                tier = 99,
                start_researched =  True,
                research_needed = 800,
                exclude_tags = ["Nanobots"]
            )

        fetish_anal_ther = SerumTraitMod(name = "Anal Proclivity Nanobots",
                desc = "Targetted endorphin emitters increase general positive opinions of public sexual encounters based on suggestability.",
                positive_slug = "Increases Anal sexual opinions, Slowly increases Anal skill, Slowly increases obedience",
                negative_slug = "+10 Serum Research, +20 Production Cost",
                value_added = 0,
                research_added = 10,
                slots_added = 1,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 0,
                on_apply = fetish_anal_function_on_apply,
                on_turn = fetish_anal_function_on_turn,
                tier = 99,
                start_researched =  True,
                research_needed = 800,
                exclude_tags = ["Nanobots"]
            )

        fetish_cum_ther = SerumTraitMod(name = "Semen Proclivity Nanobots",
                desc = "Targetted endorphin emitters increase pleasure received when in contact with semen based on suggestability.",
                positive_slug = "Increases Cum related sexual opinions, slowly increases sluttiness, slowly increases Oral skill",
                negative_slug = "+10 Serum Research, +20 Production Cost",
                value_added = 0,
                research_added = 10,
                slots_added = 1,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 0,
                on_apply = fetish_cum_function_on_apply,
                on_turn = fetish_cum_function_on_turn,
                tier = 99,
                start_researched =  True,
                research_needed = 800,
                exclude_tags = ["Nanobots"]
            )

        fetish_breeding_ther = SerumTraitMod(name = "Reproduction Proclivity Nanobots",
                desc = "Targetted endorphin emitters increase reproduction drive and associated opinions based on suggestability.",
                positive_slug = "Increases reproduction sexual opinions, Slowly increases Vaginal skill, +$20 Value",
                negative_slug = "+10 Serum Research, +20 Production Cost",
                value_added = 0,
                research_added = 10,
                slots_added = 1,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 0,
                on_apply = fetish_breeding_function_on_apply,
                on_turn = fetish_breeding_function_on_turn,
                tier = 99,
                start_researched =  True,
                research_needed = 800,
                exclude_tags = ["Nanobots"]
            )
        return

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_fetish_serum_trait(stack):
python:
    add_fetish_serum_traits()
    execute_hijack_call(stack)
return
