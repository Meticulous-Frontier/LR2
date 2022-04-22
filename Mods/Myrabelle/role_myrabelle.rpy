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
# progress = 2/29
# 25/67
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
            if day%7 in [2,3,4] and time_of_day in [1,2]:   #Check if it is previous time slot
                gaming_cafe.public = True
            elif day%7 in [5,6] and time_of_day in [1,2,3]:
                gaming_cafe.public = True
            else:
                gaming_cafe.public = False
            if myra_at_cafe() and myra_has_exclusive_energy_drink():
                gaming_cafe_dose_customers()
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
        if gaming_cafe_is_business_hours() and day%7 == 6 and myra.love >= 40:
            return True
        return False

    def myra_train_focus_intro_requirement(the_person):
        if gaming_cafe_is_business_hours() and day%7 < 6 and myra_at_cafe():
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
    "You step into the gaming cafe. As you start to walk over to the main counter, however, you realize that there isn't anyone there."
    "You wonder where [the_person.possessive_title] might be? You scan the room."
    "Near one side, you see a small group of about 8 people watching a computer. You can't tell who is playing, so you walk over."
    "When you get there, you see [the_person.title] playing."
    $ the_person.draw_person(position = "sitting")
    "She appears to be in a pretty tight match. You ask one of the other people watching."
    mc.name "Hey, why is everyone watching her play?"
    "?????" "She's at the end of a tournament. If her team wins, they automatically qualify for the Esports tournament Battle of the Bay."
    "Ahhh, so it is like a qualifying round."
    "You watch as she plays. [the_person.possessive_title] is manhandling her competition."
    "In a climactic battle, she manages to stall two attackers at home point while her team finishes off the other team at mid, securing the victory."
    the_person "Yes! We did it!"
    $ the_person.draw_person()
    "[the_person.title] jumps to her feet. All the people watching her cheer and start to give each other high fives."
    "?????" "Way to go!"
    "?????" "Nice going!"
    "The small group congratulate her on the win. Eventually she gets to you."
    the_person "Oh hey [the_person.mc_title]! Did you see?"
    mc.name "I did! Congratulations! When is the tournament?"
    the_person "I'm actually not sure. I know it is usually on a Sunday, but I'm not sure how close it is."
    mc.name "Neat. I can't wait to watch!"
    the_person "Yeah! I'll have to set up something for it. It is an online thing, so I'll be able to play for the cafe here. Maybe I could put it up on the main projection screen."
    mc.name "That is an excellent idea."
    the_person "Thanks! Oh my god, I gotta go text [alexia.name], she is going to be so excited. I'll see you around, okay?"
    mc.name "Sounds good."
    $ myra.event_triggers_dict["knows_plays_esports"] = True
    $ gaming_cafe.on_room_enter_event_list.append(myra_esports_first_tournament)
    $ the_person.draw_person(position = "walking_away")
    "Wow, so [the_person.possessive_title]'s eSports team has managed to qualify for a big tournament! You'll have to see if you can attend."
    return

