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
# initial release

init 2 python:
    myrabelle_wardrobe = wardrobe_from_xml("Myrabelle_Wardrobe")
    def myrabelle_mod_initialization():
        #Start with her wardrobe and base outfit
         #Requires creation of a new wardrobe file. Alternatively, you can use one of the default ones, IE "myra_Wardrobe"
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
        myra_role = Role(role_name ="myrabelle", actions =[myra_train_focus, myra_bigger_tits_serum, myra_lewd_game_fuck], hidden = True, on_turn = gaming_cafe_owner_on_turn, on_move = None, on_day = gaming_cafe_owner_on_day)

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
            forced_sexy_opinions = [["giving handjobs", 2, False], ["showing her ass", 2, False], ["drinking cum", -1, False], ["giving blowjobs", -2, False], ["anal sex", 2, False], ["doggy style sex" ,1, False], ["being submissive", 2, False], ["getting head", 2, False]])   #random_lists.rpy for list of sexy and normal opinions

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
        myra.event_triggers_dict["lewd_game_oral"] = False
        myra.event_triggers_dict["lewd_game_fuck"] = False
        myra.event_triggers_dict["blowjob_train_start"] = False
        myra.event_triggers_dict["blowjob_train_finish"] = False
        myra.event_triggers_dict["blowjob_progress_day"] = 9999
        myra.event_triggers_dict["deepthroat_avail"] = False
        myra.event_triggers_dict["lewd_cafe_open"] = False
        myra.event_triggers_dict["foreplay_position_filter"] = myra_foreplay_position_filter
        myra.event_triggers_dict["oral_position_filter"] = myra_oral_position_filter
        myra.event_triggers_dict["vaginal_position_filter"] = myra_vaginal_position_filter
        myra.event_triggers_dict["anal_position_filter"] = myra_anal_position_filter
        myra.event_triggers_dict["unique_sex_positions"] = myra_unique_sex_positions

        myra.event_triggers_dict["story_dict"] = True
        myra.story_character_description = "An aspriring professional gamer. Owns the Gaming Cafe at the mall."
        myra.story_love_list = myra_story_love_list
        myra.story_lust_list = myra_story_lust_list
        myra.story_teamup_list = myra_story_teamup_list
        myra.story_other_list = myra_story_other_list



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

    myra_random_positions = [SB_doggy_standing, SB_reverse_cowgirl, prone_bone, cowgirl, against_wall, missionary, doggy]
    myra_random_positions_desc = {
        SB_doggy_standing.name : "The computer screen shows the male sim bend the female over the bed and penetrate her from behind.",
        SB_reverse_cowgirl.name : "On screen, the male sim lays down and the female gets on top of him, riding him reverse cowgirl.",
        prone_bone.name : "The male sim aggressively pushes the female face down on the bed.",
        cowgirl.name : "After the male sim lays down, the female gets on top and mounts him cowgirl style.",
        against_wall.name : "The male sim picks up the female and pushes her up against the wall.",
        missionary.name : "The female sim lays down and spreads her legs, and the male sim gets on top of her.",
        doggy.name : "The female sim gets on her hands on knees on the bed, and the male gets behind her."
    }

    myra_random_positions_intro = {
        SB_doggy_standing.name : "She turns and you quickly bend her over the couch. You grab her hips and line yourself up, pushing inside of her.",
        SB_reverse_cowgirl.name : "You lay down on the couch. She climbs on top of you, and you admire the amazing view and she reaches between her legs, grabs your cock, lines it up, and sinks down on your cock.",
        prone_bone.name : "You grab her and shove her down on the couch. You pin her down with your weight, and it takes a couple seconds of poking around until your cock finds her wet cunt and pushes in.",
        cowgirl.name : "You lay down and she gets on top of you. She grabs your cock and lines it up, then moans as she lets herself sink down onto your cock.",
        against_wall.name : "She yelps as you pick her up and push her against the wall. Her legs wrap around you as you push into her.",
        missionary.name : "She lays down and spreads her legs. You quickly slide up between them, kissing her on the neck as you easily slide inside of her.",
        doggy.name : "She gets on the couch on all fours and shakes her ass as you get behind her. With one hand on her hips and one hand on your cock, you quickly slide inside of her."
    }

    myra_random_positions_cum_inside_desc = {
        SB_doggy_standing.name : "You grab her hips with both hands and fuck her as fast as you can. Her ass quivers with every thrust.",
        SB_reverse_cowgirl.name : "Her quivering hole feels too good. You reach up and grab her hips with both hands, forcing her down on your cock so you can cum deep inside her.",
        prone_bone.name : "She whimpers, your weight pinning her to the couch. You thrust deep as you start to cum inside her.",
        cowgirl.name : "She leans forward, working her hips rapidly as you start to cum inside of her.",
        against_wall.name : "As you get ready to cum, her legs wrap around you, pulling you deep as you cum inside of her.",
        missionary.name : "Her fingernails scrape your back as you moan and push yourself deep, cumming inside of her.",
        doggy.name : "You grab her hips with both hands and fuck her as fast as you can. Her ass quivers with every thrust."
    }

    myra_random_positions_obj = {
        SB_doggy_standing.name : make_couch(),
        SB_reverse_cowgirl.name : make_couch(),
        prone_bone.name : make_couch(),
        cowgirl.name : make_couch(),
        against_wall.name : make_wall(),
        missionary.name : make_couch(),
        doggy.name : make_couch()
    }
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
        if gaming_cafe_is_business_hours() and alexia.is_employee() and mc.business.days_since_event("myra_rude_intro") >= 7:
            return True
        mc.business.set_event_day("myra_rude_intro", override = False)
        return False

#Actions
init 3 python:
    myra_rude_intro = Action("Meet Myra", myra_rude_intro_requirement, "myra_rude_intro_label")
    myra_gaming_cafe_opening = Action("Gameing Cafe Gran Opening", myra_gaming_cafe_opening_requirement, "myra_gaming_cafe_opening_label")

