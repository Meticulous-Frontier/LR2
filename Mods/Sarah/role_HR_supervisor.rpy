# ****HR Director role****
# Early game: She adds her charisma and HR skill to max efficiency. Lets events scale this factor up
# Mid game: She can help shape employee work interests. She will automatically work with employees in different departments increasing their relevant likes and dislikes.
#   Once per week, you can target an individual girl and a specific work interest.
# As she gets corrupted, the opinions she can train evolve. EG: showing tits, skimpy uniforms
# Late game: Unlocks threesome scenes with employees.
#
# Required Labels
# Initial Hiring
# First Monday review
# Subsequent Monday meetings
# HR Stage One event: Beginning once a week, can have personal interview with one employee.
# HR stage two event: Can create new training videos to be looped in break rooms, emphasizing "company values"
# HR stage three event: Company sponsored sexual training.
#


#HR director functions
init -0 python:
    def get_HR_director():
        return business_HR_director

    def set_HR_director_tag(key, value):
        if business_HR_director:
            business_HR_director.HR_tags[key] = value

    def get_HR_director_tag(key, default = None):
        if business_HR_director:
            return business_HR_director.HR_tags.get(key, default)

    # used for unlocked sex positions
    def set_HR_director_unlock(key, value):
        if business_HR_director:
            business_HR_director.HR_unlocks[key] = value

    # used for unlocked sex positions
    def get_HR_director_unlock(key, default = False):
        if business_HR_director:
            return business_HR_director.HR_unlocks.get(key, default)

#HR director action requirements#
init -2 python:
    #TODO move all these true false flags to a dict so that in the future when I add more, I can call them by reference and not invalidate old saves games!

    business_HR_director = None

init 5 python:
    def build_HR_review_list(the_person, max_tier = 0):
        HR_tier_talk = -1 # init at -1 so we do the first collect with 0
        HR_employee_list = []
        # build list of girls that qualify for specified tier and max_tier score
        while len(HR_employee_list) == 0 and HR_tier_talk < get_HR_director_tag("business_HR_coffee_tier", 0) and HR_tier_talk < max_tier:
            HR_tier_talk += 1
            HR_employee_list = get_HR_review_list(the_person, HR_tier_talk)
        return (HR_employee_list, HR_tier_talk)

    def get_HR_review_list(the_person, tier = 0):   #Pass in the HR director so we don't try to counsel her
        people_list = []
        for person in [x for x in mc.business.get_employee_list() if not x is the_person]:
            topic_list = create_HR_review_topic_list(person)
            for topic in topic_list:
                if person.get_opinion_score(topic) < tier:
                    people_list.append(person)
                    break
        return people_list

    def build_HR_mc_list(the_person):
        HR_employee_list = []
        HR_employee_list = get_HR_review_list(the_person, tier = 2)
        return HR_employee_list

    def create_HR_review_topic_list(the_person):
        topic_list = ["working"]
        if the_person in mc.business.production_team:
            topic_list.append("production work")
        if the_person in mc.business.hr_team:
            topic_list.append("HR work")
        if the_person in mc.business.research_team:
            topic_list.append("research work")
        if the_person in mc.business.market_team:
            topic_list.append("marketing work")
        if the_person in mc.business.supply_team:
            topic_list.append("supply work")
        if get_HR_director_tag("business_HR_uniform", False) == True:
            topic_list.append("work uniforms")
        if get_HR_director_tag("business_HR_skimpy_uniform", False) == True:
            topic_list.append("skimpy uniforms")

        return topic_list

    def update_hire_daughter_crisis(chance):
        found = find_in_list(lambda x: x[0] == daughter_work_crisis, crisis_list)
        if found:
            found[1] = chance
            #renpy.say("", "Updated daughter at work crisis chance to: " + str(chance) + "%%")
        return

    def HR_director_initial_hire_requirement():
        if get_HR_director_tag("business_HR_meeting_last_day", 0) < day:
            if mc.business.is_open_for_business():
                if time_of_day == 1:
                    return True
        return False

    def HR_director_first_monday_requirement():
        if time_of_day == 1:
            if day%7 == 0:  #Monday
                return True
        return False

    def HR_director_monday_meeting_requirement():
        if get_HR_director() is None:
            return False
        elif time_of_day == 1:
            if day%7 == 0:  #Monday
                return True
        return False

    def HR_director_fire_requirement():
        return True

    def HR_director_coffee_tier_1_requirement(the_person):
        if get_HR_director_tag("business_HR_coffee_tier", 0) == 0:
            if get_HR_director_tag("business_HR_serum_tier", 0) > 0:
                if mc.business.funds > 500:
                    return True
                else:
                    return "Requires $500"

        return False

    def HR_director_coffee_tier_2_requirement(the_person):
        if get_HR_director_tag("business_HR_coffee_tier", 0) == 1:
            if get_HR_director_tag("business_HR_serum_tier", 0) > 1:
                if mc.business.funds > 1500:
                    return True
                else:
                    return "Requires $1500"

        return False

    def HR_director_gym_membership_tier_1_requirement(the_person):
        if mc.business.get_employee_count() > 6 and get_HR_director_tag("business_HR_gym_tier", 0)  == 0:
            return True
        return False

    def HR_director_gym_membership_tier_2_requirement(the_person):
        if mc.business.get_employee_count() > 14 and get_HR_director_tag("business_HR_gym_tier", 0)  == 1:
            return True
        return False

    def HR_director_mind_control_requirement(the_person):
        if get_HR_director_tag("business_HR_serum_tier", 0) == 3:
            if mc.business.funds > 5000:
                return True
            else:
                return "Requires $5000"
        return False

    def HR_director_mind_control_attempt_requirement(the_person):
        if get_HR_director_tag("business_HR_serum_tier", 0) == 4:
            if get_HR_director_tag("business_HR_meeting_last_day", 0) < day:
                if mc.business.is_open_for_business():
                    return True
                else:
                    return "Only during work day"
            else:
                return "One meeting per day."

    def HR_director_change_relative_recruitment_requirement(the_person):
        if get_HR_director_tag("business_HR_relative_recruitment", 0) > 0:
            if mc.business.is_open_for_business():
                return True
            else:
                return "Only on during work day"
        return False

    def HR_director_meeting_on_demand_requirement(the_person):
        if get_HR_director_tag("business_HR_meeting_on_demand", False) == True:
            if get_HR_director_tag("business_HR_meeting_last_day", 0) < day:
                if mc.business.is_open_for_business():
                    return True
                else:
                    return "Only on during work day"
            else:
                return "One meeting per day."
        return False

    def HR_director_headhunt_initiate_requirement(the_person):
        if get_HR_director_tag("business_HR_headhunter_initial", False) == True:
            if get_HR_director_tag("business_HR_headhunter_progress", 0) == 0:
                if mc.business.max_employee_count == mc.business.get_employee_count():
                    return "You have too many employees"
                if mc.business.is_open_for_business():
                    return True
                else:
                    return "Only during work day"
        return False

    def HR_director_headhunt_interview_requirement():
        if day >= get_HR_director_tag("recruit_day"):
            if mc.business.is_open_for_business():
                if time_of_day == 1:
                    return True
        return False

    def is_HR_director_employed(hr_director):
        if hr_director in mc.business.get_employee_list():
            return True
        cleanup_HR_director_meetings()
        return False

    def can_appoint_HR_director_requirement():
        if business_HR_director is None:
            if HR_director_creation_policy.is_owned():
                if len(mc.business.hr_team) > 0:
                    return True
        return False

    def remove_mandatory_crisis_list_action(crisis_name):
        found = find_in_list(lambda x: x.effect == crisis_name, mc.business.mandatory_crises_list)
        if found:
            mc.business.mandatory_crises_list.remove(found)
        return

    def cleanup_HR_director_meetings():
        remove_mandatory_crisis_list_action("Sarah_intro_label")
        remove_mandatory_crisis_list_action("Sarah_hire_label")
        remove_mandatory_crisis_list_action("Sarah_get_drinks_label")
        remove_mandatory_crisis_list_action("Sarah_stripclub_story_label")
        remove_mandatory_crisis_list_action("Sarah_epic_tits_label")
        remove_mandatory_crisis_list_action("Sarah_new_tits_label")
        remove_mandatory_crisis_list_action("Sarah_third_wheel_label")
        remove_mandatory_crisis_list_action("Sarah_catch_stealing_label")
        remove_mandatory_crisis_list_action("Sarah_weekend_surprise_crisis_label")
        remove_mandatory_crisis_list_action("Sarah_threesome_request_label")
        remove_mandatory_crisis_list_action("Sarah_initial_threesome_label")
        remove_mandatory_crisis_list_action("HR_director_initial_hire_label")
        remove_mandatory_crisis_list_action("HR_director_first_monday_label")
        remove_mandatory_crisis_list_action("HR_director_monday_meeting_label")
        remove_mandatory_crisis_list_action("HR_director_headhunt_interview_label")
        return

    def add_sarah_catch_stealing_action():
        Sarah_catch_stealing_action = Action("Catch Sarah Stealing",Sarah_catch_stealing_requirement,"Sarah_catch_stealing_label")
        mc.business.mandatory_crises_list.append(Sarah_catch_stealing_action)

    def add_sarah_third_wheel_action():
        Sarah_third_wheel_action = Action("Sarah's third wheel event",Sarah_third_wheel_requirement,"Sarah_third_wheel_label")
        mc.business.mandatory_crises_list.append(Sarah_third_wheel_action)

    def add_hr_director_first_monday_action(person):
        HR_director_first_monday_action = Action("First Monday",HR_director_first_monday_requirement,"HR_director_first_monday_label", args = person)
        mc.business.mandatory_crises_list.append(HR_director_first_monday_action)

    def add_hr_director_monday_meeting_action(person):
        HR_director_monday_meeting_action = Action("Monday HR Lunch",HR_director_monday_meeting_requirement,"HR_director_monday_meeting_label", args = person)
        mc.business.mandatory_crises_list.append(HR_director_monday_meeting_action)

    def add_hr_director_headhunt_interview_action(person):
        HR_director_headhunt_interview_action = Action("Prospect Interview",HR_director_headhunt_interview_requirement,"HR_director_headhunt_interview_label", args = person)
        mc.business.mandatory_crises_list.append(HR_director_headhunt_interview_action)

    HR_director_coffee_tier_1_action = Action("Add serum to coffee during meetings.", HR_director_coffee_tier_1_requirement, "HR_director_coffee_tier_1_label",
        menu_tooltip = "Costs $500 but makes meetings more impactful.")
    HR_director_coffee_tier_2_action = Action("Add stronger serum to coffee during meetings.", HR_director_coffee_tier_2_requirement, "HR_director_coffee_tier_2_label",
        menu_tooltip = "Costs $1500 but makes meetings impactful.")
    HR_director_gym_membership_tier_1_action = Action("Sponsor company gym membership.", HR_director_gym_membership_tier_1_requirement, "HR_director_gym_membership_tier_1_label",
        menu_tooltip = "Costs money each week, but increases girls energy over time.")
    HR_director_gym_membership_tier_2_action = Action("Sponsor company health program.", HR_director_gym_membership_tier_2_requirement, "HR_director_gym_membership_tier_2_label",
        menu_tooltip = "Costs money each week, but increases girls energy over time.")
    HR_director_mind_control_action = Action("Produce mind control Serum.", HR_director_mind_control_requirement, "HR_director_mind_control_label",
        menu_tooltip = "Costs $5000. Allows you to attempt mind control of employee.")
    HR_director_mind_control_attempt = Action("Attempt Mind Control {image=gui/heart/Time_Advance.png}", HR_director_mind_control_attempt_requirement, "HR_director_mind_control_attempt_label",
        menu_tooltip = "WARNING: May have side effects!")
    HR_director_change_relative_recruitment_action = Action("Change recruitment signage", HR_director_change_relative_recruitment_requirement, "HR_director_change_relative_recruitment_label",
        menu_tooltip = "Changes how often employees ask for employment for their daughters")
    HR_director_meeting_on_demand_action = Action("Meet with employee {image=gui/heart/Time_Advance.png}", HR_director_meeting_on_demand_requirement, "HR_director_meeting_on_demand_label",
        menu_tooltip = "Arrange a meeting with an employee")
    HR_director_headhunt_initiate_action = Action("Initiate employee search", HR_director_headhunt_initiate_requirement, "HR_director_headhunt_initiate_label",
        menu_tooltip = "Try and find a new employee for a specific job")
    HR_director_role = Role("HR Director", [HR_director_meeting_on_demand_action, HR_director_coffee_tier_1_action, HR_director_coffee_tier_2_action, HR_director_gym_membership_tier_1_action, HR_director_gym_membership_tier_2_action, HR_director_mind_control_action, HR_director_mind_control_attempt, HR_director_change_relative_recruitment_action, HR_director_headhunt_initiate_action]) #Actions go in block

    HR_director_appointment_action = Action("Appoint HR Director.", can_appoint_HR_director_requirement, "HR_director_appointment_action_label",
            menu_tooltip = "Pick a member of your HR staff to be your HR director. The HR director will help you manage your employees wellbeing and motivation.")


