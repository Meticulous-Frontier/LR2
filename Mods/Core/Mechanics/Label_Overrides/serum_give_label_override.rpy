# Replacement for giving the serum to someone
# Original code by DaMatt

init 2 python:
    config.label_overrides["serum_give_label"] = "serum_give_label_enhanced"

    def serum_give_calculate_chances(person):
        sneak_serum_chance = 70 + (mc.int * 5) - (person.focus*5)  #% chance that you will successfully give serum to someone sneakily. Less focused people are easier to fool.
        ask_serum_chance = 10 * mc.charisma + 5 * person.int #The more charismatic you are and the more intellectually curious they are the better the chance of success
        demand_serum_chance = mc.charisma * (person.obedience - 90) #The more charismatic you are and the more obedient they are the more likely this is to succeed.

        sneak_serum_chance = 0 if sneak_serum_chance < 0 else 100 if sneak_serum_chance > 100 else sneak_serum_chance
        ask_serum_chance = 0 if ask_serum_chance < 0 else 100 if ask_serum_chance > 100 else ask_serum_chance

        if mc.business.get_employee_title(person) == "None":
            demand_serum_chance += -35 #if she doesn't work for you there is a much lower chance she will listen to your demand (unless you are very charismatic or she is highly obedient.)

        demand_serum_chance = 0 if demand_serum_chance < 0 else 100 if demand_serum_chance > 100 else demand_serum_chance

        pay_serum_cost = person.salary * 5
        return [sneak_serum_chance, ask_serum_chance, demand_serum_chance, pay_serum_cost]

    def serum_give_chance_color_wrapper(chance):
        color = "#D00000"
        if chance > 80:
            color = "#00D000"
        elif chance > 50:
            color = "#D0D000"

        return "\n{size=12}{color=" + color + "}" + str(chance) + "% Success Chance{/color}{/size}"

    def serum_give_build_menu_options(person, chances):
        option_list = []
        option_list.append(["Give it to her stealthily" + serum_give_chance_color_wrapper(chances[0]), "stealth"])
        option_list.append(["Demand she takes it" + serum_give_chance_color_wrapper(chances[2]), "demand"])
        if person.has_role(slave_role):
            option_list.append(["Order her to take it\n{size=12}{color=#00D000}She is your slave{/color}{/size}", "slave"])
        elif person.is_employee():
            if mandatory_unpaid_serum_testing_policy.is_owned():
                option_list.append(["Ask her to take it\n{size=12}{color=#00D000}Required by Policy{/color}{/size}", "policy"])
            else:
                option_list.append(["Ask her to take it" + serum_give_chance_color_wrapper(chances[1]), "ask"])
                if mandatory_paid_serum_testing_policy.is_owned() and mc.business.funds >= chances[3]:
                    option_list.append(["Pay her to take it\n{size=12}{color=#D00000}Costs $" + str(chances[3]) + "{/color}{/size}", "paid"])
        else:
            option_list.append(["Ask her to take it" + serum_give_chance_color_wrapper(chances[1]), "ask"])
        option_list.insert(0, "Give Serum")
        return option_list


label serum_give_label_enhanced(the_person):
    $ ran_num = renpy.random.randint(0,100)
    $ chances = serum_give_calculate_chances(the_person)

    call screen enhanced_main_choice_display(build_menu_items([serum_give_build_menu_options(the_person, chances)]))

    if _return == "stealth":
        "You chat with [the_person.title] for a couple of minutes. Waiting to find a chance to deliver a dose of serum."
        if ran_num <= chances[0]:
            #Success
            "You're able to distract [the_person.title] and have a chance to give her a dose of serum."
            call give_serum(the_person) from _call_give_serum_enhanced_1
        else:
            #Caught!
            "You finally distract [the_person.title] and have a chance to give her a dose of serum."
            the_person "Hey, what's that?"
            "You nearly jump as [the_person.title] points down at the small vial of serum you have clutched in your hand."
            $ ran_num = renpy.random.randint(0,10)
            if ran_num < mc.charisma:
                if mc.business.get_employee_title(the_person) == "None":
                    mc.name "This? Oh, it's just something we're working on at the lab that I thought you might be interested in."
                    "You dive into a technical description of your work, hoping to distract [the_person.title] from your real intentions."
                else:
                    mc.name "This? Oh, it's just one of the serums I grabbed from production for quality control. I was just fidgeting with it I guess."
                    "You make small talk with [the_person.title], hoping to distract her from your real intentions."
                "After a few minutes you've managed to avoid her suspicion, but haven't been able to deliver the dose of serum."
            else:
                mc.name "This? Uh..."
                $ the_person.draw_person(emotion="angry")
                $ the_person.change_obedience(-10)
                $ the_person.change_happiness(-10)
                $ the_person.change_love(-5)
                the_person "Were you about to put that in my drink? Oh my god [the_person.mc_title]!"
                mc.name "Me? Never!"
                "[the_person.title] shakes her head and storms off. You can only hope this doesn't turn into something more serious."
                $ clear_scene()

    elif _return == "slave":
        #Auto success
        mc.name "[the_person.title], I'll help you to become a good slave. Take this."
        call give_serum(the_person) from _call_give_serum_enhanced_2

    elif _return == "ask":
        if mc.business.get_employee_title(the_person) == "None":
            mc.name "[the_person.title], I've got a project going on at work that could really use a test subject. Would you be interested in helping me out?"
        else:
            mc.name "[the_person.title], there's a serum design that is in need of a test subject. Would you be interested in helping out with a quick field study?"

        if ran_num <= chances[1]:
            #Success
            if mc.business.get_employee_title(the_person) == "None":
                if the_person == nora:
                    the_person "I'd be happy to help. I've seen your work, I have complete confidence you've tested this design thoroughly."
                else:
                    the_person "I'd be happy to help, as long as you promise it's not dangerous of course. I've always wanted to be a proper scientist!"
            else:
                the_person "I'll admit I'm curious what it would do to me. Okay, as long as it's already passed the safety test requirements, of course."
            mc.name "It's completely safe, we just need to test what the results from it will be. Thank you."
            call give_serum(the_person) from _call_give_serum_enhanced_3
        else:
            #Denies
            $ the_person.change_obedience(-2)
            the_person "I'm... I don't think I would be comfortable with that. Is that okay?"
            mc.name "Of course it is, that's why I'm asking in the first place."

    elif _return == "policy":
        #Auto success
        mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this."
        call give_serum(the_person) from _call_give_serum_enhanced_4

    elif _return == "demand":
        mc.name "[the_person.title], you're going to drink this for me."
        "You pull out a vial of serum and present it to [the_person.title]."
        the_person "What is it for, is it important?"
        mc.name "Of course it is, I wouldn't ask you to if it wasn't."
        if ran_num <= chances[2]:
            #Success
            the_person "Okay, if that's what you need me to do..."
            call give_serum(the_person) from _call_give_serum_enhanced_5
        else:
            #Refuse
            $ the_person.draw_person(emotion = "angry")
            $ the_person.change_obedience(-2)
            $ the_person.change_happiness(-2)
            $ the_person.change_love(-2)
            the_person "You expect me to just drink random shit you hand to me? I'm sorry, but that's just ridiculous."

    elif _return == "pay":
        #Pay cost and proceed
        $ mc.business.change_funds(chances[3])
        mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this, a bonus will be added onto your paycheck."
        call give_serum(the_person) from _call_give_serum_enhanced_6

    $ del chances
    return
