# ****Sarah profile****
# Personality type: Outgoing, extrovert.
# Background: Childhood friend. Moved away when you were kids but recently moved back to pursue a job that didn't work out. Now selling solar panels door to door, knocks on your door randomly.
#   Has a great HR resume.
#   After first chance meeting, unlocks the HR Supervisor organization policy that unlocks the role and increases maximum company size by 1.
#   After unlocking the policy, the player calls Sarah and hires her.
#   First level corruption:
#   Second level corruption: You catch her stealing breast enhancing serums. Option to forbid her, allow her, or encourage her.
#
#
# Required labels:
# INTRO
# Hire
# Story arc part one: She catches you in the office on Saturday, invites you to bar where she is meeting a friend. Close the bar down with her
# Story arc part two: She comes looking for you at the office on Saturday. Invites you out to drinks with jut her. She winds up at your place.
# Story arc part three: Catch her swiping breast enhancement serums on friday  NOTE: Part three has separate requirements from one and two and could happen before or after either part.
# Following monday, observe the results
# Story part four: Date night, starts with drinks, ends at a strip club
#
# Intro: mandatory event, in the AM knocks on MC home selling solar panels.
# Hiring: mandatory event. Call up Sarah and hire her for the HR position.

init 2 python:
    sarah_strip_pose_list = ["walking_away","back_peek","standing_doggy","stand2","stand3","stand4","stand5", "doggy","kneeling1"]
    sarah_weekend_surprise_action = ActionMod("Sarah's Weekend Surprise",Sarah_weekend_surprise_crisis_requirement,"Sarah_weekend_surprise_crisis_label",
        menu_tooltip = "You find an employee masturbating in an empty storage room.", category = "Business", is_crisis = True, crisis_weight = 7)

    sarah_wardrobe = wardrobe_from_xml("Sarah_Wardrobe")

    def Sarah_mod_initialization(): #Add actionmod as argument#

        sarah_base_outfit = Outfit("Sarah's base accessories")
        the_glasses = modern_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.45,.31,.59,1.0]
        sarah_base_outfit.add_accessory(the_glasses)
        sarah_base_outfit.add_accessory(the_eyeshadow)

        # init Sarah role
        # sarah_role = Role(role_name ="Childhood Friend", actions =[])

        global sarah
        sarah = make_person(name = "Sarah", last_name ="Cooper", age = 21, body_type = "thin_body", face_style = "Face_3", tits = "A", height = 0.90, hair_colour = "brown", hair_style = windswept_hair, skin="white",\
            eyes = "dark blue", personality = Sarah_personality, name_color = "#d62cff", dial_color = "#d62cff", starting_wardrobe = sarah_wardrobe, \
            stat_array = [4,3,3], skill_array = [5,3,2,1,1], sex_array = [1,2,3,1], start_sluttiness = 3, start_obedience = 0, start_happiness = 102, start_love = 3, \
            title = "Sarah", possessive_title = "Your childhood friend",mc_title = mc.name, relationship = "Single", kids = 0, base_outfit = sarah_base_outfit,
            force_random = True, forced_opinions = [
                ["HR work", 2, True],        # she loves HR work
                ["work uniforms", 1, False], # she likes uniforms
                ["Mondays", 1, False],       # she likes mondays, and monday meetings!
                ["working", 1, False],       # a bit of a workaholic
                ["the colour purple", 2, False], #She loves purple!
                ["skirts", 1, False],        #And Skirts
                ["the colour red", -2, False], #She hates red
            ], forced_sexy_opinions = [
                ["taking control", 1, False], # she likes taking control, type A
                ["giving handjobs", 2, False], # Not afraid to get her hands dirty ;)
                ["showing her tits", -2, False], # She hates showing her small tits
            ])

        sarah.generate_home()
        sarah.set_schedule([1,2,3], sarah.home)
        sarah.home.add_person(sarah)

        sarah.event_triggers_dict["epic_tits_progress"] = 0    # 0 = not started, 1 = mandatory event triggered, 2 = tits epic, -1 = convinced her not to do it
        sarah.event_triggers_dict["drinks_out_progress"] = 0   # 0 = not started, 1 = third wheel event complete, 2 = grab drinks complete
        sarah.event_triggers_dict["dating_path"] = False       # False = not started, or doing FWB during story, True = dating her.
        sarah.event_triggers_dict["stripclub_progress"] = 0    # 0 = not complete, 1 = strip club even complete
        sarah.event_triggers_dict["initial_threesome_target"] = None    #this will hold who sarah decides she wants to have a threesome with.
        sarah.event_triggers_dict["threesome_unlock"] = 0     # 0 = not done, 1 = first threesome after event,
        sarah.event_triggers_dict["try_for_baby"] = 0         # 0 = not trying, 1 = trying for baby, 2 = knocked up
        sarah.event_triggers_dict["fertile_start_day"] = -1    #-1 means not fertile, otherwise is the day that she tells MC she is fertile. Using math we can determine if she is fertile in the future.
        sarah.event_triggers_dict["fertile_start_creampie_count"] = -1  #Set this to the total number of creampies she has had at the beginning of her fertile period.
        sarah.event_triggers_dict["favorite_drink"] = "appletini"
        sarah.event_triggers_dict["special_tit_fuck"] = False
        sarah.event_triggers_dict["foreplay_position_filter"] = sarah_foreplay_position_filter
        sarah.event_triggers_dict["oral_position_filter"] = sarah_oral_position_filter
        sarah.event_triggers_dict["vaginal_position_filter"] = sarah_vaginal_position_filter
        sarah.event_triggers_dict["anal_position_filter"] = sarah_anal_position_filter
        sarah.event_triggers_dict["unique_sex_positions"] = sarah_unique_sex_positions

        # add appoint
        office.add_action(HR_director_appointment_action)

        Sarah_intro = Action("Sarah_intro",Sarah_intro_requirement,"Sarah_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.mandatory_crises_list.append(Sarah_intro) #Add the event here so that it pops when the requirements are met.
        return

    def Sarah_reset_vars():
        if sarah.has_large_tits():
            sarah.event_triggers_dict["epic_tits_progress"] = 2
        sarah.event_triggers_dict["drinks_out_progress"] = 0
        sarah.event_triggers_dict["dating_path"] = False
        return

    def get_Sarah_willing_threesome_list():
        target_list = []
        if willing_to_threesome(sarah, mom):
            target_list.append(mom)
        if willing_to_threesome(sarah, lily):
            target_list.append(lily)
        if willing_to_threesome(sarah, starbuck):
            target_list.append(starbuck)
        if willing_to_threesome(sarah, cousin):
            target_list.append(cousin)
        if willing_to_threesome(sarah, aunt):
            target_list.append(aunt)
        if willing_to_threesome(sarah, nora):
            target_list.append(nora)
        for person in mc.business.get_employee_list():
            if not person is sarah and willing_to_threesome(sarah, person):
                target_list.append(person)

        return target_list



init -1 python:
    def Sarah_intro_requirement():
        if day > 2: #Early for testing
            if mc_at_home():
                if time_of_day < 4:
                    return True
        return False

    def Sarah_hire_requirement():
        if HR_director_creation_policy.is_owned():
            return True
        return False

    def Sarah_catch_stealing_requirement():
        if strip_club_is_closed(): #Don't run while the strip club is closed
            return False
        if time_of_day == 3:
            if day%7 == 4:  #friday
                if mc.is_at_work():
                    return True
        return False

    def Sarah_new_tits_requirement():
        if time_of_day == 0:    # triggers right when she comes into office
            if day%7 == 0:  #Monday
                return True
        return False

    def Sarah_epic_tits_requirement():
        if time_of_day == 0:    # triggers right when she comes into office
            if day%7 == 0:  #Monday
                return True
        return False

    def Sarah_third_wheel_requirement():
        if sarah.event_triggers_dict.get("epic_tits_progress", 0) == 1: #Don't run this if epic tits is in progress
            return False
        if time_of_day > 2:
            if sarah.sluttiness > 15:
                if day%7 == 5:  #Saturday
                    if mc.is_at_work():
                        return True
        return False

    def Sarah_get_drinks_requirement():
        if sarah.event_triggers_dict.get("epic_tits_progress", 0) == 1: #Don't run this if epic tits is in progress
            return False
        if time_of_day > 2:
            if sarah.sluttiness > 30:
                if day%7 == 5:  #Saturday
                    if mc.is_at_work():
                        return True
        return False

    def Sarah_stripclub_story_requirement():
        epic_tits_progress = sarah.event_triggers_dict.get("epic_tits_progress", 0)
        if epic_tits_progress < 2 and not epic_tits_progress == -1:  #Don't run until after she has bigger tits of you convinced her not to do it
            return False
        if strip_club_is_closed(): # Don't run while strip club is closed
            return False
        if time_of_day > 2:   #Only in the evening when the strippers are at the club
            if sarah.sluttiness > 50:
                if day%7 == 5:  #Saturday
                    if mc.is_at_work():
                        return True
        return False

    def Sarah_threesome_request_requirement():
        if time_of_day > 2:
            if day%7 == 5:  #Saturday
                if mc.is_at_work():
                    if __builtin__.len(get_Sarah_willing_threesome_list()) >= 3: #at least three choices for who to hook up with.
                        return True
        return False        #Return false while I write the events

    def Sarah_arrange_threesome_requirement(the_person):
        return True

    def Sarah_initial_threesome_requirement():
        if time_of_day > 2:
            if day%7 == 5:  #Saturday
                return True
        return False


    def Sarah_ask_for_baby_requirement():
        if mc_asleep():
            if sarah.event_triggers_dict.get("threesome_unlock", 0) >= 1:
                if sarah.sex_record["Vaginal Creampies"] >= 10:
                    if sarah.has_role(girlfriend_role):
                        return True
        return False

    def Sarah_fertile_period_start_requirement():  #When this returns true, start the fertile period
        if sarah.event_triggers_dict.get("try_for_baby", 0) == 1:
            if Sarah_is_fertile():
                return True
        return False

    def Sarah_fertile_period_end_requirement():     #When this returns true, end the fertile period
        if sarah.event_triggers_dict.get("try_for_baby", 0) == 1:
            if not Sarah_is_fertile():
                return True
        return False

    def Sarah_try_for_baby_dialogue():  #Just a wrapper to make it easier to make if statements for baby making related dialogue
        if sarah.event_triggers_dict.get("try_for_baby", 0) == 1:
            return True
        return False

    def Sarah_is_fertile():
        if sarah.event_triggers_dict.get("try_for_baby", 0) != 1:  #Only fertile if actively trying
            return False
        if sarah.knows_pregnant(): # She won't ask to be bred if she already knows she's pregnant
            return False
        if sarah.event_triggers_dict.get("fertile_start_day", -1) == -1:
            return False
        elif (day - sarah.event_triggers_dict.get("fertile_start_day", -1)) % 28 < 5:   #  Generally fertile for 5 days every 28 days
            return True
        return False

    def Sarah_has_bigger_tits():
        if sarah.event_triggers_dict.get("epic_tits_progress", 0) > 1 or sarah.has_large_tits():
            return True
        return False #Just in case we used serums later


    def Sarah_remove_bra_from_wardrobe(wardrobe):  #Test this function
        for outfit in wardrobe.outfits:
            if outfit.wearing_bra():
                outfit.remove_clothing(outfit.get_bra())
        for outfit in wardrobe.underwear_sets:
            if outfit.wearing_bra():
                outfit.remove_clothing(outfit.get_bra())

    def Sarah_weekend_surprise_crisis_requirement():
        if time_of_day > 1:
            if sarah.event_triggers_dict.get("drinks_out_progress", 0) >= 2:   #You've gotten drinks out with Sarah before.
                if day%7 == 5:  #Saturday
                    if mc.is_at_work():
                        return True
        return False

    def Sarah_unlock_special_tit_fuck_requirement():  #Not an action, but make a requirement to make it easy to test anyway.
        if sarah.get_sex_record_tit_fucks() > 5:
            if not sarah_get_special_titfuck_unlocked():
                return True
        False

    def roll_dart_odds(target = 50, focus_score = 0):
        dart_roll = 0
        ran_num = renpy.random.randint(0,100)
        if target == 50:
            if ran_num < (20 + (focus_score * 4)): #Bullseye!
                dart_roll = 50
            elif ran_num < (50 + (focus_score * 5)): #HIT
                dart_roll = 25
            else:
                dart_roll = renpy.random.randint(1,20)
            pass
        elif target == 25:
            if ran_num < (40 + (focus_score * 4)): #HIT
                dart_roll = 25
            elif ran_num < (50 + (focus_score * 4)): #Bullseye!
                dart_roll = 50
            else:
                dart_roll = renpy.random.randint(1,20)
        else:
            if ran_num < (50 + (focus_score * 4)):
                dart_roll = target
            else:
                dart_roll = renpy.random.randint(1,20)

        renpy.say("", "The dart hits " + str(dart_roll) + "!")
        return dart_roll

    def get_sarah_spend_night_threesome_possibility():
        threesome_wakeup = False
        threesome_partner = None
        if sarah.event_triggers_dict.get("threesome_unlock", 0) == 1 and renpy.random.randint(0,100) < 50:
            if renpy.random.randint(0,100) < 10: #Try lily first
                if willing_to_threesome(the_person, lily):
                    threesome_partner = lily
                    threesome_wakeup = True
                elif willing_to_threesome(the_person, mom):
                    threesome_partner = mom
                    threesome_wakeup = True
            else:
                if willing_to_threesome(the_person, mom):
                    threesome_partner = mom
                    threesome_wakeup = True
                elif willing_to_threesome(the_person, lily):
                    threesome_partner = lily
                    threesome_wakeup = True
        return (threesome_wakeup, threesome_partner)

    def test_bra_function(the_person):
        Sarah_remove_bra_from_wardrobe(the_person.wardrobe)

    def add_sarah_epic_tits_action():
        Sarah_epic_tits_action = Action("Sarah Epic Tits Action", Sarah_epic_tits_requirement, "Sarah_epic_tits_label")
        mc.business.mandatory_crises_list.append(Sarah_epic_tits_action)

    def add_sarah_get_drinks_action():
        Sarah_get_drinks_action = Action("Sarah get drinks",Sarah_get_drinks_requirement,"Sarah_get_drinks_label")
        mc.business.mandatory_crises_list.append(Sarah_get_drinks_action)

    def add_sarah_stripclub_story_action():
        Sarah_stripclub_story_action = Action("Sarah Strip Club",Sarah_stripclub_story_requirement,"Sarah_stripclub_story_label")
        mc.business.mandatory_crises_list.append(Sarah_stripclub_story_action)

    def add_sarah_weekend_surprise_action():
        sarah_weekend_surprise_action = Action("Sarah's Weekend Surprise", Sarah_weekend_surprise_crisis_requirement, "Sarah_weekend_surprise_crisis_label")
        mc.business.mandatory_crises_list.append(sarah_weekend_surprise_action)

    def add_sarah_hire_action():
        Sarah_hire_action = Action("Sarah hire",Sarah_hire_requirement,"Sarah_hire_label")
        mc.business.mandatory_crises_list.append(Sarah_hire_action)

    def add_sarah_new_tits_action():
        Sarah_new_tits_action = Action("Sarah new tits",Sarah_new_tits_requirement,"Sarah_new_tits_label")
        mc.business.mandatory_crises_list.append(Sarah_new_tits_action)

    def add_sarah_threesome_request_action():
        Sarah_threesome_request_action = Action("Sarah Threesome Request",Sarah_threesome_request_requirement,"Sarah_threesome_request_label")
        mc.business.mandatory_crises_list.append(Sarah_threesome_request_action)

    def add_sarah_arrange_threesome_action(person):
        Sarah_arrange_threesome_action = Action("Sarah_threesome_arrange",Sarah_arrange_threesome_requirement,"Sarah_arrange_threesome_label")
        person.add_unique_on_talk_event(Sarah_arrange_threesome_action)

    def add_sarah_initial_threesome_action():
        Sarah_initial_threesome_action = Action("Sarah initial threesome",Sarah_initial_threesome_requirement,"Sarah_initial_threesome_label")
        mc.business.mandatory_crises_list.append(Sarah_initial_threesome_action)

    def add_sarah_ask_for_baby_action():
        Sarah_ask_for_baby = Action("Sarah asks for a baby", Sarah_ask_for_baby_requirement, "Sarah_ask_for_baby_label")
        mc.business.mandatory_crises_list.append(Sarah_ask_for_baby)

    def add_sarah_fertile_period_start_action():
        Sarah_fertile_period_start = Action("Sarah starts a fertile period", Sarah_fertile_period_start_requirement, "Sarah_fertile_period_start_label")
        mc.business.mandatory_crises_list.append(Sarah_fertile_period_start)

    def add_sarah_fertile_period_end_action():
        Sarah_fertile_period_end = Action("Sarah ends a fertile period", Sarah_fertile_period_end_requirement, "Sarah_fertile_period_end_label")
        mc.business.mandatory_crises_list.append(Sarah_fertile_period_end)

    def add_hr_director_initial_hire_action(person):
        HR_director_initial_hire_action = Action("Hire HR Director",HR_director_initial_hire_requirement,"HR_director_initial_hire_label", args = person)
        mc.business.mandatory_crises_list.append(HR_director_initial_hire_action)

    def get_sarah_date_outfit_one():
        outfit = Outfit("Sarah Date Outfit One")
        outfit.add_upper(summer_dress.get_copy(), [.95, .7, .87, .95])
        outfit.add_lower(tiny_lace_panties.get_copy(), [.95, .7, .87, .95])
        outfit.add_feet(heels.get_copy(), [.95, .7, .87, .95])
        outfit.add_feet(thigh_highs.get_copy(), [.95, .7, .87, .95])
        outfit.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        outfit.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        return outfit

    def get_sarah_date_outfit_two():
        outfit = Outfit("Sarah Date Outfit Two")
        outfit.add_upper(two_part_dress.get_copy(), [.95, .7, .87, .95])
        outfit.add_feet(fishnets.get_copy(), [.95, .7, .87, .95])
        outfit.add_feet(pumps.get_copy(), [.95, .7, .87, .95])
        outfit.add_accessory(heavy_eye_shadow.get_copy(), [.1, .1, .12, .9])
        outfit.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        outfit.add_accessory(lipstick.get_copy(), [.745, .117, .235, .8])
        return outfit


label Sarah_intro_label():
    $ the_person = sarah
    "*DING DONG*"
    "You hear the doorbell ring. You don't remember expecting anyone? You go and answer it."
    $ the_person.draw_person()
    "Standing at your door is a cute brunette, fairly short, and strikingly familiar..."
    "She appears to be holding some kind of clipboard. A door to door saleswoman? Do those still exist?"
    the_person.char "Hello sir, I am [the_person.title], with Metropolis Power and Light, I was just wondering if you had ever thought about installing solar panels..."
    "She begins talking about the benefits and tax credits associated with solar panels, but you have a hard time listening."
    "This girl... she look so familiar! Where do you know her from!?!"
    the_person.char "...with even 50%% coverage of the roof you can expect a considerable reduction in your electric bill..."
    "What did she say her name was again? [the_person.title]? Suddenly you get a flash of a memory from a long time again. You quickly interrupt her."
    mc.name "I'm sorry, you said your name was [the_person.title]? Is your name [the_person.title] [the_person.last_name]?"
    "She immediately stops her sales pitch."
    the_person.char "That's right... do... do I know your from somewhere?"
    "Faint memories come flooding back to you. When you were growing up, your dad and his best friend got married around the same time and had kids!"
    "You used to spend a lot of time with your dad and his friend, and his friend's daughter, who was just a few years younger than you!"
    "You aren't sure what happened, but one day the other family moved away, to another city, and you never saw them again."
    mc.name "Your dad, he was friends with my dad! I remember when our dad's used to hang out, we spent a lot of time together!"
    "She looks shocked, but you can see she is also starting to remember..."
    the_person.char "Wait, I think I remember... Mr. [mc.last_name]? So you must be... is it really [mc.name]???"
    "You quickly nod!"
    $ the_person.draw_person(emotion = "happy")
    the_person.char "Oh my god! I don't believe it! You and your dad used to come over every week! And even though I was a few years younger than you, you would be so nice to me!"
    "You don't really remember going out of your way to be nice, but it was also a long time ago."
    $ the_person.draw_person(position = "kissing")
    "Without warning, [the_person.name] throw herself at you and gives you a big hug."
    the_person.char "I never would have thought in a million years I would run into you again!"
    $ the_person.draw_person(position = "stand2", emotion = "happy")
    mc.name "Dad told me your family had to move away from work. What brings you back to town?"
    $ the_person.draw_person(position = "stand2", emotion = "sad")
    the_person.char "Ahh... well, I had just finished my degree and landed an internship at a company in town here. It was a great company, or so I thought..."
    "She clears her throat and continues."
    the_person.char "The director there told me if the internship went well it could become a full time position. I worked my ASS off at that place, for 6 months! And I was bartending in the evenings to make ends meet..."
    the_person.char "... well, when my six months was up, he said, sorry, that wasn't good enough. We are terminating you."
    $ the_person.draw_person(position = "stand2", emotion = "angry")
    the_person.char "I found out later, they hired some dumb bimbo for my position. I made some friends at the company, they are pretty sure the director is banging her in the office every day!"
    $ the_person.draw_person(position = "stand2", emotion = "sad")
    "[the_person.possessive_title] looks down at the ground. It looks like she is about to cry."
    mc.name "That really sucks. I'm sorry to hear that. What were you interning for, anyway?"
    $ the_person.draw_person(position = "stand3")
    "The change of topic helps her keep her composure."
    the_person.char "Well, I just finished up my degree in Sociology, and I was interning for a Human Resources position..."
    "Human Resources? That might actually be fairly useful."
    the_person.char "... I was really hoping to eventually move up to HR director there. I love working with other people, and the small business atmosphere was great!"
    "HR director? You've never heard of such a position."
    mc.name "So, what kind of work would you do as an HR director that is different from a regular HR position?"
    the_person.char "Well, I would be in charge of the direction of the company in general, as far as work values, help with company morale..."
    "She goes on to list multiple duties, aspects of running a small business that you had honestly never considered before."
    "When she finishes, you consider things for a moment. It would be REALLY handy to have someone around like this. She already has some work experience, and is young and ready to prove herself."
    "But, before you hire her, you would need to set up the HR director position at the company. Alternatively, you could still setup the new position, but hire someone else to fill the position."
    menu:
        "Offer to hire her":
            mc.name "So, as it turns out, I just recently started a new business making small run pharmaceuticals. You seem pretty knowledgeable, would you consider running the HR department?"
            "[the_person.title] is caught completely off guard by your offer."
            the_person.char "Wait, so, you run a small business? I mean, I would love to, but I can't afford to do another unpaid internship right now."
            mc.name "I didn't say it was unpaid, this would definitely be a paid position."
            $ the_person.draw_person(position = "stand3", emotion = "happy")
            $ the_person.change_happiness(5)
            $ the_person.change_love(5)
            the_person.char "That would be... incredible! I don't know what to say! I can't wait to get started!"
            mc.name "I'll have to get your phone number. I'll need to set up the position before I can officially hire you, and that might take a few days."
            the_person.char "Oh! Of course, here..."
            "You quickly exchange phone numbers with [the_person.title]."
            mc.name "I'll be in touch with you soon I think."
            the_person.char "This is great, [the_person.mc_title], you won't regret this, I promise!"
            "You say goodbye to her, and she goes to keep selling solar panels until you get back to her after creating the HR director position."
            "In order to hire [the_person.title], you will need to create a new HR Director position via the policy menu."

            $ add_sarah_hire_action()

        "Don't offer to hire her":
            "You decide maybe down the line you could make a new HR director position, but you decide the [the_person.title] is probably not the best fit for it."
            mc.name "I'm sorry it didn't work out, I hope you are able to find something in your field."
            the_person.char "Thanks... well, it was good seeing you. I'd better keep at it."
            "You say goodbye to [the_person.title]. If you want to hire an HR director, you will need to create the position via the policy menu."
            $ sarah.event_triggers_dict["rejected"] = True
            $ sarah.set_schedule([1,2,3], None)   # make her a free roaming character

    $ sarah.event_triggers_dict["first_meeting"] = True
    return

label Sarah_hire_label():
    $ the_person = sarah
    "After creating the new HR Director position, you call up [the_person.title]. She answers and says hello."
    mc.name "Hey, I just wanted to let you know, I have the details finalized for an HR Director position."
    the_person.char "That sounds great! When can I get started?"
    $ day_name = "Tomorrow"
    if day%7 == 4 or day%7 == 5: # its friday or saturday so next workday is monday
        $ day_name = "Monday"

    mc.name "[day_name] morning. I'll text the address after this call. We will go over your role and responsibilities when you get there."
    the_person.char "Yes! I'm so glad to finally be done selling solar panels. I'll see you in the morning!"
    "You hang up the phone. You quickly text [the_person.title] the address of your business."
    $ add_hr_director_initial_hire_action(the_person)
    $ set_HR_director_tag("business_HR_meeting_last_day", day) # used to make sure we meet the next day
    return

label Sarah_third_wheel_label():
    $ the_person = sarah
    $ the_person.apply_outfit(get_sarah_date_outfit_one())

    "By yourself on the weekend at work, you get up for a minute and decide to stretch your legs and walk the hallways for a bit."
    "As you pass by the HR offices, you notice the HR Director's office door is open and the light is on. You decide to investigate."
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You see [the_person.possessive_title] sitting at her desk, rummaging through her drawers looking for something."
    "She notices you step in her door and looks surprised."
    the_person.char "Oh! Hey [the_person.mc_title]. I was just looking for something I left in my desk. What are you doing here? Isn't this place closed down for the weekend?"
    mc.name "Yeah, well, I had a few things I wanted to get done over the weekend. Is it something I can help you find?"
    the_person.char "I actually just found it! One second..."
    "You see her pull a small, silver package out of her desk and shove it in her bag quickly... was that a condom?"
    the_person.char "...sorry I just... you know, like to be prepared. You never know!"
    mc.name "You look nice, you have a date tonight?"
    "[the_person.title] blushes and looks down at her desk."
    the_person.char "Errrmm... not really. I'm meeting a friend at the bar for a few drinks. I thought it was just going to be me and her, but she just texted me she is bringing her boyfriend."
    mc.name "Ah... your friend... is she like, your wing-woman or something? Helping you pick up guys at the bar?"
    the_person.char "Well, not exactly. I don't really want to talk about it right now."
    "She glances up and looks at you for a moment. Suddenly you realize she is checking you out."
    the_person.char "Say, what are you up to tonight, [the_person.mc_title]?"
    mc.name "Well, I was gonna get a few more things done around here. But to be honest, I wouldn't be against grabbing a few drinks with an old friend, if that were to be suggested."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person.char "Aww, you wouldn't mind coming along? I hate being the third wheel. If you get bored you can leave at any time, I promise!"
    mc.name "Nonsense, let me just wrap up what I was doing, lockup and we'll go."
    "You head downtown with [the_person.char]. You decide to walk since it isn't very far, and enjoy talking with her as you go."

    $ mc.change_location(downtown)
    $ mc.location.show_background()

    $ scene_manager.update_actor(the_person, position = "stand2")
    "Getting curious, you decide to ask her why she needed the condom at the office."
    mc.name "So... when I first stepped into your office you were looking for something in your desk... was that a condom?"
    "[the_person.title] doesn't stop walking, but you can see her get a little tense."
    the_person.char "Yeah, it was."
    mc.name "So, why did you need to come back and grab that?"
    the_person.char "Well my friend has been dating this guy for a while and keeps complaining, he wants them to open up their relationship some, maybe bring a lucky guy or girl back to their place sometime..."
    the_person.char "I've been out with them a couple of times now, hoping maybe they would show interest in me, but so far nothing."
    if sarah.event_triggers_dict.get("epic_tits_progress", 0) < 2:
        the_person.char "Her boyfriend... it's like he just looks right through me. I've seen them leave the bar with a girl before, and its always some dumb looking, busty girl."
        mc.name "Don't be silly, you are so sexy. There is more to look for in a woman than chest size."
        "She laughs at you sarcastically."
        the_person.char "Ha! Very funny. No, I'm afraid the guys I meet tend to friend zone me pretty quick. The flat chested third wheel! I suspect that is how things will go tonight."
    else:
        the_person.char "I though that, you know, after taking those serums that her boyfriend might actually notice me now."
        the_person.char "Really though, I'm about ready to move on. They still think of me as that flat chested third wheel I used to be!"
    "[the_person.title] considers things for a bit."
    the_person.char "However tonight goes... its pretty amazing you are willing to come out here with me like this."
    mc.name "Of course, I can't remember the last time I said no to drinks with a single lady as beautiful as you."
    the_person.char "There you go again! You know, it was a long time ago that we grew up together. But I still have so many fond memories of you. You always used to be so nice to me."
    the_person.char "I remember one time, we were playing in the living room at my house, and suddenly a bug landed on my head. I started screaming! I was so scared."
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    "She stops walking for a moment and turns to you, a serious, but happy look on her face."
    the_person.char "Suddenly, you grabbed me. HOLD STILL! you yelled, and you knocked the bug off me and on the floor and stomped on it."
    the_person.char "When my family moved away and the memories got old... I kept telling myself, we were just kids. He was sweet because we were just kids."
    the_person.char "But meeting you again, now that we are adults... and getting to know you all over again. You are still that sweet boy."
    the_person.char "You didn't even think twice about it tonight, when I asked you to go. That means a lot to me, you know?"
    $ scene_manager.update_actor(the_person, position = "stand2")
    "[the_person.possessive_title] turns and continues walking. You walk beside her the rest of the way to the bar in silence."

    #TODO change background to bar.
    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()

    $ sarah_friend = make_person(tits = "F", force_random = True) #TODO figure out how to properly delete this character later
    $ sarah_friend.set_title(sarah_friend.name)
    $ sarah_friend.set_mc_title(mc.name)
    "When you get to the bar, [the_person.title] quickly spots her friend and leads you over to the table."
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(sarah_friend, position = "sitting", character_placement = character_left_flipped)
    the_person.char "Hey [sarah_friend.title]! Good to see you."
    sarah_friend.char "Hey girl! Is he with you?"
    "She nods towards you."
    the_person.char "Yup! This is my bo... I mean, an old friend of mine. [mc.name] this is [sarah_friend.title]!"
    "You make acquaintance and sit down. [sarah_friend.title] also introduces you to her boyfriend."
    "You chat for a bit, but notice that [sarah_friend.title] keeps checking you out. Normally you would be testing the waters with her, but with [the_person.title] here, you are a little leary."
    mc.name "Hey, how about I get us a couple drinks, [the_person.title]?"
    the_person.char "Oh! That sounds great! Can you get me an appletini?"
    "As you start to get up, [sarah_friend.title]'s boyfriend also excuses himself to the restroom, leaving the girls alone."
    "It takes a few minutes to get the attention of the bartender. You order the drink for [the_person.title] and get yourself a nice bourbon, straight."
    $ mc.business.change_funds(-20)
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
    "When you come back to the table, you notice that [the_person.possessive_title] is looking down at the table and looks upset about something."
    mc.name "Hey! Here's your drink... are you okay?"
    the_person.char "Yeah... yeah I'm fine I just umm, I need to go use the lady's room."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She gets up in a hurry and walks quickly away. You look at [sarah_friend.title]"
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    mc.name "Umm... any idea what that is about?"
    sarah_friend.char "No idea... we were just talking about, well you actually."
    "Something about the way she says it makes you uncomfortable."
    sarah_friend.char "[the_person.name] says you are a great guy, a good friend of hers."
    mc.name "Yeah, something like that I guess..."
    sarah_friend.char "What do you say we get out of here? Like back to my place?"
    mc.name "That sounds pretty good actually. [the_person.name] will be excited to hear that I think."
    sarah_friend.char "Ha! No no, I mean, just you. [the_person.name] is a good friend but..."
    mc.name "But?"
    if sarah.event_triggers_dict.get("epic_tits_progress", 0) < 2:
        sarah_friend.char "My boyfriend... he just isn't attracted to her. I mean, have you seen her chest? Like, neither have we!"
        "You feel yourself getting angry at her crude remarks."
    elif sarah.event_triggers_dict.get("epic_tits_progress", 0) == 2:
        sarah_friend.char "My boyfriend can't stop staring at her tits. It's pissing me off! I can't believe she got implants, she is such a whore."
        "You feel yourself getting angry at her crude remarks."
    else:
        sarah_friend.char "Like, one day she's got nothing, next thing I know, her tits are fucking huge!?! She's such a bimbo."
        "You feel yourself getting angry at her crude remarks."
    "You are able to restrain yourself, but only just barely."
    mc.name "[the_person.name] has an amazing body, and a great personality to go with it. If you and your boyfriend don't see that, I don't think anything with me can work out."
    sarah_friend.char "Pfft, whatever. There's a dozen other dicks at the bar. Why don't you go find your date, she's probably sulking in the bathroom again!"
    "You decide not to stoop to her level and to end your conversation there. You grab you and [the_person.title]'s drink and get up, not bothering to say goodbye."
    $ scene_manager.remove_actor(sarah_friend, reset_actor = False)
    "You walk over to where the restrooms are and wait for [the_person.title]. You stand there for several minutes but start to get worried about her."
    "You don't see anyone come in or out of the women's restroom so you decide to risk it. You walk to the door and slowly open it."
    $ scene_manager.add_actor(the_person, position = "stand2", emotion = "sad")
    "Inside you see [the_person.title] looking at herself in the mirror. She is forlorn and from the look of her makeup has obviously been crying."
    mc.name "Hey, are you okay? I don't mean to invade your privacy, but I was starting to get worried about you."
    "She quickly looks up and is surprised to see you. She briefly pulls herself together."
    the_person.char "Is that you, [the_person.mc_title]? You're still here? I thought you would be gone by now..."
    mc.name "What are you talking about?"
    the_person.char "Well, [sarah_friend.title] said... she was asking me about you, asked if we were involved, and when I said no said she was going to make a pass at you tonight..."
    the_person.char "I just assumed, when I left the table that, I mean, why didn't you go with her?"
    "She assumed when her friend made a pass at you that you would bail on her! You quickly reassure her."
    mc.name "[the_person.title], I came here to support you, and to spend time with my long lost friend having some fun and a few drinks."
    mc.name "If you think I'm going to miss out on that for a silly one night stand, you are mistaken."
    $ scene_manager.update_actor(the_person, position = "stand2", emotion = "happy")
    the_person.char "I'm sorry! I didn't mean that I think you're shallow or anything I just... Look, give me one more minute and I'll be right out, okay?"
    mc.name "Sounds good!"
    "You step out of he lady's room and shortly after [the_person.title] steps out and joins you. You hand her the appletini."
    the_person.char "Thanks for waiting! I'm so sorry, I honestly thought you were going to go with them."
    the_person.char "Thank you for... I mean, everything you've done for me. You gave me a job, you let me drag you out to a bar with strangers, and then stuck with me even when you probably shouldn't have..."
    mc.name "You're crazy, it's not everyday a long last childhood friend literally knocks on your front door."
    the_person.char "You've always been amazing to me. I should have known better."
    $ the_person.change_stats(happiness = 20, obedience = 10, love = 10)
    "She takes a long sip of her drink. You begin to chat and catch up a bit."
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ mc.business.change_funds(-100)
    "You spend several hours with [the_person.title] sitting in a secluded booth catching up. After multiple appletinis and whiskeys, you are both feeling pretty good."
    the_person.char "Well, I suppose it is getting pretty late. You have no idea how great this was. I don't want to say goodbye yet..."
    "[the_person.title] thinks for a moment."
    the_person.char "Hey... do you want to walk me home?"
    mc.name "That sounds like a perfect way to end the evening. Let's go."

    $ mc.change_location(downtown)
    $ mc.location.show_background()

    $ scene_manager.update_actor(the_person, position = "stand3")
    "You walk together with [the_person.title] through the streets as she slowly leads the way. You converse a bit, but things are mostly quiet as you walk."
    "Soon you are standing in front of the door to her apartment building."
    # you now know were Sarah lives
    $ the_person.learn_home()
    the_person.char "Thanks for today! It really means a lot to me that you spend the whole evening with me."
    mc.name "Consider it making up for lost time."
    "[the_person.possessive_title] blushes and looks down."
    mc.name "Goodnight."
    "You step close and put your arms around her."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "She quickly wraps her arms around you and embraces you. You move your head to kiss her on the cheek, but at the last second she moves her head and you find your lips pressing into hers."
    $ the_person.break_taboo("kissing") # break her kissing taboo
    the_person.char "Ohhh! Mmmmm..."
    "At first she opens her eyes in surprise, but quickly closes them and begins to kiss you back."
    "Her lips part and your tongue quickly takes advantage and begins to explore her soft lips. They taste sweet, with just a hint of appletini."
    "You stand there in front of [the_person.title]'s building, holding each other and making out for several minutes until the kiss stops and you step back. Her eyes are still closed."
    mc.name "I'll see you on Monday?"
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She suddenly snaps back to reality. Her cheeks are flushed."
    the_person.char "Right! Yes of course. Goodnight!"
    $ time_of_day = 3
    "She turns and heads into her building. You check your watch and realize how late it is."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    $ sarah_friend.remove_person_from_game()
    $ del sarah_friend
    $ add_sarah_get_drinks_action()
    return

label Sarah_get_drinks_label():
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ the_person = sarah
    $ the_person.planned_outfit = get_sarah_date_outfit_one()
    $ the_person.apply_planned_outfit()

    "Lost in thought as you get your work done in the silence of the weekend, a sudden voice startles you."
    the_person.char "[the_person.mc_title]! I figured I'd find you around here on a Saturday again!"
    "You look up to see the now familiar face of [the_person.title] standing in the doorway."
    $ scene_manager.add_actor(the_person, emotion = "happy")
    "It's crazy to think that just a short time ago, she was out of your life completely, but after your chance encounter, you feel like you've been friends forever."
    mc.name "Hey [the_person.title]. You look great! Are you going out tonight?"
    the_person.char "Actually, I'm not sure yet. I hope so! But I'm not sure if the guy I want to go out with is going to be able to go yet or not..."
    mc.name "Is that so? I hope he can make it and that he treats you well!"
    the_person.char "Hahaha, yeah me too. And don't worry, he's always treated me right."
    "[the_person.possessive_title] looks down at the floor for a minute and mumbles something. Its obvious she is trying to work up the courage to ask you out, but it is cute watching her fumble a bit."
    the_person.char "So... you uhh, have any big plans for the evening, [the_person.mc_title]?"
    mc.name "Oh, well, certainly nothing as big as what you have planned! I'm just trying to get a little a head of work for next week."
    the_person.char "Ah! That's good. It is pretty amazing how much work you put into this place. It's something I admire a lot..."
    the_person.char "Anyway, I've seen how hard you work and I was thinking that, maybe we could go out and get a few drinks?"
    "You decide to tease her a bit."
    mc.name "Ahh, I see. You meeting another friend tonight? I'm not sure I want..."
    "She quickly interrupts you."
    the_person.char "No! God no, that was awful. I thought we could just go out, you know? Me and you?"
    mc.name "You mean like a date?"
    "She stutters a moment before she replies."
    the_person.char "Well, ermm, I mean, uhh..."
    the_person.char "Yeah. Pretty much that is exactly what I'm trying to ask..."
    "You admire her courage. She must be really interested in you to have the guts to ask you out like this! If you accept, she might assume you are interested in a relationship..."
    menu:
        "Sounds great!": #Begin the dating path with Sarah
            mc.name "A date sounds great! I'd love to spend some more time with you, catching up and learning about what you've been up to."
            "Her face shows visible signs of relief."
            the_person.char "Okay! This will be fun! Do want to get out of here now, or do you need some time to finish up?"
            $ sarah.event_triggers_dict["dating_path"] = True
            $ the_person.add_situational_slut("Date", 20, "There's no reason to hold back, he's here to fuck me!") # Bonus to sluttiness since she really likes you.

            $ the_person.change_happiness(20)
            $ the_person.change_love(10)
        "Just as friends":
            mc.name "I wouldn't mind going out for a few drinks, with a friend of course."
            $ scene_manager.add_actor(the_person, emotion = "sad")
            "Her face shows visible signs of disappointment."
            the_person.char "Oh, right. Friends! That's us! I don't want to interrupt you, there, buddy. Need a few minutes to finish up?"
            $ the_person.change_happiness(-20)
            $ the_person.change_obedience(20)
            $ the_person.change_love(-10)
            $ sarah.event_triggers_dict["dating_path"] = False
            $ the_person.add_situational_slut("Date", 10, "There's no reason to hold back, he's here to fuck me!") # Bonus to sluttiness not so high since we go as friends.

    mc.name "I'm actually at a great stopping point now. Let's go!"
    the_person.char "Great! Do you want to walk again tonight? It was kind of nice when we walked together last time."
    mc.name "Sounds good to me, it's good to get out and stretch the legs once in a while."
    "You lock up on your way out and head toward downtown."

    $ mc.change_location(downtown)
    $ mc.location.show_background()


    "You enjoy pleasant conversation with [the_person.possessive_title] as you walk downtown."
    if the_person.event_triggers_dict.get("dating_path", False) == True:
        "As you walk along, you feel her hand slip into yours. You twiddle your thumb with hers as you walk downtown."
    #TODO the convo




    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()

    "You walk into the bar. [the_person.title] spots an empty booth."
    the_person.char "Hey, there's an empty table over there!"
    mc.name "Go grab it. Appletini?"
    the_person.char "Sounds great!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She walks off to the booth while you head up to the bar."
    "You order your drinks with the bartender. If you wanted to, now would be a good time to slip a serum into her drink..."
    $ mc.business.change_funds(-20)
    menu:
        "Slip in a serum":
            "After you get the drinks, you carefully add a serum to it."
            call give_serum(the_person) from _call_give_sarah_serum_001
        "Leave alone":
            "You decide to leave her drink alone."
    "You grab your drinks and then head to the table. You sit down across from [the_person.title]."
    $ scene_manager.update_actor(the_person, position = "sitting")
    the_person.char "Thanks! I love these things..."
    "She takes a long sip from her glass. You take a sip of yours. [the_person.possessive_title] sets down her glass and looks at you."
    the_person.char "I have to say, I feel like I'm settling in pretty well. The girls at the office have been really nice to me so far."
    mc.name "That's good to hear. I'm very selective about who I hire."
    the_person.char "Yeah. You choice is very, shall we say, interesting? Hiring only women to work for you. Not that I'm complaining or anything!"
    mc.name "I know it may seem a bit odd, but so far it has been advantageous to keep the staff all female. Perhaps in the future that could change, but now it is working."
    the_person.char "It's quite alright with me. To be honest, I umm, enjoy the surroundings..."
    "She takes a long sip of her drink."
    mc.name "Sorry, I feel like you've hinted at this a few times before but, I just want to clarify. Are you a lesbian? I'm totally fine with that, I'm just curious."
    "[the_person.title] laughs and puts her hand on yours."
    the_person.char "Oh, I'm not dedicated to it or anything, but I've always been curious about what it would be like to be with another woman."
    "She sighs."
    the_person.char "Don't get me wrong, I don't think I could ever date another woman, I prefer men, but I've always wanted to try a Ménage à trois..."
    $ the_person.increase_opinion_score("other girls")
    $ the_person.increase_opinion_score("threesomes")
    "You have discovered that [the_person.title] is bi-curious and into threesomes!"
    mc.name "That's very open minded of you. I can certainly respect that!"
    "[the_person.title] tips her glass back and finishes her first drink. You make it a point to do the same."
    mc.name "Let me grab the next round."
    if the_person.event_triggers_dict.get("dating_path", False) == True:
        the_person.char "That sounds great. Say, want to play some darts? I'll grab us a board while you grab the drinks!"
        mc.name "That sounds great, I'll meet you over there."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title] gets up and walks over to the dart boards while you grab a couple more drinks."
        $ mc.business.change_funds(-20)
        "You feel like, so far at least, this date is going pretty well!"
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You walk over to [the_person.title], drinks in hand. You hand her a drink."
        mc.name "How about a toast? To tonight! May we love as long as we live, and live as long as we love."
        $ the_person.change_happiness(5)
        $ the_person.change_love(5)
        "You surprise yourself with your sappy toast. It seems to have the desired effect though, as she smiles wide with your toast."
    else:
        the_person.char "Hey, let me grab the next round. I want to play a game though! Can you go get us a dart game setup?"
        mc.name "Yeah, that actually sounds pretty fun. I'll do that."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title] gets up and walks over to the bar while you head over to reserve a dart board."
        "You are having a lot of fun hanging out with [the_person.title]. Even though you rejected her earlier, you are wondering how she might feel about a friends with benefits setup..."
        $ scene_manager.update_actor(the_person, position = "stand4")
        "[the_person.title] joins you and hands you another whiskey."
        the_person.char "How about to a toast? To he who has seen me at my best and has seen me at my worst and can't tell the difference!"
        "You grin at her cheesy toast, she smiles wide at you."
    "You clink your glasses together and take a deep sip."
    the_person.char "Alright! I'm going first."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    call play_darts_301(the_person, focus_mod = 2) from play_darts_301_call_1
    if _return:
        $ scene_manager.add_actor(the_person, emotion = "sad")
        "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
    else:
        $ scene_manager.add_actor(the_person, emotion = "happy")
        "[the_person.title] gives you a huge smile after winning your game of darts!"
    "You notice the drinks are empty."
    mc.name "That was a good game. Want another round and another game?"
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    the_person.char "Oh! That sounds great! I'll get it setup!"
    "You walk over to the bartender and order another round. You walk back to the dart board and give [the_person.possessive_title] her drink."
    $ mc.business.change_funds(-20)
    the_person.char "Thanksh! I love these things..."
    "You notice her speech is starting to get a little slurred... You bet as you feed her drinks, she may have trouble focusing on the game."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] starts to line herself up on the line to throw. You decide to see if you can distract her a little further."
    "You walk up behind her and put your hand on her back."
    mc.name "Hang on, I just noticed something about the way you are throwing the darts."
    "You get in close behind her until you are right behind her, your body up against hers."
    the_person.char "Oh? I thought I did okay, but if you have some... tips... for me that would be nice!"
    "The feminine smell in her hair enters your nostrils and you take a deep breath, enjoying your proximity with [the_person.title]."
    "You run your fingertips along her arm, until you are holding her hand as she holds her dart."
    mc.name "That's right, there was something about your posture that caught my eye."
    "You are now pushing yourself lightly up against [the_person.title]. She catches her breath when she feels your erection beginning to grow against her backside."
    the_person.char "Ah, something caught your eye then?"
    "You quickly release her and then walk back to the table."
    the_person.char "Yeah, something like that. I'm not sure what it was, but I'll let you know if I can put my finger on it..."
    "[the_person.title] is trying to focus on the dart board, but she keeps stealing glances back at you. Your flirting is having the desired effect on her!"
    "She readies herself for the next round of darts."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    call play_darts_301(the_person, focus_mod = -2) from play_darts_301_call_2
    if _return:
        $ scene_manager.add_actor(the_person, emotion = "sad")
        "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
    else:
        $ scene_manager.add_actor(the_person, emotion = "happy")
        "[the_person.title] gives you a huge smile after winning your game of darts!"
    "Drinks are empty again. You look at [the_person.title]. She is definitely tipsy, but you think she should be able to handle one more round."
    mc.name "How about one more game? I'll grab us another round."
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    the_person.char "Another drink! I'm loooooveeeee going out with you, [the_person.mc_title]! You know how to keep the drinksh flowing!"
    mc.name "Haha, okay, let me go grab us another round."
    "You walk over to the bartender and order another round. You walk back to the dart board and give [the_person.possessive_title] her drink."
    $ mc.business.change_funds(-20)
    the_person.char "OKAY, so, I've had a great warm up now, but I think for this next round, we should make it a littler more... intereshting."
    mc.name "Oh? What did you have in mind?"
    the_person.char "I think, whoever losses... HA thats a funny word... anyway whoever is the loser, should hafta walk the winner home!"
    "You raise an eyebrow involuntarily. For some reason you expected something a little... crazier than that."
    mc.name "Hah, okay, we can do that. You're up first!"
    "[the_person.possessive_title] turns and looks at the table where she set the darts earlier. She bends over and slowly starts picking them up, one by one."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    "She's completely bent over the table, and is obviously wiggling her hips at you. You realize when she talked earlier about the loser walking the winner home, she was probably proposing your place or hers..."
    "You step behind her and get close to her again. You push your hips against hers, and pretend to reach past her towards your darts that are also on the table."
    mc.name "Excuse me... just grabbing my darts here real quick..."
    "You slowly grab your darts, one by one. She pushes herself back against you."
    the_person.char "Of course, be careful though! The tipsh are sharp."
    mc.name "Of course, you needn't worry, I'll handle them gently..."
    "As you finish your sentence, you run your free hand down along her back. You slowly stand up and move away from her. You don't want to be too lewd in a public setting like this... not yet anyway..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title] walks over to the line and looks at the dart board, then back at you. She is so distracted, she can barely focus on the board."
    "You should be able to win this game handily, unless you decide to throw the game on purpose!"
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    $ sarah.event_triggers_dict["drinks_out_progress"] = 2
    call play_darts_301(the_person, focus_mod = -6) from play_darts_301_call_3
    if _return:
        $ scene_manager.add_actor(the_person, emotion = "happy")
        "[the_person.title] can't even pretend to be sad when you win the game."
        the_person.char "You won!"
    else:
        $ scene_manager.add_actor(the_person, emotion = "happy")
        "[the_person.title] gives you a huge smile after winning your game of darts!"
        the_person.char "You are such a gentleman. I'm pretty sure you were just letting me win! That totally doesn't count!"
    "She takes the last sip of her drink before setting it down."
    the_person.char "I'll walk you home! Besides, it's only fair, you walked me home last time."
    "You start to protest, but she quickly silences you."
    the_person.char "Don't be silly! I can see myself home whenever we get done... err... when you say goodbye I mean..."
    "Her intentions are pretty clear at this point. You take the last sip of your whiskey and set it down."
    mc.name "I can see there's no talking you out of it. And to be honest, I would appreciate the company."
    "She smiles at you. You leave the bar with her and start walking home."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    #TODO set to night time
    $ time_of_day = 3 #Hopefully this works

    "You enjoy the fresh air as you begin your walk. Thinking about your time with [the_person.title] tonight, you decide now would probably be a good idea to talk about things."
    if the_person.event_triggers_dict.get("dating_path", False) == True:
        "You take the initiative and take [the_person.title]'s hand. You can see her smile out of the corner of your eye."
        mc.name "So, I had a lot of fun on our date tonight."
        the_person.char "Me too!"
        mc.name "I think it is great that you are so open in your sexuality, and wanting to try new things."
        "You can feel her grip tighten on your hand for a second."
        mc.name "I know it is kind of weird to talk about, but I want you to know that if you want to mess around with another girl... let's just say I'm not the jealous type."
        "She laughs at you before replying."
        the_person.char "That's good to know. Honestly, I wasn't sure how you would feel about it, but I figure most guys like to idea of being with two women..."
        mc.name "Yeah, I suppose that much is obvious. But I think I could probably help set something up..."
        "She stops and turns to you."
    else:
        mc.name "So, I had a lot of fun tonight."
        the_person.char "Me too!"
        mc.name "I think it is a great that you are open in your sexuality, and wanting to try new things."
        "You see a brief frown on her face start to form."
        mc.name "I know it is kind of weird to talk about, but I want you to know that, even though I'm not looking for anything serious right now, I'd love to help you explore that side of things... sexually."
        "She stops and turns to you."
    $ scene_manager.update_actor(the_person, position = "stand3")
    the_person.char "You mean... you would be willing to try and set something up?"
    mc.name "Well... yeah! I'm pretty sure that is something I could pull off."
    "[the_person.title] looks bewildered."
    the_person.char "That would be something. Huh! I'll have to think about it... okay?"
    "As you are standing there looking at each other, you feel a cold breeze begin, followed quickly by rain drops beginning to fall."
    the_person.char "Ah! I didn't know it was going to rain!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title] turns and starts to walk quickly. You hurry to catch up to her."
    "You are only a few blocks from your house, but by the time you get there, the rain is pouring down in sheets."
    "You quickly open the door and let [the_person.title] in."

    $ mc.change_location(hall)
    $ mc.location.show_background()

    # make sure we don't alter the outfit in her wardrobe
    $ test_outfit = the_person.outfit.get_copy()
    if test_outfit.get_upper_top_layer():
        $ test_outfit.get_upper_top_layer().colour[3] *= .75 #make top transparent
    if test_outfit.get_lower_top_layer():
        $ test_outfit.get_lower_top_layer().colour[3] *= .75 #make bottom transparent

    $ the_person.apply_outfit(test_outfit)
    $ del test_outfit

    $ scene_manager.update_actor(the_person, position = "stand4")
    if (len(the_person.outfit.get_upper_ordered()) > 0 or __builtin__.len(the_person.outfit.get_lower_ordered()) > 0):
        "You look at [the_person.title]. Her clothing is soaked and you can practically see through it. She looks cold."
    else:  #She's... naked?
        "Barely clothed, [the_person.title] is shivering from the cold."
    mc.name "I'm sorry, I didn't realize it was going to rain like that!"
    "You made quite a bit of noise when you came in the door, and [mom.title] pokes her head out from the kitchen to see what is going on."
    $ scene_manager.add_actor(mom, position = "stand2", character_placement = character_left_flipped)
    mom.char "Oh! You two look absolutely soaked! Are you okay?"
    mc.name "Thanks [mom.title]! This is [the_person.title]! We got caught out in the rain walking back. Do you think you could grab us a few towels, and maybe have some dry clothes for her to wear for a bit?"
    if sarah.event_triggers_dict.get("epic_tits_progress", 0) == 0: #Small tits
        mom.char "Yes of course! She looks about Lily's size, I'm sure I can find something..."
    elif sarah.event_triggers_dict.get("epic_tits_progress", 0) == 2: #Big tits
        "[mom.title] looks her over for a moment, checking out her curves."
        mom.char "Yes! I'm not sure Lily's clothes would work... I bet I have something I could give her, just give me a minute."
    elif sarah.event_triggers_dict.get("epic_tits_progress", 0) == 3: #Huge tits
        "[mom.possessive_title] eyes travel all over [the_person.title]'s body. Her eyes go wide when she see how big her tits are."
        mom.char "I'm not sure I have... actually, I think Gabrielle might have left something that would fit her..."
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[mom.title] leaves to go find something. [the_person.title] is shivering cold."
    mc.name "I'm sorry, you look so cold. Why don't you come her for a minute..."
    "You step toward her. You put your hands around her back and draw her close to you. She wraps her arms around your neck."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "Her body feels cold, but it feels great running your hands along her body. After a minute, she stops shivering."
    the_person.char "Thank you... that feels... much better."
    "Her face is nearing yours, and you are just getting ready to kiss her."
    $ scene_manager.update_actor(mom, position = "stand2")
    mom.char "Here we go! I got you some... OH!"
    "ABORT! You quickly let go of [the_person.title] when your mother interrupts you."
    mom.char "Sorry! I didn't... here you go!"
    "She quickly hands [the_person.title] a large towel and a set of clothes."
    mom.char "There you are dear. I'm sorry, but Lily is in the bathroom right now, taking one of her ridiculously long showers..."
    mc.name "That's okay, she can change in my room! I can wait out here."
    the_person.char "Thank you! I'll be quick!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] takes the clothes and the towel. You quickly point her to your room."
    "She disappears behind your bedroom door with the clothes. You mother turns to you."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    mom.char "She seems nice!"
    mc.name "Yeah! Believe it or not, she is the daughter of one of dad's old friends. We used to play together as kids!"
    if mom.sluttiness < 40:
        if sarah.event_triggers_dict.get("epic_tits_progress", 0) == 0: #Small tits
            mom.char "Aww! That's cute! And she is so cute too. You be nice to her, okay?"
        elif sarah.event_triggers_dict.get("epic_tits_progress", 0) == 2: #Big tits
            mom.char "Aww! That's great! She certainly has blossomed into a beautiful young lady. You be nice to her, okay?"
        elif sarah.event_triggers_dict.get("epic_tits_progress", 0) == 3: #Huge tits
            mom.char "Wow! That's great! And she has... I mean... her figure is incredible! You be nice to her, okay?"
        mc.name "Don't worry, [mom.title]."
    elif mom.sluttiness < 70:
        if sarah.event_triggers_dict.get("epic_tits_progress", 0) == 0: #Small tits
            mom.char "That's cute... but... what about me? The woman who brought you into this world needs you attention too..."
        elif sarah.event_triggers_dict.get("epic_tits_progress", 0) == 2: #Big tits
            mom.char "That's nice dear... but don't forget about me, okay? I have need too!"
        elif sarah.event_triggers_dict.get("epic_tits_progress", 0) == 3: #Huge tits
            mom.char "That's nice I guess..."
            mom.char "But... look I know she is absolutely stacked, but don't forget about me, okay? I have needs too!"
        mc.name "Don't worry, [mom.title]. No one could ever replace you."
    else:
        mom.char "Wow! She is so pretty."
        mom.char "So... when do I get a chance to get my hands on her?"
        mc.name "Don't worry, it'll be soon [mom.title]."
    mom.char "Okay! I'll umm, just be in my room for the night..."
    $ scene_manager.remove_actor(mom, reset_actor = False)
    "[mom.possessive_title] quickly steps into her room and closes the door. You look at the door to your own bedroom, imagining the woman inside it slowly peeling off her soaking wet garments..."
    "As you look at your door, you realize that it isn't closed all the way. [the_person.title] left it open a crack!"
    "You creep slowly up to your door and listen. You don't hear much coming from within, so you slowly inch the door open and then peek inside."

    $ mc.change_location(bedroom)
    $ mc.location.show_background()

    $ scene_manager.add_actor(the_person, position = "walking_away")
    "You see that [the_person.title] is just starting to peel off her clothes."
    $ scene_manager.strip_actor_outfit(the_person)
    "She stands there, looking at herself in the mirror for a moment, when she spots you looking at her from the door. Busted!"
    $ scene_manager.update_actor(the_person, position = "back_peek")
    the_person.char "Hey! You gonna come in and close the door or just stand there?"
    "Nice! She must have left the door cracked on purpose, hoping you would peek."
    "You quickly step into your room, close your door and lock it behind you. [the_person.title] giggles."
    "You walk over to her and embrace her again."
    $ scene_manager.update_actor(the_person, position = "kissing")
    the_person.char "I was hoping you would come..."
    "Her mouth opens, her eyes close, and your faces move together as you begin to kiss. Her mouth immediately opens and you begin to twirl your tongues around each other."
    $ the_person.change_arousal(10)
    the_person.char "That feels good... but I'm freezing!"
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You quickly pick her up. You carry her over to your bed and then throw her down on it."
    mc.name "Don't worry, I'll get your warmed up in a hurry!"
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You start to climb on top of [the_person.possessive_title]. She opens her legs and the wraps them around you."
    "You are still wearing your wet clothes, but you don't care. You slowly start to grind your hardness into her groin through your pants."
    $ the_person.change_arousal(10)
    the_person.char "Mmmm, that feels good, but you're cold too! Let's get these off..."
    "[the_person.title] is pulling at your shirt. You quickly help her take it off, then reach down, unbutton your pants, and take them and your underwear off in one smooth motion."
    "Your cock springs free. [the_person.title] gasps as she takes it in her hand."
    the_person.char "Ohhhh. It's so warm! This is exactly what I need to warm me up!"
    "You look down at [the_person.title]. She is stroking your cock now, and you can feel her legs start to wrap around your back again, urging you to push yourself into her."
    "For a moment you consider grabbing a condom, but that thought evaporates when she runs the nails of her free hand roughly down your back."
    "You let go of yourself, and move your hips into position just above hers. Her hand stops stroking you and guides your cock to her pussy as it gets close."
    "You can feel the moist heat coming from between [the_person.title]'s legs as you get close. You feel the head begin to poke against her slit."
    "Her legs wrap tighter behind you, begging you to push into her. You happily give in, parting her labia and sinking slowly into her cunt."
    the_person.char "OH god... that's so good!"
    call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True) from _call_sex_description_sarah_grabbing_drinks_1
    if the_person.event_triggers_dict.get("dating_path", False) == True:
        the_person.char "Oh my god... ever since you came back into my life, I'd been hoping... maybe this was all happening for a reason."
        "You lay down on your side next to her. She scoots next to you and lays her head on your arm."
        the_person.char "Can we... can I just be close to you for a while? I'm not ready for this day to end!"
        $ the_person.change_happiness(5)
        $ the_person.change_love(5)
        mc.name "Of course! Your skin feels so good."
        "You cuddle up with [the_person.possessive_title] for a while, just enjoying the afterglow of your lovemaking."
        "She is starting to doze off, when suddenly she wakes up and gets up."
    else:
        the_person.char "Mmm, that was nice. It's been a while since I was able to do that."
        "She rolls on her side and looks at you."
        the_person.char "So... friends with benefits then? I think that is an arrangement that I could live with."
        mc.name "Great! Yeah if you get the urge, I'm up for a hookup now and then."
        the_person.char "Okay. You'd better satisfy me though!"
        "You give her a wink and a nod."
        $ the_person.change_happiness(5)
        $ the_person.change_slut_temp(5)
        $ the_person.change_slut_core(5)
        the_person.char "Alright... I'm just gonna lay here for a moment. It's been a long day, I need to take a few minutes before I get up."
        "She rolls over, facing away from and relaxes for a bit, enjoying coming down from the high of fucking."
        "She is starting to doze off, when suddenly she wakes up and gets up."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person.char "Sorry... I just realized how late it is getting. I'd better get home!"
    #TODO have her actually put on the outfit provided earlier. Is this worth the effort to write?
    "You watch her intently from your bed. Her body looks amazing, as she begins to hide it behind the clothes you provided her."
    the_person.char "Don't worry, I can see myself out. I had a great time tonight! I'll see you on Monday, okay?"
    mc.name "Goodbye!"
    $ scene_manager.remove_actor(the_person)
    $ the_person.clear_situational_slut("Date")

    "[the_person.possessive_title] lets herself out of your room and leaves. Wow, what an evening!"

    $ add_sarah_stripclub_story_action()
    $ add_sarah_weekend_surprise_action()
    $ scene_manager.clear_scene()
    return

