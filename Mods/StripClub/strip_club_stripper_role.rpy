## Stripclub storyline Mod by Corrado
#  Strippers role definition.
#  The role is appended to strippers after they start to work for you.

init 5 python:
    add_label_hijack("normal_start", "update_strip_club_show_requirement")
    add_label_hijack("after_load", "update_strip_club_show_requirement")

    # override default strip_club show requirement
    def strip_club_show_requirement_enhanced():
        # check available strippers in club (not possible strippers)
        if __builtin__.len([x for x in stripclub_strippers if x in mc.location.people]) == 0:
            return False
        if time_of_day in [0,1,2]:
            return "Too early for performances"
        else:
            return True

    def set_stripper_schedule(person, work_location):
        # slightly altered schedule for these characters, so it does not interfere with the story-line or work schedule.
        if person.is_employee() or person in [nora, emily, christina]:
            person.event_triggers_dict["strip_club_shifts"] = 1
            person.set_schedule(work_location, times = [4])
        elif person in [lily, mom, aunt]:
            person.event_triggers_dict["strip_club_shifts"] = 1
            person.set_schedule(work_location, days = [0, 1, 3, 4, 5, 6], times =[4]) # Mom, Sis & Aunt on Wednesday play cards.
        else:
            person.event_triggers_dict["strip_club_shifts"] = 2
            person.set_schedule(work_location, times = [3, 4])
        return

    # replace requirement on action to prevent CPickle errors
    def strip_club_hire_stripper(person, role):
        person.add_role(role)

        work_location = strip_club
        if person.has_role(bdsm_performer_role):
            work_location = bdsm_room

        set_stripper_schedule(person, work_location)
        person.event_triggers_dict["stripclub_hire_day"] = day
        person.stripper_salary = calculate_stripper_salary(person)

        if role is stripper_role and not person in stripclub_strippers:
            stripclub_strippers.append(person)
        if role is bdsm_performer_role and not person in stripclub_bdsm_performers:
            stripclub_bdsm_performers.append(person)
        if role is waitress_role and not person in stripclub_waitresses:
            stripclub_waitresses.append(person)
        return

    def strip_club_fire_stripper(person):
        if person.has_role(stripper_role):
            person.remove_role(stripper_role)
        if person.has_role(bdsm_performer_role):
            person.remove_role(bdsm_performer_role)
        if person.has_role(waitress_role):
            person.remove_role(waitress_role)

        # restore default schedules
        if person.is_employee():
            person.set_schedule(person.home, times = [4])
        elif person in [lily, mom, aunt]:
            person.set_schedule(person.home, days = [0, 1, 3, 4, 5, 6], times = [4])
        else:
            person.set_schedule(None, times = [3])
            person.set_schedule(person.home, times = [4])

        if person in stripclub_strippers:
            stripclub_strippers.remove(person)
        if person in stripclub_bdsm_performers:
            stripclub_bdsm_performers.remove(person)
        if person in stripclub_waitresses:
            stripclub_waitresses.remove(person)
        return

    def calculate_stripper_salary(person):
        shifts = person.event_triggers_dict.get("strip_club_shifts", 2)
        tit_modifier = 10 - (__builtin__.abs(5 - rank_tits(person.tits)))   # optimal size is DD-Cup
        age_modifier = 8 - (__builtin__.abs(25 - person.age) / 3.0)            # optimal age is 25
        slut_modifier = person.core_sluttiness / 20.0
        obed_modifier = 0
        if person.has_role(bdsm_performer_role):
            obed_modifier = person.obedience / 20.0

        return __builtin__.round((tit_modifier + age_modifier + slut_modifier + obed_modifier) * shifts, 1)

    def calculate_stripper_profit(person):
        shifts = person.event_triggers_dict.get("strip_club_shifts", 2)
        profit_base = person.stripper_salary * (renpy.random.random() + .7) # stripper income is variable
        if person.has_role(waitress_role):
            profit_base = person.stripper_salary * (renpy.random.random() + .5) # waitress income is variable

        tit_modifier = person.get_opinion_score("showing her tits") * 2
        ass_modifier = person.get_opinion_score("showing her ass") * 2

        return (profit_base + tit_modifier + ass_modifier + person.charisma) * shifts

    def is_strip_club_stripper_requirement(person):
        if get_strip_club_foreclosed_stage() >= 5:
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formalName]"
            if person.has_role([stripper_role, bdsm_performer_role, waitress_role]):
                return True
        return False

    def strip_club_hire_employee_requirement(person):
        if person.has_role([casual_hotwife_role, casual_FA_role]):
            return False
        if person.has_role([stripper_role, waitress_role, manager_role, mistress_role, bdsm_performer_role]):
            return False
        if person.is_employee() or person in list(set(unique_character_list)-set([cousin, aunt, mom, lily, nora])): # disqualified from action
            return False
        if __builtin__.len(stripclub_strippers) >= 5 and (not strip_club_get_manager() or __builtin__.len(stripclub_waitresses) >= 2) and (not mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False) or __builtin__.len(stripclub_bdsm_performers) >= 5):
            return "At maximum Strip Club employees"
        if day < person.event_triggers_dict.get("stripper_ask_hire", 0) + 3:
            return "Asked too recently"
        return True

    def strip_club_review_requirement(person):
        if get_strip_club_foreclosed_stage() >= 5 and person.has_role([stripper_role, bdsm_performer_role, waitress_role]):
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formalName]"
            if day - person.event_triggers_dict.get("stripclub_last_promotion_day", -7) < 7:
                return "Too recently promoted"
            if day - person.event_triggers_dict.get("day_last_performance_review", -7) < 7:
                return "Too recently reviewed"
            return True
        return False

    def add_strip_club_hire_employee_action_to_mc_actions():
        strip_club_hire_employee_action = Action("Employ at [strip_club.formalName]", strip_club_hire_employee_requirement, "strip_club_hire_employee_label", menu_tooltip = "Hire [the_person.title] to work for you in your strip club.")
        mc.main_character_actions.append(strip_club_hire_employee_action)

    def allow_promote_to_manager_requirement(person):
        if person.has_role([stripper_role, waitress_role, bdsm_performer_role]) and not strip_club_get_manager() and not strip_club_get_mistress():
            # if person.age < 25: # As requested from a lot of people to hire Gabrielle as manager
                # return "Requires: age >= 25"
            if person.int < 4 or person.charisma < 5:
                return "Requires: intelligence >= 4 and charisma >= 5"
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formalName]"
            # if day - the_person.event_triggers_dict.get("stripclub_hire_day", -7) < 7: # Maybe I hired her just because I want to have her as manager (immediately)
                # return "Too recently hired"
            return True
        return False

    def build_strip_club_hire_role_menu(person):
        available_roles = []
        if __builtin__.len(stripclub_strippers) < 5:
            available_roles.append(["Stripper", stripper_role])
        if strip_club_get_manager() and __builtin__.len(stripclub_waitresses) < 2:
            available_roles.append(["Waitress", waitress_role])
        if mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False) and __builtin__.len(stripclub_bdsm_performers) < 5:
            available_roles.append(["BDSM Performer", bdsm_performer_role])

        available_roles.append(["Forget It", "None"])

        available_roles.insert(0, "Strip Club Role")
        return [available_roles]

    promote_to_manager_action = Action("Appoint as Manager", allow_promote_to_manager_requirement, "promote_to_manager_label", menu_tooltip = "Appoint [the_person.title] as strip club manager.")

    strip_club_stripper_fire_action = Action("Fire her", is_strip_club_stripper_requirement, "strip_club_fire_employee_label", menu_tooltip = "Fire [the_person.title] from her stripper job in your strip club.")
    strip_club_stripper_performance_review_action = Action("Review her performance", strip_club_review_requirement, "stripper_performance_review_label", menu_tooltip = "Review [the_person.title]'s performances on stage.")

    stripper_role = Role("Stripper", [promote_to_manager_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action], hidden = False)

