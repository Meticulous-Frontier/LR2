#GLOBAL TODO before releasing this mechanic into the wild
#Need atleast three positions that qualify for each sex goal for variety.
#Add new personality dialogue.
#Add dialogue based on sex goals
#Control where MC finishes based on sex goals to have a better chance of meeting the goal.



init -2:
    python:
        list_of_selfish_dom_sex_goals = []
        list_of_selfish_dom_sex_goals.append("get off")
        list_of_selfish_dom_sex_goals.append("waste cum")
        #list_of_selfish_dom_sex_goals.append("hate fuck")  #We can't yet reliably path to this. Not enough pathing options

        list_of_unselfish_dom_sex_goals = []
        list_of_unselfish_dom_sex_goals.append("vaginal creampie")
        list_of_unselfish_dom_sex_goals.append("anal creampie")
        list_of_unselfish_dom_sex_goals.append("facial")
        list_of_unselfish_dom_sex_goals.append("body shot")
        list_of_unselfish_dom_sex_goals.append("get mc off") #Generally this will be foreplay tags
        list_of_unselfish_dom_sex_goals.append("oral creampie")

        list_of_all_dom_sex_goals = list_of_selfish_dom_sex_goals + list_of_unselfish_dom_sex_goals

        class dom_sex_path_node(renpy.store.object):
            def __init__(self, position, completion_requirement = True):
                self.position = position
                self.completion_requirement =  completion_requirement

init 3 python: #Add appropriate opinion tags to all vanilla positions
    blowjob.opinion_tags.append("get mc off")
    blowjob.opinion_tags.append("oral creampie")
    blowjob.opinion_tags.append("facial")
    blowjob.opinion_tags.append("body shot")
    cowgirl.opinion_tags.append("vaginal creampie")
    cowgirl.opinion_tags.append("get off")
    cowgirl.opinion_tags.append("hate fuck")
    cowgirl.opinion_tags.append("body shot")
    deepthroat.opinion_tags.append("oral creampie")
    handjob.opinion_tags.append("get mc off")
    handjob.opinion_tags.append("waste cum")
    handjob.opinion_tags.append("body shot")  #Change this later if we come up with a better position
    skull_fuck.opinion_tags.append("oral creampie")
    tit_fuck.opinion_tags.append("body shot")


init -1:
    python:
        #List of completion requirements for different possible dom sex positions.
        def dom_requirement_creampie(the_person, the_report):
            if report_log["guy orgasms"] >= 1and the_person.has_creampie_cum():
                return True
            return False

        def dom_requirement_anal_creampie(the_person, the_report):
            if report_log["guy orgasms"] >= 1 and the_person.has_creampie_cum():
                return True
            return False

        def dom_requirement_oral_creampie(the_person, the_report):
            if report_log["guy orgasms"] >= 1 and the_person.has_mouth_cum():
                return True
            return False

        def dom_requirement_facial(the_person, the_report):
            if report_log["guy orgasms"] >= 1 and the_person.has_face_cum():
                return True
            return False

        def dom_requirement_body_shot(the_person, the_report):
            if report_log["guy orgasms"] >= 1:
                if the_person.has_ass_cum() or the_person.has_tits_cum() or the_person.has_stomach_cum() or the_person.has_face_cum():
                    return True
            return False

        def dom_requirement_get_mc_off(the_person, the_report):
            if report_log["guy orgasms"] >= 1:
                return True
            return False

        def dom_requirement_get_off(the_person, the_report):
            if report_log["girl orgasms"] >= 1:
                return True
            return False

        def dom_requirement_hate_fuck(the_person, the_report):
            if report_log["girl orgasms"] >= 2:
                return True
            return False

        def dom_requirement_waste_cum(the_person, the_report):
            if report_log["guy orgasms"] >= 1:
                return True
            return False

        def dom_requirement_mc_aroused(the_person, the_report):
            if mc.arousal > 40:
                return True
            return False

        def dom_requirement_girl_aroused(the_person, the_report):
            if the_person.arousal > 40:
                return True
            return False

        def dom_requirement_mc_highly_aroused(the_person, the_report):
            if mc.arousal > 70:
                return True
            return False

        def dom_requirement_girl_highly_aroused(the_person, the_report):
            if the_person.arousal > 40:
                return True
            return False

        def dom_requirement_girl_vagina_avail(the_person, the_report):
            return the_person.vagina_available()

        def dom_requirement_tits_avail(the_person, the_report):
            return the_person.tits_available()

        def construct_mc_turn_on_weighted_list(the_person, prohibit_tags = []):
            position_option_list = []
            position_option_list.append(kissing, 30 + the_person.get_opinion_score("kissing"))
            position_option_list.append(handjob, 30 + the_person.get_opinion_score("giving handjobs"))
            # position_option_list.append(drysex_cowgirl, 30 + the_person.get_opinion_score("taking control")) #TODO Drysex isn't finished yet
            return get_random_from_weighted_list(position_option_list)



