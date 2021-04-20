#Original file by Badrabbit
# init -1 python:
#     cousin.event_triggers_dict["teach_level"] =-1
#     cousin.event_triggers_dict["oral_chance"] = 0



init 2 python:
    def cousin_role_foreplay_position_filter(foreplay_positions):
        filter_out = [tit_fuck]
        if the_person.event_triggers_dict.get("blackmail_level",-1) > 1:
            return True
        elif foreplay_positions[1] in filter_out:
            return False
        else:
            return True
        return True

    def cousin_role_oral_position_filter(oral_positions):
        filter_out = [SB_sixty_nine, blowjob, deepthroat]
        if the_person.event_triggers_dict.get("blackmail_level",-1) > 1:
            return True
        elif oral_positions[1] in filter_out1:
            return False
        else:
            return True

    def cousin_role_vaginal_position_filter(vaginal_positions):
        if the_person.event_triggers_dict.get("blackmail_level",-1) > 1:
            return True
        else:
            return False

    def cousin_role_anal_position_filter(anal_positions):
        if the_person.event_triggers_dict.get("blackmail_level",-1) > 1:
            return True
        else:
            return False

# init 2:
#     python:
#         cowgirl_cunnilingus.scenes.append("SAG_1")

init 2 python:
    #config.label_overrides["aunt_intro_phase_two_label"] = "SAG_aunt_intro_phase_two_label"
    #config.label_overrides["grope_shoulder"] = "SAG_grope_shoulder"
    #config.label_overrides["aunt_intro_phase_final_label"] = "aunt_intro_phase_final_label_enhanced"

    def gabrielle_visit_requirement():
        if mc_at_home() and cousin.sluttiness >= 15:
            return True
        return False

