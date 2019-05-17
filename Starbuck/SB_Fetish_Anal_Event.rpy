init 1 python:
    def SB_fetish_anal_requirement():
        if time_of_day == 3:
            if mc.current_stamina > 0:
                if mc.business.is_open_for_business():
                    if mc.is_at_work():
                        return True
        return False

    #SB_fetish_anal_crisis = Action("anal Fetish Crisis", SB_fetish_anal_requirement,"SB_fetish_anal_label")

    SB_anal_outfit = Outfit("A Special Night")
    SB_anal_outfit.add_upper(lace_bra.get_copy(),colour_pink)
    SB_anal_outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
    SB_anal_outfit.add_feet(high_heels.get_copy(), colour_pink)

    SB_anal_nude_outfit = Outfit("Nude")

    def SB_fetish_anal_staylate_event_requirement():
        if time_of_day == 3:
            return True
        return False

#SBA1
label SB_fetish_anal_label(the_person):
    "You are just finishing up with business for the day when you hear a pleasant voice call out to you."
    the_person.char "Hey [the_person.mc_title]."
    #$ the_person.outfit = SB_anal_outfit.get_copy()
    $ the_person.draw_person()
    show screen person_info_ui(the_person)
    ###Draw the girl###
    "You give her a quick wave as she walks up to you."
    the_person.char "Hey, I really hate to bug you but... "
    "She places extra emphasis on the word but before moving on."
    the_person.char "I was wondering if you would stay for a bit after work? I need help with something."
    "[the_person.possessive_title] looks at you with hopeful eyes."
    menu:
      "Accept":  #This begins the sex scene
        ###Set anal skill to 6
        $ the_person.sex_skills["Anal"] = 6
        mc.name "I suppose I could stay for a bit, let me just finish up a couple things and I'll be right with you."
        the_person.char "Oh! Thanks [the_person.mc_title], I'll be right back! You won't regret this!"
        $ the_person.draw_person(position = "walking_away")
        "You finish up what you were doing and say goodbye to your employees. You are just starting to wonder what [the_person.possessive_title] needs when she comes back into the room."
        $ the_person.outfit = SB_anal_outfit.get_copy()
        $ the_person.draw_person()
        "[the_person.possessive_title] has changed into some very nice lingerie. You notice as she walks up that she isn't wearing any panties..."
        "She walks up and stands next to you by your desk."
        the_person.char "So, [the_person.mc_title], I don't know why but... I decided recently I really want to try and get better at anal..."
        "You aren't surprised, it's been a while since you started giving her the serum for increased anal enjoyment."
        the_person.char "I went over to the sex shop and bought a new toy... I've been wearing it for a few days now... and I was wondering what you thought?"
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.possessive_title] turns and bends over in front of you, with her hands on your desk."
        "You can see, nestled between her curvacious ass cheeks, a matching pink jewel on the base of a butt plug."
        the_person.char "I think I'm ready for something a bit more... substantial... don't you think?"
        "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
        $ the_person.change_arousal(the_person.get_opinion_score("anal sex"))
        "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
        "You decide to tease her before you put it in."
        mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
        "[the_person.possessive_title] tries to push back against you and begins to beg."
        the_person.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
        "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
        ###Anal Scene, standing variant###
        call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True, girl_in_charge = False, private = True) from _call_fuck_person_SBA10
        $ the_person.reset_arousal()
        ###Reset Arousal
        #$ the_person.SB_fetish = "anal sex"
        $ the_person.sexy_opinions["anal sex"] = [FETISH_OPINION_VALUE, True]
        "[the_person.possessive_title] takes a few minutes to recover, then turns to you."
        $ the_person.draw_person()
        the_person.char "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately... I just can't stop thinking about you bending me over..."
        "[the_person.possessive_title] blushes and pauses..."
        mc.name "...And doing what, [the_person.title]?"
        "You tease her."
        the_person.char "I can't stop thinking about how full it feels... it feels so right when you push into my ass. It gets me so hot imagining it..."
        "She's been under the influence of your serums for a while now... you wonder if she's developed an anal fetish..."
        "[the_person.possessive_title] gets her butt plug. She slowly pushes it back into her ass."
        the_person.char "Thanks again, [the_person.mc_title]. We should do this again... and soon."
        "You wave goodbye to [the_person.possessive_title] and get ready to head home for the night."
        $ SB_give_anal_role(the_person)
        $ SB_CALCULATE_RANDOM_EVENT_RATE()
        $ FETISH_ANAL_EVENT_INUSE = False

      "Refuse":
        the_person.char "I'm sorry to hear that..." #TODO finish this
        $ FETISH_ANAL_EVENT_INUSE = False


    return