label update_strip_club_show_requirement(stack):
    python:
        strip_club_show_action.requirement = strip_club_show_requirement_enhanced #strip_club_show_action is not defined until we begin the game.

        # make sure we store the stripclub performers
        if not "stripclub_bdsm_performers" in globals():
            stripclub_bdsm_performers = MappedList(Person, all_people_in_the_game)
        if not "stripclub_waitresses" in globals():
            stripclub_waitresses = MappedList(Person, all_people_in_the_game)

        execute_hijack_call(stack)
    return

label strip_club_hire_employee_label(the_person):
    mc.name "So [the_person.title], are you looking for a job?"
    $ ran_num = renpy.random.randint(0,100)
    if the_person is lily:
        $ the_person.event_triggers_dict["strip_club_shifts"] = 1
        the_person.char "Hey [the_person.mc_title], you know I'm always looking for ways to boost my pocket money, a student has always a shortage of money."
        mc.name "Then you might like the proposal I have for you."
    elif the_person is mom:
        $ the_person.event_triggers_dict["strip_club_shifts"] = 1
        the_person.char "Hi [the_person.mc_title], you know I have a lot of bills to pay, but I also have my job, so I'm not really looking for something else."
        mc.name "I think you are going to like this offer."
    elif the_person is aunt:
        $ the_person.event_triggers_dict["strip_club_shifts"] = 1
        the_person.char "Hello [the_person.mc_title], i'm so tired of sitting around at home all day, I wouldn't mind a little diversion."
        mc.name "Well, it's not exactly a daytime job, but the hours and pay are very good."
    elif the_person is cousin:
        the_person.char "After you fired me from the strip club I didn't find anything interesting... Do you have something in mind?"

        call screen enhanced_main_choice_display(build_menu_items(build_strip_club_hire_role_menu(the_person)))
        if _return == "None":
            mc.name "I've changed my mind, we will talk about this another time."
            the_person.char "Ok, that's fine."
            $ the_person.event_triggers_dict["stripper_ask_hire"] = day
            return

        $ ran_num = calculate_stripper_salary(the_person)

        if _return is stripper_role:
            mc.name "Actually I had a change of heart, how do you feel about coming back to work for me at the strip club?"
            $ the_person.draw_person(emotion = "happy", position = "stand5")
            the_person.char "Ok, but after what you did last time, the pay should be magnificent!"
            mc.name "Your pay will be $[ran_num] a day. Do you think that will be good enough for you?"
            the_person.char "Really you will pay me that much? Ok, then my answer is yes, I'll work as stripper again."

        elif _return is bdsm_performer_role:
            mc.name "I did it just because I already knew I had a better offer for a girl like you. How do you feel about coming back at the strip club to work as BDSM performer?"
            $ the_person.draw_person(emotion = "happy", position = "stand5")
            the_person.char "Maybe, but as stripper I was getting good money, so if I do this, the pay should be a lot better!"
            mc.name "Your pay will be $[ran_num] a day. Do you think that is 'a lot better' for you?"
            the_person.char "Really you will pay me that much? Ok, then my answer is yes, I'll do some kinky stuff for you."

        else:
            mc.name "I don't like the idea of you working as stripper, but how do you feel about coming back at the strip club to work as waitress?"
            $ the_person.draw_person(emotion = "happy", position = "stand5")
            the_person.char "Ok, but as stripper I was getting good money, so the pay should be this good!"
            mc.name "Your pay will be $[ran_num] a day. Do you think that will be good enough for you?"
            the_person.char "Really you will pay me that much just to give people drinks and clean some tables? Ok, then my answer is yes."


        $ strip_club_hire_stripper(the_person, _return)
        mc.name "See you at the club."
        return
    elif the_person.is_employee():
        $ the_person.event_triggers_dict["strip_club_shifts"] = 1
        if mc.business.is_open_for_business():
            the_person.char "What do you mean, I already have a job, right here, right now."
            mc.name "Don't worry, it won't interfere with this job, I just thought you might like to make something extra on the side."
        else:
            the_person.char "I don't understand, I already work for you. Or are you terminating my position?"
            mc.name "Of course not, you are a valuable employee, but I thought you might like to make some extra cash for just a few hours work, after hours."
    elif ran_num < 33: # 33% chance Yes
        the_person.char "Actually yes, I would welcome something to do in my life... Do you have something available for me?"
    elif ran_num > 67: # 33% chance No
        the_person.char "No [the_person.mc_title], I already have a job right now and I'm happy with it."
        mc.name "Oh, that's good for you! If one day you'll change your mind, let me know."
        the_person.char "Sure, thank you!"
        $ the_person.event_triggers_dict["stripper_ask_hire"] = day
        return
    else: # chance left (34%) Maybe
        the_person.char "Maybe, but not right now, I'm really busy at the moment, so there's not too many jobs I can do..."
        mc.name "Then my proposal will be perfect for you!"

    if mc.location is strip_club:
        mc.name "I own this strip club and I could see you working here..."
    else:
        mc.name "I own the [strip_club.formalName] downtown, and I need some workers for the place..."

    the_person.char "Oh my God, really? You're proposing a job in your strip club? I don't know..."

    $ ran_num = calculate_stripper_salary(the_person)

    call screen enhanced_main_choice_display(build_menu_items(build_strip_club_hire_role_menu(the_person)))
    if _return == "None":
        mc.name "I've changed my mind, we will talk about this another time."
        the_person.char "Ok, that's fine."
        $ the_person.event_triggers_dict["stripper_ask_hire"] = day
        return

    if _return is stripper_role:
        if the_person.has_role(prostitute_role):
            the_person.char "Could I still turn tricks, when I like the guy?"
            mc.name "As long as you don't do it inside the club, you can do what ever you like."
            the_person.char "Great, then I'll be a stripper for you."
        elif the_person.effective_sluttiness() > 70:
            the_person.char "I admit, I love turning men on, just making them horny while they ogle my body, mmm... Where should I sign?"
        elif the_person.effective_sluttiness() > 40 and the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 1:
            the_person.char "I admit, I always wanted to do something like that. Seducing men, with my body on full display, mmm... Where should I sign?"
        elif the_person.effective_sluttiness() > 20 and the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 3:
            the_person.char "Maybe, if the money is good enough, I could give it a try..."
            mc.name "Your pay will be $[ran_num] a day. Do you think that will be good enough for you?"
            the_person.char "Really you will pay me that much? Ok, then my answer is yes, I'll work as stripper for you."
        else:
            the_person.char "I'm sorry [the_person.mc_title], I'm flattered you think I'm pretty enough for the job, but I don't think I would fit in there, showing so much skin..."
            "Maybe I can work on her sluttiness a bit, or change her attitude to 'showing some skin' and try again."
            mc.name "Don't worry [the_person.title], if you change your mind, just let me know."
            $ the_person.event_triggers_dict["stripper_ask_hire"] = day
            return

    elif _return is bdsm_performer_role:
        mc.name "I was thinking you might like to perform in the BDSM room..."
        if the_person.has_role(prostitute_role):
            the_person.char "Could I still turn tricks, when I like the guy?"
            mc.name "As long as you don't do it inside the club, you can do what ever you like."
            the_person.char "Great, then I'll be your naughty girl on stage."
        elif the_person.effective_sluttiness() > 70:
            the_person.char "That sounds like something interesting... What do you think I should do?"
            mc.name "You're a beautiful, sexy and attractive girl, you'll be amazing on stage!"
            the_person.char "You are absolutely right, where should I sign?"
        elif the_person.effective_sluttiness() > 40 and the_person.get_opinion_score("being submissive") + the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 1:
            the_person.char "I don't know... I really don't know... What do you think I should do?"
            mc.name "You're a beautiful, sexy and attractive girl, you'll be amazing on stage!"
            the_person.char "Ok, your offer is really tempting, where should I sign?"
        elif the_person.effective_sluttiness() > 20 and the_person.get_opinion_score("being submissive") + the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 4:
            the_person.char "Maybe, if the money is good enough, I could give it a try..."
            mc.name "Your pay will be $[ran_num] a day, is that good enough for you?"
            the_person.char "Oh! Your offer was tempting, and for that money I don't care being a bit submissive and show some skin. Ok then, my answer is yes."
        else:
            the_person.char "I'm sorry [the_person.mc_title], I'm flattered you think I'm pretty enough for the job, but I don't think I would fit in there, letting everyone know how slutty I am..."
            "Maybe I can work on her sluttiness a bit, or change her attitude to 'showing some skin' or 'being submissive' and try again."
            mc.name "Don't worry [the_person.title], if you change your mind, just let me know."
            $ the_person.event_triggers_dict["stripper_ask_hire"] = day
            return

    else:
        mc.name "I was thinking you might like to become a waitress..."
        if the_person.has_role(prostitute_role):
            the_person.char "Could I still turn tricks, when I like the guy?"
            mc.name "As long as you don't do it inside the club, you can do what ever you like."
            the_person.char "Great, then I'll be one of the best waitresses you will ever see."
        elif the_person.effective_sluttiness() > 50:
            the_person.char "I would love being a waitress, showing some skin, have them groping my ass... Ok, where should I sign?"
        elif the_person.effective_sluttiness() > 20 and the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 0:
            the_person.char "If it's just to be a waitress there, I don't mind showing some skin... Ok, where should I sign?"
        elif the_person.effective_sluttiness() > 10 and the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 2:
            the_person.char "Maybe, if the money is good enough, I could give it a try..."
            $ ran_num = calculate_waitress_salary(the_person)
            mc.name "Your pay will be $[ran_num] a day, not bad for waiting some tables, right?"
            the_person.char "Oh! Ok, then my answer is yes, for that kind of money I don't mind running around in a short skirt waiting tables."
        else:
            the_person.char "I'm sorry [the_person.mc_title], I'm flattered you think I'm pretty enough for the job, but I don't think I would fit in there, showing so much skin..."
            "Maybe I can work on her sluttiness a bit, or I change her attribute to 'showing some skin' and try again."
            mc.name "Don't worry [the_person.title], if you change your mind, just let me know."
            $ the_person.event_triggers_dict["stripper_ask_hire"] = day
            return

    "You ask her to sign the standard contract and [the_person.title] now works for you in the [strip_club.formalName]."

    $ strip_club_hire_stripper(the_person, _return)

    the_person.char "Thank you for the opportunity [the_person.mc_title], I'll try my best!"
    return