# I decided not to implement this coverup of the base game moveout scene, but left the code intact to make it easy to implement.
label aunt_intro_phase_final_label_enhanced():
    $ the_person = cousin
    $ the_person.pubes_style = shaved_pubes
    $ renpy.scene("Active")
    python:
        for clothing in the_person.outfit.get_lower_ordered():
            the_person.outfit.remove_clothing(clothing)
    $ the_person.draw_person(position = "kneeling1")
    $ bedroom.show_background()
    the_person "Wake up, [the_person.mc_title]."
    if the_person.sex_record.get("Cunnilingus", 0) < 2:
        "You wake up to the sight of a shaved pussy in your face."
    elif the_person.sex_record.get("Cunnilingus", 0) < 5:
        "You wake up to the increasingly familiar sight of [the_person.possessive_title]'s shaved pussy in your face."
    else:
        "You wake up to the familiar sight and faint smell of [the_person.possessive_title]'s pussy."
        $ the_person.change_arousal (10)
    "You are lying flat on your back. [the_person.title] is on top of you, kneeling with one knee to either side of your head. Your arms are pinned to the bed by her shins. She is holding onto your head with both of her hands."
    the_person "Now, get to it - my pussy's not going to lick itself."
    "Your cousin lowers herself onto your mouth, bringing her clit into contact with your tongue."
    "Your tongue makes contact directly with her clit as you start to lick her."
    call get_fucked(the_person, the_goal = "get off", private= True, start_position = cowgirl_cunnilingus, skip_intro = True, allow_continue = False) from GIC_SAG03
    $ the_person.change_obedience(-10)
    $ the_report = _return
    "Your cousin lifts herself up slightly off your face. She looks down at you and starts to speak."
    if the_report.get("girl orgasms",0) > 0:
        the_person "Good boy."
    the_person "Now, it's time to say good bye. My mom and I are moving out."
    if cousin.event_triggers_dict.get("teach_level", -1) == 0:
        the_person "The offer of lessons still stands."
        if mc.sex_skills["Oral"] < 5:
            the_person "You know you need them."
            if mc.sex_skills["Oral"] < 2:
                the_person "Like really. I honestly didn't realise people were as bad as you are."
        elif mc.sex_skills["Oral"] > 4 and mc.sex_skills["Oral"] < 8:
            the_person "You're better than you were but I could still teach you a good few things."
        else:
            the_person "Honestly, you're a lot better than you were but I could still teach you a good few things."
    elif cousin.event_triggers_dict.get("teach_level", -1) > 90:
        the_person "Honestly, I'm probably going to miss this."
    else:
        the_person "You still need lessons."
        if mc.sex_skills["Oral"] < 5:
            the_person "You know you need them."
        if mc.sex_skills["Oral"] > 4 and mc.sex_skills["Oral"] < 8:
            the_person "You're better than you were but I could still teach you a good few things."
        else:
            the_person "Honestly, you're a lot better than you were but I could still teach you a good few things."
    "Your cousin climbs off you and starts to leave."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(emotion = "happy", position = "back_peek")
    the_person "Later, loser."
    $ clear_scene()
    $ kitchen.show_background()
    "You stay in bed for a bit then get up for breakfast. You find [aunt.title] and [mom.title] in the kitchen, both awake earlier than normal."
    $ the_group = GroupDisplayManager([mom, aunt], aunt)
    $ the_group.draw_group(position = "sitting")
    aunt "Good morning [aunt.mc_title]."
    "She smiles at you warmly and sips coffee from a mug. [mom.possessive_title] is drinking a cup of tea across the table from her."
    mc.name "Morning. You two are up early."
    aunt "All the paperwork for my new apartment has been finished, so [cousin.title] and I will be moving out today."
    $ the_group.draw_person(mom, position = "sitting")
    mom "We're just finishing our drinks, then they'll be heading out."
    $ the_group.draw_person(aunt, position = "sitting")
    if aunt.event_triggers_dict.get("moving_apartment", 0) == 0:
        #Did nothing
        aunt "I was going to wake you up before I left, of course. You've been so busy, I barely got a chance to see you."
        $ the_group.draw_person(mom, position = "sitting")
        mom "You're welcome to come over and visit any time [aunt.title]. I'll make sure [mom.mc_title] takes a break to come visit his family."

    elif aunt.event_triggers_dict.get("moving_apartment") in [1,2,3]:
        #Did some stuff
        aunt "I was going to wake you up before I left, of course. I want to say thank you again for helping us move our things over."
        $ the_group.draw_person(mom, position = "sitting", emotion = "happy")
        $ mom.change_love(2)
        $ mom.change_happiness(5)
        mom "I'm glad you were able to find some time to help them out [mom.mc_title]. I'm proud of you."

    else:
        #Did everything
        aunt "I was going to wake you up before I left, of course. I needed to say thank you again for the huge amount of help you gave us."
        $ the_group.draw_person(mom, position = "sitting", emotion = "happy")
        $ mom.change_love(3)
        $ mom.change_happiness(8)
        mom "[aunt.title] has been telling me all morning how helpful you've been. I'm so proud of you [mom.mc_title]."
        $ the_group.draw_person(aunt, position = "sitting", emotion = "happy")
        aunt "He was a godsend, he really was."

    $ the_group.draw_person(aunt, position = "sitting", emotion = "happy")
    aunt "Come on [aunt.mc_title], sit down and join us for a few minutes."
    "You join [aunt.possessive_title] and [mom.possessive_title] while they finish their drinks and chat with each other."
    "[aunt.title] certainly seems happier now than she did a week ago when she arrived."
    $ clear_scene()
    $ the_group = GroupDisplayManager([mom, lily, aunt, cousin], aunt)
    $ the_group.draw_group()
    "When her drink is done [aunt.title] collects [cousin.possessive_title] and heads to the door. [lily.title] joins you as you say goodbye."
    $ the_group.draw_person(aunt, emotion = "happy")
    aunt "Thank you all for giving us a place to go. You're welcome to visit us any time. Just drop by."
    "[cousin.title] looks at you and shakes her head from behind her mother."
    $ the_group.draw_person(mom, emotion = "happy")
    mom "And you two are always welcome here. Call if you need anything."
    $ the_group.draw_person(aunt)
    aunt "I will. Thanks sis."
    "[mom.possessive_title] and [aunt.possessive_title] hug each other and don't let go for a long while."
    $ clear_scene()
    $ lily.draw_person()
    "When the moment has passed [mom.title] walks them out to the driveway, leaving you alone with [lily.possessive_title]."
    lily "I'm going to miss them. I think [cousin.title] and I were really getting along."
    mc.name "Really?"
    lily "Yeah! She may not talk much but she's a great listener. I hope she stays in touch."
    "You shrug and head back to your room to get ready for the day."

    python:
        aunt.event_triggers_dict["moving_apartment"] = -1 #Disables the event in their action list so you can't help them move out once they're already moved out.
        aunt.home = aunt_bedroom # Set their homes to the new locations
        cousin.home = cousin_bedroom

        aunt_bedroom.visible = True
        aunt_apartment.visible = True
        cousin_bedroom.visible = True

        #Your aunt is a homebody, but your cousin goes wandering during the day (Eventually to be replaced with going to class sometimes.)
        aunt.set_schedule(aunt.home, times = [0, 1, 4])
        aunt.set_schedule(aunt_apartment, times = [2, 3])

        cousin.set_schedule(cousin.home, times = [0, 4])
        cousin.set_schedule(None, times = [1, 2, 3])

        add_cousin_at_house_phase_one_action()

        add_aunt_share_drink_intro()
        the_group = None
    return