label Sarah_catch_stealing_label():
    $ the_person = sarah
    $ sarah.event_triggers_dict["epic_tits_progress"] = 1
    "As you walk to halls of your company, getting ready to pack things up for the weekend, you notice [the_person.title] sneaking out of the research division."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]... what brings you to research on a late Friday evening?"
    "She looks down at the ground and mutters for a second, trying to think of something. It is clear she is hiding something."
    the_person.char "Hey [the_person.mc_title]! I was just, well, [mc.business.head_researcher.name] had something for me that umm, I asked her for help with and so I was just grabbing it before I left for the weekend!"
    "With one hand behind her back, it doesn't appear she wants you to know what is it that she has."
    mc.name "Is that so? That's awfully nice of her. What is she helping with? Can I see it?"
    if the_person.obedience > 120:
        "Realizing that you need to know what she was doing in there, she lowers her head and brings her hand forward. In it are several glass vials with some prototype serum labeled 'T+'"
        the_person.char "I'm sorry... I know I shouldn't... distract the research staff but, when you told me on Monday that we had come up with a breast enhancement serum, I immediately knew I had to get some I just..."
    else:
        the_person.char "Oh, don't worry about it, it is just between me and her!"
        "You furrow your brow. Hopefully you can convince her to come clean with whatever it is that she is doing."
        mc.name "I'm sure it is fine, but you ARE coming out of a research on a Friday, after everyone has left for the weekend. Let me see what you have."
        "Reeling that you aren't going to back down, she slowly brings her hand forward. In it are several glass vials with some prototype serum labeled 'T+'"
        the_person.char "Don't be mad! When you told me on Monday that we had come up with a breast enhancement serum, I knew I had to get my hands on one of the prototypes..."
    mc.name "It's okay. I didn't realize that was something you would be interested in. If you had asked me, I would have seen it arranged without having to sneak around!"
    $ the_person.change_happiness(5)
    $ the_person.change_love(3)
    $ the_person.draw_person(emotion = "happy")
    "She is very relieved to hear that."
    the_person.char "Oh! Thank you [the_person.mc_title]! I'm sorry, I won't be sneaky like that again. I just... you know I've always had such a small chest and been really self-conscious about it."
    the_person.char "I've thought about getting implants before but... surgery seems so extreme for a cosmetic issue."
    mc.name "So, how many are you planning to take?"
    the_person.char "Oh, well, research says we don't know for sure how effective they are... I figure I'll just take one each day until I go up a few cup sizes."
    the_person.char "I've already ordered new bras and everything. I'm going to keep a careful record of how many I take and when, and then take measurements over the weekend."
    the_person.char "[stephanie.name] is going to stop by this weekend to help document everything, she said it would be good for research..."
    "You think about it for a moment. You picture [the_person.title] for a moment with some nice 'C' cup tits... but then you can't help but imagine if she went crazy with it and took more."
    $ try_to_convince = True
    menu epic_tits_choice_menu:
        "Sounds like a good plan":
            mc.name "You should definitely take it slow. I mean, worst case scenario, you can just take more later if you need to."
        "You should take them all":
            "[the_person.title] looks up at you, a bit surprised."
            the_person.char "Wh... what? I mean, I've always dreamed of having huge tits but... I mean I can always take more later, right?"
            mc.name "Fortune favors the bold, [the_person.title]. I don't think you will regret it if you do it."
            the_person.char "But... I've already bought all new bras and lingerie... I don't have the money right now to do that all over again!"
            menu:
                "Buy her new bras ($300)":
                    $ mc.business.change_funds(-300)
                    mc.name "I'll consider it an investment, from the business. It is the least we can do if you are willing to test the new serum prototypes."
                    the_person.char "Oh... that's very generous! I mean, I suppose if you're willing to do that. I can probably return a bunch of the other ones too."
                    "She stands there for a few moments, considering her options."
                    the_person.char "Ok! I'll do it! Oh god I'm so excited. I'm going to go straight home and take a few before bedtime."
                    mc.name "Sounds good. I'll look forward to seeing... all of you... on Monday."
                    "She blushes and nods."
                    the_person.char "Alright, see you Monday!"
                    $ add_sarah_epic_tits_action()
                    return
                "Stop wearing bras":
                    #TODO make new function to iterate through her wardrobe and remove the bra from every outfit.
                    if the_person.sluttiness > 40:
                        $ the_person.draw_person(position = "stand4", emotion = "happy")
                        the_person.char "Oh! Well that's an idea. Funny, why hadn't I thought of that?"
                        #TODO if based on if she has a uniform
                        # the_person.char "If I do that... Are you going to relax the dress code a bit? That's fine as long as I don't have to wear bras to work anymore..."
                        # mc.name "I will definitely look into it, if it helps you make up your mind."
                        "She stands there for a few moments, considering her options."
                        the_person.char "Ok! I'll do it! Oh god I'm so excited. I'm going to go straight home and take a few before bedtime."
                        mc.name "Sounds good. I'll look forward to seeing... all of you... on Monday."
                        "She blushes and nods."
                        the_person.char "Alright, see you Monday!"
                        $ Sarah_remove_bra_from_wardrobe(the_person.wardrobe)
                        $ add_sarah_epic_tits_action()
                        return
                    else:
                        the_person.char "I just... I don't think I can do that right now. I'm sorry [the_person.mc_title]!"
                        mc.name "It's fine, I just want you to be happy with your body."
                        the_person.char "Right. I mean, I can always take more later if I need to."

                "You're right":
                    mc.name "I just want you to be happy with your body."
                    "[the_person.title] looks a bit relieved."
                    the_person.char "Thanks [the_person.mc_title]."

        "Don't take them at all" if try_to_convince:
            "[the_person.title] looks up at you, a bit surprised."
            the_person.char "Wh... what? I mean, I've always dreamed of having huge tits... this is my opportunity to make that dream come true."
            mc.name "[the_person.title], you are a beautiful intelligent woman, with or without huge tits, you are still a woman I would love to date."
            the_person.char "Do you really mean that [the_person.mc_title], would you like dating me as I am now?"
            mc.name "Of course I would, now give me those vials."
            the_person.char "I don't know, I really want to give this a shot."
            menu:
                "Insist":
                    pass
                "Relent":
                    mc.name "Ok, have it your way, but I still think its a mistake."
                    $ try_to_convince = False
                    jump epic_tits_choice_menu
            mc.name "I have to insist [the_person.title] and be happy I don't give you a good spanking for being so dumb as to think men only judge woman by their breast size."
            "She looks at you shocked for the harshness of your words, but slowly stretches out her hand, giving you the serum."
            mc.name "Good, and if [mc.business.head_researcher.name] gives you any troubles, let her come see me. Now get out of here and go home."
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] gives a short nod and quickly scoots out of the building."
            # don't let her take them end epic tits story line
            $ sarah.event_triggers_dict["epic_tits_progress"] = -1
            return

    mc.name "Alright, you be careful this weekend. I'll look forward to seeing... all of you... on Monday."
    "She blushes and nods."
    the_person.char "Alright, see you Monday!"

    $ add_sarah_new_tits_action()
    return

