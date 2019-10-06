init 1 python:
    def SB_fetish_anal_requirement():
        if time_of_day == 3:
            if mc.current_stamina > 0:
                if mc.business.is_open_for_business():
                    if mc.is_at_work():
                        return True
        return False

    def SB_mom_anal_pay_requirement():
        if time_of_day == 4 and day%7 == 4: #It is the end of the day on friday
            return True
        return False

    def SB_starbuck_anal_requirement():
        if starbuck.shop_investment_rate == 6.0:
            if time_of_day == 3 and day%7 != 4: #It is the end of the day on friday
                return True

        return

    def SB_fetish_anal_staylate_event_requirement():
        if time_of_day == 3:
            return True
        return False

        #Mandatory Events
    SB_lily_anal_dp_fetish = Action("Lily Anal Sex", SB_fetish_anal_requirement, "SB_lily_anal_dp_fetish_label")
    SB_mom_anal_fetish = Action("Mom Anal Sex", SB_mom_anal_pay_requirement, "SB_mom_anal_pay_label")
    SB_fetish_anal_crisis = Action("Loves Anal Sex.", SB_fetish_anal_requirement, "SB_fetish_anal_label")
    SB_fetish_anal_staylate_event = Action("Employee stays late", SB_fetish_anal_staylate_event_requirement, "SB_fetish_anal_staylate_event_label")
    SB_mom_weekly_anal_action = Action("mom friday anal ", SB_mom_anal_pay_requirement, "SB_mom_anal_friday_label")
    SB_starbuck_anal_intro_event = Action("Starbuck Anal Sex", SB_starbuck_anal_requirement, "SB_starbuck_anal_intro")


    SB_anal_outfit = Outfit("A Special Night")
    SB_anal_outfit.add_upper(lace_bra.get_copy(),colour_pink)
    SB_anal_outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
    SB_anal_outfit.add_feet(high_heels.get_copy(), colour_pink)

    SB_anal_nude_outfit = Outfit("Nude")

    SB_list_of_ass_positions = []           #This is a list of positions that show off a person's ass. Can grab one randomly for when a girl wants to show off ass specifically
    SB_list_of_ass_positions.append("back_peek")
    SB_list_of_ass_positions.append("standing_doggy")
    SB_list_of_ass_positions.append("doggy")
    SB_list_of_ass_positions.append("walking_away")

    def SB_get_random_ass_position():
        return get_random_from_list(SB_list_of_ass_positions)


#SBA1
label SB_fetish_anal_label(the_person):
    "You are just finishing up with business for the day when you hear a pleasant voice call out to you."
    the_person.char "Hey [the_person.mc_title]."
    #$ the_person.outfit = SB_anal_outfit.get_copy()
    $ the_person.draw_person()

    ###Draw the girl###
    "You give her a quick wave as she walks up to you."
    the_person.char "Hey, I really hate to bug you but... "
    "She places extra emphasis on the word but before moving on."
    the_person.char "I was wondering if you would stay for a bit after work? I need help with something."
    "[the_person.possessive_title] looks at you with hopeful eyes."
    menu:
        "Accept" if mc.current_stamina > 0:  #This begins the sex scene
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
            $ the_person.special_role.append(anal_fetish_role)
            $ SB_CALCULATE_RANDOM_EVENT_RATE()
        "Refuse":
            the_person.char "I'm sorry to hear that..." #TODO finish this
            $ the_person.change_obedience(-10)
            $ the_person.change_happiness(-10)
            "[the_person.possessive_title] quickly sulks off."
        "Too Tired" if mc.current_stamina == 0:     # na stamina for the player to induce fetish
            "[the_person.possessive_title] is surprised by your answer."
            $ the_person.change_obedience(-5)
            $ the_person.change_happiness(-5)
            the_person.char "Oh! I'm sorry... I didn't think about that. Maybe tomorrow then?"
            "[the_person.possessive_title] quickly sulks off."

    $ FETISH_ANAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()
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
    return