#Story Labels
label myra_rude_intro_label():
    $ the_person = myra
    $ myra.event_triggers_dict["intro_complete"] = True
    "As you are walking around downtown, you stop at a cross walk."
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
    $ mc.business.set_event_day("myra_rude_intro")
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
    alexia "This is going to be great. I think I'll start coming here to play on the weekends. The computers are way better than mine, and being around other people is great!"
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
    $ myra.set_override_schedule(None)  #Weird glitch where Myra sometimes gets assigned an override schedule somehow
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
        if gaming_cafe_is_business_hours() and mc.business.days_since_event("myra_fails_tournament") > 5 and myra_at_cafe():
            return True
        mc.business.set_event_day("myra_fails_tournament", override = False)
        return False

    def myra_train_focus_requirement(the_person):
        if myra_at_cafe() and myra_can_train_focus():
            if myra_last_focus_train_day() + 1 < day:
                return True
            else:
                return "Trained focus too recently."
        return False

    def myra_loses_sponsor_requirement(the_person):
        if the_person.love >= 60 and gaming_cafe_is_business_hours() and myra_at_cafe() and time_of_day == 3:
            return True
        return False

    def myra_gains_sponsor_requirement(the_person):
        if myra_at_cafe() and time_of_day < 3 and mc.business.has_funds(25000):
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
    $ myra.add_unique_on_room_enter_event(myra_distracted_gaming)
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
    $ mc.business.set_event_day("myra_fails_tournament")
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
    $ the_person.draw_person(position = "walking_away")
    $ the_person.change_happiness(-50)
    "You walk up to the gaming cafe. [the_person.possessive_title] is at the front door, locking up."
    mc.name "Hey [the_person.title]. Headed out early today?"
    "She turns around after she finishes locking up."
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title]. Yeah you could say that."
    the_person "I just go some bad news, so I decided to close up early tonight and hit the bar."
    the_person "Want to come with me? I could use a drinking buddy. As a warning, I'm probably going to get fucking wasted tonight."
    mc.name "I suppose I could go for a couple of drinks. I know a good place too."
    the_person "Great! Let's get out of here."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "You step out of the mall and start walking toward downtown."
    mc.name "So... if you don't want to talk about it that's fine..."
    the_person "Nah, it's fine. I got a call today from one of the team's sponsors, letting me know that they are pulling out."
    the_person "Apparently my performance in the last tournament was not up to their standards."
    mc.name "Ah. that is unfortunate."
    the_person "Yeah. They make like, my favorite energy drinks too. That's okay though, who needs them!"
    mc.name "Exactly."
    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()
    "You step inside the bar. Aftter a quick ID check, you walk with [the_person.title] up to the bar."
    "Bartender" "Hey, what'll it be for you two?"
    mc.name "I'll just have a bourbon. Neat."
    the_person "Can I get a zombie?"
    "Bartender" "Sure thing. You paying?"
    mc.name "Yeah, let me open up a tab."
    the_person "I can get my own..."
    mc.name "Non sense. You just take it easy tonight and cut loose a little."
    the_person "Thanks..."
    $ the_person.change_love(1)
    $ the_person.change_obedience(1)
    $ mc.change_locked_clarity(10)
    "You walk with [the_person.title] over to a table and sit down."
    $ the_person.draw_person(position = "sitting")
    mc.name "So, a zombie huh? I probably should have had you pegged as a rum drinker."
    the_person "Yeah, I like fruity. Passion fruit especially."
    "You chit chat with [the_person.possessive_title] about some things while you both have your drinks."
    "You think about [the_person.title]'s financial situation as you make some small talk."
    call small_talk_person(the_person, apply_energy_cost = False) from _call_small_talk_person_myra_bar_date_01
    "The drinks are empty."
    mc.name "Hey, another round?"
    the_person "Sounds great! I'm gonna hit up the lady's room real quick."
    mc.name "Hoping to find a lady?"
    the_person "Nah, but after an energy drink and some booze I've gotta piss!"
    $ clear_scene()
    "You chuckle to yourself a bit as you get up and head back to the bar. [the_person.title] is definitely a wild, outspoken person."
    "You get two more drinks. You sit back down at the table and look at them. If you are careful, you can probably sneak a serum into hers..."
    call give_serum(the_person) from _call_give_myra_serum_bar_date_01
    "After another minute, [the_person.title] returns to the table."
    $ the_person.draw_person(position = "sitting")
    the_person "Yum, this looks good."
    "She takes a big sip of her drink."
    mc.name "So, I'm curious. Let's say a local business was interested in sponsoring your eSports team."
    mc.name "How much would you be looking for, money wise?"
    "[the_person.possessive_title] rolls her eyes a bit."
    if the_person.has_large_tits():
        the_person "I don't know. Maybe it's time for me to open one of those slutty picture accounts."
        the_person "I bet a lot of nerds out there would pay for pics of a big titty blue haired girl playing games!"
        mc.name "That's not what I was asking."
        "[the_person.title] sticks her tongue out at you instead of replying."
    else:
        the_person "Probably not much, to be honest. It seems to get a sponsorship gaming as a woman these days you gotta have milkers out to HERE."
        "[the_person.possessive_title] motions her hands over her chest, suggesting incredible endowment would be required."
        the_person "Not that I have anything against big tits anyway. I'm just not what you would call blessed in the chest."
        mc.name "Do you want to be?"
        the_person "Ha! You make it sounds like it is a choice I can just make."
        menu:
            "Encourage her to get bigger tits":
                mc.name "I mean, there are multiple ways of achieving that, if it is something you want to do."
                the_person "I... I'm sorry, are you suggesting I get implants?"
                mc.name "Not necessarily. It just seemed like you were interested in the possibility?"
                the_person "Well, I'm not. Not through surgery anwyay."
                mc.name "There are ways of achieving a larger bust without surgery"
                the_person "Wow, well, that is a subject for another time... What were we talking about again?"
                $ the_person.change_love(-1)
                $ the_person.change_obedience(1)
                $ mc.change_locked_clarity(10)
                $ myra.event_triggers_dict["suggested_bigger_tits"] = True
                $ mc.business.set_event_day("myra_bigger_tits_suggestion_day")
                $ myra.add_unique_on_room_enter_event(myra_bigger_tits_intro)
            "Change the subject":
                mc.name "Hey, you're the one who brought up tits."
                the_person "Right. Well, I would never get surgery for it. What were we talking about again?"
    mc.name "Let me get straight to the point. How much money are you going to lose from the sponsorhip you lost today?"
    "[the_person.title] quietly takes a long sip from her drink before responding."
    the_person "Well... the one I lost today was for ten grand."
    mc.name "I see. What if I sponsored you? My pharmaceutical company could use a bit more press."
    the_person "Ugh, can we talk about it another time? I wanted to go out tonight to get AWAY from fucking finances."
    $ the_person.change_happiness(-2)
    "[the_person.possessive_title] takes a long sip from her drink, finishing it."
    the_person "I just wanted to go out tonight, get wasted, and who knows? Maybe wind up in someone else's bed for once."
    mc.name "You know what? That's fair. Actually, I think I can help you out with both of those."
    the_person "Is that so?"
    "[the_person.title] leans her head back and opens her mouth. The last couple drops of her drink fall onto her tongue, as she makes a show out of being out her drink being empty."
    $ mc.change_locked_clarity(10)
    the_person "I'm not sure about that [the_person.mc_title], my glass seems awfully dry..."
    mc.name "I'll be right back, let me go fix that."
    "You start to get up."
    the_person "Hey, meet me over there, I think I see some old arcade games."
    "[the_person.title] points to the back corner where some older ardcade cabinets are set up."
    mc.name "Sounds good, I'll meet you over there."
    $ clear_scene()
    "You head over to the bartender, ordering a couple more drinks for you and her."
    "It takes a couple minutes, but you find them, then head over to where she is standing."
    $ the_person.change_happiness(10)
    $ the_person.draw_person(emotion = "happy")
    the_person "Hey! It's about time. Get your ass over here!"
    "You walk up to the cabinet she is standing next to."
    the_person "That's right! I can't believe it, they have a legit Super Street Kombat 2 Turbo machine here!"
    the_person "I already got quarters from the change machine. Prepare your ass! I am coming for you!"
    mc.name "That is pretty much word for word what I'll be saying to you in a couple hours."
    "She laughs."
    the_person "Yeah right! More like, by the gods, that ass! I'm coming already!"
    mc.name "Poe-Tay-Toe, Poe-Tah-Toe"
    $ the_person.change_happiness(10)
    "It feels good to see her smile. However, as she puts in two quarters, you brace yourself for the ass whooping you are likely about to receive from [the_person.possessive_title]."
    call bar_date_arcade_round_label(the_person, skill_modifier = 50) from _myra_bar_date_round_1_fight_01
    if _return:
        "You can't believe it. You actually won."
        "It makes no sense whatsoever, but you actually did it."
        the_person "What? I... you must be cheating!"
        mc.name "Me? Never!"
        the_person "Yeah right..."
    else:
        "[the_person.possessive_title] gloats a bit. You got absolutely dismantled."
        the_person "Fuck yeah! I still got it! I user to dominate at this game."
        mc.name "I'm pretty sure you still do."
    "?????" "Hey, that game is great. Can I get the next match?"
    "You turn around. A group of three guys is behind you, and seem interested in the game."
    the_person "Sure. I want to stay on though."
    "The guys seem skeptical."
    "?????" "No offense, but we don't want to play against a girl, we want some REAL competition."
    "Oh shit."
    the_person "Oh my. Is that so? Well I'll tell you guys what. First one of you guys to win against me gets to take me home, and I'll do anything you want."
    $ mc.change_locked_clarity(20)
    "Oh shit. These guys have no idea who they are up against."
    "?????" "Damn, I'm first!"
    mc.name "Want another drink?"
    the_person "Absolutely. Alright guys, if you want a shot, you gotta front the quarters!"
    "She could probably hustle a lot of guys this way..."
    $ clear_scene()
    "You head over to the bar. You order another round for her, and just get a water for yourself. You are a little buzzed, but you don't want to get too drunk. You have a good feeling about the rest of the night."
    "You take your time, even watch a little bit from the bar. Several guys have wandered over and have started watching her play."
    "When you get her drink, you head back over. She is just finishing up her sixth win."
    "?????" "Fuck! This bitch is good!"
    the_person "Damn right!"
    $ the_person.draw_person(emotion = "happy")
    $ the_person.change_happiness(10)
    "She looks to be having a great time, dismantling every challenger that faces her."
    the_person "Ah! [the_person.mc_title]. It's your turn!"
    "She takes the drink from you. She brings it to her lips and drinks half of it in one go."
    the_person "Don't forget the rules! If you win, I'm going home with you tonight."
    "She gives you an almost imperceptible wink. You put in a quarter and the game starts up for another round."
    call bar_date_arcade_round_label(the_person, skill_modifier = -500) from _myra_bar_date_round_1_fight_02
    "There are groans from the guys watching after you win. There was no way she was trying her hardest that match!"
    "?????" "Gah, that must be her boyfriend or something. Shoulda known..."
    if the_person.is_girlfriend():
        the_person "Yeah, sorry guys, you never REALLY had a chance."
    else:
        "[the_person.possessive_title] blushes a little at the comment."
        the_person "He isn't my boyfriend... err..."
        $ the_person.change_love(1, 80)
        "It is clear from the way she said that, she wouldn't mind if it were true..."
    "[the_person.title] takes her drink and finishes it off."
    mc.name "Let me go settle up with the bartender and let's get out of here."
    the_person "Yessir!"
    "[the_person.possessive_title] is starting to slur her words a bit."
    $ mc.business.change_funds(-100)
    "You settle up with the bartender. You've run up quite the tab, but it was worth it for a fun night with [the_person.possessive_title]."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "You step outside with [the_person.title]."
    the_person "Hey... so... we are going to your place... right?"
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title] looks at you. You can tell she is a little apprehensive of your answer."
    mc.name "If you have had too much to drink and can't, that is okay..."
    "You lean forward and whisper into her ear."
    mc.name "... but otherwise I plan to take you home and fuck your brains out."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(20)
    the_person "Mmm... that sounds nice..."
    the_person "Lead on then!"
    "You start walking towards your house."
    mc.name "So, I should probably warn you about something..."
    the_person "Oh god... you have a wife?"
    mc.name "What? No... no."
    mc.name "My umm... My dad isn't around anymore. I live with my sister and my mother."
    the_person "Oh thank god. I totally thought you were about to say you have a wife!"
    "She laughs a bit longer than is normal. But she is rather intoxicated."
    the_person "I mean, you're still a loser for living with your mom, but atleast you aren't married!"
    mc.name "Hey, you better watch your mouth."
    the_person "Or what?"
    mc.name "I might have to find better uses for that mouth of yours."
    $ the_person.change_arousal(10)
    the_person "Yeah right. I don't give blowjobs on a first date, mister. Or ever."
    the_person "You can use my other holes however you want though..."
    "Hmmm, this is interesting. Does [the_person.possessive_title] have a bit of a submissive streak?"
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You step into your house, and make it unaccosted to your bedroom."
    $ the_person.draw_person(position = "back_peek")
    "When the door is closed and locked, you grab her from behind."
    $ the_person.add_situational_slut("Date", 20, "There's no reason to hold back, he's here to fuck me!")
    the_person "Oh god, you can do anything you want to me."
    mc.name "Mmm, is that so? Let's get this off you first..."
    $ the_person.strip_outfit(position = "back_peek")
    "You get her naked. You your hands all up and down her sides, her tits, her thighs..."
    $ the_person.draw_person(position = "standing_doggy")
    "You bend her over your bed. She sighs when you run your hand across her ass, groping at her cheeks."
    mc.name "You love to put up such a tough front. But it's all an act, isn't it?"
    the_person "I... I don't know what you mean..."
    "You give her ass a hard spank."
    $ the_person.change_arousal(5)
    $ mc.change_locked_clarity(30)
    the_person "Ah!"
    mc.name "You want someone to do that to you, don't you? To treat you like the fuck doll you want to be so bad."
    "*SPANK*"
    the_person "OH FUCK."
    $ the_person.change_arousal(5)
    "[the_person.possessive_title] moans when you spank her again. She has to be a closet sub, despite her normally wild attitude."
    $ the_person.discover_opinion("being submissive")
    the_person "I, I just like it when you use me... when I make you feel good..."
    "You give her anothe spank."
    $ the_person.change_arousal(5)
    the_person "AH!"
    mc.name "You liar. You don't like. You love it. I can tell. Look at how wet you are getting."
    "You run your fingers along her slit. She loves the way you are getting rough with her. You make a note to spank her more in the future."
    $ the_person.unlock_spanking()
    $ mc.change_locked_clarity(30)
    mc.name "You are such a good little slut. What hole do you want it in?"
    the_person "Umm, whichever one you want. I like it in either one..."
    mc.name "Is that so? You want it in your tight little asshole?"
    the_person "Ah, if you want... I'm okay with that."
    mc.name "Maybe I will, but for now I'm going to fuck your pussy. Are you ready?"
    the_person "Oh fuck yeah I'm ready..."
    "You quickly pull off your clothes. You grab her by the hips and get behind her."
    "[the_person.possessive_title] wiggles her ass back and forth when she feels you get close. You can feel the heat and humidity coming off her cunt as you line yourself up."
    "She sighs when she feels the tip begin pushing into her."
    the_person "Oh fuck that feels so good..."
    "You slide yourself in inch by inch. [the_person.title]'s slippery cunt feels amazing as you push yourself in."
    the_person "Fuck your cock feels so good..."
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    $ mc.change_locked_clarity(50)
    "Fully sheathed, you enjoy the heat coming off of [the_person.possessive_title]'s ass for a moment. You give her another spank."
    "*SPANK*"
    $ the_person.change_arousal(10)
    the_person "Ah! Oh fuck me [the_person.mc_title]..."
    "You pull back and start to give it to her."
    call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_sex_description_myra_post_drinks_01
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] falls onto your bed when you finish. You lay down next to her."
    the_person "That was just what I needed, god damn."
    if not the_person.is_girlfriend():
        the_person "You know what was funny? When one of the guys at the bar was like, oh damn, she's got a boyfriend. Wasn't that funny?"
        mc.name "Funny? I suppose."
        the_person "I mean, can you imagine? Us dating? Hah, I mean... I could imagine it..."
        "[the_person.possessive_title] seems to be dropping pretty big hints that she is interested in making your relationship more official."
        menu:
            "Ask her to be your girlfriend":
                mc.name "I don't know, I think that would be pretty nice."
                the_person "Ah, I mean... I think it would be nice too..."
                mc.name "Do you want to? Be my girlfriend?"
                $ the_person.change_happiness(30)
                $ the_person.change_love(5, 90)
                the_person "Ah! Fuck, I didn't think you were ever gonna ask. I'm down for it if you are!"
                if myra_alexia_teamup_scene.stage >= 2:
                    "One thing bothers you a bit about it though."
                    mc.name "What about when I come to game nights? You know, with you and [alexia.title]."
                    the_person "Oh, I mean, she is such a good friend of mine, I wouldn't be too upset if we um... kept doing that."
                $ the_person.add_role(girlfriend_role)
            "Just be friends":
                mc.name "I definitely enjoy spending time with you, especially doing stuff like this. But I'm not ready for anything serious."
                the_person "Right, that's totally what I was thinking too. That's why it was funny... right?"
                $ the_person.change_happiness(-3)
                $ the_person.change_obedience(5)
                "While her words are optimistic, you note a hint of sadness in her voice when she says that."
    else:
        the_person "God, it feels so good to be with you. That was so funny, at the bar! That guy was like, aww fuck she's got a boyfriend!"
        the_person "Damn right! And his dick is AMAZING!"
        mc.name "Poor guys thought they actually had a chance beating you at that game."
        the_person "Yeah, I suppose that was kind of mean."
    "You lay with [the_person.possessive_title] a little longer."
    mc.name "Do you want to stay over?"
    the_person "Ah, I can't. I actually have something I need to get done in the morning."
    $ the_person.draw_person()
    "[the_person.title] slowly gets up. You just watch her as she gets herself dressed again."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    the_person "I think I can see myself out. Goodnight [the_person.mc_title]."
    mc.name "Goodnight."
    $ clear_scene()
    $ the_person.clear_situational_slut("Date")
    $ myra.event_triggers_dict["bar_arcade_avail"] = True
    $ myra.event_triggers_dict["can_sponsor"] = True
    $ myra.add_unique_on_room_enter_event(myra_gains_sponsor)
    "You think about the fun night you had at the bar with [the_person.possessive_title]."
    "Her business at the gaming cafe... You feel like there are some real opportunities there, if you can convince her to accept you as a sponsor."
    "You resolve yourself to save up some funds to invest in her sports team. You make a mental note: save atleast $25000 and talk to her about it."
    call advance_time from _call_advance_myra_post_bar_day_advance_01
    return

