## Production Failure Crisis Mod by Tristimdorion
init -1 python:
    production_failure_weight = 5

init 2 python:
    def production_failure_requirement():
        if not mc.business.is_weekend():
            if mc.is_at_work():
                if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
                    return True
        return False

    def production_failure_increase_sluttiness(the_person):
        for person in the_person.work.people:
            person.add_situational_slut("Gassed",25,"The girls become extremely slutty.")
            person.change_slut_temp(3, add_to_log = False)
            person.change_slut_core(3, add_to_log = False)

        mc.log_event("All " + the_person.work.formalName + " staff: +3 sluttiness","float_text_pink")
        return

    def production_failure_clear_situational_sluttiness(the_person):
        for person in the_person.work.people:
            person.clear_situational_slut("Gassed")

        the_person.review_outfit()
        return

    def production_failure_change_obedience(the_person, amount):
        for person in mc.business.production_team:
            person.change_obedience(amount, add_to_log = False)

        mc.log_event("All " + the_person.work.formalName + " staff: " + str(amount) + " obedience","float_text_pink")
        return

    production_failure_action = ActionMod("Production Failure", production_failure_requirement, "production_failure_action_label",
        menu_tooltip = "An accident during research / production causes some issues.", category = "Business", is_crisis = True, crisis_weight = production_failure_weight)


label production_failure_action_label:
    $ the_person = get_random_from_list(rd_division.people + p_division.people)
    if the_person is None:
        return
    
    "While monitoring the equipment you notice a problem in the [the_person.work.formalName], it seems a gas mixture is building up."
    "Without halting work and alerting everyone to the problem there is no way to fix it. You also can't be sure what the effects of this will be on your employees."
    menu:
        "Halt work and fix the problem":
            "The girls are clearly unhappy about breathing in a foreign substance. But are extremely grateful you alerted them so soon."
            python:
                for person in mc.business.production_team:
                    person.change_stats(happiness = -2, love = 2, add_to_log = False)

                mc.log_event("All " + the_person.work.formalName + " staff: +2 love, -2 happiness","float_text_pink")

            "The repair man shows up early and fixes the problem. The loss of production was negligible."

        "Call in an overnight repair man":
            "You call the repair man and tell him to come in that night, and warn him not to alert anyone and to wear a gas mask."
            "You decide to monitor the situation first hand and move to the [the_person.work.formalName]."
            $ mc.change_location(the_person.work)
            $ mc.location.show_background()

            $ the_effect_number = renpy.random.randint(0,100)
            if the_effect_number > 60: # 40% chance its a mixture that alters behavior (slutty)
                "For the first half hour everything seems fine, but then you notice a sudden shift in behavior."
                "The girls are clearly hot and bothered. They barely keep their focus on their work. Spending much of their time eyeing you and each other."

                $ production_failure_increase_sluttiness(the_person)
                $ the_person.draw_person(position = "stand2", emotion = "happy")
                $ the_person.change_slut_temp(10)
                "[the_person.name] appears to have been particularly effected."
                "[the_person.name] looks around desperately trying to figure out the source of her sudden arousal. When she sees you she immediately loses control."
                the_person.char "Please [the_person.mc_title], I need you.... please help me... "
                "[the_person.possessive_title] shoves her hand down your pants and begs for your cock."

                call fuck_person(the_person, private = False, skip_intro = True) from _call_fuck_person_production_failure_action_label
                
                the_person.char "*Panting* Oh god, [the_person.mc_title]. Thank you... thank you so much."

                $ production_failure_clear_situational_sluttiness(the_person)

                "You leave [the_person.possessive_title] to get cleaned up and get back to work."
            elif the_effect_number > 45: # 15% chance
                $ production_failure_change_obedience(the_person, 3)               
                "The girls seem slightly more respectful."
            elif the_effect_number > 30: # 15% chance
                "Everyone appears fine, there doesn't seem to be an effect."
            else: # 30% chance its a foul mixture
                $ production_failure_change_obedience(the_person, -5)
                "The mood of all the girls turn sour. They spend the next few hours bickering about petty nonsense."
    return