init 2 python:
    def SB_fetish_anal_recurring_requirement():
        if time_of_day == 3:
            if mc.is_at_work():
                for person in mc.business.get_employee_list():
                    if SB_check_fetish(person, anal_fetish_role):
                        return True
        return False

    SB_fetish_anal_recurring_crisis = Action("Anal Fetish Recurring Crisis",SB_fetish_anal_recurring_requirement,"SB_fetish_anal_recurring_label")
    crisis_list.append([SB_fetish_anal_recurring_crisis, 5])

#SBA3
label SB_fetish_anal_recurring_label():
    $ meets_fetish_list = []
    python:
        for person in mc.business.get_employee_list():
            if SB_check_fetish(person, anal_fetish_role):
                meets_fetish_list.append(person)

    $ the_person = get_random_from_list(meets_fetish_list)

    "As you are packing up your stuff to head home for the day, you hear [the_person.possessive_title]'s sweet voice call out to you."

    if mc.business.is_open_for_business():
        $ the_person.draw_person()
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

    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False)
    $ renpy.scene("Active")
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
        $ clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True) #She's slutty enough that she wants to tease you a little more
        if rand_strip_desc == 0:
                if clothing is not None:
                    "[the_person.possessive_title] pulls at her [clothing.name] seductively."
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
                if clothing is not None:
                    "[the_person.possessive_title] slips a hand under her [clothing.name] and starts to pull it off."
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

