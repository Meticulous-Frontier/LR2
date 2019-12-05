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

#HR director action requirements#
init -2 python:
    def HR_director_initial_hire_requirement():
        if business_HR_meeting_last_day < day:
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
        if business_HR_coffee_tier == 0:
            if business_HR_serum_suggest_1 == True:
                if mc.business.funds > 500:
                    return True
                else:
                    return "Requires $500"

        return False

    def HR_director_coffee_tier_2_requirement(the_person):
        if business_HR_coffee_tier < 2:
            if business_HR_serum_suggest_2 == True:
                if mc.business.funds > 1500:
                    return True
                else:
                    return "Requires $1500"

        return False

    def HR_director_mind_control_requirement(the_person):
        if business_HR_mind_control:
            if business_HR_mind_control_attempt == False:
                if mc.business.funds > 5000:
                    return True
                else:
                    return "Requires $5000"
        return False

    def  HR_director_mind_control_attempt_requirement(the_person):
        if business_HR_mind_control_attempt:
            if business_HR_meeting_last_day < day:
                if mc.business.is_open_for_business():
                    return True
                else:
                    return "Only during work day"
            else:
                return "One meeting per day."

init 2 python:
    def build_HR_review_list(the_person, max_tier = 0):
        HR_tier_talk = -1 # init at -1 so we do the first collect with 0
        HR_employee_list = []
        # build list of girls that qualify for specified tier and max_tier score
        while len(HR_employee_list) == 0 and HR_tier_talk < business_HR_coffee_tier and HR_tier_talk < max_tier:
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
        if business_HR_uniform:
            topic_list.append("work uniforms")
        if business_HR_skimpy_uniform:
            topic_list.append("skimpy uniforms")

        return topic_list

    def update_hire_daughter_crisis(chance):
        found = find_in_list(lambda x: x[0] == daughter_work_crisis, crisis_list)
        if found:
            found[1] = chance
            #renpy.say("", "Updated daughter at work crisis chance to: " + str(chance) + "%%")
        return

init 1301 python:
    def HR_director_creation_requirement():
        return True

    HR_director_creation_policy = Policy(name = "Create HR Director Position",
        desc = "Create a new position for an HR Director. Increases maximum employee count by one.",
        cost = 500,
        requirement =  HR_director_creation_requirement,
        on_buy_function = increase_max_employee_size,
        on_buy_arguments = {"amount":1})

    def HR_director_tier_1_suggest():
        if off_label_drugs.researched:
            return True
        return False

    def HR_director_tier_2_suggest():
        if blood_brain_pen.researched:
            return True
        return False

    def HR_director_mind_control_suggest():
        if mind_control_agent.researched:
            return True
        return False

    def HR_director_change_relative_recruitment_requirement(the_person):
        if business_HR_relative_recruitment_unlock:
            if mc.business.is_open_for_business():
                return True
            else:
                return "Only on during work day"
        return False

    def HR_director_meeting_on_demand_requirement(the_person):
        if business_HR_meeting_on_demand:
            if business_HR_meeting_last_day < day:
                if mc.business.is_open_for_business():
                    return True
                else:
                    return "Only on during work day"
            else:
                return "One meeting per day."
        return False



    def HR_director_breast():
        if breast_enhancement.researched:
            return True
        return False

