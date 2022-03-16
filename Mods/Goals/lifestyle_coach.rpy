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
        if person.location is not mall:
            return "Only at the mall"
        else:
            return "Only during business hours"
        return False

    def lifestyle_coach_choose_sexy_goal_requirement(the_person):
        if the_person.sluttiness > 40 and mc.energy > 80 and the_person.energy > 80:
            if the_person.location == mall:
                return True
        return False

    lifestyle_coach_review_goals = Action("Review Goals", lifestyle_coach_review_goals_requirement, "lifestyle_coach_review_goals_label")
    lifestyle_coach_role = Role(role_name ="Lifestyle Coach", actions =[lifestyle_coach_review_goals], hidden = True)
    lifestyle_coach_choose_sexy_goal = Action("Choose a Sexy Goal", lifestyle_coach_choose_sexy_goal_requirement, "lifestyle_coach_choose_sexy_goal_label")

    lifestyle_coach_intro = Action("Meet the Lifestyle Coach", lifestyle_coach_intro_requirement, "lifestyle_coach_intro_label")

#init 3 python:
    # def lifestyle_coach_init():
    #     print("Initialize Lifestyle Coach")
    #     dawn_job = Job("Lifestyle Coach", lifestyle_coach_role, mall, work_times = [1,2,3])

    #     global dawn
    #     dawn = make_person(name = "Dawn", age = 42, body_type = "thin_body", \
    #         personality = relaxed_personality, job = dawn_job, \
    #         sex_array = [3,3,4,3], start_obedience = -28, start_happiness = 129, start_love = 0, \
    #         title = "Dawn", possessive_title = "Your lifestyle coach", mc_title = mc.name, force_random = True,
    #         forced_opinions = [
    #             ["HR work", 2, True],
    #         ], forced_sexy_opinions = [
    #             ["taking control", 1, False]
    #         ])

    #     dawn.generate_home()
    #     dawn.home.add_person(dawn)
    #     dawn.event_triggers_dict["met"] = 0
    #     dawn.add_unique_on_room_enter_event(lifestyle_coach_intro)
    #     return

label lifestyle_coach_intro_label(the_person):
    $ scene_manager = Scene()
    "You decide to wander aimlessly around the mall for a bit. You do a bit of people watching and generally enjoy the time to yourself."
    "As you walk around, you spot a kiosk that catches your attention."
    "Lifestyle Coaches: We help you set and achieve long term and short term goals!"
    "You walk around the kiosk a bit, there are all kinds of testimonials and adverts up for the service."
    the_person "Hello there! I'm [the_person.name]."
    $ scene_manager.add_actor(the_person)
    mc.name "I'm [mc.name]."
    $ the_person.set_title(the_person.name)
    $ the_person.set_possessive_title("Your lifestyle coach")
    $ the_person.set_mc_title(mc.name)
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
    $ the_person.event_triggers_dict["met"] = 1
    $ scene_manager.clear_scene()
    if the_person == camilla:
        $ camilla.add_unique_on_room_enter_event(camilla_spot_at_bar)
    return

label lifestyle_coach_review_goals_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    $ mc.business.change_funds(-20)
    mc.name "Hey [the_person.title]. Do you have time to talk about goals again?"
    the_person "Certainly! Tell me about how things are going and what you would like to change."
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    mc.name "Thanks for the help!"
    $ scene_manager.clear_scene()
    if not perk_system.has_ability_perk("Tits Man"):
        $ the_person.add_unique_on_room_enter_event(lifestyle_coach_choose_sexy_goal)
    return

label lifestyle_coach_choose_sexy_goal_label(the_person):
    $ the_person.draw_person()
    $ perk_choice = None
    "You step up to [the_person.possessive_title]. She smiles as you approach her."
    the_person "Hey [the_person.mc_title] here to review your goals?"
    "You do want to... but you find yourself faltering for a second."
    "Setting goals, both long term and short term is important... but what really are your goals, anyway?"
    mc.name "I think so, but to be honest, I'm having trouble deciding what I even want."
    the_person "I see. Well, an exercise that might help. Let's pretend like money wasn't an obstacle. If you could do anything you wanted to right now, what would you do?"
    "You look at [the_person.possessive_title]. You think about the question for a moment... but soon your eyes drift down from her face..."
    "Her chest... her belly... her hips..."
    $ mc.change_locked_clarity(10)
    "You close your eyes."
    "Try as you might, you can't get images of her sexy body out of your head."
    the_person "That's it. Visualize what you want. What drives you? What get's you out of bed every morning? Your endgame?"
    "Try as you might, you can't get the women in your life out of your brain. Maybe... all the money... the company... is really all about?"
    "Having the women in your life serve your needs, physically, emotionally, sexually..."
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(30)
    "Maybe it is time to just embrace it. There's nothing wrong with that, right? Any guy in your position would do the same thing."
    "You open your eyes and look at [the_person.possessive_title]. You eyes are immediately drawn to her..."
    menu:
        "Tits":
            $ perk_choice = "Tits"
        "Hips (disabled)":
            $ perk_choice = "Ass"
    the_person "That's it. Can you envision your goal, [the_person.mc_title]?"
    if perk_choice == "Tits":
        "You look down at [the_person.title]'s ample chest. You can imagine your cock sliding between them, her smooth flesh caressing you."
        $ the_person.change_obedience(3)
        mc.name "I can envision it... and I can almost feel it."
        "She gasps when she realizes you are staring right at her chest."
        #TODO increase her sluttiness with new sluttiness score.
        mc.name "[the_person.title]... would you follow me to someplace more private?"
        the_person "Oh my... I suppose..."
        "You quickly duck into a side hall and find a family restroom, she joins you inside and you lock the door."
        mc.name "Take your top off."
        "You don't give her a choice in the matter, but she quickly complies."
        $ the_person.strip_outfit(exclude_lower = True)
        mc.name "I want to feel my cock between your tits, and I'm not taking no for an answer."
        the_person "Then I suppose it's a good thing I don't want to say no!"
        $ the_person.draw_person(position = "blowjob")
        "[the_person.title] gets on her knees and puts her tits between her hands. She looks up into your eyes as your cock slowly slides between them."
        "Yeah, this feels amazing. You know in your head, this is exactly what you goals are. To have women serve you, fuck you, make you cum."
        "You can't wait to cum all over her incredible tits."
        call get_fucked(the_person, the_goal = "body shot", private= True, start_position = tit_fuck, skip_intro = True, allow_continue = False) from _life_coach_tit_fuck_01
        the_person "Oh my god... that was so hot..."
        $ the_person.draw_person(position = the_person.idle_pose)
        "[the_person.title] stands up, her tits coated in your cum."
        "It felt amazing, but something also felt different."
        "You made the decision to just let yourself go, enjoy the moment, and cover her tits in cum."
        "Normally you feel like you would find yourself wishing you could have cum inside her somewhere, but this time... it doesn't matter."
        "What matters was that she did it willingly, happy to serve you and your needs, however you told her to."
        "You decide that in the future, you'll be open to cumming all over a girl's fun bags whenever the mood strikes you."
        $ tits_man_perk_unlock()
        "You have unlocked the perk 'Tits Man'! You now have the same clarity multiplier for cumming on tits as you do for creampies!"
        the_person "I'm going to get cleaned up... you should probably slip out when can..."
        mc.name "I'll do that. Thanks for the help, [the_person.title]."
        $ clear_scene()
        $ the_person.apply_planned_outfit()
        "You quietly exit the bathroom and go about your day."

    return