label SAG_grope_shoulder(the_person):
    "You put your hand on [the_person.title]'s shoulder as you make small talk."
    if cousin_role in the_person.special_role:
        $ ran_num = renpy.random.randint(0,100)
        if the_person.effective_sluttiness("touching_body") < 5:
            "She shoots you a cold look and takes a step back."
            $ the_person.change_love(-1)
            the_person "What in the fuck do you think that you are doing?"
        elif mc.location.get_person_count() > 1:
            "She shoots you a cold look and takes a step back."
            $ the_person.change_love(-1)
            the_person "Not with other people here, perv."
        elif (ran_num - 80 ) > the_person.arousal:
            "She shrugs her shoulders displacing your hand."
            the_person "Yeh, I'm just not feeling it."
        else:
            if the_person.effective_sluttiness("touching_body") < 10: #This branch is both a warning to the player not to push things too far and the way they increase sluttiness.
                "She glances uncertainly at your hand, but you give her a warm smile and prompt her to continue the conversation."
                "Once you have her talking again you start to gently massage her shoulder."
                "[the_person.possessive_title] seems uncomfortable but doesn't leave immediately."
                $ the_person.change_love(-1)
                $ the_person.change_slut_temp(2)
                $ the_person.change_arousal(5)

            else:
                "[the_person.possessive_title] doesn't seem to mind at all as you start to gently massage her shoulder."

            menu:
                "Move your hand to her waist\n-5 {image=gui/extra_images/energy_token.png}" if the_person.energy >=5:
                    return True

                "Move your hand to her waist\n-5 {image=gui/extra_images/energy_token.png} (disabled)" if the_person.energy < 5:
                    pass

                "Stop touching her":
                    return False

        if the_person.event_triggers_dict.get("blackmail_level", -1) >= 1:
            menu:
                "Remind her that you could blackmail her if you wanted to.":
                    $ the_person.change_love(-1)
                    "She sighs slightly as you move your hand down her body to her waist."
                    return True
                "Leave it.":
                    return False

        else:
            return False

    elif the_person.effective_sluttiness("touching_body") < 5:
        #Failure, and you've pissed her off in the process.
        "She shoots you a cold look and takes a step back."
        $ the_person.change_love(-1)
        the_person "I'm sorry, I'd prefer if you didn't touch me without permission."
        return False

    else:
        if the_person.effective_sluttiness("touching_body") < 10: #This branch is both a warning to the player not to push things too far and the way they increase sluttiness.
            "She glances uncertainly at your hand, but you give her a warm smile and prompt her to continue the conversation."
            "Once you have her talking again you start to gently massage her shoulder."
            "[the_person.possessive_title] seems uncomfortable but doesn't leave immediately."
            $ the_person.change_love(-1)
            $ the_person.change_slut_temp(2)
        else:
            "[the_person.possessive_title] doesn't seem to mind at all as you start to gently massage her shoulder."

        menu:
            "Move your hand to her waist\n-5 {image=gui/extra_images/energy_token.png}" if the_person.energy >=5:
                return True

            "Move your hand to her waist\n-5 {image=gui/extra_images/energy_token.png} (disabled)" if the_person.energy < 5:
                pass

            "Stop touching her":
                return False