label strip_club_fire_employee_label(the_person):
    if the_person.has_role(stripper_role) or the_person.has_role(waitress_role):
        mc.name "[the_person.title], I've checked your performances on stage and it is absolutely unsatisfactory."
        mc.name "There's no a nice way to say this, but you're fired, you can finish your shift tonight and collect your severance pay."
        $ the_person.draw_person(emotion = "happy", position = "stand3")
        the_person.char "Are you sure [the_person.mc_title]? There's nothing I can do to make you change your mind?"
        "She place a hand on your crotch and start to move it gently, with a clear innuendo."
    else: # bdsm performer
        mc.name "[the_person.title], I've checked your performances here, your Master is really disappointed."
        mc.name "There's not a nice way to say this, but you're fired, you can finish your shift tonight and collect your severance pay."
        $ the_person.draw_person(position = "kneeling1", emotion = "sad")
        the_person.char "Are you sure Master? There's nothing your pet here can do to make you change your mind?"
        "She places her cheek on your leg as a good pet, waiting for a caress from her Master."

    menu:
        "Accept the advances":
            mc.name "Alright [the_person.title], you've got me interested, try to convince me."
            $ the_person.add_situational_slut("seduction_approach", -5, "I'm just a toy for him.")
            $ the_person.add_situational_obedience("seduction_approach", 25, "I'll do what I need to keep my job!")
            call fuck_person(the_person, private = True) from _call_fuck_person_strip_club_fire_employee_label
            $ the_person.clear_situational_slut("seduction_approach")
            $ the_person.clear_situational_obedience("seduction_approach")
            $ the_person.apply_planned_outfit()
            $ the_person.change_stats(happiness = -5, obedience = 5, slut_temp = 3)
            mc.name "Okay [the_person.title], I'll keep you around for a little while longer, but you really need to work on your act, I'm not running a charity."
            if the_person.effective_sluttiness() < 50:
                the_person.char "I'll do my best [the_person.mc_title], I promise."
            else:
                the_person.char "It's tempting just to be fucked like this again..."
            return
        "Refuse":
            mc.name "I'm sorry [the_person.title], but sex won't make me change my mind..."
            $ the_person.draw_person(emotion = "sad", position = "stand3")
            the_person.char "Damn... Ok, I will clear out my locker at the end of my shift."
            $ the_person.change_stats(happiness = -10, obedience = -5, love = -5)
            $ strip_club_fire_stripper(the_person)
    return