### HR Director Mod init ###
label HR_director_mod_init():
    python:
        #TODO move all these true flase flags to a dict so that in the future when I add more, I can call them by reference and not invalidate old saves games!
        business_HR_director = None
        business_HR_tier = 0     # HR tiers based on progression. 1 = hired someone. 2 = training videos. 3 = company sponsored sexual training.
        business_HR_eff_bonus = mc.business.effectiveness_cap - 100  #This bonus is based on OTHER factors and can be added to via events.
        business_HR_serum_suggest_1 = False
        business_HR_serum_suggest_2 = False
        business_HR_mind_control = False
        business_HR_mind_control_attempt = False
        business_HR_serum_breast = False
        business_HR_coffee_tier = 0
        business_HR_skimpy_uniform = False
        business_HR_uniform = False
        business_HR_sexy_meeting_start = False
        business_HR_sexy_start_unlocks = {}
        business_HR_relative_recruitment_status = False
        business_HR_relative_recruitment_unlock = False
        business_HR_meeting_on_demand = False
        business_HR_meeting_last_day = 0

        Sarah_mod_initialization() #TODO this is for testing. Should probably figure out a better way to do this...

        HR_director_coffee_tier_1_action = Action("Add serum to coffee during meetings.", HR_director_coffee_tier_1_requirement, "HR_director_coffee_tier_1_label",
            menu_tooltip = "Costs $500 but makes meetings more impactful.")
        HR_director_coffee_tier_2_action = Action("Add stronger serum to coffee during meetings.", HR_director_coffee_tier_2_requirement, "HR_director_coffee_tier_2_label",
            menu_tooltip = "Costs $1500 but makes meetings impactful.")
        HR_director_mind_control_action = Action("Produce mind control Serum.", HR_director_mind_control_requirement, "HR_director_mind_control_label",
            menu_tooltip = "Costs $5000. Allows you to attempt mind control of employee.")
        HR_director_mind_control_attempt = Action("Attempt Mind Control.", HR_director_mind_control_attempt_requirement, "HR_director_mind_control_attempt_label",
            menu_tooltip = "WARNING: May have side effects!")
        HR_director_change_relative_recruitment_action = Action("Change recruitment signage", HR_director_change_relative_recruitment_requirement, "HR_director_change_relative_recruitment_label",
            menu_tooltip = "Changes how often employees ask for employment for their daughters")
        HR_director_meeting_on_demand_action = Action("Meet with employee{image=gui/heart/Time_Advance.png}", HR_director_meeting_on_demand_requirement, "HR_director_meeting_on_demand_label",
            menu_tooltip = "Arrange a meeting with an employee")
        HR_director_role = Role("HR Director", [HR_director_meeting_on_demand_action, HR_director_coffee_tier_1_action, HR_director_coffee_tier_2_action, HR_director_mind_control_action, HR_director_change_relative_recruitment_action, HR_director_change_relative_recruitment_action]) #Actions go in block
    return


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
    #TODO remove monday meeting mandatory event
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

        if the_person is sarah:
            #TODO try to detect if employee count is full again
            the_person.set_schedule([1,2,3], None) # remove previous schedule
            the_person.event_triggers_dict["employed_since"] = day
            mc.business.listener_system.fire_event("new_hire", the_person = the_person)
            the_person.special_role.append(employee_role)
            the_person.special_role.append(HR_director_role)
            mc.business.add_employee_hr(the_person)
            the_person.set_work([1,2,3], mc.business.h_div)
            business_HR_director = the_person
        else:
            mc.business.remove_employee(the_person)
            the_person.special_role.append(employee_role)
            the_person.special_role.append(HR_director_role)
            mc.business.add_employee_hr(the_person)
            the_person.set_work([1,2,3], mc.business.h_div)
            business_HR_director = the_person

    $ HR_director_first_monday = Action("First Monday",HR_director_first_monday_requirement,"HR_director_first_monday_label", args = the_person) #Set the trigger day for the next monday. Monday is day%7 == 0
    $ mc.business.mandatory_crises_list.append(HR_director_first_monday) #Add the event here so that it pops when the requirements are met.
    return

