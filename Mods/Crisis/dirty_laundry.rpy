# Dirty Laundy crisis by Starbuck!
# Scene: You go to do your laundry before bed, but notice your sister / mom has clean clothes stacked next to the dryer.
# Player has option to masturbate into clean panties and put them back.
# 50% chance mom or sister catches MC in the act. TODO higher chance at higher sluttiness? 50/50? Have cum soaked panties have some kind of effect on the person?
# Zero sluttiness they get angry, gives chance for obedience check?
# Low sluttiness they watch and touch themselves
# Mid sluttiness they give MC a handjob with the panties in their hand
# high sluttiness they put the panties on and have MC cum in the panties while they wear them

init -1 python:
    dirty_laundry_weight = 5

init 2 python:
    def dirty_laundry_requirement():
        if mc_asleep():
            return True
        return False

    dirty_laundry_action = ActionMod("Dirty Laundry", dirty_laundry_requirement, "dirty_laundry_action_label",
        menu_tooltip = "Start your laundry before bed.", category = "Home", is_crisis = True, crisis_weight = dirty_laundry_weight)

init 3 python:
    #Create Sleeping Outfits
    night_clothes = Outfit("Night Clothes")
    night_clothes.add_lower(cotton_panties.get_copy(),colour_white)
    night_clothes.add_upper(sports_bra.get_copy(),colour_white)
    night_clothes.add_upper(long_tshirt.get_copy(),colour_white)

    night_clothes_sexy = Outfit("Sexy Night Clothes")
    night_clothes_sexy.add_upper(nightgown_dress.get_copy(),colour_pink)
    night_clothes_sexy.add_lower(cute_lace_panties.get_copy(),colour_pink)

    night_clothes_slutty = Outfit("Slutty Night Clothes")
    night_clothes_slutty.add_upper(lingerie_one_piece.get_copy(),colour_yellow)
    night_clothes_slutty.add_feet(pumps.get_copy(),colour_black)
    night_clothes_slutty.add_feet(fishnets.get_copy(),colour_black)

    def set_night_outfit(person):
        if person.sluttiness > 70 or person.arousal > 70:
            person.apply_outfit(night_clothes_slutty)
        elif person.sluttiness > 40 or person.arousal > 35:
            person.apply_outfit(night_clothes_sexy)
        else:
            person.apply_outfit(night_clothes)
        return

label dirty_laundry_action_label:
    $ the_person = get_random_from_list(people_in_mc_home())
    if the_person is None:
        return

    $ set_night_outfit(the_person)

    "You are just drifting off to sleep when you suddenly you remember. You don't have any clean clothes for tomorrow!"
    "You look a the clock. It is already pretty late. You guess that your family is already asleep, so you grab your laundry and take it to the laundry room just wearing your boxers."

    $ ran_num = renpy.random.randint(0, 3)
    if ran_num < 3:
        call dirty_laundry_wash_your_clothes(the_person) from call_dirty_laundry_wash_your_clothes
    else:
        call dirty_laundry_stuck_in_dryer(the_person) from call_dirty_laundry_stuck_in_dryer

    $ clear_scene()
    $ the_person.apply_planned_outfit()
    return