init 1301 python:
    def HR_director_creation_requirement():
        if "sarah" in globals():
            return sarah.event_triggers_dict.get("first_meeting", False) == True
        return False

    HR_director_creation_policy = Policy(name = "Create HR Director Position",
        desc = "Create a new position for an HR Director. Increases maximum employee count by one.",
        cost = 500,
        requirement =  HR_director_creation_requirement,
        on_buy_function = increase_max_employee_size,
        on_buy_arguments = {"amount":1})

    organisation_policies_list.append(HR_director_creation_policy)


#####HR Director ACTION LABELS#####

label fire_HR_director(the_person):
    mc.name "[the_person.title], I need to talk to you about your role as my HR director."
    the_person.char "Yes?"
    mc.name "I've decided that the role would be better filled by someone else. I hope you understand."
    if the_person.cha > 2:
        $ the_person.change_happiness(-5)
        $ the_person.change_obedience(-1)
        $ the_person.draw_person(emotion="sad")
        the_person.char "I... I'm sorry I couldn't do a better job. Good luck filling the position, sir."
    else:
        $ the_person.draw_person(emotion="happy")
        the_person.char "Whew! I have a really hard time working with people to be honest. I hope whoever replaces me can do a better job at it!"

    $ the_person.special_role.remove(HR_director_role)
    $ business_HR_director = None
    $ cleanup_HR_director_meetings()
    return