label myra_esports_first_tournament_label():    #Mandatory event. Preluded to during the first love event
    $ the_person = myra
    "You feel your phone go off when you get a notification. It's a message from [alexia.possessive_title]"
    $ mc.start_text_convo(alexia)
    alexia "Hey! I don't know what you are doing right now, but get over to the gaming cafe!"
    alexia "[the_person.name] is hosting a watch party for her eSports tournament! She asked me to text you because she doesn't have your number I guess."
    alexia "It's going to start soon!"
    mc.name "Thanks! I'm on my way. Save me a seat?"
    alexia "Sure!"
    $ mc.end_text_convo()

    "Alright, this should be interesting. You head over to the gaming cafe."
    $ mc.change_location(gaming_cafe)
    $ mc.location.show_background()
    $ scene_manager = Scene()
    "When you get there, you look around. A bunch of seats have been set up to watch a projector screen. There is actually a fairly large crowd here... you estimate about 100 people."
    "You look around. Eventually you spot [alexia.title] with an open seat next to her. You walk over and sit next to her."
    $ scene_manager.add_actor(alexia, position = "sitting", display_transform = character_right)
    mc.name "Hey! Thanks for saving me a seat."
    alexia "Hey [alexia.mc_title]! I had to shoo away several cute guys, so I hope you can manage to keep me good company for this!"
    if alexia.is_single():
        mc.name "I'll do my best. Is [the_person.title] here?"
    else:
        mc.name "Ah, I didn't realize you were in the market for cute guys?"
        alexia "I, ermm... I mean I'm not..."
        mc.name "I'm just teasing. Is [the_person.title] here?"
    alexia "Yeah. She's over there."
    "You follower [alexia.possessive_title]'s finger pointing to a computer desk set up to the side of the project. [the_person.possessive_title] is there, getting setup."
    $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_left(yoffset = 0, zoom = 0.5))
    alexia "You are just in time, it is just getting started!"
    mc.name "Nice. Can you fill me in on the details?"
    alexia "Sure. This first match should be just a warm up for them. Technically it is an elimination match, but her team should win pretty easily."
    mc.name "Nice."
    "You chit chat with [alexia.title] for a bit, but soon the match starts up."
    "You look over at [the_person.possessive_title]. Her hands are on the keyboard, but she is shaking a little bit. It appears her nerves might be getting to her a bit?"
    mc.name "Has she ever played in something like this before?"
    alexia "No, this is her first time in a big tournament like this."
    "Oh boy. Nerves can be a powerful thing. You hope she is able to do well."
    "The match begins. You watch on the projector as [the_person.possessive_title] starts out. She plays conservatively, sticking with her team as they attack the center point."
    "The battle for the center point looks hard fought. You watch as [the_person.title]'s team manages to down an enemy, but when trying to finish them off, the enemy team successfully revives them."
    "As her team pulls back, [the_person.title]'s team has a player get downed. She quickly stealths and is able to revive them quickly."
    alexia "Wooo! You go girl!"
    "Several people in the crowd cheer for her. However, the spike in noise almost seems to startle her. She looks up from her computer and sees how many people are watching."
    "She turns back to the computer, but you note that her playstyle suddenly gets a bit rougher. She isn't capitalizing on as many opportunities and is playing too conservatively."
    "When another teammate get's downed, she attempts to stealth again to revive them. This time, however, the enemy team uses a stealth removal skill and stun her. They manage to down her and kill off her teammate."
    "A few seconds later, the enemy finishes her off, taking the center point. You hear some mumbles in the crowd as her respawn timer comes up."
    mc.name "[alexia.title]... she is completely off her game. Her nerves are really getting to her."
    alexia "Yeah... she'll pull through though! I'm sure she'll come back..."
    "The match continues, but unfortunately, [the_person.possessive_title] is unable to shake off her first time tournament jitters."
    "In an unfortunate encounter, she and a teammate engage the enemy two on two at her home point. Normally she is able to carry in these situations easily, but this time she fumbles."
    "Pushing to far against a low health enemy, suddenly they counter her attack and stun her. Before she can react, the enemy pair down her. Caught far from her teammate, she can only watch as they finish her off."
    $ scene_manager.update_actor(the_person, emotion = "sad")
    "The match itself stays fairly close as [the_person.title] push back and forth at a couple points. However, she just isn't able to tip the balance in their favor."
    "When the match is over, the score is close, but [the_person.possessive_title] is the worst performer on her team. If she had been able to focus better, they would have won."
    "The crowd is stunned. You turn to [alexia.title]."
    alexia "Oh... oh no... Myra..."
    "The people who were watching the match start to get up. There are several murmurs but nobody reall says much."
    "You watch as [the_person.title] gets up and quietly leaves the room. She looks pretty disappointed."
    $ scene_manager.remove_actor(the_person)
    $ scene_manager.update_actor(alexia, position = "stand3", emotion = "sad")
    mc.name "That was too bad. She looked really off her normal game there."
    alexia "I know! Gosh I don't know what to do... should I text her?"
    mc.name "I don't know. She might just want some space after that."
    alexia "You're right... I'll text her later."
    mc.name "Yeah... anyway, [alexia.title], thanks for letting me know about this. I appreciate it."
    alexia "Ah, of course."
    mc.name "I'm going to get going. Take care."
    alexia "See ya."
    $ scene_manager.clear_scene()
    "You stand up and walk out of the gaming cafe."
    "That was hard to watch. You are sure that [the_person.possessive_title] is devasted at the result."
    "You wonder to yourself. Could helping her with her focus be something that you could help with?"
    "Surely there are ways that you could help her out. Maybe you should wait a few days and talk to her about it?"
    $ myra.event_triggers_dict["has_failed_tournament"] = True
    $ myra.add_unique_on_room_enter_event(myra_train_focus_intro)
    return

label myra_train_focus_intro_label(the_person): #40 love, room entry event, allows for a recurring event after.
    $ myra.event_triggers_dict["can_train_focus"] = True
    $ myra.event_triggers_dict["focus_train_day"] = day
    $ myra.add_unique_on_room_enter_event(myra_loses_sponsor)
    $ myra_focus_progression_scene.call_scene([the_person])
    return

