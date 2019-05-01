## Business Meeting Crisis Mod by Tristimdorion
init -1 python:
    business_meeting_weight = 5

init 2 python:
    def business_lunchcrisis_requirement():
        if not mc.business.is_weekend(): 
            if time_of_day > 1 and time_of_day < 4: # only during morning afternoon or evening
                return True
        return False

    business_lunchcrisis = ActionMod("Business Meeting Crisis", business_lunchcrisis_requirement, "business_meeting_action_description",
        menu_tooltip = "An employee wants to discuss some business with you.", category = "Business")
    crisis_list.append([business_lunchcrisis, business_meeting_weight])

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
    if (the_person.sluttiness > 20):
        call business_meeting_arrousal(the_person) from _call_business_meeting_arrousal_1
        if (the_person.sluttiness > 40):
            call business_meeting_seduction(the_person) from _call_business_meeting_seduction_1
        else:
            $ the_person.change_happiness(5)
            "After a while she wraps up her story."
    else:
        $ the_person.change_happiness(5)
        "She finishes up her proposal."

    $ the_person.reset_outfit() #Make sure to reset her outfit so she is dressed properly.

    call business_meeting_end(the_person) from _call_business_meeting_end_1

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
    if person.sluttiness > 10:
        "While talking about her new business plan, you suddenly feel her bare foot moving up and down your leg."
    else:
        "You mind wanders off while she is talking..."
    return

label business_meeting_arrousal(person):
    if person.sluttiness > 30:
        "She moves up to your crotch and unzips your pants with her feet."
        person.char "Oh my, it seems my proposal got you all exited."
    else:
        person.char "Perhaps we could continue this 'meeting', when we are in a more private setting?"
    return


label business_meeting_seduction(person):
    if person.sluttiness > 50:
        person.char "I'm sorry, it seems i've dropped something..."
        "She slides under the table grabbing your exposed cock looking up at you with a smile."
        $ person.change_arousal(15)
        menu:
            "Continue" if  mc.current_stamina > 0:
                call fuck_person(person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True) from _call_fuck_person_business_meeting
            "Continue. (disabled)" if not mc.current_stamina > 0:
                pass
            "Not now":
                mc.name "I'm sorry [person.possessive_title], i've got another meeting to attend."
                $ person.change_happiness(-5)
    else:
        "After while she stops rubbing your exposed member."
        person.char "I see you have some other business to take care off."
    return

label business_meeting_end(person):
    if person.obedience > 140:
        person.char "Thank you for your time, Sir!"
    else:
        person.char "Thank you for the meeting."

    if person.sluttiness < 30:
        "You thank [person.name] for her time and that you will look into the matter."
    else:
        mc.name "Thank you [person.possessive_title], this was very illuminating."

    $ the_person.draw_person(position="walking_away")

    if person.sluttiness < 30:
        "You watch her walking away." 
    else:
        "After contemplating what just happend, you go back to work."
    return