label myra_gains_sponsor_label(the_person):
    $ the_person.draw_person()
    mc.name "Hey, we need to talk."
    the_person "Oh? What is it, [the_person.mc_title]?"
    mc.name "I want in. I want to sponsor your eSports team."
    the_person "Seriously, you don't have to do that..."
    mc.name "I have $15000 I want to invest. I'm want the opportunity to invest further in the business in the future also, as well as a small cut when your start dominating eSports tournaments."
    the_person "Fuck, that's a lot of money. Are you sure? That's more than double what I was getting from my last sponsor."
    mc.name "I am absolutely certain. Take it. Invest in your cafe. I believe in you, and I believe in your business."
    $ the_person.change_obedience(10)
    $ the_person.change_love(5, 90)
    "You hand her a check, made out of the full amount."
    the_person "Wow... okay... You are now a sponsor of the Predators eSports gaming team!"
    "[the_person.possessive_title] smiles at you. You really do feel like this is going to be a worthwile busines venture."
    the_person "I'm gonna go put this in the safe for the day, if you need anything else, come find me, okay?"
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] throws her arms around you and gives you a big hug, before letting go and walking off."
    $ clear_scene()
    $ myra.event_triggers_dict["has_been_sponsored"] = True
    $ mc.business.change_funds(-15000)
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
            if mc.business.days_since_event("energy_drink_start_research") > 7:
                return True
        mc.business.set_event_day("energy_drink_start_research", override = False)
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
    $ mc.business.set_event_day("energy_drink_start_research")
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
            elif not myra_serum_is_acceptable_energy_drink(the_serum):
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



###Sluttiness story labels
init -2 python:
    def myra_distracted_gaming_requirement(the_person):
        if the_person.sluttiness >= 20 and myra_at_cafe():
            return True
        return False

    def myra_lewd_gaming_requirement(the_person):
        if the_person.sluttiness >= 40 and myra_at_cafe() and time_of_day == 3:
            return True
        return False

    def myra_lewd_game_fuck_intro_requirement(the_person):
        if the_person.has_taboo("vaginal_sex"):
            return False
        if the_person.sluttiness >= 60 and myra_at_cafe() and time_of_day == 3:
            return True
        return False

    def myra_lewd_game_fuck_requirement(the_person):
        if not myra_lewd_game_fuck_avail():
            return False
        if myra_at_cafe() and time_of_day == 3:
            if mc.energy < 40:
                return "You are too tired"
            elif the_person.energy < 40:
                return "She looks too tired"
            return True
        return False



    def myra_adult_gaming_intro_requirement(the_person):
        if the_person.sluttiness >= 80 and mc.business.days_since_event("myra_lewd_game_fuck") >= 5:
            if myra_is_expanding_business() and myra_at_cafe():
                return True
        return False

    def myra_adult_gaming_opening_requirement():
        if myra_at_cafe() and mc.business.days_since_event("adult_cafe_opening_day") >= 14:
            return True
        return False

    def myra_harem_entry_requirement(the_person):
        return False

init 3 python:

    myra_distracted_gaming = Action("Myra Distracts Her Opponents", myra_distracted_gaming_requirement, "myra_distracted_gaming_label")
    myra_lewd_gaming = Action("Myra Plays Lewd Games", myra_lewd_gaming_requirement, "myra_lewd_gaming_label")
    myra_lewd_game_fuck_intro = Action("Myra Game Reenactment", myra_lewd_game_fuck_intro_requirement, "myra_lewd_game_fuck_intro_label")
    myra_lewd_game_fuck = Action("Lewd Game Reenactment", myra_lewd_game_fuck_requirement, "myra_lewd_game_fuck_label")
    myra_adult_gaming_intro = Action("Myra Wants Lewd Cafe", myra_adult_gaming_intro_requirement, "myra_adult_gaming_intro_label")
    myra_adult_gaming_opening = Action("Myra Opens Lewd Cafe", myra_adult_gaming_opening_requirement, "myra_adult_gaming_opening_label")
    myra_harem_entry = Action("Harem: Myra", myra_harem_entry_requirement, "myra_harem_entry_label")




label myra_distracted_gaming_label(the_person):       #20 sluttiness event. MC can suggest she should distract her opponents by dressing slutty. second chance to suggest bigger tits
    # $ myra.event_triggers_dict["suggested_bigger_tits"] = True
    "You step into the gaming cafe. [the_person.title] isn't at the desk, where she usually is."
    "Looking around, you see her playing a game with several guys. It looks like some kind of first person shooter game they are all playing together."
    $ the_person.draw_person(position = "sitting")
    "You walk over and watch from behind her."
    the_person "That's it! Suck on THIS shaft, boy!"
    "[the_person.possessive_title] kills an enemy player with a long green link gun. You can't help but chuckle at the tone of her voice."
    the_person "Ha! Kiss my ass. Or eat it! Your choice bitch!"
    "Her trash talking is top notch, with obvious sexual tones. You look at some of the guys sitting close to her."
    "They keep peeking over at her as she continues her sexual trash talk."
    the_person "God damn bitch. Are you worried? Are you scared? Don't worry baby what's the worst thing that could happen."
    "You realize that her trash talking is incredibly effective. Several of the guys she is playing against are either getting upset or clearly distracted by her."
    "The match finishes up. This is an area of her game you hadn't really considered before. Has she ever though of dressing suggestively for matches?"
    the_person "Alright, I better get back to the desk. I'll destroy your asses again some other time boys."
    "The guys are muttering to themselves, but seem to agree it is a break and time and start to disperse for now."
    $ the_person.draw_person()
    "[the_person.possessive_title] stretches, and then stands up. She turns and notices you."
    the_person "Oh hey [the_person.mc_title]. Good to see you! Something I can help you with?"
    mc.name "Not at the moment, but I was watching that last match. That was quite the show!"
    the_person "Ah, thank you 'coach'."
    mc.name "Hey, I have a question. You were doing a lot of trash talking, and I noticed that it was really distracting to some of them."
    mc.name "Have you ever thought about like, you know, dressing in a more provocative way for a match? Within rules obviously, but it might be an effective distraction."
    the_person "Wow. Well, I guess I'd prefer to have a more neutral match. I don't want to win just because the other team is drooling all over me."
    if not the_person.has_large_tits():
        the_person "But, it doesn't really matter anyway. For that strategy to be effective, you gotta have a little more... up top... if you know what I mean."
        "You take a moment to check out [the_person.possessive_title]. It might be effective if she were to level up a bit, in the chest."
        menu:
            "Encourage her to get bigger tits":
                mc.name "Have you ever though about having bigger tits?"
                the_person "Wow, straight to the point eh? I've thought about it, but honestly, surgery terrifies me. So I guess we'll never know?"
                $ myra.event_triggers_dict["suggested_bigger_tits"] = True
                $ myra.add_unique_on_room_enter_event(myra_bigger_tits_intro)
                $ mc.business.set_event_day("myra_bigger_tits_suggestion_day", override = False)
                "Hmmm, you wonder if you brought her a serum that would increase her chest size if she would agree to it."
                "You decide for now to just move the conversation along."
            "Move the conversation along":
                "You decide not to encourage any body modification for now."
    mc.name "I think if you dressed a little more provocatively, it might even help your business. You know, sex sells, and your target demographic here is a little on the nerdy side."
    $ mc.change_locked_clarity(20)
    if the_person.opinion_score_skimpy_outfits() < 2:
        $ the_person.increase_opinion_score("skimpy outfits")
        the_person "You know, you might actually be on to something. That isn't a bad idea."
    else:
        the_person "You're preaching to the choir. I don't mind showing some skin, but I have to keep it legal, you know?"
    the_person "Anyway, I need to get back to the desk. If you need anything, give me a hollar!"
    $ the_person.draw_person(position = "walking_away")
    "You watch as [the_person.possessive_title] walks away. There is a bit of a swagger in her step..."
    $ clear_scene()
    $ myra.event_triggers_dict["distracts_gamers"] = True
    $ myra.add_unique_on_room_enter_event(myra_lewd_gaming)
    call advance_time from _call_advance_myra_lewd_games_05
    return