label myra_train_focus_label(the_person):   #Her standard corruption event. Slowly devolves from groping to anal. role action
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
            if renpy.random.randint(0,100) <= 100:
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
    $ the_person.draw_person(emotion = "angry")
    "You step into the gaming cafe. You notice [the_person.possessive_title] talking on her phone angrily."
    "You walk over to her and see what is going on."
    the_person "No! Come on, that's crazy! Those are like my favorite!"
    the_person "No... you know what? FINE! I'll just find a competitor!"
    "She clicks her phone off."
    mc.name "You okay?"
    the_person "NO! I'm fucking not!"
    mc.name "What's going on?"
    the_person "I just got off the phone. My beverage supplier said they can't supply the store here with my favorite energy drinks anymore!"
    the_person "How am I supposed to get my game on if I can't even concentrate!?!"
    "You think about it for a moment. What is even in energy drinks? They can't be that hard to make... maybe you could make some?"
    mc.name "I have a crazy idea."
    the_person "I'm listening..."
    mc.name "I run a pharmaceuticals company... it can't be that hard to come up with an energy drink formula."
    mc.name "What if I put something together and I can supply you with energy drinks for you to distribute?"
    mc.name "I mean, I'm already a sponsor. It would be good exposure for my company and you could have an exclusive deal on an energy drink."
    the_person "Hmm..."
    $ the_person.draw_person(emotion = "happy")
    the_person "That is is actually a pretty damn good idea..."
    mc.name "I know right? What is your favorite flavor?"
    the_person "Me? Oh... well I've always loved blue raspberry flavored stuff..."
    mc.name "Give me a few weeks and see what I can come up with. I'll come up with a formula and run some basic tests and if you like it, I'll supply it."
    "She thinks about your proposal for a moment."
    the_person "Alright... Let me know what you come up with!"
    "You have agreed to try and provide [the_person.title] with a new energy drink for her gaming cafe!"
    "The only problem is... you have no idea how to make energy drinks!"
    "You should talk to your head researcher. Maybe she can help you formulate a new serum trait to mimic an energy drink syrup?"
    $ mc.business.head_researcher.add_unique_on_talk_event(myra_energy_drink_research_intro)
    $ myra.add_unique_on_room_enter_event(myra_distracted_gaming)
    return

label myra_energy_drink_research_intro_label(the_person):     #On talk event. Propose to research lead energy drink creation
    "You step into the research and development wing and step over to your head researcher's desk."
    $ the_person.draw_person(position = "sitting")
    "You set down on her desk an energy drink and blue raspberry flavored hard candy."
    the_person "Ah, hello [the_person.mc_title]. Is this supposed to help me get more research done? I'm not really into energy drinks..."
    mc.name "No, but a lot of people DO like energy drinks. I was hoping you could do some research for me on how they work..."
    mc.name "...And make it flavored like the blue raspberry, so we can market serums as energy drinks."
    the_person "Ahah. I think I understand what you are trying to do. I'm pretty sure these things are just some B vitamins and caffeine..."
    "She looks at the items for a moment."
    the_person "Give me a few days and I'll let you know what I can come up with, okay?"
    mc.name "Thank you [the_person.title]. I appreciate it."
    "You step away from [the_person.possessive_title]'s desk. She will contact you when she comes up with a solution."
    $ mc.business.add_mandatory_crisis(myra_energy_drink_research_final)
    return

label myra_energy_drink_research_final_label():     #On talk event. Test energy drink with head researcher
    $ the_person = mc.business.head_researcher
    if mc.location == mc.business.r_div:
        the_person "[the_person.mc_title], I have some good news."

    else:
        $ mc.start_text_convo(the_person)
        the_person "I have something for you to see. Can you come to the lab?"
        mc.name "I'm on my way."
        $ mc.end_text_convo()
        "You make your way to the research division."
        $ mc.business.r_div.show_background()
    $ the_person.draw_person()
    the_person "I have a serum trait that I think meets your specifications."
    "[the_person.possessive_title] holds out a small blue vial."
    the_person "Several B, C, and D vitamins, zinc, and caffeine."
    the_person "Hit it hard with raspberry flavoring, blue dye, and some high fructose corn syrup, and voila!"
    the_person "Add this to any serum, along with 8 ounces of carbonated water, and the flavor is strong enough to cover up any chemical tastes from the other serum traits we include."
    mc.name "That's great. Any downsides?"
    the_person "Well, watering down serums reduces the length of time that the serum is effective for. And it will take up a trait slot in the research phase from something more useful."
    mc.name "That is great. Thank you [the_person.title]"
    the_person "No problem."
    $ myra_unlock_energy_drink_serum()
    $ myra.add_unique_on_talk_event(myra_energy_drink_test)
    "You have unlocked the energy drink serum trait!"
    "Create a new serum using the trait and take it to [myra.possessive_title], and if she likes it you can start distrubiting it there to the public!."
    "For now, you should probably not do anything too controversial. Keep the attention of the serum 2 or less, and don't distribute any nanobots!"
    return

