#This file is to add new options to girlfriends. Ideas include: afternoon delight, my place / your place, sexting, clothes shopping.

init 2 python:
    girlfriend_morning_action_list = []     #Requirement functions can check mc.location to tell if its myplace/yourplace if necessary.
    girlfriend_sleepover_interruption_list = []     #Ideas, daughter/mother walk in, phone call,

    def girlfriend_myplace_yourplace_requirement(the_person):
        if schedule_sleepover_available():
            if time_of_day < 4:
                return True
            else:
                return "Too Late"
        else:
            return "You already have a sleepover arranged"
        return False

    def girlfriend_sleepover_requirement():
        if time_of_day == 4:
            return True
        return False

    def girlfriend_wakeup_spooning_requirement(the_person):
        return True

    girlfriend_sleepover_action = Action("Arrange a sleepover", girlfriend_myplace_yourplace_requirement, "girlfriend_myplace_yourplace_label",
        menu_tooltip = "Ask your girlfriend if she wants to sleep together tonight.")
    girlfriend_sleepover = Action("Have a sleepover", girlfriend_sleepover_requirement, "girlfriend_sleepover_label")

    girlfriend_wakeup_spooning = Action("Spooning wakeup", girlfriend_wakeup_spooning_requirement, "girlfriend_wakeup_spooning_label")
    girlfriend_wakeup_jealous_sister = Action("Jealous wakeup", girlfriend_wakeup_jealous_sister_requirement, "girlfriend_wakeup_jealous_sister_label")

    girlfriend_morning_action_list.append(girlfriend_wakeup_spooning)
    girlfriend_morning_action_list.append(girlfriend_wakeup_jealous_sister)




init 5 python:
    add_label_hijack("normal_start", "activate_girlfriend_role_enhancement")
    add_label_hijack("after_load", "activate_girlfriend_role_enhancement")

    def schedule_sleepover_in_story(the_person, your_place = True):
        mc.business.event_triggers_dict["girlfriend_person"] = the_person
        mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = True
        mc.business.event_triggers_dict["your_place"] = your_place
        mc.business.mandatory_crises_list.append(girlfriend_sleepover)
        return

    def schedule_sleepover_available():
        if mc.business.event_triggers_dict.get("girlfriend_sleepover_scheduled", False):
            return False
        return True

label activate_girlfriend_role_enhancement(stack):
    python:
        girlfriend_role.add_action(girlfriend_sleepover_action)

        execute_hijack_call(stack)
    return

label girlfriend_myplace_yourplace_label(the_person):
    $ wip_screen_show()
    mc.name "So, I'm kinda busy right now, but I thought that maybe later we could get together."
    the_person "Mmm, that sounds like fun. My place or yours?"
    menu:
        "My place":
            mc.name "Come over tonight, you can spend the night."
            the_person "Sounds great! Save some energy, we can make it a fun night."
            $ mc.business.event_triggers_dict["your_place"] = True
        "Your place":
            mc.name "How about your place? I'll bring a bottle of wine."
            the_person "Mmm, that sounds great! Bring a toothbrush, you can spend the night."
            $ mc.business.event_triggers_dict["your_place"] = False
    the_person "Anything else you need right now?"
    $ mc.business.event_triggers_dict["girlfriend_person"] = the_person
    $ mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = True
    $ mc.business.mandatory_crises_list.append(girlfriend_sleepover)
    return