label Sarah_epic_tits_label():
    python:
        the_person = sarah
        the_person.tits = "F"
        the_person.event_triggers_dict["epic_tits_progress"] = 3
        the_person.change_stats(slut_temp = 10, slut_core = 10)
    call Sarah_tits_reveal_label() from Sarah_epic_tits_call_1
    return

label Sarah_new_tits_label():
    python:
        the_person = sarah
        the_person.tits = "D"
        the_person.event_triggers_dict["epic_tits_progress"] = 2
        the_person.change_stats(slut_temp = 5, slut_core = 5)
    call Sarah_tits_reveal_label() from Sarah_new_tits_call_1
    return

label Sarah_tits_reveal_label():
    $ the_person = sarah
    if not mc.location == office:
        "Your phone rings. Its [the_person.possessive_title]. You answer it."
        the_person.char "Hello [the_person.mc_title], could you meet me in your office? It's urgent."
        "You put your phone in your pocket and head to your office."
        $ mc.change_location(office)
        $ mc.location.show_background()

    $ the_person.draw_person()
    "[the_person.title] steps confidently into your office."
    the_person.char "Good morning [the_person.mc_title]! Ready for our Monday meeting?"
    "Your jaw drops when you look up."
    mc.name "Wow, [the_person.title], you are awfully perky this morning!"
    "She laughs at you and smiles."
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person.char "Thank you [the_person.mc_title]. I'm sorry again about being sneaky about the whole thing. I really appreciate you letting me do this!"
    "You notice she turns and closes your office door... and then locks it."
    if the_person.outfit.tits_available():
        "[the_person.title] takes a breast in her hand, enjoying the weight of it."
        the_person.char "It is incredible. So much better than a implant, and they've gotten more sensitive too."
        "Her hand begins to idly pinch one of her nipples."
        $ the_person.change_arousal(15)
        the_person.char "Mmm. Go ahead and touch them. I want to feel your hands one me!"

    else:
        the_person.char "Do you want to give them a closer look? I mean, you are the man who made this all possible..."
        "You quickly agree."
        while the_person.outfit.get_upper_top_layer():    #If covered up, have her take her top off
            $ the_clothing = the_person.outfit.get_upper_top_layer()
            "[the_person.possessive_title] takes off her [the_clothing.name]"
            $ the_person.draw_animated_removal(the_clothing)
        $ the_clothing = None

        "Her chest now bare before you, [the_person.title] takes a breast in her hand, enjoying the weight."
        the_person.char "Go ahead and touch them. These are so much better than implants, I can't believe how good they feel. And they are so sensitive too..."
    "With both hands your reach and cup her considerable chest. The skin is soft and pliable in your hands."
    $ the_person.change_arousal(15)
    the_person.char "Mmmmmm. Don't be shy! Play with them a bit. It feels so goooood..."
    "You begin to knead her chest a bit rougher now. She gasps as you struggle to get all of her pleasant titflesh in your hands."
    $ the_person.change_arousal(15)
    the_person.char "Oh god, you are getting me so hot..."
    "Her knees buckle for a second when you start to play with her nipples. You pinch and roll them in your fingers."
    $ the_person.change_arousal(15)
    the_person.char "Ah! Stop! God that feels amazing. But there's something else I want to try..."
    mc.name "Oh? What is that?"
    the_person.char "Well, I've tried this a couple times before but to be honest my chest was so small I don't think it was very good for the guy but... I want your cock between my tits!"
    mc.name "That sounds hot. Lets do it!"
    "You turn your chair to the side and [the_person.title] gets on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] eagerly begins opening your pants. She pulls out your cock and gives it a few gentle strokes."
    the_person.char "I can't believe I'm finally doing this. This all feels like a dream!"
    "She looks up at you from her knees. She looks you right in the eyes as she leans forward and slides your cock between her pillowy tits."
    "With both hands holding her breasts together, she slowly starts to move her pillowy flesh up and down your erection."
    call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_sarah_tits_reveal_1
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person.char "Oh my god, I came so hard... I can't believe it. That felt so good! I need to do that again soon!"
        if the_person.get_opinion_score("showing her tits") < 2:
            $ the_person.update_opinion_with_score("showing her tits", 2)
    else:
        the_person.char "Mmm that was so hot. I can't wait to try that again..."
        if the_person.get_opinion_score("showing her tits") < 1:
            $ the_person.update_opinion_with_score("showing her tits", 1)
    the_person.char "Okay... let me go get cleaned up... then I'll come back and we can start our regular Monday meeting!"
    $ the_person.draw_person(position = "walking_away")
    "She gets up and leaves the room. You smile to yourself, thinking about how good her new tits felt around your cock."
    $ the_person.apply_planned_outfit()
    return