label myra_energy_drink_test_label(the_person):
    $ the_serum = get_random_from_list(mc.inventory.get_serums_with_trait(energy_drink_serum_trait))
    "You walk into the gaming cafe. At the main desk, you spot [the_person.title] and approach her."
    $ the_person.draw_person()
    mc.name "Good day [the_person.title]."
    the_person "Hey [the_person.mc_title]."
    mc.name "I have something for you."
    "You set a can of your new energy drink and set it on the table."
    mc.name "One proprietary, blue raspberry flavored energy drink."
    the_person "Wow! This is neat... May I?"
    mc.name "Of course."
    "[the_person.possessive_title] takes the drink and opens it. She gives it a sniff, then takes a long sip."
    $ mc.inventory.change_serum(the_serum,-1)
    $ the_person.give_serum(copy.copy(the_serum), add_to_log = True)
    "She smiles."
    the_person "Hey... that is really good!"
    "She takes another long sip."
    the_person "What all is in it?"
    mc.name "Well, I'll be honest, it was mostly done by my head researcher, but she said there are a lot of vitamins in it, some caffeine, and zinc."
    "[the_person.title] keeps drinking it."
    mc.name "After that, we had to balance the raspberry flavor, and added some sweetness with corn syrup."
    "You conveniently leave out the remaining serum traits that went into the production. [the_person.possessive_title] takes several large gulps."
    mc.name "We have nutritional facts we can publish, as well as an ingredient and allergen list."
    "She tips up her drink and finishes it off."
    the_person "This is incredible. I love it!"
    $ the_person.change_love(2)
    $ the_person.change_obedience(2)
    the_person "I feel more energized already. Alright, if you can make delivery on Wednesday mornings, I'll set it up to sell!"
    mc.name "Sounds good. I'll arrange for delivery with one of my employees."
    the_person "This is fucking awesome. What do you call it?"
    mc.name "Well, we have an internal name for it, but it isn't really something we would call on brand for you."
    mc.name "Since it is made to your specifications, why not call it something like Myra's Gaming Fuel."
    the_person "Ooo! I like it!"
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title] throws her arms around you and gives you a big hug."
    the_person "Thank you [the_person.mc_title]! This is going to be great!"
    mc.name "I agree."
    $ clear_scene()
    "You step away from the desk after saying goodbye. You should setup delivery of the serum with one of your employees."
    $ delivery_person = None

    if alexia.is_employee():
        $ myra.event_triggers_dict["energy_drink_supplier"] = alexia.identifier
        "Since [alexia.possessive_title] is working for you, it makes sense to have her do the deliveries. You should talk to her about it next chance you get."
        $ delivery_person = alexia
    else:
        "No one really stands out to you as an obvious choice for who to have run the deliveries."
        "Who should you talk to about it?"
        call screen enhanced_main_choice_display(build_menu_items([["Call in"] + mc.business.get_employee_list() ], draw_hearts_for_people = False))
        $ delivery_person = _return
        $ myra.event_triggers_dict["energy_drink_supplier"] = delivery_person.identifier
        "You decide to talk to [delivery_person.title] about running the deliveries. You should talk to her about it as soon as practical."
    $ delivery_person.add_unique_on_room_enter_event(myra_energy_drink_distribution_intro)
    return

label myra_energy_drink_distribution_intro_label(the_person):     #On talk event. Work out details of distributing energy drink at gaming cafe with myra
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. I want to talk to you about something."
    the_person "Oh? Go ahead."
    if the_person == alexia:
        mc.name "The company has developed a new energy drink for [myra.title] to sell over at the gaming cafe. I was hoping you could run the deliveries for me."
        the_person "Oh! That is really neat! I bet she is exited! When do you want me to run the deliveries out?"
    else:
        mc.name "The company has started sponsoring an esports team at the local gaming cafe. We have developed an exclusive energy drink to sell there."
        mc.name "I want you to be in charge of running the deliveries every week."
        the_person "Okay, I can do that. When do you want me to do the deliveries?"
    "You talk to [the_person.title] about taking some energy drink over to the gaming cafe every Wednesday."
    the_person "Okay, I'll talk to you on Wednesday morning then."
    $ mc.business.add_mandatory_crisis(myra_energy_drink_weekly_distribution)
    $ myra.event_triggers_dict["can_distribute_serum"] = True
    "[the_person.possessive_title] will be running your deliveries. Make sure you have atleast 10 of the serum in the company's inventory to send to the gaming cafe."
    return

