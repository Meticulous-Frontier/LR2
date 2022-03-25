init 5 python:
    config.label_overrides["daughter_work_crisis_label"] = "daughter_work_crisis_label_enhanced"

    def get_random_mother_from_company_with_children():
        valid_people_list = []
        for person in [x for x in mc.business.get_employee_list() if x.age >= 34 and not quest_director.is_person_blocked(x) and x not in unique_character_list]:
            available_kids = person.kids - person.number_of_children_with_mc()
            if available_kids > 0 and available_kids > town_relationships.get_existing_child_count(person): #They have undiscovered kids we can add in.
                valid_people_list.append(person)

        return get_random_from_list(valid_people_list) #Pick someone appropriate from the company.


label daughter_work_crisis_label_enhanced():
    if mc.business.get_employee_count() >= mc.business.max_employee_count:
        return #The business is full due to some other crisis triggering this time chunk.

    $ the_person = get_random_mother_from_company_with_children()
    if the_person is None:
        return #We couldn't find anyone to be a parent, so the event fails.

    $ the_person.draw_person()
    the_person "[the_person.mc_title], could I talk to you for a moment in your office?"
    mc.name "Of course. What's up?"
    $ ceo_office.show_background()
    "You and [the_person.possessive_title] step into your office. You sit down at your desk while she closes the door."
    $ ran_num = renpy.random.randint(0,2)
    if ran_num == 0: #TODO: Make this based on her stats?
        the_person "I wanted to ask you... My daughter is living at home and I think it's time she got a job."
        the_person "I promise she would be a very hard worker, and I'd keep a close eye on her."

    elif ran_num == 1:
        the_person "This is embarrassing to ask, but... my daughter was let go from her job last week."
        the_person "It would mean the world to me if you would look at this and at least consider it."

    else: # ran_num == 2
        the_person "I wanted to ask you... Well, my daughter just finished school and has been looking for a job." #TOOD: Add other excuses, like 'needs to pay rent somehow' or 'can't keep out of trouble.'
        the_person "I was thinking that she might be a good fit for the company. I can tell you she's very smart."
    $ promised_sex = False
    if the_person.effective_sluttiness() > 70:
        "[the_person.title] hands over a printed out resume and leans forward onto your desk, bringing her breasts closer to you."
        the_person "If you did hire her, I would be so very thankful. I'm sure we could find some way for me to show you how thankful."
        $ promised_sex = True

    else:
        "[the_person.title] hands over a printed out resume and waits nervously for you to look it over."

    menu:
        "Look at the resume for [the_person.name]'s daughter":
            pass

        "Tell her you aren't hiring":
            "You hand the resume back."
            mc.name "I'm sorry, but I'm not looking to hire anyone right now."
            if the_person.effective_sluttiness() > 50 and not promised_sex:
                the_person "Wait, please [the_person.mc_title], at least take a look. Maybe I could... convince you to consider her?"
                the_person "She means the world to me, and I would do anything to give her a better chance. Anything at all."
                "She puts her arms behind her back and puffs out her chest in a clear attempt to show off her tits."
                $ mc.change_locked_clarity(5)
                menu:
                    "Look at the resume for [the_person.name]'s daughter":
                        "Convinced, you start to read through the resume."
                        $ promised_sex = True

                    "Tell her you aren't hiring":
                        if the_person.love < 10:
                            mc.name "If I want to fuck you I wouldn't need to hire your daughter to do it. Give it up, you look desperate."
                            $ the_person.change_obedience(3)
                            "She steps back and looks away."
                            the_person "Uh, right. Sorry for taking up your time."
                            "[the_person.possessive_title] hurries out of your office."
                        else:
                            mc.name "I'm not hiring right now, and that's final. Now I'm sure you have work to do."
                            $ the_person.change_obedience(1)
                            "She takes the resume back and steps away from your desk, defeated."
                            the_person "Right, of course. Sorry for wasting up your time."
                        $ clear_scene()
                        return
            elif promised_sex:
                the_person "There's nothing I could do? Nothing at all?"
                "She moves to run a hand down your shirt, but you shove the resume back into her hand."
                if the_person.love < 10:
                    mc.name "If I want to fuck you I wouldn't need to hire your daughter to do it. Give it up, you look desperate."
                    $ the_person.change_obedience(3)
                    "She steps back and looks away."
                    the_person "Uh, right. Sorry for taking up your time."
                    "[the_person.possessive_title] hurries out of your office."
                else:
                    mc.name "I'm not hiring right now, and that's final. Now I'm sure you have work to do."
                    $ the_person.change_obedience(1)
                    "She takes the resume back and steps away from your desk, defeated."
                    the_person "Right, of course. Sorry for wasting up your time."
                $ clear_scene()
                return

            else:
                $ the_person.draw_person(emotion = "sad")
                $ the_person.change_happiness(-3)
                the_person "I understand. Sorry for taking up your time."
                "She collects the resume and leaves your office."
                $ clear_scene()
                return

    $ the_daughter = the_person.generate_daughter() #Produces a person who has a high chance to share characteristics with her mother.

    # block rollback before this point
    $ renpy.block_rollback()

    call hire_select_process([the_daughter, 1]) from _call_hire_select_process_daughter_work_crisis_enhanced #Hire her or reject her. Padded with an extra item in the array or we crash due to trying to pre-calculate forward/backwards buttons

    $ the_person.draw_person()
    if _return == the_daughter: #You've chosen to hire her.
        $ hire_day = "tomorrow"
        if day%7 == 4 or day%7 == 5: #If it's Friday or Saturday, don't start tomorrow
            $ hire_day = "Monday"
        if promised_sex:
            mc.name "Alright, I'll admit this looks promising, but I need some convincing."
            the_person "Of course, [the_person.mc_title]."
            "She steps around your desk and comes closer to you."
            $ the_person.add_situational_obedience("bribe", 30, "It's for my daughter and her future!")
            call fuck_person(the_person) from _call_fuck_person_daughter_work_crisis_enhanced
            $ the_person.draw_person()
            $ the_person.clear_situational_obedience("bribe")
            $ the_person.change_obedience(2)
            $ the_person.review_outfit()
            the_person "Are we all done then?"
            mc.name "For now. You can call your daughter and tell her she can start [hire_day]. I won't give her any preferential treatment from here on out though."
            the_person "Of course. Thank you."
            call hire_someone(the_daughter) from _call_hire_someone_daughter_work_crisis_enhanced_1
        else:
            mc.name "Alright [the_person.title], this looks promising, she can start [hire_day]. I can't give her any preferential treatment, but I'll give her a try."
            $ the_person.change_stats(happiness = 5, love = 2)
            the_person "Thank you so much!"
            call hire_someone(the_daughter) from _call_hire_someone_daughter_work_crisis_enhanced_2
        # make sure to set titles for the daughter (prevent introduction dialogs)
        $ the_daughter.set_mc_title(get_random_from_list(get_player_titles(the_daughter)))
        $ the_daughter.set_title(get_random_title(the_daughter))
        $ the_daughter.set_possessive_title(get_random_possessive_title(the_daughter))
    else: #is "None
        $ the_daughter.remove_person_from_game()
        if promised_sex: #You promised to do it for sex but don't want to hire her, mom is disappointed.
            mc.name "I'm sorry but her credentials just aren't what they need to be. I could never justify hiring your daughter."
            $ the_person.change_stats(happiness = -5, love = -1)
            $ the_person.draw_person(emotion = "sad")
            "[the_person.possessive_title] seems to deflate. She nods sadly."
            the_person "I understand. Thank you for your time."
        else:
            mc.name "I'm sorry but I don't think her skills are where I would need them to be."
            $ the_person.change_obedience(1)
            the_person "I understand, thank you for at least taking a look for me."

    $ the_daughter = None
    $ clear_scene()
    return