label HR_director_first_monday_label(the_person):
    "It's lunchtime, so you prepare to have your first meeting with your new HR Direction, [the_person.title]."
    "You grab your lunch from the break head to your office and sit down."
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
    $ HR_director_monday_meeting = Action("Monday HR Lunch",HR_director_monday_meeting_requirement,"HR_director_monday_meeting_label", args = the_person) #Set the trigger day for the next monday. Monday is day%7 == 0
    $ mc.business.mandatory_crises_list.append(HR_director_monday_meeting) #Add the event here so that it pops when the requirements are met.
    $ business_HR_tier = 1
    if the_person is sarah:
        $ Sarah_third_wheel_action = Action("Sarah's third wheel event",Sarah_third_wheel_requirement,"Sarah_third_wheel_label")
        $ mc.business.mandatory_crises_list.append(Sarah_third_wheel_action)
    return

label HR_director_monday_meeting_label(the_person):
    if mc.location != office:
        "You hurry to your office for your weekly meeting with your HR director [the_person.title]."
        $ mc.change_location(office)
        $ mc.location.show_background()
        "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        mc.name "Hi [the_person.title], come in and take a seat."
    else:
        "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        "Your HR Director appears in the doorway to your office. It is time for your weekly HR meeting."
        "She sits down across from you and starts to eat her lunch."

    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.sluttiness > 40 and business_HR_sexy_meeting_start == False:
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
        $ business_HR_sexy_meeting_start = True
        the_person.char "So... can we start today?"
        menu:
            "Let's go":
                call HR_diector_sexy_meeting_start_label(the_person) from sexy_meeting_start_one
                $ scene_manager.update_actor(the_person, position = "sitting")
                "Feeling good, [the_person.title] returns to her seat and starts to pull out her notes."
            "Not Today":
                the_person.char "Ahh, okay. I know this was short notice, but you can plan on it next week, okay?"
                "She reaches down to her backpack and begins to pull out her notes from the previous week."
    elif business_HR_sexy_meeting_start:
        "She looks at you intently."
        the_person.char "So, need some relief before we get started today?"
        menu:
            "Let's go":
                call HR_diector_sexy_meeting_start_label(the_person) from sexy_meeting_start_two
                $ scene_manager.update_actor(the_person, position = "sitting")
                "Feeling good, [the_person.title] returns to her seat and starts to pull out her notes."
            "Not Today":
                the_person.char "Ahh, damn. Okay, give me a second and we can get started here."
                "She reaches down to her backpack and begins to pull out her notes from the previous week."
    the_person.char "Here are my plans for the week. I think I have a few tweaks to efficiency I can make, but overall I wouldn't expect to see a big change company wide."
    call HR_director_calculate_eff(the_person) from HR_director_monday_meeting_1
    "She hands you a few documents. You check them over."
    mc.name "Looks good. Go ahead and continue with those plans."

    $ (HR_employee_list, HR_tier_talk) = build_HR_review_list(the_person, business_HR_coffee_tier)
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
                call HR_director_personnel_interview_label(the_person, max_opinion = business_HR_coffee_tier) from HR_DIR_INTERVIEW_CALL_2

    the_person.char "Ok, next up, I wanted to review progress made on serums and policy changes from the past week to see if anything might be useful."
    call HR_director_review_discoveries_label(the_person) from HR_DIR_INTERVIEW_CALL_3
    mc.name "Alright, I think that is all for today. Unless something comes up, same time next week?"
    $ the_person.draw_person(position = "stand2")
    the_person.char "Sounds great! I'll see you then!"

    $ HR_director_monday_meeting = Action("Monday HR Lunch",HR_director_monday_meeting_requirement,"HR_director_monday_meeting_label", args = the_person) #Set the trigger day for the next monday. Monday is day%7 == 0
    $ mc.business.mandatory_crises_list.append(HR_director_monday_meeting) #Add the event here so that it pops when the requirements are met.
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

    the_person.char "Alright, let me go get her."
    $ renpy.scene("Active")

    "[person_choice.title] steps in to the office after a few minutes, followed by [the_person.title]."
    person_choice.char "Hello [person_choice.mc_title]."

    # initialize
    $ scene_manager = Scene()
    $ scene_manager.add_actor(person_choice, position = "stand3", character_placement = character_left_flipped)
    mc.name "Hello [person_choice.title], come in and take a seat."

    $ scene_manager.update_actor(person_choice, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "stand4")

    if business_HR_coffee_tier > 0:
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
        mc.name "I know that it feels weird, being asked to come in to work wearing clothes that show a lot of skin, but in the market we are in, dressing to impress can be a key business advantage."
    else:
        mc.name "I know the policy in place feels weird, but I want you to rethink your opinion on [opinion_chat]. It would be helpful if you would "
    the_person.char "All of our employees are valued here, not just as employees, but as people."
    person_choice.char "Thanks... I guess... I've never really thought about it like that."
    if person_choice.obedience > 120: #She is obedient
        person_choice.char "I'm not sure I really thought about things here as more than just another job... but I want this place to succeed. I want you to succeed, [person_choice.mc_title]."
    else:
        person_choice.char "I guess I never really though about it like that. I mean, if I have to have a job... I guess I might as well try to be more positive about it, right?"
    "She stops for a moment and gathers her thoughts."
    person_choice.char "I'll think about this for a bit, but I think I understand what you are saying. I'll try to have a better attitude about things going forward."
    $ scene_manager.update_actor(person_choice, position = "sitting", character_placement = character_left_flipped, emotion = "happy")
    "[person_choice.title] thinks for a moment, then smiles at both of you."
    person_choice.char "Thanks for calling me in... I guess I'd better go get back to work!"
    if opinion_chat in opinions_list:
        $ person_choice.opinions[opinion_chat] = [max_opinion, True]
    else:
        $ person_choice.sexy_opinions[opinion_chat] = [max_opinion, True]
    $ scene_manager.update_actor(person_choice, position = "walking_away", character_placement = character_left_flipped)
    $ scene_manager.update_actor(the_person, position = "stand2")
    "[the_person.title] gets up and walks [person_choice.title] to the door."
    "They exchange a few pleasantries before [person_choice.title] leaves the room."
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
    if business_HR_serum_suggest_1 == False:
        if off_label_drugs.researched: #Researched!
             $ business_HR_serum_suggest_1 = True
             the_person.char "Hmmm... interesting."
             "[the_person.title] looks closely at one of the serums that has been researched."
             the_person.char "I see here that you've managed to create a serum that has the ability to increase a person's... suggestibility?"
             mc.name "Right. Basically it sets up the brain to make new connections it might not have previously made, opening up a person to suggestions they may not normally consider."
             the_person.char "That would actually be useful... We could use some, in the coffee we make when we bring them in for meetings?"
             mc.name "A version of the serum with a short useful life would be useful for giving the meetings more impact."
             "[the_person.title] looks into more details of the serum."
             the_person.char "Looks like the serum is fairly easy to produce. I'd say fo about $500 we could probably setup an something long term for the monday meetings..."
             mc.name "Noted. I'll consider it and get back to you if I decide to do this."
             the_person.char "Sounds good [the_person.mc_title]!"

    elif business_HR_serum_suggest_2 == False:
        if blood_brain_pen.researched: #Researched!
            $ business_HR_serum_suggest_2 = True
            the_person.char "Hmmm... interesting."
            "[the_person.title] looks closely at one of the serums that has been researched."
            the_person.char "I see here that you've managed to improve on an earlier design to increase a person's suggestibility!"
            mc.name "Right. It bypasses connections that would normally trigger a rejection response and causes the person to consider actions that would normally be rejected."
            if business_HR_coffee_tier == 0:
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

    elif business_HR_mind_control == False:
        if mind_control_agent.researched: #Researched
            $ business_HR_mind_control = True
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
        if business_HR_serum_breast == False:
            if breast_enhancement.researched: #Researched!
                $ business_HR_serum_breast = True
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
                $ Sarah_catch_stealing_action = Action("Catch Sarah Stealing",Sarah_catch_stealing_requirement,"Sarah_catch_stealing_label") #Set the trigger day for the next monday. Monday is day%7 == 0
                $ mc.business.mandatory_crises_list.append(Sarah_catch_stealing_action) #Insert the event to the top of the list
    "You spend a few minutes with [the_person.title] going over the progress in the research department over the last week or so."
    the_person.char "That's it for research, let's take a look at policy changes from the last week."
    if business_HR_uniform == False:
        if relaxed_uniform_policy.is_owned():
            the_person.char "Hmmm, I see here that we have recently opened up company policy to allow for uniform guidelines."
            the_person.char "This is something that could potentially alienate some of our employees. It might be a good idea if we include opinions on work uniforms when meeting one on one with them."
            "You hadn't considered how your employees would react when you instituted the uniform policy. You decide [the_person.possessive_title] is right."
            mc.name "That's a good idea. Go ahead and implement that going forward."
            the_person.char "Sure thing [the_person.mc_title]!"
            $ business_HR_uniform = True
    elif business_HR_skimpy_uniform == False:
        if corporate_enforced_nudity_policy.is_owned():
            if the_person.sluttiness > 40:  #She only volunteers to start doing this if she is slutty enough.
                the_person.char "I see here that the uniform policy has recently been loosened further."
                the_person.char "Personally, I think it is great that I can come to work and show off lots of skin, but with the latest change in uniform policy, it might be intimidating to employees who don't like skimpy uniforms."
                the_person.char "It might be a good to idea to include opinions on skimpy uniforms when meeting one on one with employees."
                "You realize the swing in the uniform policy might be a bit much for some girls, so this is probably a good thing to start counseling for."
                mc.name "That's a good idea. Go ahead and implement that going forward."
                the_person.char "Sure thing [the_person.mc_title]!"
                $ business_HR_skimpy_uniform = True
                if the_person is sarah:
                    the_person.char "Mmm, I can't wait to see what some of the outfits other girls wear around the office..."
                    $ the_person.change_slut_temp(5)
    if business_HR_relative_recruitment_unlock == False:
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
                    $ business_HR_relative_recruitment_status = True
                "Deny":
                    mc.name "I think for now I'd like to stick with more traditional recruiting methods."
                    $ business_HR_relative_recruitment_status = False

            "Sure thing [the_person.mc_title]. If you change your mind in the future, just let me know. I can always put the sign up or down based on what we need at the time."
            $ business_HR_relative_recruitment_unlock = True

    if business_HR_meeting_on_demand == False:
        if mc.business.get_employee_count() > 10:
            the_person.char "I see the business has grown. We now have a double digit number of employees!"
            the_person.char "I was thinking, with the number of employees we have now, we could probably do our one on one meetings more often without losing their effectiveness."
            the_person.char "We still don't want to do it too often, but I was thinking we could have meetings as often as once a day?"
            "With your growing number of employees, it makes sense that you would be able to have meetings more often."
            mc.name "I'll keep that in mind going forward. If I want to have a meeting with an employee, I'll make sure to come find you first."
            the_person.char "Great! I think that will work out nicely."
            $ business_HR_meeting_on_demand = True
    return