label myra_lewd_gaming_label(the_person):           #40 sluttiness event. Catch Myra playing lewd games.
    "You step into the gaming cafe. It is pretty late in the day, and it appears to be mostly empty."
    "You look towards the main desk, but you don't see anyone. You look around a bit, eventually finding [the_person.possessive_title] in a secluded corner, playing a game."
    $ the_person.draw_person(position = "sitting")
    $ the_person.arousal = 70
    the_person "Mmm... fuck..."
    "As you walk up behind her, you notice she is making some gasping and soft moaning noises. She has a headset on and doesn't notice you approach."
    "You see on her screen, she is playing The Sims. However, it is clear from the scene that is being shown on her screen that she has installed some sexual mods for it."
    "You quickly walk up behind her now. On her screen is a blue haired sim, getting fucked from behind by another sim that looks surprisingly similar to you..."
    "You notice as you get close that [the_person.title] is touching herself and seems really into it."
    the_person "Yeah... oh..."
    "This opportunity seems too good to pass up. You decide to see if she wants a little help."
    mc.name "That looks like a fun game [the_person.title]."
    $ the_person.draw_person()
    the_person "Ah!"
    "[the_person.possessive_title] jumps up. She pushes her chair back and stands up, turning her body so it is between you and the computer screen."
    the_person "I wasn't... Ah!"
    "She pulls at her headset, taking it off. However, in her urgency, it pulls the headphone jack out of the computer."
    "Fucking noises and sounds start coming from her computer speakers."
    the_person "That's not... ugh fuck."
    "[the_person.title]'s arms drop to her sides. She gives up pretending she isn't playing a lewd version of The Sims."
    mc.name "Seriously though, that looks like a really fun game. You don't have to stop just because I'm here."
    mc.name "In fact, maybe you could use some help?"
    "Her face looks conflicted for a few seconds, but as she realizes what you are saying, she quickly accepts."
    the_person "We can't like, fuck back here, but if we could be discreet..."
    mc.name "Don't worry, I know just want to do. Sit back down."
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] sits down. You decide to get down below desk level and eat her out until she finishes."
    mc.name "Here, turn this way, so I can have better access."
    "[the_person.title] turns, and you start to pull aside the clothes in your way."
    $ the_person.strip_to_vagina(prefer_half_off = True, position = "missionary")
    "You hear as [the_person.possessive_title] plugs her headphones back in and looks at the computer screen again."
    "You bring your face up to her cunt. She is soaked, her puffy pink lips showing clear signs of arousal. This should be quick!"
    $ the_person.break_taboo("licking_pussy")
    "You stick your tongue out and run it up and down her cunt a few times. You feel her hand running through your hair."
    "You easily find her clit and start to circle your tongue around it. She gives a couple muffled moans as you get to work."
    $ the_person.change_arousal(20)
    "[the_person.title]'s hips start to move as you eat her out. Her hand is grabbing the back of your head now, encouraging you as you lick her clit."
    the_person "Oh fuck... [the_person.mc_title] I'm already so close..."
    $ the_person.change_arousal(30)
    "[the_person.possessive_title]'s groans get urgent, and her legs are twitching noticeably on either side of you."
    "You speed up your efforts, doing your best to drive her towards her orgasm. She moans and begins to writhe under your skilled tongue."
    the_person "That's it!... Oh fuck!..."
    "All at once the tension in her body is unleashed in a series of violent tremors. Her hand urgently holds your face in place as she grinds against it."
    $ the_person.have_orgasm(half_arousal = True, force_trance = True, sluttiness_increase_limit = 60)
    $ mc.change_locked_clarity(50)
    $ the_person.change_energy(-40)
    "She definitely just orgasmed, but the hand on the back of your head remains."
    "Sensing she isn't done yet, you bring up two fingers and easily slide them into her sloppy cunt."
    $ the_person.change_arousal(20)
    the_person "Oh fuck! That's so good... keep going I'm going to cum again..."
    "[the_person.possessive_title]'s voice is waivering as she pleads with you to keep going."
    "You pump your fingers inside of her as you lick her clit. You gently suck on it, and her moans are growing even more urgent."
    $ the_person.change_arousal(40)
    the_person "Yes... YES! Oh..."
    "The hand on the back of your head is starting to shake. Her legs are quivering too as she begins to orgasm again."
    $ the_person.have_orgasm(half_arousal = True, force_trance = True, sluttiness_increase_limit = 60)
    $ mc.change_locked_clarity(50)
    $ the_person.change_energy(-40)
    "Her body shudders for several seconds, and her breathing is ragged between muffled moans of pleasure."
    the_person "So good... that feels so good [the_person.mc_title]."
    "Her voice is getting husky. She almost growls at you. Her hips haven't stopped moving with you though."
    "Can you make her cum again? She seems really turned on. You decide to double down and see if you can make it happen."
    "You push your two fingers deep inside of her, turn them so that they can curl up, then find her g-spot."
    "You start to stroke her g-spot firmly with your fingers, and with your mouth you suck her clit into your mouth and start to suck on it aggressively."
    $ the_person.change_arousal(30)
    the_person "Ah! Oh fuck [the_person.mc_title] that's so good you're gonna make me cum again!"
    "Her voice is urgent and getting louder. Thankfully the place is basically empty or you are sure someone would have noticed."
    "[the_person.possessive_title]'s hips are still moving, but the movements are disjointed, and she is having trouble getting a rhythm going."
    "Her hand in your hair is just holding on as you eat her out. Her juices are running down her cunt and have started collecting on the chair below her."
    the_person "I'm cumming... I'm cumming again!"
    $ the_person.change_arousal(30)
    "[the_person.title]'s whole body spasms as she starts to cum again."
    $ the_person.have_orgasm(half_arousal = True, force_trance = True, sluttiness_increase_limit = 60)
    $ mc.change_locked_clarity(50)
    $ the_person.change_energy(-40)
    "When she finishes, her body goes limp. She is completely spent."
    $ the_person.draw_person(position="sitting")
    "You slowly stand up. Looking around, it appears that your oral session went unnoticed. Actually it appears there isn't anyone else here."
    the_person "That... holy fuck..."
    "[the_person.possessive_title] is in a post orgasm stupor. She seems like she would be receptive to some training."
    call do_training(the_person) from _call_do_training_myra_post_oral_01
    the_person "I don't think I can get up."
    mc.name "Sure you can. Here, let me help you."
    "You take [the_person.title]'s hand and help her up."
    $ the_person.draw_person()
    the_person "I need to close up now... I'm sorry, I'll have to owe you one... okay?"
    mc.name "Sounds good. I'm going to go clean up."
    the_person "Fuck, I'm gonna sleep good tonight..."
    $ clear_scene()
    "You say goodbye to [the_person.possessive_title] and leave the cafe. You quickly use the restroom to clean your face off before continuing on your way."
    $ myra.event_triggers_dict["lewd_game_oral"] = True
    $ myra.add_unique_on_room_enter_event(myra_lewd_game_fuck_intro)
    call advance_time from _call_advance_myra_lewd_games_01
    return

label myra_lewd_game_fuck_intro_label(the_person):
    $ the_person.draw_person()
    the_person "Oh hey [the_person.mc_title]!"
    "As you step into the gaming cafe, you almost walk into [the_person.possessive_title]."
    mc.name "Oh hey, I was just coming to play some games."
    the_person "Ah, sorry. Things were really slow this evening so I was just about to close up."
    "She looks at your thoughtfully."
    the_person "Actually, we could hang out for a bit if you want to?"
    the_person "I haven't forgotten that I umm... sort of owe you for the other day when you caught me playing The Sims..."
    $ mc.change_locked_clarity(20)
    "Hmmm, sounds like maybe she might be thinking about something sexy..."
    mc.name "Sure, I'll hang out for a bit."
    $ the_person.change_happiness(2)
    the_person "Great! Head to the back and let me lock up. I have a fun idea..."
    "[the_person.possessive_title] gives you a wink."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns to go lock the doors. You look at her desk, and see she has an energy drink out. If you are quick, you could slip a serum into it..."
    call give_serum(the_person) from _call_give_myra_lewd_game_fuck_01
    $ the_person.draw_person()
    the_person "Alright, let's go back here. I have a couple couches set up."
    "You follow her to the back."
    the_person "So, I like to play this game where you play as little avatars... you can hook up with other people and I installed this mod where you can even fuck each other."
    the_person "It has an option to cycle through random positions. I thought it would be fun to start it up and let it run and we could try and act out each scene as it goes."
    mc.name "Sounds hot. Let's give it a shot!"
    the_person "Okay! We should probably get comfortable..."
    $ the_person.strip_full_outfit(position = "stand3")
    "[the_person.possessive_title] gets naked, so you do the same."
    call myra_sex_roullette_session_label(the_person) from _myra_lewd_game_fuck_intro_01
    if _return:
        "Wow. Who knew that following a computer game could be so much fun. You feel great after your orgasm."
    else:
        "Damn. You just couldn't finish."
    the_person "Okay... that was hot."
    mc.name "Yeah, it was."
    the_person "We should, like... do that again sometime..."
    mc.name "Yeah?"
    the_person "How about, if you ever want to do that again, just swing by in the evening, and when I close up we can do it again?"
    mc.name "Sounds hot to me."
    the_person "Alright, well, I'm gonna go clean up and head home... can you let yourself out?"
    mc.name "Yeah, I can do that."
    the_person "Alright [the_person.mc_title], I'll see you next time."
    mc.name "See ya."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "You let yourself out of the gaming cafe after getting dressed."
    "You can now visit [the_person.possessive_title] at the gaming cafe in the evening and she will let you fuck her in random positions, even letting you finish wherever it shows on the game!"
    $ myra.event_triggers_dict["lewd_game_fuck"] = True
    $ clear_scene()
    $ mc.business.set_event_day("myra_lewd_game_fuck", override = True)
    #$ myra.add_unique_on_room_enter_event(myra_lewd_gaming)
    call advance_time from _call_advance_myra_lewd_fuck_01
    return

label myra_lewd_game_fuck_label(the_person):    #Repeatable game reenactment scene.
    mc.name "Hey, I was wondering. You up for some Sims tonight?"
    if the_person.energy < 80:
        the_person "I'm a little tired, but I'd be down to give it a shot."
    else:
        the_person "Mmm, sound fun."
    the_person "There aren't many people here. Let me close up and we can meet in the back."
    mc.name "Sounds good."
    $ clear_scene()
    "[the_person.possessive_title] walks off to clear out the store and lock up. She leaves her drink open on the counter..."
    "Maybe you could dropa a serum in really quick..."
    call give_serum(the_person) from _call_give_myra_lewd_game_fuck_02
    "It takes her a while, but eventually [the_person.title] joins you in the back of the cafe."
    $ the_person.draw_person()
    the_person "Alright. I was kind of hoping you swing by tonight. Let's get comfortable first."
    "She gives you a wink as she starts to strip down."
    $ the_person.strip_full_outfit(position = "stand3")
    "[the_person.possessive_title] gets naked, so you do the same."
    call myra_sex_roullette_session_label(the_person) from _myra_lewd_game_fuck_intro_02
    "Finished for now, you decide it is time to head out."
    mc.name "That was as amazing as always. I'm going to head out."
    the_person "Yeah... I'm going to get cleaned up. See you [the_person.mc_title]!"
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    $ myra.add_unique_on_room_enter_event(myra_adult_gaming_intro)
    "You leave the gaming cafe."
    call advance_time from _call_advance_myra_lewd_fuck_02
    return