label SAG_aunt_intro_phase_two_label():
    #They show up at your house in the morning. Quick introductions with everyone.
    "In the morning [mom.possessive_title] wakes you up early with a knock on your door."
    mom "[mom.mc_title], I just got a call, your aunt and cousin are on their way over. Get ready so you can help move their stuff inside."
    $ kitchen.show_background()
    "You get up, get dressed, and head to the kitchen to have some breakfast. [mom.possessive_title] paces around the house nervously, looking for things to tidy."
    $ hall.show_background()
    "Finally the doorbell rings and she rushes to the door. You and [lily.title] join her in the front hall as she greets your guests."
    $ mom.draw_person()
    mom "[aunt.name], I'm so glad you made it!"
    $ aunt.draw_person()
    aunt "[mom.name]!"
    "[aunt.title] lets out an excited, high pitched yell and rushes forward to hug [mom.possessive_title]."
    aunt "Thank you so much for taking us in. It means the world to me and [cousin.title]."
    $ cousin.draw_person()
    "[mom.possessive_title] breaks the hug. Your cousin, [cousin.title], sits outside the door on a suitcase, idly scrolling through her phone."
    mom "How are you doing [cousin.title]? Holding up okay?"
    "She shrugs and doesn't take her eyes off her phone."
    cousin "Eh. Fine..."
    $ aunt.draw_person()
    aunt "She's thrilled, really. Now who are these two little rascals I see?"
    "[aunt.possessive_title] steps into the house and throws her arms wide, pulling you and your sister in to a hug."
    aunt "I mean, it must be [mc.name] and [lily.title], but you're both so much bigger than I remember!"
    "She hugs you both tight and then lets go. [aunt.title] looks at you in particular and laughs."
    aunt "I remember when you were just a little baby, and now you're a full grown man. Oh no, I'm showing my age, aren't I. Hahaha."
    "She laughs and turns back to grab her things. [cousin.title] sighs loudly outside and rolls her eyes."
    aunt "Now [mom.name], where should I bring my things?"
    $ mom.draw_person()
    mom "Just follow me, I'll show you around. We got everything set up as soon as we heard the news."
    "[mom.possessive_title] leads [aunt.possessive_title] into the house. When they're gone [lily.possessive_title] takes a step towards [cousin.title]."
    $ lily.draw_person()
    lily "Hi [cousin.title], it's nice to see you again. I don't think we've talked since we were little kids."
    $ cousin.draw_person()
    cousin "Yep..."
    "There's a long period of awkward silence."
    $ lily.draw_person()
    lily "... Right. Well I'm sure we'll get along while you're staying with me."
    "[aunt.possessive_title] calls from further inside the house."
    aunt "[cousin.name], sweetheart, you should come see your room! I'm sure [lily.name] and [mc.name] will help bring your stuff in."
    $ cousin.draw_person()
    "[cousin.possessive_title] gets up from her suitcase seat, picks up her smallest bag, and walks inside."
    cousin "Thanks for the help."
    $ lily.draw_person()
    "[lily.title] glances at you and rolls her eyes dramatically. The two of you grab more luggage and start hauling it inside."
    "After a few minutes all of the suitcases have been moved to where they need to go."
    $ aunt.draw_person()
    aunt "Thank you two so much, you're such sweethearts. Here's something for all your hard work."
    $ aunt.change_love(2)
    $ mc.business.funds += 20
    "[aunt.possessive_title] finds her purse, pulls out her wallet, and hands you and [lily.possessive_title] $20."
    aunt "Now I think your mother wanted to talk with me. I'm sure you both have busy days, so don't let me keep you!"
    #Their temporary homes are at your place. Later we will restore them to their normal homes.
    $ add_aunt_phase_three_action()
    $ add_cousin_phase_one_action()
    $ gabrielle_visit = Action("gabrielle visit",gabrielle_visit_requirement,"gabrielle_visit_label")
    $ mc.business.mandatory_morning_crises_list.append(gabrielle_visit) #Add the event here so that it pops when the requirements are met.
    $ renpy.scene("Active")
    return

