#This file is to add new options to girlfriends. Ideas include: afternoon delight, my place / your place, sexting, clothes shopping.
#Roleplays: These are scenes that will involve your girlfriend pretending to be someone/something else. Designed to take the place of the initial fucking scene.

init 3 python:
    girlfriend_morning_action_list = []     #Requirement functions can check mc.location to tell if it's myplace/yourplace if necessary.
    girlfriend_sleepover_interruption_list = []     #Ideas, daughter/mother walk in, phone call,
    girlfriend_roleplay_list = []           #When a roleplay is created, add it here as an option. list of ACTIONS

    def girlfriend_myplace_yourplace_requirement(the_person):
        if schedule_sleepover_available():
            if time_of_day < 4:
                return True
            else:
                return "Too Late"
        else:
            return "You already have a sleepover arranged"
        return False

    def girlfriend_sleepover_crisis_requirement():
        if time_of_day == 4:
            return True
        return False

    def girlfriend_wakeup_spooning_requirement(the_person):
        return True

    def girlfriend_underwear_shopping_requirement(the_person):
        if the_person.love < 80 and the_person.sluttiness < 40:
            return False
        if time_of_day == 0:
            return "Clothes store closed"
        elif time_of_day == 4: # Can be removed
            return "Clothes store closed"
        elif not mc.business.has_funds(500):
            return "Requires: $500"
        else:
            return True
        return False

    def girlfriend_quit_dikdok_requirement(the_person):
        if not the_person.has_role(dikdok_role):
            return False
        if the_person in unique_character_list:
            return False
        if the_person.love < 40: # hide option will love is very low
            return False
        if the_person.love < 60:
            return "Requires: 60 Love"
        return True


    girlfriend_sleepover_action = Action("Arrange a sleepover", girlfriend_myplace_yourplace_requirement, "girlfriend_myplace_yourplace_label",
        menu_tooltip = "Ask your girlfriend if she wants to sleep together tonight.")
    girlfriend_sleepover_crisis = Action("Have a sleepover", girlfriend_sleepover_crisis_requirement, "girlfriend_sleepover_crisis_label")
    girlfriend_underwear_shopping = Action("Shop for new lingerie", girlfriend_underwear_shopping_requirement , "girlfriend_underwear_shopping_label",
        menu_tooltip = "Take your girlfriend out to shop for some exciting underwear to wear for you.")

    girlfriend_wakeup_spooning = Action("Spooning wakeup", girlfriend_wakeup_spooning_requirement, "girlfriend_wakeup_spooning_label")
    girlfriend_wakeup_jealous_sister = Action("Jealous wakeup", girlfriend_wakeup_jealous_sister_requirement, "girlfriend_wakeup_jealous_sister_label")

    girlfriend_morning_action_list.append(girlfriend_wakeup_spooning)
    girlfriend_morning_action_list.append(girlfriend_wakeup_jealous_sister)

    girlfriend_quit_dikdok_action = Action("Quit DikDok", girlfriend_quit_dikdok_requirement, "girlfriend_quit_dikdok_label",
        menu_tooltip = "Ask your girlfriend to stop showing herself off on DikDok.")



init 5 python:
    add_label_hijack("normal_start", "activate_girlfriend_role_enhancement")
    add_label_hijack("after_load", "activate_girlfriend_role_enhancement")

    def schedule_sleepover_in_story(person, your_place = True):
        mc.business.event_triggers_dict["girlfriend_person"] = person.identifier
        mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = True
        mc.business.event_triggers_dict["your_place"] = your_place
        mc.business.add_mandatory_crisis(girlfriend_sleepover_crisis)
        return

    def schedule_sleepover_get_girlfriend_person():
        identifier = mc.business.event_triggers_dict.get("girlfriend_person", None)
        if isinstance(identifier, Person):
            return identifier
        return get_person_by_identifier(identifier)

    def schedule_sleepover_available():
        return not mc.business.event_triggers_dict.get("girlfriend_sleepover_scheduled", False)

    def get_random_girlfriend_morning_action(person):
        possible_action_list = []
        for wakeup_scene in girlfriend_morning_action_list:
            if wakeup_scene.is_action_enabled(person):
                wakeup_scene.args = [person]
                possible_action_list.append(wakeup_scene)
        return get_random_from_list(possible_action_list)

