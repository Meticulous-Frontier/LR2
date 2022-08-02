# Stephanie story add ons.
init 5 python:
    add_label_hijack("normal_start", "activate_head_researcher_role_enhancement")
    add_label_hijack("after_load", "activate_head_researcher_role_enhancement")

label activate_head_researcher_role_enhancement(stack):
    python:
        head_researcher.add_action(head_researcher_serum_trait_test)
        if not mc.business.event_triggers_dict.get("testing_room_policy_avail",0) == 1:
            mc.business.add_mandatory_crisis(head_researcher_suggest_testing_room)
        execute_hijack_call(stack)
    return

init 1400 python:
    def testing_room_creation_requirement():
        if mc.business.event_triggers_dict.get("testing_room_policy_avail",0) == 1:
            return True
        return "Story Progression"

    def testing_room_policy_unlock(unlock):
        mc.business.event_triggers_dict["testing_room_policy_unlock"] = unlock

    testing_room_creation_policy = Policy(name = "Serum Testing Room",
        desc = "Some medical equipment, a couple windows, and a privacy curtain creates an ideal place to test specific serum traits.",
        cost = 1000,
        requirement =  testing_room_creation_requirement,
        on_buy_function = testing_room_policy_unlock,
        extra_arguments = { "unlock" : 1})
    serum_policies_list.insert(9, testing_room_creation_policy)

#Requirement Functions
init -1 python:
    def head_researcher_suggest_testing_room_requirement():
        if mc.business.research_tier >= 1:
            if mc.business.days_since_event("tier_1_serum_unlock_day") > TIER_2_TIME_DELAY:
                if mc.is_at_work() and mc.business.is_open_for_business():
                    return True
        return False

    def head_researcher_testing_room_intro_requirement(the_person):
        return False

    def head_researcher_serum_trait_test_requirement(the_person):
        if testing_room_creation_policy.is_active():
            if mc.business.days_since_event("serum_trait_test") > TIER_1_TIME_DELAY:
                return True
            else:
                return "Tested serum too recently"
        return False

#Action definitions
    head_researcher_suggest_testing_room = Action("Testing room reuqest", head_researcher_suggest_testing_room_requirement, "head_researcher_suggest_testing_room_label")
    head_researcher_testing_room_intro = Action("Testing Room Intro", head_researcher_testing_room_intro_requirement, "head_researcher_testing_room_intro_label")
    head_researcher_serum_trait_test = Action("Test a Serum Trait", head_researcher_serum_trait_test_requirement, "head_researcher_serum_trait_test_label",
        menu_tooltip = "Perform intensive serum trait test with the help of your head researcher on an employee.")

label head_researcher_suggest_testing_room_label():
    if mc.business.event_triggers_dict.get("testing_room_policy_avail",0) == 1: #We've already run this event.
        return
    $ the_person = mc.business.head_researcher
    if mc.location == mc.business.r_div:
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! Can you meet me down in the lab?"
        mc.name "Sure"
        $ mc.end_text_convo()
        "You walk down to the lab."
        $ mc.change_location(mc.business.r_div)
        $ mc.location.show_background()
    $ the_person.draw_person()
    the_person "Hey! Thanks for coming. I wanted to show you something really quick."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and starts to walk to the far end of the lab. You follow her."
    "When she gets there, she opens a side door and goes down a short hallway, and at the end is a small room, with another small room adjacent room."
    "The two rooms are currently sitting completely unused."
    $ the_person.draw_person()
    the_person "I was thinking about what you said, about testing for changes based on orgasms and interactions with our serums."
    the_person "But the problem is... we don't really have a good place to run the tests at. The lab is great, but it is so open."
    the_person "It might make things uncomfortable and skew results."
    mc.name "You're right."
    the_person "Anyway, I found these two old rooms, that I thought would make a good serum testing site. We could set up a medical exam bed here, and install a window between the two rooms."
    the_person "That way we can research serum effects in a more clinical environment."
    mc.name "That's a great idea. How much would it run?"
    the_person "I priced out some basic medical equipment. A bed, some monitors, etc. I think it could be done for about $1000."
    mc.name "That seems pretty reasonable."
    the_person "Yeah, then we could bring employees here to help test serums once in a while. It would be very handy for newly created traits specifically."
    if mandatory_paid_serum_testing_policy.is_active():
        the_person "With the mandatory testing policy, we'd be able to test it on just about anyone, really."
    else:
        the_person "You might want to consider some type of mandatory testing policy though... for now we would just need to rely on volunteers."
    mc.name "This is a good idea. I'll add it to the to do list, though I can't promise when I'll get around to arranging it."
    the_person "Okay! Thanks for hearing me out."
    $ clear_scene()
    "[the_person.possessive_title] leaves you alone in the small room. A policy has been added to create a designated serum testing room."
    "Once unlocked, you will be able to test and observe the results of serum traits there with your head researcher."
    $ mc.business.event_triggers_dict["testing_room_policy_avail"] = 1
    $ the_person.add_unique_on_room_enter_event(head_researcher_testing_room_intro)
    return

label head_researcher_testing_room_intro_label(the_person):
    "In this label, we go with the head researcher to the new serum testing room, where we introduce the idea of an intensive serum trait test."
    $ mc.business.set_event_day("serum_trait_test", override = True)
    return

label head_researcher_serum_trait_test_label(the_person):
    "In this label, we test a serum on a someone with the help of the head researcher."
    $ mc.business.set_event_day("serum_trait_test", override = True)
    return