label Sarah_stripclub_story_label():
    $ the_person = sarah
    $ the_person.planned_outfit = get_sarah_date_outfit_two()
    $ the_person.apply_planned_outfit()

    $ scene_manager = Scene()
    #TODO going out outfit
    "Lost in thought as you get your work done in the silence of the weekend, a sudden voice startles you."
    the_person.char "[the_person.mc_title]! You crazy workaholic, let's go blow off some steam!"
    "You look up and see [the_person.title] standing in the doorway."
    $ scene_manager.add_actor(the_person, emotion = "happy")
    if sarah.event_triggers_dict["epic_tits_progress"] != -1:
        "You still aren't quite used to her enhanced chest size. You realize you are blatantly checking her out as she stands in the door."
        the_person.char "Mmm, I've been getting exactly that look from a ton of guys lately... and a few girls to."
        the_person.char "It's been great! I can't thank you enough for helping this happen. I think I might know a way to repay you a little bit though..."
    else:
        "She is a quite a stunner and you realize you are blatantly checking her out as she stands in the door."
        the_person.char "Mmm, I like the way you look at me and just the other day I saw some girls checking me out too."
        the_person.char "Thank you for convincing me to stay true to myself. I think I might know a way to repay you a little bit though..."

    mc.name "It's okay, you don't have to do anything, I was just happy to help!"
    if the_person.event_triggers_dict.get("dating_path", False) == True:
        the_person.char "Hah! [the_person.mc_title], that's one of the things I love about you. You are so giving of yourself and your resources."
        $ the_person.change_love(10)
    else:
        the_person.char "Hey now, friends with benefits means we both get benefits, but lately it feels like I've been getting most of the benefits!"
        the_person.char "This arrangement has been great, I don't it to end just because I'm the only one getting anything out of it."
    the_person.char "This time though, you are going to have to let me do something for you. Don't worry, we're both gonna like it."
    mc.name "Ok, what did you have in mind?"
    the_person.char "You'll just have to see! Let's go!"

    $ mc.change_location(downtown)
    $ mc.location.show_background()
    if the_person.event_triggers_dict.get("dating_path", False) == True:
        "[the_person.possessive_title] holds your hand as you leave the lab and head downtown."
        "You pass the bar you usually go to. Where is this girl taking you?"
    else:
        "[the_person.possessive_title] leads the way as you leave the lab and head downtown."
        "You pass the bar you usually go to. You wonder what this crazy girl has in mind for tonight."
    "Soon you walk up to a building and [the_person.title] comes to a stop. The sign out from says [strip_club.formalName]."
    "Wow, a strip club? This could be interesting. You decide to tease her."

    # if MC has not yet discovered this place, make it visible on the map
    if not strip_club.visible:
        $ strip_club.visible = True

    mc.name "You know, its against company policy to be moonlighting at a place like this. Even with a body like yours."
    the_person.char "Ha! No I haven't been working here, I just thought it would be fun to watch a couple shows."
    mc.name "Sounds great!"

    $ mc.change_location(strip_club)
    $ mc.location.show_background()

    "You head inside. Your senses are assaulted by everything going on. The loud bass music thumps in your ears. On stage you see a girl shaking her ass for a group of guys."
    "You check around quickly... looks like [the_person.title] is one of the few women in the crowd with you."
    the_person.char "Come on, let's grab a table to the side before we decide what to do first!"
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You sit down across from [the_person.possessive_title] in a booth."
    the_person.char "Alright, lets just watch the girls from here for a little bit. I'm going to buy you a private dance before we go."
    mc.name "That's... very generous of you. You know you don't have to do that, right?"
    the_person.char "Sure but, it's not like I'm not going to have fun while we're here too. I've heard the girls here are hot!"
    "It's been clear for a while now that [the_person.title] has an interest in both men and women. It's cute to see her coming out of her shell a bit and enjoying her sexuality."
    the_person.char "Oh look! Here comes a girl now!"
    "Your eyes are drawn to the stage."
    call watch_strip_show(the_person) from Sarah_strip_show_call_1
    the_person.char "Wow! That was impressive! I've never been to a place like this before, but I can see why guys like it so much..."
    "As she finishes her sentence, one of the guys who had been around the stage gets a little too close to your table. You can see him checking out [the_person.title]"
    "???" "Hey there, aren't you a doll! Whaddya say to a private dance in the back? Not sure how much this guy is paying, but I could make it worth your while..."
    if the_person.event_triggers_dict.get("dating_path", False) == True:
        the_person.char "Not likely! I'm reserved for my boyfriend here."
    else:
        the_person.char "Not likely!"
        "???" "Come on baby, I bet I can pay you better than what this guy is payin' you to be here with him!"
        the_person.char "Yeah right! This guy owns his own pharmaceutical business. Move along now."
    "You get ready to add in to the conversation, but the guy gets the point."
    if sarah.event_triggers_dict.get("epic_tits_progress", 0) >= 2: # only when she got the big boobs
        "???" "Damn, alright. Enjoy those tits mister, they look fantastic."
    else:
        "???" "Damn, alright. Have a nice time mister, she's gorgeous."
    $ the_person.change_happiness(5)
    "The guy wanders off. [the_person.possessive_title] has a smug look on her face."
    the_person.char "Damn right they're fantastic. What do you think, [the_person.mc_title]. Are you gonna enjoy these tits later?"
    "Before you can respond, the music starts up again and another girl comes out on the stage."
    the_person.char "Oh! Here we go again!"
    call watch_strip_show(the_person) from Sarah_strip_show_call_2
    $ showgirl = _return
    if showgirl.has_large_tits():
        the_person.char "Damn! That girl had a nice chest. Wish I could get my hands on her..."
    else:
        the_person.char "That was impressive! Even though her chest was small, she certainly knows how to work her body. Wish I could get my hands on her..."
    if showgirl is cousin:
        "While it was true, you aren't sure you have the guts to tell her that the girl on stage was your cousin, [cousin.title]."
        "Either way, she seemed to really enjoy her performance."
    else:
        "She seems to have really enjoyed this particular performance."
    "You enjoy your time with [the_person.title]. As girls come and go off the stage you both remark on what you like or didn't like about each performance."
    the_person.char "Mmm, I think I've seen enough. So, want to go back to the private room for a lap dance? Any girls in particular stand out to you?"
    "You think about it for a second. Then decide to change it up a little."
    mc.name "I've got a better idea. Why don't we both get a private dance?"
    "[the_person.title] raises an eyebrow"
    the_person.char "You mean... I figured that they only did private dances for guys..."
    mc.name "Nah, if you give me a minute, I bet I can get it setup."
    the_person.char "But I don't have the money for two..."
    mc.name "Ah! Forget about it. I'll put it on the company card. This is a team building exercise, right?"
    the_person.char "Team building... right! I can get behind that!"
    mc.name "Ok, I'll be right back."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    if get_strip_club_foreclosed_stage() < 5:
        "You get up and head over to the counter where the owner is."
    else:
        "You get up and head over to the counter and talk with the manager."
    if cousin.event_triggers_dict["blackmail_level"] >= 2 and cousin.has_role(stripper_role):
        if showgirl is cousin:
            "You arrange two private lap dances. For [the_person.title], you get [cousin.possessive_title], since she enjoyed her so much."
        else:
            "You arrange two private lap dances. For [the_person.title], you ask for the girl that did the second dance on stage."
            "You smile when you look at the list of stage names for the different strippers. You see the one that must be referring to [cousin.title] and pick her for yours."
    "You arrange two private lap dances. For [the_person.title], you ask for the girl that did the second dance on stage. You pick a random girl for yours."
    $ mc.business.change_funds(-200)
    "You go to the back, and find a room with two chairs facing each other. [the_person.title] sits across from you."
    $ scene_manager.add_actor(the_person, position = "sitting", emotion = "happy", character_placement = character_left_flipped)
    the_person.char "Mmm, I'm so nervous..."
    #TODO make a variant on character left that is a close to Sarah so it looks more like an actual lap dance.
    $ showgirl.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ scene_manager.add_actor(showgirl, character_placement = character_center_flipped)
    if cousin.event_triggers_dict["blackmail_level"] >= 2 and cousin.has_role(stripper_role):  #We have blackmailed Gabrielle about stripping already#
        if showgirl is cousin:
            $ showgirl_2 = get_random_from_list([x for x in stripclub_strippers if x != showgirl])
        else:
            $ showgirl_2 = cousin
    else:
        $ showgirl_2 = get_random_from_list([x for x in stripclub_strippers if x != showgirl])
    $ showgirl_2.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ scene_manager.add_actor(showgirl_2)
    showgirl_2.char "Alright! We got a couple in here tonight, this should be fun!"
    if showgirl_2 is cousin:
        "Suddenly, [showgirl_2.title] realizes its you she is getting ready to dance for."
        "[showgirl_2.possessive_title] lowers her face to your ear and whispers in it."
        showgirl_2.char "What the fuck? You want me to give you a lap dance? Here??? In front of your little bimbo? You're a sick fuck..."
        mc.name "Don't worry, I'll make it worth it."
        showgirl_2.char "You better..."
        "She stands back up and acts as if nothing happened."
    if showgirl is cousin:
        "You see [showgirl.title] looking over to you, realizing that you are gonna be in the room as she performs for [the_person.title]"
        "She gives you a quick wink."
    showgirl.char "Alright, lets get the fun started!"
    $ scene_manager.update_actor(showgirl_2, position = "kneeling1")
    "Your stripper gets on your lap. She starts to take off her top."
    $ scene_manager.strip_actor_outfit(showgirl_2, exclude_lower = True, exclude_feet = True)
    "With her tits free, she begins to gyrate them back and forth, right in front of your face. They wobble appealingly."
    $ scene_manager.update_actor(showgirl, position = "blowjob")
    "You glance over and notice the girl in front of [the_person.title] is doing something similar."
    $ scene_manager.strip_actor_outfit(showgirl, exclude_lower = True, exclude_feet = True)
    showgirl_2.char "For $100, you two can play with our tits for a bit."
    if showgirl_2 is cousin:
        "[showgirl_2.title] lowers her lips to your ear again."
        showgirl_2.char "Don't you wanna grab your cousin's tits, pervert?"
    "You see [the_person.title] look over at you. You can see her mouth the word 'please'"
    mc.name "That sounds fair."
    "You grab $100 and put it in the tip jar."
    $ mc.business.change_funds(-100)
    "Before you finish putting the money in the jar, you notice that [the_person.title] has her hands all over her stripper's chest."
    "She seems to be really enjoying the show so far!"
    $ mc.change_arousal(10)
    $ the_person.change_arousal(12)
    if showgirl_2 is cousin:
        "You reach up and grope [showgirl_2.possessive_title]'s tits. You're mesmerized by how soft and warm they are."
    else:
        "You reach up and begin to fondle your stripper's tits. They are so soft and warm. They feel amazing."
    "After a while, it's time to change things up. Both strippers get up and turn to so their backs are facing you and [the_person.title]."
    $ scene_manager.update_actor(showgirl_2, position = "standing_doggy")
    $ scene_manager.update_actor(showgirl, position = "standing_doggy")
    "Your girl puts her ass against your chest and starts to wiggle her hips back and forth as she slowly works herself down your body."
    "Soon she is working your erection with her hips, through both of your clothes."
    "She starts to strip down her remaining clothing."
    $ scene_manager.strip_actor_outfit(showgirl_2)
    "You notice that [the_person.title] and her stripper are in a similar state."
    $ scene_manager.strip_actor_outfit(showgirl)
    "Her ass bare now, you find it difficult to restrain your hands from molesting the girl in front of you."
    $ mc.change_arousal(15)
    $ the_person.change_arousal(20)
    showgirl_2.char "For $200, you two can touch, anywhere you want other than pussies while we dance for you."
    if showgirl_2 is cousin and showgirl_2.sluttiness > 50:
        "[showgirl_2.title] looks bank and whispers at you."
        showgirl_2.char "Maybe later you can touch me there..."
    "You don't hesitate. You grab $200 and put it in the tip jar."
    $ mc.business.change_funds(-200)
    "[the_person.title] sees you do it and immediately starts to run her hands along her girl's hips."
    "You do the same. The girl in front of you continues to work her hips back and forth across your erection as you run your hands along her hips."
    "You cup and grab her ass a few times when you have the opportunity. Her hips sway enticingly."
    "You look up and see [the_person.title] hands roaming all over her stripper's body. She plays with her tits for a while, then runs her hands along her sides and down her legs."
    $ mc.change_arousal(40)
    $ the_person.change_arousal(45)
    "It's beginning to get hard to control yourself, you are getting close to cumming, when it is time for the lap dance to end."
    $ scene_manager.update_actor(showgirl, position = "stand4")
    $ scene_manager.update_actor(showgirl_2, position = "stand5")
    showgirl.char "Mmm, that was fun! It's been forever since I had a female client. They always give such loving touches..."
    if showgirl_2 is cousin and showgirl_2.sluttiness > 70:
        "[showgirl_2.possessive_title] whispers in your ear before she leaves."
        showgirl_2.char "That was fun... how soon until I get to play with your girlfriend too? Soon I hope?"
    elif showgirl_2 is cousin:
        "[showgirl_2.possessive_title] whispers in your ear before she leaves."
        showgirl_2.char "I hope your little slut doesn't realize we're related. That would be an unfortunate event, for sure..."
    "The strippers leave, leaving you and [the_person.title] alone and highly aroused."
    $ scene_manager.remove_actor(showgirl)
    $ scene_manager.remove_actor(showgirl_2)
    $ del showgirl
    $ del showgirl_2
    the_person.char "Good lord... we need to get out here! Can we go back to your place?"
    mc.name "Absolutely."
    "You both head out and are soon walking through your front door."
    $ mc.change_location(hall)
    $ mc.location.show_background()
    $ scene_manager.update_actor(the_person, position = "stand2", character_placement = character_right)
    the_person.char "Oh god I can't wait to get to your bedroom and..."
    $ scene_manager.add_actor(mom, character_placement = character_left_flipped)
    "[mom.title] pops around the corner when she hears you walking down the hall and unknowingly interrupts."
    mom.char "Hey [mom.mc_title]. You missed dinner! Leftovers are in the fridge. Oh! Hello again!"
    mc.name "Thanks, we're just going to go to my room for a bit to discuss some... work related matters."
    "You see [mom.title] quickly appraises the situation."
    mom.char "Right. Have fun talking about work stuff! HAH! Nice to see you again!"
    the_person.char "Nice to see you again too."
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[mom.possessive_title] walks away, chuckling to herself."
    $ scene_manager.remove_actor(mom)

    $ mc.change_location(bedroom)
    $ mc.location.show_background()

    "Finally, you reach your bedroom and quickly close and lock the door."
    mc.name "God I'm sorry, if you aren't in the mood anymore..."
    the_person.char "Sorry for what? Its your mom, I think its sweet."
    mc.name "So... do you wanna..."
    the_person.char "Oh fuck yeah, I'm so worked up. But first I want to try something! Why don't you sit down on the bed there."
    "You quickly sit down."
    mc.name "What do you have in mind, [the_person.title]?"
    the_person.char "I'm gonna give you a lap dance. Just like that girl at the strip club."
    if the_person.event_triggers_dict.get("dating_path", False) == True:
        the_person.char "But the difference is, you can touch me all you want to!"
        mc.name "Mmm, don't mind if I do."
    else:
        the_person.char "But remember, no touching!"
        mc.name "No promises."
    $ scene_manager.update_actor(the_person, position = "kneeling1")
    "[the_person.title] climbs up on your lap."

    if the_person.outfit.tits_available():
        "She runs her hands through your hair and brings your face up to her naked, heaving chest."
    else:
        "She begins to undress her top half right in front of you, letting you watch as she exposes her soft skin."
        $ scene_manager.strip_actor_outfit(the_person, exclude_lower = True, exclude_feet = True)
        "As she pulls off her last piece of clothing, she runs her hands through your hair and brings your face to her naked, heaving chest."

    if the_person.event_triggers_dict.get("dating_path", False) == True:
        "Your hands naturally reach up and begin to fondle [the_person.possessive_title]'s breasts."
        the_person.char "Mmmm that's it baby. It feels so good when you touch me there."
        $ the_person.change_arousal(10)
    else:
        "Your hands begin to move towards [the_person.possessive_title]'s breasts, but she slaps your hands away."
        the_person.char "Hey! You know the rules, no touching!"
        "You quickly lower your hands to your sides."
    "[the_person.title] is slowly grinding herself in circles against your lap. The heat of her body against yours is really getting you worked up."
    "With the excitement from the strip club earlier, you are starting to ache for some relief."
    $ mc.change_arousal(10)
    $ scene_manager.update_actor(the_person, position = "back_peek")
    "[the_person.possessive_title] stands up and turns away from you."
    if the_person.outfit.vagina_available():
        "Her hips sway back forth. Her shapely ass inches from your face makes a tantalizing target."
        $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
    else:
        "She begins to slowly strip her bottom half down in front of you, swaying her hips tantalizingly as she does so."
        $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
        "Now naked in front of you, you can't tear your eyes away from her bare ass, mere inches from your face."
    "Her pussy is dripping with excitement. It looks like you could probably make her cum in seconds, she is so turned on."
    the_person.char "Oh god I'm so hot... I can't take it!"
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    "She bends over and pushes her ass back against your face. You immediately begin to lick and probe her slit with your tongue."
    the_person.char "It was so hot having those girls strip for us earlier... I need to cum, make me cum!"
    "You reach up and grab her hips with your hands. You give one cheek a hard spank while your tongue snakes its way inside of her."
    $ the_person.change_arousal(30)
    the_person.char "Yes! Oh fuck I'm gonna cum!!!"
    $ mc.listener_system.fire_event("girl_climax", the_person = the_person)
    $ the_person.change_happiness(5)
    $ the_person.change_obedience(5)
    $ the_person.change_slut_temp(5)
    "You grip her hips roughly to hold her still as you bring her to a climax. Her knees start to buckle but you hold her ass firmly in place."
    "She gives a low, steady moan when she finally finishes climaxing."
    $ the_person.change_arousal(-(the_person.arousal / 3))
    the_person.char "Oh god I need that so bad... I think... you're gonna have to take over, [the_person.mc_title]."
    "The excitement of the evening has you on edge, so you grab [the_person.title] and throw her down on the bed."
    $ scene_manager.update_actor(the_person, position = "doggy")
    "You quickly strip out of your clothes and get behind her, lining yourself up with her slit."
    if mc.energy < 30:
        $ mc.energy = 30
    call fuck_person(the_person, start_position = doggy, start_object = make_bed(), skip_intro = False, girl_in_charge = False, position_locked = True) from _call_sex_description_stripclub_aftermath_1
    "When you finish with her, [the_person.title] collapses in the bed."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You cuddle up next to her as you both catch your breath."
    #complex decision tree here.
    # If dating path, have her ask to be your girlfriend officially.
    # If she is already dating someone else, have her break up with them
    # If she is already married, turn it into an affaire
    # if she is engaged, have her break it off.
    # If not dating path, she recovers, then heads out
    if the_person.has_role(girlfriend_role):  #You are already dating her via other means. She just cuddles up with you.
        "As you both recover, [the_person.possessive_title] starts kissing you along your neck, then whispers in your ear."
        the_person.char "Thank you for the good time tonight. I love you."
        mc.name "I love you too."

    elif the_person.event_triggers_dict.get("dating_path", False) == True:
        "After you both recover, you continue to lie together, enjoying your flesh being against one another. She seems deep in though, but eventually asks you a question."
        if the_person.relationship == "Single":
            the_person.char "So... we've done this a couple times now and... I know this is usually where the man kind of takes the lead but umm..."
            the_person.char "Every time I think about you, and being with you, I get so happy, and I start smiling."
            the_person.char "Is it... can we just make it official? I want to be with you. I want to be your girlfriend!"
            menu:
                "Make it official":
                    the_person.char "Yes! Oh my god you have no idea how happy that makes me to hear, that you feel the same way!"
                    $ the_person.change_happiness(15)
                    $ the_person.change_love(5)
                    "She kisses you, and you kiss her back."
                    $ the_person.add_role(girlfriend_role)

                "Let's just be friends":
                    the_person.char "Ah... okay wow, I guess I was just... totally misinterpreting things between us..."
                    $ the_person.change_happiness(-15)
                    $ the_person.change_love(-20)
                    $ the_person.event_triggers_dict["dating_path"] = False
                    the_person.char "I didn't realize you just wanted things to be strictly physical between us. Is that what you want? Friends with benefits?"
                    mc.name "Yes that is what I am looking for right now."
                    the_person.char "Okay... I'm sorry I didn't realize. But I think I can manage that."

        elif the_person.relationship == "Married":
            the_person.char "So... we've done this a couple of times. I know, I'm a married woman, but I can't stop thinking about you."
            the_person.char "Every time I think about you, I get a little bit wet thinking about what you do to me."
            the_person.char "Is this something you want to continue? I can't leave my husband but you can fuck me anytime you want!"
            menu:
                "Have an affair":
                    the_person.char "Okay. Wow, I never thought I would do this..."
                    "She reaches down and gives your softened cock a few strokes."
                    the_person.char "But the things you do to me... my husband doesn't even come close!"
                    $ the_person.add_role(affair_role)
                    $ the_person.change_slut_temp(2)
                "Let's keep it casual":
                    the_person.char "Ah, okay. So like, friends with benefits? Is that what we are talking about here?"
                    mc.name "Exactly."
                    the_person.char "Okay. That actually makes things a little easier for me. I can manage that!"
                    the_person.char "And if my husband ever asks, I'm just with friends!"
                    $ the_person.event_triggers_dict["dating_path"] = False
        else:       #She is a girlfriend or a fiancee
            the_person.char "So... we've done this a couple of times. I know, I'm seeing someone else right now, but I can't stop thinking about you."
            the_person.char "Honestly, if you gave the word, I would call him up and dump him right now so that we could be together!"
            the_person.char "So... should I do that? I just want to be your girlfriend!"
            menu:
                "Dump him for me":
                    "[the_person.title] takes a deep breath, then slowly gets up."
                    $ scene_manager.update_actor(the_person, position = "walking_away")
                    the_person.char "Okay. For you, I'll do it. Here we go."
                    "You watch as she dials her man. She talks quietly into her phone, so you can't make out everything she is saying."
                    "It takes her several minutes, and you hear her apologize a few times, but eventually finishes and hangs up her phone."
                    "She crawls back into bed beside you."
                    $ scene_manager.update_actor(the_person, position = "missionary")
                    "Well, it's official. I'm all yours now!"
                    python:
                        the_person.add_role(girlfriend_role)
                        the_person.change_stats(love = 10, obedience = 5)
                "Let's keep it casual":
                    the_person.char "Ah, okay. So like, friends with benefits? Is that what we are talking about here?"
                    mc.name "Exactly."
                    the_person.char "Okay. That actually makes things a little easier for me. I can manage that!"
                    $ the_person.event_triggers_dict["dating_path"] = False

    else:
        "As you both recover, [the_person.possessive_title] just lays back and enjoys the warmth of your skin."
        the_person.char "Mmmm, that was such a fun night, [the_person.mc_title]. I don't want to get up..."
    $ the_person.event_triggers_dict["stripclub_progress"] = 1
    $ staying_over = False
    if the_person.has_role(girlfriend_role):
        the_person.char "It feels so good to be next to you, I could lay like this all night."
        mc.name "Why don't you? Just spend the night here."
        the_person.char "Oh! That's a great idea!"
        $ staying_over = True
    elif the_person.has_role(affair_role):
        the_person.char "It feels so good to be next to you, but I need to get home."
        mc.name "You don't have to. Just spend the night here."
        the_person.char "I'm sorry I can't. Thanks for the offer though!"
    else:
        the_person.char "I need to get going... I guess. Thanks for the evening though. It was great!"
        mc.name "You don't have to. Just spend the night here."
        the_person.char "That's tempting, believe me, but I need to get home. Thanks for the offer!"
    if staying_over:
        $ the_person.next_day_outfit = the_person.planned_outfit # she stays the night so she will have to wear the same outfit again
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "Worn out from your date with [the_person.possessive_title], you cuddle up with her and quickly fall asleep."
        call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_overnight_after_stripclub
        call Sarah_spend_the_night() from sarah_stripclub_spend_the_night_sequence
    else:
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand3")
        "You lay on your bed and watch as [the_person.possessive_title] slowly gets her clothes on. She says goodbye then lets herself out."
        $ scene_manager.remove_actor(the_person)

    $ add_sarah_threesome_request_action()
    $ scene_manager.clear_scene()
    return "Advance Time"