label stripper_performance_review_label(the_person):
    $ the_person.event_triggers_dict["day_last_performance_review"] = day
    mc.name "[the_person.title], I'd like to have a talk with you about your recent performance here at the club. Can you follow me to my office?"
    if the_person.obedience > 100:
        the_person.char "Oh, of course [the_person.mc_title]."
    else:
        the_person.char "Uh, I guess. so."

    "You lead [the_person.title] to your office at the strip club and close the door behind her, asking her to sit down."
    $ the_person.draw_person(position = "sitting")
    mc.name "So [the_person.title], tell me what you think about your job."
    if the_person.get_job_happiness_score() > 0: # She's happy enough with the job to stay here
        if the_person.stripper_salary > the_person.calculate_base_salary() + 20: # She get a lot of money as stripper in comparison with a 'regular' job
            the_person.char "It's a fantastic job and I'm lucky to have it! There aren't very many places that would be able to pay me as well as I am here."
        elif the_person.stripper_salary > the_person.calculate_base_salary() + 5: # She get some money more as stripper in comparison with a 'regular' job
            the_person.char "It's a great job. The pay is great and the work is 'stimulating'."
        elif the_person.stripper_salary > the_person.calculate_base_salary() - 5: # She get the same money as stripper in comparison with a 'regular' job
            the_person.char "I really like my job, every day I feel like I can come in and do an honest day's work."
        else: # She get less money as stripper in comparison with a 'regular' job
            the_person.char "The pay isn't the greatest, but I really enjoy working here."
    else: #She's thinking about quitting.
        if the_person.stripper_salary > the_person.calculate_base_salary() + 20: #She's very overpaid# She get a lot of money as stripper in comparison with a 'regular' job
            the_person.char "The pay is amazing, but the work environment here is just terrible. I honestly don't know how much longer I can take it."
        elif the_person.stripper_salary > the_person.calculate_base_salary() + 5: # She get some money more as stripper in comparison with a 'regular' job
            the_person.char "I know you're paying me very well, but the work here is terrible. I hope you have some plans to make things better."
        elif the_person.stripper_salary > the_person.calculate_base_salary() - 5: # She get the same money as stripper in comparison with a 'regular' job
            the_person.char "Things could be better. I'd like it if my conditions to work here were improved a little, or I could be paid a little bit more."
        else: # She get less money as stripper in comparison with a 'regular' job
            the_person.char "I don't really have anything positive to say. The pay isn't great and it isn't exactly the most pleasant work environment."
    "You nod and take some notes while you think of how you want to respond."
    $ ran_num = calculate_stripper_salary(the_person)
    "Her actual salary is $[the_person.stripper_salary], but for her current performance level it should be $[ran_num], what will you do?"
    menu:
        "Reward her for work well done":
            $ raise_amount = __builtin__.round(the_person.stripper_salary * 0.1)
            menu:
                "Give her a raise\n{color=#ff0000}{size=18}Costs: $[raise_amount] / day{/size}{/color}": #Pay her more money. Large happiness and obedience raise.
                    mc.name "I've been very impressed by your work lately, and I'd like to make sure you stay happy with your decision to work here."
                    mc.name "I'm going to put you down for a 10%% raise. How does that sound?"
                    $ the_person.stripper_salary += raise_amount
                    $ the_person.change_stats(happiness = 1 + mc.charisma, obedience = 1 + mc.charisma)
                    $ the_person.draw_person(position = "sitting", emotion = "happy")
                    the_person.char "That sounds amazing! Thank you sir, I promise I won't let you down!"
                    mc.name "Good to hear it."
                "Reward her sexually" if the_person.effective_sluttiness() >= 40: #At high sluttiness you can make her cum to make her even happier with her job.
                    mc.name "You do a lot of work here in the club, and I know how stressful your job can be at times."
                    "You get up, step behind [the_person.title] and place your hands on her shoulders, rubbing them gently."
                    mc.name "I'd like to do something for you to help you relax. How does that sound for a bonus?"
                    $ the_person.add_situational_slut("seduction_approach", 15, "It's all about me!")
                    $ the_person.add_situational_obedience("seduction_approach", -10, "It's all about me!")
                    the_person.char "Oh [the_person.mc_title], that sounds like a great idea..."
                    call fuck_person(the_person, private = True) from _call_fuck_stripper_performance_review_1
                    $ the_report = _return
                    $ the_person.clear_situational_slut("seduction_approach")
                    $ the_person.clear_situational_obedience("seduction_approach")
                    if the_report.get("girl orgasms", 0) > 1: #We made her cum multiple times! Congratulations!
                        $ the_person.change_stats(happiness = 10, slut_temp = 3, love = 2)
                        the_person.char "Oh [the_person.mc_title], that was wonderful! I couldn't have asked for a better performance bonus!"
                    elif the_report.get("girl orgasms", 0) == 1:
                        $ the_person.change_stats(happiness = 5, slut_temp = 1)
                        the_person.char "Well, that was a good time [the_person.mc_title]. It's a lot more fun than a normal performance bonus, that's for sure!"
                    else:
                        $ the_person.change_stats(happiness = -5, obedience = -2)
                        the_person.char "It's not much of a bonus if you're the only one who gets to cum. Maybe next time a cash bonus would be better, okay?"
                    $ the_person.apply_planned_outfit()

        "Punish her for poor performance":
            $ cut_amount = __builtin__.round(the_person.salary * 0.1)
            menu:
                "Cut her pay\n{color=#00ff00}{size=18}Profit: $[cut_amount] / day{/size}{/color}": #Pay her less. Large happiness and obedience drop.
                    mc.name "I'm really sorry to do this [the_person.title], but your performance lately just doesn't justify what I'm paying you."
                    mc.name "I'm going to have to cut your pay by 10%%."
                    $ the_person.change_salary(-cut_amount)
                    $ the_person.change_stats(happiness = -10 - mc.charisma, obedience = -5 - mc.charisma)
                    if the_person.get_job_happiness_score() > 0:
                        $ the_person.draw_person(position = "sitting", emotion = "sad")
                        the_person.char "I... I understand."
                    elif the_person.get_job_happiness_score() > -25:
                        $ the_person.draw_person(position = "sitting", emotion = "angry")
                        the_person.char "What? I... I don't know what to say!"
                        mc.name "Like I said, I'm sorry but it has to be done."
                    else: #She's so unhappy with her job she quits.
                        $ the_person.draw_person(position = "sitting", emotion = "angry")
                        the_person.char "What? I... I can't believe that [the_person.mc_title], why would you ever think I would stay here for less money?"
                        mc.name "Like I said, I'm sorry but it has to be done."
                        the_person.char "Well you know what, I think I'm just going to find somewhere else to work. I quit."
                        $ clear_scene()
                        "[the_person.title] stands up and storms out of the room."
                        $ the_person.change_stats(happiness = -25, obedience = -15, love = -30)
                        $ strip_club_fire_stripper(the_person)
                        $ person.location.move(the_person.home)
                        return
                "Threaten to fire her": #She may ask to stay in exchange for some sort of favour, or get fired on the spot.
                    mc.name "I'll be honest with you [the_person.title], your performance here at the club leaves a lot to be desired."
                    mc.name "I've been running the numbers and I think, unless you can convince me otherwise, we'd be better off without you."
                    if the_person.get_job_happiness_score() > -10:
                        if the_person.effective_sluttiness() < 20:
                            the_person.char "No sir, I really need this job. What if I took a pay cut? Would that be enough?"
                            menu:
                                "Cut her pay\n{color=#00ff00}{size=18}Profit: $[cut_amount] / day{/size}{/color}":
                                    mc.name "If you're willing to take a pay cut I think I can keep you around and see if your performance improves."
                                    $ the_person.stripper_salary += -cut_amount
                                    $ the_person.change_stats(happiness = 10, obedience = 5)
                                    the_person.char "Thank you sir! Thank you so much!"
                                "Fire her":
                                    mc.name "I'm sorry, but that wouldn't be enough."
                                    the_person.char "I understand. I'll clear out my locker at the end of my shift."
                                    $ the_person.change_stats(happiness = -10, obedience = -5)
                                    $ strip_club_fire_stripper(the_person)
                        else:
                            the_person.char "Wait, I really need this job... What if I... let you use me. Just so you'll keep me around."
                            menu:
                                "Fuck her":
                                    $ the_person.add_situational_slut("seduction_approach", -5, "I'm just a toy to him.")
                                    $ the_person.add_situational_obedience("seduction_approach", 25, "I'll do what I need to keep my job!")
                                    mc.name "Alright, you've got me interested. Let's see what you can do."
                                    call fuck_person(the_person,private = True) from _call_fuck_stripper_performance_review_2
                                    $ the_person.clear_situational_slut("seduction_approach")
                                    $ the_person.clear_situational_obedience("seduction_approach")
                                    $ the_person.apply_planned_outfit()
                                    $ the_person.change_stats(happiness = -5, obedience = 5, slut_temp = 3)
                                    mc.name "Okay [the_person.title], I'll keep you around for a little while longer, but you're going need to work on your act, else I might change my mind about keeping you here."
                                    if the_person.effective_sluttiness() < 50:
                                        the_person.char "I'll do my best [the_person.mc_title], I promise."
                                    else:
                                        the_person.char "It's tempting just to be fucked like this again..."
                                "Fire her":
                                    mc.name "I'm sorry, but that wouldn't be enough."
                                    the_person.char "I understand. I'll clear out my locker at the end of the shift."
                                    $ the_person.change_stats(happiness = -15, obedience = -10, love = -10)
                                    $ strip_club_fire_stripper(the_person)
                                    return
                    else:
                        $ the_person.draw_person(position = "sitting", emotion = "angry")
                        the_person.char "What? You want me to beg to stay at this shitty job? If you don't want me here I think it's best I just move on. I quit!"
                        $ clear_scene()
                        "[the_person.title] stands up and storms out."
                        $ the_person.change_stats(happiness = -15, obedience = -10, love = -10)
                        $ strip_club_fire_stripper(the_person)
                        return
                "Punish her sexually" if the_person.effective_sluttiness() >= 40 and the_person.obedience >= 120: #Orgasm denial and/or make her service you.
                    "You sigh dramatically, stand up and walk over to [the_person.title]."
                    mc.name "Your performance has really let me down, but I think what you need is a little motivation."
                    mc.name "I want to have some fun with you, but you're not allowed to climax, is that understood?"
                    $ opinion_modifier = the_person.get_opinion_score("being submissive") * 5
                    $ the_person.add_situational_slut("seduction_approach", -5+opinion_modifier, "I'm just being used...")
                    $ the_person.add_situational_obedience("seduction_approach", 15+opinion_modifier, "I'm being punished")
                    the_person.char "I... if you think this is what I need, sir."
                    call fuck_person(the_person, private = True) from _call_fuck_person_stripper_performance_review_3
                    $ the_report = _return
                    $ the_person.clear_situational_slut("seduction_approach")
                    $ the_person.clear_situational_obedience("seduction_approach")
                    if the_report.get("girl orgasms", 0) > 0: #We made her cum! Congratulations!
                        $ the_person.change_stats(happiness = 5, slut_temp = 1, love = 2)
                        the_person.char "You just can't resist pleasing me, can you [the_person.mc_title]? I thought I wasn't supposed to cum?"
                        "[the_person.title] seems smug about her orgasmic victory."
                    elif the_report.get("end arousal", 0) >= 80:
                        $ the_person.change_stats(happiness = 5, slut_temp = 2, obedience = 3)
                        the_person.char "Oh my god [the_person.mc_title], you got me so close... Can't you just finish me off, real quick?"
                        mc.name "Do a better job and I'll let you cum next time, understood?"
                        "[the_person.title] nods meekly."
                    else:
                        $ the_person.change_stats(happiness = -5, obedience = 3)
                        mc.name "That felt great [the_person.title], I suppose if your performance doesn't improve you'll still be useful as a toy."
                        the_person.char "I... Yes sir, I suppose I would be."
                    $ the_person.apply_planned_outfit()
        "Finish the performance review":
            mc.name "Well, I think you're doing a perfectly adequate job around here [the_person.title]. If you keep up the good work I don't think we will have any issues."
            $ the_person.change_stats(happiness = 2, obedience = 1)
            the_person.char "Thank you, I'll do my best."
    "You stand up and open the door for [the_person.title] at the end of her performance review."
    $ clear_scene()
    return