init 2:
    python:
        #Use this function to make a "random" sex goal. Weights outcome based on the person and how far things have already gone.
        #weight is scale 0-100
        def create_sex_goal(the_person, report_log = None):
            if report_log != None: #First, check if we are here
                if report_log.get("guy orgasms", 0) > 0 and report_log.get("girl orgasms", 0) == 0:   #We are here because Mc finished too fast.
                    pass #TODO do this here or in the original call?

            dom_sex_goal_weighted_list = []
            # If love is less than 0, we consider selfish sex goals
            if the_person.love < 0:
                for goal in list_of_selfish_dom_sex_goals:
                    dom_sex_goal_weighted_list.append ([goal,-the_person.love])
            else: #Always have atleast one option in the list
                dom_sex_goal_weighted_list.append(["get mc off", 30])

            #Next, we add individual goals based on her sluttiness. #TODO consider a list of constants declared at the top that can be changed for setting sluttiness threshholds for these.
            #TODO adjust weights based on fetishes
            #body shot
            if the_person.sluttiness > 30:
                body_shot_weight = 40 + (the_person.get_opinion_score("being covered in cum") * 10)
                dom_sex_goal_weighted_list.append(["body shot", body_shot_weight])

            #Facial
            if the_person.sluttiness > 40:
                facial_weight = 40 + (the_person.get_opinion_score("being covered in cum") * 10) + (the_person.get_opinion_score("cum facials") * 10)
                dom_sex_goal_weighted_list.append(["facial", facial_weight])

            #oral creampie
            if the_person.sluttiness > 50:
                oral_creampie_weight = 40 + (the_person.get_opinion_score("drinking cum") * 20)
                dom_sex_goal_weighted_list.append(["oral creampie", oral_creampie_weight])

            #vaginal creampie
            if the_person.sluttiness > 60:
                vaginal_creampie_weight = 40 + (the_person.get_opinion_score("creampies") * 20)
                dom_sex_goal_weighted_list.append(["vaginal creampie", vaginal_creampie_weight])

            #anal creampie
            if the_person.sluttiness > 70:
                anal_creampie_weight = 40 + (the_person.get_opinion_score("anal creampies") * 20)
                dom_sex_goal_weighted_list.append(["anal creampie", anal_creampie_weight])

            return get_random_from_weighted_list(dom_sex_goal_weighted_list)

        def create_sex_path(the_person, the_goal, prohibit_tags = []):
            position_option_list = []
            second_position_option_list = []
            extra_positions = []
            ### Create list of possible positions###
            # when she enjoys blow jobs, add one to her choices (to prevent always going to blowjob variant)
            if the_person.sex_skills["Oral"] >= 5 and the_person.get_opinion_score("giving blowjobs") > 1 and the_person.get_opinion_score("being submissive") > 1:
                extra_positions.append(skull_fuck)
            elif the_person.sex_skills["Oral"] > 3 and the_person.get_opinion_score("giving blowjobs") > 1:
                extra_positions.append(deepthroat)
            elif the_person.sex_skills["Oral"] > 2 and the_person.get_opinion_score("giving blowjobs") > 0:
                extra_positions.append(blowjob)
            elif the_goal == "oral creampie" or the_goal == "facial":
                extra_positions.append(blowjob)

            # when she enjoys tit fucks, add it to her position choices
            if the_person.sex_skills["Foreplay"] > 2 and the_person.get_opinion_score("giving tit fucks") > 1 and the_person.has_large_tits():
                extra_positions.append(tit_fuck)


            #TODO we also need to check and make sure an object exists for each possible sex position. Figure out how to do this
            for position in list_of_girl_positions + extra_positions:
                if the_goal in position.opinion_tags:
                    if the_person.sluttiness >= position.slut_requirement:
                        if not position.skill_tag in prohibit_tags:
                            position_option_list.append([position, min(20, 100 - abs(the_person.sluttiness - position.slut_requirement))])  #every qualifying position has atleast weight 20, with higher weights if actual sluttiness is close to requirement

            if len(position_option_list) == 0: #Somehow no positions available for this requirement.
                return None

            #Construct final node by choosing appropriately tagged final position
            final_node = dom_sex_path_node(get_random_from_weighted_list(position_option_list))
            if the_goal == "get off":
                final_node.completion_requirement = dom_requirement_get_off
            if the_goal =="waste cum":
                final_node.completion_requirement = dom_requirement_waste_cum
            if the_goal =="hate fuck":
                final_node.completion_requirement = dom_requirement_hate_fuck
            if the_goal =="vaginal creampie":
                final_node.completion_requirement = dom_requirement_creampie
            if the_goal =="anal creampie":
                final_node.completion_requirement = dom_requirement_anal_creampie
            if the_goal =="facial":
                final_node.completion_requirement = dom_requirement_facial
            if the_goal =="body shot":
                final_node.completion_requirement = dom_requirement_body_shot
            if the_goal =="get mc off":
                final_node.completion_requirement = dom_requirement_get_mc_off
            if the_goal =="oral creampie":
                final_node.completion_requirement = dom_requirement_oral_creampie

            ###Construct path to final node
            #First, we explore cases where we MUST have an earlier node
            req_func = None
            first_position = None

            #She isn't naked enough to go straight to final node
            if not final_node.position.check_clothing(the_person):  #She isn't naked enough to go straight to the end node
                for position in list_of_girl_positions + extra_positions:
                    if allow_position(the_person, position) and mc.location.has_object_with_trait(position.requires_location) and (the_person.has_large_tits() or not position.requires_large_tits):
                        if position.check_clothing(the_person):
                            if final_node.position.skill_tag == "Vaginal" or final_node.position.skill_tag == "Anal":
                                if position.skill_tag == "Foreplay" or position.skill_tag == "Oral":
                                    if not position.skill_tag in prohibit_tags:
                                        second_position_option_list.append([position, min(20, 100 - abs(the_person.sluttiness - position.slut_requirement))])
                            else:
                                if position.skill_tag == "Foreplay":
                                    if not position.skill_tag in prohibit_tags:
                                        second_position_option_list.append([position, min(20, 100 - abs(the_person.sluttiness - position.slut_requirement))])
                if len(second_position_option_list) == 0: #No workable options.
                    return None
                first_position = get_random_from_weighted_list(second_position_option_list)
                if final_node.position.requires_clothing == "Vagina":
                    req_func = dom_requirement_girl_vagina_avail
                else:
                    req_func = dom_requirement_tits_avail

            #MC isn't hard enough for final node
            elif mc.recently_orgasmed and final_node.position.requires_hard:
                first_position = construct_mc_turn_on_weighted_list(the_person, prohibit_tags)
                req_func = dom_requirement_mc_aroused

            #If we don't have a first node, 50/50 chance we create a first node, or sex begins with final node
            elif renpy.random.randint(0,100) < 50:
                for position in list_of_girl_positions + extra_positions:
                    if allow_position(the_person, position) and mc.location.has_object_with_trait(position.requires_location) and (the_person.has_large_tits() or not position.requires_large_tits):
                        if position.check_clothing(the_person):
                            if final_node.position.skill_tag == "Vaginal" or final_node.position.skill_tag == "Anal":
                                if position.skill_tag == "Foreplay" or position.skill_tag == "Oral":
                                    if not position.skill_tag in prohibit_tags:
                                        second_position_option_list.append([position, min(20, 100 - abs(the_person.sluttiness - position.slut_requirement))])
                            else:
                                if position.skill_tag == "Foreplay":
                                    if not position.skill_tag in prohibit_tags:
                                        second_position_option_list.append([position, min(20, 100 - abs(the_person.sluttiness - position.slut_requirement))])
                first_position  = get_random_from_weighted_list(second_position_option_list)

                if first_position.girl_arousal > first_position.guy_arousal: #Choose our exit function based on who the position arouses more
                    req_func = dom_requirement_girl_aroused
                else:
                    req_func = dom_requirement_mc_aroused

            ###Now we construct our path.
            sex_path = []
            if first_position == None:  #We are going straight to our final position
                sex_path.append(final_node)
                return sex_path
            else:
                first_node = dom_sex_path_node(first_position, completion_requirement = req_func)
                sex_path.append(first_node)
                sex_path.append(final_node)
                return sex_path