label HR_director_initial_hire_label(the_person):
    #TODO if away from work, move MC to work.
    "You meet with your new HR Director, [the_person.title] in the morning."
    $ the_person.draw_person()
    if the_person is sarah:
        "Since she is new to the company in general, you give [the_person.title] a tour of the company first."
        the_person.char "So... what kind of pharmaceuticals are being researched, exactly?"
        "You decide to just be honest. If she is going to be working here at the company, she is going to figure it out sooner or later anyway."
        mc.name "Well, most of our research right now is targeted toward making people's lives better."
        mc.name "We came across a formula not long ago with almost no known side effects, that with tweaks to the final formula can be used for a number of different things, from increasing happiness to increasing charisma, to making sex better."
        the_person.char "Wow, that sounds very versatile!"
        "After the tour you head back to your office."

    else:
        "You head to your office with her."
    the_person.char "Well, I am excited to have this opportunity. To be honest I'm not really even sure where to begin!"
    mc.name "I'll tell you what, for the rest of this week, why don't you just work alongside the others in the HR department. I'll send over to you my personal dossiers on all the employees, and as you have time you can look over them."
    the_person.char "Okay, I can do that. I'll look over them over the weekend as well. Do you want to plan on having a meeting sometime next week?"
    mc.name "That sounds good. How about we do lunch on Monday? Since you are going to heading up the department, having a meeting every week might be a good idea."
    $ the_person.draw_person(emotion = "happy")
    the_person.char "Great! I'll look forward to it. I'll try to have a plan ready for the meeting on Monday on what we can accomplish."
    "You say goodbye to [the_person.title]."

    # update employee relationships
    python:
        for other_employee in mc.business.get_employee_list():
            town_relationships.begin_relationship(the_person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"

        business_HR_director = the_person
        business_HR_director.HR_tags = {}
        business_HR_director.HR_unlocks = {}

        if the_person is sarah:
            the_person.set_schedule([1,2,3], None)
            mc.business.add_employee_hr(the_person)
            the_person.event_triggers_dict["employed_since"] = day
            mc.business.listener_system.fire_event("new_hire", the_person = the_person)
        else:
            mc.business.remove_employee(the_person)
            mc.business.add_employee_hr(the_person)

        business_HR_director.special_role.append(employee_role)
        business_HR_director.special_role.append(HR_director_role)
        business_HR_director.set_work([1,2,3], mc.business.h_div)

        set_HR_director_tag("business_HR_eff_bonus", mc.business.effectiveness_cap - 100)
        add_hr_director_first_monday_action(the_person)        
    return

label HR_director_first_monday_label(the_person):
    if not is_HR_director_employed(business_HR_director):
        $ business_HR_director = None
        return
    "It's lunchtime, so you prepare to have your first meeting with your new HR Direction, [the_person.title]."
    "You grab your lunch from the break head to your office and sit down."
    $ scene_manager = Scene()
    $ mc.change_location(office)
    $ mc.location.show_background()
    $ the_person.draw_person()
    "Soon, [the_person.title] appears in your door."
    the_person.char "Knock knock!"
    "She walks into your office and sits down across from you."
    $ the_person.draw_person(position = "sitting")
    "You both sit quietly for a minute, eating your lunches together. Eventually you break the silence."
    mc.name "So, did you have a chance to go over those dossiers?"
    the_person.char "I did! Actually. There's a surprising amount of detail in them..."
    the_person.char "I'm not sure I want to know how you gave a numerical rating to girls and their... sexual performance, but it is definitely useful info."
    "[the_person.possessive_title] pulls out a notebook and looks at some notes she has taken."
    the_person.char "So far, aside from personnel, I've noted a few different areas where I think I can improve the efficiency of the business."
    the_person.char "With your approval, I can go ahead and get those started. Are you okay with that?"
    mc.name "Yes, definitely. Efficiency is always a concern at a small business like this."
    call HR_director_calculate_eff(the_person) from HR_director_first_monday_1
    the_person.char "Right, aside from that, I have an idea for a new program. Basically, I noted in the dossiers that there are several employees here who either don't enjoy what they are doing, or are unhappy for some other, unknown reason..."
    the_person.char "My proposal is to start a program where, every weekend I'll go through all the latest employee info and compile a list of girls most at risk at quitting."
    the_person.char "We can call one in, and see if we can have a productive discussion on their reservations. Maybe over time we can even change their opinions on work tasks they don't currently enjoy."
    mc.name "That sounds like a good idea, but why limit it to one girl a week?"
    the_person.char "Well, we don't want to come across as micromanaging. People are more productive if they feel they have some degree of autonomy in their work."
    the_person.char "Besides that, it takes time! And if we did it all the time, I think it would lose some of the effectiveness."
    mc.name "Okay. That all sounds like good ideas. Should we make this Monday lunch a permanent arrangement? We can talk about the developments of the past week, discuss who we want to meet with, and make a plan for the upcoming week."
    $ the_person.draw_person(position = "sitting", emotion = "happy")

    $ (HR_employee_list, HR_tier_talk) = build_HR_review_list(the_person, 0)
    if len(HR_employee_list) == 0:
        the_person.char "That sounds great! Alright, I currently have no employees that would benefit from a meeting, perhaps next week."
    else:
        the_person.char "That sounds great! Alright, I actually have a set of possibilities arranged for a meeting today if you would like. Do you want to go over my list of girls?"
        menu:
            "Let's start next week":
                pass
            "Let's start today":
                mc.name "If you think meeting with some of these girls would be helpful, I think we should start immediately."
                the_person.char "Ok! Let me see who I have on my list here..."
                call HR_director_personnel_interview_label(the_person, max_opinion = 0) from HR_DIR_INTERVIEW_CALL_1

    mc.name "Alright, I think that is all for today. Unless something comes up, same time next week?"
    $ the_person.draw_person(position = "stand2")
    the_person.char "Sounds great! I'll see you then!"
    $ add_hr_director_monday_meeting_action(the_person)
    # HR tiers based on progression. 1 = hired someone. 2 = training videos. 3 = company sponsored sexual training.
    $ set_HR_director_tag('business_HR_tier', 1)

    if the_person is sarah:
        $ add_sarah_third_wheel_action()
    return

label HR_director_monday_meeting_label(the_person):
    if not is_HR_director_employed(business_HR_director):
        $ business_HR_director = None
        return

    $ scene_manager = Scene()

    if mc.location != office:
        "You hurry to your office for your weekly meeting with your HR director [the_person.title]."
        $ mc.change_location(office)
        $ mc.location.show_background()
        the_person.char "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        mc.name "Hi [the_person.title], come in and take a seat."
    else:
        the_person.char "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        "Your HR Director appears in the doorway to your office. It is time for your weekly HR meeting."
        "She sits down across from you and starts to eat her lunch."

    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.sluttiness > 40 and get_HR_director_tag("business_HR_sexy_meeting", False) == False:
        "For some reason, she doesn't begin with her usual efficiency talk. Instead, she seems to be keenly interested in watching you eat..."
        the_person.char "So, before we get started today, I was wondering if umm..."
        mc.name "Yes?"
        "Her cheeks a little flushed, she's obviously embarrassed about what she is about to ask."
        the_person.char "Well... I've just noticed that, we employ women here, and it must be hard on you to be around so many women all day long..."
        "You don't really see where she is going with this."
        the_person.char "It would cause the company a lot of trouble if some sort of sexual harassment suit that would come up."
        mc.name "I suppose."
        the_person.char "So anyway, I thought maybe, to start the meeting, we could fool around a little."
        the_person.char "It would help clear your mind when we talk about the staff as well as give you an outlet for all the tension you have being around women all day..."
        mc.name "That's very generous of you. All in the name of efficiency?"
        the_person.char "Well, plus it would be fun..."
        "You consider her offer."
        mc.name "That would be acceptable, and I can see how it would be helpful to start the meeting with a clear mind."
        "She smiles widely when you accept her explanation. You can tell she really just wants to fuck around..."
        $ set_HR_director_tag("business_HR_sexy_meeting", True)
        the_person.char "So... can we start today?"
        menu:
            "Let's go":
                call HR_director_sexy_meeting_start_label(the_person) from sexy_meeting_start_one
                $ scene_manager.update_actor(the_person, position = "sitting")
                "Feeling good, [the_person.title] returns to her seat and starts to pull out her notes."
            "Not Today":
                the_person.char "Ahh, okay. I know this was short notice, but you can plan on it next week, okay?"
                "She reaches down to her backpack and begins to pull out her notes from the previous week."
    elif get_HR_director_tag("business_HR_sexy_meeting", False) == True:
        "She looks at you intently."
        the_person.char "So, need some relief before we get started today?"
        menu:
            "Let's go":
                call HR_director_sexy_meeting_start_label(the_person) from sexy_meeting_start_two
                $ scene_manager.update_actor(the_person, position = "sitting")
                "Feeling good, [the_person.title] returns to her seat and starts to pull out her notes."
            "Not Today":
                the_person.char "Ahh, damn. Okay, give me a second and we can get started here."
                "She reaches down to her backpack and begins to pull out her notes from the previous week."
    the_person.char "Here are my plans for the week. I think I have a few tweaks to efficiency I can make, but overall I wouldn't expect to see a big change company wide."
    call HR_director_calculate_eff(the_person) from HR_director_monday_meeting_1
    "She hands you a few documents. You check them over."
    mc.name "Looks good. Go ahead and continue with those plans."
    #$ scene_manager.clear_scene()

    $ (HR_employee_list, HR_tier_talk) = build_HR_review_list(the_person, get_HR_director_tag("business_HR_coffee_tier", 0))
    if len(HR_employee_list) == 0:
        the_person.char "Can do! I have currently no girls on my counseling list, perhaps next week."
    else:
        the_person.char "Can do! Did you want to call in a girl for a counseling session this week?"
        menu:
            "Let's not this week":
                pass
            "Call one in":
                mc.name "Yes I want to do that."
                the_person.char "Ok! Let me see who I have on my list here..."
                call HR_director_personnel_interview_label(the_person, max_opinion = get_HR_director_tag("business_HR_coffee_tier", 0)) from HR_DIR_INTERVIEW_CALL_2
                $ set_HR_director_tag("business_HR_meeting_last_day", day)
    the_person.char "Hmm, let's see, what's next..."
    call HR_director_manage_gym_membership(the_person) from HR_Gym_manage_1

    if get_HR_director_tag("business_HR_headhunter_initial", False) == False and recruitment_batch_two_policy.is_owned():  #Unlock the new headhunter rewards
        the_person.char "Our new recruiting software is useful for widening the pool of applicants to hire from, but when you cast a wider net, sometimes you get less than desirable results."
        the_person.char "After this meeting, I'll see if I can rework some of the software to better find applicants for specific departments."
        the_person.char "If you want to find an employee for a specific job, let me know, I might be able to get more fitting results!"
        $ set_HR_director_tag("business_HR_headhunter_initial", True)
    elif get_HR_director_tag("business_HR_headhunter_initial", False) == True:
        call HR_director_monday_headhunt_update_label(the_person) from HR_headhunter_monday_update_1

    the_person.char "Ok, next up, I wanted to review progress made on serums and policy changes from the past week to see if anything might be useful."
    call HR_director_review_discoveries_label(the_person) from HR_DIR_INTERVIEW_CALL_3
    mc.name "Alright, I think that is all for today. Unless something comes up, same time next week?"
    $ the_person.draw_person(position = "stand2")
    the_person.char "Sounds great! I'll see you then!"

    $ add_hr_director_monday_meeting_action(the_person)
    $ the_person.review_outfit(dialogue = False)
    return

label HR_director_personnel_interview_label(the_person, max_opinion = 0):
    $ (HR_employee_list, HR_tier_talk) = build_HR_review_list(the_person, max_opinion)
    if len(HR_employee_list) == 0: #No one qualifies!
        the_person.char "Actually, thing are running really smoothly right now, I didn't come across any dossiers this past weekend that drew my attention!"
        #TODO add another option here? Offer to bring in any girl?
        return
    if HR_tier_talk == 0:
        the_person.char "Alright, here's my list. Who do you want me to call in?"
    elif HR_tier_talk == 1:
        the_person.char "Things are running pretty good right now, but they could always be better. Here's my list, who do you want me to call in?"
    elif HR_tier_talk == 2:
        the_person.char "Honestly? All the girls here like all the policies I've looked at, but its possible with a bit of persuasion we could make them love them."
        the_person.char "Here's my list. Who do you want me to call in?"

    # use new menu layout for selecting people
    if "build_menu_items" in globals():
        call screen main_choice_display(build_menu_items([["Call in"] + HR_employee_list], draw_hearts_for_people = False))
    else:
        call screen main_choice_display([["Call in"] + HR_employee_list])

    $ person_choice = _return
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person.char "Alright, let me go get her."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    #$ renpy.scene("Active")
    #$ scene_manager.clear_scene()
    "[person_choice.title] steps in to the office after a few minutes, followed by [the_person.title]."
    person_choice.char "Hello [person_choice.mc_title]."

    # initialize
    #$ scene_manager = Scene()
    $ scene_manager.add_actor(person_choice, position = "stand3", character_placement = character_left_flipped)
    mc.name "Hello [person_choice.title], come in and take a seat."

    $ scene_manager.update_actor(person_choice, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "stand4")

    if the_person.sluttiness > 80:
        "You notice that [the_person.title] locks the door as she enters your office."

    if the_person.outfit.check_outfit_cum():
        "[person_choice.title] sits down across from you, but is clearly distracted by [the_person.title]. She clearly notices your cum still on her."
        if person_choice.sluttiness > 80:
            person_choice.char "Wow, not sure why you called me in here, but I hope its for the same thing you have her in here for..."
        else:
            person_choice.char "Is that... I'm sorry, what is that you needed, [person_choice.mc_title]?"
        $ person_choice.change_slut_temp(10) # give her a temp slut boost to maybe have a threesome later...
    elif the_person.outfit.vagina_visible():
        "[person_choice.title] sits down across from you, but is clearly distracted by [the_person.title] showing off her pussy."
        $ person_choice.change_slut_temp(5)
        person_choice.char "Uh...right, what can I do for you, [person_choice.mc_title]"
    elif the_person.outfit.tits_visible():
        "[person_choice.title] sits down across from you, but is clearly distracted by the tits of [the_person.title]."
        $ person_choice.change_slut_temp(3)
        person_choice.char "Oh...what can I do for you, [person_choice.mc_title]"

    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        "[person_choice.title] sits down across from you at your desk. [the_person.title] pours a cup of coffee while talking."
        the_person.char "Thanks for coming. [the_person.mc_title] just wanted to have quick chat. Here, have a cup of coffee."
        $ scene_manager.update_actor(the_person, position = "sitting")
        "[person_choice.title] takes the coffee and nods. She takes a few sips as you begin."
    else:
        "[person_choice.title] sits down across from you at your desk. [the_person.title] starts talking while she sits down."
        $ scene_manager.update_actor(the_person, position = "sitting")
        the_person.char "Thanks for coming. [the_person.mc_title] just wanted to have quick chat."

    mc.name "That's right. As you know, we run a small business here, and I like to make sure all my employees enjoy their work here."
    mc.name "Recently, I've become concerned you may not like the work environment."
    python:
        opinion_list = create_HR_review_topic_list(person_choice)
        opinion_chat_list = []
        for opinion in opinion_list:
            if person_choice.get_opinion_score(opinion) <  max_opinion:
                title_desc = opinion.title() + "\n{size=14}" + "She " + opinion_score_to_string(person_choice.get_opinion_score(opinion)) + " it{/size}"
                opinion_chat_list.append([title_desc, opinion])

    $ opinion_chat_list.insert(0, "Discuss Topic")
    if "build_menu_items" in globals():
        call screen main_choice_display(build_menu_items([opinion_chat_list]))
    else:
        call screen main_choice_display([opinion_chat_list])
    $ opinion_chat = _return

    if opinion_chat == "working":
        mc.name "I know that a job is just a job, but I think if you take the time to get to know your fellow employees and come in each day with a good attitude, you could learn to like coming to work every day."
    elif opinion_chat == "HR work":
        mc.name "I know that working with people all day long can be exhausting, but think about how much you can impact your fellow employees if you greet them with a smile every day."
    elif opinion_chat == "production work":
        mc.name "I know that production work is boring and tedious, but it is your hard work down in the production lab that keeps this business moving forward."
    elif opinion_chat == "research work":
        mc.name "I know that sometimes research work feels thankless, but I want you to know right now, I am so thankful for all the hard work you put into the department."
    elif opinion_chat == "marketing work":
        mc.name "I know that marketing work is difficult. For every sale theres dozens of rejections. But I want you know that without your hard work, it doesn't matter how good our product is if no one knows it's being made."
    elif opinion_chat == "supply work":
        mc.name "I know that sourcing chemicals and trying to keep costs down is thankless work, but I want you to know, as the owner of the company, I appreciate your hard work and dedication to doing what needs to be done."
    elif opinion_chat == "work uniforms":
        mc.name "I know that it feels like we are taking some of your creativity away when we assign uniforms. I understand that, but it is also important that we keep a professional atmosphere here."
    elif opinion_chat == "skimpy uniforms":
        mc.name "I know that it feels weird, being asked to come in to work wearing clothes that show a little skin, but in the market we are in, dressing to impress can be a key business advantage."
    else:
        mc.name "I know the policy in place feels weird, but I want you to rethink your opinion on [opinion_chat]. It would be helpful if you would."
    the_person.char "All of our employees are valued here, not just as employees, but as people."
    person_choice.char "Thanks... I guess... I've never really thought about [opinion_chat] like that."
    if person_choice.obedience > 120: #She is obedient
        person_choice.char "I'm not sure I really thought about being here as more than just another job... but I want this place to succeed. I want you to succeed, [person_choice.mc_title]."
    else:
        person_choice.char "I guess I never really thought about it like that. I mean, if I have to have a job... I guess I might as well try to be more positive about it, right?"
    "She stops for a moment and gathers her thoughts."
    person_choice.char "I'll think about this for a bit, but I think I understand what you are saying. I'll try to have a better attitude about [opinion_chat] going forward."
    $ scene_manager.update_actor(person_choice, position = "sitting", character_placement = character_left_flipped, emotion = "happy")
    "[person_choice.title] thinks for a moment, then smiles at both of you."
    if person_choice.sluttiness > 80 and the_person.sluttiness > 80: # TODO come back after writing sarah threesome content to unlock this instead
        person_choice.char "Thanks for calling me in. Is that all? Or was there maybe someone... I mean someTHING else on the to do list?"
        menu:
            "Attempt a threesome with [the_person.title]":
                mc.name "I have one more thing for you before you go..."
                person_choice.char "Yes sir?"
                mc.name "Having this meeting has been great, but, I think you could use a little more... hands on training."
                person_choice.char "Mmm, that sounds nice, is [the_person.name] going to join us?"
                if the_person.outfit.check_outfit_cum():
                    "With [the_person.title] still wearing your cum from her service earlier, you get a burst of energy and arousal."
                    $ mc.change_arousal(30)
                    $ mc.change_energy(100)
                mc.name "Of course. Let's get started."
                call start_threesome(person_choice, the_person) from threesome_HR_meeting_happy_ending
                person_choice.char "Oh my... that was fun. Thanks for calling me in! I guess I'd better go get back to work..."
                if the_person == sarah:
                    $ the_person.change_happiness(10)
            "That's all":
                person_choice.char "Thanks for calling me in... I guess I'd better go get back to work!"

    else:
        person_choice.char "Thanks for calling me in... I guess I'd better go get back to work!"
    if opinion_chat in opinions_list:
        $ person_choice.opinions[opinion_chat] = [max_opinion, True]
    else:
        $ person_choice.sexy_opinions[opinion_chat] = [max_opinion, True]
    $ scene_manager.update_actor(person_choice, position = "walking_away", character_placement = character_left_flipped)
    $ scene_manager.update_actor(the_person, position = "stand2", character_placement = character_right)
    "[the_person.title] gets up and walks [person_choice.title] to the door."
    "They exchange a few pleasantries before [person_choice.title] leaves the room."
    $ scene_manager.remove_actor(person_choice)
    # remove actor first (without reset), so she continues the meeting as she was dressed before
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    $ scene_manager.clear_scene()
    "[the_person.title] comes back to the desk and sits down."
    $ the_person.draw_person(position = "sitting")

    #Cleanup?
    python:
        del HR_employee_list
        del opinion_list
        del opinion_chat_list
        del person_choice
    return

label HR_director_review_discoveries_label(the_person):
    "[the_person.title] pulls out a report on all the latest achievements of the research department."
    if get_HR_director_tag("business_HR_serum_tier", 0) == 0:
        if off_label_drugs.researched: #Researched!
            $ set_HR_director_tag("business_HR_serum_tier", 1)
            the_person.char "Hmmm... interesting."
            "[the_person.title] looks closely at one of the serums that has been researched."
            the_person.char "I see here that you've managed to create a serum that has the ability to increase a person's... suggestibility?"
            mc.name "Right. Basically it sets up the brain to make new connections it might not have previously made, opening up a person to suggestions they may not normally consider."
            the_person.char "That would actually be useful... We could use some, in the coffee we make when we bring them in for meetings?"
            mc.name "A version of the serum with a short useful life would be useful for giving the meetings more impact."
            "[the_person.title] looks into more details of the serum."
            the_person.char "Looks like the serum is fairly easy to produce. I'd say for about $500 we could probably setup an something long term for the monday meetings..."
            mc.name "Noted. I'll consider it and get back to you if I decide to do this."
            the_person.char "Sounds good [the_person.mc_title]!"

    if get_HR_director_tag("business_HR_serum_tier", 0) == 1:
        if blood_brain_pen.researched: #Researched!
            $ set_HR_director_tag("business_HR_serum_tier", 2)
            the_person.char "Hmmm... interesting."
            "[the_person.title] looks closely at one of the serums that has been researched."
            the_person.char "I see here that you've managed to improve on an earlier design to increase a person's suggestibility!"
            mc.name "Right. It bypasses connections that would normally trigger a rejection response and causes the person to consider actions that would normally be rejected."
            if get_HR_director_tag("business_HR_coffee_tier", 0) == 0:
                the_person.char "I know I brought this up last time we researched a similar serum, but having a serum like that to give employees when they come in for reviews would be very useful."
                the_person.char "You should definitely consider it. I think it would give our meetings more impact with employees."
                the_person.char "This version of the serum... I think we could get something setup for about $1500. It's a little difficult to synthesize."
                mc.name "Noted. I'll consider it and get back to you if I decide to do this."
                the_person.char "Sounds good [the_person.mc_title]!"
            else:
                the_person.char "We already have the equipment setup form the previously researched serum. We should be able to modify it to take advantage of this advancement."
                "[the_person.title] checks her notes on the synthesis process."
                the_person.char "I think for about $1500 we could probably set something similar up for this one. It would give out meetings considerably more impact."
                mc.name "Noted. I'll consider it and get back to you if I decide to do this."
                the_person.char "Sounds good [the_person.mc_title]!"

    if get_HR_director_tag("business_HR_serum_tier", 0) == 2:
        if mind_control_agent.researched: #Researched
            $ set_HR_director_tag("business_HR_serum_tier", 3)
            the_person.char "Wow... this is crazy."
            "[the_person.title] looks closely at one of the serums that has been researched."
            the_person.char "It says here, you have researched a serum that allows for temporary mind control!?!"
            mc.name "Right. It bypasses all inhibitions and allows direct implantation of suggestions."
            the_person.char "So... obviously the ethics of this are dubious but... You could do incredible things with it, from an HR standpoint."
            mc.name "Well, we've had to dilute it quite a bit. High concentrations can have pretty bad side effects."
            the_person.char "So... maybe we could consider creating a concentrated, single use version? With something like that, we could change a girl's work opinions all at once!"
            the_person.char "Looks like for about $5000 we could stock a single use version like that. It would be pretty challenging to synthesize."
            mc.name "Noted. I'll consider it and get back to you if I decide to do this."
            the_person.char "Sounds good [the_person.mc_title]!"


    if the_person is sarah:
        if get_HR_director_tag("business_HR_serum_breast", False)  == False:
            if breast_enhancement.researched: #Researched!
                $ set_HR_director_tag("business_HR_serum_breast", True)
                "Suddenly, [the_person.title] sits straight up in her chair as she reads the report."
                the_person.char "Wait wait... you managed to synthesize a serum that can increase breast size?"
                mc.name "Right. It works with the pancreas to deliver local growth of fatty tissue to the breasts."
                the_person.char "That's amazing! And it says here it won't leave behind stretch marks?"
                mc.name "Correct. We were able to combine the enhancement of fatty tissue with a temporary increase in skin elasticity."
                the_person.char "That incredible... but I can't afford..."
                "She furrows her brow when she sees the initial estimate of the cost of the synthesization."
                the_person.char "I mean uh, it'll be interesting to see how this progresses..."
                "You notice [the_person.title] writing herself a note to visit the research department later."
                #TODO add breast serum sneak event to mandatory list
                $ add_sarah_catch_stealing_action()
    "You spend a few minutes with [the_person.title] going over the progress in the research department over the last week or so."
    the_person.char "That's it for research, let's take a look at policy changes from the last week."
    if get_HR_director_tag("business_HR_uniform", False) == False:
        if relaxed_uniform_policy.is_owned():
            the_person.char "Hmmm, I see here that we have recently opened up company policy to allow for uniform guidelines."
            the_person.char "This is something that could potentially alienate some of our employees. It might be a good idea if we include opinions on work uniforms when meeting one on one with them."
            "You hadn't considered how your employees would react when you instituted the uniform policy. You decide [the_person.possessive_title] is right."
            mc.name "That's a good idea. Go ahead and implement that going forward."
            the_person.char "Sure thing [the_person.mc_title]!"
            $ set_HR_director_tag("business_HR_uniform", True)
    elif get_HR_director_tag("business_HR_skimpy_uniform", False) == False:
        if corporate_enforced_nudity_policy.is_owned():
            if the_person.sluttiness > 40:  #She only volunteers to start doing this if she is slutty enough.
                the_person.char "I see here that the uniform policy has recently been loosened further."
                the_person.char "Personally, I think it is great that I can come to work and show off lots of skin, but with the latest change in uniform policy, it might be intimidating to employees who don't like skimpy uniforms."
                the_person.char "It might be a good to idea to include opinions on skimpy uniforms when meeting one on one with employees."
                "You realize the swing in the uniform policy might be a bit much for some girls, so this is probably a good thing to start counseling for."
                mc.name "That's a good idea. Go ahead and implement that going forward."
                the_person.char "Sure thing [the_person.mc_title]!"
                $ set_HR_director_tag("business_HR_skimpy_uniform", True)
                if the_person is sarah:
                    the_person.char "Mmm, I can't wait to see what some of the outfits other girls wear around the office..."
                    $ the_person.change_slut_temp(5)
    if get_HR_director_tag("business_HR_relative_recruitment", 0) == 0:
        if (mc.business.max_employee_count - mc.business.get_employee_count()) > 4:
            the_person.char "I see here that changes within the company have produced several vacancies."
            the_person.char "If you like, I could post something in the break room that we are looking for more employees."
            the_person.char "Several of the women who work here have children or relatives who could use the work. They might be more likely to come to you asking for employment if they know we need the help."
            "You consider what she is saying. It might be good for company morale to have mothers and their daughters both employed by you. Who knows, it could lead to other situations too."
            "You weigh the option. Do you want to post something?"
            menu:
                "Approve":
                    mc.name "That's a good idea. Go ahead and implement that going forward."
                    $ update_hire_daughter_crisis(10)
                    $ set_HR_director_tag("business_HR_relative_recruitment", 2)
                "Deny":
                    mc.name "I think for now I'd like to stick with more traditional recruiting methods."
                    $ set_HR_director_tag("business_HR_relative_recruitment", 1)

            "Sure thing [the_person.mc_title]. If you change your mind in the future, just let me know. I can always put the sign up or down based on what we need at the time."

    if get_HR_director_tag("business_HR_meeting_on_demand", False) == False:
        if mc.business.get_employee_count() > 10:
            the_person.char "I see the business has grown. We now have a double digit number of employees!"
            the_person.char "I was thinking, with the number of employees we have now, we could probably do our one on one meetings more often without losing their effectiveness."
            the_person.char "We still don't want to do it too often, but I was thinking we could have meetings as often as once a day?"
            "With your growing number of employees, it makes sense that you would be able to have meetings more often."
            mc.name "I'll keep that in mind going forward. If I want to have a meeting with an employee, I'll make sure to come find you first."
            the_person.char "Great! I think that will work out nicely."
            $ set_HR_director_tag("business_HR_meeting_on_demand", True)

    if HR_director_gym_membership_tier_1_requirement(the_person) and get_HR_director_tag("business_HR_gym_msg_tier", 0) == 0:
        $ set_HR_director_tag("business_HR_gym_msg_tier", 1)
        the_person.char "With our small, but growing employee group, I thought it might be worth looking into a company sponsored gym fitness program."
        the_person.char "I did some research, and it turns out there is a local one with a nice facility with great pricing for companies."
        mc.name "How much would it cost?"
        the_person.char "For the company I found, the pricing is $5 per person, per week."
        mc.name "That seems pretty reasonable actually. What benefits would it provide?"
        the_person.char "Well, having something like that available to employees would certainly help employees get more fit."
        the_person.char "It might take a while to see changes, but I would say girls would have more energy over all."
        mc.name "Okay, I'll consider it and get back to you on that."

    if HR_director_gym_membership_tier_2_requirement(the_person) and get_HR_director_tag("business_HR_gym_msg_tier", 0) == 1:
        $ set_HR_director_tag("business_HR_gym_msg_tier", 2)
        the_person.char "The company is getting bigger, and I was thinking about possible benefits to the company for increasing good health habits of the employees."
        the_person.char "There is a company that specializes in information campaigns on healthy eating habits, exercise, and good mental health."
        the_person.char "Combined with the company gym membership, I think we would see a sizable benefit to the company as a whole."
        mc.name "How much would it cost?"
        the_person.char "For the company I found, the pricing is $10 per person, per week. This would be on top of the $5 per person for the company gym membership."
        mc.name "What would be the benefits we would see if we invest in this?"
        the_person.char "Well, generally it would increase the energy of employees as they develop healthier eating patterns."
        the_person.char "Additionally, I think employees with interests in sports and hiking would really appreciate the change also."
        mc.name "Okay, I'll consider it and get back to you on that."
    return

label HR_director_manage_gym_membership(the_person):
    if get_HR_director_tag("business_HR_gym_tier", 0) == 0:
        $ cost = 0
        return
    elif get_HR_director_tag("business_HR_gym_tier", 0) == 1:
        python:
            for x in mc.business.get_employee_list():
                if x.max_energy < 120:
                    if x.get_opinion_score("sports") > 0:
                        x.change_max_energy(3 * x.get_opinion_score("sports"), add_to_log = False)
                    else:
                        x.change_max_energy(2, add_to_log = False)
                if x.get_opinion_score("sports") > 0:
                    x.change_happiness(3 * x.get_opinion_score("sports"))
                if x.get_opinion_score("hiking") > 0:
                    x.change_happiness(1 * x.get_opinion_score("sports"))
            cost = len(mc.business.get_employee_list()) * 5
    elif get_HR_director_tag("business_HR_gym_tier", 0) == 2:
        python:
            for x in mc.business.get_employee_list():
                if x.max_energy < 150:
                    if x.get_opinion_score("sports") > 0:
                        x.change_max_energy(3 * x.get_opinion_score("sports"), add_to_log = False)
                    else:
                        x.change_max_energy(2, add_to_log = False)
                if x.get_opinion_score("sports") > 0:
                    x.change_happiness(5 * x.get_opinion_score("sports"))
                if x.get_opinion_score("hiking") > 0:
                    x.change_happiness(2 * x.get_opinion_score("sports"))
            cost = len(mc.business.get_employee_list()) * 15
    the_person.char "Just to let you know, I wrote out the check this morning for this week's employee health program."
    $ mc.business.change_funds(-cost)
    return

label HR_director_coffee_tier_1_label(the_person):
    $ mc.business.change_funds(- 500)
    mc.name "I've been thinking about your proposal to add serums to the coffee we serve to employees when we meet with them. I'm giving you approval to set it up."
    the_person.char "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person.char "I'll keep it in a locked cabinet and from now on I'll only use it when we give an employee coffee during our monday meetings."
    mc.name "Sounds good."
    the_person.char "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_coffee_tier", 1)
    return