label dirty_laundry_wash_your_clothes(the_person):
    "You throw your laundry in the washing machine, add some detergent and start it up."
    "As you are thinking about what to do for the next 30 minutes while the washer runs and you can move your clothes to the dryer, you notice a laundry basket on the floor filled with clean, folded clothes."
    "It looks like they all belong to [the_person.title]. Sitting on top of the laundry is a pair of sexy black panties."
    "You feel your cock stir when you think about the ass those panties cover. Maybe while you wait for your laundry you could relieve some tension fantasizing about that..."
    menu:
        "Masturbate with panties":
            "You take a quick look out the door to make sure the coast is clear, then close it behind you. You grab the panties and then pull your pants down."
            "You wrap the cloth of the panties around your cock and start to work them up and down. The satin texture feels great."
            "You close your eyes and imagine [the_person.title]. You imagine her in the morning, pulling up her cum filled panties up and wearing them around all day long."
            $ ran_num = renpy.random.randint(1,2) # increase for more situations
            if ran_num == 1: #No one catches you
                "Images of [the_person.title] flood you brain as you continue to jack off. She's bent over now, begging you to cum all over her ass."
                "You go past the point of no return. You wrap the panties around the tip and then fire your load off into them."
                "When you finish, you take a look at them. Your cum is all over [the_person.title]'s panties."
                "You do your best to fold them back up and put them back at the top of her laundry pile. You wonder if she'll notice."
                "Soon the washer is done. You swap your clothes to the dryer and start it, then head for bed. They should be dry in the morning!"
                #TODO mandatory event the next day when the girl discovers her used panties
            elif ran_num == 2:                               #the panty owner catches you!
                "Your imagination is running wild and lewd images of [the_person.title] run through your head. Suddenly, you hear the laundry room door open!"
                the_person.char "Holy fuck!"
                "You are totally busted! You stop what you are doing and open you eyes, seeing [the_person.title] looking at you wide eyed."
                if the_person.sluttiness < 20:
                    $ the_person.draw_person(position = "stand4", emotion= "angry")
                    the_person.char "[the_person.mc_title]! Those are my panties! What the fuck do you think you're doing? "
                    "You try to respond but just stammer. You're pretty sure theres no way to salvage this."
                    the_person.char "God I can't believe you. Don't touch my stuff! This is so gross! I'm gonna have to rewash these!"
                    "She quickly grabs her panties from your hand. She grabs the rest of her laundry and walks out of the laundry room."
                    $ the_person.change_stats(happiness = -10, obedience = -10, slut_temp = 10)
                    "Soon the washer is done. You swap your clothes to the dryer and start it, then head for bed. They should be dry in the morning!"
                elif the_person.sluttiness < 50:
                    $ the_person.draw_person(position = "stand4")
                    the_person.char "Is that... are those MY panties?"
                    "Her eyes are glued on your crotch. She actually doesn't seem mad?"
                    the_person.char "I didn't realize that my panties made you feel that way..."
                    "You decide to take a risk. You look her in the eyes and start to stroke your cock. The movement shocks her out of her staring and you make eye contact."
                    the_person.char "Oh god... can I... can I watch you?"
                    mc.name "Go ahead."
                    "Her eyes go back down to your crotch as you continue to stroke yourself."
                    mc.name "You should do it too, we all need to get off once a while!"
                    "She looks at you, still a bit conflicted."
                    the_person.char "I could... I mean... you aren't going to tell anyone about this are you?"
                    mc.name "Of course not."
                    $ the_person.draw_person(position = "kneeling1")
                    "[the_person.possessive_title] begins to rub her crotch. She gets down on her knees and continues to watch as you stroke yourself."
                    the_person.char "It looks so hard, I bet you are gonna cum so much."
                    "Her hand is moving rapidly between her legs. She is really getting off on this!"
                    the_person.char "You should do it... cum in my panties! I want to watch you hose them down!"
                    "Her encouragement and attention drive you over the edge.  You wrap the panties around the tip and then fire your load off into them."
                    the_person.char "Oh wow! There's so much!"
                    "You glance down and see her rapidly rubbing circles around her pussy."
                    mc.name "Do you want some help getting off?"
                    if the_person.obedience > 130:          #
                        the_person.char "Oh, I mean umm, I couldn't possibly ask you to do something like that..."
                        "You decide to take charge."
                        mc.name "Nonsense. Here, let me help you up."
                        "You put her cum soaked panties back on top of her clean laundry, then pick her up and put her on the edge of the dryer with her ass on the edge."
                        "You gently push her on her back."
                        $ the_person.draw_person (position = "missionary")
                        the_person.char "[the_person.mc_title]? Oh god, what are you going to do to me?"
                        "You put your finger over her lips to silence her."
                        if the_person.outfit.vagina_available():           #If its available no need to strip.
                            "You lower your face down between her legs. With her pussy exposed you waste no time diving right in"
                        else:                                              #Otherwise, strip her down.
                            "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy"

                            $ the_person.strip_outfit(exclude_upper = True, position = "missionary")

                            "With her pussy finally exposed you waste no time diving right in"
                        $ the_person.break_taboo("bare_pussy")
                        $ the_person.break_taboo("licking_pussy")
                        "Cupping her ass with your hands, you circle your tongue all around her wet, inviting cunt."
                        the_person.char "Oh [the_person.mc_title], you have no idea how bad I need this."
                        "[the_person.possessive_title] runs her hands your hair. You bury your nose in her mound and flick your tongue in and out of her slick hole"
                        "You circle her clit a few times with your tongue. You suck it into your mouth roughly a couple of times and then release it, you lips making a wet, lewd smacking noise"
                        the_person.char "I am so close... you're gonna make me cum!"
                        $ the_person.draw_person(emotion="orgasm", position ="missionary")
                        "You double your efforts, licking, sucking, and teasing every corner of her pleasing slit"
                        "[the_person.possessive_title] begins to orgasm convulsively, and she cries out."
                        the_person.char "Yes [the_person.mc_title]! Yes! Yes! Oh fuck, how do you do that!"
                        $ mc.listener_system.fire_event("girl_climax", the_person = the_person, the_position = "missionary")
                        $ the_person.change_stats(obedience = 5, happiness = 5, love = 3, slut_temp = 5, slut_core = 2)
                        "[the_person.possessive_title] runs her hands through your hair one last time. She sits up and gives you a kiss, tasting herself on your tongue."
                        the_person.char "Remember... this is our little secret... okay?"
                        "You hear the sound of the washing machine stopping. You start to open it up and move your laundry over to the dryer."
                        "Each time you move some clothing over, you bend over unnecessarily far so your face is near her cunt again. A couple times you give her a quick lick and she shudders."
                        $ the_person.draw_person()
                        "[the_person.title] slowly gets to her feet, but she is a little unsteady. You start the dryer with all your clothes in it, then grab her clean laundry."
                        mc.name "I'll get this for you."
                        the_person.char "Thanks, just give me a second."
                        "You slowly escort her to her room with her clean laundry, her cum filled panties sitting on the top of the pile. You set the clothes down and say goodnight."
                        "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                    else:
                        the_person.char "Oh, that's okay [the_person.mc_title]. I'm just gonna grab my laundry and go back to my room for some private time..."
                        mc.name "You should let me help, after all..."
                        "She cuts you off mid-sentence."
                        the_person.char "No, you've done quite enough already! Thanks though!"
                        "She grabs her cum filled panties from your hands, then grabs her laundry and quickly leaves the room."
                        $ clear_scene()
                        "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                        "You walk by [the_person.title]'s room as you go. You stop for a second outside her door and can hear soft moans coming from inside. You wonder if she is playing with those panties..."
                        "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                        $ the_person.change_stats(happiness = 3, slut_core = 2, slut_temp = 3)
                elif the_person.sluttiness < 75:
                    $ the_person.draw_person(position = "stand4", emotion = "happy")
                    the_person.char "Oh! You're using my panties!"
                    "You stand there for a few seconds, dumbfounded."
                    the_person.char "Well? Go ahead! I don't want to be the one to stop your fun."
                    "It takes a second for your brain to process what she just said. You slowly start to stroke yourself again."
                    "[the_person.possessive_title] watches you intently as you jack yourself off with her panties. It's actually a little distracting..."
                    mc.name "Umm, you know what, maybe this is a bad idea..."
                    the_person.char "What? Don't be silly! Here, why don't you let me help you?"
                    "She walks over to you and puts her arms around your neck."
                    $ the_person.draw_person(position = "kissing")
                    "[the_person.title] starts to kiss you softly on the side of your neck. She nibbles at your ear and then whispers."
                    if the_person is mom:
                        if day % 7 == 4 or day % 7 == 5: # tomorrow is weekend
                            the_person.char "Mommy wants your cum in her panties. I wanna wear them going out tomorrow, knowing your cum is rubbing against me all day long."
                        else:
                            the_person.char "Mommy wants your cum in her panties. I wanna wear them to work tomorrow, knowing your cum is rubbing against me all day long."
                    elif the_person is lily:
                        if day % 7 == 4 or day % 7 == 5: # tomorrow is weekend
                            the_person.char "Your little sister wants your cum in her panties. I wanna wear them all day tomorrow, talking to my friends, knowing your cum is kissing my pussy."
                        else:
                            the_person.char "Your little sister wants your cum in her panties. I wanna wear them when I go to class tomorrow, squirming in my seat through the lecture, knowing your cum is rubbing against me."
                    elif the_person is aunt:        #Wow, congrats on getting her so slutty while shes living with you!
                        the_person.char "Your aunt wants your cum in her panties. When I wear them around tomorrow I'll remember your cum is filling them up."
                    elif the_person is cousin:        #Wow, congrats on getting her so slutty while shes living with you!
                        the_person.char "Go ahead and fill up my panties, you perv. Turns out, I'm as much of a perv as you are. I'm totally wearing these all day tomorrow."
                    else:                           #Someone else someday? A live in girlfriend maybe?
                        the_person.char "I want you to cum in my panties. I'm going to wear them all day tomorrow, knowing you've marked me as yours with your hot cum..."
                    "Wow! The dirty talking really turns you on. You start stroking yourself again."
                    "Soon, you feel a hand on yours. There's another whisper in your ear."
                    the_person.char "Let me... I want to feel you in my hand when you blow your load."
                    $ the_person.break_taboo("touching_penis")
                    "You let go, and feel [the_person.title]'s hand take over. She continues you kiss and nibble on your neck."
                    "The sensations are overwhelming, and soon you are ready to cum. She can sense it and jacks you enthusiastically."
                    the_person.char "Do it! Cum in my panties!"
                    "You moan as your orgasm hits you. You dump spurt after spurt into [the_person.possessive_title]'s panties as she jacks you off with them."
                    $ the_person.draw_person(emotion = "happy")
                    "When you come back to your senses, you look and see [the_person.title]. She is licking a little bit of cum that got on her hand."
                    the_person.char "Mmm... that was hot! I can't wait to wear these tomorrow."
                    $ the_person.change_stats(obedience = 5, happiness = 5, slut_temp = 5)
                    "She grabs her other laundry and you say goodnight before she leaves you alone in the laundry room, recovering."
                    $ clear_scene()
                    "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                    "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                    #TODO event having her wear the panties the next day
                else:
                    $ the_person.draw_person(position = "stand4", emotion = "happy")
                    the_person.char "Oh! You're using my panties! That looks like fun!"
                    "She walks over to you, then hops on on the side of the dryer with her legs hanging off the end."
                    $ the_person.draw_person(position = "sitting")
                    "She looks at you, expectantly."
                    the_person.char "What are you waiting for? Keep going!"
                    "She continues to watch you. You gives yourself a few tentative strokes."
                    the_person.char "Mmm, I love watching a man get himself off..."
                    "You try to get back into the swing of things, you have a hard time with [the_person.title] in the room. She seems to be oblivious though."
                    the_person.char "I can't wait to wear those panties after you cum in them... I think I'll wear them to bed tonight! Actually... maybe I could wear them before that..."
                    "She looks at you for another second. What is she talking about?"
                    "She suddenly stands up and starts stripping."

                    $ the_person.strip_outfit(position = "stand2")

                    $ the_person.break_taboo("bare_tits")
                    $ the_person.break_taboo("bare_pussy")
                    "Once she is naked, [the_person.title] turns to you."
                    the_person.char "Here, let me have those!"
                    "You hand her the panties. She quickly puts them on."

                    $ the_person.outfit.add_lower(lace_panties.get_copy(), colour_black)
                    $ the_person.draw_person()

                    the_person.char "Mmm, yeah this will be more fun! Don't worry, you can still cum in my panties... but you have to do it while I'm wearing them!"
                    $ the_person.draw_person(position = "standing_doggy")
                    "[the_person.possessive_title] turns around and bends over with her hands on the dryer. She looks back at you."
                    the_person.char "Go ahead! Rub your cock against me..."
                    "You step up behind [the_person.title] and put your hands on her hips. She wiggles her ass back at you. You nestle your cock between her ass cheeks and start to hump against her panties."
                    the_person.char "Mmm... that's it..."
                    "Her ass looks great, barely covered in her satin panties. The combination of the soft cloth with the heat of her body feels great."
                    "You pull back for a second, then reach down and angle your cock down more, then slide it between her thighs. Now as your begin to hump her it is rubbing right up against her panty covered slit."
                    the_person.char "Oh! Yeah I knew this would be fun... keep going that feels so good!"
                    "You grab her ass with both hands and hump her aggressively. You can feel the heat and humidity coming from her cunt as her panties get damp with her excitement."
                    "It feels great, but you can tell you probably won't be able to get off this way."
                    "You stop when you feel [the_person.title]'s hand on your cock. She pulls her panties to the side then slides your cock underneath them."
                    "You give a slow thrust and feel your dick now rubbing directly against her labia."
                    the_person.char "Mmmm... I want you to cum like this, all over the inside of my panties, while I'm wearing them!"
                    "You work your hips against hers for a bit, enjoying the feeling of her wet slit as you rub yourself along the length of it."
                    "The heat and the moisture of it feels great... but your cock is aching to bury itself inside of her!"
                    menu:
                        "'Accidentally' slip it in":
                            "You slowly start to change the angle of your thrusting, and making thrusts a bit shallower. She gets frustrated that you aren't going full forward against her clit and starts to push herself back against you."
                            "One time, when she is about to thrust back, you bend your knees a bit, but angle your hips back up. When she thrusts back your cock slips inside her."
                            $ the_person.break_taboo("vaginal_sex")
                            $ the_person.break_taboo("condomless_sex")
                            "You grab [the_person.title]'s hips and thrust your hips forward, pushing yourself deep inside her. You hold her hips place, enjoying being finally buried in her cunt. She moans loudly at the sudden penetration."
                            mc.name "Whoops! Sorry about that!"
                            "You apologize, but don't let go of her hips. She starts to grind against you."
                            the_person.char "Mmm, that's okay! Just try to pull out when you cum! I still want you to finish in my panties..."
                            "[the_person.possessive_title] is being a good sport, so you decide to try and do that for her. You start to fuck her now, your hips smacking up against her ass."
                            "With all the action you've had up until this point, you feel yourself getting ready to finish."
                            "At the last second, you pull back just enough to pull out of her pussy."
                            "Your first couple of spurts erupt and splash up against her cunt and along the front of her panties. She moans when she feels the splash."
                            "You pull back completely now and grab your cock. You aim another spurt and one ass check, then for the next one at the other."
                            $ the_person.cum_on_ass()

                        "Finish like this":
                            "You decide to humor [the_person.title]'s wishes and continue the way you are going now."
                            "The heat coming from her sopping wet slit feels amazing, sliding up and down your erection."
                            "With all the action you've had up until this point, you feel yourself getting ready to finish."
                            "Your first couple of spurts erupt and splash up against her cunt and along the front of her panties. She moans when she feels the splash."
                            "You pull back completely now and grab your cock. You aim another spurt and one ass check, then for the next one at the other."
                            $ the_person.cum_on_ass()

                    $ the_person.draw_person(position="back_peek")
                    "As you step back, [the_person.title] slowly stands up and looks back at you."
                    the_person.char "Wow, that was so hot..."
                    "You see her hand go down her side and she starts to touch herself through her cum soaked panties."
                    the_person.char "I think umm... I'm gonna retire to my room for the night..."
                    menu:
                        "Masturbate for me" if the_person.obedience >= 130:
                            mc.name "I mean, its my cum you're using, just get yourself off right here."
                            "She thinks about it for second, then agrees."
                            the_person.char "Okay! Just do me a favor and don't get dressed."
                            $ the_person.draw_person( position = "missionary")
                            "[the_person.title] sits on the edge of the dryer now and starts to touch herself."
                            "Her hand is making big circles around her clit. You can see some of your cum starting to leak out the sides of her panties."
                            the_person.char "Mmm, your cum feels so good..."
                            "She strokes herself as you watch. She looks you right in the eyes."
                            the_person.char "Oh god, I'm gonna cum!"
                            "Her body quakes and spasms. She is moaning loudly as she continues to stroke herself through her panties."
                            $ the_person.change_happiness(5)
                            mc.name "Damn, that was hot."
                            the_person.char "Ahh, thanks for the help. I really needed that..."
                            "[the_person.title] slowly gets up. She grabs her laundry and says goodnight."
                            $ clear_scene()
                            "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                            "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                        "Say Goodnight":
                            "You say goodnight to [the_person.title]. She slowly walks out of the laundry room. You note that she forgot to take her laundry with her."
                            $ clear_scene()
                            "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                            "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                        "Masturbate for me\n{color=#ff0000}{size=18}Requires 130 Obedience{/size}{/color} (disabled)" if the_person.obedience < 130:
                            pass
                    $ the_person.change_stats(obedience = 5, happiness = 5, slut_temp = 5)
            else:      #Someone else catches you! for now this is disabled
                pass
                #TODO this

        "Find something else to do":
            "You decide to do something else. You head back to room and hop on your PC, doing work related tasks until the washer is done."
            "While you are working on researching business methods, you accidentally get caught up in a click bait, 10 ways to increase your bottom line item on some random economics website."
            "Most of the info is garbage, but one of them actually makes sense for you to use. You make note of the method and decide to institute it at your business."
            $ mc.business.effectiveness_cap += 1
            if get_HR_director_tag("business_HR_eff_bonus"):
                $ set_HR_director_tag("business_HR_eff_bonus", get_HR_director_tag("business_HR_eff_bonus") + 1)
            "You go back to swap your laundry to the dryer."
            $ the_person.draw_person()
            "[the_person.title] is just coming out of the laundry room with her laundry basket."
            #TODO outfit and text based on her sluttiness.
            "You say goodnight to [the_person.title] and then swap your clothes from the washer to the dryer. They should be dry in the morning!"

    return

