## Business Meeting Crisis Mod by Tristimdorion
init -1 python:
    business_meeting_weight = 5

init 2 python:
    def business_meeting_requirement():
        if not mc.business.is_weekend():
            if mc.is_at_work():
                if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
                    return True
        return False

    def remove_person_shoes(person):
        feet = person.outfit.remove_random_feet(top_layer_first = True, do_not_remove = True)
        if feet:
            person.draw_animated_removal(feet, position="sitting", emotion="default")
        return

    business_meeting_action = ActionMod("Business Meeting", business_meeting_requirement, "business_meeting_action_label",
        menu_tooltip = "An employee wants to discuss some business with you.", category = "Business", is_crisis = True, crisis_weight = business_meeting_weight)

label business_meeting_action_label:
    $ the_person = get_random_employees(1)
    $ the_place = mc.business.get_employee_workstation(the_person)
    $ day_part = time_of_day_string()

    if (mc.location ==  the_place):
        "You're hard at work in the [day_part], when [the_person.possessive_title] asks you over to discuss some plans."
    else:
        "You're hard at work in the [day_part], when [the_person.possessive_title] calls you on your phone to discuss some plans."

    "You meet up in an empty office of the [the_place.name] department."

    $ the_place.show_background()
    $ the_place = None
    $ the_person.draw_person(position="sitting", emotion="happy")

    call business_meeting_introduction(the_person) from _call_business_meeting_introduction_1
    call business_meeting_flirtation(the_person) from _call_business_meeting_flirtation_1
    if the_person.effective_sluttiness() > 25:
        call business_meeting_arrousal(the_person) from _call_business_meeting_arrousal_1
        if (the_person.effective_sluttiness() > 40):
            call business_meeting_seduction(the_person) from _call_business_meeting_seduction_1
        else:
            $ the_person.change_happiness(5)
            "After a while [the_person.title] wraps up her story."
    else:
        $ the_person.change_happiness(5)
        "[the_person.title] finishes up her proposal."

    $ the_person.review_outfit(dialogue = False)

    call business_meeting_end(the_person) from _call_business_meeting_end_1

    $ change = renpy.random.randint(1, 3)
    $ hr_employee = get_random_from_list(mc.business.hr_team)
    if hr_employee == the_person:
        "You give [the_person.title] a call and tell her that she can implement the changes you discussed."
    elif hr_employee is None:
        "You decide to implement the changes you discussed with [the_person.title]."
    else:
        "You make a call to [hr_employee.title] from HR to implement some of the changes you discussed with [the_person.title]."
    $ mc.business.effectiveness_cap += change
    if get_HR_director_tag("business_HR_eff_bonus"):
        $ set_HR_director_tag("business_HR_eff_bonus", get_HR_director_tag("business_HR_eff_bonus") + change)
    #$ mc.log_event("Company Efficiency: " + str(mc.business.effectiveness_cap) + "%", "float_text_grey")
    "The changes increased your business effectivity by [change]%%."

    $ hr_employee = None
    $ the_person.reset_arousal()
    $ mc.location.show_background()
    $ renpy.scene("Active")
    return "Advance Time"

label business_meeting_introduction(the_person):
    the_person.char "Hello [the_person.mc_title], thank you for meeting me on such short notice."
    the_person.char "I have been thinking about some ways to improve the streamlining of the company."
    return

label business_meeting_flirtation(the_person):
    if the_person.effective_sluttiness() > 15:
        $ remove_person_shoes(the_person)
        "While talking about her proposal, you suddenly feel her bare foot moving up and down your leg."
    else:
        "You mind wanders off while she is talking..."
    return

label business_meeting_arrousal(the_person):
    if the_person.effective_sluttiness() > 30:
        "She moves up to your crotch and unzips your pants with her feet, sliding with her foot over you growing bulge."
        $ mc.change_arousal(20)
        the_person.char "Oh my [the_person.mc_title], it seems my proposal got you all exited."
    else:
        the_person.char "She keeps stroking your legs while she talks, making sure you are focussed on her."
    return