#SBA40
label SB_mom_anal_pay_label():
    $ the_person = mom
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You're getting ready for bed when [the_person.possessive_title] calls from downstairs."
    the_person.char "[the_person.mc_title], could we talk for a moment?"
    mc.name "Sure, down in a second."
    $ mc.change_location(kitchen)
    $ mc.location.show_background()    
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
            $ mom_bedroom.show_background()
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
            $ the_person.special_role.append(anal_fetish_role)
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
            call sex_description(the_person, doggy_anal, make_bed(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBA43
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
            $ mc.business.mandatory_crises_list.append(SB_mom_weekly_anal_action)
        "Strip and ride me. -$1000 (disabled)" if mc.business.funds <1000:
            pass
        "Not this week.":
            mc.name "Sorry [the_person.title], but I'm tight on cash right now as well. Maybe next week, okay?"
            "[the_person.possessive_title] nods and turns back to her bills."
            the_person.char "I understand sweetheart. Now don't let me keep you, I'm sure you were up to something important."
            $ mc.business.mandatory_crises_list.append(SB_mom_weekly_pay_action)
            $ the_person.review_outfit(show_review_message = False)

    $ FETISH_ANAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()

    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
    $ mc.location.show_background()
    $ renpy.scene("Active")

    return

#SBA50
label SB_mom_anal_friday_label():
    $ the_person = mom
    $ bedroom.show_background()
    "You're hanging out in your room when you here [the_person.possessive_title] call form her room."
    the_person.char "[the_person.mc_title], are you home? It's Friday night! Can you come to my room?"
    mc.name "Sure, down in a second."
    $ mom_bedroom.show_background()
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
            call sex_description(the_person, doggy_anal, make_bed(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBA53
            if the_person.arousal > 100:
                "[the_person.mc_title] lays there on the bed, speechless from your anal plundering."
            else:
                "[the_person.mc_title] lays there on the bed"
            $ the_person.reset_arousal()
            mc.name "Mmm, thanks [the_person.mc_title]. That ass is amazing. Next friday, right?"
            the_person.char "Yes [the_person.mc_title]. But don't feel like you HAVE to wait to take my ass. We can do it whenever you want. I'll be ready!"
            $ mc.business.mandatory_crises_list.append(SB_mom_weekly_anal_action)
        "Strip and ride me. -$200 (disabled)" if mc.business.funds <100:
            pass
        "Not this week.":
            mc.name "Sorry [the_person.title], work was hell and I'm exhausted. Maybe next week, okay?"
            "[the_person.possessive_title] frowns."
            the_person.char "I understand sweetheart. Now don't let me keep you, I'm sure you were up to something important."
            $ mc.business.mandatory_crises_list.append(SB_mom_weekly_anal_action)

    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
    $ mc.location.show_background()
    $ renpy.scene("Active")
    return

#SBA60
label SB_lily_anal_dp_fetish_label():
    $ the_person = lily # make sure we use lily for the event
    "As you are finishing up with work for the day, you get a text on your phone. It is from Lily, [the_person.possessive_title]."
    the_person.char "Hey [the_person.mc_title]! Can you do me a favor? Meet me at the mall when you get off work. I need your help with something..."
    "You let her know you'll be there. You quickly finish up with your work and head over to the mall."
    $ mall.show_background()
    "When you get to the mall, you look around for a minute, then spot Lily. She waves to you then comes running over to you, giving you a big hug."
    $ the_person.draw_person(position = "stand4")
    the_person.char "Hey! Thanks for coming with me! I need your help with something!"
    "You are a little hesitant. She wants you to go shopping with her?"
    mc.name "Are you sure you need me for this?"
    "She gives you a mischevious smile."
    the_person.char "Definitely! Don't worry, you'll be glad you came when you see where we are going."
    "Lily grabs you by the hand and leads you into the mall. It seems any inhibition she might have previously had being seen with her [the_person.mc_title] has vanished after being corrupted by your serums."
    "You are almost surprised when she leads you into the sex shop. The owner greets you as you walk in."
    $ sex_store.show_background()
    if starbuck.sluttiness > 50 or starbuck.love > 30:
        $ starbuck.draw_person(emotion = "happy")
        starbuck.char "Hello! Welcome to... Oh hey [the_person.mc_title]! Good to see you! Oh and you brought a partner! Hi I'm [starbuck.title]!"
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
    $ the_person.special_role.append(anal_fetish_role)

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

    $ FETISH_ANAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()

    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False)
    $ renpy.scene("Active")
    return

#SBA70
label SB_starbuck_anal_intro():
    $ the_person = starbuck

    "You get a text message from [the_person.title]."
    the_person.char "Hey partner! I was just closing up the shop, butt craving something a little more real than this... want to swing by?"

    $ the_person.outfit = SB_anal_nude_outfit.get_copy()
    $ the_person.draw_person(position = SB_get_random_ass_position())
    "She attached a picture. It looks like she is bending over her counter. Between her ass cheeks you spy a good sized glass butt plug!"
    "You decide this is too good of an opportunity to pass up. You head over to the sex shop."
    #TODO Change locations to the sex shop

    $ mc.change_location(sex_store)
    $ mc.location.show_background()
    
    "The door is locked so you give it a knock. [the_person.possessive_title] appears in the glass and quickly opens it for you."
    the_person.char "[the_person.mc_title]! You came!"
    "She gives you a quick wink."
    the_person.char "Hopefully thats not the last time I say that tonight..."
    "You share a quick laugh."
    the_person.char "So... I take it you got my picture? We just got that plug in stock. As soon as I saw it I knew I had to try it."
    mc.name "Yeah... still got it in?"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and begins to slowly walk away from you."
    the_person.char "Maybe..."
    "She slowly bends over the counter. The dark glass butt plug appears as her cheeks spread."
    $ the_person.draw_person(position = "standing_doggy")
    the_person.char "I've had it in all day... but all I've been able to think about is your amazing cock, ramming up inside me, filling me up!"
    "You walk up behind her and begin to run your hands along her delicious hips. You can see goosebumps break out along her skin."
    mc.name "Thinking of getting fucked in the ass? My my, [the_person.possessive_title], you seem to have quite the affinity for anal these days?"
    "[the_person.title] looks back at you."
    the_person.char "It's true... I don't understand why, but lately I just find myself cosntantly daydreaming about taking it in the ass. I can't even masturbate anymore without some kind of plug back there!"
    "Sounds like [the_person.title] has developed an anal fetish!"
    "You reach down and start to slowly play with her plug. Her body stiffens as she feels it begin to slowly work in and out of her. She lets out a long, low moan."
    $ the_person.change_arousal(10)
    the_person.char "Oh thank god... Oh [the_person.mc_title]."
    mc.name "Don't worry, [the_person.title]. I'm just the man to help you with all these urges you've been dealing with."
    "You slowly pull the plug out and take a look. She's already got a lot of lube worked in and around her asshole."
    "You push the plug back up against [the_person.possessive_title]'s pucker. It gives way easily and slides right in."
    $ the_person.change_arousal(10)
    the_person.char "Mmm, that feels good [the_person.mc_title], but you don't have to tease me!"
    "You decide to oblige her. You leave the plug in as you quickly undress yourself. Your cock aches in anticipation, ready for another plunge into [the_person.possessive_title]'s backdoor."
    "With her plug still in, you slide your cock up and down a few times between her cheeks. She pushes herself back against you, grinding her hips against yours."
    "Her soft, pliant cheeks feel great pushed up against your hips. You reach down and slowly pull out her plug and set it on the counter."
    "With her hip in one hand and your dick in the other, you line yourself up and slowly push into [the_person.possessive_title]'s tender behind."
    "You lean forward and whisper into her ear."
    mc.name "Hey [the_person.title]. I'm about to fuck your ass now, just the way you like."
    "Her body shudders from your dirty talk. She wiggles her ass back up against you."
    the_person.char "It's about fucking time! Give it to me good, [the_person.mc_title], you know I can take it!"
    call sex_description(the_person, doggy_anal, make_bed(), 1, private= True, girl_in_charge = False) from _call_sex_description_SBA70
    $ the_person.sexy_opinions["anal sex"] = [FETISH_OPINION_VALUE, True]
    $ the_person.special_role.append(anal_fetish_role)
    $ the_person.sex_skills["Anal"] = 6
    "It's pretty clear from her sexual performance and the way she talks to you, that [the_person.title] has developed an anal fetish."
    $ the_person.reset_arousal()
    "[the_person.title] takes a few minutes to recover. She eventually stands up and turns to you."
    $ the_person.draw_person(position = "stand4")
    the_person.char "Hey so, what you said earlier about, you know, being the man to help me with all these urges I've been dealing with lately... were you being serious?"
    mc.name "Of course. We've already been through so much together, you know I'd be glad to help you out!"
    "She thinks for a moment."
    the_person.char "Ok, stay right here! I'm going to go get something..."
    $ the_person.draw_person(position = "walking_away")
    "You watch [the_person.possessive_title]'s shapely bottom as she walks away."
    "You are definitely looking forward to fucking that ass as much as possible."
    "She is gone for several minutes, but [the_person.title] soon comes back."
    $ the_person.draw_person(position = "stand2")
    "She hands you small card that has a username and password on it, and a logo for some company at the top that advertises being the best in teledildonics."
    mc.name "Thanks? I'm not sure what this is..."
    the_person.char "Well, that would be the sign in info for you to control, remotely from your phone, the vibrating plug I have in my ass right now..."
    "Wow! This should be interesting!"
    "[the_person.title] helps you download the app and sign in. When you finish signing in you can see all kinds of information about the plug."
    "Apparently it has some kind of heat sensor, so it can tell whether it is inserted or not and how long its been in."
    "Theres an icon for making the plug vibrate, and it can even tell when it is moving in and out rapidly so you can see when she is masturbating with it!"
    "You tap the little vibrate icon. [the_person.title] jumps."
    the_person.char "Mmm! That felt good! I guess we got it working!"
    $ the_person.change_arousal(7)
    "This should allow for some... unique experiences!"
    the_person.char "Well, I'd better get home. Feel free to uh, check in on me whenever you want [the_person.mc_title]!"
    "You say goodbye and head out so she can finish locking up the sex shop."

    $ FETISH_ANAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()
    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False)
    $ renpy.scene("Active")
    return

#SBA80
label SB_starbuck_anal_swing_demo(the_person):
    $ the_person = starbuck
    mc.name "Hey, I was just wondering, you wanna go for a swing in the back?"
    "[the_person.possessive_title] gives you a big smile."
    the_person.char "That sounds great!"
    $ scene_private = True
    #TODO determine if there are people here
    if len(mc.location.people) >= 2: #If Starbuck is not the only girl
        the_person.char "I've got an idea! I've got a few customers in here... want to do a demonstration for anyone who wants to attend?"
        "You consider her proposition carefully."
        menu:
            "Do a demo!":
                mc.name "That would be hot! Let's do it!"
                the_person.char "Yes! Okay, you head back there, I'll get ready, make an announcement, then meet you back there, okay?"
                "You head to the back room. You make sure the swing is in a good position for people to be watch you... demonstrate it."
                "Soon you hear [the_person.title] making her announcement."
                the_person.char "Attention everyone! In five minutes, myself and a partner will be demonstrating one of the sex swingsets that we have for sale! Feel free to come watch and ask questions!"
                $ the_person.outfit = SB_anal_nude_outfit.get_copy()
                $ the_person.draw_person(position = "stand4")
                "Soon, [the_person.title] appears in the doorway, completely naked."
                #TODO: Determine if anyone wants to watch
                $ audience_list = []
                python:
                    check_person = None
                    for girl in mc.location.people:
                        if girl != the_person:
                            if girl.sluttiness > 60:
                                audience_list.append(girl)
                            else:
                                mc.location.move_person(girl, mall)
                if len(audience_list) < 1:  #No one wants to watch
                    the_person.char "Well, I made my announcement, but it doesn't look like anyone is interested in watching..."
                    "You can hear the disappointment in her voice."
                    mc.name "Hey, their loss. Don't worry, it'll still feel just as good when I slide into that amazing ass of yours..."
                    "Her nipple stiffen slightly when she hears what you say."
                    the_person.char "Mmm... I can feel it already... Probably because I still have this thing in!"
                    $ the_person.draw_person(position = "back_peek")
                    "[the_person.possessive_title] turns away from you. You see her plug nestled between her cheeks."
                    "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when its fully removed."
                    mc.name "Alright, let's replace that with something a little... meatier... shall we?"
                    $ the_person.draw_person(position = "sitting")
                    "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
                    "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
                    the_person.char "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"
                else:   #People watch
                    the_person.char "Here they come! This is gonna be great!"
                    "[the_person.possessive_title] looks genuinely excited! She walks over next to swing and nonchalantly takes out her plug and sets it to the side."
                    $ get_random_from_list(mc.location.people).draw_person(position = "stand4")
                    "You watch as people begin to walk into the room..."
                    "You are about to fuck [the_person.title], in the ass, in front of customers..."
                    "You can't believe this is actually happening!"
                    $ the_person.draw_person(position = "sitting")
                    "[the_person.title] makes begin to speak. When you turn to her she is already seated in the swing. You quickly move around behind her."
                    the_person.char "So, today, my wonderful partner and I are going to demonstrate proper technique on this swing..."
                    "You zone out for a bit as she begins explaining the basics, how to set it up, etc."
                    "You can't wait to feel yourself slide into her tight rear end. You start to day dream a bit."
                    the_person.char "Alright, [the_person.mc_title], go ahead, I think we are ready for the demonstration."
                    "Hearing her mention you grabs your attention. You slide up behind her, your hands squeezing her pliant cheeks."
                    "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
                    "She whimpers back at you."
                    the_person.char "Alright, lets give em a good show."
                    $ scene_private = False
                    pass
            "Keep it private.":
                mc.name "I think I'd like to keep it between me and you, if that's okay."
                "You can tell she is a little disappointed, but she quickly smiles again when she remembers that you are about to fuck her in the ass..."
                the_person.char "Okay! Lets go!"
                $ the_person.draw_person(position = "walking_away")
                "[the_person.possessive_title] walks to the back room. You quickly follow her."
                "You get to the back room and [the_person.title] turns to you."
                the_person.char "Alright. Before we get started, let me get ready. You should probably get naked too!"
                $ the_person.draw_person( position = "stand2")
                "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."
                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice is not None:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
                    $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                "When you finish stripping, she turns her back to you."
                $ the_person.draw_person(position = "back_peek")
                mc.name "It's going to feel so good when I slide into that amazing ass of yours..."
                "She gives her ass a little wiggle."
                the_person.char "Mmm... I can feel it already... Probably because I still have this thing in!"
                "[the_person.possessive_title] pulls her cheeks apart. You can see her plug nestled between her cheeks."
                "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when its fully removed."
                mc.name "Alright, let's replace that with something a little... meatier... shall we?"
                $ the_person.draw_person(position = "sitting")
                "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
                "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
                the_person.char "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"
    else:
        the_person.char "Okay! Lets go!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] walks to the back room. You quickly follow her."
        "You get to the back room and [the_person.title] turns to you."
        the_person.char "Alright. Before we get started, let me get ready. You should probably get naked too!"
        $ the_person.draw_person( position = "stand2")
        "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."
        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        while strip_choice is not None:
            $ the_person.draw_animated_removal(strip_choice)
            "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        "When you finish stripping, she turns her back to you."
        $ the_person.draw_person(position = "back_peek")
        mc.name "It's going to feel so good when I slide into that amazing ass of yours..."
        "She gives her ass a little wiggle."
        the_person.char "Mmm... I can feel it already... Probably because I still have this thing in!"
        "[the_person.possessive_title] pulls her cheeks apart. You can see her plug nestled between her cheeks."
        "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when its fully removed."
        mc.name "Alright, let's replace that with something a little... meatier... shall we?"
        $ the_person.draw_person(position = "sitting")
        "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
        "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
        the_person.char "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"

    call sex_description(the_person, SB_anal_swing, SB_make_swing(), 1, private= scene_private, girl_in_charge = False) from _call_sex_description_SBA080

    #TODO the rest of this scene.
    if scene_private:
        the_person.char "Oooh, fuck that was just what I needed."
        $ the_person.draw_person(position = "stand3")
        "[the_person.possessive_title] slowly stands up. Her knees are a little wobbly."
        "She grabs her plug. She reaches back and slowly re-inserts it with a moan."
        the_person.char "Mmm, that feels nice. Alright, you run a long now! Don't worry about me, I'll get cleaned up and back out front in a quick minute."
        "You excuse yourself as [the_person.title] heads to the bathroom."
    else:
        $ random_person = get_random_from_list(mc.location.people)
        "You look around the room. All eyes are on you and [the_person.title]."
        $ random_person.draw_person (position = "stand4")
        "To one side you see [random_person.title], clearly touching herself, after watching you and [the_person.title] fuck."
        random_person.char "Oh wow... maybe I should... I wonder if..."
        "She is muttering things under her breath as she touches herself. She closes her eyes and you see her body tense as she orgasms."
        $ random_person.change_happiness(5)
        $ the_person.draw_person(position = "sitting")
        "[the_person.title] has noticed and is smiling wide."
        the_person.char "So... as you can see... the swing makes a wide variety of sexual maneuvers possible... For anyone who attended, I'd like to offer a discount!"
        "You hear a few murmurs of approval. [the_person.title] looks up at you and winks."
        the_person.char "Thanks [the_person.mc_title], that was amazing. Alright, you run a long now! Don't worry about me, I'll get cleaned up and back out front in a quick minute."
        "You excuse yourself. You wonder if this will help sell the swing any!"

    $ the_person.reset_arousal()
    call advance_time from _call_advance_SB_Anal_call_time_SBA081

    return
