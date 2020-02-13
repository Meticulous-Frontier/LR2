#####################################  Scene Idea  ##############################################
# Scene: One one One Training
#        Pick a random (obedient? intelligent? Probably not bimbo) employee during business hours. Verify they have atleast one work skill lower than MC
#        Give MC the option to train the NPC in the skill for a random (small) increase
#        ***Optional:
#        If NPC is slutty (>60?), check and see if MC has sex skill greater than NPC
#        If yes, have NPC ask if MC will train her in sex skill
#        Check if MC has energy. If yes give MC option to train in sex skill
#        If yes, trigger sex skill training scene.
#
#        Future options: Other benefits for NPCs having high sex skills
#
################################################################################################

init -1 python:
    one_on_one_weight = 5

init 2 python:
    # increases affection for trained job (if not maxed)
    def increase_job_affection(person, job_description):
        score = person.get_opinion_score(job_description)
        if score < 2:
            score += 1
            person.opinions[job_description] = [score, True]
            mc.log_event(person.title + " now " + opinion_score_to_string(score) + " " + job_description + ".", "float_text_grey")
        return

    def one_on_one_training_requirement():
        if not mc.business.is_weekend():
            if mc.is_at_work():
                if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
                    return True
        return False

    one_on_one_action = ActionMod("One on One Training", one_on_one_training_requirement, "SB_one_on_one_label",
        menu_tooltip = "You give an employee on the job training.", category = "Business", is_crisis = True, crisis_weight = one_on_one_weight)

label SB_one_on_one_label():
    python:
        training_eligible = []
        for person in mc.business.get_employee_list():
            if person.obedience > 110:
                if person.int > 1:
                    training_eligible.append(person)
        the_person = get_random_from_list(training_eligible)
        del training_eligible

    if the_person is None:
        # "No one eligible for training!"
        return

    "You take a quick break from work to go get a quick snack from the vending machine. While you are trying do decide what snack to buy, [the_person.possessive_title] enters the break room."
    $ the_person.draw_person()
    the_person.char "Oh, hey [the_person.mc_title]!"
    "You make small with [the_person.possessive_title] for a while. Eventually, the subject of your role in the company and the various jobs you fulfill around the lab comes up."
    the_person.char "Yeah, I've heard that you are pretty skilled at some of the different jobs are the lab here. I was wondering if maybe you could give me some pointers?"
    "You consider [the_person.possessive_title]'s request for a moment."
    $ change_amount = 0
    $ skill_master = False
    menu:
        "Train HR" if the_person.hr_skill < mc.hr_skill:
            if mc.hr_skill == mc.max_work_skills:
                $ skill_master = True
            "You explain to [the_person.possessive_title] the ins and outs of HR work. You do it in pretty broad terms, but it seems like she gets the hang of it pretty quickly."
            $ change_amount = renpy.random.randint(1,(mc.hr_skill - the_person.hr_skill))
            $ the_person.hr_skill += change_amount
            $ mc.log_event(the_person.title + ": +[change_amount] HR Skill", "float_text_grey")
            $ increase_job_affection(the_person, "HR work")
            if perk_system.has_ability_perk("Those Who Can't, Teach"):
                if mc.hr_skill < mc.max_work_skills:
                    $ mc.hr_skill += 1
                    $ mc.log_event("+1 HR skill from Perk", None)


        "Train Supply" if the_person.supply_skill < mc.supply_skill:
            if mc.supply_skill == mc.max_work_skills:
                $ skill_master = True
            "You do some hands on with [the_person.possessive_title], showing her various methods for securing the different chemicals required for serum production."
            $ change_amount = renpy.random.randint(1,(mc.supply_skill - the_person.supply_skill))
            $ the_person.supply_skill += change_amount
            $ mc.log_event(the_person.title + ": +[change_amount] Supply skill", "float_text_grey")
            $ increase_job_affection(the_person, "supply work")
            if perk_system.has_ability_perk("Those Who Can't, Teach"):
                if mc.supply_skill < mc.max_work_skills:
                    $ mc.supply_skill += 1
                    $ mc.log_event("+1 Supply skill from Perk", None)


        "Train Marketing" if the_person.market_skill < mc.market_skill:
            if mc.market_skill == mc.max_work_skills:
                $ skill_master = True
            "You spend some time with [the_person.possessive_title], giving all kind of advice on the art of the sale. It's not just all about good deals, but making people understand they need the product you offer."
            $ change_amount = renpy.random.randint(1,(mc.market_skill - the_person.market_skill))
            $ the_person.market_skill += change_amount
            $ mc.log_event(the_person.title + ": +[change_amount] Marketing skill", "float_text_grey")
            $ increase_job_affection(the_person, "marketing work")
            if perk_system.has_ability_perk("Those Who Can't, Teach"):
                if mc.market_skill < mc.max_work_skills:
                    $ mc.market_skill += 1
                    $ mc.log_event("+1 Market skill from Perk", None)


        "Train Research" if the_person.research_skill < mc.research_skill:
            if mc.research_skill == mc.max_work_skills:
                $ skill_master = True
            "You talk with [the_person.possessive_title] about various chemicals and scientific methods, and how they apply do different portions of the brain."
            $ change_amount = renpy.random.randint(1,(mc.research_skill - the_person.research_skill))
            $ the_person.research_skill += change_amount
            $ mc.log_event(the_person.title + ": +[change_amount] Researching skill", "float_text_grey")
            $ increase_job_affection(the_person, "research work")
            if perk_system.has_ability_perk("Those Who Can't, Teach"):
                if mc.research_skill < mc.max_work_skills:
                    $ mc.research_skill += 1
                    $ mc.log_event("+1 Research skill from Perk", None)


        "Train Production" if the_person.production_skill < mc.production_skill:
            if mc.production_skill == mc.max_work_skills:
                $ skill_master = True
            "You share some insights with [the_person.possessive_title] about the chemical processes and reactions between common serum elements."
            $ change_amount = renpy.random.randint(1,(mc.production_skill - the_person.production_skill))
            $ the_person.production_skill += change_amount
            $ mc.log_event(the_person.title + ": +[change_amount] Production skill", "float_text_grey")
            $ increase_job_affection(the_person, "production work")
            if perk_system.has_ability_perk("Those Who Can't, Teach"):
                if mc.production_skill < mc.max_work_skills:
                    $ mc.production_skill += 1
                    $ mc.log_event("+1 Production skill from Perk", None)

        "Too Busy":
            "You apologize. You are just too busy to offer one on one training right now."
    if change_amount > 0:
        the_person.char "Thanks for the help, [the_person.mc_title] I'm sure that will come in handy during work around here!"
        if not perk_system.has_ability_perk("Those Who Can't, Teach"):
            "Teaching someone else has given you new insights into your own skills. You realize by teaching others, you increase you own mastery in a given skill set."
            $ those_who_teach = Ability_Perk(description = "When you teach someone else a skill, you also gain a skill point in that area.", toggle = False, usable = False)
            $ perk_system.add_ability_perk(those_who_teach, "Those Who Can't, Teach")
        elif not perk_system.has_ability_perk("Those Who Can, Do"):
            if skill_master:
                "Sharing with someone a skill you thought you had wholly mastered reveals a few final deficient areas. You feel like you can take your skills even further now."
                $ those_who_do = Stat_Perk(description = "Teaching others has raised your skill ceiling to new levels. +1 work skills cap", skill_cap = 1)
                $ perk_system.add_stat_perk(those_who_do, "Those Who Can, Do")
    else:
        the_person.char "Thats okay, [the_person.mc_title], I understand. Maybe another time then!"

    $ renpy.scene("Active")
    return