label activate_girlfriend_role_enhancement(stack):
    python:
        girlfriend_role.add_action(girlfriend_sleepover_action)
        girlfriend_role.add_action(girlfriend_underwear_shopping)
        girlfriend_role.add_action(girlfriend_quit_dikdok_action)

        sister_girlfriend_role.add_action(girlfriend_underwear_shopping)
        mom_girlfriend_role.add_action(girlfriend_underwear_shopping)

        execute_hijack_call(stack)
    return

label girlfriend_myplace_yourplace_label(the_person):
    mc.name "So, I'm kinda busy right now, but I thought that maybe later we could get together."
    the_person "Mmm, that sounds like fun. My place or yours?"
    menu:
        "My place":
            mc.name "Come over tonight, you can spend the night."
            $ the_person.call_dialogue("sleepover_yourplace_response")
            $ mc.business.event_triggers_dict["your_place"] = True
        "Your place":
            mc.name "How about your place? I'll bring a bottle of wine."
            $ the_person.call_dialogue("sleepover_herplace_response")
            $ mc.business.event_triggers_dict["your_place"] = False
    the_person "Anything else you need right now?"
    $ mc.change_locked_clarity(15)
    $ mc.business.event_triggers_dict["girlfriend_person"] = the_person.identifier
    $ mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = True
    $ mc.business.add_mandatory_crisis(girlfriend_sleepover_crisis)
    return

