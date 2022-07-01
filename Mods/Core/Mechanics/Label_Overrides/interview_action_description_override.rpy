init 2 python:
    config.label_overrides["interview_action_description"] = "interview_action_description_enhanced"

    def get_candidate_count_costs():
        interview_cost = mc.business.recruitment_cost
        count = 3 #Num of people to generate, by default is 3. Changed with some policies
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active():
                count += recruitment_policy.extra_data.get("recruitment_batch_adjust",0)
                interview_cost +=  recruitment_policy.extra_data.get("interview_cost_adjust",0)

        return count, interview_cost

    def interview_build_candidates_list(count):
        start_time = time.time()
        candidates = []
        for x in __builtin__.range(0, count): #NOTE: count is given +1 because the screen tries to pre-calculate the result of button presses. This leads to index out-of-bounds, unless we pad it with an extra character (who will not be reached).
            candidates.append(make_person(**(mc.business.generate_candidate_requirements())))

        reveal_count = 0
        reveal_sex = False

        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active():
                reveal_count += recruitment_policy.extra_data.get("reveal_count_adjust",0)
                reveal_sex = reveal_sex or recruitment_policy.extra_data.get("reveal_sex_opinion",False)

        for a_candidate in candidates:
            for x in __builtin__.range(0,reveal_count): #Reveal all of their opinions based on our policies.
                a_candidate.discover_opinion(a_candidate.get_random_opinion(include_known = False, include_sexy = reveal_sex),add_to_log = False) #Get a random opinion and reveal it.

            # new candidate could be pregnant
            if persistent.pregnancy_pref > 0:
                if a_candidate.age > 21 and renpy.random.randint(0,100) < (58 - a_candidate.age) // 5: # chance she is already pregnant decreases with age
                    #Can hire her up to 10 days from due date. Probably not hiring anyone a week from due!
                    become_pregnant(a_candidate, mc_father = False, progress_days = renpy.random.randint(5,80))
                    #renpy.say("Pregnant", "Candidate: " + a_candidate.name + " " + a_candidate.last_name + " is pregnant.")

        if debug_log_enabled:
            add_to_debug_log("Candidates (" + str(count) + "): {total_time:.3f}", start_time)
        return candidates


label interview_action_description_enhanced():
    $ count, interview_cost = get_candidate_count_costs()

    "Bringing in [count] people for an interview will cost $[interview_cost]. Do you want to spend time interviewing potential employees?"
    menu:
        "Yes, I'll pay the cost\n{color=#ff0000}{size=18}Costs: $[interview_cost]{/size}{/color}":
            $ mc.business.change_funds(-interview_cost)
            $ clear_scene()

            $ candidates = interview_build_candidates_list(count)

            # pad with one extra element, to make sure we can see all candidates
            call hire_select_process(candidates + [1]) from _call_hire_select_process_interview_action_enhanced

            if not _return == "None":
                $ new_person = _return
                $ new_person.generate_home() #Generate them a home location so they have somewhere to go at night.
                $ candidates.remove(new_person)

                call hire_someone(new_person, add_to_location = True) from _call_hire_someone_interview_action_enhanced
                $ new_person.set_title(new_person.get_random_title())
                $ new_person.set_possessive_title(new_person.get_random_possessive_title())
                $ new_person.set_mc_title(new_person.get_random_player_title())
                $ del new_person
            else:
                "You decide against hiring anyone new for now."

            # cleanup not used candidates
            python:
                if persistent.keep_patreon_characters:
                    for person in candidates:
                        if person.is_patreon: # preserve Patreon unique characters.
                            person.generate_home()
                            person.home.add_person(person)
                        else:
                            person.remove_person_from_game()

                candidates.clear() #Prevent it from using up extra memory
                person = None
                clean_memory() # extra memory cleanup after interview screen

            call advance_time from _call_advance_time_interview_action_enhanced
        "Never mind":
            pass
    return
