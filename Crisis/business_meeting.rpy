## Business Meeting Crisis Mod by Tristimdorion
init -1 python:
    business_meeting_weight = 5

init 2 python:
    def business_meeting_requirement():
        if not mc.business.is_weekend():
            if mc.is_at_work():
                if time_of_day > 1 and time_of_day < 4: # only during morning afternoon or evening
                    return True
        return False

    business_meeting_action = ActionMod("Business Meeting Crisis", business_meeting_requirement, "business_meeting_action_description",
        menu_tooltip = "An employee wants to discuss some business with you.", category = "Business")
    crisis_list.append([business_meeting_action, business_meeting_weight])

label business_meeting_action_description:
    call business_meeting_action from _call_business_meeting_action_1
    return
    
label business_meeting_action:
    $ the_person = get_random_from_list(mc.business.get_employee_list())
    $ the_place = mc.business.get_employee_workstation(the_person)
    $ day_part = time_of_day_string()

    if (mc.location ==  the_place):
        "You're hard at work in the [day_part], when [the_person.possessive_title] asks you over to discuss some plans."
    else:
        "You're hard at work in the [day_part], when [the_person.possessive_title] calls you on your phone to discuss some plans."

    "You meet up in an empty office of the [the_place.name] department."

    $ change_scene_display(the_place)
    $ the_person.draw_person(position="sitting", emotion="happy")
    show screen person_info_ui(the_person)

    call business_meeting_introduction(the_person) from _call_business_meeting_introduction_1
    call business_meeting_flirtation(the_person) from _call_business_meeting_flirtation_1
    if (the_person.sluttiness > 25):
        call business_meeting_arrousal(the_person) from _call_business_meeting_arrousal_1
        if (the_person.sluttiness > 40):
            call business_meeting_seduction(the_person) from _call_business_meeting_seduction_1
        else:
            $ the_person.change_happiness(5)
            "After a while [the_person.title] wraps up her story."
    else:
        $ the_person.change_happiness(5)
        "[the_person.title] finishes up her proposal."

    $ the_person.wear_uniform() #Make sure to reset her outfit so she is dressed properly.

    call business_meeting_end(the_person) from _call_business_meeting_end_1

    $ improvement_chance = renpy.random.randint(0, 100)
    if improvement_chance < 40:
        $ hr_employee = get_random_from_list(mc.business.hr_team)
        if hr_employee == the_person:
            "You give [the_person.title] a call and tell her that she can implement the changes you discussed."
        else:
            "You make a call to [hr_employee.title] from HR to implement some of the changes you discussed with [the_person.title]"
        $ mc.business.team_effectiveness += 1
        $ mc.log_event("Company Efficiency: " + str(mc.business.team_effectiveness) + "%", "float_text_grey")
        "The changes incease your business effectivity by one percent."

    hide screen person_info_ui
    $ the_person.reset_arousal()
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return

label business_meeting_introduction(person):
    if person.obedience > 140:
        person.char "Hello Sir, thank you for meeting me on such short notice."
    else:
        person.char "Hi [person.mc_title], thank you for the meeting."
    return

label business_meeting_flirtation(person):
    person.char "Thank you for taking the time to listen to my proposal....."
    if person.sluttiness > 15:
        $ feet = person.outfit.remove_random_feet(top_layer_first = True, do_not_remove = True)
        if feet:
            $ person.outfit.remove_clothing(feet)
            $ person.draw_person(position="sitting")
        "While talking about her new business plan, you suddenly feel her bare foot moving up and down your leg."
    else:
        "You mind wanders off while she is talking..."
    return

label business_meeting_arrousal(person):
    if person.sluttiness > 30:
        "She moves up to your crotch and unzips your pants with her feet, sliding with her foot over you growing bulge."
        if person.obedience > 140:
            person.char "Sir, it seems you need some personal attention."
        else:
            person.char "Oh my [person.mc_title], it seems my proposal got you all exited."
    else:
        if person.obedience > 140:
            person.char "Perhaps we should continue this another time, Sir?"
        else:
            person.char "Perhaps we could discuss this matter in a more private setting?"
    return


label business_meeting_seduction(person):
    if person.sluttiness > 50:
        $ top_clothing = person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
        if top_clothing:
            "After talking for a while she takes off her [top_clothing.name]."
            $ person.outfit.remove_clothing(top_clothing)
            $ person.draw_person(position="sitting")            
            person.char "This should help you focus, [person.mc_title]."
            "You can't help but admire [person.possessive_title] boldness."

        person.char "I'm sorry, it seems i've dropped something..."
        "[person.possessive_title] slides under the table grabbing your now exposed cock looking up at you with a smile."
        $ person.change_arousal(25)
        menu:
            "Continue" if  mc.current_stamina > 0:
                call fuck_person(person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True) from _call_fuck_person_business_meeting
            "Continue. (disabled)" if not mc.current_stamina > 0:
                pass
            "Not now":
                mc.name "I'm sorry [person.possessive_title], i've got another meeting to attend."
                $ person.change_happiness(-5)
    else:
        "After while [person.title] stops rubbing your exposed member."
        person.char "I see you have some other business to take care off."
    return

label business_meeting_end(person):
    if person.obedience > 140:
        if person.sluttiness < 40:
            person.char "Thank you for your time, Sir!"
        else:
            person.char "Thank you, Sir, I'm always happy to serve you or the business!"
    else:
        if person.sluttiness < 40:
            person.char "Thank you for the meeting, [person.mc_title]!"
        else:
            person.char "Thank you for giving me the personal attention I needed, [person.mc_title]!"


    if person.sluttiness < 40:
        "You thank [person.title] for her time and that you will look into the matter."
    else:
        mc.name "You did well [person.title], this was very productive and relaxing."

    $ the_person.draw_person(position="walking_away")

    if person.sluttiness < 40:
        "You watch her walking away, deciding what to do next." 
    else:
        "After contemplating what just happend, you decide what to do next."
    return