label girlfriend_sleepover_crisis_label():
    $ the_person = schedule_sleepover_get_girlfriend_person()
    if the_person == None:
        return
    #TODO give player the option to cancel the sleepover. she's probably sad.
    if mc.business.event_triggers_dict.get("your_place", True):
        "You go home for the night. Knowing that [the_person.title] is coming over, you quickly hop in the shower."
        $ mc.change_location(bedroom)
        $ mc.location.show_background()
        "When you finish, you go to your room. You make sure everything is nice and tidy."
        $ mc.start_text_convo(the_person)
        the_person "Hey, I'm here, let me in?"
        $ mc.end_text_convo()
        $ the_person.draw_person()
        "You go to the front door. Your girlfriend is waiting for you."
        the_person "Hey!"
        #TODO mom or sister notice you, say hi, etc
        "You quickly lead her to your room. After you enter, you lock the door."
        the_person "I brought a few things with me. Mind if I use your bathroom?"
        mc.name "Go ahead."
        $ clear_scene()
        "[the_person.possessive_title] walks into your bathroom. You sit down on the bed and wait a couple minutes. Soon, you hear to door open."
        $ the_person.change_to_lingerie()
        $ the_person.draw_person()
        $ mc.change_locked_clarity(30)
        "[the_person.title] has changed into something much more comfortable..."
        mc.name "Damn, you look amazing..."
        $ the_person.call_dialogue("sleepover_yourplace_sex_start")
    else:
        "It's time for your date with [the_person.title]. You swing by the store on the way and pick up a decent bottle of wine."
        $ mc.business.change_funds(-15)
        $ the_person.learn_home()
        "You make your way to her place, then knock on the door. She quickly answers."
        $ the_person.draw_person()
        the_person "Ah! I'm so glad you're here. Come in!"
        $ mc.change_location(the_person.home)
        $ mc.location.show_background()
        "You step inside. She leads you to the kitchen, where you set the wine."
        $ the_person.draw_person(position = "walking_away")
        the_person "That looks great! Let me get a couple wine glasses..."
        "She reaches up into the cabinet and pulls a couple down."
        $ the_person.draw_person(position = "stand2")
        the_person "You pour! I just got home a few minutes ago and I need to slip into something more comfortable."
        $ clear_scene()
        "You look through her drawers until you find a bottle opener. You pop the cork on the wine and pour a couple glasses."
        "She's busy... maybe you should put a serum in it?"
        menu:
            "Add a dose of serum to [the_person.title]'s wine" if mc.inventory.get_any_serum_count() > 0:
                call give_serum(the_person) from _call_give_serum_girlfriend_sleepover_01
                "You mix the serum into [the_person.title]'s wine."
            "Add a dose of serum to [the_person.title]'s shake\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.get_any_serum_count() == 0:
                pass
            "Leave her drink alone":
                "You decide to leave her wine alone."
        "You wait for another minute, when you hear the bedroom door open."
        $ the_person.change_to_lingerie()
        $ the_person.draw_person()
        "[the_person.possessive_title] has changed into some sexy clothes."
        $ mc.change_locked_clarity(30)
        the_person "Hey... bring the glasses in here!"
        "She disappears into her bedroom. You quickly grab the glasses and follow her in. She is sitting on the edge of her bed."
        $ the_person.draw_person(position = "sitting")
        "You hand her the wine glass. She takes a long sip."
        $ the_person.call_dialogue("sleepover_herplace_sex_start")
    call fuck_person(the_person, private = True) from _call_fuck_person_sleepover_gf_01

    $ the_report = _return

    $ done = False
    $ girl_came = the_report.get("girl orgasms", 0)
    $ fuck_time_interrupted = False
    $ energy_gain_amount = 50 #Drops each round, representing your flagging endurance.
    if perk_system.has_ability_perk("Lustful Youth"):
        $ energy_gain_amount += 70
    while done == False:

        if girl_came > 5:
            $ the_person.change_stats(love = 3, slut = 1)
            $ the_person.call_dialogue("sleepover_impressed_response")
            if not perk_system.has_ability_perk("Lustful Youth"):
                "You feel like making [the_person.possessive_title] cum over and over has woken something inside you."
                "You feel like no matter what happens or how your day is going, you will always have the energy to make the ones you love cum."
                $ lustful_youth_perk_unlock()
                "You have gained the perk 'Lustful Youth'!"
        elif girl_came > 0:
            $ the_person.change_love(1)
            $ the_person.call_dialogue("sleepover_good_response")
        else:
            $ the_person.call_dialogue("sleepover_bored_response")

        if mc.energy < 40 and energy_gain_amount <= 20: #Forced to end the fuck date, so we set done to True.
            "The spirit is willing, but the flesh is spent. Try as she might [the_person.title] can't coax your erection back to life."
            if girl_came > 0:
                the_person "Mmm, I wore you out! That was fun."
                "She kisses you and runs her hand over your back."
            else:
                $ the_person.change_stats(slut = -1, love = -1)
                the_person "Well I guess we're done then... Maybe next time you can get me off as well."
            $ done = True

        else:
            "After a short rest you've recovered some of your energy and [the_person.possessive_title]'s eager to get back to work."
            $ mc.change_energy(energy_gain_amount)
            $ the_person.change_energy(energy_gain_amount) #She gains some back too
            if energy_gain_amount >= 10:
                $ energy_gain_amount += -10 #Gain less and less energy back each time until eventually you're exhausted and gain nothing back.
            menu:
                "Fuck her again":
                    "With your cock hard again, you pull [the_person.title] towards you."
                    $ mc.change_locked_clarity(30)
                    if renpy.random.randint(0,100) < 12 and not fuck_time_interrupted:
                        python:
                            fuck_time_interrupted = True    #Limit ourselves to one interruption per sleepover
                            possible_action_list = []
                            for interruption_scene in girlfriend_sleepover_interruption_list:
                                if interruption_scene.is_action_enabled(the_person): #Make sure requirement functions take the person as an arg
                                    possible_action_list.append(interruption_scene) #Build a list of valid crises from ones that pass their requirement.
                        $ interruption_action = get_random_from_list(possible_action_list)
                        if interruption_action:
                            call expression interruption_action.effect pass (*interruption_action.args) from _call_interruption_action_girlfriend_sleepover
                            $ del interruption_action
                        else: #default to fuck person if there isn't an interruption here.
                            call fuck_person(the_person, private = True) from _call_fuck_person_sleepover_gf_02
                            $ the_report = _return
                            $ girl_came += the_report.get("girl orgasms", 0)
                    elif renpy.random.randint(0,100) < ((the_person.get_opinion_score("taking control") + 1) * 15): #Baseline 15% chance, max 45% if she loves it
                        the_person "Mmm, lay back. I want to be on top this time..."
                        $ mc.change_locked_clarity(30)
                        "[the_person.possessive_title] pushes you on your back, you decide to take it easy for now and let her have her way with you."
                        call get_fucked(the_person, private = True)  from _call_get_fucked_sleepover_gf_03
                        $ the_report = _return
                        $ girl_came += the_report.get("girl orgasms", 0)
                    else:
                        call fuck_person(the_person, private = True) from _call_fuck_person_sleepover_gf_04
                        $ the_report = _return
                        $ girl_came += the_report.get("girl orgasms", 0)
                    if the_person.energy + energy_gain_amount < 30:
                        "[the_person.title] is panting. She is completely out of breath."
                        the_person "That's enough... oh my god, I can't move a muscle..."
                        the_person "I'm sorry honey, you wore me out! I need to be done for the night..."
                        $ done = True
                "Call it a night":
                    mc.name "Sorry, I need to get some sleep. I need to be done for tonight."
                    if girl_came:
                        the_person "Mmm, okay! That was nice."
                        "She kisses you and runs her hand over your back."
                    else:
                        $ the_person.change_stats(slut = -1, love = -1)
                        the_person "Well... Maybe next time you can get me off as well?"
                    $ done = True
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] turns her back to you. You cuddle up with her, wrapping your arm around her."
    mc.name "Goodnight..."
    the_person "Night..."

    $ the_person.next_day_outfit = the_person.outfit # stay in current outfit next day
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sleepover_01

    $ picked_event = get_random_girlfriend_morning_action(the_person)
    if picked_event:
        call expression picked_event.effect pass (*picked_event.args) from _call_picked_event_girlfriend_sleepover
        $ del picked_event
    else:
        "You wakeup, but [the_person.possessive_title] isn't there. She must have gotten up early and left."
        $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
        $ the_person.apply_planned_outfit()
    $ mc.business.event_triggers_dict["girlfriend_person"] = None
    $ mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = False  #Reset these so we can have another girlfriend sleepover.
    return