#SBA2
label SB_fetish_anal_staylate_event_label(the_person):
    if not mc.is_at_work():
        "Your phone rings. It's [the_person.possessive_title]. You answer it."
        the_person.char "Hey, are you at work? I can't find you."
        "You forgot! You asked [the_person.possessive_title] to stay after work today."
        mc.name "Sorry, I had something come up and had to leave early."
        "[the_person.possessive_title] tries to mask disappointment in her voice but it is still obvious."
        the_person.char "Oh... okay... well try to let me know next time before I stay late. I thought... anyway, maybe some other time. Bye!"

        $ FETISH_ANAL_EVENT_INUSE = False
        $ SB_CALCULATE_RANDOM_EVENT_RATE()
        return
    "You finish up with your work for the day and return to your office. You are organizing some papers when [the_person.possessive_title] enters the room."
    show screen person_info_ui(the_person)
    $ the_person.outfit = SB_anal_outfit.get_copy()
    $ the_person.draw_person()
    "From the look of her attire, she seems to have guessed the purpose of your meeting correctly."
    the_person.char "Hey [the_person.mc_title]. You wanted to see me?"

    mc.name "That's right. While your job performance has been ideal, it has recently come to my attention that you may not be of sound moral character."
    "[the_person.possessive_title] smiles slightly. She can see where you are going with this conversation."
    mc.name "I asked you to stay late so I could punish you properly for your misconduct. Now, I want you to bend over my desk to prepare for your punishment."
    the_person.char "Yes Sir!"
    $ the_person.draw_person(position = "standing_doggy")
    $ the_person.change_arousal(10)
    "You approach [the_person.possessive_title] and begin to inspect her shapely ass. Nestled between her cheeks, you can see the pink jewel of her butt plug."
    "Below her plug, you can see the soft wet lips of her cunt. They are already flushed, showing a slight glisten of moisture. She is getting aroused just from presenting her ass to you."
    "She begins to wiggle her hips slightly in response to your intense gaze."
    the_person.char "Is everything to your satisfaction, sir?"
    "Should you reward her with your cock in her ass? Or spank it first?"
    menu:
        "Spank Her":
            "SMACK!"
            "You hand lands a firm blow on her supple ass. Her knees buckle a bit and she arches her back, surprised by the sudden blow."
            mc.name "Quiet slut! You will speak only when spoken to. Do you understand?"
            the_person.char "Yes sir!"
            "You murmur a soft approval. You give her ass another hard spank."
            "SMACK"
            "[the_person.possessive_title]'s accomodating ass ripples in shockwaves out from where you hand spanks it."
            "You give her hind quarters a few more spanks, giving her few seconds in between."
            $ the_person.change_arousal(20)
            "[the_person.possessive_title] barely stifles a moan as you spank her again. Her cheeks are beginning to glow a rosey red. Her pussy lips are growing puffy with clear signs of arousal."
            "You decide it is time to move on."
        "Fuck Her Ass" if mc.current_stamina > 0:
            "You firmly grasp one of her ass cheeks in one hand before responding."
            mc.name "Everything seems to be in order, but I'll still need to carry out your punishment."
            "With two fingers, you start to pull the jewelled plug from her. When only the tip remains, you push it back in."
            the_person.char "Oh! Whatever you think is best sir..."
            "You fuck her for a few moments with the jewelled plug. She loves the penetration and begins to push her hips back against you as you work the plug in and out of her."
            $ the_person.change_arousal(10)
            mc.name "Now, I think it is time for something a bit more substantial than the plug..."
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.get_opinion_score("anal sex"))
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title] tries to push back against you and begins to beg."
            the_person.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
            call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True, girl_in_charge = False, private = True) from _call_fuck_person_SBA20
            if the_person.arousal > 100:
                "[the_person.possessive_title] lays over the desk for a while, recovering from her ass reaming."
                the_person.char "God... that felt so fucking good..."
                $ the_person.change_obedience(5)
                $ the_person.change_happiness(5)

            else:
                the_person.char "Okay... I guess we're done already?"
                "[the_person.possessive_title] seems disappointed she didn't finish."
                $ the_person.change_love(-2)
                $ the_person.change_happiness(-5)
            $ the_person.reset_arousal()
            "[the_person.possessive_title] gets up and starts getting ready to go home."
            "You say goodbye to her as she walks out your office door."
            $ FETISH_ANAL_EVENT_INUSE = False
            $ SB_CALCULATE_RANDOM_EVENT_RATE()
            hide screen person_info_ui
            return
        "Fuck Her Ass\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
            pass



    menu:
        "Fuck Her Ass" if mc.current_stamina > 0:
            "You firmly grasp one of her ass cheeks in one hand. It is hot to the touch."
            "With two fingers, you start to pull the jewelled plug from her. When only the tip remains, you push it back in."
            "You fuck her for a few moments with the jewelled plug. She loves the penetration and begins to push her hips back against you as you work the plug in and out of her."
            $ the_person.change_arousal(10)
            mc.name "Now, I think it is time for something a bit more substantial than the plug..."
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.get_opinion_score("anal sex"))
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title] tries to push back against you and begins to beg."
            the_person.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
            call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True, girl_in_charge = False, private = True) from _call_fuck_person_SBA21
            if the_person.arousal > 100:
                "[the_person.possessive_title] lays over the desk for a while, recovering from her ass reaming and spanking."
                the_person.char "God... that felt so fucking good..."
                $ the_person.change_obedience(5)
                $ the_person.change_happiness(5)
            else:
                the_person.char "Okay... I guess we're done already?"
                "[the_person.possessive_title] seems disappointed she didn't finish."
                $ the_person.change_love(-2)
                $ the_person.change_happiness(-5)
            $ the_person.reset_arousal()
            "[the_person.possessive_title] gets up and starts getting ready to go home."
            "You say goodbye to her as she walks out your office door. She walks a bit funny, clearly uncomfortable after the spanking she received."
            $ FETISH_ANAL_EVENT_INUSE = False
            $ SB_CALCULATE_RANDOM_EVENT_RATE()
        "Fuck Her Ass\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
            pass
        "Send her home":
            mc.name "That's enough for today [the_person.title]."
            "[the_person.possessive_title] looks back at your, clearly surprised that you are sending her away already."
            the_person.char "What? I mean, already? Okay..."
            "She grabs her stuff and quickly makes an exit from your office."
            $ the_person.change_love(-2)
            $ the_person.change_happiness(-5)
            $ the_person.change_obedience(10)
            $ FETISH_ANAL_EVENT_INUSE = False
            $ SB_CALCULATE_RANDOM_EVENT_RATE()

    hide screen person_info_ui
    return

