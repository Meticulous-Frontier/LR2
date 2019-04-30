## Business Meeting Crisis Mod by Tristimdorion
init -1 python:
    business_meeting_weight = 5

init 2 python:
    def business_lunchcrisis_requirement():
        if not mc.business.is_weekend(): 
            if time_of_day > 1 or time_of_day < 4: # only during morning afternoon or evening
                return True
        return False

    business_lunchcrisis = Mod("Business Meeting Crisis", business_lunchcrisis_requirement, "business_meeting_action_description",
        menu_tooltip = "An employee wants to discuss some business with you.", category = "Business")
    crisis_list.append([business_lunchcrisis.action, business_meeting_weight])

label business_meeting_action_description:
    call business_meeting_action from _call_business_meeting_action_1
    return
    
label business_meeting_action:
    $ the_person = get_random_from_list(mc.business.get_employee_list())
    $ the_place = mc.business.get_employee_workstation(the_person)
    $ day_part = time_of_day_string()

    if (mc.location ==  the_place):
        "You're hard at work in the [day_part], when [the_person.name] asks you over to discuss some plans."
    else:
        "You're hard at work in the [day_part], when [the_person.name] calls you on your phone to discuss some plans."

    "You meet up in an empty office of the [the_place.name] department."

    $ change_scene_display(the_place)
    $ the_person.draw_person(position="sitting", emotion="happy")
    show screen person_info_ui(the_person)

    call business_meeting_introduction(the_person) from _call_business_meeting_introduction_1
    call business_meeting_flirtation(the_person) from _call_business_meeting_flirtation_1
    call business_meeting_arrousal(the_person) from _call_business_meeting_arrousal_1
    call business_meeting_seduction(the_person) from _call_business_meeting_seduction_1
    call business_meeting_end(the_person) from _call_business_meeting_end_1

    hide screen person_info_ui
    $ the_person.reset_arousal()
    $ the_person.reset_outfit() #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return

label business_meeting_introduction(person):
    if person.obedience > 140:
        person.char "Hello Sir, thank you for meeting me on such short notice."
    else:
        person.char "Hi [mc.name], thank you for the meeting."
    return

label business_meeting_flirtation(person):
    if person.sluttiness > 10:
        pass
    return

label business_meeting_arrousal(person):
    if person.sluttiness > 20:
        pass
    return


label business_meeting_seduction(person):
    if person.sluttiness > 40:
        pass
    return

label business_meeting_end(person):
    if person.obedience > 140:
        the_person.char "Thank you for your time, Sir!"
    else:
        the_person.char "Thank you for the meeting."
    return