label girlfriend_wakeup_spooning_label(the_person):
    $ the_person.draw_person(position = "walking_away")
    "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
    "She is still sleeping, but her skin is setting off electric sparks everywhere it is touching yours."
    $ mc.change_locked_clarity(50)
    if the_person.has_large_tits():
        "Your hands cup and squeeze one of her [the_person.tits_description]. It's so full and hot, it feels so good in your hands."
    else:
        "Your hand cups one of her [the_person.tits_description]. It's so soft and warm, it feels good in your hand."
    the_person "Mmmmmmmm......"
    "[the_person.title] moans but doesn't stir. Maybe you could surprise her with a little good morning dicking."
    menu:
        "Try to slide yourself in":
            pass
        "Get ready for the day":
            "Thinking about your tasks for the day, you feel yourself get a bit anxious about wasting the morning."
            "You get up and head for bathroom to take a leak."
            "When you come back, [the_person.title] is awake."
            $ the_person.draw_person(position = "missionary")
            the_person "Good morning! I slept great."
            $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "stand3")
            "You both get ready for the day before heading out."
            $ clear_scene()
            return
    "Your cock is already hard, being up against [the_person.title], but she may not be fully wet yet."
    "You spit into your hand and rub it on your dick a few times, getting it lubed up."
    "When you feel good about it, you reach down and gently spread her cheeks apart. You position yourself at her entrance and give it a little push."
    "You are able to ease yourself about halfway in, but the angle makes it hard to get deep penetration."
    the_person "Oh [the_person.mc_title]. Mmmmmm..."
    "She's asleep, but is still responding to your touch. She must be a heavy sleeper! Or maybe she is just really worn out from last night..."
    "You give her a few gentle, smooth strokes. You can feel her pussy getting wetter with each stroke as her body begins to respond to the stimulation."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "With her legs closed and on her side like this, her pussy feels really tight. You can feel her gripping you every time you start to pull it out."
    $ mc.change_arousal(15)
    "Your reach around her with your hand and grab one of her tits. You start to get a little rough with her and pinch and pull at one of her nipples."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    the_person "Mmm, that feels so... wait... [the_person.mc_title]?"
    $ the_person.draw_person( position = "back_peek", emotion = "happy")
    "[the_person.possessive_title] wakes up and looks back at you smiling."
    the_person "Oh my god that feels so good... Baby you know how to give a wakeup call, holy fuck!"
    "Encouraged by her words, you reach your hand down and lift her leg, giving you a better angle for deeper penetration."
    "You pick up the pace and begin to fuck her earnestly."
    $ the_person.change_arousal(30) #70
    $ mc.change_locked_clarity(30)
    the_person "Oh yes that feels so good, fuck me good!"
    "She reaches down and holds her leg for you, freeing up your hand. You reach down between her legs and start to play with her clit."
    "Her ass is making smacking noises now, every time your hips drive your cock deep inside of her."
    $ the_person.change_arousal(40) #110
    the_person "Oh fuck, yes! YES!"
    $ mc.change_locked_clarity(30)
    "She shoves her ass back against you as she cums. Her helpless body quivers in delight. Her moans drive you even harder."
    $ the_person.have_orgasm(the_position = "back_peek")
    $ mc.change_arousal(20) #110
    mc.name "I'm gonna cum!"
    $ the_person.call_dialogue("cum_pullout")
    menu:
        "Cum inside":
            $ the_person.cum_in_vagina()
            $ the_person.draw_person( position = "back_peek")
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
            "You grab her hip and shove your cock deep and hold it there, cumming deep inside her. She moans and gasps with every spurt."
            $ the_person.call_dialogue("cum_vagina")
            "Satisfied, you slowly pull out of her."
            the_person "That's certainly one way to start the day... holy hell."
        "Pull out":
            $ the_person.cum_on_ass()
            $ the_person.draw_person( position = "back_peek")
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
            "You pull out at the last second. Large, thick ropes of cum rocket out of your cock, coating her ass."
            the_person "Oh my god... it's so warm!"
            "When you finish you lay back, admiring your painting skills."
            the_person "That's certainly one way to start the day..."
    $ the_person.reset_arousal()
    $ mc.arousal = 0
    "You lay in bed together for a little longer, but soon it is time to start the day."
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "stand4")
    "You both get ready for the day."
    the_person "Alright, I need to get some things done today. Thanks for the sleepover!"
    $ clear_scene()
    return

