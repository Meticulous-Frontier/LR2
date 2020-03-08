#This file is for the lifestyle coach. A new minor unique characte who can help coach the MC to meet new life goals.
#Found at the mall. Initially can help MC setup new work and personal goals, after corruption can help setup new sex goals and help meet them.
init -2 python:
    MIN_GOAL_LiST_LENGTH = 2  #This determines the smallest length allowed for the goal list length.



init 3 python:
    def lifestyle_coach_goal_dump(): #This function adds all new goals to the modded list when the player opts out of the lifestyle coach portion of the mod.
        sex_goals.append(ass_cum_goal)
        sex_goals.append(threesome_goal)
        stat_goals.append(daily_profit_goal)
        stat_goals.append(side_money_goal)
        work_goals.append(HR_interview_goal)


    def lifestyle_coach_init():
        dawn_home = Room("Dawn's home", "Dawn's home", [], apartment_background, [],[],[],False,[0,0], visible = False, hide_in_known_house_map = False, lighting_conditions = standard_indoor_lighting)
        dawn_home.add_object(make_wall())
        dawn_home.add_object(make_floor())
        dawn_home.add_object(make_bed())
        dawn_home.add_object(make_window())

        list_of_places.append(dawn_home)

        lifestyle_coach_review_goals = Action("Review Goals", lifestyle_coach_review_goals_requirement, "lifestyle_coach_review_goals_label")

        lifestyle_coach_role = Role(role_name ="Lifestyle Coach", actions =[lifestyle_coach_review_goals], hidden = False)

        global dawn
        dawn = create_random_person(name = "Dawn", age = 42, body_type = "thin_body", \
            personality = relaxed_personality, \
            sex_array = [3,3,4,3], start_obedience = -28, start_happiness = 129, start_love = 0, \
            title = "Dawn", possessive_title = "Your lifestyle coach", mc_title = mc.name)

        dawn.special_role.append(lifestyle_coach_role)

        dawn.set_schedule([0,4], dawn_home)
        dawn.set_schedule([1,2,3], mall)
        dawn.home = dawn_home

        dawn.home.add_person(dawn)


        #Set opinions up here.
        dawn.opinions["HR work"] = [2, True]
        dawn.sexy_opinions["taking control"] = [1, False]


        lifestyle_coach_intro = Action("Meet the Lifestyle Coach", lifestyle_coach_intro_requirement, "lifestyle_coach_intro_label")
        dawn.on_room_enter_event_list.append(lifestyle_coach_intro)

        # Get default goals list
        global work_goals_options_list
        global sex_goals_options_list
        global stat_goals_options_list

        stat_goals_options_list = stat_goals.copy()
        work_goals_options_list = work_goals.copy()
        sex_goals_options_list = sex_goals.copy()

        # Add modded goals.

        stat_goals_options_list.append(daily_profit_goal)
        stat_goals_options_list.append(side_money_goal)
        work_goals_options_list.append(HR_interview_goal)
        sex_goals_options_list.append(ass_cum_goal)
        sex_goals_options_list.append(threesome_goal)

        return

init 2 python:
    def lifestyle_coach_intro_requirement(the_person):
        if the_person.location() is mall: # only trigger event when Dawn at mall
            return True
        return False

    def lifestyle_coach_review_goals_requirement(the_person):
        if mc.location == mall:
            return True
        else:
            return "Wait until she is working to ask about that!"
        return False

init 4 python:
    def toggle_goal_avail(the_goal):
        if the_goal in stat_goals_options_list: #is a stat goal
            if the_goal in stat_goals:  #Attempt to remove it
                if len(stat_goals) > MIN_GOAL_LiST_LENGTH:  #The length is big enough we can remove one
                    stat_goals.remove(the_goal)
            else: # Add it
                stat_goals.append(the_goal)
        elif the_goal in work_goals_options_list: #is a work goal
            if the_goal in work_goals:
                if len(work_goals) > MIN_GOAL_LiST_LENGTH:
                    work_goals.remove(the_goal)
            else:
                work_goals.append(the_goal)
        elif the_goal in sex_goals_options_list: #is a sex goal
            if the_goal in sex_goals:
                if len(sex_goals) > MIN_GOAL_LiST_LENGTH:
                    sex_goals.remove(the_goal)
            else:
                sex_goals.append(the_goal)
        else:
            pass  #Possibly add some debug stuff here, becuase this shouldn't reach this point
            renpy.say("","goal toggle failed.") #Where are we right now?
            return
        return

label lifestyle_coach_intro_label(the_person):
    $ scene_manager = Scene()
    "You decide to wander aimlessly around the mall for a bit. You do a bit of people watching and generally enjoy the time to yourself."
    "As you walk around, you spot a kiosk that catches your attention."
    "Lifestyle Coaches: We help you set and achievement long term and short term goals!"
    "You walk around the kiosk a bit, there are all kinds of testimonials and adverts up for the service."
    the_person.char "Hello there! I'm [the_person.title]."
    $ scene_manager.add_actor(the_person)
    mc.name "I'm [mc.name]."
    the_person.char "Nice to meet you! I'm a lifestyle coach, here to help people achieve their dreams!"
    "The sales pitch is a little... optimistic? But to be honest, she is pretty good looking, so you decide to let her continue."
    the_person.char "I've personally helped all kinds of people achieve all kinds of things, from giving up drugs, to losing a few pounds!"
    the_person.char "Our first consultation is free. Would you be interested?"
    "What the hell. It couldn't hurt anything, right?"
    mc.name "I suppose."
    "You sit down with [the_person.title]. She asks you some generic questions about your personal and work life."
    "You explain that you are a small business owner, working with pharmaceuticals, leaving out some of the details."
    "You share some of your basic short term, and a few long term goals, both for your business and for yourself, personally."
    the_person.char "I see. Those sound like interesting goals! Might I offer a few alternatives also?"
    mc.name "Sure."
    #TODO call the screen for the goal system.
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    the_person.char "I hope that was helpful! Come back again and see me if you want to adjust your goals again in the future!"
    mc.name "I think it was. I'll be sure to check back with you again if I need to. Thanks!"
    return

label lifestyle_coach_review_goals_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "I was wondering, do you have time to talk about goals again?"
    the_person.char "Certainly! Tell me about how things are going and what you would like to change."
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    mc.name "Thanks for the help!"
    return

label test_goal_screen():
    call screen lifestyle_goal_sheet(the_person)
    return


# label toggle_goal_avail(the_goal):
#     python:
#         if the_goal in stat_goals_options_list: #is a stat goal
#             if the_goal in stat_goals:  #Attempt to remove it
#                 if len(stat_goals) > MIN_GOAL_LiST_LENGTH:  #The length is big enough we can remove one
#                     stat_goals.remove(the_goal)
#             else: # Add it
#                 stat_goals.append(the_goal)
#         elif the_goal in work_goals_options_list: #is a work goal
#             if the_goal in work_goals:
#                 if len(work_goals) > MIN_GOAL_LiST_LENGTH:
#                     work_goals.remove(the_goal)
#             else:
#                 work_goals.append(the_goal)
#         elif the_goal in sex_goals_options_list: #is a sex goal
#             if the_goal in sex_goals:
#                 if len(sex_goals) > MIN_GOAL_LiST_LENGTH:
#                     sex_goals.remove(the_goal)
#             else:
#                 sex_goals.append(the_goal)
#         else:
#             pass  #Possibly add some debug stuff here, becuase this shouldn't reach this point
#             # return False
#     return True