label get_fucked(the_person, the_goal = None, sex_path = None, private= True, start_position = None, start_object = None, skip_intro = False, report_log = None, ignore_taboo = False, prohibit_tags = [], unit_test = False):
    $ apply_sex_modifiers(the_person) #Apply sex modifiers before choosing goals and positions to avoid choosing positions girl shouldn't accept
    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ object_choice = start_object
    $ start_mc_orgasm = 0
    $ start_girl_orgasm = 0
    if report_log != None:  #We set orgasms in the report to zero for now so that requirement functions can check for them easier.
        $ start_mc_orgasm = report_log.get("guy orgasms", 0)
        $ start_girl_orgasm = report_log.get("girl orgasms", 0)
        $ report_log["guy orgasms"] = 0
        $ report_log["girl orgasms"] = 0
    else:
        $ report_log = defaultdict(int) #Holds information about the encounter: what positions were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
        $ report_log["positions_used"] = []


    if start_position != None and sex_path == None:
        $ sex_path = [dom_sex_path_node(start_position, dom_requirement_get_mc_off)]  #If we have a start position only, we set the path to be the start position with MC getting off as the goal
        $ the_goal = "get mc off"

    if the_goal == None:
        $ the_goal = create_sex_goal(the_person, report_log)
        if unit_test: #unit_test is for debug dialogue
            "The goal for this session is [the_goal]."

    if sex_path == None:
        $ sex_path = create_sex_path(the_person, the_goal, prohibit_tags)
        if unit_test:
            "The first position for this session is [sex_path[0].position.name]."

    if sex_path == None:  #We couldn't find a sex path, so abort the session, or possibly rerun it relaxing conditions? #TODO

        "[the_person.title] can't think of anything more to do with you."
        $ finished = True
        if unit_test: #unit_test is for debug dialogue
            "No viable path."

    if len(sex_path) > 1:
        the_person.char "Let's get warmed up a little bit first..."

    elif object_choice == None:
        $ object_choice = girl_choose_object_enhanced(the_person, sex_path[0].position)
        $ current_node = sex_path.pop(0)  #Pop the first node in the list of sex path nodes.
    #Next we mimic fuck_person() but only with applicable girl in charge parameters.
    #Privacy modifiers
    if mc.location.get_person_count() == 1 and not private:
        $ private = True #If we're alone in the space we're always Private, even if we had left the possibility for people being around.
    #Next, check for generic conditions that keep us from continuing

    if not finished:
        if current_node.position is None: #There's no position we can take
            "[the_person.title] can't think of anything more to do with you."
            $ finished = True
        elif object_choice is None:
            "[the_person.title] looks around, but can't see anywhere to have fun with you."
            $ finished = True
        elif the_person.energy < 15 :
            the_person.char "I'm tired. Maybe we will continue this another time."
            $ finished = True

    #TODO determine condom usage. Can probably just call a method from the sex bugfix file

    #We should be able to initiate sex. If we need to, call initial intros and taboo breaks.
    if not skip_intro and not finished:
        $ the_person.draw_person()
        if not ignore_taboo and the_person.has_taboo(current_node.position.associated_taboo):
            # call mod taboo break
            $ current_node.position.call_transition_taboo_break(None, the_person, mc.location, object_choice)
            $ the_person.break_taboo(current_node.position.associated_taboo)
        else:
            $ current_node.position.call_intro(the_person, mc.location, object_choice)

    #Now begin the sex loop
    while not finished:

        if current_node.position.requires_hard and mc.recently_orgasmed:
            "Your post orgasm cock softens, stopping [the_person.possessive_title] for now."
            #TODO if this keeps us from accomplishing sex goal, consider rerunning this method from the beginning, or just ending the scene. Or creating a new path?
            $ finished = True
        else:
            call sex_description(the_person, current_node.position, object_choice, private = private, report_log = report_log) from _call_sex_description_girl_in_charge_override_1

        if mc.condom and mc.recently_orgasmed: # you orgasmed so you used your condom.
            $ mc.condom = False

        #TODO figure out what to do in the following three cases


        if current_node.position.guy_energy > mc.energy:
            "You're too exhausted to let [the_person.possessive_title] keep [current_node.position.verbing] you."
            $ finished = True

        elif current_node.position.girl_energy > the_person.energy:
            the_person.char "I'm exhausted [the_person.mc_title], I can't keep this up..."
            $ finished = True

        #Determine if the current node has completed its finished requirement.
        if current_node.completion_requirement(the_person, report_log):
            if len(sex_path) > 0:
                $ current_node = sex_path.pop(0)
                $ object_choice = girl_choose_object_enhanced(the_person, current_node.position)
                the_person.char "Mmm, I think we're ready. Let's move on now!"
                $ current_node.position.redraw_scene(the_person)
                if not ignore_taboo and the_person.has_taboo(current_node.position.associated_taboo):
                    # call mod taboo break
                    $ current_node.position.call_transition_taboo_break(current_node.position, the_person, mc.location, object_choice)
                    $ the_person.break_taboo(current_node.position.associated_taboo)
                else:
                    $ current_node.position.call_transition(current_node.position, the_person, mc.location, object_choice)

            else:
                $ finished = True    #Sex goal has been accomplished
                the_person.char "Mmm, that was exactly what I was hoping for!"
        elif len(sex_path) > 0:
            if not sex_path[0].position.check_clothing(the_person): #We don't meet the clothing requirements for the next position, so we strip some
                $ the_clothing = the_person.choose_strip_clothing_item()
                $ current_node.position.call_strip(the_person, the_clothing, mc.location, the_object)
            else:
                call girl_strip_event(the_person, current_node.position, object_choice) from _call_girl_strip_event_girl_in_charge_01


    #TODO create positive feedback here for accomplishing sex goal

    python:
        clear_sex_modifiers(the_person)

        report_log["end arousal"] = the_person.arousal
        report_log["girl orgasms"] = report_log.get("girl orgasms",0) + start_girl_orgasm
        if report_log.get("girl orgasms",0) > 0 or report_log.get("girl one orgasms", 0) > 0:
            the_person.arousal = 0 # If she came she's satisfied.
        else:
            the_person.change_arousal(-the_person.arousal/2) #Otherwise they are half as aroused as you leave them.

        report_log["guy orgasms"] = report_log.get("guy orgasms",0) + start_mc_orgasm
        mc.condom = False
        mc.recently_orgasmed = False
        #TODO determine if we want to offer an affair from this
    # if affair_ask_after and private and ask_girlfriend_requirement(the_person) is True and not the_person.relationship == "Single":
    #     if the_person.love >= 60 and the_person.sluttiness >= 30 - (the_person.get_opinion_score("cheating on men") * 5) and report_log.get("girl orgasms",0) >= 1: #If she loves you enoguh, is moderately slutty, and you made her cum
    #         call affair_check(the_person, report_log) from _call_affair_check_bugfix

    python:
        update_person_sex_record(the_person, report_log)
        the_goal = None
        sex_path = None

    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log


init 1000 python:
    def GIC_unit_test(count = 1):#Count is the number of times we repeat the unit test.
        unit_test_count = 0
        while unit_test_count < count:
            mc.change_location(bedroom)
            the_person = get_random_from_list(known_people_in_the_game([mc]))
            the_person.love = renpy.random.randint(-50,50)
            the_person.sluttiness = renpy.random.randint(60,120)
            mc.energy = mc.max_energy
            the_person.energy = the_person.max_energy
            renpy.call("get_fucked", the_person, unit_test = True)
            unit_test_count += 1