label myra_adult_gaming_intro_label(the_person):    #80 sluttiness event. requires finishing her love story, Myra wabts to open adults only section of the cafe.
    "[the_person.title] asks MC for some feedback on an idea. Want's to know his opinion because he is sponsor and scared she will lose money."
    "She wants to open an adults only lewd section to the gaming cafe. Want's to know what MC thinks about it."
    "MC thinks it is a great idea. She says check back at a later time."
    $ mc.business.add_mandatory_crisis(myra_adult_gaming_opening)
    $ mc.business.set_event_day("adult_cafe_opening_day", override = True)
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

label myra_sex_roullette_session_label(the_person, breeding_fetish_intro = False): #In this scene, MC and Myra are acting out a randomized sex scene from the Sims. They alternate through sex positions until MC finishes.
    $ current_position = None
    $ report_log = defaultdict(int) #Holds information about the encounter: what positions were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
    $ report_log["positions_used"] = [] #This is a list, not an int.
    if mc.arousal > 100:
        $ mc.arousal = 80
    the_person "Alright, give me one second to get the game setup."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] bends over a computer desk and starts to load up the game, her ass pointing back at you."
    $ mc.change_locked_clarity(40)
    "It would be a shame to let this opportunity go by..."
    "*SMACK*"
    the_person "Ah!"
    $ the_person.change_arousal(20)
    "You give her ass a solid spank, then grope it gingerly."
    "You slide your fingers down her crack to her slit. You give it some attention as she pulls the game up."
    "When she finishes pulling up the game, you see a couple of people in a bedroom together."
    the_person "Alright, got it ready..."
    if persistent.always_ask_condom or the_person.effective_sluttiness("condomless_sex") < the_person.get_no_condom_threshold() + 50 or the_person.has_taboo("condomless_sex"):
        $ condom_threshold = the_person.get_no_condom_threshold()
        if the_person.has_breeding_fetish() or breeding_fetish_intro:
            the_person "Don't even think about wearing a condom. Hopefully the game has you finish deep inside of me..."
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(20)
            if the_person.knows_pregnant():
                the_person "Besides, I'm already pregnant anyways. Isn't it just better without those stupid things?"
            else:
                the_person "Oh god what if you knocked me up like that... that would be so hot!"
            "[the_person.possessive_title] rubs her belly absent mindedly."
        elif the_person.effective_sluttiness() < condom_threshold:
            the_person "Do you need a condom? I have some extra if you don't have any."
            the_person "And yes. You NEED to have one."
            call put_on_condom_routine(the_person) from _call_put_on_condom_routine_myra_gaming_session_01
        elif the_person.get_opinion_score("bareback sex") < 0 or the_person.effective_sluttiness("condomless_sex") < condom_threshold + 20 or the_person.has_taboo("condomless_sex"):
            the_person "You... you need to wear a condom."
            the_person "I mean, who knows how the game will have you finish... it'll be safer if the finale has you finish inside me..."
            call put_on_condom_routine(the_person) from _call_put_on_condom_routine_myra_gaming_session_02
        elif the_person.is_dominant() and the_person.get_opinion_score("bareback sex") > 0:
            the_person "Don't even think about wearing a rubber. It feels way too fucking good when your hot cock is inside me bare..."
            if the_person.get_opinion_score("creampies"):
                the_person "Besides, what if the game has you cum inside me? Wouldn't it feel good to dump a hot load inside of me?"
        else:
            if the_person.knows_pregnant():
                the_person "I'm already pregnant, but I guess if you REALLY want to you could put a condom on..."
            else:
                the_person "Do you want to put a condom on? I have one if you need one."
                the_person "It doesn't matter to me though, you can go bare if you really want to."
            menu:
                "Put on condom":
                    mc.name "I think a condom is a good idea."
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_myra_gaming_session_03

                "Fuck her raw":
                    mc.name "No arguments here."
    else:
        "[the_person.possessive_title] doesn't bring up anything about a condom, so you don't even bother."
    the_person "Alright! Here we go. Remember to tell me when you are getting ready to finish, and however they finish in game is what we'll do, okay?"
    "[the_person.title] holds up a small wireless mouse."
    the_person "All I have to do is click this and it will make them finish, with a random cumshot. Ready?"
    mc.name "Let's do it."

    while mc.arousal < 100 and mc.energy > 20 and the_person.energy > 20:
        $ current_position = get_random_from_list(myra_random_positions)
        "The sims start a new position."
        $ renpy.say(None, myra_random_positions_desc[current_position.name])
        "You look at [the_person.possessive_title]."

        $ current_position.redraw_scene(the_person)
        $ renpy.say(None, myra_random_positions_intro[current_position.name])
        $ current_position.call_scene(the_person, gaming_cafe, myra_random_positions_obj[current_position.name])
        $ the_person.change_arousal(current_position.girl_arousal * (1.0 + 0.1 * mc.sex_skills[current_position.skill_tag]))
        $ mc.change_arousal(current_position.guy_arousal * (1.0 + 0.1 * the_person.sex_skills[current_position.skill_tag]))
        $ mc.change_locked_clarity(100)
        $ the_person.change_energy(-current_position.girl_energy, add_to_log = False)
        $ mc.change_energy(-current_position.guy_energy, add_to_log = False)
        if the_person.arousal >= the_person.max_arousal:
            if report_log.get("girl orgasms", 0) == 0:
                the_person "Oh fuck, [the_person.mc_title], I'm cumming!"
            else:
                the_person "Fuck me [the_person.mc_title], I'm cumming again!"
            $ the_person.run_orgasm(force_trance = True, sluttiness_increase_limit = current_position.slut_requirement, reset_arousal = False)
            $ the_person.change_arousal(-__builtin__.max(the_person.arousal/(report_log.get("girl orgasms", 0)+2), the_person.arousal - the_person.max_arousal - 1))
            $ report_log["girl orgasms"] += 1
        if mc.arousal < 100:
            "The sims start to change positions, so you pull your cock out of [the_person.possessive_title] and get ready for the next round."
    if mc.arousal < 100 and the_person.energy > 20:    #Too tired
        "You try to follow the next round, but you are just too tired."
        mc.name "I'm sorry, I just can't keep going..."
        "[the_person.possessive_title] looks disappointed but understands."
        the_person "I wanted you to cum, but I understand, it IS getting pretty late."
        return False
    elif mc.arousal < 100:  #SHE wore out. Give the option to prone bone her.
        "[the_person.possessive_title] puts her hands out and stops you before you can continue the next position."
        the_person "I'm sorry, I completely wore out. Can we stop?"
        call prone_decision_label(the_girl = the_person, the_location = gaming_cafe, the_object = make_couch(), the_position = current_position) from _prone_sex_myra_takeover_01
        if _return:
            call fuck_person(the_person, private= True, start_position = prone_bone, start_object = make_couch(), skip_intro = True, position_locked = True, report_log = None, affair_ask_after = False, skip_condom = True) from _myra_submissive_finish_01
            "You slowly stand up, the exhausted [the_person.possessive_title] laying face down on the couch."
            return True
        else:
            mc.name "That's fine, I'm a little wore out as well."
            return False
    else:   #MC is cumming
        $ cum_target = None
        mc.name "Fuck. I'm gonna cum!"
        $ cum_target = get_random_from_list(["cum_inside", "face", "tits", "ass", "swallow"])
        if breeding_fetish_intro or (the_person.has_breeding_fetish()and renpy.random.randint(0,100) < 60): #60 chance she makes you cum inside if she has a breeding fetish.
            "Suddenly, the wireless mouse she was holding clatters across the floor."
            the_person "Ohhhh noooooo. I dropped the mouse. Guess you'd better just cum inside me then!"
            "Her voice is thick with lust and need. She obviously dropped it on purpose."
            "That's fine with you though, time to breed this slut!"
            $ cum_target = "cum_inside_breeding"
        else:
            "You hear [the_person.possessive_title] click the mouse. You look over at the screen to see how the sims finish."
        if cum_target == "cum_inside":
            "You watch as the sims keep going at it. The male sim moans and it is clear that he is finishing inside the female sim."
            if the_person.has_breeding_fetish() or breeding_fetish_intro:
                the_person "Oh fuck yes cum inside me [the_person.mc_title]!!!"
                if the_person.knows_pregnant():
                    the_person "Flood my womb with your seed! Over and over!"
                else:
                    the_person "Knock me up and make me your cow! Cum inside me over and over until we make a baby!"
            elif the_person.wants_creampie():
                the_person "Oh my god, cum inside me [the_person.mc_title]!"
            elif mc.condom:
                the_person "That's it, cum inside me [the_person.mc_title]!"
            else:
                the_person "Oh fuck... is this really happening?"
            mc.name "Oh fuck, get ready!"
            $ renpy.say(None, myra_random_positions_cum_inside_desc[current_position.name])
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
            if mc.condom:
                $ the_person.call_dialogue("cum_condom")
                "You cum. Wave after wave captured by the condom."
            else:
                $ the_person.call_dialogue("cum_vagina")
                $ the_person.cum_in_vagina()
                $ current_position.redraw_scene(the_person)
                "You fire wave after wave of cum into [the_person.possessive_title]'s unprotected cunt."
            "Neither of you move for several seconds. Eventually though, your cock starts to get too soft to stay inside her, so you slowly pull apart."
            if the_person.has_breeding_fetish() or breeding_fetish_intro:
                if current_position == missionary:
                    "As you pull off her, [the_person.title] lifts her legs up a bit, angle her hips up to keep your cum inside."
                else:
                    the_person "Hang on!..."
                    $ the_person.draw_person(position = "missionary")
                    "[the_person.possessive_title] lays down on the couch, then lifts her legs, angling her hips up to keep as much cum inside as possible."
                "You stand up and look down at your cum drink breeding stock."
                $ the_person.change_happiness(20)
                if breeding_fetish_intro:
                    return
                else:
                    the_person "Fuck, another load of your fertile cum..."
            else:
                $ the_person.draw_person()
                "You both stand up."
                if mc.condom:
                    the_person "Wow, that thing looks full... that's just impressive."
                    $ the_person.change_obedience(2)
                    $ mc.condom = False
                else:
                    "Your cum is slowly dripping down the inside of her legs."

                    if the_person.wants_creampie():
                        the_person "Wow... that was so good..."
                    else:
                        the_person "Oh my god... I can't believe I let that go so far..."
                        "She looks a little concerned, but there isn't much she can do about it now."
        elif cum_target == "cum_inside_breeding":
            "You growl at [the_person.possessive_title]."
            mc.name "Get ready slut! I'm about to fill you up like a bitch in heat!"
            the_person "Oh fuck yes cum inside me [the_person.mc_title]!!!"
            if the_person.knows_pregnant():
                the_person "Flood my womb with your seed! Over and over!"
            else:
                the_person "Knock me up and make me your cow! Cum inside me over and over until we make a baby!"
            $ renpy.say(None, myra_random_positions_cum_inside_desc[current_position.name])
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
            $ the_person.call_dialogue("cum_vagina")
            $ the_person.cum_in_vagina()
            $ current_position.redraw_scene(the_person)
            "You fire wave after wave of cum into [the_person.possessive_title]'s unprotected cunt."
            "Neither of you move for several seconds. Eventually though, your cock starts to get too soft to stay inside her, so you slowly pull apart."
            if current_position == missionary:
                "As you pull off her, [the_person.title] lifts her legs up a bit, angle her hips up to keep your cum inside."
            else:
                the_person "Hang on!..."
                $ the_person.draw_person(position = "missionary")
                "[the_person.possessive_title] lays down on the couch, then lifts her legs, angling her hips up to keep as much cum inside as possible."
            "You stand up and look down at your cum drink breeding stock."
            $ the_person.change_happiness(20)
            if breeding_fetish_intro:
                return
            else:
                the_person "Fuck, another load of your fertile cum..."

        elif cum_target == "face":
            "You watch as the female sim suddenly gets on her knees. The screen zooms in a bit as the male sim starts spraying her face down with cum."
            if the_person.opinion_score_cum_facials() < 0:
                the_person "Oh god... I didn't think it would go this way..."
            elif the_person.opinion_score_cum_facials() > 0:
                the_person "Oh fuck that looks hot!"
            else:
                the_person "Oh fuck on my face? Okay..."
            $ the_person.draw_person(position = "blowjob")
            "[the_person.possessive_title] gets on her knees as you stand up."
            if mc.condom:
                "She quickly pulls your condom off and starts to stroke you, pointing it at her face."
                $ mc.condom = False
            else:
                "She grabs your cock and starts to stroke it eagerly, pointing it at her face."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
            if the_person.opinion_score_cum_facials() > 0:
                "[the_person.title] sticks out her tongue for you and holds still, eager to take your hot load."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shuddering moan as you cum, pumping your sperm onto [the_person.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            else:
                "[the_person.title] closes her eyes and waits patiently for you to cum."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shuddering moan as you cum, pumping your sperm onto [the_person.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."

            "You take a deep breath to steady yourself once you've finished cumming. [the_person.title] looks up at you from her knees, face covered in your semen."
            $ the_person.call_dialogue("cum_face")
            $ the_person.draw_person()
            "You both stand up."
        elif cum_target == "tits":
            "You watch on the screen as the male pulls out of the female. She lays down on the bed on her back and he sprays down her tits with cum."
            if the_person.opinion_score_being_covered_in_cum() < 0:
                the_person "Ugh. On my tits? Typical..."
            elif the_person.opinion_score_being_covered_in_cum() > 0:
                the_person "Oh fuck, cover my tits in your hot cum [the_person.mc_title]!"
            else:
                the_person "Mmm, time to cum on my tits, [the_person.mc_title]!"
            if current_position == missionary:
                "You pull out of [the_person.title] and move up the couch. She grabs your cock and starts to stroke you."
            else:
                $ the_person.draw_person(position = "missionary")
                "[the_person.title] throws herself down on the couch on her back and looks up at you."
                "You quickly get on top of her waist and she strokes you eagerly."
            if mc.condom:
                "[the_person.possessive_title] pulls your condom off just in time."
                $ mc.condom = False
            $ the_person.cum_on_tits()
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
            $ the_person.draw_person(position = "missionary")
            "You watch as your cum coats [the_person.title]'s tits with spurt after spurt of cum."
            if the_person.opinion_score_being_covered_in_cum() < 0:
                the_person "Ugh. It feels so sticky..."
            elif the_person.opinion_score_being_covered_in_cum() > 0:
                the_person "God, your seed feels so fucking hot..."
                "[the_person.title] licks her fingers clean."
            else:
                the_person "Mmm, that it [the_person.mc_title], let it all out..."

            "After several seconds, you look down at [the_person.possessive_title]. Her tits are coated in your spunk."
            $ the_person.draw_person()
            "You both stand up."
        elif cum_target == "ass":
            "You watch on the screen as the male pulls out of the female. The screen zooms in as he bends her over the bed and starts to cum all over her ass"
            if the_person.opinion_score_being_covered_in_cum() < 0:
                the_person "Ugh. On my ass? Fine..."
            elif the_person.opinion_score_being_covered_in_cum() > 0:
                the_person "Oh fuck, cover my ass in your hot cum [the_person.mc_title]!"
            else:
                the_person "Mmm, time to cum on my ass, [the_person.mc_title]!"
            if current_position == SB_doggy_standing or current_position == doggy:
                "You pull out of [the_person.title]."
            else:
                $ the_person.draw_person(position = "standing_doggy")
                "[the_person.title] bends over the couch and you get behind her."

            if mc.condom:
                "You pull your condom off and start to stroke yourself."
                $ mc.condom = False
            "[the_person.possessive_title] wiggles her ass back at you as start to cum."
            $ the_person.cum_on_ass()
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
            $ the_person.draw_person(position = "standing_doggy")
            "You watch as your cum coats [the_person.title]'s ass with spurt after spurt of cum."
            if the_person.opinion_score_being_covered_in_cum() < 0:
                the_person "Ugh. It feels so sticky..."
            elif the_person.opinion_score_being_covered_in_cum() > 0:
                the_person "God, your seed feels so fucking hot..."
            else:
                the_person "Mmm, that it [the_person.mc_title], let it all out..."

            "After several seconds, you look down at [the_person.possessive_title]. Her ass is coated in your spunk."
            $ the_person.draw_person()
            "You both stand up."
        elif cum_target == "swallow":
            "You look at the screen. The female sim gets on her knees and takes the male in her mouth as he cums. The virtual character makes loud slurping and gulping noises as she swallows it down."
            if the_person.opinion_score_drinking_cum() < 0:
                the_person "Shit, why did I say I would do this!..."
            elif the_person.opinion_score_drinking_cum() > 0:
                the_person "Oh fuck, I'm ready for it, let me drink your cum!"
            else:
                the_person "Ah, I guess it is time to swallow it for you [the_person.mc_title]..."
            $ the_person.draw_person(position = "blowjob")
            "[the_person.possessive_title] gets on her knees as you stand up."
            if mc.condom:
                "She quickly pulls your condom off. She opens her mouth and takes the tip while stroking the shaft with her hand."
                $ mc.condom = False
            else:
                "She opens her mouth and takes the tip, while she strokes your shaft with her hand rapidly..."
            "After a couple strokes, you explode, dumping your cum into [the_person.possessive_title] mouth. Some of it drips down her chin."
            $ the_person.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
            $ the_person.draw_person(position = "blowjob")
            if the_person.opinion_score_drinking_cum() < 0:
                "When you finish, [the_person.possessive_title] looks up at you. Her face isn't pleasant."
                mc.name "Come on now. You saw the screen. Swallow like a good girl."
                $ the_person.change_obedience(5)
                "She gives you a middle finger, but eventually swallows, the gags a little and makes a face."
                the_person "Fuck, I hate doing that. You're a lucky son of a bitch, you know that?"
            elif the_person.opinion_score_drinking_cum() > 0:
                "As you cum [the_person.possessive_title] eagerly drinks every drop."
                mc.name "Damn. What a good girl, swallowing my cum like that."
                $ the_person.change_obedience(5)
                the_person "Mmm, it helps that you taste so good sir..."
            else:
                "You look down when you are finished. [the_person.possessive_title] still has the tip in her mouth."
                mc.name "Good girl. Now swallow."
                $ the_person.change_obedience(5)
                "[the_person.title] grimaces a bit, but dutifully swallows your cum."
                the_person "Mmm, that wasn't so bad."


            "You take a deep breath to steady yourself. [the_person.title] looks up at you from her knees, a bit of your cum still on her chin."
            $ the_person.draw_person()
            "You both stand up."
    $ mc.condom = False
    $ del cum_target
    $ del current_position
    return True

#End game sexual events
init -2 python:
    def myra_breeding_on_stream_requirement():
        if myra.has_breeding_fetish() and myra.has_exhibition_fetish() and myra.is_highly_fertile():    #Pretty stringent requirements
            if time_of_day == 3:
                return True
        return False


label myra_breeding_on_stream_label():    #Requires breeding and exhibition fetish
    $ the_person = myra
    $ the_person.arousal = 40
    "You feel your phone vibrate. It's a message from [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey! Can you come to the cafe? I need your help with something."
    mc.name "What help do you need?"
    the_person "Some of my streaming fans have been requesting something. I need your help with it though."
    the_person "As a hint, I am super fertile right now ;)"
    mc.name "I'll be right there."
    $ mc.end_text_convo()
    "Sounds like [the_person.title] wants to get bred on stream... seems to good to pass up!"
    "You head over to the game cafe. Then make your way to the adults only section."
    $ mc.change_location(gaming_cafe)
    $ mc.location.show_background()
    $ the_person.apply_outfit(special_fetish_nude_outfit)
    "When you get there, you take a quick look around, then spot [the_person.possessive_title]. It appears she has already started her stream..."
    $ the_person.draw_person(position = "walking_away")
    "She is laying on a couch, facing a screen while she holds a controller. She is naked, and her ass is ripe and ready to be fucked."
    "To one side, you see a computer screen where she has her streaming setup. There is a side angle view of her, showing off her curves on the couch."
    the_person "Fuck yeah! Got you bitch!"
    "As you start walking towards her, she manages to score a kill in the shooter she is playing. You know exactly what part you play in this stream."
    "You have no doubt she really is fertile right now. You are about to knock her up live on stream."
    "You take your clothes off, then slowly approach her from behind."
    "You run your hand up her legs as you climb onto the couch. She peaks at the screen and sees that it's you, but otherwise doesn't let herself react at all."
    "Her legs part just the slightest you run you hand up between them. You can feel the heat and humidity coming off her cunt when you hand gets to it."
    "[the_person.title] is turned on and ready to fuck. You give her ass a little spank then climb onto her."
    "The only indication she gives of what is about to happen, she says on the headset to her teammates."
    if the_person.is_girlfriend():
        the_person "Hey, sorry if I seem distracted for a bit. My boyfriend is her and he is going to knock me up now. No no, I'm going to keep playing."
    else:
        the_person "Hey, sorry my sperm donor is here and he's about to knock me up, sorry if I seem a bit distracted. No no, I'm going to keep playing."



    return





# Obedience related events

init -2 python:
    def myra_bigger_tits_intro_requirement(the_person):
        if the_person.obedience >= 120 and myra_at_cafe():
            if mc.business.days_since_event("myra_bigger_tits_suggestion_day") > 7:
                return True
        return False

    def myra_bigger_tits_serum_requirement(the_person):
        if myra_wants_bigger_tits() and not myra.has_large_tits():
            if myra_at_cafe():
                if mc.inventory.has_serum_with_trait(breast_enhancement):
                    return True
                else:
                    return "Requires serum with Breast Enhancement Trait"
        return False

    def myra_bigger_tits_final_requirement(the_person):
        if myra.has_large_tits() and myra_at_cafe():
            return True
        return False

    def myra_blowjob_training_intro_requirement(the_person):
        if the_person.obedience >= 140:
            if myra_at_cafe():
                return True
        return False

    def myra_blowjob_training_progress_requirement(the_person):
        if myra_at_cafe() and mc.business.days_since_event("myra_bj_train") >= 7 and the_person.obedience >= 160:
            return True
        mc.business.set_event_day("myra_bj_train", override = False)
        return False

    def myra_blowjob_training_final_requirement(the_person):
        if myra_at_cafe() and mc.business.days_since_event("myra_bj_train")  >= 7 and the_person.obedience >= 180:
            return True
        mc.business.set_event_day("myra_bj_train", override = False)
        return False

init 3 python:
    myra_bigger_tits_intro = Action("Myra Wants Bigger Tits", myra_bigger_tits_intro_requirement, "myra_bigger_tits_intro_label")
    myra_bigger_tits_serum = Action("Give Serum for Bigger Tits", myra_bigger_tits_serum_requirement, "myra_bigger_tits_serum_label")
    myra_bigger_tits_final = Action("Myra Gets Large Tits", myra_bigger_tits_final_requirement, "myra_bigger_tits_final_label")
    myra_blowjob_training_intro = Action("Myra Needs Help", myra_blowjob_training_intro_requirement, "myra_blowjob_training_intro_label")
    myra_blowjob_training_progress = Action("Develop Myra Orally", myra_blowjob_training_progress_requirement, "myra_blowjob_training_progress_label")
    myra_blowjob_training_final = Action("Develop Myra Orally", myra_blowjob_training_final_requirement, "myra_blowjob_training_final_label")

label myra_bigger_tits_intro_label(the_person):        #120 obedience event. If MC suggested bigger tits in love story, myra is interested now.
    $ the_person.draw_person()
    "You step into the gaming cafe. As you walk in, [the_person.possessive_title] notices you and walks over."
    the_person "Hey, do you have a second? I wanted to talk to you about something..."
    mc.name "Absolutely. What is on your mind [the_person.title]?"
    the_person "The other day, you said something that kind of got some gears turning in my head..."
    the_person "I've never been one to stress about looks, especially things that are outside of my control but..."
    the_person "Do you really think I should get bigger tits?"
    $ mc.change_locked_clarity(30)
    mc.name "That is a pretty loaded question."
    the_person "I know, and honestly the prospect of getting surgery terrifies me but, I don't know, you seem like a good guy, and I thought you could give me an honest opinion."
    mc.name "Well, I think you need to do what is right for you, first of all. But, I do have something that I think you might be interested in."
    the_person "Oh?"
    mc.name "As you know, I run a pharmaceutical company, and we are actually running tests on a drug that naturally increases breast size."
    the_person "What? Like, without surgery?"
    mc.name "That is correct."
    the_person "Do you need anyone to help test it?"
    mc.name "Actually yes. Would you be interested?"
    the_person "Yeah. I think I am. I want to know what it is like... you know?"
    mc.name "Well, I can't promise anything, but I'll make sure to keep you in mind if we do any trials soon."
    the_person "Ah, thank you [the_person.title]! I'd better get back to the desk."
    $ the_person.change_obedience(2)
    $ the_person.change_happiness(2)
    $ clear_scene()
    "[the_person.title] will now accept breast enhancement serums."
    $ myra.event_triggers_dict["wants_bigger_tits"] = True  #This will open up the option on her role
    $ myra.add_unique_on_talk_event(myra_bigger_tits_final)
    return

label myra_bigger_tits_serum_label(the_person):       #This option becomes available if Myra wants bigger tits.
    mc.name "Hey, I have a breast enhancement serum for you to try. Still interested?"
    the_person "I am, yes!"
    call give_serum(the_person) from _call_give_myra_bigger_tits_serum_01
    if _return:
        "You hand her the serum, and she quickly drinks it down."
        mc.name "It might be a few days until you see the effects."
        the_person "Okay... I'll let you know how they work!"
    else:
        mc.name "Actually, I think I left them at the shop."
        "[the_person.title] looks disappointed, but understands."
    return

label myra_bigger_tits_final_label(the_person):       #If her tits are bigger, she thanks MC.
    "As you step into the gaming cafe, [the_person.possessive_title] spots you. She quickly walks up to you and grabs your hand."
    $ the_person.draw_person(position = "walking_away")
    the_person "Come on! I need to show you something!"
    "As you follow after her, you feel like you notice a little more... jiggle? In her step?"
    "She leads you to a stock room in the back. After practically shoving you in, she closes the door and locks it."
    $ the_person.draw_person()
    the_person "Sorry, I just had to do this. Check these out!"
    $ the_person.strip_to_tits(position = "stand3")
    $ mc.change_locked_clarity(30)
    if the_person.sluttiness >= 40 or the_person.love > 60:
        "[the_person.possessive_title] quicky strips off her top, revealing a generous set of tits."
        the_person "They're amazing! And they feel completely natural! Come, feel this..."
        "She grabs your hand and drags it to her chest, forcing you to feel her up."
        the_person "See? And..."
        $ the_person.change_arousal(20)
        the_person "And... they're so sensitive too..."
        $ the_person.increase_opinion_score("showing her tits")
        $ mc.change_locked_clarity(30)
        "You spend several seconds feeling up her new and improved rack. You admit, they are impressive."
        $ mc.change_arousal(20)
        "You can feel yourself getting excited as she starts to whimper from your touch."
        the_person "They are awesome, right?"
        "[the_person.possessive_title] looks down and notices your erection."
        the_person "Hey... you know... I've never had big enough tits to like..."
        "She looks at you for a moment."
        the_person "Want to fuck them?"
        mc.name "Yes. Yes I do."
        $ mc.change_locked_clarity(30)
        the_person "Hell yeah let's do it. I bet it feels amazing..."
        $ the_person.draw_person(position = "blowjob")
        "As [the_person.possessive_title] gets down on her knees, you whip out your cock. She slides over to you."
        the_person "I've like, never done this so... you might have to help me a bit..."
        mc.name "I'm sure you'll do great."
        "With your cock in her hand, she slides the tip of your cock into her cleavage. Your erection quietly disappears into her ample busom."
        "Her soft tit flesh feels great wrapped around you."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(30)
        the_person "Wow, it feels so hot... God this is naughty... I love it!"
        "[the_person.title] starts to move her chest up and down, stroking your cock."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_myra_tits_reveal_1
        "When you finish, [the_person.possessive_title] stands up."
        $ the_person.draw_person()
        the_person "Wow... We'll have to do that again sometime."
        mc.name "Yes, anytime you need a cock between your tits, hit me up."
        the_person "Ha! Okay 'coach'. I'll keep that in mind! I'd better get cleaned up and get back to work."
    else:
        "[the_person.title] quickly pulls off her top, giving you an amazing view of her tits."
        mc.name "Damn. They look amazing."
        the_person "Yeah... they feel so sensitive too..."
        mc.name "Is that so?"
        "You step close to her, she takes a half step back."
        the_person "That's... what are you doing?"
        mc.name "I want to feel them for myself. You don't mind, right?"
        the_person "I suppose not... You did give me the drugs to do this I guess..."
        "You step forward and again. You reach forward with both hands and take hold of her twin peaks."
        "They feel hot and soft to the touch. She whimpers a bit as you feel her up."
        $ the_person.change_arousal(20)
        the_person "They are amazing. You should proud to show these girls off."
        $ the_person.increase_opinion_score("showing her tits")
        $ mc.change_locked_clarity(30)
        the_person "Mmm... yeah I think so..."
        "You pinch her nipples, then roll them between your thumb and fingers."
        $ the_person.change_arousal(20)
        the_person "Oh fuck they are so sensitive too..."
        $ mc.change_arousal(20)
        mc.name "Yeah you like it when I touch you like this don't you."
        the_person "Mmm... I do..."
        "You spend several seconds with [the_person.possessive_title], just enjoying the weight and softness of her improved rack."
        $ mc.change_arousal(20)
        mc.name "Damn. Now I'm all turned on. Why don't you get on your knees, let's see how they feel wrapped around my cock."
        "[the_person.title] looks at you, conflicted. This is a little outside her comfort zone."
        the_person "I... I don't know..."
        mc.name "Come on now. I made this possible, don't I deserve a little reward? I gave you the serums, free of charge."
        the_person "That's true."
        "She thinks about it for a few more moments."
        the_person "Fuck it. I was wondering what it would be like to do this anyway. Might as well be with you!"
        $ the_person.draw_person(position = "blowjob")
        "As [the_person.possessive_title] gets down on her knees, you whip out your cock. She slides over to you."
        the_person "I've like, never done this so... you might have to help me a bit..."
        mc.name "I'm sure you'll do great."
        "With your cock in her hand, she slides the tip of your cock into her cleavage. Your erection quietly disappears into her ample busom."
        "Her soft tit flesh feels great wrapped around you."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(30)
        the_person "Wow, it feels so hot... God this is naughty... I love it!"
        "[the_person.title] starts to move her chest up and down, stroking your cock."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_myra_tits_reveal_2
        "When you finish, [the_person.possessive_title] stands up."
        $ the_person.draw_person()
        mc.name "Damn, that was amazing. We'll have to do this again sometime."
        the_person "That was surprisingly pleasant. I wouldn't mind doing it again!"
    $ the_person.increase_opinion_score("giving tit fucks")
    $ the_person.apply_planned_outfit()
    $ myra.event_triggers_dict["wants_bigger_tits"] = False
    $ clear_scene()
    "You quietly exit the stock room. "
    return

label myra_blowjob_training_intro_label(the_person):      #Myra ask for blowjob training after sessions with Alexia. Requires 140 obedience
    $ the_person.draw_person()
    if myra.event_triggers_dict.get("blowjob_train_start", False):  #This has already run once.
        return
    $ myra.event_triggers_dict["blowjob_train_start"] = True
    "When you step into the gaming cafe, you see [the_person.title], at her usual spot at the main desk."
    "She spots you when you walk in. She smiles so you decide to go say hello."
    mc.name "Good day [the_person.title]"
    the_person "Hey."
    "[the_person.possessive_title] looks around, then says to you in a hushed voice."
    the_person "So... how'd you enjoy that other night with [alexia.name]? That was pretty wild, huh?"
    mc.name "Yeah, but definitely in a good way."
    the_person "Yeah, you WOULD say that..."
    "[the_person.title] sticks her tongue into the side of her cheek, and briefly mimics a blowjob motion."
    $ mc.change_locked_clarity(10)
    mc.name "Oh come on, don't pretend like you didn't have a good time too."
    the_person "The gaming nights are fun. Hanging with [alexia.name], hanging out with you..."
    the_person "That doesn't mean I like giving blowjobs though."
    mc.name "That's okay. I'll just throw the game for you next time. [alexia.title] gives way better head anyway."
    $ the_person.draw_person(emotion = "angry")
    $ the_person.change_happiness(-5)
    the_person "What? Are you fucking kidding me? You get head from [alexia.name] often then?"
    mc.name "What? I mean, it's completely true. Your blowjobs need work."
    "It seems that comparing her to [alexia.possessive_title] has got her feeling competitive. You decide to push the issue."
    the_person "Yeah right. And let me guess, you just happen to be the man to teach me."
    mc.name "I mean, I am your coach. I guess it just depends. Is it a skill you WANT to be better at?"
    mc.name "You might be able to beat [alexia.title] at games, but in the oral skills department, she has you outclassed, hands down."
    the_person "Yeah right. Fuck off, I've got stuff to do."
    mc.name "Alright. I'm just gonna go play something for a bit."
    $ clear_scene()
    "You step away from the desk. You find a computer and sit down."
    "You aren't sure if that will work or not, but atleast it left her thinking about it. Maybe she'll come around to it."
    "You hop on a computer and load up Guild Quest 2. You just play some overland stuff for a bit, your mind thinking about [the_person.title]."
    "After a couple hours, you are just getting ready to get up..."
    $ the_person.draw_person(emotion = "sad")
    the_person "Hey..."
    mc.name "Hey [the_person.title]."
    the_person "Look, I'm sorry I got pissed earlier. Obviously I know that you fool around with [alexia.name]."
    the_person "She talks about you way too much for things between you two to be just friendly."
    mc.name "Oh... she talks about me a lot?"
    the_person "I... look, I'm not here to talk about her, okay?"
    mc.name "Ok... what are you here to talk about?"
    the_person "I was thinking about it a lot. I DO want to get better, I had honestly just written off blowjob as something OTHER girls do..."
    the_person "But the other night, the atmosphere was just... different? I WANTED to make you feel good. But I felt like I had no idea what I was doing..."
    mc.name "Ah, so you really DO need a coach! Don't worry [the_person.title]. I'm here to help."
    the_person "That's... why did I not see that reaction coming. You are so predictable."
    mc.name "Don't worry, you'll have an up close look at me coming soon."
    the_person "You are such a dumbass."
    mc.name "Alright, let's go find somewhere private."
    the_person "What, like... right now?"
    mc.name "Of course! There's no time like the present."
    the_person "Ummm, maybe we could start like some other..."
    mc.name "Non sense! I'm your coach, I know what's best. Let's go."
    $ the_person.change_obedience(5)
    $ the_person.draw_person(position = "stand3")
    "You stand up."
    the_person "Umm, I guess there is a stock room where I keep spare computer parts."
    mc.name "Lead the way."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns away and you follow her. She goes into a door way, down a small hall, and into a small parts room."
    $ the_person.draw_person()
    the_person "Fuck, I can't believe I'm doing this."
    mc.name "Don't worry. I'll help you develop skills that will be useful the rest of your life."
    "[the_person.title] rolls her eyes."
    the_person "So... what now coach?"
    mc.name "Well, first, you need to drop the smartass attitude."
    the_person "What? Fuck off, I'm just..."
    mc.name "Let's be honest with each other. We both know WHY you are doing this. You are competitive by nature, and you can't stand the thought that [alexia.title] might be better than you."
    mc.name "But the most important part about blowjobs has nothing to do with technique. It's all about attitude. Guys can tell when your forcing it, and it's a big turn-off."
    "For a moment, [the_person.possessive_title] seems shocked at your forceful words. For a second, it seems she is about to tell you to fuck off again, but then she relaxes."
    the_person "I... I DO want to be better..."
    mc.name "That's great, but to get good at blowjobs, you have to WANT to give them. So far, all I can tell is that you are actively avoiding it."
    mc.name "Here's what you need to do. Get on your knees. Take out my cock. And lick it, like you WANT to. You WANT to make it good. You WANT to do anything you can to make me feel good."
    $ the_person.change_obedience(20)
    the_person "Okay..."
    $ the_person.draw_person(position = "blowjob")
    $ mc.change_locked_clarity(30)
    "Finally, [the_person.possessive_title] gets on her knees in front of you. She undoes your pants and slowly pulls them down with your underwear."
    "She looks a little scared as she looks at your full size."
    the_person "I... I'll never be able to... it's too big!"
    mc.name "You let me worry about working up to handling the whole thing. For now, just lick it."
    the_person "Okay..."
    "You can feel [the_person.title]'s hot breath on your groin as she brings her face right up to it. She sticks out her tongue and runs it up the side a few times."
    mc.name "That's it. Now be honest. Before you met me, how many blowjobs have you given before?"
    the_person "I... don't see how that's relevant to my training..."
    mc.name "Just answer. I'll decide what's relevant."
    "[the_person.possessive_title] sighs."
    the_person "Two."
    mc.name "Really? Haven't had serious boyfriends before?"
    the_person "I have, I just... I was with a guy once who kept begging for blowjobs all the time. I finally gave in and did it once, but..."
    the_person "He... wasn't very gentle. He grabbed me by the hair and just kept..."
    the_person "Honestly, at one point, I thought I was doing to die. I was gagging so hard."
    mc.name "Ahh, I understand now. Don't worry [the_person.title]. We may work up to that point, but I won't do anything like that to you yet."
    the_person "Yeah?"
    "[the_person.possessive_title] takes another long couple of licks up and down your shaft."
    $ mc.change_locked_clarity(30)
    mc.name "Alright, we're gonna take this slow, okay? First, lick all around the tip, then put just the tip in your mouth."
    the_person "Hmm... okay..."
    "[the_person.title]'s hot tongue swirls around your tip a few times. "
    "Finally, her lips open and you feel your tip enter her mouth. She quietly sucks on the tip for several seconds."
    $ mc.change_arousal(10)
    mc.name "Mmm, that's it. That feels really good."
    $ the_person.change_happiness(5)
    "[the_person.possessive_title] looks up at you, and your eyes meet. You can see the beginning of something new. Something passionate. She is ready to learn to service you."
    "And more importantly, she WANTS to."
    $ the_person.break_taboo("sucking_cock")
    "[the_person.title] maintains her eye contact as she starts to bob her head a bit, servicing the tip of your cock."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(50)
    mc.name "Why don't you touch yourself a little too."
    "[the_person.title] pops off your dick."
    the_person "What? You want me to masturbate?"
    mc.name "It'll help. Making yourself feel good will help get you in the mood. Plus little moans and gasps are fucking hot."
    $ the_person.draw_person(position = "kneeling1")
    the_person "I guess that makes sense..."
    "[the_person.possessive_title] reaches down and starts to touch herself. You let her go for several seconds."
    mc.name "See? Feels good, right?"
    the_person "Mmm... yeah..."
    mc.name "When you are feeling it, keep going. It'll make it easier."
    the_person "Fuck... mmm.... okay..."
    "[the_person.title] touches herself for several more seconds."
    $ the_person.draw_person(position = "blowjob")
    $ mc.change_locked_clarity(50)
    "When she turns back to your cock, she opens her mouth and starts to suck on it, more eagerly this time. This is shaping up to be a good blowjob session now."
    call fuck_person(the_person, start_position = blowjob, skip_intro = True, position_locked = True) from _call_sex_description_myra_bj_train_01
    mc.name "That's enough for now."
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        "That went way better than you had expected. It seems that you may have flipped a switch in [the_person.possessive_title]'s brain."
    else:
        "Even though you didn't finish, her eagerness shows that she is ready and willing to learn."
        "It seems you may have flipped a switch in [the_person.possessive_title]'s brain."
    $ myra.increase_sex_skill("Oral")
    $ myra.increase_opinion_score("giving blowjobs")
    $ mc.business.set_event_day("myra_bj_train", override = True)
    $ myra.add_unique_on_room_enter_event(myra_blowjob_training_progress)
    the_person "That actually was a lot more fun than I thought it would be."
    mc.name "Yes. Your enthusiasm helped a lot. I want you to practice your technique for a bit."
    the_person "My... technique?"
    mc.name "Yeah. Another good idea would be to watch some videos. And by that, I mean porn."
    the_person "Right... for science."
    mc.name "Exactly."
    $ the_person.draw_person()
    "[the_person.possessive_title] stands up."
    the_person "I'll umm... keep that in mind..."
    mc.name "Of course, you're always welcome to practice on me also."
    "[the_person.title] rolls her eyes."
    the_person "Ah yes, the white knight offers graciously to let me suck his dick whenever I want. How gallant."
    the_person "I'm going to get cleaned up, but I will keep your offer in mind..."
    mc.name "Alright, I'll see you later."
    $ clear_scene()
    $ the_person.apply_outfit(the_person.planned_outfit)
    "You step out of the stock room. The gaming nights your are having with [the_person.possessive_title] and [alexia.title] are paying off."
    "A week ago, [the_person.title] would never even consider sucking you off, but now she seems interested, if only to show up her friend."
    "You make a mental note to check back up with her in a week or so and see how her technique is progressing."
    "She might also be more willing to further her blowjob skills if you increase her obedience as well..."
    call advance_time from _call_advance_myra_bj_train_01_time_
    return

label myra_blowjob_training_progress_label(the_person):
    "Part two of [the_person.title]'s blowjob training."
    "MC works with her on going deep. Let's her set the pace for the most part. She gags a lot but struggles though it."
    "At the end, suggest that she practice deepthroating. Opens up the deepthroat position via filters."
    "Setup final scene to be available in a week."
    $ myra.increase_sex_skill("Oral")
    $ myra.increase_opinion_score("giving blowjobs")
    $ myra.event_triggers_dict["deepthroat_avail"] = True
    $ mc.business.set_event_day("myra_bj_train", override = True)
    $ myra.add_unique_on_room_enter_event(myra_blowjob_training_final)
    return  #160 Obedience

label myra_blowjob_training_final_label(the_person):
    "After training her throat for a week, [the_person.title] is ready for final training."
    "In this session, you teach her to relax her throat and to be submissive."
    "She struggles for a bit, but finally manages to let go and you face fuck her."
    "At the end, she asks MC to help Alexia win gaming night this week, she wants to show off her face fucking skill to her friend."
    $ myra.event_triggers_dict["blowjob_train_finish"] = True

    return  #180 Obedience

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

    def myra_plays_esports():
        return myra.event_triggers_dict.get("knows_plays_esports", False)

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

    def myra_distracts_gamers():
        return myra.event_triggers_dict.get("distracts_gamers", False)

    def myra_caught_masturbating():
        return myra.event_triggers_dict.get("lewd_game_oral", False)

    def myra_lewd_game_fuck_avail():
        return myra.event_triggers_dict.get("lewd_game_fuck", False)

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
        if the_serum.has_trait(energy_drink_serum_trait) and the_serum.attention <= 3:
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
                    person.give_serum(copy.copy(the_serum), add_to_log = False)
        return

    def myra_foreplay_position_filter(foreplay_positions):
        return True

    def myra_oral_position_filter(oral_positions):
        if myra_finish_blowjob_training():
            return True
        elif myra_started_blowjob_training() and myra_deepthroat_avail():
            filter_out = [skull_fuck]
            if oral_positions[1] in filter_out:
                return False
            else:
                return True
        elif myra_started_blowjob_training():
            filter_out = [skull_fuck, deepthroat]
            if oral_positions[1] in filter_out:
                return False
            else:
                return True
        else:
            filter_out = [skull_fuck, deepthroat, blowjob, cowgirl_blowjob]
            if oral_positions[1] in filter_out:
                return False
            else:
                return True
        return True

    def myra_vaginal_position_filter(vaginal_positions):
        return True

    def myra_anal_position_filter(anal_positions):
        return True


    def myra_unique_sex_positions(person, prohibit_tags = []):
        positions = []

        return positions