label business_meeting_seduction(the_person):
    if the_person.effective_sluttiness() > 40:
        $ strip_choice = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
        if strip_choice:
            "After talking for a while she takes off her [strip_choice.name]."
            $ the_person.draw_animated_removal(strip_choice, position="sitting", emotion="default")
            if the_person.outfit.tits_visible():
                if the_person.has_taboo("bare_tits"):
                    "She hesitates for a second, it seems she forgot she didn't put on a bra today, but after a second she continues without hesitation."
                    $ the_person.break_taboo("bare_tits")
            elif not the_person.outfit.bra_covered():
                if the_person.has_taboo("underwear_nudity"):
                    "She seems nervous at first, but quickly gets used to being in her underwear in front of you."
                    $ the_person.break_taboo("underwear_nudity")

            the_person.char "This should help you focus, [the_person.mc_title]."
            $ mc.change_arousal(20)

        if the_person.effective_sluttiness() > 60:
            "After spending a few more minutes talking she suddenly perks up."
            the_person.char "I'm sorry [the_person.mc_title], it seems i've dropped something..."

            $ mc.change_arousal(10)
            $ the_person.draw_person(position = "blowjob")

            if the_person.has_taboo("touching_penis"):
                the_person.char "Oh my god, that is a big one!"
                mc.name "You can touch it for real, if you want."
                "She wraps her hand around your shaft and rubs it gently."
                the_person.char "Sure thing [the_person.mc_title], it feels nice and warm."
                $ the_person.break_taboo("touching_penis")
            else:
                "[the_person.possessive_title] slides under the table grabbing your now exposed cock looking up at you with a smile."

            $ the_person.change_arousal(25)
            menu:
                "Continue":
                    if the_person.has_taboo("sucking_cock"):
                        "You move your hand to her face, pushing back a hair, slowly moving your hand behind her head pulling her closer to your throbbing cock."
                        "She looks at you with confusion when the tip of your cock moves over her cheek and lips."
                        mc.name "Why don't you give it a lick, you might like the taste."
                        the_person.char "What? I don't know... it looks quite tasty though."
                        "She kisses the tip slowly at first, but soon after she starts moving her tongue along the base of the head."
                        mc.name "Now try sliding into your mouth and sucking on it, like eating a popsicle."
                        "[the_person.possessive_title] only nods slightly and starts to move your member into her mouth."
                        $ the_person.break_taboo("sucking_cock")

                    call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_business_meeting
                "Not now":
                    mc.name "I'm sorry [the_person.title], i've got another meeting to attend."
                    $ the_person.draw_person(position = "stand4", emotion="sad")
                    "[the_person.possessive_title] stands up with a disappointed look on her face."
                    $ the_person.change_happiness(-5)
        else:
            "You can't help but admire [the_person.possessive_title] boldness, while she keeps on talking."
    else:
        "After while [the_person.title] stops rubbing your exposed member."
        the_person.char "I will leave you now, it seems you have some other business to take care off."
    return

label business_meeting_end(the_person):
    if the_person.effective_sluttiness() < 20:
        the_person.char "Thank you for listening to my ideas, [the_person.mc_title]."
    elif the_person.effective_sluttiness() < 40:
        the_person.char "Thank you, [the_person.mc_title], I hope you 'come' to see things my way."
    else:
        the_person.char "Thank you, [the_person.mc_title], I hope you liked my contribution."

    if the_person.effective_sluttiness() < 40:
        "You thank [the_person.title] for her time and that you will look into the matter."
    else:
        mc.name "You did well [the_person.title], this was very productive and relaxing."

    if the_person.effective_sluttiness() > 50:
        "[the_person.possessive_title] puts on her clothes and walks away."

    $ the_person.draw_person(position="walking_away")

    if the_person.effective_sluttiness() < 40:
        "You watch her walking away, deciding what to do next."
    else:
        "After contemplating what just happened, you decide what to do next."
    return