label Sarah_threesome_request_label():
    $ scene_manager = Scene()
    $ the_person = sarah
    $ gossip_target = get_random_employees(1, exclude_list = [sarah], slut_required = 50)
    if gossip_target is None:
        return

    "Another Saturday, another extra workday for you. You are hardly surprised when you here [the_person.title]'s familiar voice."
    the_person.char "Hey [the_person.mc_title]. I figured you'd be around here."
    $ scene_manager.add_actor(the_person)
    mc.name "Hello [the_person.title]."
    if the_person.has_role(girlfriend_role):
        "You admire your girlfriend as she stands in the door. God she is sexy"
    elif the_person.has_role(affair_role):
        "You admire your mistress as she stands in the door. It's so hot fucking a taken woman."
    else:
        "You admire [the_person.title] as she stands in the door."
    "You notice she is carrying a bottle of something."
    mc.name "Is that... Scotch?"
    the_person.char "Yup! I'm like... totally not suggesting we just get wasted right here or anything..."
    "You feel yourself raise an eyebrow."
    the_person.char "But uhh, you know, if we DID happen to get wasted and banged in every room in the business, I'm pretty sure I would be okay with that."
    "Jesus, this girl is insatiable. Its amazing!"
    the_person.char "You got any shot glasses?"
    mc.name "No... I actually don't have any around."
    "You think about a possible solution."
    if not mc.location == mc.business.r_div:
        mc.name "Why don't we start down in research? I'm sure we have some extra beakers we could use."
        the_person.char "Let's go!"
        $ mc.change_location(rd_division)
        $ mc.location.show_background()
    mc.name "Pull up a seat."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You grab a couple vials from one of the desks. [the_person.possessive_title] hands you the bottle and you pour the first round."
    mc.name "Cheers!"
    the_person.char "Cheers!"
    "You tap your vials together and take your shots together. It burns on the way down, but the aftertaste is smooth."
    mc.name "Mmm, that's a good scotch."
    the_person.char "Thanks! I had to look for recommendations. I usually drink more girly drinks, but a good scotch is good to drink neat."
    "You pour the next round."
    the_person.char "Oh, in a hurry to get me tipsy, are we? You wouldn't be looking to take advantage of little ol' me, are you sir?"
    "She cracks a smile as she plays innocent."
    mc.name "You see right through me miss. Suppose I'll have to find some other unsuspecting lass."
    "She takes the vial from your hand with round two."
    the_person.char "Oh, that won't be necessary sir."
    "You clink your vials together again and drain them both."
    "As you sit there drinking you both start to gossip about drama around the office."
    "Being in HR, [the_person.title] knows a surprising amount of details of the other girls and their private lives."
    "You drink, gossip, and laugh with [the_person.possessive_title] for a while."
    "You aren't sure how many shots you've both done. You look at the bottle. There's only about a third of it left! That feels like a lot, but you're not sure, maybe that's a normal amount."
    "[the_person.title] is talking about a meeting she had recently an employee."
    the_person.char "So then I said... what exactly am I supposed to do with these pictures of [gossip_target.name] getting fucked in the backseat of Jeep Wrangler?"
    the_person.char "And she said... nothing! She just thought the pictures were hot and so she was showing all the girls in the office."
    the_person.char "So I said, that is pretty hot... can you text me those? Hahahahaha."
    mc.name "That's great... so do you have them?"
    the_person.char "Oh hell yeah, one sec..."
    "[the_person.title] fumbles around on her phone for a second. She is pretty drunk, so it takes her a while to find them."
    $ gossip_target.strip_outfit_to_max_sluttiness()
    $ scene_manager.add_actor(gossip_target, position = "cowgirl", emotion = "orgasm", character_placement = character_center)
    "She shows you her phone. It shows [gossip_target.title] in the backseat of a Jeep, riding some guy you don't recognize while he is sitting."
    mc.name "Damn! She looks like she is enjoying herself there!"
    "You enjoy the picture for a few more moments before [the_person.title] takes her phone back."
    $ scene_manager.remove_actor(gossip_target)
    $ del gossip_target
    the_person.char "God, I know. She is so hot, wish I could get my hands on her..."
    "So, at this point, [the_person.possessive_title] has brought it up multiple times that she would like to have some action with another girl sometime."
    "As you think through your business and all the people you have interacted with, you are pretty sure you have some girls who would love to join a threesome with you and [the_person.title]"
    mc.name "So, I know we've talked about this before, but, is a threesome still something that you would be interested in doing sometime?"
    the_person.char "Oh god I would do anything, just to try it once. I know it may not turn out to be as good as I hope, but, I just want to TRY, you know!?!"
    "You don't remember pouring this shot, but you grab the drink in front of you and drain it."
    mc.name "Alright, how about this. This time, next week, I'll have something setup."
    the_person.char "What? You mean it?"
    mc.name "Absolutely."
    the_person.char "That would be incredible... but... I mean, I feel like I have a right to know... who do you have in mind?"
    # use new menu layout for selecting people
    call screen enhanced_main_choice_display(build_menu_items([["Request Threesome From"] + get_Sarah_willing_threesome_list()], draw_hearts_for_people = False))
    $ person_choice = _return
    $ scene_manager.update_actor(the_person, position = "sitting")
    if person_choice.is_employee():
        mc.name "I was thinking about [person_choice.title]. She seems like she would be down for just about anything, to be honest."
        the_person.char "Oh! She's cute! Damn, that would be great!"
    elif person_choice is mom:
        mc.name "So, uh, this might sound kind of weird, but, I actually have a family member in mind."
        "[the_person.title] stays quiet for a moment before she responds."
        the_person.char "I mean... that's a little weird, sure. But, I mean, we're already pushing boundaries having a threesome in the first place."
        the_person.char "Who did you have in mind?"
        mc.name "It's actually my mom."
        the_person.char "Oh! Well, I mean, she DOES have a really nice body..."
    elif person_choice is lily:
        mc.name "So, uh, this might sound kind of weird, but, I actually have a family member in mind."
        "[the_person.title] stays quiet for a moment before she responds."
        the_person.char "I mean... that's a little weird, sure. But, I mean, we're already pushing boundaries having a threesome in the first place."
        the_person.char "Who did you have in mind?"
        mc.name "It's actually my sister, [lily.title]."
        the_person.char "Oh! Well, I mean, she DOES have a really nice body..."
    elif person_choice is cousin:
        "You consider carefully whether or not you should reveal that [cousin.title] is your cousin, but you decide not to."
        mc.name "Actually, one of the strippers at the club we went to the other night is a good friend of mine."
        the_person.char "Ah. Are you friends with a lot of... strippers?"
        mc.name "Ha! Not really, but she and I go back a ways. And she actually owes me a favor or two."
    elif person_choice is aunt:
        mc.name "So, uh, this might sound kind of weird, but, I actually have a family member in mind."
        "[the_person.title] stays quiet for a moment before she responds."
        the_person.char "I mean... that's a little weird, sure. But, I mean, we're already pushing boundaries having a threesome in the first place."
        the_person.char "Who did you have in mind?"
        mc.name "It's actually my aunt. She's been going through a rough patch after her divorce. I think it would really help pick her up."
        the_person.char "Oh! Well, I mean, an aunt is fairly distant relation. And it sounds like she could use a good opportunity to cut loose..."
    elif person_choice is starbuck:
        if starbuck.shop_progress_stage >= 1:
            mc.name "I actually have a joint venture in another business. There's a woman who owns the mall sex shop, and I invested a decent some of money in it recently."
            the_person.char "Ah, so, she's a business partner?"
        else:
            mc.name "I actually have a friend who owns the sex shop, over in the mall."
            the_person.char "Ah, so, she's another small business owner?"
        mc.name "Yeah. Her husband died a while ago, and she opened the shop in memory of him. It's a little weird, but also kinda sweet."
        mc.name "Anyway, she is very open to experimentation. I think a threesome would be right up her alley, so to speak."
        the_person.char "Aww, you are a sweetheart."
    elif person_choice is nora:
        mc.name "I have an old college professor, who helped develop some of the original formulas that we make here."
        mc.name "She works full time over at the university, and is overworked a bit. I'm sure she would appreciate the chance to blow off some steam with us."
    "A few moments go by as she thinks about it."
    the_person.char "Okay! Let's do it!"

    # Make threesome request even on talk event and add it here.
    $ sarah.event_triggers_dict["initial_threesome_target"] = person_choice
    $ sarah.event_triggers_dict["initial_threesome_arranged"] = False

    $ add_sarah_arrange_threesome_action(person_choice)

    $ add_sarah_initial_threesome_action()

    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person.char "Oh man, all this talk about sex is starting to get me all hot. Or is it just warm in here?"
    "Without prompting, [the_person.possessive_title] stands up and starts stripping down."
    $ scene_manager.strip_actor_outfit(the_person)
    the_person.char "Aaahhhh, that's better."
    "You cock is getting hard, looking at [the_person.title], completely naked in front of you."
    call fuck_person(the_person) from _sarah_threesome_request_aftermath_1
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.title] takes it easy for a moment, enjoying the afterglow of her orgasm."
    the_person.char "Mmm, that was hot as always."
    $ the_person.apply_planned_outfit()
    $ scene_manager.update_actor(the_person, position = "stand3")
    if the_person.has_role(girlfriend_role):
        pass
    elif the_person.has_role(affair_role):
        the_person.char "I don't want to go... but I know I probably should. I'm sure someone will be waiting for be to get home..."
        $ scene_manager.update_actor(the_person, position = "stand3")
        the_person.char "Don't forget to talk to [person_choice.name]! I'll be looking forward to next Saturday!"
        "You both say goodbye, and [the_person.title] leaves you alone in the research lab."
        $ scene_manager.clear_scene()
        $ del person_choice
        return
    else:
        the_person.char "God, you wore me out. I know I promised every room, but I don't think I can go on. I think I'd better catch a cab home..."
        $ scene_manager.update_actor(the_person, position = "stand3")
        the_person.char "Don't forget to talk to [person_choice.name]! I'll be looking forward to next Saturday!"
        "You both say goodbye, and [the_person.title] leaves you alone in the research lab."
        $ scene_manager.clear_scene()
        $ del person_choice
        return
    #Assume everything from her on, sarah is girlfriend status.
    the_person.char "God babe, you wore me out. I know I promised every room, but I don't think I can go on. I think I'd better catch a cab home..."
    mc.name "Why don't I just get us a cab back to my place? I'm in no condition to walk home either. You can stay over."
    the_person.char "Ah, charming, AND economical! That's my man."
    "You call the cab and soon it arrives. You give each other little gropes and quick kisses in the back of the cab, but manage to keep things from getting to heated."
    "You get home and walk through the front door."

    $ mc.change_location(hall)
    $ mc.location.show_background()

    if person_choice is aunt:
        $ scene_manager.add_actor(mom, character_placement = character_left_flipped, position = "sitting")
        $ scene_manager.add_actor(aunt, character_placement = character_center, position = "sitting")
        "As you walk down the hall, you see that [aunt.possessive_title] is sitting with [mom.possessive_title], having coffee."
        "They notice you as you enter."
        aunt.char "Oh hey! Good to see you [aunt.mc_title]. And who is this?"
        mc.name "Hey [mom.title], [aunt.title]. This is my girlfriend, [the_person.title]"
        mc.name "[the_person.title], you've met my mom, and THIS is my AUNT, [aunt.title]."
        the_person.char "Nice to meet you... OH!"
        "It suddenly dawns on her that this is who you are planning to hook up with next week..."
        the_person.char "Wow, you are beautiful. It's a pleasure!"
        "[the_person.title] is blatantly checking out [aunt.possessive_title]. Being drunk, she's lost her subtlety..."
        aunt.char "It's nice to meet you too!"
        "She actually seems to be appreciating the attention."
        $ aunt.change_happiness(5)
        mc.name "Ah, well, we've been drinking so uh, I think we're gonna go sleep it off now."
        mom.char "Okay! Make sure you drink a glass of water so you aren't hungover in the morning. Goodnight you two!"
        "As you turn to leave the room, you overhear [mom.possessive_title] whispering to your aunt."
        mom.char "She's been over a few times... I think they are great together..."
        $ scene_manager.remove_actor(mom)
        $ scene_manager.remove_actor(aunt)
    elif person_choice is mom:
        $ scene_manager.add_actor(mom, character_placement = character_left, position = "sitting")
        "As you walk down the hall past the kitchen, you see [mom.possessive_title] sitting at the table, having a cup of coffee. She notices you in the hall."
        mom.char "Oh, hey [mom.mc_title]."
        "She notices [the_person.possessive_title] walking beside you."
        mom.char "Oh! Hello again dear! It's great to see you!"
        "You both step into the kitchen for a moment."
        mc.name "Hey [mom.title]. I told my girlfriend, [the_person.title] she could spend the night, is that okay?"
        mom.char "Girlfriend? Oh that's great! Yes of course she's welcome to stay here anytime!"
        the_person.char "Thank you! Might I say you are looking sexy tonight."
        "[the_person.possessive_title] is blatantly checking out [mom.possessive_title]. Suggesting her for the threesome has changed the way she looks at her now."
        "However, being drunk, [the_person.title] has lost her subtlety."
        mom.char "Ha! That's sweet of you to say."
        mc.name "We've had a few drinks. I think we're gonna go sleep it off. Goodnight!"
        mom.char "Make sure you drink a glass of water so you aren't hungover in the morning. Goodnight you two!"
        $ scene_manager.remove_actor(mom)
    elif person_choice is lily:
        $ scene_manager.add_actor(mom, character_placement = character_left_flipped, position = "sitting")
        $ scene_manager.add_actor(lily, character_placement = character_center, position = "sitting")
        "As you walk down the hall and past the living room, you see [mom.possessive_title] and [lily.possessive_title] sitting at the couch, watching a movie."
        "They notice you walking by."
        lily.char "Hey Bro, we're watching a movie if you wanna join us... Wow! Whose the girl?"
        mc.name "Hey [lily.title], this is my girlfriend [the_person.title]."
        lily.char "Wow, you didn't tell me you had a girlfriend!"
        "[lily.title] is checking out [the_person.title]. You look at her and see she is doing the same."
        lily.char "Nice to meet you! Damn you did good bro!"
        the_person.char "Ah, nice to meet you! [the_person.mc_title] you didn't tell me your sister was so hot."
        "[mom.possessive_title] clears her throat, trying to clear some of the sexual tension in the air."
        mc.name "Right. Anyway, we've been doing some drinking, I think we're gonna go try and sleep it off. Goodnight!"
        mom.char "Make sure you drink a glass of water so you aren't hungover in the morning. Goodnight you two!"
        "As you and [the_person.possessive_title] walk away, you can feel [lily.possessive_title]'s eyes lingering on the two of you."
        $ scene_manager.remove_actor(mom)
        $ scene_manager.remove_actor(lily)
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You get to your room. When you walk in, [the_person.possessive_title] starts to strip down."
    the_person.char "Hope you don't mind if I sleep naked!"
    mc.name "Umm, that would actually be ideal, if I'm being honest."
    $ scene_manager.strip_actor_outfit(the_person)
    $ scene_manager.update_actor(the_person, position = "missionary")
    "She flops down on your bed. You hop in bed next to her."
    "You run your hands along her body as you snuggle up next to her. Her skin is so soft."
    "Her breathing is getting deep... soon you hear... is that snoring?"
    "You look at her face. She passed out."
    "Worn out, you cuddle up with her and quickly fall asleep as well."
    $ scene_manager.clear_scene()
    $ del person_choice

    $ the_person.next_day_outfit = the_person.planned_outfit # she stays the night so she will have to wear the same outfit again

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_overnight_threesome_request
    call Sarah_spend_the_night() from sarah_threesome_request_spend_the_night_sequence

    return

