# This file is used to define the functions and actions needed for a new clarity based character menu
# Screen is in a different file

init -2 python:
    def persuade_person_requirement(the_person):
        if mc.free_clarity < 500:
            return "Requires: 500+ Free Clarity"
        else:
            return True

    def clarity_train_int_requirement(the_person):
        if the_person.int >= mc.int:
            return "Requires: Higher MC Intelligence"
        elif the_person.int >= 7:
            return "Intelligence maximum reached"
        elif mc.free_clarity < (the_person.int * 500):
            return "Requires: {} Free Clarity".format(the_person.int * 500)
        else:
            return True

    def clarity_train_cha_requirement(the_person):
        if the_person.charisma >= mc.charisma:
            return "Requires: Higher MC Charisma"
        elif the_person.charisma >= 7:
            return "Charisma maximum reached"
        elif mc.free_clarity < (the_person.charisma * 500):
            return "Requires: {} Free Clarity".format(the_person.charisma * 500)
        else:
            return True

    def clarity_train_focus_requirement(the_person):
        if the_person.focus >= mc.focus:
            return "Requires: Higher MC Focus"
        elif the_person.focus >= 7:
            return "Focus maximum reached"
        elif mc.free_clarity < (the_person.focus * 500):
            return "Requires: {} Free Clarity".format(the_person.charisma * 500)
        else:
            return True

    def clarity_serum_dose_requirement(the_person):
        if len(the_person.serum_effects) >= the_person.serum_tolerance:
            return "Already at Serum Limit"
        if mc.free_clarity < 500:
            return "Requires: 500 Free Clarity"
        return True


    def build_clarity_person_actions_menu(the_person):
        clarity_train_int_action = Action("Train her Intelligence", requirement = clarity_train_int_requirement, effect = "clarity_train_int", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to increase her intelligence score.", priority = -5)
        clarity_train_cha_action = Action("Train her Charisma", requirement = clarity_train_cha_requirement, effect = "clarity_train_cha", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to increase her charisma score.", priority = -5)
        clarity_train_focus_action = Action("Train her Focus", requirement = clarity_train_focus_requirement, effect = "clarity_train_focus", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to increase her focus score.", priority = -5)
        clarity_serum_dose_action = Action("Persuade her to test a serum", requirement = clarity_serum_dose_requirement, effect = "clarity_serum_dose", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to convince her to test a serum.", priority = -5)

        return ["Persuade", clarity_train_int_action, clarity_train_cha_action, clarity_train_focus_action , clarity_serum_dose_action, ["Never mind", "Return"]]


label persuade_person(the_person):
    mc.name "[the_person.title], I was hoping you would do something for me."
    the_person "Yes [the_person.mc_title]?"

    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items([build_clarity_person_actions_menu(the_person)]))
    else:
        call screen main_choice_display([build_clarity_person_actions_menu(the_person)])

    if isinstance(_return, Action):
        $ _return.call_action()
    return

label clarity_train_int(the_person):
    mc.name "I was hoping we could have some one on one time. I came across a few things I thought you might appreciate."
    the_person "I suppose we could do that."
    $ the_person.draw_person(position = "sitting")
    "You sit down with [the_person.possessive_title]. You spend a few hours chatting about recent advances in science and the scientific method."
    $ mc.spend_clarity(the_person.int * 500)
    $ the_person.change_int(1)
    the_person "Thank you [the_person.mc_title], that was very educational!"

    call advance_time from _call_advance_clarity_int_01
    return "Advance Time"

label clarity_train_cha(the_person):
    mc.name "Hey, did you hear the latest rumors?."
    the_person "No, I haven't."
    mc.name "Ah, have a bit that I could fill you in?"
    the_person "I suppose we could do that."
    $ the_person.draw_person(position = "sitting")
    "You sit down with [the_person.possessive_title]. You spend a few hours chatting about the latest rumors and gossip."
    $ mc.spend_clarity(the_person.charisma * 500)
    $ the_person.change_cha(1)
    the_person "Thank you [the_person.mc_title], that was very educational!"
    call advance_time from _call_advance_clarity_cha_01
    return "Advance Time"

label clarity_train_focus(the_person):
    mc.name "Hey, are you busy? I was thinking about doing some meditation, and I thought you might want to join me."
    the_person "I didn't realize you did that. Sure I'd love to join you."
    $ the_person.draw_person(position = "sitting")
    "You sit down with [the_person.possessive_title]. You spend a few hours chatting about the latest rumors and gossip."
    $ mc.spend_clarity(the_person.focus * 500)
    $ the_person.change_focus(1)
    the_person "Thank you [the_person.mc_title]. I feel like I can really focus on the rest of my day now!"
    call advance_time from _call_advance_clarity_focus_01
    return "Advance Time"

label clarity_serum_dose(the_person):
    mc.name "Hey, could you do me a huge favor?"
    the_person "Maybe... what is it?"
    if the_person.is_employee():
        mc.name "[the_person.title], there's a serum design that is in need of a test subject. Would you be interested in helping out with a quick field study?"
        the_person "I'll admit I'm curious what it would do to me. Okay, as long as it's already passed the safety test requirements, of course."
    else:
        mc.name "[the_person.title], I've got a project going on at work that could really use a test subject. Would you be interested in helping me out?"
        the_person "I'd be happy to help, as long as you promise it's not dangerous of course. I've always wanted to be a proper scientist!"

    mc.name "It's completely safe, we just need to test what the results from it will be. Thank you."
    $ mc.spend_clarity(500)
    call give_serum(the_person) from _call_clarity_serum_dose_01
    return