label gabrielle_visit_label():
    $ the_person = cousin
    if the_person.event_triggers_dict.get("teach_level", -1) == -2:
        return
    $ the_person.pubes_style = shaved_pubes.get_copy()
    $ renpy.scene("Active")
    python:
        for clothing in the_person.outfit.get_lower_ordered():
            the_person.outfit.remove_clothing(clothing)
    $ the_person.draw_person(position = "kneeling1")
    $ bedroom.show_background()
    "You wake up to the sight of a shaved pussy in your face."
    "You are lying flat on your back. [the_person.title] is on top of you, kneeling with one knee to either side of your head. Your arms are pinned to the bed by her shins. She is holding onto your head with one hand."
    $ the_person.opinions["taking control"] = [2, True]
    mc.name "What the fuck?"
    "Gabrielle lifts one of her index fingers to her lips."
    the_person "Shhh! It's early - you don't want to wake everybody up."
    if the_person.home == cousin_bedroom:
        mc.name "How did you even get in here?"
        the_person "I still have my key from when I lived her."
    "She tightens her grip on your head with her hand."
    the_person "Wondering what's going on?"
    the_person "I was feeling horny and needed some release."
    the_person "I bet your rug-muncher of a sister would love this but girls just don't do it for me..."
    the_person "And I saw the way that you were looking at me the other day, perv."
    menu:
        "Force her off":
            mc.name "Fuck off. I'm not doing that."
            "You use your strength to force her off. She walks out your door."
            the_person "Didn't realize you didn't like girls. Whatever nerd, your loss."
            $ the_person.draw_person(emotion = "happy", position = "back_peek")
            $ the_person.apply_planned_outfit()
            $ cousin.event_triggers_dict["teach_level"] = -2
            return
        "Give in":
            pass
    if the_person.has_taboo("vaginal sex"):
        the_person "This is probably the closest you'll get to touching a real girl."
    if the_person.has_taboo("licking_pussy"):
        the_person "Now, let's see if you're any good at this."
    else:
        the_person "Now, get to it - my pussy's not going to lick itself."
    "Your cousin lowers herself onto your mouth, bringing her clit into contact with your tongue."
    $ the_person.break_taboo("bare_pussy")
    $ the_person.break_taboo("licking_pussy")
    "Your tongue makes contact directly with her clit as you start to lick her."
    $ the_person.opinions["getting head"] = [2, True]
    the_person "Ohh!"
    call get_fucked(the_person, the_goal = "get off", private= True, start_position = cowgirl_cunnilingus, skip_intro = True, allow_continue = False) from GIC_SAG01
    $ the_person.change_obedience(-10)
    $ the_report = _return
    "Your cousin lifts herself up slightly off your face. She continues to hold the hair of your head in her hands as she looks at you and starts to speak."
    if the_report.get("girl orgasms",0) > 0:
        the_person "Good boy."
    the_person "Now say thank you."
    menu:
        "Thank you.":
            the_person "Good."
            $ the_person.change_obedience(-2)
        "Fuck off!":
            "Quick as a flash your cousin lets go with one of her hands and slaps you hard on the face, then goes back to holding your head."
            the_person "Don't ever talk to me like that."
            $ the_person.change_love(-2)
            $ the_person.change_slut_temp(5)
            $ the_person.change_arousal(10)
            "Your cousin is surprisingly flexible as she leans down and licks your face. She straightens up and laughs."
            the_person "This'll be fun."
    if the_report.get("girl orgasms",0) > 0:
        the_person "So, yeh."
        the_person "I had fun but you suck at giving head."
    else:
        the_person "So, yeh."
        the_person "You suck at giving head."
    the_person "... and like not in a good way. You might think sucking was good but not this time."
    the_person "U...S...U...C...K..."
    mc.name "Hey! That's not..."
    if mc.sex_skills["Oral"] < 2:
        the_person "Shut it. We both know it's true."
        the_person "You need help - serious help."
    else:
        the_person "You've got some skills but you need help to get better."
        the_person "Practicising on your pillow can only take you so far - you need a real girl - Pinnochio."
        mc.name "I don't think that... "
        the_person "Whatever, nerd."
    the_person "Anyway, that's where I come in."
    the_person "You need a real pussy to practice on and it so happens that I have one."
    the_person "You need lessons and I can teach you - it won't be free but it'll be worth it - trust me."
    the_person "I think $100 sounds fair."
    mc.name "Wait a minute, so I get what, exactly?"
    the_person "You get to lick a real life pussy of a real life girl who is totally out of your league - obviously."
    mc.name "Ha, ha. Seriously though."
    the_person "You get the chance to learn from the best."
    the_person "I was at a Catholic boarding school before this and believe me - what I don't know about licking a girl out isn't worth knowing."
    the_person "I don't know how often I'll be needing your services like this."
    the_person "If you get good enough this sort of visit might not be entirely one way - if you get my meaning."
    the_person "It wouldn't be the worst thing if you learnt how to do it the way I like it, for either of us."
    the_person "You scratch my back, I scratch yours. You get good at eating my pussy...well"
    "Your cousin climbs off you, gets dressed and starts to leave."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(emotion = "happy", position = "back_peek")
    the_person "You think about it, Cunt Munch - best $100 you'll ever spend."
    $ the_person.set_mc_title("Cunt Munch")
    $ cousin.event_triggers_dict["teach_level"] = 0
    # $ gabrielle_house = 1
    "As it is still early you fall back asleep."
    return