label HR_director_coffee_tier_1_label(the_person):
    $ mc.business.funds -= 500
    mc.name "I've been thinking about your proposal to add serums to the coffee we serve to employees when we meet with them. I'm giving you approval to set it up."
    the_person.char "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person.char "I'll keep it in a locked cabinet and from now on I'll only use it when we give an employee coffee during our monday meetings."
    mc.name "Sounds good."
    the_person.char "Did you need anything else, [the_person.mc_title]?"
    $ business_HR_coffee_tier = 1
    return

label HR_director_coffee_tier_2_label(the_person):
    $ mc.business.funds -= 1500
    mc.name "I've been thinking about your proposal to add the stronger serum to the coffee we serve to employees when we meet with them. I'm giving you approval to set it up."
    the_person.char "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person.char "I'll keep it in a locked cabinet and from now on I'll only use it when we give an employee coffee during our monday meetings."
    mc.name "Sounds good."
    the_person.char "Did you need anything else, [the_person.mc_title]?"
    $ business_HR_coffee_tier = 2
    return

label HR_director_calculate_eff(the_person):
    $ HR_dir_factor = 0
    if not get_HR_director() is None:
        $ HR_dir_factor = ((the_person.charisma * 2 ) + the_person.hr_skill)   #Charisma + HR skill
        #TODO make events later on that factor this to be better
    $ HR_dir_factor += business_HR_eff_bonus
    $ mc.business.effectiveness_cap = (100 + HR_dir_factor)   #100% base effectiveness
    return

