#Myra and Alexia teamup scene! Myra invites Alexia over for a game night.
#Happens on Friday nights because that's the only night that makes actual logical sense to have an all night gaming session
#Unfortunately this conflicts with dates so probably lots of QQ
#Oh well. Progression is similar to Myra's focus practice.
#Mc shows up to game night, but girls are playing a two player only game.
#Girls wager that winner gets a back rub. MC agrees. Myra wins, but they agree to make it a weekly thing and invite MC back anytime
#During recurrent, reward progression goes to...
#Back rub - fingering - oral servicing - Full service - Free Use
#

init 1 python:
    def myra_alexia_teamup_scene_0_req(the_group):    #Requirements for the basic scene. Should almost always be true.
        return True

    def myra_alexia_teamup_scene_1_req(the_group):    #Requirements fo the second stage.
        if the_group[0].sluttiness > 20:
            return True
        return False


    def myra_alexia_teamup_scene_action_req(the_person):  #Use this function to determine the requirement for when to actually run the scene itself.
        if the_person.location == university:
            return True
        return False

    def myra_alexia_teamup_unit_test_func(the_group):
        for person in the_group:
            person.change_slut(20)
            person.change_energy(200)
        mc.change_energy(200)
        return

init 2 python:
    def myra_alexia_teamup_scene_compile_scenes(the_progression_scene):
        #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
        the_progression_scene.start_scene_list = ["myra_alexia_teamup_scene_intro_0", "myra_alexia_teamup_scene_intro_1"]
        the_progression_scene.req_list = [myra_alexia_teamup_scene_0_req, myra_alexia_teamup_scene_1_req]
        the_progression_scene.trans_list = ["kaya_erica_trans_scene_0", "kaya_erica_trans_scene_1"]
        the_progression_scene.final_scene_list = ["myra_alexia_teamup_scene_scene_0", "myra_alexia_teamup_scene_scene_1"]
        the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.
        return

    myra_alexia_teamup_scene_action = Action("myra_alexia_teamup Fuck session", myra_alexia_teamup_scene_action_req, "myra_alexia_teamup_scene_action_label")

    def myra_alexia_teamup_scene_init():  #Run this during init only
        global myra_alexia_teamup_scene
        myra_alexia_teamup_scene = Progression_Scene(
            compile_scenes = myra_alexia_teamup_scene_compile_scenes,
            start_scene_list = [],  #Set via the compile action
            req_list = [],  #Set via the compile action
            trans_list = [],    #Set via the compile action
            final_scene_list = [],  #Set via the compile action
            intro_scene = "myra_alexia_teamup_scene_intro_scene", #Scene that plays the first time this scene is run
            exit_scene = "myra_alexia_teamup_scene_exit_scene",   #Scene for if the player chooses to exit the scene
            progression_scene_action = myra_alexia_teamup_scene_action,      #The action used to call for this progression scene.
            choice_scene = "myra_alexia_teamup_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
            stage = -1,     #-1 will play the intro
            person_action = True,   #If this progression scene should run when encountering a person
            business_action = False,    #If this progression scene is a mandatory business event
            is_random = False,  #If this progression scene is a randomly occuring crisis event
            unit_test_func = myra_alexia_teamup_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
            advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
            is_multiple_choice = False, #If MC can choose what final scene he wants
            multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
            regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.
        myra_alexia_teamup_scene.compile_scenes(myra_alexia_teamup_scene)   #This will populate the scenes that are blank above.


label myra_alexia_teamup_scene_action_label(the_person):  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: myra_alexia_teamup_scene_action_label():
    $ mc.change_location(gaming_cafe)
    $ mc.location.show_background()
    call progression_scene_scene_label(myra_alexia_teamup_scene, [the_person, alexia]) from _myra_alexia_teamup_scene_call_test_01
    return

label myra_alexia_teamup_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "Walking through the mall, nearly everything is closing down. It is a bit of a ghost town as you make your way to the gaming cafe."
    "You step inside, and hear a familiar voice calling out to you."
    the_person "Hey, sorry we are just closing up, you'll have to come another time..."
    $ scene_manager.add_actor(the_person)
    "[the_person.possessive_title] suddenly appears from around a group of desks."
    the_person "Oh hey [the_person.mc_title]. Did you need something?"
    alexia "[alexia.mc_title] is here?"
    "You hear [alexia.possessive_title] call out from the back of the cafe. [the_person.title] has a couple couches and some retro consoles set up back there."
    mc.name "I knew you two were gonna hang out tonight, just thought maybe I'd swing by for a bit."
    the_person "Oh... I suppose we could all hang out for a bit. Hey [alexia.name]! Do you care if he hangs out with us some?"
    alexia "Sure! Let's put him to work though. The food court is probably almost closed, can you go get me a milkshake?"
    the_person "Ooooh! That sounds good! Get me one too!"
    mc.name "Ummm, sure... what flavors?"
    alexia "Strawberry!"
    the_person "Chocolate for me..."
    mc.name "Okay, I'll be right back with those."
    the_person "Sounds good. Do me a favor, I'll leave the door unlock but closed behind you. When you get back can you lock up behind you?"
    mc.name "Yeah I can do that."
    the_person "Great!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] turns and walks back towards the couches. "
    $ scene_manager.clear_scene()
    "You walk down to the food court. Most places are closing up, but a few are still open."
    "Luckily, the stand that sells milkshakes is still open. You purchase a strawberry and a chocolate and head back towards the gaming cafe."
    $ mc.business.change_funds(-10)
    "As you walk back to the cafe, you look around. The mall is deserted... maybe you should slip a couple serums in the milkshakes?"
    "You look at [the_person.possessive_title]'s drink."
    call give_serum(the_person) from _call_give_myra_serum_teamup_01
    "You look at [alexia.set_possessive_title]'s drink."
    call give_serum(the_person) from _call_give_elexia_serum_teamup_02
    "When you get back to the cafe, you step inside and lock the door behind you."
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You walk to the back where the couches are and see the two girls playing an old game together."
    mc.name "I've got milkshakes!"
    alexia "Yay!"
    the_person "Hey, thanks [the_person.mc_title]!"
    $ the_person.change_happiness(5)
    $ alexia.change_happiness(5)
    "The girls seem thankful for their drinks. You sit down on the couch next to [the_person.title] and watch as the girls play."
    "They are playing a fighting game where the character's look like they are made clay. A match is just getting ready to start."
    the_person "Are you okay just watching? This game is only two player... maybe we play it where winner stays on?"
    mc.name "That's okay, I'm fine with just watching and hanging out with you two."
    $ alexia.change_love(1, 50)
    $ the_person.change_love(1,50)
    alexia "Aww, that's sweet of you. Alright [myra.name], you're mine!"
    "Round one starts, but it is clear that [the_person.possessive_title] is the better gamer. After two quick rounds, the game declares her as the winner."
    the_person "Yes!"
    alexia "Geeze! You just going to sit there and watch this slaughter [alexia.mc_title]? Or are you going to help me?"
    mc.name "Help? By doing what?"
    alexia "I don't know... distract her or something!"
    the_person "Oh! That's a good idea! Do that thing we did the other day, [the_person.mc_title]."
    alexia "Thing?"
    the_person "Yeah, he is helping me train my focus while playing games while giving me backrubs. It makes it hard to play when you are feeling relaxed."
    the_person "His hands are amazing though, so it helps me learn to focus, and at the same time it feels great..."
    "You glance at [alexia.title] and see a hint of jealousy in her face..."
    alexia "Ahh... yeah... I just didn't realize you two were getting to be so friendly I guess..."
    "[the_person.possessive_title] blushes a little but tries to deflect."
    the_person "It's not like that! He's just like... being my coach or something..."
    "The room is getting awkward."
    mc.name "Hey, I've got an idea, just to make this fair. How about whoever wins a match, during the next I'll give the winner a back rub."
    alexia "Yeah! That's a great idea!"
    the_person "Yeah! Can't wait to have your hands on me all night!"
    $ mc.change_locked_clarity(10)
    "[the_person.title] sticks her tongue out at [alexia.possessive_title], teasing her."
    alexia "Ha! As if! It's time to bring out my secret weapon... Frosty!"
    "[alexia.title] selects the snowman clay fighter on the screen. You scoot over close to [the_person.title] as she selects the scarecrow themed fighter."
    $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = .2, zoom = 1.2))
    $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
    "[the_person.possessive_title] sighs when you put your hands on her shoulders. You can already feel her relaxing as [alexia.title] selects an arena."
    "TV" "Round one. Fight!"
    "You are only half paying attention to the game as you massage [the_person.possessive_title]'s neck and shoulders."
    "She gets tense for a second as she tries to pull off a combo, but your hands dig in and she sighs."
    the_person "Mmnnff..."
    "A small moan escapes her lips. [alexia.possessive_title] glances over and notices she is distracted."
    "She quickly strings together a combo before [the_person.title] can react, and soon the round is over."
    the_person "Ah! Hey!"
    alexia "Yes! Lookout girl, I need a backrub too!"
    the_person "I don't think so!"
    "TV" "Round two. Fight!"
    "[the_person.possessive_title] jumps out aggressively. She gets in a few good hits, so you double down and press hard under her shoulder blades."
    the_person "Oh! Mmmm..."
    $ the_person.change_arousal(10)
    "There is a definite pleasurable tone to her gasp as you work on her back. [alexia.possessive_title] looks over and flashes you a big smile."
    "[alexia.title] runs another combo, dropping [the_person.possessive_title]'s health by over half."
    the_person "No! [the_person.mc_title] stop for just a second I'm not ready for you to be done yet!"
    "Unwilling to play fairly, you keep kneading her back."
    "[the_person.title] tries holding the block button, just trying to prolong the match as long as she can."
    "[alexia.possessive_title] quickly catches on, jumps over her character and uses a grab move."
    "TV" "Player two wins!"
    $ scene_manager.update_actor(alexia, position = "stand3")
    "[alexia.title] jumps up."
    alexia "YES!!!"
    the_person "No!"
    alexia "Get your ass over here [alexia.mc_title]! From the noises she was making, those hands must be magical!"
    "You move over next to [alexia.title]."
    $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
    $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
    "You start to rub [alexia.possessive_title]'s back as the girls get ready to play another round. She let's out an exaggerated moan."
    alexia "MMMM that feels AMAZING [alexia.mc_title]!"
    $ mc.change_locked_clarity(10)
    if alexia.is_single() or alexia.is_girlfriend():    #
        $ the_person.event_triggers_dict["knows_alexia_single"] = True
        the_person "Wow, should I give you two some privacy?"
        if alexia.sluttiness > 20:
            alexia "Wow, you would do that? You're such a good friend [myra.name]!"
            "[the_person.title] rolls her eyes."
        else:
            alexia "Just teasing, geesh! No need to take it so far."
            "[the_person.title] rolls her eyes."
    else:
        $ the_person.event_triggers_dict["knows_alexia_single"] = False
        the_person "Wow, does your boyfriend know you're out getting backrubs from strange men tonight [alexia.name]?"
        "[alexia.title] rolls her eyes."
        alexia "What he doesn't know won't hurt him..."
        $ alexia.change_slut(1, 50)
        "You are a little surprised by her words. You wonder how far you'll be able to take things in the future at these gaming sessions with [alexia.title]..."
    "The match starts, but [alexia.possessive_title] doesn't even bother trying to win."
    "She guards, counters and plays defensively, just trying to prolong the match."
    the_person "Seriously? This is how its gonna be huh?"
    alexia "Mmmff... Hey you started it..."
    $ alexia.change_arousal(10)
    "[alexia.title] groans as you work on her shoulders. You think hear a gasp even."
    "[alexia.possessive_title] successfully drags the match out for several minutes, but eventually it's over."
    "TV" "Player one wins!"
    the_person "Yes!"
    alexia "Arg... five more minutes?"
    the_person "Not a chance! Get over here magic hands!"
    $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = .2, zoom = 1.2))
    $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
    "You scoot back over next to [the_person.title]."
    "For a while, you massage the backs of the two girls as they play games. Once in a while [alexia.possessive_title] wins, but you spend most of your time with [the_person.title]."
    alexia "Damn! I hate this game! I need a break."
    the_person "Me too. I have snacks, let me go grab some."
    mc.name "I think it is time for me to head out. You two have fun tonight."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose, display_transform = character_right(yoffset = 0, zoom = 0))
    $ scene_manager.update_actor(alexia, position = alexia.idle_pose, display_transform = character_center_flipped(yoffset = 0, zoom = 0))
    "When you stand up, so do both girls."
    alexia "Okay, I lied. That was super fun. I just need to get better."
    the_person "Yeah, honestly it is really nice playing a different game for a change too. We should do this more often!"
    alexia "How about next week? [alexia.mc_title] could come by if he wants too!"
    the_person "Oh! That's a great idea! Friday night, game night!"
    mc.name "That sounds great! I can't promise I'll be here every Friday, but I'll try to swing by when I can."
    the_person "Neat! Can you let yourself out? The door should lock itself."
    mc.name "Certainly. Goodnight girls, have a good night!"
    alexia "Bye!"
    $ scene_manager.clear_scene()
    "You let yourself and head home."
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "The friendship between [the_person.title] and [alexia.possessive_title] seems to be in good health. And this Friday night appointment seems to be a great opportunity."
    "You are pretty sure that if you offer to grab milkshakes for the girls, you can probably continue to test serums on them... you wonder how far you can push things at Friday Night game night!"
    # call advance_time from _call_advance_myra_alexia_teamup_scene_adv_01
    return