init 2 python:
    def SB_fetish_anal_recurring_requirement():
        if time_of_day == 3:
            if mc.is_at_work():
                for person in mc.business.get_employee_list():
                    if person.sex_skills["Anal"] > 5:
                        return True

        return False

    SB_fetish_anal_recurring_crisis = Action("anal Fetish Recurring Crisis",SB_fetish_anal_recurring_requirement,"SB_fetish_anal_recurring_label")
    crisis_list.append([SB_fetish_anal_recurring_crisis,10])

    def SB_mom_anal_pay_requirement():
        if time_of_day == 4 and day%7 == 4: #It is the end of the day on friday
            return True
        return False
            #block of code to run


#SBA3
label SB_fetish_anal_recurring_label():
    $ meets_fetish_list = []
    python:
        for person in mc.business.get_employee_list():
            if person.sex_skills["Anal"] > 5:
                meets_fetish_list.append(person)
    $ the_person = get_random_from_list(meets_fetish_list)

    "As you are packing up your stuff to head home for the day, you hear [the_person.possessive_title]'s sweet voice call out to you."

    if mc.business.is_open_for_business():
        $ the_person.draw_person()
        show screen person_info_ui(the_person)
        the_person.char "Hey, [the_person.mc_title]. Just wondering if... you know... you wanna stick around for a bit after work today?"
        "She flashes you a quick smile. You wonder if she has in that butt plug she showed you last time you stayed late at the office wit her..."
        mc.name "Sure, I can probably stick around for a little bit. Just give me a few minutes."
        the_person.char "Oh! Thanks [the_person.mc_title], I'll be right back! You won't regret this!"
        $ the_person.draw_person(position = "walking_away")
        "You finish up what you were doing and say goodbye to your employees. Your curiosity about what [the_person.possessive_title] needs is answered when she comes back into the room."
        $ the_person.outfit = SB_anal_outfit.get_copy()
        $ the_person.draw_person()
        "[the_person.possessive_title] has changed into her pink lingerie. You notice as she walks up that she isn't wearing any panties..."
        "She walks up and stands next to you by your desk. Then she turns around."
        $ the_person.draw_person(position = "back_peek")
        "Between her pillowy cheeks is her pink jewelled butt plug."
        the_person.char "What do you say, [the_person.mc_title]? Want to replace my plug with something else?"
    else:
        $ the_person.outfit = SB_anal_outfit.get_copy()
        $ the_person.draw_person()
        show screen person_info_ui(the_person)
        the_person.char "Hey, [the_person.mc_title]. I was wondering if you would be here on the weekend! Want to have some fun before you head home?"
        "[the_person.possessive_title] is dressed to impress. You wonder if she has in that butt plug she showed you last time you stayed late at the office wit her..."
        "As if sensing your thoughts, [the_person.possessive_title] turns around."
        $ the_person.draw_person(position = "back_peek")
        "Between her pillowy cheeks is her pink jewelled butt plug."
        the_person.char "What do you say, [the_person.mc_title]? Want to replace my plug with something else?"
    menu:
        "Fuck her ass" if mc.current_stamina > 0:
            the_person.char "Mmmm I can't wait to feel it."
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.possessive_title] walks over in front of you, with her hands on your desk."
            ###Anal Scene, standing variant###
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.get_opinion_score("anal sex"))
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title] tries to push back against you and begins to beg."
            the_person.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
            call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True, girl_in_charge = False, private = True) from _call_fuck_person_SBA30
            $ the_person.reset_arousal()
            ###Reset Arousal
            the_person.char "It was so good. I've been thinking about that all day."
            "[the_person.possessive_title] gets her butt plug. She slowly pushes it back into her ass."
            the_person.char "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            "You wave goodbye to [the_person.possessive_title] and get ready to head home for the night."
        "No Thanks":
            "[the_person.possessive_title] is caught completely off gaurd by your refusal."
            $ the_person.change_obedience(-10)
            $ the_person.change_happiness(-10)
            the_person.char "Oh!... Okay... Well... hey I understand... Maybe some other time yeah?"
            "[the_person.possessive_title] quickly sulks off. Maybe you should've?"
        "Too Tired" if mc.current_stamina == 0:
            "[the_person.possessive_title] is surprised by your answer."
            $ the_person.change_obedience(-5)
            $ the_person.change_happiness(-5)
            the_person.char "Oh! I'm sorry... I know you work so hard around here. Maybe tomorrow then?"
            "[the_person.possessive_title] quickly sulks off."
    return