label HR_director_change_relative_recruitment_label(the_person):
    if business_HR_relative_recruitment_status:
        the_person.char "I see, are you sure you want me to take down the sign in the break room that we are looking for more employees?"
        menu:
            "Take the Sign Down":
                the_person.char "Ok, I'll take it down as soon as we are finished here. Is there anything else I can do for you?"
                $ update_hire_daughter_crisis(2)
                $ business_HR_relative_recruitment_status = False
            "Leave the Sign Up":
                the_person.char "Oh... sorry I thought you said you wanted to change it. Is there anything else I can do for you?"
        return
    else:
        the_person.char "I see, are you sure you want me to put the sign in the break room that we are looking for more employees?"
        menu:
            "Put the Sign Up":
                the_person.char "Ok, I'll put it up as soon as we are finished here. Is there anything else I can do for you?"
                $ update_hire_daughter_crisis(10)
                $ business_HR_relative_recruitment_status = True
            "Leave the Sign Down":
                the_person.char "Oh... sorry I thought you said you wanted to change it. Is there anything else I can do for you?"
        return

label HR_director_meeting_on_demand_label(the_person):
    the_person.char "Okay, I think I have time for that! Let me grab my dossiers from Monday and I'll meet you in your office."
    "You head to your office and [the_person.possessive_title] quickly arrives with her papers."
    $ the_person.draw_person(position = "sitting")
    the_person.char "Ok! Let me see who I have on my list here..."
    call HR_director_personnel_interview_label(the_person, max_opinion = business_HR_coffee_tier) from HR_DIR_INTERVIEW_CALL_4
    the_person.char "I'd say that went pretty well! I'm going to head back to work, if that is okay with you, [the_person.mc_title]?"
    "You thank her for her help and excuse her. She gets up and leaves you to get back to work."
    $ renpy.scene("Active")
    $ business_HR_meeting_last_day = day
    call advance_time from hr_advance_time_one
    return