label myra_alexia_teamup_scene_intro_0(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You step into the gaming cafe. It looks like [the_person.title] is getting ready to close up."
    $ scene_manager.add_actor(the_person)
    the_person "Oh hey [the_person.mc_title]. We are having another game night!"
    mc.name "We?"
    alexia "Hey!"
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    "[alexia.possessive_title] suddenly stands up from a couch and walks over."
    alexia "[alexia.mc_title]! Couldn't stay away from gamer girl's night could you?"
    the_person "Here to rub my back all night?"
    alexia "Hey now, he only rubs the WINNER's back!"
    "[the_person.title] sticks out her tongue, then retorts."
    the_person "I know."
    alexia "Hey, I've been practicing!"
    the_person "Sure, sure."
    "You can feel some friendly competition in the air."
    return

label myra_alexia_teamup_scene_intro_1(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You step into the gaming cafe. It looks like [the_person.title] and [alexia.possessive_title] are chatting as they close up."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    "[alexia.title] notices you first."
    alexia "Oh hey! Excuse me sir we are closing up for the night!"
    "She gives you a big wink."
    return

label myra_alexia_teamup_scene_intro_2(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You step into the gaming cafe. It looks like [the_person.title] and [alexia.possessive_title] are chatting as they close up. They don't notice you right away..."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    alexia "Yeah, well... let's just say working there has been... interesting."
    "[the_person.title] looks up an notices you. She quickly elbows [alexia.title]."
    the_person "Hey! You're here! We were wondering if you would be swinging by."
    alexia "Hoping, even."
    "She gives you a big wink."
    return

label myra_alexia_teamup_scene_intro_3(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You step into the gaming cafe. It looks like [the_person.title] and [alexia.possessive_title] are chatting as they close up."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    "[alexia.title] notices you right away. It's almost like they were waiting for you?"
    alexia "Yes! You're here!"
    the_person "Told you he couldn't stay away. A couple hot bitches like us, who could?"
    "She gives you a big wink."
    return

label myra_alexia_teamup_scene_intro_4(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You go to the gaming cafe. As you try to enter the door though, it is already locked. Are you late?"
    "You knock on the door. Suddenly a figure appears in the doorway."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.strip_full_outfit(the_person, delay = 0)
    $ mc.change_locked_clarity(40)
    "She quickly opens the door and you step inside."
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    $ scene_manager.strip_full_outfit(alexia, delay = 0)
    "[alexia.title] is also inside. The state of the girls dress leaves you speechless."
    $ mc.change_locked_clarity(40)
    alexia "Hey [alexia.mc_title]! I've been looking forward to game night all week!"
    the_person "Yeah, me too!"
    "The girls both give you big smiles."
    return

#For more progression, add more scenes.

label myra_alexia_teamup_scene_scene_0(the_group, scene_transition = False):  #Massages
    $ the_person = the_group[0]
    $ current_round = 1
    $ round_count = 1
    $ myra_wins = 0
    $ alexia_wins = 0
    $ the_target = None
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You walk to the back where the couches are and see the two girls playing the claymation fighting game again."
    mc.name "Milkshakes time!"
    alexia "Yay!"
    the_person "Hey, thanks [the_person.mc_title]!"
    $ the_person.change_happiness(5)
    $ alexia.change_happiness(5)
    "The girls seem thankful for their drinks."
    "As the girls get ready to play, you check your watch. It is already pretty late, but you want to watch enough matches to atleast declare a winner."
    "How many wins will it take to win tonight?"
    "NOTE: the larger the number, the longer the event."
    menu:
        "1":
            pass
        "2":
            $ round_count = 2
        "3":
            $ round_count = 3

    alexia "Same rules as last time, right? Winner get's a back massage during the next round?"
    the_person "Sure, but I think we should put him to work right away. Why don't you sit down next to me and start that massage now? It'll be like a handicap."
    alexia "Hey, that's not fair! You should start with me, [alexia.mc_title]!"
    "Which girl do you want to sit next to first?"
    menu:
        "[myra.title]":
            $ the_target = myra
        "[alexia.title]":
            $ the_target = alexia

    "You sit down next to [the_target.possessive_title]. You think you see a hint of jealousy in the other girl's eyes, but it quickly vanishes as the game starts up."
    while myra_wins < round_count and alexia_wins < round_count:
        #Get close to the target
        if the_target == myra:
            $ scene_manager.update_actor(myra, display_transform = character_right(yoffset = .2, zoom = 1.2))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
        else:
            $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
        "The character select screen comes up, and you get close to [the_target.title], ready to begin your back massage."
        call myra_alexia_teamup_fight_round_label(the_group, (the_target == myra)) from _myra_alexia_back_massage_round_call_01
        if _return == myra:
            $ myra_wins += 1
            $ the_target == myra
            if the_target.arousal >= 30:
                myra "Yes! I win again! This is the best night ever! Your hands feel amazing [myra.mc_title]!"
                $ mc.change_locked_clarity(10)
            else:
                myra "Yes! I could use a good back massage."
        else:
            $ alexia_wins += 1
            $ the_target == alexia
            if the_target.arousal >= 30:
                alexia "Oh my god... I won again? This is great!"
            else:
                alexia "Yay! You give great massages, [alexia.mc_title]!"

    if alexia_wins >= round_count:
        "It's over. [alexia.possessive_title] is the winner for the night."
    else:
        "It's over. [myra.possessive_title] is the winner for the night."
    mc.name "Alright girls, I need to get going soon, but I also don't want to go without giving the final winner her reward."
    if the_target == alexia:
        mc.name "[alexia.title], why don't you grab some snacks for you two while I work on [myra.title] for a bit?"
        alexia "Fine. I need to use the ladies room anyway... just don't do anything too crazy while I'm gone you two!"
        myra "No promises!"
        alexia "[alexia.mc_title], I'll see you at work next week, okay?"
        mc.name "Bye [alexia.title]."
        "The girls laugh, but [alexia.possessive_title] gets up and heads towards the restroom."
        $ scene_manager.remove_actor(alexia)
    else:
        mc.name "[myra.title], why don't you grab some snacks for you two while I work on [alexia.title] for a bit?"
        myra "Damn. Beat at games in my own gaming cafe. Fine! I think I'm going to heat up a frozen pizza I got in the back."
        "[myra.possessive_title] starts to get up, but then stops and looks at you."
        myra "Don't do anything too crazy while I'm gone... or I'll send you the cleaning bill!"
        alexia "[myra.name]!"
        "You and [myra.title] share a good laugh at [alexia.possessive_title]'s expense."
        myra "See ya around [myra.mc_title]."
        mc.name "Bye [alexia.title]."
        "[myra.possessive_title] gets up and heads towards the kitchen area."
        $ scene_manager.remove_actor(myra)
    "You scoot back over next to [the_target.title]."
    the_target "Hey, I got an idea. I'm going to lay on my stomach and just relax, okay?"
    mc.name "Sure, sounds good."
    $ scene_manager.update_actor(the_target, position = "walking_away")
    "You gently sit on [the_target.title]'s back, leaning forward as you begin your work on her back."
    the_target "Ahhh, sweet victory."
    "You spend a while just rubbing and caressing her back. She sighs and coos as your massage her."
    $ the_target.change_love(2, 60)
    "After a bit though, it is definitely time to go."
    mc.name "Alright, well I need to get home. You have a good night, okay?"
    the_person "God that was so good. Is it okay if I don't get up?"
    mc.name "That is fine. I'll see myself out."
    $ scene_manager.clear_scene()
    "You get up and head home."
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "There was a lot of tension in the air tonight between you and the two girls. You know you can push things between you and them farther with a little more time..."
    # call advance_time from _call_advance_myra_alexia_teamup_scene_adv_01
    return

label myra_alexia_teamup_scene_scene_1(the_group, scene_transition = False):  #Groping intro
    $ the_person = the_group[0]
    "This is the second scene. I'm not coding it, but you could code it that she gets naked and bends over, preseting her ass here."
    $ the_person.draw_person(position = "standing_doggy")
    the_person "Don't worry, my ass is always ready for you!"
    call fuck_person(the_person) from _call_sex_description_myra_alexia_teamup_scene_02

    the_person "Oh my god I hope I can walk tomorrow!"
    #You probably want to to advance time after this
    #call advance_time from _call_advance_myra_alexia_teamup_scene_adv_03
    return



label myra_alexia_teamup_trans_scene_0(the_group):
    pass
    #This label should probably never be called because this event can't regress.
    return

label myra_alexia_teamup_trans_scene_1(the_group):
    $ the_person = the_group[0]
    "This is the transition to the second scene."
    the_person "I have another idea though... what if you fucked... my other hole?"
    mc.name "That's a good idea."
    return



label myra_alexia_teamup_scene_choice_label(the_group):
    $ the_person = the_group[0]
    the_person "So, are you going to stick around? Or just stopping by?"
    "[alexia.possessive_title] looks at you, you can tell she wants you to hang out."
    if myra_alexia_teamup_scene.stage < 2:
        alexia "Please [alexia.mc_title]? It's not the same without your magic hands to play for!"
        the_person "Ha! Yeah having something to play for definitely makes it more fun!"
    elif myra_alexia_teamup_scene.stage == 2:
        alexia "I honestly don't even care if I win or lose... but you should stick around!"
        "[alexia.title] glances down at your crotch and licks her lips. She's clearly thinking about what would happen if she loses..."
        the_person "Not me! I want to win for sure!"
        $ mc.change_locked_clarity(25)
        "Thought's of eating out [the_person.title] while [alexia.possessive_title] sucks your cock are certainly tantalizing..."
    elif myra_alexia_teamup_scene.stage == 3:
        alexia "You can warm me up while we play the first few rounds! You should stick around!"
        "[alexia.title] appears ready to start getting naked already."
    else:
        "You look at the two girls, ready and eager to let you fuck them as they play games together."
        "Their naked bodies already on display for you."
        alexia "It is so nice now, just playing for fun and relaxing while you fuck us good!"
        the_person "Yeah! You're totally going to stick around... right [the_person.mc_title]?"

    "Are you going to stay while the girls play?"
    menu:
        "Stay":
            pass
        "Leave":
            return False
    mc.name "Of course, I'd be crazy not to stick around. Do you two want milkshakes?"
    the_person "Fuck yeah!"
    alexia "One for me too please!"
    mc.name "Okay, I'll be right back."
    $ scene_manager.clear_scene(reset_actor = False)
    call myra_alexia_teamup_serum_label(the_group) from _myra_alexia_milkshake_serums_02
    return True

label myra_alexia_teamup_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    mc.name "Sorry, it has been a really long week and I need to head home."
    alexia "What? Damn..."
    the_person "That's okay. Maybe next week then?"
    mc.name "I'll try."
    $ clear_scene()
    "You leave the gaming cafe, leaving the girls to their game night"
    return

label myra_alexia_teamup_serum_label(the_group):
    "You walk down to the food court. Most places are closing up, but a few are still open."
    "Luckily, the stand that sells milkshakes is still open. You purchase a strawberry and a chocolate and head back towards the gaming cafe."
    $ mc.business.change_funds(-10)
    "As you walk back to the cafe, you look around. The mall is deserted... time to decide if you want to drop a serum in."
    if myra_alexia_teamup_scene.stage != 4:
        "If you wanted a particular girl to win, you could probably influence it with a serum you put in."
        "To be good at games, someone needs to have focus, and be good with their hands... (foreplay)"
    else:
        "The girls are already basically putty in your hands."
    "You look at [the_person.possessive_title]'s drink."
    call give_serum(the_person) from _call_give_myra_serum_teamup_03
    "You look at [alexia.set_possessive_title]'s drink."
    call give_serum(the_person) from _call_give_elexia_serum_teamup_04
    "When you get back to the cafe, you step inside and lock the door behind you."
    return

label myra_alexia_teamup_fight_round_label(the_group, myra_is_target):
    #Use skill score to determine the likely winner. Foreplay and focus score, with arousal bein a distraction.
    $ skill_score = int(((myra.focus + myra.sex_skills["Foreplay"]) - (myra.arousal / 10) ) - ((alexia.focus + alexia.sex_skill["Foreplay"]) - (alexia.arousal / 10) ))
    if myra_is_target:
        $ the_target = myra
    else:
        $ the_target = alexia
        $ skill_score = (-skill_score)

    if myra_alexia_teamup_scene.stage < 4:
        "[the_target.title] leans back against you as the girls pick their characters. The heat of her body feels good against your chest."
    else:
        "[the_target.title] sits on your lap and leans back against you, your cock nestled in the crack of her ass."
        "She gives a sigh and a little giggle as she picks up her controller and the girls pick their characters."
    if skill_score > 2:
        "[the_target.possessive_title] has an excellent chance of winning the matchup..."
        "That is, of course, depending on if your magic hands happen to be a distraction."
        "Maybe you should even up the match up a little?"
    if skill_score < -2:
        "[the_target.possessive_title] has a low chance of winning the matchup from what you have seen so far."
        "Maybe you should take the opportunity to have some fun with [the_target.title]..."
    else:
        "The matchup seems to be pretty even. You feel like this round could go either way."
        "You could go easy on [the_target.possessive_title] to keep the matchup for... or..."

    "How much should you distract [the_target.title]?"
    menu:
        "Light Distraction":
            call myra_alexia_teamup_light_distraction(the_target) from _myra_alexia_teamup_light_dist_0101
            $ skill_score -= 1
        "Moderate Distraction":
            call myra_alexia_teamup_med_distraction(the_target) from _myra_alexia_teamup_med_dist_0101
            $ skill_score -= 3
        "Major Distraction":
            call myra_alexia_teamup_large_distraction(the_target) from _myra_alexia_teamup_large_dist_0101
            $ skill_score -= 5
    if _return:
        $ the_target.change_arousal(_return)
    if myra_alexia_teamup_scene.stage >= 2 and the_target.arousal >= 100:   #You drive her to orgasm
        pass
    return

label myra_alexia_teamup_light_distraction(the_person):
    if myra_alexia_teamup_scene.stage == 0:
        "You put your hands on [the_person.possessive_title]'s shoulders and start a soft massage."
        "You keep your hands light to make sure not to distract her too much."
        "At a couple points in time, the fight gets tense, so you take a second and let [the_person.title] fight before resuming your back rub."
        the_person "Mmm..."
        "[the_person.title] sighs as you hit a particulary tense area. She feels good and relaxed."
        return 10
    if myra_alexia_teamup_scene.stage == 1:
        if the_person.arousal < 40:
            "You let your hands roam up an down [the_person.possessive_title]'s back for a bit as the match gets started."
            "She wiggles a bit when you put your hands on her sides and pull her back against you a little bit more."
            "Your wrap your hands around her front, rubbing her stomach."
            "The fighting suddenly gets tense. Since she is distracted, you softly bring your hands up to her tits."
            the_person "Mmmm! Ahhh..."
            "[the_person.title] suddently realizes what you are doing when your thumb grazes against her nipple."
            if the_person.tits_available():
                "The heat and weight of her soft skin feels amazing in you hand. You softly knead her titflesh for the remainder of the match."
                return 20
            else:
                "You wish you could put your hand under her clothes, but you don't want to distract her too much."
                "You softly knead her tits through her clothes for the remainder of the match."
                return 15
        else:
            "[the_person.possessive_title] is breathing a little heavy in front of you. She seems to be pretty excited."
            "[the_person.title] steals a quick glance at the other girl, then quietly takes your hand and guides it from her side up to her chest."
            the_person "Mmmm..."
            "Encouraged by her, you run your thumb over her nipples. They are erect with excitement."
            if the_person.tits_available():
                "The heat and weight of her soft skin feels amazing in you hand. You eagerly caress her as she plays her match."
                return 20
            else:
                "You wish you could put your hand under her clothes, but you don't want to distract her too much."
                "You softly knead her tits through her clothes for the remainder of the match."
                return 15
    if myra_alexia_teamup_scene.stage == 2:
        if the_person.arousal < 30:
            "You softly run hands up and down [the_person.possessive_title]'s soft skin on her sides and belly as the match gets started."
            "You don't want to be too much of a distraction, you just want to get her slowly turned on as the match progresses."
            "Slowly, you reach up with your right hand and run your finger tips along her breast."
            "With your left hand, you reach down and cup her mound between her legs, applying gentle pressure."
            if the_person.vagina_available():
                "Some warmth is eminating from her exposed pussy as she slowly starts to get aroused."
            else:
                "[the_person.title] squirms a bit as you touch her pussy over her clothes."
            "The match has its ebbs and lulls, but you just keep slowly steady pressure on [the_person.title] as you touch her."
            the_person "Mmm... ah..."
            "She gives a small moan as the matches are just about finished."
            if the_person.vagina_available():
                return 30
            return 25

        elif the_person.arousal < 65:
            "[the_person.possessive_title] leans back against you. She sighs when your hands start to move along her skin."
            the_person "Mmm, that's nice..."
            "You bring both hands up to her tits for a bit. Her nipples are hard with arousal, so give them a few light pinches as the game begins."
            "You keep cupping her breast with one hand, then let the other work its way south."
            if the_person.vagina_available():
                "Your hand slowly slides down her mound, then reaches her cunt."
                "Her arousal is just barely starting leak out, moistening your fingers as you run them along her soft lips."
                "You are careful not to push your fingers inside, as much as you want to, trying to keep her arousal building but not providing too big of a distraction."
            else:
                "You run your hand along her mound on the outside of her clothes. You consider for a moment pulling them down."
                "You decide against it. You aren't trying to distract her too much, just keep her arousal building."
                "You cup her between her legs, applying moderately heavy pressure, and moving your fingers in a circular motion to stimulate her."
            the_person "That feels good... Mmm..."
            "You can tell that her arousal is starting to distract her from the match, but [the_person.title] is still doing pretty good."
            "Sometimes when there is a lull in the match, you feel her move her hips a bit, grinding against your hand as she plays."
            if the_person.vagina_available():
                return 35
            else:
                return 30
        else:
            if not the_person.vagina_available()
                "[the_person.possessive_title] is pretty clearly aroused, and you feel like you are about at your limit of how far you can drive her while she has clothes on."
                "You reach down and start to take her bottoms off."
                the_person "Hey, that's no fair, I can't concen..."
                mc.name "Shh, the match is starting."
                "[the_person.title] starts to protest, but you quickly pull her clothes off her lower body anyway as the match starts."
                $ scene_manager.strip_to_vagina(the_person)
                "Finally exposed, you drop one hand to her soaking wet pussy."
            else:
                "You can smell [the_person.possessive_title]'s arousal. You drop one hand down to her exposed soaking wet pussy."
            "You try to go easy on her, trying to prolong her pleasure as long as possible."
            "A couple times you feel her body start to tense up, not from the game, but from pleasure, so you back off each time."
            the_person "[the_person.mc_title]... I'm so close... just... just..."
            "You try to back off again, but [the_person.title] has other ideas. She grabs your hand with hers, shifts forward a bit, then sits on your hand, pinning it to the couch."
            "Completely ignoring the game, [the_person.possessive_title] starts rocking her hips, grinding herself on your hand."
            return 40

    if myra_alexia_teamup_scene.stage == 3:
        pass
    return

label myra_alexia_teamup_med_distraction(the_person):
    if myra_alexia_teamup_scene.stage == 0:
        "You put your hands on [the_person.possessive_title]'s shoulders and start a massage."
        "She has several tense areas, so you alternate between a light and more forceful massage, trying to get her tensest areas loosened up."
        "At a couple points in time, the fight gets tense, so you keep your touch light on [the_person.title] for a few seconds so you aren't TOO much of a distraction."
        the_person "Mmm... that's nice..."
        "[the_person.title] sighs as you hit a particulary tense area. She feels good and relaxed."
        return 15
    if myra_alexia_teamup_scene.stage == 1:
        if the_person.arousal < 40:
            "You let your hands roam up an down [the_person.possessive_title]'s back for a bit as the match gets started."
            "She wiggles a bit when you put your hands on her sides and pull her back against you a little bit more."
            "Your wrap your hands around her front, rubbing her stomach and working your way upward."
            "The fighting suddenly gets tense. Since she is distracted, you bring your hands up to her tits."
            the_person "Mmmm! Ahhh..."
            "[the_person.title] gasps when you run your thumbs over he nipples. Her body wiggles back against you a bit as you grope her breasts."
            if the_person.tits_available():
                "The heat and weight of her soft skin feels amazing in you hands. You eagerly knead her titflesh for the remainder of the match, much to her enjoyment."
                return 30
            else:
                "You wish you could put your hand under her clothes, but you don't want to distract her too much."
                "You eagerly knead her tits through her clothes for the remainder of the match, much to her enjoyment."
                return 20
        else:
            "[the_person.possessive_title] is breathing a little heavy in front of you. She seems to be pretty excited."
            if not the_person.tits_available():
                "Not content touch her over her clothes, you quietly start to pull at her top."
                "[the_person.title] glances over at the other girl, but with the match already starting she quickly decides to let you."
                $ scene_manager.strip_to_tits(the_person)
                "Finally topless, you bring your hands up to her amazing tits."
            else:
                "[the_person.title] steals a quick glance at the other girl, then quietly takes your hand and guides it from her side up to her chest."
            the_person "Mmmm..."
            "You grope and massage [the_person.possessive_title]'s tits. You keep a steady pace, not slowing down even when the matchup gets tense."
            "[the_person.title] gasps and squirms under your touch. She's trying to hide her pleasure, but she is barely keeping it together."
            return 30

    if myra_alexia_teamup_scene.stage == 2:
        if the_person.arousal < 30:
            "You softly run hands up and down [the_person.possessive_title]'s soft skin on her sides and belly as the match gets started."
            "Your goal isn't necessarily to throw the match, but you want to get her aroused and needy as the match progresses."
            "You reach up with your right hand and grab her breast, kneading it and once in a while you give her nipple a light pinch."
            "With your left hand, you reach down and cup her mound between her legs, applying pressure."
            if the_person.vagina_available():
                "Some warmth is eminating from her exposed pussy as she slowly starts to get aroused."
            else:
                "[the_person.title] squirms a bit as you touch her pussy over her clothes."
            "The match has its ebbs and lulls, but you just keep steady pressure on [the_person.title] as you touch her."
            "It is slight, but as the match goes on, her body is respdoning to your touches more and more. Her hips are moving slightly and her back arches when you pinch her nipple."
            the_person "Mmm... ah..!"
            "She gives a moan as the matches are just about finished."
            if the_person.vagina_available():
                return 35
            return 30

        elif the_person.arousal < 65:
            if not the_person.vagina_available()
                "[the_person.possessive_title] is starting to get aroused, and you want to drive her arousal even further, but that is hard to do while she is still covered up."
                "You reach down and start to take her bottoms off."
                the_person "Hey, that's no fair, I can't concen..."
                mc.name "Shh, the match is starting."
                "[the_person.title] starts to protest, but you quickly pull her clothes off her lower body anyway as the match starts."
                $ scene_manager.strip_to_vagina(the_person)
                "Finally exposed, you drop one hand to her moist pussy."
            else:
                "You can smell [the_person.possessive_title]'s arousal in the air faintly. You drop one hand down to her exposed pussy."
            "[the_person.possessive_title] leans back against you. She sighs when your other hand gropes her tit."
            the_person "Mmm, that feels so good."
            "Her body is melting into yours. She is trying to concentrate on the match, but is thoroughly enjoying your touch too."
            "Her pussy is getting so wet, "
            return 40
        else:
            if not the_person.vagina_available()
                "[the_person.possessive_title] is pretty clearly aroused, and you feel like you are about at your limit of how far you can drive her while she has clothes on."
                "You reach down and start to take her bottoms off."
                the_person "Hey, that's no fair, I can't concen..."
                mc.name "Shh, the match is starting."
                "[the_person.title] starts to protest, but you quickly pull her clothes off her lower body anyway as the match starts."
                $ scene_manager.strip_to_vagina(the_person)
                "As you finish pulling her clothes off, you can smell her arousal. You drop one hand to her soaking wet pussy."
            else:
                "You can smell [the_person.possessive_title]'s arousal. You drop one hand down to her exposed soaking wet pussy."

            return 40
    if myra_alexia_teamup_scene.stage == 3:
        pass
    return

label myra_alexia_teamup_large_distraction(the_person):
    if myra_alexia_teamup_scene.stage == 0:
        "You put your hands on [the_person.possessive_title]'s shoulders and start a massage."
        "She has several tense areas, so you press your hands into her muscles with urgency."
        "[the_person.title] gasps, trying to concentrate on the fight, but your hands are relentless."
        "At a couple points in time, the fight gets tense. You use the opportunity to find her tensest muscles and ."
        the_person "God... that feels amazing [the_person.mc_title]..."
        "[the_person.title] sighs as you hit a particulary tense area. She feels good but you have definitely distracted her."
        return 20
    if myra_alexia_teamup_scene.stage == 1:
        if not the_person.tits_available():
            "You are immediately annoyed by her top. You decide to take it off, whether she likes it or not."
            "[the_person.title] starts to protest, but you quickly pull her clothes off her upper body anyway as the match starts."
            $ scene_manager.strip_to_tits(the_person)
            "Finally topless, you bring your hands up to her amazing skin, running both hands down her sides."
        if the_person.arousal < 40:
            "You let your hands roam up an down [the_person.possessive_title]'s soft skin on her back and sides."
            "You don't even bother pretending to be gentle. With one hand you work on a knot you find on her back, with the other hand your reach around and grab one of her tits."
            the_person "Mmm! God... take it easy..."
            "[the_person.title] is trying to concentrate as the match gets suddenly tense, but instead of letting up, you double down."
            "You reach both hands around now and give her nipples a little pinch."
            "She curses under her breath and squirms a bit as you are now shamelessly groping her."
            return 40
        else:
            "[the_person.possessive_title] is breathing a heavy in front of you. She seems to be pretty excited."
            "[the_person.title] steals a quick glance at the other girl, then quietly takes your hand and guides it from her side up to her chest."
            the_person "Mmmm..."
            if the_person.has_large_tits()
                "You grope and massage [the_person.possessive_title]'s amazing tits. They feel heavy and full in your hands, her titflesh spilling between your fingers as you grab her."
            else:
                "You grope and massage [the_person.possessive_title]'s perky tits. She gasps with each pull and tug on her sensitive nipples."
            "When the matchup gets intense, you double down, pinching her nipples."
            the_person "Mmm! God... take it easy..."
            "[the_person.title] gasps and squirms under your touch. She's trying to hide her pleasure, but she is barely keeping it together."
            return 40
    if myra_alexia_teamup_scene.stage == 2:
        pass
    if myra_alexia_teamup_scene.stage == 3:
        pass
    return


label myra_alexia_teamup_orgasm_finish(the_person):