label myra_energy_drink_weekly_distribution_label():          #mandatory event. select which serum to distribute for the week.
    $ contact = myra.event_triggers_dict.get("energy_drink_supplier", None)
    $ new_delivery_person = False
    $ finished = False
    if contact == None:
        "Unfortunately, your delivery person is not available anymore. You decide to appoint someone new to do it."
        call screen enhanced_main_choice_display(build_menu_items([["Call in"] + mc.business.get_employee_list() ], draw_hearts_for_people = False))
        $ the_person = _return
        $ myra.event_triggers_dict["energy_drink_supplier"] = delivery_person.identifier
        $ new_delivery_person = True
    else:
        $ the_person = get_person_by_identifier(contact)
        if not the_person.is_employee() or not the_person.is_available:
            "Unfortunately, your delivery person is not available anymore. You decide to appoint someone new to do it."
            call screen enhanced_main_choice_display(build_menu_items([["Call in"] + mc.business.get_employee_list() ], draw_hearts_for_people = False))
            $ the_person = _return
            $ myra.event_triggers_dict["energy_drink_supplier"] = delivery_person.identifier
            $ new_delivery_person = True

    if new_delivery_person:
        "You head to your office, paging [the_person.title] to meet you there."
        $ mc.change_location(office)
        $ ceo_office.show_background()
        $ the_person.draw_person()
        the_person "Hello [the_person.mc_title]!"
        mc.name "Hi [the_person.title], I need you to do something for me."
        mc.name "The company has started sponsoring an esports team at the local gaming cafe. We have developed an exclusive energy drink to sell there."
        mc.name "I want you to be in charge of running the deliveries every week."
        the_person "Okay, I can do that. When do you want me to go?"
        mc.name "Now, let me just set up which serums I want you to deliver."
    elif mc.is_at_work():
        $ the_person.draw_person()
        $ the_serum = None

        the_person "Hey [the_person.mc_title]. I was just getting ready to take over the energy drinks for [myra.name]."
        the_person "Which one did you want me to take over?"
    else:
        "You get a message from [the_person.title]. She wants to know which serums you want delivered to the gaming cafe this week."
    "You take a look at your business' inventory. Time to decide which serum to send over to the gaming cafe for the next week."
    while not finished:
        "You quickly remind yourself, the serum must include the energy drink trait, and you need atleast 10."
        call screen serum_inventory_select_ui(mc.business.inventory)
        if not _return == "None":
            $ the_serum = _return
            if mc.business.inventory.get_serum_count(the_serum) >= 10 and myra_serum_is_acceptable_energy_drink(the_serum):
                "You set it up for [the_person.title] to take 10 [the_serum.name]s to the gaming cafe."
                "It will be distributed there for the next week to anyone who stops by."
                $ myra_set_weekly_serum(the_serum)
                $ mc.business.inventory.change_serum(the_serum, -10)
                $ finished = True
            elif mc.business.inventory.get_serum_count(the_serum) < 10:
                "Unfortunately you don't have enough of that serum to send it over."
            elif myra_serum_is_acceptable_energy_drink(the_serum):
                "Unfortunately that serum isn't acceptable to send over to the gaming cafe."
        else:
            $ the_serum = None
            "You decide not to send over any energy drinks this week."
            $ myra_set_weekly_serum(None)
            $ finished = True
    if new_delivery_person or mc.is_at_work():
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] walks away."
    else:
        "You setup the delivery of the energy drink over the phone."
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
        return mc.inventory.has_serum_with_trait(energy_drink_serum_trait)

    def myra_serum_is_acceptable_energy_drink(the_serum):   #Make this a function so that as things progress we can loosen energy drink requirements.
        if the_serum.has_trait(energy_drink_serum_trait) and the_serum.attention <= 2:
            return True
        return False

    def myra_set_weekly_serum(the_serum):
        myra.event_triggers_dict["weekly_serum"] = copy.copy(the_serum)

    def myra_unlock_energy_drink_serum():
        the_serum = find_in_list(lambda x: x.name == "Energy Drink", list_of_traits)
        the_serum.tier = 0
        the_serum.researched = True
        return

    def gaming_cafe_dose_customers():
        the_serum = copy.copy(myra_get_exclusive_energy_drink())
        for person in gaming_cafe.people:
            if the_serum not in person.serum_effects:
                if len(person.serum_effects) < person.serum_tolerance:
                    person.give_serum(copy.copy(the_serum), add_to_log = True)
        return