label girlfriend_sleepover_label():
    $ wip_screen_show()
    $ the_person = mc.business.event_triggers_dict.get("girlfriend_person", None)
    if the_person == None:
        return
    #TODO give player the option to cancel the sleepover. she's probably sad.
    if mc.business.event_triggers_dict.get("your_place", True):
        "You go home for the night. Knowing that [the_person.title] is coming over, you quickly hop in the shower."
        $ mc.change_location(bedroom)
        $ mc.location.show_background()
        "When you finish, you go to your room. You make sure everything is nice and tidy."
        "Eventually, you get a text message."
        the_person "Hey, I'm here, let me in?"
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
        "[the_person.title] has changed into something much more comfortable..."
        mc.name "Damn, you look amazing..."
        "[the_person.title] slowly walks over to you, purposefully exaggerating her hip movements with each step."
        the_person "Thanks... you ready for some fun?"
    else:
        "It's time for your date with [the_person.title]. You swing by the store on the way and pick up a decent bottle of wine."
        $ mc.business.change_funds(-15)
        if the_person.home not in mc.known_home_locations:
            $ mc.known_home_locations.append(the_person.home)
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
            "Leave her drink alone.":
                "You decide to leave her wine alone."
        "You wait for another minute, when you hear the bedroom door open."
        $ the_person.change_to_lingerie()
        $ the_person.draw_person()
        "[the_person.possessive_title] has changed into some sexy clothes."
        the_person "Hey... bring the glasses in here!"
        "She disappears into her bedroom. You quickly grab the glasses and follow her in. She is sitting on the edge of her bed."
        $ the_person.draw_person(position = "sitting")
        "You hand her the wine glass. She takes a long sip."
        the_person "Mmm... what do you say we stay in and just cuddle tonight?"
        "She gives you a smirk. You can't help but frown at the thought of just cuddling..."
        the_person "Hah! Oh my god, you should have scene your face..."
        "She sets her wine down on her nightstand."
        the_person "Get over here! I'm ready for some fun!"
    call fuck_person(the_person, private = True) from _call_fuck_person_sleepover_gf_01

    $ the_report = _return

    $ done = False
    $ girl_came = False
    $ fuck_time_interrupted = False
    $ energy_gain_amount = 50 #Drops each round, representing your flagging endurance.
    while done == False:

        if the_report.get("girl orgasms", 0) > 5:
            $ the_person.change_love(5)
            $ the_person.change_slut_temp(1)
            the_person.char "Oh my god, you're making me cum my brains out... this is amazing..."
            "[the_person.title] lies down in bed and catches her breath."
            the_person.char "I think I can keep going... I'm gonna be sore in the morning though!"
            $ girl_came = True
        elif the_report.get("girl orgasms", 0) > 0:
            $ the_person.change_love(1)
            the_person "Ahhh, that was nice..."
            "[the_person.title] lies down in bed and catches her breath."
            the_person.char "I'm ready to go again if you are!"
            $ girl_came = True
        else:
            the_person.char "Whew, good job. Get some water and let's go for another!"
            "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
            "You hold [the_person.title] in bed while she caresses you and touches herself, keeping herself ready for you."

        if mc.energy < 40 and energy_gain_amount <= 20: #Forced to end the fuck date, so we set done to True.
            "The spirit is willing, but the flesh is spent. Try as she might [the_person.title] can't coax your erection back to life."
            if girl_came:
                the_person "Mmm, I wore you out! That was fun."
                "She kisses you and runs her hand over your back."
            else:
                $ the_person.change_love(-1)
                $ the_person.change_slut_temp(-1)
                the_person.char "Well I guess we're done then... Maybe next time you can get me off as well."
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
                    if renpy.random.randint(0,100) < 12 and not fuck_time_interrupted:
                        python:
                            fuck_time_interrupted = True    #Limit ourselves to one interruption per sleepover
                            possible_action_list = []
                            for interruption_scene in girlfriend_sleepover_interruption_list:
                                if interruption_scene.is_action_enabled(the_person): #Make sure requirement functions take the person as an arg
                                    possible_action_list.append(interruption_scene) #Build a list of valid crises from ones that pass their requirement.
                        $ interruption_action = get_random_from_list(possible_action_list)
                        if interruption_action:
                            $ interruption_action.call_action()
                        else: #default to fuck person if there isn't an interruption here.
                            call fuck_person(the_person, private = True, report_log = the_report) from _call_fuck_person_sleepover_gf_02
                    elif renpy.random.randint(0,100) < ((the_person.get_opinion_score("taking control") + 1) * 15): #Baseline 15% chance, max 45% if she loves it
                        the_person "Mmm, lay back. I want to be on top this time..."
                        "You pushes you on your back, you decide to take it easy for now and let her have her way with you."
                        call get_fucked(the_person, private = True, report_log = the_report)  from _call_get_fucked_sleepover_gf_03
                    else:
                        call fuck_person(the_person, private = True, report_log = the_report) from _call_fuck_person_sleepover_gf_04
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
                        $ the_person.change_love(-1)
                        $ the_person.change_slut_temp(-1)
                        the_person.char "Well... Maybe next time you can get me off as well?"
                    $ done = True
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] turns her back to you. You cuddle up with her, wrapping your arm around her."
    mc.name "Goodnight..."
    the_person "Night..."

    $ the_person.next_day_outfit = the_person.outfit # stay in current outfit next day
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sleepover_01
    python:
        possible_action_list = []
        for wakeup_scene in girlfriend_morning_action_list:
            if wakeup_scene.is_action_enabled(the_person): #Make sure requirement functions take the person as an arg
                possible_action_list.append(wakeup_scene) #Build a list of valid crises from ones that pass their requirement.
    $ wakeup_action = get_random_from_list(possible_action_list)
    if wakeup_action:
        $ wakeup_action.call_action(the_person)
    else:
        "You wakeup, but [the_person.possessive_title] isn't there. She must have gotten up early and left."
        $ the_person.planned_outfit = the_person.wardrobe.decide_on_outfit2(the_person) # choose a new outfit for the day
        $ the_person.apply_planned_outfit()
    $ mc.business.event_triggers_dict["girlfriend_person"] = None
    $ mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = False  #Reset these so we can have another girlfriend sleepover.
    return