label HR_diector_sexy_meeting_start_label(the_person):
    #Phases of this label.
    #   First we determine if we have any new acts of service our girl is willing to perform.
    #   If not, give the player the option to choice an unlocked act of service
    #   Next, perform the act
    #   Then, clean up, with higher sluttiness giving the player the option to have her not clean up.

    if len(business_HR_sexy_start_unlocks) == 0:  #This is the first time this function has been run
        the_person.char "So... I have no idea the best way to do this..."
        mc.name "Why don't you just come over here and give me a blowjob."
        the_person.char "Okay! That should be fun!"
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "[the_person.possessive_title] comes around to your side of the desk and gets down on her knees. She pulls down your zipper and pulls your cock out."
        the_person.char "Mmm, it smells so good. Let's get this taken care of!"
        "She runs her tongue up and down your length a few times, then parts her lips and begins to suck you off."
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True) from _call_sex_description_meeting_start_one
        mc.name "Mmm, this is a great way to start Monday. This was a great idea [the_person.title]."
        $ scene_manager.update_actor(the_person, emotion = "happy")
        "[the_person.possessive_title] stops licking the cum off her lips for a second and smiles."
        the_person.char "Thank you sir! I am willing to do this next week again if you decide to."
        $ business_HR_sexy_start_unlocks["blowjob"] = True
        "She cleans herself up and makes herself presentable again."

        #TODO code for her to clean herself up
        return

    if business_HR_sexy_start_unlocks.get("titfuck", False) == False:
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
            $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
            "She gets up and starts walking around the desk. By the time she gets to you, you already have your rock hard dick out."
            "She gets on her knees and gives you a couple strokes with her hand."
            the_person.char "Mmmm, I love the feeling of a cock buried between by big tits... this is gonna be great!"
            "With her hands on each side of her chest, she wraps her sizable boobs around you and begins to bounce them up and down."
            call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = True) from _call_sex_description_meeting_start_two
            $ business_HR_sexy_start_unlocks["titfuck"] = True
            "After you finish, [the_person.possessive_title] runs her hands along her tits, rubbing your cum into her skin."
            the_person.char "Mmm, god that was hot. Let me just enjoy this a minute before we move on with the meeting..."
            "You run your hands through her hair for a bit while she enjoys the warmth of your cum on her skin."
            "Eventually she cleans herself up and makes herself presentable again."
            return

    the_person.char "Okay! How do you want me to take care of you this week, [the_person.mc_title]?"

    python:
        tuple_list = []
        for position in business_HR_sexy_start_unlocks.keys():
            if business_HR_sexy_start_unlocks[position] == True:
                tuple_list.append([position, position])
        tuple_list.append(["Surprise me", "any"])

        position_choice = renpy.display_menu(tuple_list,True,"Choice")

    if position_choice == "any":
        the_person.char "Mmmm, I can do that! "
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(-5)
        $ position = get_random_from_list(business_HR_sexy_start_unlocks.keys())

    if position_choice == "blowjob":
        the_person.char "Get your cock out, I want to taste it!"
        "[the_person.possessive_title] stands up and starts to walk around the desk while you pull out your erection."
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "She gets down on her knees in front of you and takes a moment to admire your hardness."
        "She opens her mouth and runs her tongue along it a few times, and then parts her lips and begins to suck you off."
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True) from _call_sex_description_meeting_mid_one

    elif position_choice == "titfuck":
        if the_person.outfit.tits_available() == False:
            "[the_person.possessive_title] begins to take off her top. "
            $ scene_manager.strip_actor_outfit(the_person, exclude_lower = True)
            "With her tits out and ready to be used, she gives you a big smile."
        the_person.char "Get your cock out, I want to feel it slide between my boobs!"
        "You pull your cock out as she gets up and walks around your desk. She drops down on her knees in front of you."
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "[the_person.possessive_title] smiles at you as she uses her hands to wrap her tits around your cock, and then starts to move them up and down."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = True) from _call_sex_description_meeting_mid_two

    return

label HR_director_mind_control_label(the_person):
    $ mc.business.funds -= 5000
    mc.name "I've been thinking about your proposal to create a specialized serum for mind control attempts. I would like to move forward with it."
    the_person.char "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person.char "I'll make sure it stay locked away, and only you and I will have a key to get some out."
    mc.name "Sounds good."
    the_person.char "Did you need anything else, [the_person.mc_title]?"
    $ business_HR_mind_control_attempt = True
    return

label HR_director_mind_control_attempt_label(the_person):
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

    the_person.char "Okay. I'll go get them."
    $ renpy.scene("Active")
    call HR_mind_control_attempt(person_choice, the_person) from HR_mind_control_attempt_call_1

    $ renpy.scene("Active")
    $ business_HR_meeting_last_day = day
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
                        $ mc.business.funds -= 1000
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

init 1200 python:
    def mind_control_backfire(the_person):
        the_person.change_cha(-2)
        the_person.change_int(-2)
        the_person.change_focus(-2)
        # Use this function to create random backfire to person. Ideas: Bimbo, loss of stats, decrease all opinions.
        return "Backfire: Stat Loss"
