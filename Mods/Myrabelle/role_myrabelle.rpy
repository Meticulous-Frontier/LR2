# Myrabella is our generic gamer girl archetype. Blue hair, attitude, etc.
# Friends with Alexia from the start, she is opening a gaming cafe and is trying to make money in esports
# Her love story will be her primary story, revolves around her trying to establish an esports brand and make a name for herself
# Timeline involves working to get better, her first tournament (and failure), MC offering to sponsor her, 2nd attempt (success), finally business expansion
# Sluttiness story is a corruption of each step as we go along. When helping her to get better, train her focus while she is playing by fondling her.
# After sponsoring her, MC can add his own serum formular to the drink machines at the gaming cafe, allowing for corruption of the general public.
# When she reveals she didn't get a sponsorship the first time, can tell her she should get bigger tits.
# Myra's bar date opens up the option to play arcade game
#
# Teamup option is Alexia. On friday nights, they start to have all night gaming sessions. At first, MC just plays games with them, but it transitions to massages...
# ... topless massages, fingering, eventually at full corruption start the night with them naked and MC has total free-use while they play video games.

# $ mother_role.actions.append(myra_focus_progression_scene_action)

init 2 python:
    myrabelle_wardrobe = wardrobe_from_xml("Myrabelle_Wardrobe")
    def myrabelle_mod_initialization():
        #Start with her wardrobe and base outfit
         #Requires creation of a new wardrobe file. Alternatively, you can use one of the default ones, IE "Sarah_Wardrobe"
        myrabelle_base_outfit = Outfit("myrabelle's base accessories")
        the_glasses = modern_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [.8, .26, .04, 0.33]
        the_bracelet = bead_bracelet.get_copy()
        the_bracelet.colour = [.4,.6,.93,0.8]
        the_choker = wide_choker.get_copy()
        the_choker.colour = [.15, .15, .15, 1.0]
        the_makeup = light_eye_shadow.get_copy()
        the_makeup.colour = [.0, .28, .67, 0.33]

        myra_job = Job("Gaming Cafe Owner", critical_job_role, job_location = gaming_cafe, work_days = [2,3,4,5,6], work_times = [2,3])
        myra_job.schedule.set_schedule(gaming_cafe, the_days = [5,6], the_times=[1,2,3])    #Extended hours on weekends


        myrabelle_base_outfit.add_accessory(the_lipstick)
        myrabelle_base_outfit.add_accessory(the_bracelet)
        myrabelle_base_outfit.add_accessory(the_glasses)
        myrabelle_base_outfit.add_accessory(the_choker)
        myrabelle_base_outfit.add_accessory(the_makeup)

        # init myrabelle role
        myra_role = Role(role_name ="myrabelle", actions =[myra_train_focus, myra_bigger_tits_serum], hidden = True, on_turn = gaming_cafe_owner_on_turn, on_move = None, on_day = gaming_cafe_owner_on_day)

        #global myrabelle person file
        global myra
        myra = make_person(name = "Myrabelle", # First name
            last_name ="Cassidy",                   # Last Name
            age = 28,                               # Years Old
            body_type = "thin_body",                # Use "thin_body", "standard_body", or "curvy_body". For pregnant, suggest using become_pregnant() function after person is created.
            face_style = "Face_12",                 # 1-4 and 6-14 (5 is missing from vanilla files.)
            tits="B",                               # "AA" "A" "B" "C" "D" "DD" "DDD" "E" "F" "FF"... blame vren for weird sizing.
            height = 0.92,                          # Not sure the limits on this one
            hair_colour="sky blue",                    # See game/mods/Core/Mechanics/Person_Extentions/more_hair_colours.rpy for options
            hair_style = shaved_side_hair,
            #pubes_colour = "sky blue",
            #pubes_style = diamond_pubes,
            skin="white",
            tan_style = None,                       # ?Not sure, presumably mod related
            eyes = "light blue",                    # "dark blue", "light blue", "green", "brown", "grey", or "emerald"
            job = myra_job,                         # Generic job title. Use for random town people or people with jobs OUTSIDE of MC's company
            personality = myrabelle_personality,    # Personality
            custom_font = None,                     #
            name_color = "2a9df4",                 #
            dial_color = "2a9df4" ,                 #
            starting_wardrobe = myrabelle_wardrobe,  # Leave None to make basic wardrobe
            stat_array = [1,3,3],                   # [charisma, int, focus]
            skill_array = [1,1,5,2,1],              # [HR, market, research, production, supply]
            sex_array = [4,1,2,4],                  # [foreplay, oral, vagninal, anal]
            start_sluttiness = 2,                   #
            start_obedience = -5,                   # For some reason Vren adds 100 to this. Use negative values for disobedient girls
            start_happiness = 115,                   #
            start_love = 0,                         #
            start_home = None,                      # Use if this girl is living with someone else
            title = None,                           # Only use if MC knows this girl from the start of the game or whenever she is generated
            possessive_title = None,                # Same as above
            mc_title = None,                        # Same as above
            relationship = "Single",                # "Single", "Girlfriend", "Fiancée", "Married"
            kids = 0,                               #
            SO_name = None,                         # IF she isn't Single
            generate_insta = None,                  # True or False, random if None
            generate_dikdok = None,                 #
            generate_onlyfans = None,               #
            force_random = True,                    # If False, we may grab a pre-generated person for his function from patreon rewards and overwrite her properties!
            base_outfit = myrabelle_base_outfit,     #
            forced_opinions = [["punk", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", -1, False], ["the colour blue", 2, False], ["pants", 1, False], ["gaming", 2, False]],
            forced_sexy_opinions = [["giving handjobs", 2, False], ["showing her ass", 2, False], ["drinking cum", -1, False], ["giving blowjobs", -2, False], ["anal sex", 2, False], ["doggy style sex" ,1, False]])   #random_lists.rpy for list of sexy and normal opinions

        #myra.add_job(unemployed_job)
        myra.generate_home()                                    #Omit this if girl lives with someone else
        myra.set_schedule(myra.home, the_times = [0,1,2,3,4])   #Hide myrabelle at home until we are ready to use her
                                                                    #Any unused times, girl will wander public areas during those time slots.
        myra.home.add_person(myra)                          #Need to add her to the world or MC will not encounter her.

        myra.event_triggers_dict["intro_complete"] = False      #Use this section to init her event_triggers_dict. Useful for character story flags or variables.
        myra.event_triggers_dict["gaming_cafe_open"] = False
        myra.event_triggers_dict["will_grind_with_mc"] = False
        myra.event_triggers_dict["knows_plays_esports"] = False
        myra.event_triggers_dict["can_train_focus"] = False
        myra.event_triggers_dict["has_failed_tournament"] = False
        myra.event_triggers_dict["can_sponsor"] = False
        myra.event_triggers_dict["has_been_sponsored"] = False
        myra.event_triggers_dict["has_won_tournement"] = False
        myra.event_triggers_dict["is_expanding_business"] = False
        myra.event_triggers_dict["focus_train_day"] = 9999
        myra.event_triggers_dict["focus_train_grope"] = False
        myra.event_triggers_dict["focus_train_sit_on_lap"] = False
        myra.event_triggers_dict["focus_train_finger"] = False
        myra.event_triggers_dict["focus_train_assjob"] = False
        myra.event_triggers_dict["focus_train_anal"] = False
        myra.event_triggers_dict["can_distribute_serum"] = False
        myra.event_triggers_dict["weekly_serum"] = None
        myra.event_triggers_dict["suggested_bigger_tits"] = False
        myra.event_triggers_dict["wants_bigger_tits"] = False
        myra.event_triggers_dict["bar_arcade_avail"] = False
        myra.event_triggers_dict["alexia_teamup_start"] = False
        myra.event_triggers_dict["knows_alexia_single"] = False
        myra.event_triggers_dict["character_bought"] = False
        myra.event_triggers_dict["blowjob_train_start"] = False
        myra.event_triggers_dict["blowjob_train_finish"] = False
        myra.event_triggers_dict["blowjob_progress_day"] = 9999
        myra.event_triggers_dict["deepthroat_avail"] = False
        myra.event_triggers_dict["lewd_cafe_open"] = False



        # Below is an example of how you could make a mandatory event that would start the myrabelle character's story. The label and the requirement functions are not included in this template.
        # myrabelle_intro = Action("myrabelle_intro",myrabelle_intro_requirement,"myrabelle_intro_label")
        # mc.business.add_mandatory_crisis(myrabelle_intro) #Add the event here so that it pops when the requirements are met.

        # set town relationships
        # town_relationships.update_relationship(myrabelle, kaya, "Daughter", "Mother")
        town_relationships.update_relationship(alexia, myra, "Friend")
        # town_relationships.update_relationship(lily, myrabelle, "Rival")

        myra.add_role(myra_role)
        downtown.on_room_enter_event_list.append(myra_rude_intro)
        return


#Gaming cafe owner functions
init 1 python:
    def gaming_cafe_owner_on_turn(person): #Use this function to determine if the gaming cafe is open or not. Would on move be better for this?
        if gaming_cafe_is_open():
            if day%7 in [2,3,4] and time_of_day in [0,1]:   #Check if it is previous time slot
                gaming_cafe.public = True
            elif day%7 in [5,6] and time_of_day in [0,1,2]:
                gaming_cafe.public = True
            else:
                gaming_cafe.public = False
        #Here also run if Myra has energy drink and is at the cafe, dose people.
        return

    def gaming_cafe_owner_on_day(person):   #Use this function for if MC is making money from her business.
        pass
        return

#Requirement Functions
init -2 python:
    def myra_rude_intro_requirement():
        if time_of_day == 1 and day > 7:
            return True
        return False

    def myra_gaming_cafe_opening_requirement():
        if gaming_cafe_is_business_hours() and alexia.is_employee():
            return True
        return False

#Actions
init 3 python:
    myra_rude_intro = Action("Meet Myra", myra_rude_intro_requirement, "myra_rude_intro_label")
    myra_gaming_cafe_opening = Action("Gameing Cafe Gran Opening", myra_gaming_cafe_opening_requirement, "myra_gaming_cafe_opening_label")

#Story Labels
label myra_rude_intro_label():
    $ the_person = myra
    $ myra.event_triggers_dict["intro_complete"] = True
    "As you are walking around down town, you stop at a cross walk."
    $ the_person.draw_person()
    "As you stand there, a woman walks up and stands next to you, also waiting at the crosswalk."
    "You are struck by the woman's brightly colored hair. You decide to say hello."
    mc.name "Hi there."
    "She looks at your briefly, then looks away. Did she not hear you?"
    mc.name "I like your hair, it looks great!"
    the_person "Err, thanks."
    mc.name "I'm [mc.name]."
    the_person "Fuck off, I don't talk with creepy randos on the street."
    $ the_person.draw_person(position = "walking_away")
    "As she says that, the crosswalk light turns to walk. She turns away from you and quickly starts walking."
    "You stop and watch her as she walks away. Despite your recent luck with women, you suppose it isn't surprising that not everyone is going to be receptive."
    $ clear_scene()
    "You continue walking, parting ways with the blue haired lady."
    $ mall.on_room_enter_event_list.append(myra_gaming_cafe_opening)
    return

label myra_gaming_cafe_opening_label():
    $ scene_manager = Scene()
    $ the_person = myra
    $ gaming_cafe.visible = True        #Cafe is now open for business and you can go there anytime.
    $ gaming_cafe.public = True
    $ myra.event_triggers_dict["gaming_cafe_open"] = True
    "As you walk around the mall, you notice a large sign."
    "GRAND OPENING: Predator LAN Gaming Cafe! Play for free during our grand opening!"
    "A gaming cafe? That seems interesting. You decide to head over to it."
    $ mc.change_location(gaming_cafe)
    $ mc.location.show_background()
    "As you walk in, the place looks amazing. There are dozens of gaming PCs set up all over the place."
    "The place is pretty crowded, but you still see several open PCs. At the front counter, you spot someone familiar talking to someone behind the counter."
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    $ scene_manager.add_actor(the_person, display_transform = character_right)
    "[alexia.possessive_title] appears to be talking to someone... isn't that the rude girl the other day you tried to talk to downtown?"
    alexia "This is awesome, I can't believe you actually did it."
    the_person "Yeah! It has been a crazy amount of work, but I finally did it!"
    "As you step up, [alexia.title] notices you."
    alexia "Oh hey [alexia.mc_title]! Here to check out the new gaming cafe?"
    mc.name "Indeed I am."
    "The girl behind the counter notices you. You think she remembers you, you notice her scrunch her nose a bit as she looks at you."
    the_person "You know this guy, [alexia.name]?"
    alexia "Yeah! We went to the university around the same time, so we have known each other for a while, but he is actually my boss these days..."
    "The blue haired girl behind the counter appears to be sizing you up."
    mc.name "I'm [mc.name]."
    "She's quiet for a moment longer."
    the_person "I'm [the_person.name], but you can call me Myra."
    $ the_person.set_title("Myra")
    $ the_person.set_possessive_title("Your gamer girl")
    $ the_person.set_mc_title(mc.name)
    "There is a bit of an odd silence for a few seconds."
    alexia "... well this is awkward... have you two met?"
    "Before you can say anything, [the_person.title] answers."
    the_person "He tried hitting on me the other day downtown."
    alexia "Ha! That sounds like him! I take it you shut him down?"
    mc.name "Now wait just a..."
    the_person "Of course."
    mc.name "I was just trying to tell you I thought your hair was very pretty."
    "[the_person.title] rolls her eyes."
    the_person "Right."
    alexia "Don't worry, he probably would have followed it up with a pick up line. But let's be serious here, your hair DOES look great!"
    the_person "Thanks! I got it done in preparation for the grand opening, but I really like it! I think I might keep it like this."
    alexia "You should!"
    mc.name "So I take it you two are friends?"
    alexia "Yep! I've been playing this game called Guild Quest 2, and she is the guild leader."
    mc.name "So you met... playing a game?"
    alexia "No, we go back farther than that, but lately it is mainly when playing that game."
    the_person "Yep! Blonde Cupcake and I go way back."
    alexia "Oh my gosh don't tell..."
    mc.name "Blonde... Cupcake?"
    the_person "That's her character name."
    "You laugh out loud."
    mc.name "Ha! Oh my, that is perfect for her!"
    "[alexia.possessive_title] just sighs."
    $ the_person.change_love(1)
    alexia "Anyway, [alexia.mc_title] here is actually a decent guy. He is the one who bailed me out of my coffee shop job."
    the_person "Ahh, that new marketing job you were telling me about?"
    alexia "Yeah! So, do you have Guild Quest on any of the PCs here already?"
    the_person "You better believe it! Let me show you. How about you [the_person.mc_title]? Want to play for a bit?"
    alexia "Oh! You should! Sit next to me, and I can help you get started!"
    "You've never played this game before, but you figure it couldn't hurt to give it a shot."
    mc.name "Sure, why not."
    the_person "The game has a free trial, but if you wind up liking it, you should probably buy it. Anyway, the PCs over here have the game setup and ready..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You and [alexia.title] follow [the_person.title] to a row of computers."
    "You follow [the_person.title] to one and [alexia.possessive_title] sits next to it."
    $ scene_manager.update_actor(alexia, position = "sitting")
    $ scene_manager.update_actor(myra, position = "standing_doggy")
    "[the_person.title] leans over the computer and starts the game up, and brings up a registration screen. You take a moment to check out her ass."
    "She is skinny but has some very nice curves, especially her back side..."
    $ mc.change_locked_clarity(10)
    $ scene_manager.update_actor(myra, position = "stand3")
    "When she stands back up, she looks at you with a smirk. Did she notice you checking her out? You were trying to be discreet..."
    $ the_person.change_slut(1)
    the_person "Alright, I've got it all setup for you! Have fun you two!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] turns and starts to walk away. You check her out one last time then sit down at the computer."
    alexia "This game is great! You're going to love it!"
    $ scene_manager.remove_actor(the_person)
    "You turn to the computer. You make an account, and soon you have a brand new level 1 ranger named Bud Lightyear."
    alexia "Alright, this is the tutorial area..."
    "You play the game for a while with [alexia.possessive_title]. After a couple hours, you are level 6. "
    "You finish up an event where a giant undead monster rises up out of the swamp. With the help of Blonde Cupcake, you manage to kill it."
    alexia "Alright! Even though I'm max level, when you help noobs in this game, you can still get decent rewards."
    mc.name "That's good, I don't want to be a drag."
    alexia "Don't worry. Well, that is it for the free trial. What did you think?"
    mc.name "Well, I'm not much of a gamer, but it was neat that I can just pop in anytime I want to and make progress on my ranger."
    alexia "You should buy it!"
    $ scene_manager.add_actor(the_person, display_transform = character_right)
    "As she is urging you, [the_person.title] walks up, checking on you and [alexia.title]."
    the_person "Hey, everything working good here?"
    alexia "Yeah this is great! And [alexia.mc_title] just finished up with trial. I'm trying to convince him to buy it!"
    the_person "It is a great game, for hardcore and casual gamers a like, the way it is setup."
    "You think about it. It's only $20, and even though you don't play that many games anymore, it might be a good way to get closer with [alexia.title] and [the_person.title]."
    mc.name "Okay, why not. I'm not sure I'll be able to play much but it's only $20."
    $ alexia.change_happiness(5)
    alexia "Yay! We'll have to get you up to max level so you can help with end game stuff..."
    "[alexia.title] looks at [the_person.title]."
    alexia "Hey, can you add him to the guild?"
    the_person "Ah, that's a good idea! What's the username?"
    "[the_person.title] looks closely at your screen and laughs."
    $ the_person.change_love(1)
    the_person "Bud Lightyear huh? That's pretty funny. I'll send out the invite later when I get the chance."
    $ mc.business.change_funds(-20)
    "You spend a few minutes and buy the game. You've been playing for a while now though and you decide to be done for now."
    "The two girls are talking as you close the game down."
    alexia "This is going to be great. I think I'll start coming her to play on the weekends. The computers are way better than mine, and being around other people is great!"
    the_person "It'll be fun having you around Blonde Cupcake! We'll be closed on Mondays and Tuesdays, but we have extended hours on the weekends!"
    $ alexia.set_schedule(gaming_cafe, the_days = [5,6], the_times = [2,3]) #Alexia plays at the cafe on weekends.
    mc.name "I need to get going, but this has been fun."
    alexia "See ya [alexia.mc_title]."
    the_person "I'll get that guild invite sent out later. Nice to meet you [the_person.mc_title]."
    mc.name "Thanks, you too."
    $ scene_manager.clear_scene()
    "You step away from the computer. This has certainly been an interesting development."
    "Any additional business here at the mall is good, and a gaming cafe should hopefully draw customers."
    "[the_person.title], the woman who is running it, is intriguing. You wonder if you might be able to get to know her better?"
    "She should be here at the cafe while it is open. Maybe you could impress her if you got good at the game she plays?"
    "You might have a chance to play with [alexia.title] sometimes too."
    $ mc.business.event_triggers_dict["guild_quest_level"] = 6
    $ mc.business.event_triggers_dict["guild_quest_name"] = "Bud Lightyear"
    $ mc.business.event_triggers_dict["gaming_cafe_grind_day"] = day
    $ myra.add_unique_on_room_enter_event(myra_esports_practice)
    return

###Love story labels###

init -2 python:
    def myra_esports_practice_requirement(the_person):
        if the_person.love >= 20 and gaming_cafe_is_business_hours() and day%7 < 5:
            return True
        return False

    def myra_esports_first_tournament_requirement():
        if gaming_cafe_is_business_hours() and day%7 == 6:
            return True
        return False

    def myra_train_focus_intro_requirement(the_person):
        if gaming_cafe_is_business_hours() and day%7 < 6 and myra_at_cafe() and the_person.love >= 40:
            return True
        return False

    def myra_train_focus_requirement(the_person):
        if myra_at_cafe() and myra_can_train_focus():
            if myra_last_focus_train_day() + 2 < day:
                return True
            else:
                return "Trained focus too recently."
        return False

    def myra_loses_sponsor_requirement(the_person):
        if the_person.love >= 60 and gaming_cafe_is_business_hours() and myra_at_cafe() and time_of_day == 3:
            return True
        return False

    def myra_gains_sponsor_requirement(the_person):
        if myra_at_cafe() and time_of_day < 3 and mc.business.has_funds(20000):
            return True
        return False

    def myra_esports_second_tournament_intro_requirement(the_person):
        if the_person.love >= 80:
            if myra_focus_progression_scene.get_stage() >= 2 and gaming_cafe_is_business_hours() and myra_at_cafe() and day%7 < 4:
                return True
        return False

    def myra_esports_second_tournament_requirement():
        if gaming_cafe_is_business_hours() and day%7 == 6:
            return True
        return False

    def myra_gaming_cafe_expansion_intro_requirement(the_person):
        if the_person.love >= 95:
            if gaming_cafe_is_business_hours() and myra_at_cafe() and day%7 != 6:
                return True
        return False

init 3 python:
    myra_esports_practice = Action("Myra's Esports Aspirations", myra_esports_practice_requirement, "myra_esports_practice_label")
    myra_esports_first_tournament = Action("Esports Tournament", myra_esports_first_tournament_requirement, "myra_esports_first_tournament_label")
    myra_train_focus_intro = Action("Myra needs help", myra_train_focus_intro_requirement, "myra_train_focus_intro_label")
    myra_train_focus = Action("Help Myra Train Focus", myra_train_focus_requirement, "myra_train_focus_label")
    myra_loses_sponsor = Action("Myra Loses a Sponsor", myra_loses_sponsor_requirement, "myra_loses_sponsor_label")
    myra_gains_sponsor = Action("Myra Gains a Sponsor", myra_gains_sponsor_requirement, "myra_gains_sponsor_label")
    myra_esports_second_tournament_intro = Action("Myra Sets Up New Tournament", myra_esports_second_tournament_intro_requirement, "myra_esports_second_tournament_intro_label")
    myra_esports_second_tournament = Action("Myra's Redemption", myra_esports_second_tournament_requirement, "myra_esports_second_tournament_label")
    myra_gaming_cafe_expansion_intro = Action("Myra Wants to Expand", myra_gaming_cafe_expansion_intro_requirement, "myra_gaming_cafe_expansion_intro_label")



label myra_esports_practice_label(the_person):  #20 love event, on room enter event on myra
    "In this event, you walk into the gaming cafe, but notice that [the_person.title] isn't behind the counter like usual"
    "When you find her, a few people are watching. She is playing a game with a team as part of an esports qualifier."
    "She manages to win the qualifier, therefore placing and earning a spot in an upcoming esports tournament."
    $ myra.event_triggers_dict["knows_plays_esports"] = True
    $ gaming_cafe.on_room_enter_event_list.append(myra_esports_first_tournament)
    return

label myra_esports_first_tournament_label():    #Mandatory event. Preluded to during the first love event
    $ the_person = myra
    "In this event, you watch [the_person.title] take part in her esports tournament."
    "Unfortunately, during one of the early matches, she get distracted by the number of people watching and makes a few fatal mistakes, costing her team the match."
    "You note that she has trouble focusing, and that maybe you can help her with that in the future."
    $ myra.event_triggers_dict["has_failed_tournament"] = True
    $ myra.add_unique_on_room_enter_event(myra_train_focus_intro)
    return

label myra_train_focus_intro_label(the_person): #40 love, room entry event, allows for a recurring event after.
    "After her tournament loss, on a later day, you offer to help [the_person.title] train her focus some."
    $ myra.event_triggers_dict["can_train_focus"] = True
    $ myra.event_triggers_dict["focus_train_day"] = day
    $ myra.add_unique_on_room_enter_event(myra_loses_sponsor)
    $ myra_focus_progression_scene.call_scene([the_person])
    return

label myra_train_focus_label(the_person):   #Her standard corruption event. Slowly devolves from groping to anal. role action
    "This is a recurring label, calling the progression scene for training her focus."
    $ myra_focus_progression_scene.call_scene([the_person])
    return

label myra_loses_sponsor_label(the_person):   #mandatory 60 love event. Has a date at the bar, unlock street fighter, option to sponsor her, spend the night at her place.
    "In this event, you stumble on [the_person.title] closing down her shop early. She confides in MC that she lost her team a sponsorship from a major drink company."
    "Rather lengthy event, you go with her to the bar to have drinks. You offer to sponsor her team, but for now she turns it down."
    "At the bar she has a few drinks with MC and plays street fighter 2 at an arcade box."
    "If MC loses street fighter, she claims it is because MC is distracted by her."
    "MC suggests maybe she should distract opponents when she can during esports tournaments. She says she doesn't have the body for it."
    "MC has the option to suggest bigger tits, which she laughs off for now."
    "After bar date, [the_person.title] spends the night at MC's. Leaves the next morning after telling MC he has given her a LOT of things to think about."
    $ myra.event_triggers_dict["bar_arcade_avail"] = True
    $ myra.event_triggers_dict["can_sponsor"] = True

    $ myra.event_triggers_dict["suggested_bigger_tits"] = True
    $ myra.add_unique_on_room_enter_event(myra_bigger_tits_intro)
    $ myra.add_unique_on_room_enter_event(myra_gains_sponsor)
    return

label myra_gains_sponsor_label(the_person):
    "A few days after the bar date, she asks MC if he was serious about sponsoring her. She tells him the team lost 10k from original sponsor."
    "MC offers a 15k sponsorship, with priority given for future business ventures at the gaming cafe."
    "She accepts and MC thinks to self he should develop a new energy drink at the business. Starts the public serum distribution questline."
    $ myra.event_triggers_dict["has_been_sponsored"] = True
    $ myra.add_unique_on_room_enter_event(myra_esports_second_tournament_intro)
    $ myra.add_unique_on_room_enter_event(myra_develop_energy_drink_intro)
    return

label myra_esports_second_tournament_intro_label(the_person):   #Sets up for the second tournament. on room enter event. 80 love
    "Requires significant progress in the focus training. [the_person.title] announces there is another tournament this weekend."
    "The gaming cafe has actually won the contract for the tournament to be held in person. She is excited but scared how it will go with all the people there."
    #Just use this event to set up anticipation for the tournament itself.
    $ mc.business.add_mandatory_crisis(myra_esports_second_tournament)
    return

label myra_esports_second_tournament_label(): #Mandatory event. Myra wins her second tournament
    $ the_person = myra
    "The tournament itself occurs. [the_person.title] plays a key role on her team, and thanks to her focus training, they place 3rd overall at the tournament."
    "While this isn't first, it is a huge improvement over the last tournament's early exit. Thanks to your sponsorship, you gain a 5% market boost."
    $ myra.event_triggers_dict["has_won_tournement"] = False
    $ myra.add_unique_on_room_enter_event(myra_gaming_cafe_expansion_intro)
    return

label myra_gaming_cafe_expansion_intro_label(the_person):   #100 love event. Myra approaches MC about further expander her business. offers to move in.
    "With winnings from tournaments, [the_person.title] has bought two adjacent shops and is planning to expand her gaming cafe."
    "The gaming cafe expands their hours to open 7 days a week now. She remarks she feels like she barely goes home anymore."
    "She makes a remark that maybe she should just move in with MC because she can barely keep up around her apartment as a joke."
    "MC can either jump on it and tell her to move in with him, or just move on."
    $ myra.event_triggers_dict["is_expanding_business"] = True
    return

###Sluttiness story labels

#Public serum distribution questline

init -2 python:
    def myra_develop_energy_drink_intro_requirement(the_person):
        if the_person.sluttiness > 20 and myra_focus_progression_scene.get_stage() >= 1:    #Must have started focus training
            return True
        return False

    def myra_energy_drink_research_intro_requirement(the_person):
        if the_person.location == rd_division:
            return True
        return False

    def myra_energy_drink_research_final_requirement():
        if mc.business.head_researcher.location == rd_division:
            if renpy.random.randint(0,100) <= 90:
                return True
        return False

    def myra_energy_drink_test_requirement(the_person):
        if myra_at_cafe() and myra_mc_has_acceptable_energy_serum():
            return True
        return False

    def myra_energy_drink_distribution_intro_requirement(the_person):
        if the_person.is_at_work():
            return True
        return False

    def myra_energy_drink_weekly_distribution_requirement():
        if day%7 == 2 and myra_can_distribute_serum() and time_of_day == 1:
            return True
        return False

init 3 python:
    myra_develop_energy_drink_intro = Action("Myra Loves Energy Drinks", myra_develop_energy_drink_intro_requirement, "myra_develop_energy_drink_intro_label")
    myra_energy_drink_research_intro = Action("Develop an Energy Drink", myra_energy_drink_research_intro_requirement, "myra_energy_drink_research_intro_label")
    myra_energy_drink_research_final = Action("New Serum Trait", myra_energy_drink_research_final_requirement, "myra_energy_drink_research_final_label")
    myra_energy_drink_test = Action("Test Your Energy Drink", myra_energy_drink_test_requirement, "myra_energy_drink_test_label")
    myra_energy_drink_distribution_intro = Action("Setup Distribution", myra_energy_drink_distribution_intro_requirement, "myra_energy_drink_distribution_intro_label")
    myra_energy_drink_weekly_distribution = Action("Weekly Energy Drink Distribution", myra_energy_drink_weekly_distribution_requirement, "myra_energy_drink_weekly_distribution_label")




label myra_develop_energy_drink_intro_label(the_person):  #20 sluttiness event. requires sponsorship. on room entry event. Why does this require sluttiness? Replace with something?
    "In this event, MC suggests to [the_person.title] that he could develop a new branded energy drink for her to sell at her business."
    "She indicates that she would be open to that, and requests her favorite flavor, blue raspberry."
    $ mc.business.head_researcher.add_unique_on_talk_event(myra_energy_drink_research_intro)
    $ myra.add_unique_on_room_enter_event(myra_distracted_gaming)
    return

label myra_energy_drink_research_intro_label(the_person):     #On talk event. Propose to research lead energy drink creation
    "MC gives his head researcher an energy drink and blue raspberry flavored candy and asks her to combine the two into a new serum trait."
    $ mc.business.add_mandatory_crisis(myra_energy_drink_research_final)
    return

label myra_energy_drink_research_final_label():     #On talk event. Test energy drink with head researcher
    $ the_person = mc.business.head_researcher
    "Head researcher comes back to MC with details of a new serum trait. The flavor is strong enough to override any other serum traits in the drink."
    $ myra.add_unique_on_talk_event(myra_energy_drink_test)
    return

label myra_energy_drink_test_label(the_person):
    "After making a serum with the energy drink trait, take one to [the_person.title] to try it. She approves."
    $ alexia.add_unique_on_room_enter_event(myra_energy_drink_distribution_intro)
    return

label myra_energy_drink_distribution_intro_label(the_person):     #On talk event. Work out details of distributing energy drink at gaming cafe with myra
    "You talk to Alexia about taking some energy drink over to the gaming cafe every Wednesday."
    $ mc.business.add_mandatory_crisis(myra_energy_drink_weekly_distribution)
    return

label myra_energy_drink_weekly_distribution_label():          #mandatory event. select which serum to distribute for the week.
    "This is a weekly recuring event. Alexia comes to MC and MC can select which serum to send over to the gaming cafe for the week."
    $ mc.business.add_mandatory_crisis(myra_energy_drink_weekly_distribution)
    return



init -2 python:
    def myra_bigger_tits_intro_requirement(the_person):
        if the_person.sluttiness >= 40 and myra_at_cafe():
            return True
        return False

    def myra_bigger_tits_serum_requirement(the_person):
        if myra_wants_bigger_tits() and not myra.has_large_tits():
            if myra_at_cafe():
                return True
        return False

    def myra_bigger_tits_final_requirement(the_person):
        if myra.has_large_tits() and myra_at_cafe():
            return True
        return False

    def myra_distracted_gaming_requirement(the_person):
        if the_person.sluttiness >= 40 and myra_at_cafe():
            return True
        return False

    def myra_blowjob_training_intro_requirement(the_person):
        if myra_alexia_teamup_scene.get_stage() >= 2:
            if myra_at_cafe():
                return True
        return False

    def myra_blowjob_training_progress_requirement(the_person):
        if myra_at_cafe() and myra.event_triggers_dict.get("blowjob_progress_day", 9999) + 7 <= day:
            return True
        return False

    def myra_blowjob_training_final_requirement(the_person):
        if myra_at_cafe() and myra.event_triggers_dict.get("blowjob_progress_day", 9999) + 7 <= day:
            return True
        return False

    def myra_adult_gaming_intro_requirement(the_person):
        if the_person.sluttiness >= 80:
            if myra_is_expanding_business() and myra_at_cafe():
                return True
        return False

    def myra_adult_gaming_opening_requirement():
        if myra_at_cafe() and myra.event_triggers_dict.get("adult_cafe_opening_day", 9999) + 14 <= day:
            return True
        return False

    def myra_harem_entry_requirement():
        return False

init 3 python:
    myra_bigger_tits_intro = Action("Myra Wants Bigger Tits", myra_bigger_tits_intro_requirement, "myra_bigger_tits_intro_label")
    myra_bigger_tits_serum = Action("Give Serum for Bigger Tits", myra_bigger_tits_serum_requirement, "myra_bigger_tits_serum_label")
    myra_bigger_tits_final = Action("Myra Gets Large Tits", myra_bigger_tits_final_requirement, "myra_bigger_tits_final_label")
    myra_distracted_gaming = Action("Myra Distracts Her Opponents", myra_distracted_gaming_requirement, "myra_distracted_gaming_label")
    myra_blowjob_training_intro = Action("Myra Needs Help", myra_blowjob_training_intro_requirement, "myra_blowjob_training_intro_label")
    myra_blowjob_training_progress = Action("Develop Myra Orally", myra_blowjob_training_progress_requirement, "myra_blowjob_training_progress_label")
    myra_blowjob_training_final = Action("Develop Myra Orally", myra_blowjob_training_final_requirement, "myra_blowjob_training_final_label")
    myra_adult_gaming_intro = Action("Myra Wants Lewd Cafe", myra_adult_gaming_intro_requirement, "myra_adult_gaming_intro_label")
    myra_adult_gaming_opening = Action("Myra Opens Lewd Cafe", myra_adult_gaming_opening_requirement, "myra_adult_gaming_opening_label")
    myra_harem_entry = Action("Harem: Myra", myra_harem_entry_requirement, "myra_harem_entry_label")

#Bigger tits questline

label myra_bigger_tits_intro_label(the_person):        #40 sluttiness event. If MC suggested bigger tits in love story, myra is interested now.
    "[the_person.title] asks MC if he was being serious that she should get bigger tits."
    "MC can choose yes or no. If no abandon this series."
    "If yes, she says she is scared to get implants, that they might mess up or whatever."
    "MC can say that his company has the ability to make an experimental serum to grow her tits naturally."
    "She agrees to try them."
    $ myra.event_triggers_dict["wants_bigger_tits"] = True  #This will open up the option on her role
    $ myra.add_unique_on_talk_event(myra_bigger_tits_final)
    return

label myra_bigger_tits_serum_label(the_person):       #This option becomes available if Myra wants bigger tits.
    "MC offers [the_person.title] the serum that will grow her tits."
    return

label myra_bigger_tits_final_label(the_person):       #If her tits are bigger, she thanks MC.
    "Once [the_person.title]'s tit size passes the large tits threshold, she thanks MC and offers to let him fuck them."
    $ myra.event_triggers_dict["wants_bigger_tits"] = False
    return

label myra_distracted_gaming_label(the_person):       #40 sluttiness event. MC can suggest she should distract her opponents by dressing slutty. second chance to suggest bigger tits
    $ myra.event_triggers_dict["suggested_bigger_tits"] = True
    "If MC didn't suggest bigger tits earlier, have a second chance."
    "[the_person.title] is practicing. MC notices her using sultry tones and double entendres for callouts, causing a bit of a distraction for other players."
    "After the match, MC can suggest she gets bigger tits to distract her opponents. If he doesn't, he just enjoys her teasing the opponents."
    $ myra.event_triggers_dict["wants_bigger_tits"] = True
    $ myra.add_unique_on_talk_event(myra_bigger_tits_final)
    $ myra.add_unique_on_room_enter_event(myra_blowjob_training_intro)
    return

label myra_blowjob_training_intro_label(the_person):      #60 sluttiness event. Myra ask for blowjob training after sessions with MC and Alexia.
    "Requires progress in the event with [alexia.title]."
    "[the_person.title] says she's always hated giving blowjobs... until she met MC."
    "Asks MC who gives better blowjobs, her or [alexia.title]. MC is honest and says [alexia.title]."
    "She asks MC if he would be willing to help her get better at blowjobs. MC obviously agrees."
    "This starts a three part questline where we get her trained to be a good oral slut."
    "In the first training session, we teach [the_person.title] that the most important part of BJs is to have a good attitude."
    "Don't be fake, but enthusiasm goes a long way."
    "Setup the next event to be available in a week."
    $ myra.event_triggers_dict["blowjob_train_start"] = True
    $ myra.event_triggers_dict["blowjob_progress_day"] = day
    $ myra.add_unique_on_room_enter_event(myra_blowjob_training_progress)
    return

label myra_blowjob_training_progress_label(the_person):
    "Part two of [the_person.title]'s blowjob training."
    "MC works with her on going deep. Let's her set the pace for the most part. She gags a lot but struggles though it."
    "At the end, suggest that she practice deepthroating. Opens up the deepthroat position via filters."
    "Setup final scene to be available in a week."
    $ myra.event_triggers_dict["deepthroat_avail"] = True
    $ myra.event_triggers_dict["blowjob_progress_day"] = day
    $ myra.add_unique_on_room_enter_event(myra_blowjob_training_final)
    return

label myra_blowjob_training_final_label(the_person):
    "After training her throat for a week, [the_person.title] is ready for final training."
    "In this session, you teach her to relax her throat and to be submissive."
    "She struggles for a bit, but finally manages to let go and you face fuck her."
    "At the end, she asks MC to help Alexia win gaming night this week, she wants to show off her face fucking skill to her friend."
    $ myra.event_triggers_dict["blowjob_train_finish"] = True
    $ myra.add_unique_on_room_enter_event(myra_adult_gaming_intro)
    return

label myra_adult_gaming_intro_label(the_person):    #80 sluttiness event. requires finishing her love story, Myra wabts to open adults only section of the cafe.
    "[the_person.title] asks MC for some feedback on an idea. Want's to know his opinion because he is sponsor and scared she will lose money."
    "She wants to open an adults only lewd section to the gaming cafe. Want's to know what MC thinks about it."
    "MC thinks it is a great idea. She says check back at a later time."
    $ mc.business.add_mandatory_crisis(myra_adult_gaming_opening)
    $ myra.event_triggers_dict["adult_cafe_opening_day"] = day
    return

label myra_adult_gaming_opening_label():
    $ the_person = myra
    "[the_person.title] is excited, opens new adults only section of the gaming cafe. Texts MC to meet her there."
    "It has restricted entry via ID card scanner. Clothing is optional and anything goes there. PCs are loaded with pornographic games."
    "When MC walks back, there are already a few girls back there. MC spots a woman playing an adult game and with [the_person.title]'s encouragement, approaches her."
    "Without any introductions, she agrees to suck MC's cock while she plays."
    "This unlocks a new gaming cafe action. Entering the adults only section. The game will grab a random girl sluttiness >40 there for MC to play with."
    $ myra.event_triggers_dict["lewd_cafe_open"] = True
    $ myra.add_unique_on_room_enter_event(myra_harem_entry)
    return

label myra_harem_entry_label(): #100 sluttiness event. If MC already has a harem started, you initiate Myra into it
    "This label is referring to a harem mechanic that does not yet exist."
    return


#Myra related wrappers
init 3 python:
    def myra_intro_complete():
        return myra.event_triggers_dict.get("intro_complete", False)

    def gaming_cafe_is_open():
        return myra.event_triggers_dict.get("gaming_cafe_open", False)

    def gaming_cafe_is_business_hours():
        if day%7 in [2,3,4] and time_of_day in [2,3]:
            return True
        if day%7 in [5,6] and time_of_day in [1,2,3]:
            return True
        return False

    def myra_will_grind_with_mc():
        return myra.event_triggers_dict.get("will_grind_with_mc", False)

    def myra_last_focus_train_day():
        return myra.event_triggers_dict.get("focus_train_day", 9999)

    def myra_has_exclusive_energy_drink():
        return myra.event_triggers_dict.get("weekly_serum", None)

    def myra_get_exclusive_energy_drink():
        return myra.event_triggers_dict.get("weekly_serum", None)

    def myra_can_train_focus():
        return myra.event_triggers_dict.get("can_train_focus", False)

    def myra_has_failed_tournament():
        return myra.event_triggers_dict.get("has_failed_tournament", False)

    def myra_can_sponsor():
        return myra.event_triggers_dict.get("can_sponsor", False)

    def myra_has_been_sponsored():
        return myra.event_triggers_dict.get("has_been_sponsored", False)

    def myra_has_won_tournament():
        return myra.event_triggers_dict.get("has_won_tournement", False)

    def myra_is_expanding_business():
        return myra.event_triggers_dict.get("is_expanding_business", False)

    def myra_can_distribute_serum():
        return myra.event_triggers_dict.get("can_distribute_serum", False)

    def bar_date_arcade_avail():
        return myra.event_triggers_dict.get("bar_arcade_avail", False)

    def myra_suggested_bigger_tits():
        return myra.event_triggers_dict.get("suggested_bigger_tits", False)

    def myra_wants_bigger_tits():
        return myra.event_triggers_dict.get("wants_bigger_tits", False)

    def myra_knows_alexia_single():
        return myra.event_triggers_dict.get("knows_alexia_single", False)

    def myra_mc_bought_character():
        return myra.event_triggers_dict.get("character_bought", False)

    def myra_started_blowjob_training():
        return myra.event_triggers_dict.get("blowjob_train_start",False)

    def myra_finish_blowjob_training():
        return myra.event_triggers_dict.get("blowjob_train_finish", False)

    def myra_deepthroat_avail():
        return myra.event_triggers_dict.get("deepthroat_avail", False)

    def myra_lewd_cafe_open():
        return myra.event_triggers_dict.get("lewd_cafe_open", False)

    def myra_at_cafe():
        return myra.location == gaming_cafe

    def myra_acceptable_energy_serum(the_serum):    #Use this to specify if a serum is acceptable to use as an energy drink.
        return False

    def myra_mc_has_acceptable_energy_serum():
        return False
