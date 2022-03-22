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
            choice_scene = "myra_alexia_teamup_scene_study_choice",   #The action used to let player decide if they want to continue the scene or leave
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
    $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = -.2, zoom = 0.8))
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




    $ scene_manager.clear_scene()
    #You probably want to to advance time after this
    # call advance_time from _call_advance_myra_alexia_teamup_scene_adv_01
    return

label myra_alexia_teamup_scene_intro_0(the_group):
    $ the_person = the_group[0]
    "This is the most basic intro scene. It should run after you have experienced the intro."
    $ the_person.draw_person()
    the_person "Hey, down to fuck?"
    return

label myra_alexia_teamup_scene_intro_1(the_group):
    $ the_person = the_group[0]
    "This is the second intro scene, played after you unlocked it."
    the_person "Hey, I had fun last time when you fucked my ass!"
    return

#For more progression, add more scenes.

label myra_alexia_teamup_scene_scene_0(the_group):
    $ the_person = the_group[0]
    "This is the most basic final scene.."
    $ the_person.draw_person()
    the_person "Alright, let's do it!"
    call fuck_person(the_person) from _call_sex_description_myra_alexia_teamup_scene_01

    the_person "Whew! that was great!"
    #You probably want to to advance time after this
    # call advance_time from _call_advance_myra_alexia_teamup_scene_adv_02
    return

label myra_alexia_teamup_scene_scene_1(the_group):
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
    #This label should probably never be called.
    return

label myra_alexia_teamup_trans_scene_1(the_group):
    $ the_person = the_group[0]
    "This is the transition to the second scene."
    the_person "I have another idea though... what if you fucked... my other hole?"
    mc.name "That's a good idea."
    return



label myra_alexia_teamup_scene_study_choice(the_group):
    $ the_person = the_group[0]
    "Use this scene to give MC a chance to bail out."
    "Are you going to fuck her?"
    menu:
        "Fuck her":
            return True
        "Leave":
            return False
    return True

label myra_alexia_teamup_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    "Use this scene to show MC bailing out."
    mc.name "Unfortunately, I don't have time to fuck you. Goodbye."
    the_person "Bye!"
    "You stand up and leave the room, leaving the girls to their study session."
    $ clear_scene()
    return

label myra_alexia_teamup_multiple_choice_scene_label(the_group):
    $ the_person = the_group[0]
    "Use this scene if you want MC to have the option of what to do."
    "For example."
    the_person "How do you want to fuck me?"
    menu:
        "Vaginal" if 0 in myra_alexia_teamup_scene.scene_unlock_list:
            the_person "Yay! Let's fuck!"
            return 0
        "Anal" if 1 in myra_alexia_teamup_scene.scene_unlock_list:
            the_person "My ass? Oh boy!"
            return 1
    return 0

#Use regression scenes if you want to be able to go back steps in the scene. Useful if requirements are set on the edge of when characters would normally tolerate them.
label myra_alexia_teamup_regression_scene_scene_0(the_group):
    the_person "Actually, I don't like it in my ass... can we just fuck instead?"
    return

label myra_alexia_teamup_regression_scene_scene_1(the_group):
    pass
    return
