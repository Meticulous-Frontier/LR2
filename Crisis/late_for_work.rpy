## Late for Work Crisis Mod by Tristimdorion
init -1 python:
    late_for_work_weight = 10   # Increase weight because it only occurs in one timeslot.

init 2 python:
    def late_for_work_requirement():
        if mc.business.get_employee_count() > 0:
            if time_of_day == 1: #is morning when employees arrive.
                if mc.business.is_open_for_business() and mc.is_at_work():
                    return True
        return False

    late_for_work_action = ActionMod("Late for Work Crisis", late_for_work_requirement, "late_for_work_action_label",
        menu_tooltip = "An employee is late for work.", category = "Business")
    crisis_list.append([late_for_work_action, late_for_work_weight])

label late_for_work_action_label:
    #Lets get the girl of interest.
    $ the_person = get_random_from_list(mc.business.get_employee_list())

    "As you are walking through the main corridor you spot [the_person.possessive_title] rushing through the entrance doors."
    
    if the_person.sluttiness > 20:
        $ the_person.cum_on_tits()
        $ the_person.draw_person(position="stand3", emotion="default")
        the_person.char "I'm sorry [the_person.mc_title], my boyfriend needed some personal attention when he dropped me off at the office."
        $ upper_clothing = the_person.outfit.get_upper_ordered()[-1]
        menu:
            "Lecture Her On Being Late":
                $ the_person.draw_person(emotion = 'sad')
                mc.name "Do you know what time we start here [the_person.title]?"
                the_person.char "I am really sorry [the_person.mc_title]."
                if (upper_clothing):
                    mc.name "I don't care, next time be on time and cleanup your [upper_clothing.name]"
                else:
                    mc.name "I don't care, next time be on time and make your tits presentable."
                $ the_person.change_obedience(3)
                $ the_person.change_happiness(-2)

            "Let it slide":
                $ the_person.draw_person(emotion = 'happy')
                if (upper_clothing):
                    mc.name "Well at least cleanup your [upper_clothing.name], before you start."
                else:
                    mc.name "At least get that cum of your tits, before you go to work."
                the_person.char "Thank you, [the_person.mc_title]!"
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(2)

        $ the_person.draw_person(position = 'walking_away')
        "[the_person.possessive_title] rushes to the ladies room to cleanup."

    elif the_person.sluttiness > 40:
        $ the_person.cum_on_face()
        $ the_person.cum_on_tits()
        $ the_person.draw_person(position="stand3", emotion="default")
        the_person.char "Sorry [the_person.mc_title], a client caught me in the parking lot and wanted to have a business meeting in his car. You can let marketing know I made the sale."
        mc.name "Well, it sure does look like it was a productive meeting. Go clean yourself up before you get back to work. I don't want you dripping that all over the building."
        if the_person.get_opinion_score("cum facials") > 0:
            the_person.char "Aww. But I like the way it feels."
        elif the_person.get_opinion_score("cum facials") < 0:
            the_person.char "Definitly, I hate feeling all sticky."
        else:
            the_person.char "Of Course [the_person.mc_title]."
        
        $ the_person.draw_person(position = 'walking_away')
        "The client wires the money to your company account, but must have forgot to actually placed an order."
        $ mc.business.funds += 250

    else:
        $ the_person.draw_person(position="stand3", emotion="default")
        menu:
            "Lecture Her On Being Late":
                $ the_person.draw_person(emotion = 'sad')
                mc.name "Do you know what time we start here [the_person.title]?"
                the_person.char "Sorry [the_person.mc_title], I missed my bus."
                mc.name "I don't care what you have to do, but I need you to be here on time. Now get going..."
                $ the_person.change_obedience(3)
                $ the_person.change_happiness(-2)

            "Let it slide":
                $ the_person.draw_person(emotion = 'happy')
                mc.name "Well, ok, now quickly run along [the_person.title]."
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(2)

        $ the_person.draw_person(position = 'walking_away')
        "[the_person.possessive_title] quietly rushes to her desk."
    
    $ the_person.clear_scene()
    return