label cousin_teach_action_label(the_person):
    if the_person.sex_record.get("Cunnilingus", 0) < 5:
        mc.name "I've got $100."
        the_person "Good for you - did you save up your pocket money?"
        mc.name "Why are you such a bitch?"
        the_person "Why are you such a dick?"
        $ the_person.change_love(-1)
        $ the_person.change_slut_temp(2)
        $ the_person.change_arousal(5)
    else:
        pass
    mc.name "So how about a lesson?"

    if the_person.energy <25:
        the_person "I'm a bit tired - maybe another time."
        return
    elif renpy.random.randint(0,100) < 80:
        the_person "OK."
        pass
    else:
        the_person "Yeh well, I'm not feeling like it."
        $ the_person.change_obedience(-2)
        menu:
            "OK":
                the_person "Next time, loser."
                $ the_person.change_obedience(-2)
                return
            "Try to persuade her.":
                mc.name "Come on. You'll have a good time and make some easy cash."
                if renpy.random.randint(0,100) < the_person.sluttiness + the_person.love + (mc.sex_skills["Oral"]*10) + (mc.charisma * 5):
                    the_person "OK."
                elif renpy.random.randint(0,100) < 50:
                    the_person "$200"
                    mc.name "What?"
                    the_person "I've got other stuff to do but if you pay me double then I'll clear my schedule."
                    menu:
                        "Pay for it\n{color=#ff0000}{size=18}Costs: $5000{/size}{/color}" if mc.business.funds >= 200:
                            the_person "Alright then, let's do this."
                            $ mc.business.funds += -100
                            $ the_person.change_obedience(-2)
                        "Pay for it\n{color=#ff0000}{size=18}Requires: $5000{/size}{/color} (disabled)" if mc.business.funds < 200:
                            return
                        "Don't.":
                            the_person "Your loss. See ya."
                            return
                else:
                    the_person "No means no, rape-boy."
                    return

    $ mc.business.funds += -100
    if mc.location.get_person_count() > 1:
        the_person "Let's go somewhere a bit quieter first."
        "You manage to find a comparatively secluded spot."
    the_person "Alright! Let's go!"
    "She quickly takes off some clothes to give you easy access."
    $ the_person.strip_outfit(position = "stand3", exclude_upper = True)
    if cousin.event_triggers_dict.get("oral_chance", 0) == -999:
        mc.name "I feel like I'm not making progress lately."
        the_person "You might be right."
        if the_person.love < 0:
            mc.name "What?"
            the_person "You might be right - dick for brains - don't get too used to me saying that though."
        the_person "It's time to take the training wheels off."
        the_person "I'll let you go down on me - however you think best - and I'll record you on my phone."
        the_person "Then we can watch the recording back together, while I tell you what you're doing wrong."
        the_person "I want you to do something for me though."
        mc.name "What?"
        if the_person.obedience > 120:
            the_person "I want to switch it up for a change."
        the_person "Call me Mistress, let me call you slave, keep going until you are exhausted..."
        the_person "...and when you are finished look up at the phone and thank me, your mistress, for being permitted to eat my declicious cunt."
    elif cousin.event_triggers_dict.get("oral_chance", 0) == -1000:
        the_person "I've told you what I want you to do. I don't think that anything else will help."

    if cousin.event_triggers_dict.get("oral_chance", 0) == -999 or cousin.event_triggers_dict.get("oral_chance", 0) == -1000:
        menu:
            "OK (do it properly).":
                the_person "Cool. Now strip naked and stand there."
                "[the_person.title] gets her phone out and starts recording you."
                "You strip naked."
                "[the_person.title] lies down and opens her legs."
                $ the_person.draw_person(position = "missionary")
                the_person "Now, Slave. Come and eat your Mistresses cunt."
                "[the_person.title] opens her legs wide and beckons you forward with her finger."
                "She mouths the words 'Yes, Mistress'."
                mc.name "Yes, Mistress."
                "You do as you are told trying your best. You draw on everything that [the_person.possessive_title] has taught you."
                "You manage to give [the_person.title] multiple orgasms from your efforts."
                "Eventually, exhausted, you raise your head from between [the_person.title] legs."
                mc.name "Thank you, Mistress."
                the_person "For what, Slave?"
                mc.name "For being permitted to eat your delicious cunt, Mistress."
                "[the_person.title] smiles broadly and noticeably pushes a button on her phone stopping the recording. She seems to play about with the phone for a bit before sitting up and patting the floor beside her."
                the_person "Come here."
                "You go over and sit beside [the_person.possessive_title]"
                the_person "Now, let's review."
                "[the_person.title] goes through the video of you eating her out."
                "She pauses the video at vartious stages and points out what's wrong with your technique - and more surprisingly - what you're doing right."
                if perk_system.has_stat_perk("Starbuck Oral Bonus"):
                    the_person "This bit here. That was good, but I didn't teach you it - I would have remembered if I did."
                    mc.name "Well, maybe I'm just naturally talented."
                    the_person "Yeah - right. Anyway..."
                    "[the_person.title] goes back to reviewing your performance."
                else:
                    pass
                "When you are finished you feel that you have made a break-through and that you have learned everything that [the_person.title] can teach you."
                $ perk_system.add_stat_perk(Stat_Perk(description = "Increase to oral skill after learning all your cousin can teach you. + 1 Oral Skill", oral_bonus = 1, bonus_is_temp =False), "Gabrielle Oral Bonus")
                $ cousin.event_triggers_dict["teach_level"] = 99
                the_person "That's it. I don't think that I can teach you anymore. This has been ..."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person(emotion = "happy", position = "back_peek")
                "[the_person.title] gets up, puts her phone away and gets dressed."
                $ mc.location.show_background()
                the_person "See you around, nerd."
                call advance_time from _call_advance_time_Gab_oral_01

            "OK (piss her off).":
                the_person "Cool. Now strip naked and stand there."
                "[the_person.title] gets her phone out and starts recording you."
                "You go to take off your top but instead roll your hands forward flicking your middle fingers on both hands at [the_person.title]."
                mc.name "Fuck off."
                the_person "No - fuck you. Easiest money I ever earned."
                $ the_person.change_love(-1)
                "[the_person.title] gets back up, puts her phone away and gets dressed."
                $ cousin.event_triggers_dict["oral_chance"] = -1000

            #"Blackmail her to avoid her request.":
            #    mc.name "How about your mom doesn't find out what you've been doing and I don't do what you say."
            #    $ the_person.change_love(-1)
            #    return
            "No.":
                the_person "OK, but I'm not seeing how you can improve without this sort of thing..."
                "[the_person.title] gets back up, puts her phone away and gets dressed."
                $ cousin.event_triggers_dict["oral_chance"] = -1000

        $ the_person.apply_planned_outfit() #TODO: get dressed
        $ the_person.draw_person()
        $ mc.location.show_background()
        $ clear_scene()


    else:
        $ the_person.draw_person(position = "kneeling1")
        call fuck_person(the_person, start_position = teach_oral, start_object = mc.location.get_object_with_name("floor"), skip_intro = False, position_locked = True) from _call_fuck_person_SAG1234
        $ the_report = _return
        $ orgasms = the_report.get("girl orgasms",0)
        if orgasms < 2:
            the_person "This only really works if we spend a proper amount of time doing it." # no gain
        elif orgasms < 1:
            the_person "So what? You're practicing not giving head? Is that it?" # no gain
            $ cousin.event_triggers_dict["oral_chance"] += -10
        else:
            if cousin.event_triggers_dict["teach_level"] == 6:               # and mc.sex_skills["Oral"] > 4:
                pass
            elif mc.sex_skills["Oral"] < 4:
                pass
            else:
                $ cousin.event_triggers_dict["teach_level"] += 1

            if (not perk_system.has_stat_perk("Starbuck Oral Bonus") and mc.sex_skills["Oral"] < 8) or (perk_system.has_stat_perk("Starbuck Oral Bonus") and mc.sex_skills["Oral"] < 9):
                $ the_roll = renpy.random.randint(0,100)
                if the_roll < cousin.event_triggers_dict.get("oral_chance", 0):
                    $ mc.sex_skills["Oral"] += 1
                    $ cousin.event_triggers_dict["oral_chance"] = 0 - (mc.sex_skills["Oral"] * 5)
                    "Your skills at giving head have improved."
                else:
                    "Although you've spent some time with Gabrielle trying to teach you, you have not managed to improve any."
            elif cousin.event_triggers_dict.get("teach_level", -1) == 6:
                "Although you've spent some time with Gabrielle trying to teach you, you have not managed to improve any."
                "You feel that you are maybe not learning anything from her."
                "Maybe you should say something about it at your next lesson."
                $ cousin.event_triggers_dict["oral_chance"] = -999
            else:
                "Although you've spent some time with Gabrielle trying to teach you, you have not managed to improve any."
                "That said, you feel that she's teaching you new things so yoe're probably still getting some benefit."

        "[the_person.title] gets back up and gets dressed."
        $ the_person.apply_planned_outfit() #TODO: get dressed
        $ mc.location.show_background()
        $ clear_scene()
    return