label HR_director_coffee_tier_2_label(the_person):
    $ mc.business.change_funds(- 1500)
    mc.name "I've been thinking about your proposal to add the stronger serum to the coffee we serve to employees when we meet with them. I'm giving you approval to set it up."
    the_person.char "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person.char "I'll keep it in a locked cabinet and from now on I'll only use it when we give an employee coffee during our monday meetings."
    mc.name "Sounds good."
    the_person.char "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_coffee_tier", 2)
    return

label HR_director_calculate_eff(the_person):
    $ HR_dir_factor = 0
    if not get_HR_director() is None:
        $ HR_dir_factor = ((the_person.charisma * 2 ) + the_person.hr_skill)   #Charisma + HR skill
        #TODO make events later on that factor this to be better
    $ HR_dir_factor += get_HR_director_tag("business_HR_eff_bonus")
    $ mc.business.effectiveness_cap = (100 + HR_dir_factor)   #100% base effectiveness
    return

label HR_director_gym_membership_tier_1_label(the_person):
    mc.name "I've been thinking about your proposal to sponsor a company gym membership. I'm giving you approval to set it up."
    the_person.char "Sounds good sir! I'll have that set up and ready to begin next week."
    mc.name "Sounds good."
    the_person.char "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_gym_tier", 1)
    return

