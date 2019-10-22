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
        if time_of_day == 1:
            return True
        return False

    def HR_director_first_monday_requirement():
        if time_of_day == 1:
            if day%7 == 0:  #Monday
                return True
        return False

    def HR_director_monday_meeting_requirement():
        if get_HR_director() == None:
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

init 1301 python:
    def HR_director_creation_requirement():
        return True

    HR_director_creation_policy = Policy(name = "Create HR Director Position",
        desc = "Create a new position for an HR Director. Inccreases maximum employee count by one.",
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

    def HR_director_breast():
        if breast_enhancement.researched:
            return True
        return False

### HR Director Mod init ###
label HR_director_mod_init():
    python:
        business_HR_director = None
        business_HR_tier = 0     # HR tiers based on progression. 1 = hired someone. 2 = training videos. 3 = company sponsored sexual training.
        business_HR_eff_bonus = mc.business.effectiveness_cap - 100  #This bonus is based on OTHER factors and can be added to via events.
        business_HR_serum_suggest_1 = False
        business_HR_serum_suggest_2 = False
        business_HR_serum_breast = False
        business_HR_coffee_tier = 0


        Sarah_mod_initialization() #TODO this is for testing. Should probably figure out a better way to do this...

        HR_director_coffee_tier_1_action = Action("Add serum to coffee during meetings.", HR_director_coffee_tier_1_requirement, "HR_director_coffee_tier_1_label",
            menu_tooltip = "Costs $500 but makes meetings more impactful.")
        HR_director_coffee_tier_2_action = Action("Add stronger serum to coffee during meetings.", HR_director_coffee_tier_2_requirement, "HR_director_coffee_tier_2_label",
            menu_tooltip = "Costs $1500 but makes meetings impactful.")
        HR_director_role = Role("HR Director", [HR_director_coffee_tier_1_action, HR_director_coffee_tier_2_action]) #Actions go in block
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
    if the_person == sarah:
        "Since she is new to the company in general, you give [the_person.title] a tour of the company first."
        the_person.char "So... what kind of pharmaceuticals are being researched, exactly?"
        "You decide to just be honest. If she is going to be working here at the company, she is going to figure it out sooner or later anyway."
        mc.name "Well, most of our research right now is targetted toward making people's lives better."
        mc.name "We came across a formula not long ago with almost no known side effects, that with tweeks to the final formula can be used for a number of different things, from increasing happiness to increasing charisma, to making sex better."
        the_person.char "Wow, that sounds very versatile!"
        "After the tour you head back to your office."

    else:
        "You head to your office with her."
    the_person.char "Well, I am excited to have this opportuniy. To be honest I'm not really even sure where to begin!"
    mc.name "I'll tell you what, for the rest of this week, why don't you just work alongside the others in the HR department. I'll send over to you my personal dossiers on all the employees, and as you have time you can look over them."
    the_person.char "Okay, I can do that. I'll look over them over the weekend as well. Do you want to plan on having a meeting sometime next week?"
    mc.name "That sounds good. How about we do lunch on Monday? Since you are going to heading up the department, having a meeting every week might be a good idea."
    $ the_person.draw_person(emotion = "happy")
    the_person.char "Great! I'll look forward to it. I'll try to have a plan ready for the meeting on Monday on what we can accomplish."
    "You say goodbye to [the_person.title]."
    if the_person == sarah:
        python:
            #TODO try to detect if employee count is full again
            the_person.schedule[1] = None # remove previous schedule
            the_person.schedule[2] = None
            the_person.schedule[3] = None
            the_person.event_triggers_dict["employed_since"] = day
            mc.business.listener_system.fire_event("new_hire", the_person = the_person)
            the_person.special_role.append(employee_role)
            the_person.special_role.append(HR_director_role)
            mc.business.add_employee_hr(the_person)
            the_person.set_work([1,2,3], mc.business.h_div)
            business_HR_director = the_person
    else:
        python:
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
    #TODO move MC to office if required
    "It's lunchtime, so you prepare to have your first meeting with your new HR Direction, [the_person.title]."
    "You grab your lunch from the break head to your office and sit down."
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
    if the_person == sarah:
        $ Sarah_third_wheel_action = Action("Sarah's third wheel event",Sarah_third_wheel_requirement,"Sarah_third_wheel_label")
        $ mc.business.mandatory_crises_list.append(Sarah_third_wheel_action)
    return

label HR_director_monday_meeting_label(the_person):
    "Hello [the_person.mc_title]!"
    $ the_person.draw_person()
    "Your HR Director appears in the doorway to your office. It is time for your weekly HR meeting."
    "She sits down across from you and starts to eat her lunch."
    $ the_person.draw_person(position = "sitting")
    the_person.char "Here are my plans for the week. I think I have a few tweeks to efficiency I can make, but overall I wouldn't expect to see a big change company wide."
    call HR_director_calculate_eff(the_person) from HR_director_monday_meeting_1
    "She hands you a few documents. You check them over."
    mc.name "Looks good. Go ahead and continue with those plans."
    the_person.char "Can do! Did you want to call in a girl for a counseling session this week?"
    menu:
        "Let's not this week":
            pass
        "Call one in":
            mc.name "Yes I want to do that."
            the_person.char "Ok! Let me see who I have on my list here..."
            call HR_director_personnel_interview_label(the_person, max_opinion = business_HR_coffee_tier) from HR_DIR_INTERVIEW_CALL_2
    the_person.char "Ok, next up, I wanted to review progress made on serums the past week to see if anything new discoveries might be useful."
    call HR_director_review_discoveries_label(the_person) from HR_DIR_INTERVIEW_CALL_3
    mc.name "Alright, I think that is all for today. Unless something comes up, same time next week?"
    $ the_person.draw_person(position = "stand2")
    the_person.char "Sounds great! I'll see you then!"

    $ HR_director_monday_meeting = Action("Monday HR Lunch",HR_director_monday_meeting_requirement,"HR_director_monday_meeting_label", args = the_person) #Set the trigger day for the next monday. Monday is day%7 == 0
    $ mc.business.mandatory_crises_list.append(HR_director_monday_meeting) #Add the event here so that it pops when the requirements are met.
    return

label HR_director_personnel_interview_label(the_person, max_opinion = 0):
    $ HR_employee_list = []
    python:
        for person in mc.business.get_employee_list():
            if person == the_person:  #This employee is the HR director, don't do anything with them.
                pass
            elif person.get_opinion_score("working") < max_opinion:
                HR_employee_list.append([(person.title + ' opinion: working'), person])
            elif person in mc.business.production_team:
                if person.get_opinion_score("production work") < max_opinion:
                    HR_employee_list.append([(person.title + ' opinion: production'), person])
            elif person in mc.business.research_team:
                if person.get_opinion_score("research work") < max_opinion:
                    HR_employee_list.append([(person.title + ' opinion: research'), person])
            elif person in mc.business.hr_team:
                if person.get_opinion_score("HR work") < max_opinion:
                    HR_employee_list.append([(person.title + ' opinion: HR'), person])
            elif person in mc.business.market_team:
                if person.get_opinion_score("marketing work") < max_opinion:
                    HR_employee_list.append([(person.title + ' opinion: marketing'), person])
            elif person in mc.business.supply_team:
                if person.get_opinion_score("supply work") < max_opinion:
                    HR_employee_list.append([(person.title + ' opinion: supply'), person])
            elif person.happiness < 85:  #Some arbitrary number
                HR_employee_list.append([person, (person.title + ' opinion: unhappy')])
            #TODO add other reasons, EG, work uniforms, showing ass, etc as business evolves

    if len(HR_employee_list) == 0: #No one qualifies!
        the_person.char "Actually, thing are running really smoothly right now, I didn't come across any dossiers this past weekend that drew my attention!"
        #TODO add another option here? Offer to bring in any girl?
        return
    the_person.char "Alright, here's my list. Who do you want me to call in?"
    python:
        choice = None
        choice = menu(HR_employee_list)
    the_person.char "Alright, let me go get her."
    #TODO scene manager, draw the girls.
    "[choice.title] steps in to the office in a minute, follow by [the_person.title]."
    choice.char "Hello [choice.mc_title]."
    #TODO they both sit down.
    "[choice.title] sits down across from you at your desk. [the_person.title] takes the lead makes a cup of coffee for her before she sits down."
    the_person.char "Thanks for coming. [the_person.mc_title] just wanted to have quick chat. Here, have a cup of coffee."
    "[choice.title] takes the coffe and nods. She takes a few sips as you begin."
    mc.name "That's right. As you know, we run a small business here, and I like to make sure all my employees enjoy their work here."
    mc.name "Recently, I've become concerned you may not like the work environment."
    $ opinion_chat = None
    menu:
        "Talk about working" if choice.get_opinion_score("working") < max_opinion:
            $ opinion_chat = "working"
            mc.name "I know that a job is just a job, but I think if you take the time to get to know your fellow employees and come in each day with a good attitude, you could learn to like coming to work every day."
        "Talk about HR work" if choice.get_opinion_score("HR work") < max_opinion:
            $ opinion_chat = "HR work"
            mc.name "I know that working with people all day long can be exhausting, but think about how much you can impact your fellow employees if you greet them with a smile every day."
        "Talk about production work" if choice.get_opinion_score("production work") < max_opinion:
            $ opinion_chat = "production work"
            mc.name "I know that production work is boring and tedious, but it is your hard work down in the production lab that keeps this business moving forward."
        "Talk about research work" if choice.get_opinion_score("research work") < max_opinion:
            $ opinion_chat = "research work"
            mc.name "I know that sometimes research work feels thankless, but I want you to know right now, I am so thankful for all the hard work you put into the department."
        "Talk about marketing work" if choice.get_opinion_score("marketing work") < max_opinion:
            $ opinion_chat = "marketing work"
            mc.name "I know that marketing work is difficult. For every sale theres dozens of rejections. But I want you know that without your hard work, it doesn't matter how good our product is if no one knows it's being made."
        "Talk about supply work" if choice.get_opinion_score("supply work") < max_opinion:
            $ opinion_chat = "supply work"
            mc.name "I know that sourcing chemicals and trying to keep costs down is thankless work, but I want you to know, as the owner of the company, I appreciate your hard work and dedication to doing what needs to be done."
        "Ask if something is bothering her" if choice.happiness < 85:
            mc.name "Lately, I've noticed that you aren't smiling anymore when you come in to work. Is there something that I can help you with? Or something about work that is bothering you?"
            #TODO possibly grab a few random opinions and see if any are applicable?
    the_person.char "All of our employees are valued here, not just as employees, but as people."
    choice.char "Thanks... I guess... I've never really thought about it like that."
    if choice.obedience > 120: #She is obedient
        choice.char "I'm not sure I really thought about things here as more than just another job... but I want this place to succeed. I want you to succeed, [choice.mc_title]."
    else:
        choice.char "I guess I never really though about it like that. I mean, if I have to have a job... I guess I might as well try to be more positive about it, right?"
    "She stops for a moment and gathers her thoughts."
    choice.char "I'll think abou this for a bit, but I think I understand what you are saying. I'll try to have a better attitude about things going forward."
    #draw girl with smiles
    "[choice.title] thinks for a moment, then smiles at both of you."
    choice.char "Thanks for calling me in... I guess I'd better go get back to work!"
    $ choice.opinions[opinion_chat] = [max_opinion, True]
    "[the_person.title] gets up and walks [choice.title] to the door."
    #TODO finish scene
    #TODO scene manager unload scene
    return

label HR_director_review_discoveries_label(the_person):
    "[the_person.title] pulls out a report on all the latest achievements of the research department."
    if business_HR_serum_suggest_1 == False:
        if off_label_drugs.researched: #Researched!
             $ business_HR_serum_suggest_1 = True
             the_person.char "Hmmm... interesing."
             "[the_person.title] looks closely at one of the serums that has been researched."
             the_person.char "I see here that you've managed to create a serum that has the ability to increase a person's... suggestability?"
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
            the_person.char "Hmmm... interesing."
            "[the_person.title] looks closely at one of the serums that has been researched."
            the_person.char "I see here that you've managed to improve on an earlier design to increase a person's suggestability!"
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

    if the_person == sarah:
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
                $ mc.business.mandatory_crises_list.append(Sarah_catch_stealing_action) #Add the event here so that it pops when the requirements are met.
    "You spend a few minutes with [the_person.title] going over the progress in the research department over the last week or so."
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
    if get_HR_director() != "None":
        $ HR_dir_factor = ((the_person.charisma * 2 ) + the_person.hr_skill)   #Charisma + HR skill
        #TODO make events later on that factor this to be better
    $ HR_dir_factor += business_HR_eff_bonus
    $ mc.business.effectiveness_cap = (100 + HR_dir_factor)   #100% base effectiveness