label girlfriend_roleplay_step_sister_label(the_person):
    #First, get the outfit, if we've picked one out for it.
    if (the_person.event_triggers_dict.get("stepsister_lingerie", None)):
        $ the_person.apply_outfit(the_person.event_triggers_dict.get("stepsister_lingerie", None))
    else:
        $ the_person.change_to_lingerie()
    #Now set nick names, etc
    $ the_person.roleplay_title_swap("Step Sis")
    $ the_person.roleplay_mc_title_swap("Step Brother")
    $ the_person.roleplay_possessive_title_swap("Your Step Sister")
    $ the_person.roleplay_personality_swap(lily_personality)

    if mc.business.event_triggers_dict.get("your_place", True):
        "Your girlfriend doesn't emerge from the bathroom right away, but eventually you hear her calling out."
        the_person "Help me! Someone help!"
        "You quickly get up and run into the bathroom."
        $ the_person.draw_person(position = "standing_doggy")
        the_person "Oh! [the_person.mc_title]? Is that you?"
        "The roleplaying has begun..."
        mc.name "It's me, [the_person.title]. What's going on?"
        "She is bent over and has her head in the sink."
        the_person "Oh thank god it's you [the_person.mc_title]! I somehow got my hair stuck! In the... err... sink!"
        mc.name "You got your hair stuck in the sink, again!?! How does this keep happening [the_person.title]?"
        "Her hips start to wiggle a bit as you approach her."
        $ mc.change_locked_clarity(30)
        the_person "I don't know! You've got to help me [the_person.mc_title]!"
        "She is laying it on pretty thick, but if it wasn't for her ass sticking up in the air, you might find this comical. Instead you are starting to get aroused."
        if the_person.vagina_available():
            "[the_person.possessive_title]'s ass, exposed and pointing at you, makes an enticing target. You run your hands along her hips and then grope it."
        else:
            "You walk over to [the_person.title]. You pull away the clothing between you and her ass."
            $ the_person.strip_outfit(top_layer_first = True, exclude_upper = True, exclude_lower = False, exclude_feet = True)
        $ the_person.change_arousal(15)
        $ mc.change_locked_clarity(30)
        the_person "Oh my gooooooddd... [the_person.mc_title], what are you doing back there?"
        "You dip a finger into her cunt."
        mc.name "Just checking the plumbing, [the_person.title]. Nothing to worry about..."
    $ the_person.roleplay_title_revert()
    $ the_person.roleplay_mc_title_revert()
    $ the_person.roleplay_possessive_title_revert()
    $ the_person.roleplay_personality_revert()
    return