label Sarah_arrange_threesome_label(the_person):
    if the_person.is_employee():
        mc.name "Hello [the_person.title]. I've got something I need help with I was hoping to talk to you about."
        the_person.char "Hello! What can I help you with?"
        mc.name "Well, you know [sarah.name], right? From HR?"
        the_person.char "Oh yeah, I was just talking to her this morning about the best way to get a guy to go down on you."
        mc.name "You were... what?"
        mc.name "Never mind. Anyway, she's never been in a threesome before, and she really wants to try one sometime."
        mc.name "She keeps hinting, so I promised her I'd try to arrange something for Saturday. Would you be interested in coming over Saturday night?"
        the_person.char "That sounds really fun! You better believe I'll go! Just let me know what time to be there."
        mc.name "Thanks!"
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is mom:
        mc.name "Hello [the_person.title]. I've got something I need help with I was hoping to talk to you about."
        the_person.char "Hey Honey. What can I help you with?"
        mc.name "Well, you know how I've been seeing that girl, [sarah.name]."
        the_person.char "I know! It's so great that you're seeing someone. I'm so proud of you."
        mc.name "Well, as it turns out, she's a little curious about the fairer sex. She's never been in a threesome before."
        mc.name "Anyway, she's been asking, so I promised her I'd try to arrange something for Saturday. I was wondering if you would be willing to join us?"
        the_person.char "That sounds really fun! But umm, I mean, how would she respond to you and I... being intimate?"
        mc.name "I've actually already talked to her about it, and she's okay with it. Are you in?"
        "She thinks for a moment."
        the_person.char "Okay... I'll do it! I'll see you two on Saturday!"
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is lily:
        mc.name "Hello [the_person.title]. I've got something I need help with I was hoping to talk to you about."
        the_person.char "Hey Bro. What do you need?"
        mc.name "Well, you know how I've been seeing that girl, [sarah.name]."
        the_person.char "I know! Damn when you brought her in here the other night, that was impressive!"
        the_person.char "You know you guys woke me up the next morning? I know you we're trying to be quiet, but the bed banging against the wall is really loud in the rest of the house..."
        mc.name "Sorry about that."
        mc.name "Well, as it turns out, she's a little curious about the fairer sex. She's never been in a threesome before."
        mc.name "Anyway, she's been asking, so I promised her I'd try to arrange something for Saturday. I was wondering if you would be willing to join us?"
        the_person.char "That sounds really fun! But umm, I mean, how would she respond to you being intimate with your sister?"
        mc.name "I've actually already talked to her about it, and she's okay with it. Are you in?"
        the_person.char "Oh! She's kinky? That sounds like fun. Okay, I'll clear my schedule for Saturday night."
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is cousin:
        mc.name "Hello [the_person.title]. I need a favor I was hoping to talk to you about."
        the_person.char "Seriously?"
        mc.name "Yeah seriously. Don't worry you'll like it."
        mc.name "There's this girl I've been seeing lately. She is pretty bi-curious, and has never had a threesome before."
        the_person.char "Oh jesus I can tell where this is going already."
        mc.name "Anyway, she's been asking, so I promised her I'd try to arrange something for Saturday. I need you to come over to my place Saturday night."
        if cousin.event_triggers_dict["blackmail_level"] >= 2 and cousin.has_role([stripper_role, waitress_role, bdsm_performer_role]):
            the_person.char "That's ridiculous. I'm gonna make a ton of money in tips on a Saturday night. You're gonna have to convince me..."
            mc.name "How about I promise not to tell your mom where you make all those tips at? Does that sound good?"
            the_person.char "Look, I need that money. I'm sorry but I can't just give up the most lucrative night of the week."
            mc.name "Fine, I'll give you $500, right now."
            the_person.char "Deal!"
            $ mc.business.change_funds(-500)
            "You give her the cash. She counts it twice to make sure its all there."
            the_person.char "Alright, I'll call in sick on Saturday. It's been a pleasure doing business with you."
        else:
            the_person.char "Can't. I have other plans for Saturday night."
            mc.name "You're always doing something late at night. What have you been up to anyway?"
            the_person.char "Nothing! Its none of your business, even if I was doing something."
            mc.name "Can't you just give up one Saturday night?"
            the_person.char "What's it worth to you?"
            mc.name "What?"
            the_person.char "Give me $500, right now, and I'll be there."
            mc.name "You're crazy."
            "She looks at you, unwavering."
            mc.name "Fine, I'll give you $500, right now."
            $ mc.business.change_funds(-500)
            "You give her the cash. She counts it twice to make sure its all there."
            the_person.char "Alright, I'll see you on Saturday. It's been a pleasure doing business with you."
        "You give her the details. maybe picking [the_person.possessive_title] was a bad idea..."
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is aunt:
        "Note, this dialogue is not yet written. I'm waiting until [aunt.name] gets further developed as a character."  #TODO
        "At the end of the dialogue, she agrees to be the threesome partner..."
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is starbuck:
        mc.name "Hello [the_person.title]. I've got something I need help with I was hoping to talk to you about."
        the_person.char "Hello! What can I help you with?"
        mc.name "Well, there's this girl I've been seeing lately. She is pretty bi-curious, and has never had a threesome before."
        the_person.char "Oh! I think I like her already!"
        mc.name "Anyway, she's been asking, so I promised her I'd try to arrange something for Saturday. Would you be interested in coming over Saturday night?"
        the_person.char "That sounds really fun! You better believe I'll go! Just let me know what time to be there."
        mc.name "Thanks!"
        "You give her the details. This is going to be a fun night!"
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is nora:
        "Note, this dialogue is not yet written. I'm waiting until Nora gets further developed as a character."  #TODO
        "At the end of the dialogue, she agrees to be the threesome partner... for science..."
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    return

label Sarah_initial_threesome_label():
    if sarah.event_triggers_dict.get("initial_threesome_arranged", False) == False:
        "You get a text from [sarah.possessive_title]"
        sarah.char "Hey, are we still on for tonight?"
        "You text her back."
        mc.name "Actually, I haven't been able to talk to her yet. I'm sorry, It'll be ready next week."
        sarah.char "Okay..."
        $ sarah.change_stats(happiness = -10, love = -3)
        $ add_sarah_initial_threesome_action()
        return

    $ the_person_one = sarah
    $ the_person_two = sarah.event_triggers_dict.pop("initial_threesome_target") # get and remove from dictionary
    $ scene_manager = Scene()

    if the_person_two == None:
        "How did we get here? Tell Starbuck her shitty code is missing the initial threesome target."
        return
    "It's Saturday night. You quickly head home, you have an exciting night ahead of you."
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You make sure your bedroom is nice and tidy. Soon you get a text on your phone."
    the_person_one.char "Hey, I'm here."
    "You head to the front door and invite her in."
    $ scene_manager.add_actor(the_person_one)
    "You head back to your bedroom and she sits on your bed."
    $ scene_manager.update_actor(the_person_one, position = "sitting", character_placement = character_center_flipped)
    the_person_one.char "Oh god, I've got butterflies in my stomach. I cant believe this is finally happening. Do I look okay?"
    mc.name "You look incredible, as always."
    if the_person_two is lily or the_person_two is mom:
        "Okay, let me go get [the_person_two.title], I'll be right back."
        "You walk into her room. She follows you back to your room."
    else:
        "Soon, you get another text on your phone."
        the_person_two.char "I'm here now. Come let me in?"
        mc.name "She's here, give me one second."
        "You go to the front door and let in [the_person_two.title]. She follows you quietly to your room."
    # make the second person wear a more sexy outfit (50% sluttiness boost)
    $ the_person_two.apply_outfit(the_person_two.wardrobe.decide_on_outfit2(the_person_two, sluttiness_modifier = .5))
    $ scene_manager.add_actor(the_person_two)
    "Alright, here you are, in your room, with [the_person_one.title] and [the_person_two.possessive_title]."
    the_person_one.char "Hi..."
    "She's getting shy. The atmosphere in the room is getting awkward. You'd better do something to break the ice!"
    mc.name "Hey, why don't you sit on the bed, [the_person_two.title]. I'm gonna turn on some music."
    the_person_two.char "Okay! Sounds good."
    $ scene_manager.update_actor(the_person_two, position = "sitting")
    "You turn some music on. A soft instrumental that should help set the mood. The girls are starting to chat."
    the_person_two.char "I'll be honest, after [the_person_two.mc_title] asked me to do this, I was pretty surprised, but I've really been looking forward to it."
    the_person_one.char "Oh... really?"
    the_person_two.char "Yeah. Don't worry. It might be awkward at first, but once we get going, this is going to be a LOT of fun."
    the_person_one.char "That's what I keep hoping!"
    "[the_person_two.possessive_title] stands up and motions towards [the_person_one.title]"

    the_person_two.char "Come here. This will help..."
    $ scene_manager.update_actor(the_person_two, position = "walking_away")
    $ scene_manager.update_actor(the_person_one, position = "kissing", character_placement = character_right)
    "The two girls embrace. They begin to run their hands along each others bodies. Then they begin to kiss."
    the_person_one.char "Mmm... your skin is so soft..."
    "Damn! They are starting to get into it. [the_person_two.title] has her hands around her back, while [the_person_one.possessive_title] is grabbing her ass."
    $ the_person_one.change_arousal(10)
    $ the_person_two.change_arousal(10)
    "The girls are starting to moan into each other's mouths. Things are heating up quickly!"
    "You decide its time for you to make your presence known. You step directly behind [the_person_one.title] and hug her from behind."
    $ scene_manager.update_actor(the_person_one, position = "back_peek")
    the_person_one.char "Oh... oh my god..."
    "You wrap your left hand around and begin to fondle her tits. With your other hand you reach all the way to [the_person_two.possessive_title]'s back, pulling you all close together."
    "With her head to one side, you and [the_person_two.title] begin kissing both sides of [the_person_one.possessive_title]'s neck."
    $ the_person_one.change_arousal(25)
    $ the_person_two.change_arousal(10)
    "You grind your erection into her backside. She is beginning to pant heavily."
    the_person_one.char "Oh god... I need to stop... Give me as second!"
    "You both pause while you wait for her. She looks [the_person_two.title] in the eyes..."
    the_person_one.char "I want to taste you. I've never kissed another woman down there... I want to try it!"
    the_person_two.char "Mmm, that sounds nice. Let's do it!"
    "[the_person_one.possessive_title] looks back at you."
    the_person_one.char "I want you to fuck me... fuck me while I eat out another woman!"
    mc.name "Glady! But I think everyone here is still wearing way too many clothes..."
    "The girls chuckle and then quickly agree."
    $ scene_manager.update_actor(the_person_two, position = "stand2", character_placement = character_center_flipped)
    $ scene_manager.update_actor(the_person_one, position = "stand3")
    $ scene_manager.strip_actor_outfit(the_person_one)
    $ scene_manager.strip_actor_outfit(the_person_two)
    "After everyone is naked, the action moves to the bed."
    call start_threesome(the_person_one, the_person_two, start_position = Threesome_doggy_deluxe, swapped = True) from sarah_initial_threesome_1
    $ scene_manager.update_actor(the_person_one, position = "missionary", character_placement = character_center)
    $ scene_manager.update_actor(the_person_two, position = "back_peek", character_placement = character_right)
    "As the activity winds down, you all lay down next to each other. You have [the_person_one.possessive_title] on one side and [the_person_two.possessive_title] on the other."
    the_person_one.char "Oh my god... that was so good. I never knew it could be so good, to be with another woman like that..."
    $ sarah.event_triggers_dict["threesome_unlock"] = 1
    "You hear a murmur of approval from [the_person_two.title]."
    "You enjoy the pair of bedwarmers, and are just getting ready to fall asleep when you feel movement."
    $ scene_manager.update_actor(the_person_two, position = "stand4")
    the_person_two.char "Well, I had a lot of fun, but I should be going. Goodnight you two."
    "You both say goodbye. [the_person_two.title] grabs her stuff and leaves the room."
    $ scene_manager.remove_actor(the_person_two)
    if not the_person_one.has_role(girlfriend_role):
        the_person_one.char "Ohh, I'm not sure I can walk... but I should get going too..."
        "[the_person_one.title] slowly gets out of bed."
        $ scene_manager.update_actor(the_person_one, position = "stand4")
        the_person_one.char "That was more than I could have hoped for. Thank you so much for this!"
        $ scene_manager.remove_actor(the_person_one)
        "You say goodbye, and slowly drift off to sleep."
        call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_initial_threesome_no_overnight
        $ del the_person_one
        $ del the_person_two
        return
    mc.name "You're staying tonight... right?"
    the_person_one.char "Oh god, I don't think I could get up, even if I wanted to. Which I don't."
    "Worn out, you cuddle up with her and quickly fall asleep as well."
    $ scene_manager.clear_scene()
    $ the_person.next_day_outfit = the_person.planned_outfit # she stays the night so she will have to wear the same outfit again

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_overnight_after_threesome_1
    call Sarah_spend_the_night() from sarah_threesome_spend_the_night
    $ add_sarah_ask_for_baby_action()
    $ del the_person_one
    $ del the_person_two
    return

label Sarah_ask_for_baby_label():
    $ the_person = sarah
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    $ scene_manager = Scene()
    "As you are getting ready for bed, you get a text on your phone. It's from [the_person.possessive_title]"
    the_person.char "Hey, can I come over tonight? I had something I wanted to talk to you about."
    "You quickly text her back."
    mc.name "Sure. Want to spend the night?"
    the_person.char "Hell yeah! I'll bring some stuff over."
    "About 20 minutes later she texts you."
    the_person.char "Hey, I'm here! Come let me in!"
    "You head to your front door and open it."
    "For once, you managed to get her back to your room while avoiding [mom.possessive_title] and [lily.title]."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "She walks over and sits on your bed."
    mc.name "So... what did you want to talk about?"
    "She clears her throat. You can tell she is a little nervous."
    the_person.char "Well, this is kind of hard to talk about. But... we've been having a lot of unprotected sex lately..."
    mc.name "Oh my god, are you pregnant?"
    the_person.char "No! No, not yet anyway..."
    mc.name "Not... yet?"
    the_person.char "Well, [the_person.mc_title], it's been like a dream, having you back in my life like this. Things are amazing, being with you."
    the_person.char "I've been, well, tracking my cycles recently and, well, basically, I'm fertile right now."
    "You can feel your cock twitch in your pants. You imagine [the_person.possessive_title], knocked up, her tits swelling with milk and her belly growing..."
    the_person.char "Every time you finish inside me, I find myself thinking about it, more and more, what it would be like to get pregnant and have a baby with you."
    the_person.char "Look, you don't have to answer me right now, but, I thought maybe we could try and have a baby. Together?"
    "This is quite a twist! You weren't expecting this so soon, but you have to admit that the thought is exciting..."
    menu:
        "Try for a baby":
            mc.name "Honestly, I didn't realize this was something you were thinking about. But I would love to make a baby with you!"
            $ the_person.change_stats(happiness = 15, obedience = 10)
            the_person.char "Oh! Wow, I honestly... I thought you we're gonna say no! This is... I can't believe it."
            "She looks up at you, and you can see the changes in her facial expression. She goes from surprised, to happy, to sultry."
            the_person.char "So umm, like I was saying, I'm pretty sure I'm actually fertile right now..."
            mc.name "I think we should get naked now."
            the_person.char "Yes sir!"
            $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
            "You get naked with [the_person.possessive_title]. She rolls on her back and spreads her legs."
            the_person.char "Come fill me up, [the_person.mc_title]!"
            if the_person.get_opinion_score("creampies") < 2:   #From now on, she loves getting creamed, and has relevant dialogue
                $ the_person.update_opinion_with_score("creampies", 2)
            if the_person.get_opinion_score("bareback sex") < 2:    #TODO see if we can actually make her refuse condoms?
                $ the_person.update_opinion_with_score("bareback sex", 2)
            $ the_person.event_triggers_dict["try_for_baby"] = 1
            $ the_person.event_triggers_dict["fertile_start_day"] = day  #Her 5 day fertility period starts today.
            call Sarah_fertile_period_start_label() from sarah_initial_fertile_period_start_01
            #TODO create mandatory event for starting fertility period. Stores creampies before fertility period. Then second mandatory event at the end of the fertility period determines if pregnant based on # of creampies and RNG
            call fuck_person(the_person, start_position = missionary, start_object = bedroom.get_object_with_name("bed"), skip_intro = False, girl_in_charge = False, position_locked = True) from _sarah_ask_for_baby_01
            if the_person.has_creampie_cum():
                the_person.char "Oh my god... we actually did it..."
                "She grabs an extra pillow and puts it under her butt so her hips are elevated."
                the_person.char "I'm just going to lay her like this for a bit, you know. Keep that seed nice and deep."
            else:
                mc.name "I'm sorry, I really want to, I'm just really tired."
                "You can tell she is a little disappointed."
                the_person.char "That's okay. Maybe in the morning?"
            "You snuggle up with [the_person.possessive_title]. You both quickly fall asleep."

            call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_breeding_request_1
            call Sarah_spend_the_night() from sarah_ask_for_baby_overnight
        "Think about it":
            mc.name "This is a really big decision. Give me some time to think about it, okay?"
            "You can tell she is a little disappointed, but she understands your answer."
            the_person.char "Of course! I understand."
            #TODO add ability to revisit this decision later.
            the_person.char "I guess, umm, just be careful then. Wouldn't want to get knocked while you are still considering it, right?"
            "You walk up to [the_person.possessive_title] as she stands up. You put your hands on her hips and draw her close."
            $ scene_manager.update_actor(the_person, position = "kissing")
            "Your tongues meet and you begin to make out. The kissing starts innocent, but quickly grows in urgency."
            the_person.char "Mmm."
            call fuck_person(the_person, start_position = kissing, skip_intro = True, girl_in_charge = False) from _sarah_ask_for_baby_reject_01
            $ scene_manager.update_actor(the_person, position = "missionary")
            "When you finish, you lay down next to [the_person.title] in your bed. You both quickly fall asleep together."
            call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_breeding_request_2
            call Sarah_spend_the_night() from sarah_ask_for_baby_overnight_reject

    return