label SB_free_strip_scene(the_person):
    #Shamelessly copied and modified from Vrens base function, but this one is free :)

    $ pose_list = [["Turn around","walking_away"],["Turn around and look back","back_peek"],["Hands down, ass up.","standing_doggy"],["Be flirty","stand2"],["Be casual","stand3"],["Strike a pose","stand4"],["Move your hands out of the way","stand5"]]

    $ picked_pose = the_person.idle_pose #She starts in her idle pose (which is a string)
    $ rand_strip_desc = renpy.random.randint(0,3) #Produce 4 different descriptions at each level to help keep this interesting.

    $ strip_willingness = the_person.sluttiness + (5*the_person.get_opinion_score("not wearing anything")) - the_person.outfit.slut_requirement
    #If there are other things that influence how willing a person is to strip they go here!

    $ keep_stripping = True #When set to false the loop ends and the strip show stops.

    while keep_stripping:
        $ rand_strip_desc = renpy.random.randint(0,3)
        $ the_person.draw_person(position = picked_pose)
        $ tease_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True) #She's slutty enough that she wants to tease you a little more
        if rand_strip_desc == 0:
                if tease_clothing is not None:
                    "[the_person.possessive_title] pulls at her [tease_clothing.name] seductively."
                    the_person.char "Mmm, I bet you want me to take this off, right?"
                    "[the_person.possessive_title] wiggles her hips side to side and bites her bottom lip, as if imagining some greater pleasure yet to come."
                else:
                    "[the_person.possessive_title] runs her hands down her body seductively."
                    the_person.char "Mmm, I bet you want to get your hands on me now, right?"
                    "[the_person.possessive_title] wiggles her hips side to side and bites her bottom lip, as if imagining some greater pleasure yet to come."

        elif rand_strip_desc == 1:
                if the_person.has_large_tits():
                    "[the_person.possessive_title] moves her body side to side for you, letting her large tits bounce and jiggle while you watch."
                    "[the_person.possessive_title] takes a wider stances and slides her hands down her own thighs, all while maintaining eye contact with you."
                    the_person.char "You're looking so good today [the_person.mc_title], did you know that?"
                else:
                    "[the_person.possessive_title] moves her body side to side for you while you watch."
                    "[the_person.possessive_title] takes a wider stances and slides her hands down her own thighs, all while maintaining eye contact with you."
                    the_person.char "You're looking so good today [the_person.mc_title], did you know that?"

        elif rand_strip_desc == 2:
                if tease_clothing is not None:
                    "[the_person.possessive_title] slips a hand under her [tease_clothing.name] and starts to pull it off."
                    the_person.char "Maybe I should just... slip this off. What do you think?"
                else:
                    if the_person.has_large_tits():
                        "[the_person.possessive_title]'s hands slide up and down her body. She cups one of her sizeable breast and squeezes it, pinching her own nipple while she does."
                        the_person.char "Oh [the_person.mc_title], I think I'm going to need more than your eyes on me soon..."
                    else:
                        "[the_person.possessive_title]'s hands slide up and down her body. She rubs her small breasts, paying special attention to their firm nipples."
                        the_person.char "Oh [the_person.mc_title], I think I'm going to need more than your eyes on me soon..."
        else:
                the_person.char "I hope you're enjoying the show [the_person.mc_title]."
                "She wiggles her hips for you and winks."

        $menu_list = [] #Tuple of menu things.
        # High obedience characters are more willing to be told to strip down (althoug they still expect to be paid for it)
        # Low obedience characters will strip off less when told but can be left to run the show on their own and will remove some.
        python:
            for item in the_person.outfit.get_unanchored():
                test_outfit = the_person.outfit.get_copy()
                test_outfit.remove_clothing(item)

                display_string = "Strip " + item.name

                menu_list.append([display_string, [item, 0]])

            menu_list.append(["Just watch.","Watch"])
            menu_list.append(["Tell her to pose.","Pose"])
            if the_person.outfit.vagina_visible() and the_person.outfit.tits_visible():
                menu_list.append(["Finish the show.","Finish"])

        $ strip_choice = renpy.display_menu(menu_list,True,"Choice")
        if strip_choice == "Watch":
            if renpy.random.randint(0,1) == 0:
                $ tease_item = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True) #The clothing item she's considering taking off
                if renpy.random.randint(0,100) < 50: #She's independant enough to strip, change pose, etc. on her own.
                    if tease_item is not None : #A more obedient person is less willing to strip without being told to. A less obedient person will strip further on their own.

                        $ the_person.draw_animated_removal(tease_item, position = picked_pose)
                        "You watch as [the_person.possessive_title] grabs their [tease_item.name] and pulls it off."
                    else:
                        #She has nothing to strip off or she's as slutty as she's willing to get
                        "[the_person.possessive_title] seems comfortable just the way she is."

                else: #She doesn't quite know what to do without you telling her.
                    "Without any direction [the_person.possessive_title] just keeps doing what she was doing."

            else:
                #She decides to change pose half the time.
                $ new_pose = get_random_from_list(pose_list)
                if not new_pose[1] == picked_pose:
                    $ picked_pose = new_pose[1]
                    "While you're watching [the_person.possessive_title] changes pose so you can see her from a different angle."
                else:
                    "[the_person.possessive_title] seems comfortable just the way she is."



        elif strip_choice == "Pose":
            #You ask her to change into a different pose
            mc.name "I want to see you from a different angle."
            $pose_menu_tuple = []
            python:
                for pose_tuple in pose_list:
                    if not pose_tuple[1] == picked_pose:
                        pose_menu_tuple.append(pose_tuple)
                pose_menu_tuple.append(["Nevermind.",None])

            $ pose_choice = renpy.display_menu(pose_menu_tuple,True,"Choice")
            if pose_choice is not None:
                $ picked_pose = pose_choice
                "[the_person.possessive_title] nods and moves for you."

            else:
                mc.name "Nevermind, you look perfect like this."

        elif strip_choice == "Finish":
            $ keep_stripping = False
            mc.name "Wow [the_person.title], that was amazing."
            the_person.char "Oh, are we done already? It feels like something is just getting started!"

        else:
            $ the_clothing = strip_choice[0]
            the_person.char "This you mean? You want me to take this off?"
            $ the_person.draw_animated_removal(strip_choice[0], position = picked_pose)
            "[the_person.possessive_title] strips off her [the_clothing.name]. She throws it playfully, hitting you in the face." #Hopefully this wasn't shoes, lol

    return