init 2 python:
    def cousin_teach_requirement(the_person):
        if cousin.event_triggers_dict.get("teach_level", -1) > -1 and cousin.event_triggers_dict.get("teach_level", -1) <99:
            if mc.energy >= 100 and mc.business.funds >= 100:
                return True
            elif not mc.energy >= 100:
                return "Too tired."
            else:
                return "Need $100."
        else:
            return False


    cousin_teach_action = Action("Have a personal lesson", cousin_teach_requirement, "cousin_teach_action_label",
        menu_tooltip = "Pay $100 for a personal lesson.")


init 5 python:
    add_label_hijack("normal_start", "activate_cousin_role_enhancement")
    add_label_hijack("after_load", "activate_cousin_role_enhancement")

label activate_cousin_role_enhancement(stack):
    python:
        cousin_role.add_action(cousin_teach_action)
        if cousin.event_triggers_dict.get("teach_level", -1) < 1 and cousin.event_triggers_dict.get("teach_level", -1) != -2:
            cousin.event_triggers_dict["oral_chance"] = 0
            gabrielle_visit = Action("gabrielle visit",gabrielle_visit_requirement,"gabrielle_visit_label")
            mc.business.mandatory_morning_crises_list.append(gabrielle_visit)
        cousin.event_triggers_dict["foreplay_position_filter"] = cousin_role_foreplay_position_filter
        cousin.event_triggers_dict["oral_position_filter"] = cousin_role_oral_position_filter
        cousin.event_triggers_dict["vaginal_position_filter"] = cousin_role_vaginal_position_filter
        cousin.event_triggers_dict["anal_position_filter"] = cousin_role_anal_position_filter
        #cousin.event_triggers_dict["unique_sex_positions"] = cousin_role_unique_sex_positions


        execute_hijack_call(stack)
    return