label dirty_laundry_stuck_in_dryer(the_person):
    "As you walk into the laundry room, you see [the_person.title] with her head in the dryer."
    $ the_person.draw_person(position = "doggy")
    "She is muttering to herself about how she could have been so clumsy as to get her hair stuck in there; plainly it is preventing her from getting out."

    menu:
        "Help her get out":
            mc.name "Hey [the_person.title], what are you doing in there?"
            the_person.char "Hey [the_person.mc_title], it's good that you're here, I'm stuck in this infernal machine."
            if the_person is mom:
                mc.name "Don't worry, mom, I'll have you out there in a jiffy."
            elif the_person is lily:
                mc.name "Don't worry, little sis, let me help you."
            else:
                mc.name "No worries, [the_person.title]. Here, let me untangle this for you."

            "You manage to untangle [the_person.possessive_title]'s hair."
            the_person.char "Thanks, [the_person.mc_title], you're a lifesaver. Don't worry, I can finish the rest of this myself."
            $ the_person.change_stats(love = 2, happiness = 5)

        "Masturbate":
            "You don't say anything, but quickly pull out your already hard member."
            "All the while you are masturbating, [the_person.possessive_title] keeps on muttering and wiggling her shapely ass, right in front of you."
            "You soon reach your tipping point and spray your load right onto her ass."
            $ the_person.cum_on_ass()
            $ the_person.draw_person(position="doggy")
            the_person.char "Hey [the_person.mc_title], is that you? What's going on back there... don't just stand there, get me out of this thing!"
            mc.name "Hi [the_person.title], don't worry, just wait a sec, I'll get some scissors and get you out."
            "When you return you carefully manage to untangle her from the machine and she looks at you, running a hand across her bum."
            if the_person.effective_sluttiness() > 40 or the_person.get_opinion_score("being covered in cum") > 0:
                $ the_person.draw_person(position = "stand4", emotion = "happy")
                the_person.char "Did you just jerk off all over my ass?"
                if the_person is mom:
                    the_person.char "So you really like your mommy's ass, you little pervert."
                elif the_person is lily:
                    the_person.char "So you enjoy masturbating to your little sister's bottom?"
                else:
                    the_person.char "So you really liked masturbating to my wiggling ass?"

                the_person.char "Why don't you just ask next time, so I can enjoy it too?"
                if the_person.get_opinion_score("drinking cum") > 0:
                    "[the_person.possessive_title] moves her hand to her mouth and licks off your seed from her fingers."

                mc.name "Maybe I will. See ya."

                $ the_person.change_stats(obedience = -2, happiness = 5, slut_temp = 5)
            else:
                $ the_person.draw_person(position = "stand4", emotion = "angry")
                if the_person is mom:
                    the_person.char "Jesus, [the_person.mc_title], did you just cum on my ass? I'm your mother!"
                    "You just stare at her, while [the_person.possessive_title] continues her tirade."
                    the_person.char "You shouldn't do that! What would your sister say if she saw this?"
                    the_person.char "Now be a good son and behave, and don't {i}ever{/i} let me catch you doing this again."
                elif the_person is lily:
                    the_person.char "What the fuck, [the_person.mc_title]? Why the fuck would you jizz on me like that? You bastard!"
                    "You just stare at her, while [the_person.possessive_title] continues her tirade."
                    the_person.char "Now I have to wash this too, dammit. Don't you {i}ever{/i} do this again."
                else:
                    the_person.char "Dammit [the_person.mc_title], you can't just cum on my ass like that!"
                    "You just stare at her, while [the_person.possessive_title] continues her tirade."
                    the_person.char "What would your mother and sister say if they find out about your behavior?"
                    the_person.char "Now get out of my way, so I can get out of these clothes."

                $ the_person.change_stats(happiness = -5, slut_temp = 2)

        "Fuck her" if not the_person.has_taboo("vaginal_sex") and the_person.effective_sluttiness("bare_pussy") > 40:
            mc.name "Hey [the_person.title], what are you doing in there?"
            the_person.char "Hey [the_person.mc_title], it's good that you're here, I've managed to get my hair stuck in this contraption."
            mc.name "Don't worry, I know how to help you."

            $ the_item = the_person.outfit.get_lower_top_layer()
            if the_item.is_extension:
                $ the_item = the_person.outfit.get_upper_top_layer()
            if the_item:
                "You move your hands along [the_person.possessive_title]'s ass and remove her [the_item.display_name]"
                $ the_person.draw_animated_removal(the_item, position = "doggy")

            the_person.char "[the_person.mc_title]? I don't think taking off my [the_item.display_name] will get me out of here."
            mc.name "Trust me [the_person.title], I have a good reason for doing it this way."
            the_person.char "Okay, go ahead, just don't pull too much on my head."

            $ del the_item
            if not the_person.outfit.vagina_visible():
                "You quickly start removing the remaining clothing from [the_person.possessive_title]."
                $ the_person.strip_outfit(position = "doggy", exclude_upper = True)

            "Now that you have clear access, you quickly remove your shorts and position yourself behind [the_person.possessive_title] and push the tip of your cock against her wet slit."
            the_person.char "What the fuck! You're going to fuck me like {i}this?{/i}"
            mc.name "Yes, and don't pretend that you don't like it, because I know you do."
            call fuck_person(the_person, start_position = doggy, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_person_dirty_laundry_stuck_in_dryer
            $ the_report = _return
            "With your activities concluded, you help [the_person.title] out of the dryer onto shaky legs."
            if the_report.get("girl orgasms", 0) > 1:
                $ the_person.change_stats(happiness = 10, obedience = 5)
                $ the_person.draw_person(position = "stand4", emotion = "orgasm")
                the_person.char "Oh my god, I came so much... I didn't think that would be possible in this position."
                $ the_person.draw_person(position = "stand4", emotion = "default")
                the_person.char "It's still not cool that you took advantage of me like that, even if it was really good."
            elif the_report.get("girl orgasms", 0) > 0:
                $ the_person.change_stats(happiness = 5, obedience = 3)
                $ the_person.draw_person(position = "stand4", emotion = "orgasm")
                the_person.char "Oh wow, that really felt good, thank you [the_person.mc_title]."
                $ the_person.draw_person(position = "stand4", emotion = "default")
                the_person.char "It's still not cool that you took advantage of me like that, though."
            else:
                $ the_person.change_stats(happiness = -5, obedience = -1)
                $ the_person.draw_person(position = "stand4", emotion = "angry")
                the_person.char "You take advantage of me like that and don't even get me off? Not cool, [the_person.mc_title], not cool."

            mc.name "Haven't you noticed?"
            the_person.char "What?"
            mc.name "You hair came loose about a minute in, you could have stopped at any point."
            the_person.char "Oh... well, next time just get me out, and we can do this properly. Now move..."

    "[the_person.possessive_title] quickly grabs her laundry and scoots out of the laundry room."
    return