#SBA4
label SB_mom_anal_pay_label(the_person):
    $ renpy.show(bedroom.name,what=bedroom.background_image)
    "You're getting ready for bed when [the_person.possessive_title] calls from downstairs."
    the_person.char "[the_person.mc_title], could we talk for a moment?"
    mc.name "Sure, down in a second."
    show screen person_info_ui(the_person)
    $ renpy.show(kitchen.name,what=kitchen.background_image)
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] is sitting at the kitchen table, a collection of bills laid out in front of her."
    "She is fidgeting a bit. You can tell she is a little nervous about something."
    the_person.char "[the_person.mc_title], I'm really sorry about this. Some things have come up around the house that need repair but I'm not sure have the money to have the work done..."
    the_person.char "I know that you've been working so hard at your new business and I'm so proud of you, and I'm happy we've been so close lately."
    the_person.char "I wouldn't feel right about just taking your hard earned money though, so I was hoping we could make a deal..."
    mc.name "What sort of deal [the_person.title]?"
    the_person.char "Well, I was thinking... we could make a deal where, instead of just stripping for you, we could do other things too."
    "You think about her proposal. It has been a while now since you started giving her your serums to test."
    mc.name "What kind of things do you have in mind, Mom?"
    "[the_person.possessive_title] stumbles over her words for a second. You can tell this is difficult for her to say, but her urges are getting the better of her."
    the_person.char "Well, after I get done stripping, I could please you, in whatever way you want..."
    "[the_person.possessive_title] blushes and looks down at the ground as she finishes her sentence."
    the_person.char "I could even stick it, back there, in my ass the way you like it..."
    "[the_person.possessive_title] has been exposed to your serums enough, you know that she probably wants it anal too. You decide to push the issue a bit."
    mc.name "You mean the way you like it?"
    "[the_person.possessive_title]'s cheeks turn even redder and she looks up at you."
    the_person.char "I'm sorry honey I just... I can't explain it, but lately I just find myself constantly fantasizing..."
    "She stops herself before she says too much."
    the_person.char "The bills are just really starting to pile up. I'm sorry, I know its wrong but, I promise I'll make it good for you!"
    menu:
        "Strip and ride me. -$1000" if mc.business.funds >= 1000:
            $ mc.business.funds += -1000
            "[the_person.possessive_title] smiles wide when you give her the money."
            the_person.char "Thank you [the_person.mc_title]! Now, are you ready a show?"
            call SB_free_strip_scene(the_person) from _call_SB_free_strip_scene_SBA40
            "Now that she is naked, [the_person.possessive_title] quickly grabs your hand and leads you to her bedroom. When you get to her bed, she shoves you down on your back."
            $ renpy.show(mom_bedroom.name,what=mom_bedroom.background_image)
            the_person.char "Oh god, I need this so bad honey. You just lay back and let momma take care of you now."
            "[the_person.possessive_title] quickly strips you down. She reaches into her nightstand and grabs some lube. She hands it to you."
            the_person.char "Here! Can you get me, you know... ready?"
            $ the_person.draw_person(position = "back_peek")
            "[the_person.possessive_title] turns away from you. You squirt a liberal amount of lube onto your hand and then reach up between her supple ass cheeks and spread it around her tight asshole."
            "You start to work one finger into her. She moans and starts to push back against you. When you push a second finger into her she gasps."
            $ the_person.change_arousal(15)
            the_person.char "Oh [the_person.mc_title], I've been thinking about this all week... I'm sorry I brought money into this... I won't ask you for money again!"
            #Cowgirl pose#
            $ the_person.draw_person(position = "cowgirl")
            the_person.char "Now, just let [the_person.title] take care of you. I'm gonna stick it into my most intimate hole now..."
            "[the_person.possessive_title] goes slow, but steadily slides down, impaling her sphincter on your throbbing erection. She bottoms out and moans loudly."
            call sex_description(the_person, SB_anal_cowgirl, make_bed(), 1, private= True, girl_in_charge = True) from _call_sex_description_SBA41
            if the_person.arousal > 100:
                the_person.char "Oh god, I came so hard..."
                "[the_person.possessive_title] collapses onto the bed next to you, exhausted from her anal cowgirl ride."
            else:
                the_person.char "Mmm, that was so good, thank you [the_person.mc_title]..."
                "[the_person.possessive_title] rolls off you and lays down on the bed next to you."
            $ the_person.reset_arousal()
            "You start to get up to go to your room, but [the_person.possessive_title] calls out to you as you start to get up."
            the_person.char "[the_person.mc_title]? Why don't you just stay in here tonight? [the_person.title] loves you... its okay!"
            "You slip back into bed next to her."
            $ SB_give_anal_role(the_person)
            $ SB_CALCULATE_RANDOM_EVENT_RATE()
            $ FETISH_ANAL_EVENT_INUSE = False
            "[the_person.possessive_title] has already fallen asleep. You can hear her murmuring in her dreams about taking stuff in her ass."
            "It seems your serums have given her an anal fetish!"
            "You cuddle up behind her and enjoy the heat of her soft flesh as you slowly drift off to sleep."

            call SB_process_overnight_no_events() from _SB_process_overnight_no_events_SBA42
            $ the_person.outfit = SB_anal_nude_outfit.get_copy()
            "The next morning, you slowly wake up. The bed next to you is cold. You look around and see [the_person.possessive_title] getting ready for the day in the bathroom."
            $ mc.change_location(mom_bedroom)
            #Position peek back
            $ the_person.draw_person(position = "walking_away")
            "You walk up behind [the_person.possessive_title] and wrap your arms around her. She arches her back against you as your hands roam across her chest."
            the_person.char "Good morning sleepy head..."
            "[the_person.possessive_title] starts to tremble at your touch."
            the_person.char "Look, about last night... I'm sorry I asked for money in exchange for... the wonderful thing we did afterword. I promise I won't do that again!"
            the_person.char "I know that we have this tradition that... every Friday night I work on the budget and things have been really tight lately."
            the_person.char "I was thinking we should start a new tradition! Every Friday night... Why don't we just plan on doing what we did. It will be something to look forward to with the stress of each week."
            "[the_person.title] begins to grind her hips up against you, nestling your now quickly hardening dick between her ass cheeks."
            the_person.char "Plus... god I just can't stop fantasizing about you... sticking it in me... back there."
            "You grab her hips and start to grind against her. Her breathing starts to get a bit heavier."
            the_person.char "[the_person.mc_title], last night [the_person.title] took care of you. Do you think this morning, you could take care of me?"
            "You smile to yourself."
            mc.name "Are you asking me to fuck you in your ass?"
            the_person.char "Yes... Please! Please [the_person.mc_title]! I don't know why I keep feeling this way, but I need you in my ass!"
            "You pick her up from behind and take her back to the bed. You throw her on the bed. She quickly gets on her hands and knees and starts wiggling her ass at you."
            #Draw doggystyle
            $ the_person.draw_person(position = "doggy")
            "You grab the lube leftover from the night before. You quickly apply another glob to [the_person.title]'s back side. You apply some more to your cock until it is good and slick."
            "You get yourself lined up with your mom's back passage. You slowly begin your anal penetration."
            the_person.char "That's it [the_person.mc_title]! Fuck me good!"
            call sex_description(the_person, SB_doggy_anal, make_bed(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBA43
            $ mc.current_stamina += -1
            if the_person.arousal > 100:
                "[the_person.title] lays there on the bed, speechless from your anal plundering."
            else:
                "[the_person.title] lays there on the bed"
            $ the_person.reset_arousal()
            mc.name "So... every friday night? I think I could get used to that..."
            "You can see [the_person.possessive_title]'s body quiver slightly at your words."
            mc.name "BUT, I am a man. I may have needs more often then that. Be ready for me with that amazing ass of yours anytime."
            "[the_person.possessive_title] meekly responds."
            the_person.char "Yes [the_person.mc_title]. You know it will be... take my ass, whenever you want. I'll be ready!"
            $ SB_mom_weekly_anal_action = Action("mom friday anal ", SB_mom_anal_pay_requirement, "SB_mom_anal_friday_label", the_person)
            $ mc.business.mandatory_crises_list.append(SB_mom_weekly_anal_action)
        "Strip and ride me. -$1000 (disabled)" if mc.business.funds <1000:
            pass
        "Not this week.":
            mc.name "Sorry [the_person.title], but I'm tight on cash right now as well. Maybe next week, okay?"
            "[the_person.possessive_title] nods and turns back to her bills."
            the_person.char "I understand sweetheart. Now don't let me keep you, I'm sure you were up to something important."
            $ SB_mom_weekly_pay_action = Action("mom anal pay", SB_mom_anal_pay_requirement, "SB_mom_anal_pay_label", the_person)
            $ mc.business.mandatory_crises_list.append(SB_mom_weekly_pay_action)
            $ the_person.review_outfit()

    hide screen person_info_ui
    $ the_person.reset_arousal()
    $ the_person.review_outfit() #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")

    return

#SBA50
label SB_mom_anal_friday_label(the_person):
    $ renpy.show(bedroom.name,what=bedroom.background_image)
    "You're hanging out in your room when you here [the_person.possessive_title] call form her room."
    the_person.char "[the_person.mc_title], are you home? It's Friday night! Can you come to my room?"
    mc.name "Sure, down in a second."
    show screen person_info_ui(the_person)
    $ renpy.show(mom_bedroom.name,what=mom_bedroom.background_image)
    $ the_person.outfit = lingerie_wardrobe.pick_random_outfit()
    $ the_person.draw_person(position = "stand4")
    "[the_person.title] is standing next to her bed. You quickly shut her door and lock it."
    the_person.char "[the_person.mc_title]! Hey, it time for our Friday night date! Are you ready for your show and, well you know what comes afterword..."
    "[the_person.title] smiles wide, waiting for your response."
    menu:
        "Strip and ride me." if mc.current_stamina > 0:

            "You sit down on the bed. [the_person.title] walks over to you."
            the_person.char "Remember, no touching! Atleast during this part. Now, are you ready a show?"
            call SB_free_strip_scene(the_person) from _call_SB_free_strip_scene_SBA50
            "Now that she is naked, [the_person.possessive_title] pushes you over, back on to the bed."
            "[the_person.possessive_title] quickly strips you down. She reaches into her nightstand and grabs some lube. She hands it to you."
            the_person.char "Here! Can you get me, you know... ready?"
            #facing away pose#
            $ the_person.draw_person(position = "back_peek")
            "[the_person.title] turns away from you. You squirt a liberal amount of lube onto your hand and then reach up between her supple ass cheeks and spread it around her tight asshole."
            "You start to work one finger into her. She moans and starts to push back against you. When you push a second finger into her she gasps."
            $ the_person.change_arousal(15)
            the_person.char "Oh god, I need this so bad honey. You just lay back and let momma take care of you now."
            #Cowgirl pose#
            $ the_person.draw_person(position = "cowgirl")
            the_person.char "Now, just let [the_person.title] take care of you. I'm gonna stick it into my most intimate hole now..."
            "[the_person.title] goes slow, but steadily slides down, impaling her sphincter on your throbbing erection. She bottoms out and moans loudly."
            $ mc.current_stamina += -1
            call sex_description(the_person, SB_anal_cowgirl, make_bed(), 1, private= True, girl_in_charge = True) from _call_sex_description_SBA51
            if the_person.arousal > 100:
                the_person.char "Oh god, I came so hard..."
                "[the_person.title] collapses onto the bed next to you, exhausted from her anal cowgirl ride."
            else:
                the_person.char "Mmm, that was so good, thank you [the_person.mc_title]..."
                "[the_person.possessive_title] rolls off you and lays down on the bed next to you."
            $ the_person.reset_arousal()

            "You cuddle up behind her and enjoy the heat of her soft flesh as you slowly drift off to sleep."

            call SB_process_overnight_no_events() from _SB_process_overnight_no_events_SBA52
            $ the_person.outfit = SB_anal_nude_outfit.get_copy()
            "The next morning, you slowly wake up. The bed next to you is cold. You look around and see [the_person.possessive_title] getting ready for the day in the bathroom."
            $ mc.change_location(mom_bedroom)
            #Position peek back
            $ the_person.draw_person(position = "walking_away")
            "You walk up behind [the_person.possessive_title] and wrap your arms around her. She arches her back against you as your hands roam across her chest."
            the_person.char "Good morning sleepy head..."
            "[the_person.possessive_title] starts to tremble at your touch."
            the_person.char "I love being so close to you... and so intimate..."
            "[the_person.title] begins to grind her hips up against you, nestling your now quickly hardening dick between her ass cheeks."
            the_person.char "I just want you to fuck my ass, all weekend long! Is there really anything wrong with that?"
            "You grab her hips and start to grind against her. Her breathing starts to get a bit heavier."
            the_person.char "Honey, last night [the_person.title] took care of you. Do you think this morning, you could take care of me?"
            "You smile to yourself."
            mc.name "Of course [the_person.title]. I'll fuck you in the ass, just the way you like it."
            the_person.char "Yes... Please! Please [the_person.mc_title]! Fuck me in the ass!"
            "You pick her up from behind and take her back to the bed. You throw her on the bed. She quickly gets on her hands and knees and starts wiggling her ass at you."
            #Draw doggystyle
            $ the_person.draw_person(position = "doggy")
            "You grab the lube leftover from the night before. You quickly apply another glob to [the_person.mc_title]'s back side. You apply some more to your cock until it is good and slick."
            "You get yourself lined up with [the_person.possessive_title]'s back passage. You slowly begin your anal penetration."
            the_person.char "That's it [the_person.mc_title]! Fuck me good!"
            call sex_description(the_person, SB_doggy_anal, make_bed(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBA53
            if the_person.arousal > 100:
                "[the_person.mc_title] lays there on the bed, speechless from your anal plundering."
            else:
                "[the_person.mc_title] lays there on the bed"
            $ the_person.reset_arousal()
            mc.name "Mmm, thanks [the_person.mc_title]. That ass is amazing. Next friday, right?"
            the_person.char "Yes [the_person.mc_title]. But don't feel like you HAVE to wait to take my ass. We can do it whenever you want. I'll be ready!"
            $ SB_mom_weekly_anal_action = Action("mom friday anal ", SB_mom_anal_pay_requirement, "SB_mom_anal_friday_label", the_person)
            $ mc.business.mandatory_crises_list.append(SB_mom_weekly_anal_action)
        "Strip and ride me. -$200 (disabled)" if mc.business.funds <100:
            pass
        "Not this week.":
            mc.name "Sorry [the_person.mc_title], work was hell and I'm exhausted. Maybe next week, okay?"
            "[the_person.possessive_title] frowns."
            the_person.char "I understand sweetheart. Now don't let me keep you, I'm sure you were up to something important."
            $ SB_mom_weekly_anal_action = Action("mom friday anal ", SB_mom_anal_pay_requirement, "SB_mom_anal_friday_label", the_person)
            $ mc.business.mandatory_crises_list.append(SB_mom_weekly_anal_action)

    hide screen person_info_ui
    $ the_person.reset_arousal()
    $ the_person.review_outfit() #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")

    return

#SBA60
label SB_lily_anal_dp_fetish_label(the_person):
    "As you are finishing up with work for the day, you get a text on your phone. It is from Lily, [the_person.possessive_title]."
    the_person.char "Hey [the_person.mc_title]! Can you do me a favor? Meet me at the mall when you get off work. I need your help with something..."
    "You let her know you'll be there. You quickly finish up with your work and head over to the mall."
    $ renpy.show(mall.name,what=mall.background_image)
    "When you get to the mall, you look around for a minute, then spot Lily. She waves to you then comes running over to you, giving you a big hug."
    $ the_person.draw_person(position = "stand4")
    the_person.char "Hey! Thanks for coming with me! I need your help with something!"
    "You are a little hesitant. She wants you to go shopping with her?"
    mc.name "Are you sure you need me for this?"
    "She gives you a mischevious smile."
    the_person.char "Definitely! Don't worry, you'll be glad you came when you see where we are going."
    "Lily grabs you by the hand and leads you into the mall. It seems any inhibition she might have previously had being seen with her [the_person.mc_title] has vanished after being corrupted by your serums."
    "You are almost surprised when she leads you into the sex shop. The owner greets you as you walk in."
    if starbuck.sluttiness > 50 or starbuck.love > 30:
        $ starbuck.draw_person(emotion = "happy")
        starbuck.char "Hello! Welcome to... Oh hey [the_person.mc_title]! Good to see you! Oh and you brought a partner! Hi I'm Starbuck!"
    else:
        $ starbuck.draw_person(emotion = "happy")
        starbuck.char "Hello! Welcome to Starbuck's Sex Shop! It's so great to see a couple come in."
    starbuck.char "Is there anything I can help you find?"
    $ the_person.draw_person(position = "stand4")
    "Lily takes the lead."
    the_person.char "Yeah so, I was wondering, do you sell a special type of strap on that came be used to... umm... strap on to a guy so he can fuck your pussy and ass at the same time?"
    "You can barely believe your ears. You knew that the serums you had been giving Lily were starting to really corrupt her, but you had no idea she was ready for something like this."
    $ starbuck.draw_person(emotion = "happy")
    starbuck.char "Oh! I've got just the thing! Follow me!"
    $ starbuck.draw_person(position = "walking_away")
    "Starbuck leads you over to a selection of dildos. They have special straps that go around the man so that they are secured, just below penis, and can be used for double penetration."
    $ the_person.draw_person(position = "stand4")
    the_person.char "Hmm... I don't know, what do you think about this one?"
    "Lily picks up one. It has an extra little vibrating unit."
    mc.name "That looks pretty good, actually."
    "Lily takes it up to the counter."
    $ starbuck.draw_person(emotion = "happy", position = "stand2")
    starbuck.char "Great! This one is actually on sale, but I hadn't gotten around to marking it yet. Its only $20!"
    "You decide to offer to pay for it."
    mc.name "Here, let me just put this on the company card..."
    $ mc.business.funds += -20
    starbuck.char "Okay! You're all set! Do you two want to try it out? I have a special room in the back, sometimes people just can't WAIT to get home before trying out a purchase!"
    $ the_person.draw_person(position = "stand4")
    "Lily quickly speaks up."
    the_person.char "That would be great! Come one [the_person.mc_title]!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] grabs your hand and you follow her to the backroom. It has a familiar smell of body fluids and sweat."
    $ the_person.draw_person(position = "stand4")
    "Come on [the_person.mc_title], I can't wait to feel you fuck me with this thing on..."
    "[the_person.possessive_title] quickly strips, eager to get started."
    $ the_person.outfit = SB_anal_nude_outfit.get_copy()
    $ the_person.draw_person(position = "stand4")
    "You get yourself naked as well. On a nearby shelf you spot a bulk size bottle of intimate lube."
    "[the_person.possessive_title] gets down on her knees and starts to secure the toy to your cock."
    $ the_person.draw_person(position = "blowjob")
    mc.name "Mmm, you look amazing on your knees [the_person.title]."
    "[the_person.possessive_title] looks up at you."
    the_person.char "Yeah, you like it anytime I'm near your dick. Trust me, I'd love to blow you, but I've got something else in mind..."
    $ the_person.draw_person(position = "doggy")
    "[the_person.possessive_title] turns over and gets on her hands and knees in front of you on the floor. She lifts her hips and starts waving her ass in the air."
    "You grab a few squirts of the lube and get your cock and the dildo all lubed up. You grab another squirt and start working it in her rear entry."
    the_person.char "Mmm... that is so good... I don't know why, lately I just haven't been to stop thinking about your cock fucking me back there..."
    "You've been having her test some of your anal enhancing serums. It sounds like she might be developing an anal fetish!"
    "You push two fingers into her tight rump. They grip and squeeze at your fingers."
    $ the_person.change_arousal(10)
    the_person.char "Oh! That feels good... but I'm ready for you. Let me have it [the_person.mc_title]!"
    "You use your hand to line yourself cock up with her puckered hole. She reaches down and grabs the dildo and lines it up with her pussy."
    "With one slow, smooth motion, you push your cock past her well lubed sphincter. It goes in with a small pop, and then you continue with a slow thrust until your cock is buried in her ass."
    the_person.char "Fuck! Holy hell... [the_person.mc_title] that is intense! I've never felt... I'm so full!!!"
    "Going tantalizingly slow, you pull yourself mostly out, then back into her buttery smooth back door."
    the_person.char "Okay... Go slow... but I'm ready!"
    call sex_description(the_person, SB_doggy_anal_dildo_dp, make_floor(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBA60
    if the_person.arousal > 150:
        "[the_person.possessive_title] is a sweaty, heaving mess. You know she orgasmed multiple times from the intense sensations of the double penetration."
        "She looks back at you in awe."
    elif the_person.arousal > 100:
        "[the_person.possessive_title] is laying on the floor, exhausted from the intensity of the double penetration."
        "She looks back at you and smiles"
    the_person.char "[the_person.mc_title]... That felt amazing. I'm not sure though... are we going to able to keep this from mom? I don't think I can stay quiet enough when I'm getting fucked in both holes like that..."
    "You give her a reassuring smile."
    mc.name "Don't worry [the_person.title], we'll be careful."
    the_person.char "Good... because lately I've just been craving you so bad. We don't have to always use the strap on. But just thinking about you fucking my ass makes me so horny."
    $ SB_give_anal_role(the_person)
    $ SB_CALCULATE_RANDOM_EVENT_RATE()
    $ FETISH_ANAL_EVENT_INUSE = False
    #TODO come back and change other events involving lily to account for her anal fetish.
    "It is pretty clear from the way she got off while you were fucking her and the way she was talking afterwards, you're convinced [the_person.possessive_title] has developed an anal fetish!"
    $ mc.change_location(sex_store)
    "After you both clean up, you leave the back room of the sex shop."
    $ starbuck.draw_person(emotion = "happy")
    starbuck.char "Have a good day! Thanks for shopping at Starbuck's sex shop!"
    if starbuck.sluttiness > 50:
        "You wave goodbye to Starbuck. You note some telltale signs of arousal, flushed cheeks, and you can see her nipples are erect."
        "Was she watching you somehow? Oh well, you decide to head out."
    else:
        "You wave goodbye to Starbuck and head out."
    return