label HR_director_gym_membership_tier_2_label(the_person):
    mc.name "I've been thinking about your proposal to sponsor a company wide health program. I'm giving you approval to set it up."
    the_person.char "Sounds good sir! I'll have that set up and ready to begin next week."
    mc.name "Sounds good."
    the_person.char "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_gym_tier", 2)
    return

label HR_director_change_relative_recruitment_label(the_person):
    if get_HR_director_tag("business_HR_relative_recruitment", 2):
        the_person.char "I see, are you sure you want me to take down the sign in the break room that we are looking for more employees?"
        menu:
            "Take the Sign Down":
                the_person.char "Ok, I'll take it down as soon as we are finished here. Is there anything else I can do for you?"
                $ update_hire_daughter_crisis(2)
                $ set_HR_director_tag("business_HR_relative_recruitment", 1)
            "Leave the Sign Up":
                the_person.char "Oh... sorry I thought you said you wanted to change it. Is there anything else I can do for you?"
        return
    else:
        the_person.char "I see, are you sure you want me to put the sign in the break room that we are looking for more employees?"
        menu:
            "Put the Sign Up":
                the_person.char "Ok, I'll put it up as soon as we are finished here. Is there anything else I can do for you?"
                $ update_hire_daughter_crisis(10)
                $ set_HR_director_tag("business_HR_relative_recruitment", 2)
            "Leave the Sign Down":
                the_person.char "Oh... sorry I thought you said you wanted to change it. Is there anything else I can do for you?"
        return