label girlfriend_underwear_shopping_label(the_person):
    mc.name "Hey, I got an idea. Why don't we go shopping for some new lingerie? Spice things up in the bedroom a bit?"
    if the_person.sluttiness < 40:
        the_person "Oh! Ummm... I guess..."
        the_person "I mean, if you want me to. I suppose I could get something new to wear for you once in a while..."
    else:
        the_person "Oh! That sounds fun!"
        the_person "This will be great! You can tell me what you like, and then I'll know what to wear whenever I want to get your engine revving."
    "You walk with your girlfriend to the mall. Soon you are in the clothes store, walking around the underwear section."
    $ mc.change_location(clothing_store)
    $ mc.location.show_background()
    "Normally this would be a bit awkward by yourself, but with [the_person.title], it's not so bad..."
    the_person "Hmm, how should we do this? Want me to pick something out first? Or do you want to?"
    $ lingerie_outfit = None
    $ done = False
    while done == False:
        menu:
            "Have her pick something out":
                if lingerie_outfit == None:
                    the_person "Okay! I'll go with something I would normally wear, and you can let me know what you think, okay?"
                    mc.name "Sounds good. We can always make modifications to it or try something different if we need to."
                else:
                    mc.name "I think we should start over. Why don't you pick something out?"
                    the_person "Aww, I thought we were getting close. Ah well, I'll go pick something out."
                    $ the_person.draw_person(position = "kissing" )
                    "She gives you a quick kiss."
                    the_person "Thank you for being so patient!"
                    $ the_person.draw_person (position = "stand2")
                "You spend a few minutes with [the_person.possessive_title] as she looks through the different clothes racks. Eventually she picks something."
                "She takes your hand and you follow her to the dressing room."
                the_person "I'll be right back!"
                $ clear_scene()
                $ lingerie_outfit = build_lingerie_selection(the_person)
                $ the_person.apply_outfit(lingerie_outfit)
                $ the_person.draw_person()
                "The door opens, and there stands your girlfriend."
                the_person "Aha! What do you think?"
                "You check her out for a bit. Should you change it? Or start over?"
            "Modify current outfit" if lingerie_outfit != None:
                mc.name "I like it... but I'd like to make a few changes. Is that okay?"
                the_person "Okay! Grab what you think would look good, I'll be in the dressing room until you figure it out."
                $ clear_scene()
                "You pick out a few items to change her outfit a bit..."
                call screen outfit_creator(lingerie_outfit, outfit_type = "under")
                if _return != "Not_New":
                    $ lingerie_outfit = _return
                    "You pull out a few pieces of clothing to modify and take them to [the_person.possessive_title]. You set them on the top of the dressing room door."
                    mc.name "Here you go, try this."
                    if lingerie_outfit.slut_requirement <= the_person.sluttiness and lingerie_outfit.slut_requirement <= 40: #She likes it enough to try it on.
                        $ the_person.call_dialogue("lingerie_shopping_tame_response")
                    elif lingerie_outfit.slut_requirement >= 70 and lingerie_outfit.slut_requirement >= the_person.sluttiness:
                        $ the_person.call_dialogue("lingerie_shopping_wow_response")
                    else:
                        $ the_person.call_dialogue("lingerie_shopping_excited_response")
                    $ the_person.apply_outfit(lingerie_outfit, update_taboo = True)
                    $ the_person.draw_person()
                    the_person "What do you think?"
                    "You check her out for a bit. Should you change it? Or start over?"
                else:
                    mc.name "Sorry, I can't figure out a way to make it work. Why don't you get dressed really quick..."
                    the_person "Aww, okay..."
                    $ the_person.apply_outfit(the_person.planned_outfit)
                    $ the_person.draw_person()
                    $ lingerie_outfit = None
                    "She quickly gets dressed then emerges."
                    the_person "Okay... do you want to start over then?"

            "Pick something yourself":
                mc.name "Let me pick something out for you."
                if lingerie_outfit != None:
                    the_person "Awww, okay. I kinda like this one, but I don't mind letting you dress me up a bit more."
                    the_person "I'll get changed, and while I do that, you pick something out for me, okay?"
                else:
                    the_person "Oh! Okay! I'll hop in the dressing room. You pick something out for me and just set it on top of the door, okay?"
                $ clear_scene()
                ""
                "You pick out a few items to change her outfit a bit..."
                call screen outfit_creator(Outfit("New Outfit"), outfit_type = "under")
                if _return != "Not_New":
                    $ lingerie_outfit = _return
                    "You pick out an outfit and take the clothes to [the_person.possessive_title]. You set them on the top of the dressing room door."
                    mc.name "Here you go, try this."
                    $ the_person.apply_outfit(lingerie_outfit, update_taboo = True)
                    if lingerie_outfit.slut_requirement <= the_person.sluttiness and lingerie_outfit.slut_requirement <= 40: #She likes it enough to try it on.
                        $ the_person.call_dialogue("lingerie_shopping_tame_response")
                    elif lingerie_outfit.slut_requirement >= 70 and lingerie_outfit.slut_requirement >= the_person.sluttiness:
                        $ the_person.call_dialogue("lingerie_shopping_wow_response")
                    else:
                        $ the_person.call_dialogue("lingerie_shopping_excited_response")

                    $ the_person.draw_person()
                    the_person "What do you think?"
                    "You check her out for a bit. Should you change it? Or start over?"
                else:
                    mc.name "Sorry, I can't figure out a way to make it work. Why don't you get dressed really quick..."
                    the_person "Aww, okay..."
                    $ the_person.apply_outfit(the_person.planned_outfit)
                    $ the_person.draw_person()
                    $ lingerie_outfit = None
                    "She quickly gets dressed then emerges."
                    the_person "Okay... do you want to start over then?"

            "Buy this" if lingerie_outfit != None:
                $ done = True
                $ mc.change_locked_clarity(30)
                $ the_person.change_novelty(5)
            "Give up" if lingerie_outfit == None:
                $ done = True
    if lingerie_outfit == None:
        $ the_person.draw_person(emotion = "sad")
        the_person "Ah, okay. That's alright, maybe we could try again another time?"
        mc.name "Yeah, I think that might be for the better."
        $ the_person.change_stats(happiness = -3)
        "You head to the front of the store and walk out without buying anything."
    else:
        mc.name "That's it. That is exactly what I want."
        the_person "Ahh! Okay! Let me change out of it real quick and let's buy it."
        $ clear_scene()
        "[the_person.possessive_title] retreats into the dressing room for a minute."
        "Soon, she emerges, holding the items you've decided to purchase."
        $ the_person.apply_outfit(the_person.planned_outfit)
        $ the_person.draw_person()
        if the_person.has_taboo("roleplay"):
            pass
        else:
            "As you are walking up to the checkout counter, [the_person.title] asks you about the outfit."
            the_person "So... is this something you want me to wear when we like... do some roleplaying? Or just a sexy outfit?"
            "NOTE! Roleplay scenes are not yet implemented, but you can save outfits for them now..."
            menu:
                "Just a sexy outfit":
                    $ the_person.event_triggers_dict["favorite_lingerie"] = lingerie_outfit
                    the_person "Mmmm, okay! I'll wear this for you when I just want to be sexy!"
                "Roleplay: My baby girl":
                    $ the_person.event_triggers_dict["babygirl_lingerie"] = lingerie_outfit
                    if the_person.get_opinion_score("incest") > 0:
                        the_person "Oh! That sounds hot... You want to spank me while I call you daddy?"
                    else:
                        the_person "That's kinda weird... like those porn videos? I guess if you want to try it..."
                "Roleplay: My employee":
                    $ the_person.event_triggers_dict["employee_lingerie"] = lingerie_outfit
                    if the_person.is_employee():
                        the_person "Oh! But... I'm already your employee?"
                        mc.name "But what if you were a slutty employee who wasn't dating her boss and really needed a promotion."
                        the_person "Aaahhhh I see where you are going with this..."
                    else:
                        the_person "That's kinda weird... like those porn videos? I guess if you want to try it..."
                "Roleplay: My student":
                    $ the_person.event_triggers_dict["student_lingerie"] = lingerie_outfit
                    the_person "Ahhh, oh teacher? I'm sorry I forgot to study! What can I do to pass this class?"
                    mc.name "You've got exactly the right idea."
                "Roleplay: My ditzy stepsister" if not the_person.has_role(sister_girlfriend_role):
                    $ the_person.event_triggers_dict["stepsister_lingerie"] = lingerie_outfit
                    if the_person.get_opinion_score("incest") > 0:
                        the_person "Oh! That sounds hot... What are you going to do to me... step bro?"
                    else:
                        the_person "That's kinda weird... like those porn videos? I guess if you want to try it..."
        "You buy the outfit at the counter. It's a little pricey, but you're sure it'll be worth the investment."
        $ mc.business.change_funds(-150)
        $ the_person.add_outfit(lingerie_outfit, outfit_type = "under")
        the_person "Thanks, [the_person.mc_title]! This was fun!"
        if schedule_sleepover_available():
            the_person "So... want me to come over tonight? I'm not doing anything later..."
            menu:
                "Come over":
                    mc.name "I'd like to see this outfit in action. My place, say 9pm?"
                    the_person "Okay! See you then!"
                    $ the_person.event_triggers_dict["girlfriend_sleepover_lingerie"] = lingerie_outfit
                    $ schedule_sleepover_in_story(the_person)
                "Another time":
                    mc.name "Sorry, I'm running behind on work stuff. Another time, and soon."
                    the_person "Okay, I understand!"

    "You chat with your girlfriend for a bit, but soon it is time to go."
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title] embraces you and gives you a quick kiss before you part ways."
    $ mc.change_locked_clarity(10)
    $ clear_scene()
    $ del lingerie_outfit
    call advance_time from _call_advance_girlfriend_lingerie_shopping_01
    return

label girlfriend_quit_dikdok_label(the_person):
    mc.name "Hey [the_person.title], would you do something for me?"
    the_person "Sure, [the_person.mc_title], what do you need?"
    mc.name "I'm not very comfortable with you on DikDok, so I would prefer if you closed your account."
    the_person "Well, since I have you in my life, I don't see why not."
    $ the_person.remove_role(dikdok_role)
    "She pulls out her phone and closes her account right there."
    return