label girlfriend_wakeup_spooning_label(the_person):
    $ the_person.draw_person(position = "walking_away")
    "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
    "She is still sleeping, but her skin is setting off electric sparks everywhere it is touching yours."
    if the_person.has_large_tits():
        "Your hands cup and squeeze one of her breasts. It's so full and hot, they feel so good in your hands."
    else:
        "Your hand cups one of her breasts. It's so perky and warm, it feels good in your hand."
    the_person.char "Mmmmmmmm......"
    "[the_person.title] moans but doesn't stir. Maybe you could surprise her with a little good morning dicking."
    menu:
        "Try to slide yourself in":
            pass
        "Get ready for the day":
            "Thinking about your tasks for the day, you feel yourself get a bit anxious about wasting the morning."
            "You get up and head for bathroom to take a leak."
            "When you come back, [the_person.title] is awake."
            $ the_person.draw_person(position = "missionary")
            the_person.char "Good morning! I slept great."
            $ the_person.planned_outfit = the_person.wardrobe.decide_on_outfit2(the_person) # choose a new outfit for the day
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "stand3")
            "You both get ready for the day before heading out."
            $ clear_scene()
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
    $ the_person.draw_person( position = "back_peek", emotion = "happy")
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
    $ the_person.have_orgasm()
    $ mc.change_arousal(20) #110
    mc.name "I'm gonna cum!"
    $ the_person.call_dialogue("cum_pullout")
    menu:
        "Cum inside":
            $ the_person.cum_in_vagina()
            $ the_person.draw_person( position = "back_peek")
            "You grab her hip and shove your cock deep and hold it there, cumming deep inside her. She moans and gasps with every spurt."
            $ the_person.call_dialogue("cum_vagina")
            "Satisfied, you slowly pull out of her."
            the_person.char "That's certainly one way to start the day... holy hell."
        "Pull out":
            $ the_person.cum_on_ass()
            "You pull out at the last second. Large, thick roaps of cum rocket out of your cock, coating her ass."
            $ the_person.draw_person( position = "back_peek")
            the_person "Oh my god... its so warm!"
            "When you finish you lay back, admiring your painting skills."
            the_person.char "That's certainly one way to start the day..."
    $ the_person.reset_arousal()
    $ mc.arousal = 0
    "You lay in bed together for a little longer, but soon it is time to start the day."
    $ the_person.planned_outfit = the_person.wardrobe.decide_on_outfit2(the_person) # choose a new outfit for the day
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "stand4")
    "You both get ready for the day."
    the_person.char "Alright, I need to get some things done today. Thanks for the sleepover!"
    $ clear_scene()
    return
