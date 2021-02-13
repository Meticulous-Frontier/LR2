#This file is for the lifestyle coach. A new minor unique character who can help coach the MC to meet new life goals.
#Found at the mall. Initially can help MC setup new work and personal goals, after corruption can help setup new sex goals and help meet them.
init -1 python:
    def lifestyle_coach_intro_requirement(person):
        if person.location == mall: # only trigger event when Dawn at mall
            return True
        return False

    def lifestyle_coach_review_goals_requirement(person):
        if mc.business.is_open_for_business() and mc.location is mall:
            return True
        else:
            return "Only during work hours"
        return False

    lifestyle_coach_review_goals = Action("Review Goals", lifestyle_coach_review_goals_requirement, "lifestyle_coach_review_goals_label")
    lifestyle_coach_role = Role(role_name ="Lifestyle Coach", actions =[lifestyle_coach_review_goals], hidden = False)

    lifestyle_coach_intro = Action("Meet the Lifestyle Coach", lifestyle_coach_intro_requirement, "lifestyle_coach_intro_label")

init 3 python:
    def lifestyle_coach_init():
        global dawn
        dawn = make_person(name = "Dawn", age = 42, body_type = "thin_body", \
            personality = relaxed_personality,  \
            sex_array = [3,3,4,3], start_obedience = -28, start_happiness = 129, start_love = 0, \
            title = "Dawn", possessive_title = "Your lifestyle coach", mc_title = mc.name, force_random = True,
            forced_opinions = [
                ["HR work", 2, True],
            ], forced_sexy_opinions = [
                ["taking control", 1, False]
            ])

        dawn.generate_home()
        dawn.set_schedule(mall, times = [1,2,3], days = [0, 1, 2, 3, 4])
        dawn.add_role(lifestyle_coach_role)
        dawn.home.add_person(dawn)
        dawn.event_triggers_dict["met"] = 0
        dawn.add_unique_on_room_enter_event(lifestyle_coach_intro)
        return

label lifestyle_coach_intro_label(the_person):
    $ scene_manager = Scene()
    "You decide to wander aimlessly around the mall for a bit. You do a bit of people watching and generally enjoy the time to yourself."
    "As you walk around, you spot a kiosk that catches your attention."
    "Lifestyle Coaches: We help you set and achievement long term and short term goals!"
    "You walk around the kiosk a bit, there are all kinds of testimonials and adverts up for the service."
    the_person "Hello there! I'm [the_person.title]."
    $ scene_manager.add_actor(the_person)
    mc.name "I'm [mc.name]."
    the_person "Nice to meet you! I'm a lifestyle coach, here to help people achieve their dreams!"
    "The sales pitch is a little... optimistic? But to be honest, she is pretty good looking, so you decide to let her continue."
    the_person "I've personally helped all kinds of people achieve all kinds of things, from giving up drugs, to losing a few pounds!"
    the_person "Our first consultation is free. Would you be interested?"
    "What the hell. It couldn't hurt anything, right?"
    mc.name "I suppose."
    "You sit down with [the_person.title]. She asks you some generic questions about your personal and work life."
    "You explain that you are a small business owner, working with pharmaceuticals, leaving out some of the details."
    "You share some of your basic short term, and a few long term goals, both for your business and for yourself, personally."
    the_person "I see. Those sound like interesting goals! Might I offer a few alternatives also?"
    mc.name "Sure."
    #TODO call the screen for the goal system.
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    the_person "I hope that was helpful! Come back again and see me if you want to adjust your goals again in the future!"
    mc.name "I think it was. I'll be sure to check back with you again if I need to. Thanks!"
    $ dawn.event_triggers_dict["met"] = 1
    $ scene_manager.clear_scene()
    return

label lifestyle_coach_review_goals_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "I was wondering, do you have time to talk about goals again?"
    the_person "Certainly! Tell me about how things are going and what you would like to change."
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    mc.name "Thanks for the help!"
    $ scene_manager.clear_scene()
    return