label Sarah_spend_the_night():      #She spends the night with you. Have a random chance of a threesome with mom or lily
    $ the_person = sarah
    $ scene_manager = Scene()
    $ the_person.apply_outfit(SB_vaginal_nude_outfit)
    $ the_person.change_energy(200)

    $ (threesome_wakeup, threesome_partner) = get_sarah_spend_night_threesome_possibility()

    if not threesome_wakeup:
        $ scene_manager.add_actor(the_person, position = "walking_away")
        "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
        "She is still sleeping, but her skin is setting off electric sparks everywhere it is touching yours."
        "Your hands cup and squeeze one of her breasts. It's so full and hot, they feel so good in your hands."
        the_person.char "Mmmmmmmm......"
        "[the_person.title] moans but doesn't stir. Maybe you could surprise her with a little good morning dicking."
        if Sarah_is_fertile():
            "You're sure she wouldn't mind an extra creampie to start the day. The more cum in her the better during her fertile period!"
        menu:
            "Try to slide yourself in":
                pass
            "Get ready for the day":
                "Thinking about your tasks for the day, you feel yourself get a bit anxious about wasting the morning."
                "You get up and head for bathroom to take a leak."
                "When you come back, [the_person.title] is awake."
                $ scene_manager.update_actor(the_person, position = "missionary")
                the_person.char "Good morning! I slept great."
                $ the_person.apply_planned_outfit()
                $ scene_manager.update_actor(the_person, position = "stand3")
                "You both get ready for the day before heading out."
                $ scene_manager.clear_scene()
                return
        "Your cock is already hard, being up against [the_person.title], but she may not be fully wet yet."
        "You spit into your hand and rub it on your dick a few times, getting it lubed up."
        "When you feel good about it, you reach down and gently spread her cheeks apart. You position yourself at her entrance and give it a little push."
        "You are able to ease yourself about halfway in, but the angle makes it hard to get deep penetration."
        the_person.char "Oh [the_person.mc_title]. Mmmmmm"
        "She's still asleep, but is still responding to your touch. She must be a heavy sleeper! Or maybe she is just really worn out from last night..."
        "You give her a few gentle, smooth strokes. You can feel her pussy getting wetter with each stroke as her body begins to respond to the stimulation."
        $ the_person.change_arousal(20)
        "With her legs closed and on her side like this, her pussy feels really tight. You can feel her gripping you every time you start to pull it out."
        $ mc.change_arousal(15)
        "Your reach around her with your hand and grab one of her tits. You start to get a little rough with her and pinch and pull at one of her nipples."
        $ the_person.change_arousal(20)
        $ mc.change_arousal(15)
        the_person.char "Mmm that feels so... wait... [the_person.mc_title]?"
        $ scene_manager.update_actor(the_person, position = "back_peek", emotion = "happy")
        "[the_person.possessive_title] wakes up and looks back at you smiling."
        the_person.char "Oh my god that feels so good... Baby you know how to give a wakeup call, holy fuck!"
        "Encouraged by her words, you reach your hand down and lift her leg, giving you a better angle for deeper penetration."
        "You pick up the pace and begin to fuck her earnestly."
        $ the_person.change_arousal(30) #70
        $ mc.change_arousal(25) #55
        the_person.char "Oh yes that feels so good, fuck me good!"
        "She reaches down and holds her leg for you, freeing up your hand. You reach down between her legs and start to play with her clit."
        "Her ass is making smacking noises now, every time your hips drive your cock deep inside of her."
        $ the_person.change_arousal(40) #110
        $ mc.change_arousal(35) #90
        the_person.char "Oh fuck, yes! YES!"
        "She shoves her ass back against you as she cums. Her helpless body quivers in delight. Her moans drive you even harder."
        $ mc.change_arousal(20) #110
        mc.name "I'm gonna cum!"
        if Sarah_is_fertile():
            the_person.char "Cum deep! Knock me up with your hot cum, [the_person.mc_title]!"
        else:
            the_person.char "Shove it in deep! I want to feel your seed inside me all day long!"
        $ the_person.cum_in_vagina()
        #TODO internal fetish specific dialogue
        "You grab her hip and shove your cock deep and hold it there, cumming deep inside her. She moans and gasps with every spurt."
        "Satisfied, you slowly pull out of her."
        the_person.char "That's certainly one way to start the day... holy hell."
        $ the_person.reset_arousal()
        $ mc.arousal = 0
        "You lay in bed together for a little longer, but soon it is time to start the day."
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You both get ready for the day."
        the_person.char "Alright, I need to get some things done today. Thanks for letting me spend the night!"
        $ scene_manager.remove_actor(the_person)
        $ scene_manager.clear_scene()
        return

    #sexy morning wakeup starts here
    if threesome_wakeup:
        $ threesome_partner.apply_outfit(SB_vaginal_nude_outfit)
        "You are slow to wakeup. You had several sexy dreams the night before, and you aren't ready to leave them yet."
        "It feels good, in your dream, as you slowly push your cock into [the_person.title]'s hot pussy."
        "Something stirs you though. You hear a hushed whisper. But that wasn't to you? Then a little giggle."
        threesome_partner.char "Mmmm, he's so big..."
        $ threesome_partner.change_arousal(30)
        "You must still be dreaming, that sounded like [threesome_partner.title]. Your cock feels amazing, wrapped in a warm, wet vice."
        the_person.char "I know. He was grinding against me all night last night. It was making me so horny!"
        $ the_person.change_arousal(30)
        "Wait... what?"
        "You slowly open your eyes."
        $ scene_manager.add_actor(threesome_partner, position = "cowgirl")
        "[threesome_partner.possessive_title] is on top of you, your cock inside of her. Holy fuck!"
        "You open your eyes completely."
        $ scene_manager.add_actor(the_person, position = "kneeling1", character_placement = character_center_flipped)
        "[the_person.title] is beside her, touching herself while [threesome_partner.title] fucks you. She notices you wakeup."
        the_person.char "Good morning! [threesome_partner.name] came in this morning looking for you, so I invited her to hop on for a bit."
        threesome_partner.char "I'm sorry, I didn't realize your girlfriend was spending the night, and I was feeling needy this morning..."
        "As she talks, [threesome_partner.title] starts to rock her hips back and forth, enjoying the fullness of being penetrated by you."
        mc.name "Wow, what a wakeup... a guy could get used to this..."
        the_person.char "Mmm, I don't mind sharing you. I need a little more stimulation than my fingers though..."
        "[the_person.title] turns around, facing away from you and lifts one leg over your body, back her pussy up to your face."
        the_person.char "Do me a favor and kiss me for a bit?"
        mc.name "Mmm, definitely."
        "You waste no time and dive right into [the_person.possessive_title]'s delicious cunt."
        # TODO change this scene if the girls both like anal? Need to figure out how to handle starting in a specific threesome action
        call start_threesome(threesome_partner, the_person, start_position = Threesome_double_down, round = 1, private = True, position_locked = False, affair_ask_after = False, hide_leave = False) from sarah_overnight_threesome_wakeup
        $ the_report = _return
        $ scene_manager.update_actor(the_person, position = "missionary", character_placement = character_center_flipped)
        $ scene_manager.update_actor(threesome_partner, position = "missionary", character_placement = character_right)
        "All finished, the girls flop onto their backs, one on each side of you."
        if the_report["girl one orgasms"] > 0 and the_report["girl two orgasms"] > 0:  #They both finished.
            the_person.char "Oh wow, that was so hot..."
            if the_person.get_opinion_score("incest") < 1:
                $ the_person.increase_opinion_score("incest")
            if threesome_partner is mom:
                threesome_partner.char "I know... I just had a threesome with my son and his girlfriend... and I loved it!"
                $ threesome_partner.increase_opinion_score("incest")
            else:
                threesome_partner.char "I know! A threesome with my bro and his girl... and I loved it!"
                $ threesome_partner.increase_opinion_score("incest")
            threesome_partner.char "It was amazing... [the_person.name] don't be a stranger now..."
        else:
            "You lay together for a few moments, enjoying each other's proximity."
        $ scene_manager.update_actor(threesome_partner, position = "stand3")
        "[threesome_partner.title] gets up, and remarks before leaving."
        threesome_partner.char "That was fun! I'm gonna head back to my room. Thanks for sharing [the_person.name]!"
        $ scene_manager.remove_actor(threesome_partner)
        "She walks out, leaving you alone with [the_person.possessive_title]"
        the_person.char "That's certainly one way to start the day... holy hell."
        "You lay in bed together for a little longer, but soon it is time to start the day."
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You both get ready for the day."
        the_person.char "Alright, I need to get some things done. Thanks for letting me spend the night!"
        $ scene_manager.remove_actor(the_person)
        $ threesome_partner = None

    else:
        "You are slow to wakeup. You had several sexy dreams the night before, and you aren't ready to leave them yet."
        "It feels good, in your dream, as you slowly push your cock into [the_person.title]'s hot pussy."
        "It's so wet and tight, it feels almost real..."
        the_person.char "...[the_person.mc_title]... mmm.... I can't take it anymore..."
        $ scene_manager.add_actor(the_person, position = "cowgirl")
        $ the_person.change_arousal(30)
        $ mc.change_arousal(30)
        "You slowly open your eyes and discover [the_person.possessive_title] is on top of you, riding your cock."
        the_person.char "Oh thank god you're awake. I swear you were poking me all night long! I kept hoping you would just stick it in, but I think you were sleeping."
        the_person.char "I couldn't take it anymore. I hope you don't mind!"
        "[the_person.title]'s epic tits are bouncing up and down right in front of you as she rides you."
        mc.name "Definitely. Ride me good!"
        call fuck_person(the_person, start_position = cowgirl, start_object = bedroom.get_object_with_name("bed"), skip_intro = True, girl_in_charge = True) from _sarah_cowgirl_wakeup_overnight_1
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            $ the_person.change_love(5)
            the_person.char "Oh wow I came so hard [the_person.mc_title]."
            "She rolls over and kisses you, then rests her head on your chest."

        "You lay in bed together for a little longer, but soon it is time to start the day."
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You both get ready for the day."
        the_person.char "Alright, I need to get some things done today. Thanks for letting me spend the night!"
        $ scene_manager.remove_actor(the_person)

    $ scene_manager.clear_scene()
    return "Advance Time"

label watch_strip_show(the_person):  #This scene assumes scene manager is running and the_person is with you, so she won't strip for you.
    $ showgirl = get_random_from_list(stripclub_strippers)
    $ showgirl.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    "You watch as a girl gets on stage and starts to do her routine."
    $ scene_manager.add_actor(showgirl, character_placement = character_left_flipped)
    if showgirl is cousin:
        if showgirl.event_triggers_dict.get("blackmail_level",-1) < 2 and cousin.has_role(stripper_role) and not showgirl.event_triggers_dict.get("seen_cousin_stripping",False):
            python:
                blackmail_2_confront_action = Action("Confront her about her stripping", blackmail_2_confront_requirement, "cousin_blackmail_level_2_confront_label",
                    menu_tooltip = "Tell her that you know about her job as a stripper and use it as further leverage.")
                cousin_role.add_action(blackmail_2_confront_action)
                showgirl.event_triggers_dict["seen_cousin_stripping"] = True

            "It takes you a moment to recognize your cousin, [showgirl.title], as she struts out onto the stage."
            if not showgirl.event_triggers_dict.get("found_stripping_clue", False):
                "[showgirl.possessive_title]'s late nights and secret keeping suddenly make a lot more sense."

            "With the glare of the stage lights it's likely she won't be able to see who you are, but you can talk to her later and use this as leverage to blackmail her."
    $ finished = True
    $ finished_chance = 0
    python:
        for x in range(6):
            scene_manager.update_actor(showgirl, position = get_random_from_list(sarah_strip_pose_list))
            if renpy.random.randint(0,100) <76: #Take something off
                showgirl.outfit.remove_random_any(top_layer_first = True)
            if renpy.random.randint(0,100) < finished_chance:
                finished = False
            else:
                finished_chance += 5
                renpy.pause(1)
    if showgirl.outfit.vagina_visible():
        "As she finishes, the showgirl gives one more pose, showing off her exposed ass to the crowd."
        $ scene_manager.update_actor(showgirl, position = "standing_doggy")
    elif showgirl.outfit.tits_visible():
        "As she finishes, the showgirl gives one more pose, showing off her exposed tits to the crowd."
        $ scene_manager.update_actor(showgirl, position = "kneeling1")
    else:
        "As she finished, the showgirl gives one more pose, to the enjoyment of everyone in the crowd."
        $ scene_manager.update_actor(showgirl, position = get_random_from_list(sarah_strip_pose_list))
    $ scene_manager.update_actor(showgirl, position = "walking_away")
    "After finishing, the showgirl grabs her tips then exits the stage."
    $ scene_manager.remove_actor(showgirl)
    return showgirl

label play_darts_301(the_person, focus_mod = 0): #Label returns true if mc wins, false if the_person wins
    $ mc_score = 301
    $ p2_score = 301
    $ scene_manager.add_actor(the_person, position = "walking_away")
    "[the_person.title] steps to the line and prepares to throw her first set of darts."
    while (mc_score != 0) and (p2_score != 0):
        "It's [the_person.title]'s turn."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.title] begins to throw her darts."

        #First Dart
        if p2_score > 49:
            $ p2_score -= roll_dart_odds(target = 50, focus_score = (the_person.focus + focus_mod))
        elif p2_score > 24:
            $ p2_score -= roll_dart_odds(target = 25, focus_score = (the_person.focus + focus_mod))
        elif p2_score > 19:
            $ p2_score -= roll_dart_odds(target = 20, focus_score = (the_person.focus + focus_mod))
        else:
            $ p2_score -= roll_dart_odds(target = p2_score, focus_score = (the_person.focus + focus_mod))

            #Second Dart
        if p2_score > 50:
            $ p2_score -= roll_dart_odds(target = 50, focus_score = (the_person.focus + focus_mod))
        elif p2_score < 0:
            pass
            #TODO BUST
        elif p2_score == 0:
            pass
            #TODO SHE WINS
        elif p2_score > 24:
            $ p2_score -= roll_dart_odds(target = 25, focus_score = (the_person.focus + focus_mod))
        else:
            $ p2_score -= roll_dart_odds(target = p2_score, focus_score = (the_person.focus + focus_mod))

            #Third Dart
        if p2_score > 50:
            $ p2_score -= roll_dart_odds(target = 50, focus_score = (the_person.focus + focus_mod))
        elif p2_score < 0:
            pass
            #TODO BUST
        elif p2_score == 0:
            pass
            #TODO SHE WINS
        elif p2_score > 24:
            $ p2_score -= roll_dart_odds(target = 25, focus_score = (the_person.focus + focus_mod))
        else:
            $ p2_score -= roll_dart_odds(target = p2_score, focus_score = (the_person.focus + focus_mod))

        "[the_person.title] score: [p2_score]"
        if p2_score == 0:
            "[the_person.title] wins the game!"
            $ scene_manager.remove_actor(the_person, reset_actor = False)
            return False
        elif p2_score < 0:
            "[the_person.title] busts! Her score is reset to 101!"
            $ p2_score = 101
        $ scene_manager.update_actor(the_person)
        the_person.char "Okay, [the_person.mc_title]. Your turn!"
        "Your score: [mc_score], what would you like to target?"
        menu:
            "Bullseye (50)" if mc_score > 49:
                $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                pass
            "Bullseye (50)" if mc_score < 50:
                "You decide to try and bust on purpose."
                $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
            "Outer Ring (25)" if mc_score > 24:
                $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                pass
            "Outer Ring (25)" if mc_score < 25:
                "You decide to try and bust on purpose."
                $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
            "20" if mc_score > 20:
                $ mc_score -= roll_dart_odds(target = 20, focus_score = mc.focus)
                pass
            "[mc_score]" if mc_score < 21:
                "This is it, you're going for the win!"
                $ mc_score -= roll_dart_odds(target = mc_score, focus_score = mc.focus)

        if mc_score > 0:
            "Now for your second dart. Your score: [mc_score], what would you like to target?"
            menu:
                "Bullseye (50)" if mc_score > 49:
                    $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                    pass
                "Bullseye (50)" if mc_score < 50:
                    "You decide to try and bust on purpose."
                    $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                "Outer Ring (25)" if mc_score > 24:
                    $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                    pass
                "Outer Ring (25)" if mc_score < 25:
                    "You decide to try and bust on purpose."
                    $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                "20" if mc_score > 20:
                    $ mc_score -= roll_dart_odds(target = 20, focus_score = mc.focus)
                    pass
                "[mc_score]" if mc_score < 21:
                    "This is it, you're going for the win!"
                    $ mc_score -= roll_dart_odds(target = mc_score, focus_score = mc.focus)

        if mc_score > 0:
            "Now for your third dart. Your score: [mc_score], what would you like to target?"
            menu:
                "Bullseye (50)" if mc_score > 49:
                    $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                    pass
                "Bullseye (50)" if mc_score < 50:
                    "You decide to try and bust on purpose."
                    $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                "Outer Ring (25)" if mc_score > 24:
                    $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                    pass
                "Outer Ring (25)" if mc_score < 25:
                    "You decide to try and bust on purpose."
                    $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                "20" if mc_score > 20:
                    $ mc_score -= roll_dart_odds(target = 20, focus_score = mc.focus)
                    pass
                "[mc_score]" if mc_score < 21:
                    "This is it, you're going for the win!"
                    $ mc_score -= roll_dart_odds(target = mc_score, focus_score = mc.focus)
        if mc_score == 0: #MC wins!
            "You win the game of darts!"
            $ scene_manager.remove_actor(the_person, reset_actor = False)
            return True
        elif mc_score < 0:
            "You bust! Your score is reset to 101."
            $ mc_score = 101
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    return False