label HR_director_meeting_on_demand_label(the_person):
    $ scene_manager = Scene() # make sure we have an empty scene manager for on-demand meetings
    the_person.char "Okay, I think I have time for that! Let me grab my dossiers from Monday and I'll meet you in your office."
    "You head to your office and [the_person.possessive_title] quickly arrives with her papers."
    $ the_person.draw_person(position = "sitting")
    the_person.char "Ok! Let me see who I have on my list here..."
    call HR_director_personnel_interview_label(the_person, max_opinion = get_HR_director_tag("business_HR_coffee_tier", 0)) from HR_DIR_INTERVIEW_CALL_4
    the_person.char "I'd say that went pretty well! I'm going to head back to work, if that is okay with you, [the_person.mc_title]?"
    "You thank her for her help and excuse her. She gets up and leaves you to get back to work."
    $ scene_manager.clear_scene()
    $ set_HR_director_tag("business_HR_meeting_last_day", day)
    call advance_time from hr_advance_time_one
    return

label HR_director_sexy_meeting_start_label(the_person):
    #Phases of this label.
    #   First we determine if we have any new acts of service our girl is willing to perform.
    #   If not, give the player the option to choice an unlocked act of service
    #   Next, perform the act
    #   Then, clean up, with higher sluttiness giving the player the option to have her not clean up.

    if get_HR_director_unlock("blowjob") == False:  #This is the first time this function has been run
        the_person.char "So... I have no idea the best way to do this..."
        mc.name "Why don't you just come over here and give me a blowjob."
        the_person.char "Okay! That should be fun!"
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "[the_person.possessive_title] comes around to your side of the desk and gets down on her knees. She pulls down your zipper and pulls your cock out."
        the_person.char "Mmm, it smells so good. Let's get this taken care of!"
        "She runs her tongue up and down your length a few times, then parts her lips and begins to suck you off."
        $ mc.change_arousal(40)
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_start_one
        mc.name "Mmm, this is a great way to start Monday. This was a great idea [the_person.title]."
        $ scene_manager.update_actor(the_person, emotion = "happy")
        "[the_person.possessive_title] stops licking the cum off her lips for a second and smiles."
        the_person.char "Thank you sir! I am willing to do this next week again if you decide to."
        $ set_HR_director_unlock("blowjob", True)
        "She cleans herself up and makes herself presentable again."

        $ the_person.review_outfit(dialogue = False)
        return

    if get_HR_director_unlock("titfuck") == False:
        if the_person == sarah and sarah.event_triggers_dict.get("epic_tits_progress", 0) > 1:
            the_person.char "So... I was thinking this week maybe I could do that thing again. You know, where I put your cock between my tits?"
            the_person.char "It felt soooo good last time. I've been thinking about it a lot."
            mc.name "That sounds great, I'll admit it, seeing my cock between your tits is hot."
            if the_person.outfit.tits_available():
                "With her tits already out and ready to be used, she just gives you a big smile."
            else:
                "[the_person.possessive_title] begins to take off her top."
                $ scene_manager.strip_actor_outfit(the_person, exclude_lower = True)
                "With her tits out and ready to be used, she gives you a big smile."
            $ mc.change_arousal(20)
            $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
            "She gets up and starts walking around the desk. By the time she gets to you, you already have your rock hard dick out."
            "She gets on her knees and gives you a couple strokes with her hand."
            $ mc.change_arousal(20)
            the_person.char "Mmmm, I love the feeling of a cock buried between by big tits... this is gonna be great!"
            "With her hands on each side of her chest, she wraps her sizable boobs around you and begins to bounce them up and down."
            call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_start_two
            $ set_HR_director_unlock("titfuck", True)
            "After you finish, [the_person.possessive_title] runs her hands along her tits, rubbing your cum into her skin."
            the_person.char "Mmm, god that was hot. Let me just enjoy this a minute before we move on with the meeting..."
            "You run your hands through her hair for a bit while she enjoys the warmth of your cum on her skin."
            "Eventually she cleans herself up and makes herself presentable again."
            $ the_person.review_outfit(dialogue = False)
            return

    if get_HR_director_unlock("missionary on desk") == False:
        if (the_person.sluttiness + the_person.get_opinion_score("vaginal sex") * 5) >= 60:
            the_person.char "Hey... you know what would be really hot?"
            "You feel yourself raise your eyebrow in response. This should be good!"
            the_person.char "What if I just layed down on your desk and you had your way with me, right here in your office?"
            the_person.char "Having my boss pin me to his desk and ravage me..."
            $ mc.change_arousal(20)
            mc.name "I'm think thats a good idea. Why don't you get your ass over here and we'll find out for sure!"
            the_person.char "Oh! Yes sir!"
            "[the_person.possessive_title] gets on your desk and lays on her back."
            $ scene_manager.update_actor(the_person, position = "missionary", emotion = "happy")
            if the_person.outfit.vagina_available():
                "She spreads her legs, her pussy on display in front of you."
            else:
                "You start to strip [the_person.possessive_title] down."
                $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
                "Soon her body is on full display in front of you, on your desk."
            $ mc.change_arousal(20)
            "You have your cock out in a flash. You position it at her slick entrance."
            "You push yourself inside of her nice and slow, since she hasn't had much time to warm up yet."
            the_person.char "Mmmm, [the_person.mc_title]. Use me boss! I'm here to serve you!"
            "You start to piston your cock in and out of her."
            call fuck_person(the_person, start_position = missionary, start_object = make_desk(), skip_intro = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_meeting_start_three
            $ set_HR_director_unlock("missionary on desk", True)
            "[the_person.possessive_title] lays on your desk, recovering."
            mc.name "You were right, [the_person.title]. It IS really hot to fuck you on my desk!"
            the_person.char "Ah, yes, I suspected it would be, sir!"
            "Eventually she cleans herself up and makes herself presentable again."
            $ the_person.review_outfit(dialogue = False)
            return

    if get_HR_director_unlock("bent over desk") == False:
        if (the_person.sluttiness + the_person.get_opinion_score("doggy style sex") * 5) >= 70:
            if the_person.obedience > 130:
                mc.name "Come here, I'm going to use you the way I see fit today."
                if the_person.get_opinion_score("being submissive"):
                    the_person.char "Oh! Yes sir!"
                    $ the_person.change_obedience(3)
                else:
                    the_person.char "Ok..."
                "You stand up as she walks around to your side of the desk. You roughly turn her around and bend her over your desk."
                $ scene_manager.update_actor(the_person, position="standing_doggy")
                $ mc.change_arousal(20)
                the_person.char "Oh my!"
                $ set_HR_director_unlock("bent over desk", True)

                if the_person.outfit.vagina_available():
                    "She wiggles her hips back at you a bit. Her pussy lips glisten with a bit of moisture."
                else:
                    "You start to strip [the_person.possessive_title] down."
                    $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
                    "Soon her ass is on full display in front of you, bent over your desk."
                "You push yourself inside of her nice and slow, since she hasn't had much time to warm up yet."
                the_person.char "Oh God! its going so deep."
                $ mc.change_arousal(20)
                "You give her ass a solid spank, then begin to fuck her roughly."
                call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_desk(), skip_intro = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_meeting_start_four
                $ the_report = _return
                if the_report.get("girl_orgasms",0)>0:
                    "[the_person.possessive_title] is still bent over your desk, recovering from her orgasm."
                    the_person.char "That's... yeah you can do that to me any time."
                else:
                    "[the_person.possessive_title] slowly recovers from using her body for your pleasure."
                    the_person.char "Mmm, happy to be of service, sir. We can do that again next time... if you want!"
                "Eventually she cleans herself up and makes herself presentable again."
                $ the_person.review_outfit(dialogue = False)
                return


    the_person.char "Okay! How do you want me to take care of you this week, [the_person.mc_title]?"

    python:
        tuple_list = []
        for position in business_HR_director.HR_unlocks.keys():
            if business_HR_director.HR_unlocks[position] == True:
                tuple_list.append([position.title(), position])
        tuple_list.append(["Surprise me", "any"])

        position_choice = renpy.display_menu(tuple_list,True,"Choice")
        del tuple_list

    if position_choice == "any":
        the_person.char "Mmmm, I can do that! "
        $ mc.change_arousal(20)
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(-5)
        $ position_choice = get_random_from_list(business_HR_director.HR_unlocks.keys())

    if position_choice == "blowjob":
        the_person.char "Get your cock out, I want to taste it!"
        "[the_person.possessive_title] stands up and starts to walk around the desk while you pull out your erection."
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "She gets down on her knees in front of you and takes a moment to admire your hardness."
        $ mc.change_arousal(20)
        "She opens her mouth and runs her tongue along it a few times, and then parts her lips and begins to suck you off."
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_mid_one

    elif position_choice == "titfuck":
        if not the_person.outfit.tits_available():
            "[the_person.possessive_title] begins to take off her top. "
            $ scene_manager.strip_actor_outfit(the_person, exclude_lower = True)
            "With her tits out and ready to be used, she gives you a big smile."
        the_person.char "Get your cock out, I want to feel it slide between my boobs!"
        $ mc.change_arousal(20)
        "You pull your cock out as she gets up and walks around your desk. She drops down on her knees in front of you."
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "[the_person.possessive_title] smiles at you as she uses her hands to wrap her tits around your cock, and then starts to move them up and down."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_mid_two

    elif position_choice == "missionary on desk":
        if not (the_person.outfit.vagina_available() and the_person.outfit.vagina_visible()):
            "[the_person.possessive_title] begins to take off her clothes. "
            $ scene_manager.strip_actor_outfit(the_person, exclude_upper = True, exclude_lower = False)
            "When she finishes getting naked, she gives you a big smile."
        the_person.char "Oh my, fucking me on your desk? You are so naughty, [the_person.mc_title]!"
        $ scene_manager.update_actor(the_person, position = "missionary")
        mc.name "Oh, I'm the naughty one? I seem to remember this was your idea in the first place..."
        "You pull your cock out and line it up with [the_person.title]'s pussy. You ease yourself inside of her with one slow, smooth push."
        $ mc.change_arousal(20)
        the_person.char "I never said I wasn't naughty too... Oh god, [the_person.mc_title], that feels good. Have your way with me!"
        call fuck_person(the_person, start_position = missionary, start_object = make_desk(), skip_intro = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_meeting_mid_three

    elif position_choice == "bent over desk":
        mc.name "Get over here, I'm going to bend you over my desk again."
        if the_person.get_opinion_score("being submissive"):
            the_person.char "Oh! Yes sir!"
            $ the_person.change_obedience(2)
        else:
            the_person.char "Ok."
        "You stand up as she walks around to your side of the desk. You roughly bend her over your desk and give her ass a spank."
        $ scene_manager.update_actor(the_person, position="standing_doggy")
        the_person.char "Oh my!"

        if the_person.outfit.vagina_available() and the_person.outfit.vagina_visible():
            "She wiggles her hips back at you a bit. Her pussy lips glisten with a bit of moisture."
        else:
            "You start to strip [the_person.possessive_title] down."
            $ scene_manager.strip_actor_outfit(the_person, exclude_upper = True, exclude_lower = False)
            "Soon her ass is on full display in front of you, bent over your desk."
        "You don't waste any time. You pull your cock out and point it at her slit. You pull her hips back as you push inside of her with one smooth push."
        the_person.char "Mmm, fuck me good [the_person.mc_title]!"
        $ mc.change_arousal(20)
        "You eagerly begin to pump your hips and fuck your HR director over your desk."
        call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_desk(), skip_intro = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_meeting_mid_four


    if ((the_person.obedience - 100) + the_person.sluttiness) > 100: #If she is either very obedient, slutty, or a mixture
        menu:
            "Tell her to stay like that for the meeting":
                mc.name "I'm very busy, lets just continue the meeting. Don't bother to clean up."
                "[the_person.title] opens her mouth for a second, ready to protest, but quickly reconsiders."
                the_person.char "Of course, [the_person.mc_title]. Let's see what is next."
            "Let her clean herself up":
                $ the_person.review_outfit(dialogue = False)
                "[the_person.possessive_title] quickly cleans herself up, ready to continue the meeting."
    else:
        "She quickly starts to get dressed to continue your meeting."


    return

label HR_director_mind_control_label(the_person):
    $ mc.business.change_funds(- 5000)
    mc.name "I've been thinking about your proposal to create a specialized serum for mind control attempts. I would like to move forward with it."
    the_person.char "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person.char "I'll make sure it stay locked away, and only you and I will have a key to get some out."
    mc.name "Sounds good."
    the_person.char "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_serum_tier", 4)
    return

label HR_director_mind_control_attempt_label(the_person):
    $ scene_manager = Scene()
    $ backfire_odds = 100
    $ HR_employee_list = build_HR_mc_list(the_person)
    if len(HR_employee_list) == 0: #No one qualifies!
        the_person.char "Actually, things are running really smoothly right now, I'm not sure that would be beneficial?"
        return

    the_person.char "Okay... remember this act has a chance of backfiring, having all kinds of unknown side effects. Are you sure you want to continue?"
    "Note: The chance of the session backfiring is directly related to your mastery level of the Mind Control serum effect!"
    $ backfire_odds = mind_control_agent.base_side_effect_chance / mind_control_agent.mastery_level
    "Current odds of backfiring are: [backfire_odds]. Successful mind control will increase all current trainable opinions by 1 tier. Are you sure you want to attempt?"
    menu:
        "Yes":
            pass
        "No":
            return
    the_person.char "Okay. Who do you want me to make the attempt on?"

    if "build_menu_items" in globals():
        call screen main_choice_display(build_menu_items([["Call in"] + HR_employee_list], draw_hearts_for_people = False))
    else:
        call screen main_choice_display([["Call in"] + HR_employee_list])

    $ person_choice = _return

    the_person.char "Okay. I'll go get her."
    $ renpy.scene("Active")
    call HR_mind_control_attempt(person_choice, the_person) from HR_mind_control_attempt_call_1

    $ scene_manager.clear_scene()
    $ set_HR_director_tag("business_HR_meeting_last_day", day)
    call advance_time from hr_advance_time_two
    return True

label HR_mind_control_attempt(the_person, the_HR_dir):
    "[the_HR_dir.title] returns with [the_person.title]."
    $ scene_manager.add_actor(the_HR_dir)
    $ scene_manager.add_actor(the_person,  character_placement = character_left_flipped)
    the_person.char "You wanted to see me sir?"
    mc.name "Ah, yes, thank you for coming. [the_person.title], we are trying a new experimental counseling method, that we are combining with one our recent serum developments."
    mc.name "I've asked you to come, because I would like you to help us test it. [the_HR_dir.title] here is going to administer the session."
    "She looks a bit concerned when you tell her what you want her to do."
    if the_person.obedience > 130:
        "When she looks into your eyes though, you can see her hesitation vanish. Her obedience to you melts away her objections."
    else:
        the_person.char "I don't know sir... are you sure this is safe?"
        menu:
            "(Lie) It is perfectly safe" if mc.charisma > 4:
                pass
            "There are risks involved":
                the_person.char "I'm not sure I want to do that. Why should I agree to something like this?"
                menu:
                    "I'll reward you sexually" if the_person.sluttiness > 60:
                        "Her face lights up at the prospect of having some alone time with you."
                        #TODO code it so it happens
                    "It would mean a lot to me" if the_person.love > 60:
                        "Her face softens when you appeal to her emotionally."
                    "I'll reward you financially ($1000)":
                        the_person.char "Oh... well I suppose I could really use the extra pay."
                        $ mc.business.change_funds(- 1000)
                    "I'll fire you if you don't.":
                        $ scene_manager.update_actor(the_person, emotion = "angry")
                        the_person.char "What!?! You're kidding me? I can't afford to lose this job right now!"
                        if the_person.happiness > 90:
                            $the_person.change_happiness(70 - the_person.happiness)
                        else:
                            $the_person.change_happiness(-35)

    the_person.char "Okay... I'll do it. Let's get this over with!"
    the_HR_dir.char "Alright. Come with me, and we will get the process started."
    $ scene_manager.remove_actor(the_person)
    $ scene_manager.remove_actor(the_HR_dir)
    "The two girls get up and leave to go to a quite room where [the_HR_dir.title] makes the mind control attempt."
    "You return to your work while the attempt is made."
    "..."
    "....."
    $ is_backfire = False
    $ backfire_odds = mind_control_agent.base_side_effect_chance / mind_control_agent.mastery_level
    if int(backfire_odds) > renpy.random.randint(0,100): #FAIL
        $ backfire_string = mind_control_backfire(the_person)
        "The mind control event has backfired!"
        #TODO add backfire string to event log
        $ is_backfire = True
    else:
        python:
            topic_list = create_HR_review_topic_list(the_person)
            for topic in topic_list:
                update_opinion(the_person, topic)

    $ scene_manager.add_actor(the_HR_dir)
    "[the_HR_dir.title] eventually returns."
    mc.name "Welcome back. How did it go?"
    if is_backfire:
        the_HR_dir.char "Unfortunately, the attempt backfired. I'm not sure yet what the effects were, but they certainly weren't the desired ones."
        mc.name "That is... unfortunate."
        the_HR_dir.char "She is resting for now. It would probably be best to leave her to rest, but if you want you can go and see her."
    else:
        the_HR_dir.char "I believe the attempt was successful. I have no indication that she experienced any side effects."
        mc.name "Excellent. Good work [the_HR_dir.title]"
        the_HR_dir.char "She is resting for now, but before I left she asked to see you. It's up to you if you want to go see her."
    mc.name "Thank you. I'll consider it. That'll be all for now."
    $ scene_manager.remove_actor(the_HR_dir)
    "[the_HR_dir.title] leaves."
    #TODO the rest of this encounter. Go see her, pay her with sexual favors, etc.
    return

label HR_director_appointment_action_label:
    $ people_list = get_sorted_people_list(mc.business.hr_team, "Appoint", ["Back"])

    if "build_menu_items" in globals():
        call screen main_choice_display(build_menu_items([people_list]))
    else:
        call screen main_choice_display([people_list])
    $ person_choice = _return
    $ del people_list

    if person_choice == "Back":
        return

    call HR_director_initial_hire_label(person_choice) from _call_HR_director_initial_hire_label_appointment
    return

label HR_director_headhunt_initiate_label(the_person):
    mc.name "I'd like to initiate a search for a specific job opening."
    the_person.char "Ah! Okay, just fill out this form with your requirements."

    $ reset_headhunter_criteria()
    $ hide_ui()
    call screen HR_director_recruitment_screen(the_person)
    $ show_ui()
    if _return:
        python:
            days_to_find = 1
            if get_HR_director_tag("recruit_obedience", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_focused", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_marital", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_slut", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_kids", 0) != 0:
                days_to_find += 1
            if get_HR_director_tag("recruit_height", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_body", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_bust", None) is not None:
                days_to_find += 1

        the_person.char "Okay, I'll go ahead and start the search."
        if days_to_find <= 2:
            the_person.char "This shouldn't take me long. Hopefully just a day or two!"
        elif days_to_find <= 5:
            the_person.char "Alright, this is fairly specific, so give me a few days to see what I can find and I'll get back to you."
        else:
            the_person.char "This is... pretty specific. It'll probably take me at least a week to find someone who meets all these criteria!"
        mc.name "Thank you. Let me know when you have found someone and we'll do the interview."

        $ set_HR_director_tag("recruit_day", day + days_to_find)
        $ set_HR_director_tag("business_HR_headhunter_progress", 1)

        $ add_hr_director_headhunt_interview_action(the_person)
        the_person.char "Is there anything else you need?"
    else:
        mc.name "I've changed my mind."
        the_person.char "No problem, just let me know if you want me to start recruiting someone."
    return

label HR_director_headhunt_interview_label(the_person):
    $ prospect = generate_HR_recruit()
    $ scene_manager = Scene()  #Start fresh like Trist always says
    $ set_HR_director_tag("business_HR_headhunter_progress", 2)
    if mc.location != office:
        "You are hard at work when you get a message from your HR supervisor."
        the_person.char "Hey, I got a hit on criteria you had for a prospective employee. Want me to send you the info?"
        if mc.business.max_employee_count == mc.business.get_employee_count():  #We accidentally filled all available slots
            mc.name "Actually, I accidentally filled that position already. Sorry, I must have forgotten to tell you."
            "A few minutes later, she responds to you."
            the_person.char "Ah... ok, well try to let me know next time, okay?"
            "You promise to do so."
            return
        mc.name "Sure, meet me in my office"
        $ mc.change_location(office)
        $ mc.location.show_background()
        the_person.char "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        mc.name "Hi [the_person.title], come in and take a seat."
    else:
        the_person.char "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        "Your HR Director appears in the doorway to your office."
        the_person.char "Hey, I got a hit on criteria you had for a prospective employee. I think you are going to like this."
        if mc.business.max_employee_count == mc.business.get_employee_count():  #We accidentally filled all available slots
            mc.name "Actually, I accidentally filled that position already. Sorry, I must have forgotten to tell you."
            the_person.char "You... ahh, okay. Try to remember to let me know next okay?"
            "You promise to do so."
            return
    $ scene_manager.update_actor(the_person, position = "sitting")

    call hire_select_process([prospect, 1]) from _call_hire_prospect_process_1  #Copying how Vren calls this... hopefully this is right...

    if _return == prospect: #MC chooses to hire her
        mc.name "Alright [the_person.title], this looks promising. Good work finding her."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(5)
        the_person.char "Alright! I'll give her the news."
        $ prospect.generate_home()
        call hire_someone(prospect, add_to_location = True) from _call_hire_HR_prospect_1
        $ prospect.set_title(get_random_title(prospect))
        $ prospect.set_possessive_title(get_random_possessive_title(prospect))
        $ prospect.set_mc_title(get_random_player_title(prospect))
        the_person.char "Give me the rest of the week to catch up on my normal HR work. If you want me to start the process again, talk to me on Monday."
    else:
        mc.name "I'm sorry, this wasn't exactly what I had in mind."
        the_person.char "Ah, okay. Well give me the rest of the week to catch up on my normal HR work. If you want me to start the process again, talk to me on Monday."
    $ del prospect
    return


#Headhunter unlocks and requirements:
#Initial unlock: recruitment_batch_two_policy.is_owned()  second screening pool size increase ###
#obedience unlock: recruitment_obedience_improvement_policy.is_owned() ###
#slutty unlock: recruitment_slut_improvement_policy.is_owned() ###
#Married / unmarried unlock: recruitment_knowledge_two_policy.is_owned()  ###
#Has kids unlock: recruitment_knowledge_three_policy.is_owned()
#focused production unlock: recruitment_batch_three_policy.is_owned() ###
#Big / small tits unlock: recruitment_knowledge_four_policy.is_owned()

label HR_director_monday_headhunt_update_label(the_person):
    the_person.char "Let's see if I have any updates to the targeted recruiting program."
    if get_HR_director_tag("business_HR_headhunter_progress", 0) == 0:
        the_person.char "Looks like I'm not currently running any target searches. Let me know if you want me to initiate one."
    elif get_HR_director_tag("business_HR_headhunter_progress", 0) == 1:
        the_person.char "I'm still working on the current search. Give me a few more days to finish it up."
    else:
        the_person.char "I should have the time now to initiate another search. If you want me to start another talent search let me know!"
        $ set_HR_director_tag("business_HR_headhunter_progress", 0)

    # all updates researched (quick exit)
    if get_HR_director_tag("headhunter_kids", False) == True and get_HR_director_tag("headhunter_slut", False) == True and get_HR_director_tag("headhunter_focused", False) == True and get_HR_director_tag("headhunter_obedience", False) == True:
        return

    the_person.char "Let's see if any recent recruiting policy updates will change how we look for employees."
    if get_HR_director_tag("headhunter_obedience", False) == False and recruitment_obedience_improvement_policy.is_owned():
        the_person.char "I can now target a new employee based on their free will! I can either scout for an obedient, or free spirited prospect."
        $ set_HR_director_tag("headhunter_obedience", True)
    elif get_HR_director_tag("headhunter_focused", False) == False and recruitment_batch_three_policy.is_owned():
        the_person.char "I can now target highly specialized prospects. They will be more skilled in an area, but may not be well rounded individuals."
        $ set_HR_director_tag("headhunter_focused", True)
    elif get_HR_director_tag("headhunter_physical", False) == False and recruitment_knowledge_one_policy.is_owned():
        the_person.char "With the new software update, I can now search by a variety of physical preferences. Busty? Short? Thick? I can make it happen!"
        $ set_HR_director_tag("headhunter_physical", True)
    elif get_HR_director_tag("headhunter_marital", False) == False and recruitment_knowledge_two_policy.is_owned():
        the_person.char "I can now target married or single individuals. It might be illegal in most states, but not here!"
        $ set_HR_director_tag("headhunter_marital", True)
    elif get_HR_director_tag("headhunter_slut", False) == False and recruitment_slut_improvement_policy.is_owned():
        the_person.char "I can now narrow down prospects based on general promiscuity. Want a prude or a slut? I can do that."
        $ set_HR_director_tag("headhunter_slut", True)
    elif get_HR_director_tag("headhunter_kids", False) == False and recruitment_knowledge_three_policy.is_owned():
        the_person.char "I can now pick prospects based on whether or not they have kids. More MILFs around here? I could handle that!"
        $ set_HR_director_tag("headhunter_kids", True)
    else:
        "Looks like I don't have any additions to the prospecting system this week."
    return


init 1200 python:
    def mind_control_backfire(the_person):
        the_person.change_cha(-2)
        the_person.change_int(-2)
        the_person.change_focus(-2)
        # Use this function to create random backfire to person. Ideas: Bimbo, loss of stats, decrease all opinions.
        return "Backfire: Stat Loss"

    def reset_headhunter_criteria():
        set_HR_director_tag("recruit_dept", None)
        set_HR_director_tag("recruit_obedience", None)
        set_HR_director_tag("recruit_focused", None)
        set_HR_director_tag("recruit_marital", None)
        set_HR_director_tag("recruit_slut", None)
        set_HR_director_tag("recruit_kids", None)
        set_HR_director_tag("recruit_age", None)
        set_HR_director_tag("recruit_bust", None)
        set_HR_director_tag("recruit_height", None)
        set_HR_director_tag("recruit_body", None)
        set_HR_director_tag("recruit_day", day)
        return

    def generate_HR_recruit():
        # department boosted stats
        main_stat = renpy.random.randint(5,7)
        main_skill = renpy.random.randint(5,7)
        other_stat = 0

        min_slut = (get_HR_director_tag("recruit_slut", 0) or 0) // 10
        sex_array = [renpy.random.randint(min_slut,5), renpy.random.randint(min_slut,5), renpy.random.randint(min_slut,5), renpy.random.randint(min_slut,5)]

        # extra boost for focused recruit
        if get_HR_director_tag("recruit_focused", False) == True:
            main_stat += 2
            main_skill += 2
            other_stat = 2

        recruit = create_random_person(tits = get_HR_director_tag("recruit_bust", None),
            start_obedience = get_HR_director_tag("recruit_obedience", None),
            start_sluttiness = get_HR_director_tag("recruit_slut", None),
            relationship = get_HR_director_tag("recruit_marital", None),
            age = get_HR_director_tag("recruit_age", None),
            kids = get_HR_director_tag("recruit_kids", None),
            body_type = get_HR_director_tag("recruit_body", None),
            height = get_HR_director_tag("recruit_height", None),
            sex_array = sex_array)

        # make balanced stats
        recruit.int = renpy.random.randint(3,6)
        recruit.focus = renpy.random.randint(3,6)
        recruit.charisma = renpy.random.randint(3,6)
        recruit.production_skill = renpy.random.randint(3,6)
        recruit.hr_skill = renpy.random.randint(3,6)
        recruit.supply_skill = renpy.random.randint(3,6)
        recruit.market_skill = renpy.random.randint(3,6)
        recruit.research_skill = renpy.random.randint(3,6)

        if get_HR_director_tag("recruit_dept") == "HR":
            recruit.charisma = main_stat
            recruit.hr_skill = main_skill
            recruit.focus -= other_stat
            recruit.opinions["HR work"] = [2, True]
        elif get_HR_director_tag("recruit_dept") == "supply":
            recruit.focus = main_stat
            recruit.supply_skill = main_skill
            recruit.int -= other_stat
            recruit.opinions["supply work"] = [2, True]
        elif get_HR_director_tag("recruit_dept") == "market":
            recruit.charisma = main_stat
            recruit.market_skill = main_skill
            recruit.int -= other_stat
            recruit.opinions["marketing work"] = [2, True]
        elif get_HR_director_tag("recruit_dept") == "research":
            recruit.int = main_stat
            recruit.research_skill = main_skill
            recruit.charisma -= other_stat
            recruit.opinions["research work"] = [2, True]
        elif get_HR_director_tag("recruit_dept") == "production":
            recruit.focus = main_stat
            recruit.production_skill = main_skill
            recruit.charisma -= other_stat
            recruit.opinions["production work"] = [2, True]

        # use enhanced make person options
        update_person_opinions(recruit)
        update_random_person(recruit)
        rebuild_wardrobe(recruit)
        update_person_outfit(recruit, -0.2) # choose a less slutty outfit as planned outfit

        # discover some opinions
        for x in __builtin__.range(0, 6):
            recruit.discover_opinion(recruit.get_random_opinion(include_known = False, include_sexy = True),add_to_log = False)

        return recruit