label Sarah_weekend_surprise_crisis_label():
    $ the_person = sarah
    $ the_person.planned_outfit = get_sarah_date_outfit_two()
    $ the_person.apply_planned_outfit()
    $ scene_manager = Scene()

    "Lost in thought as you get your work done in the silence of the weekend, a sudden voice startles you."
    the_person.char "[the_person.mc_title]! Working away your weekend again I see!"
    "You look up to see the now familiar face of [the_person.title] standing in the doorway."
    $ scene_manager.add_actor(the_person, emotion = "happy")
    the_person.char "You work too much! Let's go have some fun somewhere!"
    "You have been working quite a bit lately, it would be good to have a chance to blow off some steam."
    menu:
        "Let's Go":
            the_person.char "Yes! You won't regret this. Let's go!"
            "You finish up what you are working on and grab your stuff. You make sure to lock up the business on your way out with [the_person.possessive_title]"
            "As you exit the building, you consider where you should head for the night."
            menu:
                "The Bar" if sarah.event_triggers_dict.get("drinks_out_progress", 0) >= 2:    #If you've grabbed drinks before. In requirements, so this SHOULD always be true
                    mc.name "What do you say we head to the bar and have a few drinks? Maybe play some darts?"
                    the_person.char "Oh! That sounds great!"
                    call Sarah_weekend_date_grab_drinks_label from sarah_weekend_date_crisis_01

                "Strip Club" if sarah.event_triggers_dict.get("stripclub_progress", 0) >= 1 and not strip_club_is_closed():
                    mc.name "In the mood for a titty bar?"
                    the_person.char "Oh! That sounds like a good evening!"
                    call Sarah_weekend_date_strip_club_label from sarah_weekend_date_crisis_02

                "Your Place":   #Added as a default while testing. Probably limit this with sluttiness later #TODO
                    the_person.char "Oh! A direct approach? Not even going to bother getting me boozed up?"
                    mc.name "Nah. The sex is better when you are sober anyway."
                    the_person.char "Ha! Okay, lead the way then stud!"
                    "A short walk later, and you are walking through your front door."
                    call Sarah_date_ends_at_your_place_label(the_person) from sarah_date_happy_ending_02

        "Not Today":
            the_person.char "Seriously? You're going to turn me down?"
            mc.name "I'm sorry, there is a lot I want to get done around here."
            if sarah.sluttiness > 70:
                the_person.char "You know, it is so sexy how much work you put into this place."
                mc.name "Is that so?"
                $ scene_manager.update_actor(the_person, position = "kneeling1")
                "She slowly climbs up onto your desk and begins to touch herself."
                the_person.char "I know you have a lot to do. Feel free to watch... or blow a little steam off with me!"
                mc.name "Right! I'm sure a short diversion wouldn't delay me too much."
                "She walks right up to you and starts to get down on her knees. You pull your cock out, which is now fully erect."
                $ scene_manager.update_actor(the_person, position = "blowjob")
                the_person.char "That's it. Let me just take care of this for you..."
                call fuck_person(the_person, start_position = deepthroat, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_sarah_weekend_deepthroat_1
                "[the_person.possessive_title] moans while licking the last drops from her lips."
                the_person.char "You taste so good, just call me when you need to blow off some more steam..."
                "You clear your throat and then respond."
                mc.name "That was great, thank you!"
                $ scene_manager.update_actor(the_person, position = "stand4")
                the_person.char "Alright, I know you wanted to get other things done, so I'll let you get back to it. But don't work too hard!"
                "She quickly cleans herself up then leaves, giving you a chance to continue your work, but now with your balls empty."
            elif sarah.event_triggers_dict.get("epic_tits_progress", 0) > 1:
                the_person.char "I got an idea. Why don't you let me help you, you know, relieve a little tension?"
                mc.name "I'm not honestly that tense right now..."
                if the_person.outfit.tits_available():
                    "[the_person.title] begins to grope her own tits and play with her nipples."
                else:
                    "Without prompting, [the_person.title] starts to remove her top..."
                    $ scene_manager.strip_actor_outfit(the_person, exclude_lower = True)
                the_person.char "Are you sure? My big tits don't make you tense... at all?"
                "You have to admit it, seeing her epic tits gets you excited. You can feel an erection starting."
                the_person.char "Hmmm. Earth to [the_person.mc_title]?"
                mc.name "Right! I'm sure a short diversion wouldn't delay me too much."
                the_person.char "Mmm, ever since I took those serums, I've been craving your cock between my tits..."
                "She walks right up to you and starts to get down on her knees. You pull your cock out, which is now fully erect."
                $ scene_manager.update_actor(the_person, position = "blowjob")
                the_person.char "That's it. Let me just take care of this for you..."
                call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_sarah_weekend_titfuck_1
                "[the_person.possessive_title] moans as she rubs your cum into her chest."
                the_person.char "It feels so sticky on my skin... Mmmm that was nice."
                "You clear your throat and then respond."
                mc.name "That felt great!"
                $ scene_manager.update_actor(the_person, position = "stand4")
                the_person.char "Alright, I know you wanted to get other things done, so I'll let you get back to it. But don't work too hard! Look me up if you need another break sometime!"
                "She quickly cleans herself up then leaves, giving you a chance to continue your work, but now with your balls empty."
            else:
                $ the_person.change_happiness(-10)
                $ the_person.change_love(-5)
                $ the_person.change_obedience(5)
                the_person.char "Wow, okay. Sorry, I didn't realize you were so busy. Maybe next time I guess?"
                "[the_person.title] quickly turns and walks out, leaving you to your work."
                $ scene_manager.remove_actor(the_person)

    $ scene_manager.clear_scene()
    return _return


label Sarah_weekend_date_grab_drinks_label():
    $ the_person = sarah
    $ scene_manager = Scene()
    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()
    $ scene_manager.add_actor(the_person, emotion = "happy")
    $ favorite_drink = the_person.event_triggers_dict.get("favorite_drink" "appletini")
    $ intoxication_level = 0 #Start at 0, options may open up depending on how drunk you get her.
    "After a short walk, you arrive at the bar that you and [the_person.title] have been to a few times recently."
    the_person.char "Oh! I think I see a booth over there."
    mc.name "Perfect, go grab it while I get the first round."
    "You wander over to the bar and buy drinks for you and [the_person.possessive_title]. You make sure to get her favorite, the [favorite_drink]."
    $ mc.business.change_funds(-20)
    "If you wanted to, now would be a good time to slip a serum into her drink..."
    menu:
        "Slip in a serum":
            "After you get the drinks, you carefully add a serum to it."
            call give_serum(the_person) from _call_give_sarah_serum_005
        "Leave alone":
            "You decide to leave her drink alone."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You join [the_person.title] at the booth and begin to enjoy your drinks together."
    "You spend some time, shooting the breeze and enjoying each other's company."
    "After a while the drinks are empty. You consider what to do next."
    $ intoxication_level += 1
    $ loop_count = 0
    while loop_count < 5: #Limited number of rounds available
        $ chance_service_him = the_person.sluttiness + ((the_person.obedience - 100) / 4 ) + (mc.charisma * 4) + (intoxication_level * 4)
        if chance_service_him > 100:
            $ chance_service_him = 100
        elif chance_service_him < 0:
            $ chance_service_him = 0
        menu:
            "Have another round" if intoxication_level < 7:
                mc.name "Wow, drinks are empty already. Another round?"
                the_person.char "Hell yeah!"
                if renpy.random.randint(0,100) < 35:  #She offers to buy a round once in a while
                    the_person.char "Tell you what, let me pick up this round. It's only fair!"
                    $ scene_manager.update_actor(the_person, position = "walking_away")
                    "[the_person.possessive_title] jumps up and walks away. You admire her figure as she makes her way over to the bartender."
                    "After a short time, she returns with the drinks and sits down."
                    $ scene_manager.update_actor(the_person, position = "sitting")
                else:
                    "You wander over to the bar and buy drinks for you and [the_person.possessive_title]. You make sure to get her favorite, the [favorite_drink]."
                    $ mc.business.change_funds(-20)
                    "You come back to the booth with the drinks."
                    the_person.char "Yum! Thank you!"
                "You sit with [the_person.title], enjoying your drinks while chatting."
                call Sarah_get_drunk_dialogue(the_person, intoxication_level) from sarah_drunk_dialogue_01 #found in personality file
                $ intoxication_level += 2
                "After a while the drinks are empty. You consider what to do next."
            "Play some darts":
                mc.name "How about a round of darts?"
                the_person.char "Hell yeah!"
                "You walk over to the dart boards and get ready to have a game."
                call play_darts_301(the_person, focus_mod = -intoxication_level) from play_darts_301_call_date_night_1
                if _return:
                    $ scene_manager.add_actor(the_person, emotion = "sad")
                    "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
                    the_person.char "Damn you're good at that!"
                    $ the_person.change_obedience(5)
                else:
                    $ scene_manager.add_actor(the_person, emotion = "happy")
                    "[the_person.title] gives you a huge smile after winning your game of darts!"
                    the_person.char "Ha! In your face!"
                    $ the_person.change_happiness(5)
                $ intoxication_level += -1

            "Propose sex in the bathroom\n{color=#ff0000}{size=18}Success Chance: [chance_service_him]%%{/size}{/color}" if intoxication_level > 10: #TODO this option currently disabled while it is being written (10 is impossible)
                "You lean in close and whisper to her."
                mc.name "Why don't we take a break from the drinking and sneak back the restroom and do something a little more... physical."
                the_person.char "Oh my..."
                if renpy.random.randint(0,100) < chance_service_him: #Success
                    the_person.char "That sounds hot... okay! Let's do it!"
                    call Sarah_sex_in_the_bar_restroom_label(the_person) from sarah_seduction_public_restroom_1
                else:
                    the_person.char "I'm sorry... the restrooms are always so dirty... why don't we just get out of here?"
                $ loop_count += 5
            "Get outta here":
                $ loop_count += 5


        $ loop_count += 1
    "You step out of the bar with [the_person.title]. You can tell she is hesitant to part ways with you already."
    if intoxication_level < 5:
        the_person.char "So... how about I walk you back to your place?"
    else:
        the_person.char "Sooooo, listen here. I had such a great time tonight. Why don't we go back to your place and mess around a bit?"
        "Her slurred speech make you chuckle."
    menu:
        "Back to your place":
            pass
        "Part ways for tonight":
            mc.name "I had a great time tonight, but I'm afraid we need to part ways for now."
            if intoxication_level < 5:
                the_person.char "Ah, okay. Well have a good night. I think I'm gonna grab a taxi home tonight!"
            else:
                the_person.char "Damn, that's cold! Fine... but could you think you could calls me a taxi? I'm not sure I'm good to walk home..."
                "You call up a local taxi company, soon one is on the way."
            "You stay out front of the bar with [the_person.title] until her cab arrives. You say goodnight and soon the cab is driving off."
            return "Advance Time"

    mc.name "My place sounds great. Let's go!"
    "A short walk later, and you are walking through your front door."
    call Sarah_date_ends_at_your_place_label(the_person) from sarah_date_happy_ending_01
    $ scene_manager.clear_scene()
    return

label Sarah_sex_in_the_bar_restroom_label(the_person):
    #TODO this function
    "This option currently being written."

    return

label Sarah_weekend_date_strip_club_label():
    $ the_person = sarah
    $ scene_manager = Scene()
    $ mc.change_location(strip_club)
    $ mc.location.show_background()
    $ scene_manager.add_actor(the_person, emotion = "happy")
    "After a short walk, you and [the_person.possessive_title] enter the front door of the now familiar strip club."
    "Your senses are assaulted by everything going on. The loud bass music thumps in your ears. On stage you see a girl shaking her ass for a group of guys."
    "You notice several guys checking out [the_person.title] as you find a secluded booth and sit down."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You sit down across from [the_person.possessive_title]."
    "The sights, sounds, and smells of a strip club. There's really nothing quite like it."
    "You consider what you would like to do first."
    $ loop_count = 0
    while loop_count < 5: #Limited number of rounds available
        menu:
            "Watch a dance":
                "You and [the_person.title] chat for a bit until the lights in the room dim in preparation for the next girl's show."
                call watch_strip_show(the_person) from weekend_date_strip_club_strip_call_01
                the_person.char "Ugh, the girls they have working here are so hot."
                $ the_person.change_arousal(renpy.random.randint(5,15))
                $ mc.change_arousal(renpy.random.randint(5,15))
                $ showgirl = None
            "Get a private dance  -$200":
                mc.name "Want to get a private dance? I'll get it setup."
                the_person.char "Ohh, now we're talking! Sounds great!"
                $ scene_manager.remove_actor(the_person, reset_actor = False)
                call Sarah_date_strip_club_private_dance_label(the_person) from weekend_date_strip_club_strip_dance_01
                pass
            "Get outta here":
                $ loop_count += 5
        if the_person.arousal >= 70:
            the_person.char "Hey, so... don't you think its about time for us to get outta here? I'm not sure I can take much more teasing!"
            $ loop_count += 5
            mc.name "Good idea..."

    "You step out of the strip club with [the_person.title]. You can tell she is hesitant to part ways with you already."
    if the_person.arousal < 70:
        the_person.char "That was fun! Can we go back to your place now?"
    else:
        the_person.char "That was hot. I'm am SO worked up. Can we please go back to your place now?"
    menu:
        "Back to your place":
            mc.name "My place sounds great. Let's go!"
            "A short walk later, and you are walking through your front door."
            call Sarah_date_ends_at_your_place_label(the_person) from sarah_date_happy_ending_03
        "Part ways for tonight":
            mc.name "I had a great time tonight, but I'm afraid we need to part ways for now."
            the_person.char "Damn, that's cold! Fine... I'll grab a taxi. Your loss!"
            "You stay out front of the strip club with [the_person.title] until her cab arrives. You say goodnight and soon the cab is driving off."
        "Wait for [cousin.title]" if willing_to_threesome(sarah, cousin):
            "Sorry! This isn't written yet. You decide actually to not wait for her and just head back to your place."

    $ scene_manager.clear_scene()
    return


label Sarah_date_ends_at_your_place_label(the_person):
    $ mc.change_location(hall)
    $ mc.location.show_background()
    $ scene_manager.update_actor(the_person, position = "stand2", character_placement = character_right)
    if Sarah_is_fertile():
        the_person.char "Oh god, I can't wait to feel you fill me up again..."
    else:
        the_person.char "Oh god, I can't wait to feel your hands all over me again..."
    $ scene_manager.add_actor(mom, character_placement = character_left_flipped)
    "[mom.title] pops around the corner when she hears you walking down the hall and unknowingly interrupts."
    mom.char "Ah! It's [the_person.name] again!"
    "[mom.possessive_title] raises her arms and gives [the_person.title] a hug."
    $ scene_manager.update_actor(the_person, position = "kissing")
    $ scene_manager.update_actor(mom, position = "walking_away", character_placement = character_right)
    if mom.sluttiness > 40:
        "[mom.possessive_title] embraces her warmly. In fact it seems to be going on for quite some time..."
        if mom.sluttiness > 80 and the_person.sluttiness > 80:
            the_person.char "Mmmmm..."
            "You hear the soft sound of lips smacking each other... wait are they kissing?"
            "... yep... they are definitely kissing. Damn this is hot."
        elif the_person.sluttiness < 40:
            the_person.char "Awww. Hello [mom.name]. I was just coming over to spend some quality time with [the_person.mc_title]"
    "Eventually they back away from each other."
    $ scene_manager.update_actor(mom, position = "stand4", character_placement = character_left_flipped)
    $ scene_manager.update_actor(the_person, position = "stand2")
    mom.char "Alright, well don't let me keep you. You two have fun!"
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[mom.possessive_title] walks away, chuckling to herself."
    $ scene_manager.remove_actor(mom)

    $ mc.change_location(bedroom)
    $ mc.location.show_background()

    "You reach your bedroom and quickly close and lock the door."
    "[the_person.possessive_title] looks at you."
    the_person.char "Well, I think we both know where this is going!"
    $ scene_manager.strip_actor_outfit(the_person, exclude_feet = True)
    if Sarah_is_fertile():
        the_person.char "Let's go! Ovulating is driving me crazy, I've been daydreaming about your cock filling me with seed all night long!"
    else:
        the_person.char "What are you staring at? Let's go! I've been looking forward to this all night!"
    call fuck_person(the_person, skip_intro = False, girl_in_charge = False) from _call_sex_description_date_happy_ending_1
    "When you finish with her, [the_person.title] collapses in the bed."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You cuddle up next to her as you both catch your breath."
    if the_person.has_role(girlfriend_role):  #You are already dating her via other means. She just cuddles up with you.
        "As you both recover, [the_person.possessive_title] starts kissing you along your neck, then whispers in your ear."
        the_person.char "Thank you for the good time tonight. I love you."
        mc.name "I love you too."
        the_person.char "Do you care if I just stay here tonight? I umm... actually brought my toothbrush..."
        mc.name "Of course! I wouldn't have it any other way!."
        $ the_person.change_love(5)
        $ scene_manager.strip_actor_outfit(the_person, exclude_feet = False)
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "Worn out from your romp with [the_person.possessive_title], you cuddle up with her and quickly fall asleep."
        $ the_person.next_day_outfit = the_person.planned_outfit # she stays the night so she will have to wear the same outfit again
        call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_overnight_after_date
        call Sarah_spend_the_night() from sarah_date_night_happy_ending_gf_path
    elif the_person.has_role(affair_role):
        the_person.char "It feels so good to be next to you, but I need to get home."
        mc.name "You don't have to. Just spend the night here."
        the_person.char "I'm sorry I can't. You know I can't. Thanks for the offer though!"
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand3")
        "You lay on your bed and watch as [the_person.possessive_title] slowly gets her clothes on. She says goodbye then lets herself out."
    else:
        the_person.char "I need to get going... I guess. Thanks for the evening though. It was great!"
        mc.name "You don't have to. Just spend the night here."
        the_person.char "That's tempting, believe me, but I need to get home. Thanks for the offer!"
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand3")
        "You lay on your bed and watch as [the_person.possessive_title] slowly gets her clothes on. She says goodbye then lets herself out."
        return "Advance Time"
    return

label Sarah_date_strip_club_private_dance_label(the_person):
    $ showgirl_1 = get_random_from_list([x for x in stripclub_strippers if x not in [cousin]])
    $ showgirl_2 = get_random_from_list([x for x in stripclub_strippers if x not in [showgirl_1, cousin]])
    if get_strip_club_foreclosed_stage() < 5:
        "You get up and head over to the counter where the owner is."
    else:
        "You get up and head over to the counter and talk with the manager."
    "You look through the list of girls available for private dances."
    if cousin.event_triggers_dict["blackmail_level"] >= 2 and cousin.has_role(stripper_role):
        "You spot your cousin on the list. You could ask for her to dance for either you or [the_person.possessive_title]..."
        menu:
            "Dance for [the_person.title]":
                $ showgirl_1 = cousin
                "You just can't pass up an opportunity to have [cousin.possessive_title] dance for [the_person.title]. You arrange for her to be her private dancer."
            "Dance for you":
                $ showgirl_2 = cousin
                "You just can't pass up an opportunity to have [cousin.possessive_title]'s huge tits in your face. You arrange for her to be your private dancer."
            "Don't ask for her":
                "You decide not to bring [cousin.possessive_title] into the private dance this time."
    else:
        "You don't really care too much about who does the dance, so you pick a couple random girls."

    $ mc.business.change_funds(-200)
    "You go to the back, and find a room with two chairs facing each other. [the_person.title] sits across from you."
    $ scene_manager.add_actor(the_person, position = "sitting", emotion = "happy", character_placement = character_left_flipped)
    the_person.char "Mmm, I'm so nervous..."
    #TODO make a variant on character left that is a close to Sarah so it looks more like an actual lap dance.
    $ showgirl_1.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ scene_manager.add_actor(showgirl_1, character_placement = character_center_flipped)

    $ showgirl_2.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ scene_manager.add_actor(showgirl_2)
    showgirl_2.char "Alright! We got a couple in here tonight, this should be fun!"
    if showgirl_2 is cousin:
        "Suddenly, [showgirl_2.title] realizes its you she is getting ready to dance for."
        "[showgirl_2.possessive_title] lowers her face to your ear and whispers in it."
        showgirl_2.char "Wow, you have your slut here, with you, but you want MY tits in your face? You're a sick fuck."
        "She stands back up and winks at you, then acts as if nothing happened."
    if showgirl_1 is cousin:
        "You see [showgirl_1.title] looking over to you, realizing that you are gonna be in the room as she performs for [the_person.title]"
        "She gives you a quick wink."
    showgirl_1.char "Alright, lets get the fun started!"
    $ scene_manager.update_actor(showgirl_2, position = "kneeling1")
    "Your stripper gets on your lap. She starts to take off her top."
    $ scene_manager.strip_actor_outfit(showgirl_2, exclude_lower = True, exclude_feet = True)
    "With her tits free, she begins to gyrate them back and forth, right in front of your face. They wobble appealingly."
    $ scene_manager.update_actor(showgirl_1, position = "blowjob")
    "You glance over and notice the girl in front of [the_person.title] is doing something similar."
    $ scene_manager.strip_actor_outfit(showgirl_1, exclude_lower = True, exclude_feet = True)
    showgirl_2.char "For $100, you two can play with our tits for a bit."
    if showgirl_2 is cousin:
        "[showgirl_2.title] lowers her lips to your ear again."
        showgirl_2.char "Don't you wanna grab your cousin's tits?"
    "You see [the_person.title] look over at you. You can see her mouth the word 'please'"
    menu:
        "Pay\n{color=ff0000}{size=18}Costs: $100{/size}{/color}" if mc.business.funds >= 100:
            mc.name "That sounds fair."
            "You grab $100 and put it in the tip jar."
            $ mc.business.change_funds(-100)
            "Before you finish putting the money in the jar, you notice that [the_person.title] has her hands all over her stripper's chest."
            "She seems to be really enjoying the show so far!"
            $ mc.change_arousal(10)
            if showgirl_2 is cousin:
                "You reach up and grope [showgirl_2.possessive_title]'s tits. You're mesmerized by how soft and warm they are."
            else:
                "You reach up and begin to fondle your stripper's tits. They are so soft and warm. They feel amazing."
            $ the_person.change_arousal(15)
        "Pay\n{color=ff0000}{size=18}Requires: $100{/size}{/color} (disabled)" if mc.business.funds < 100:
            pass
        "Not today":
            mc.name "We're just here to watch."
            "Glancing at [the_person.title], you can tell she is a little disappointed, but she quickly returns her attention to the girl in front of her."

    "After a while, it's time to change things up. Both strippers get up and turn to so their backs are facing you and [the_person.title]."
    $ scene_manager.update_actor(showgirl_2, position = "standing_doggy")
    $ scene_manager.update_actor(showgirl_1, position = "standing_doggy")
    "Your girl puts her ass against your chest and starts to wiggle her hips back and forth as she slowly works herself down your body."
    "Soon she is working your erection with her hips, through both of your clothes."
    "She starts to strip down her remaining clothing."
    $ scene_manager.strip_actor_outfit(showgirl_2)
    "You notice that [the_person.title] and her stripper are in a similar state."
    $ scene_manager.strip_actor_outfit(showgirl_1)
    "Her ass bare now, you find it difficult to restrain your hands from molesting the girl in front of you."
    $ mc.change_arousal(10)
    $ the_person.change_arousal(10)
    showgirl_2.char "For $200, you two can grope and spank it!"
    menu:
        "Pay\n{color=ff0000}{size=18}Costs: $200{/size}{/color}" if mc.business.funds >= 200:
            "You don't hesitate. You grab $200 and put it in the tip jar."
            $ mc.business.change_funds(-200)
            "[the_person.title] sees you do it and immediately starts to run her hands along her girl's hips."
            if showgirl_2 is cousin:
                "You reach up and grope [showgirl_2.possessive_title]'s ass. It is firm and supple."
                "You give her cheeks a few firm spanks."
                if showgirl_2.sluttiness > 60:
                    "You glance over and notice that [the_person.title] is thoroughly distracted. You run your hand down [showgirl_2.possessive_title]'s ass crack and start to play with her labia."
                    "She stifles a moan. You can feel the humidity radiating from her. She is really worked up!"
                    "You push a finger in and giver her cunt a few strokes. She wiggles her hips for you as you finger her briefly."
                    $ showgirl_2.change_arousal(35)
                    "[showgirl_2.title] looks back and whispers at you."
                    showgirl_2.char "Maybe later you can finish this..."

            else:
                "You reach up and begin to fondle your stripper's ass. It is firm and supple."
                "You give her cheeks a few firm spanks."
            $ the_person.change_arousal(15)
            $ mc.change_arousal(15)
        "Pay\n{color=ff0000}{size=18}Requires: $200{/size}{/color} (disabled)" if mc.business.funds < 200:
            pass
        "Not today":
            mc.name "We're just here to watch."
            "Glancing at [the_person.title], you can tell she is a little disappointed, but she quickly returns her attention to the girl in front of her."

    "Soon it is time for the private dance to end."
    $ scene_manager.update_actor(showgirl_1, position = "stand4")
    $ scene_manager.update_actor(showgirl_2, position = "stand5")
    showgirl_1.char "Mmm, that was fun! It's been forever since I had a female client. They always give such soft touches..."
    if showgirl_2 is cousin and showgirl_2.sluttiness > 80:
        "[showgirl_2.possessive_title] whispers in your ear before she leaves."
        showgirl_2.char "That was fun... if you wait for me to get off work, we could head back to your place for some fun?"
    elif showgirl_2 is cousin:
        "[showgirl_2.possessive_title] whispers in your ear before she leaves."
        showgirl_2.char "I hope your little slut doesn't realize we're related. That would be an unfortunate event, for sure..."
    "The strippers leave, leaving you and [the_person.title] alone and highly aroused."

    $ scene_manager.remove_actor(showgirl_1)
    $ scene_manager.remove_actor(showgirl_2)
    $ del showgirl_1
    $ del showgirl_2
    "You head back out to the main room and sit down at a booth."
    $ scene_manager.update_actor(the_person, position = "sitting", character_placement = character_right)
    return

label Sarah_unlock_special_tit_fuck(the_person):
    the_person.char "So umm... I have a little confession to make."
    "You raise an eyebrow."
    mc.name "Oh? Go ahead then."
    the_person.char "Last night... I was playing with one of my special toys... pretending it was you... obviously."
    the_person.char "It was nice... but I just couldn't get off. I don't know why, it just wasn't feeling right."
    the_person.char "So I took it out, then put it, you know, between my tits..."
    "Interesting"
    the_person.char "I kept imagining you, fucking my tits, cumming all over me."
    $ the_person.change_arousal(20)
    "Her cheeks are starting to get a little flushed."
    the_person.char "I actually came, without even touching myself, you know, down there."
    mc.name "Those serums have made your tits very sensitive. I think it is normal to want to explore all these new sensations you have been having."
    the_person.char "Yeah, of course..."
    "Absent mindedly, she reaches up with one hand and starts to play with one of her breasts."
    $ the_person.change_arousal(20)
    the_person.char "I can't stop thinking about it. Can I... Can I service you with them? Please?"
    mc.name "Go ahead. I want to see if your practice has been paying off."
    if the_person.outfit.tits_available():
        "With her tits already out and ready to be used, she just gives you a big smile."
    else:
        "[the_person.possessive_title] begins to take off her top."
        $ scene_manager.strip_actor_outfit(the_person, exclude_lower = True)
        "With her tits out and ready to be used, she gives you a big smile."
    "She gets up and starts walking around the desk. By the time she gets to you, you already have your rock hard dick out."
    "She gets on her knees and gives you a couple strokes with her hand."
    $ mc.change_arousal(10)
    $ the_person.change_arousal(10)
    the_person.char "Oh god, here we go! Don't hold back, use me like I'm your big titted cum slut!"
    "With her hands on each side of her chest, she wraps her sizable boobs around you and begins to bounce them up and down."
    "Your cock disappears inside of her ample cleavage."
    $ sarah.update_sex_skill("Foreplay", 6)
    $ sarah.max_opinion_score("giving tit fucks")
    call fuck_person(the_person, start_position = sarah_tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _unlock_special_tit_fuck_actual_1
    "Finished, she takes a few moments to recover. You have to admit, she has refined her technique and is very good."
    $ the_person.event_triggers_dict["special_tit_fuck"] = True
    $ the_person.apply_planned_outfit()
    return

label Sarah_fertile_period_start_label():
    $ the_person = sarah
    $ the_person.event_triggers_dict["fertile_start_creampie_count"] = the_person.sex_record["Vaginal Creampies"]
    #TODO add slutty crisis events where Sarah tries to get creampies from MC
    $ add_sarah_fertile_period_end_action()
    return

label Sarah_fertile_period_end_label():
    $ the_person = sarah
    $ success_chance = the_person.sex_record["Vaginal Creampies"] - the_person.event_triggers_dict.get("fertile_start_creampie_count", the_person.sex_record["Vaginal Creampies"])
    if (success_chance * 3) >=  renpy.random.randint(0,100): #She is pregnant!
        $ add_sarah_fertile_period_end_action() #Until we write this segment, just let us have fun trying to make babies without ever actually getting pregnant.
        #TODO make her pregnant!
    else:
        $ add_sarah_fertile_period_start_action()
    return

init 2 python:
    def sarah_foreplay_position_filter(foreplay_positions):
        if sarah_get_special_titfuck_unlocked():
            filter_out = [tit_fuck]
            if foreplay_positions[1] in filter_out:
                return False
            else:
                return True
        return True

    def sarah_oral_position_filter(oral_positions):

        return True

    def sarah_vaginal_position_filter(vaginal_positions):
        if sarah_get_sex_unlocked():
            return True
        return False

    def sarah_anal_position_filter(anal_positions):
        if sarah_get_sex_unlocked():
            return True
        return False

    def sarah_unique_sex_positions(person, prohibit_tags = []):
        positions = []
        if sarah_get_special_titfuck_unlocked() and "Foreplay" not in prohibit_tags:
            positions.append([sarah_tit_fuck, 1])

        return positions

init 1 python:
    def sarah_get_special_titfuck_unlocked():
        return sarah.event_triggers_dict.get("special_tit_fuck", False)

    def sarah_get_sex_unlocked():
        if sarah.event_triggers_dict.get("drinks_out_progress", 0) >= 2:
            return True
        return False
