init 1 python:
    def SB_fetish_vaginal_requirement():
        if mc_asleep():
            if mc.energy > 30:  #Must have the energy to handle a long sexy night
                return True
        return False

    SB_vaginal_outfit = Outfit("A Special Night")
    SB_vaginal_outfit.add_upper(lace_bra.get_copy(),colour_black)
    SB_vaginal_outfit.add_feet(garter_with_fishnets.get_copy(), colour_black)
    SB_vaginal_outfit.add_feet(high_heels.get_copy(), colour_black)

    SB_vaginal_nude_outfit = Outfit("Nude")

    #colour_sky_blue
    SB_vaginal_lily_outfit = Outfit("Lily's Special Night")
    SB_vaginal_lily_outfit.add_lower(thong.get_copy(), colour_sky_blue)
    SB_vaginal_lily_outfit.add_upper(thin_bra.get_copy(),colour_sky_blue)
    SB_vaginal_lily_outfit.add_lower(mini_skirt.get_copy(), colour_black)
    SB_vaginal_lily_outfit.add_upper(tube_top.get_copy(), colour_sky_blue)
    SB_vaginal_lily_outfit.add_feet(fishnets.get_copy(), colour_black)
    SB_vaginal_lily_outfit.add_feet(slips.get_copy(), colour_black)
    SB_vaginal_lily_outfit.add_accessory(lipstick.get_copy(), colour_red)

    def SB_fetish_mom_vaginal_requirement():
        if mc_asleep():
            if mc.energy > 30:
                return True
        return False

    def SB_fetish_lily_vaginal_requirement():
        if mc_asleep():
            if mc.energy > 30:
                return True
        return False

    def SB_fetish_vaginal_event_requirement():
        if mc_asleep():
            return True
        return False

    def add_breed_me_collar_to_base_outfit(person):
        person.base_outfit.remove_all_collars()

        bm_collar = breed_collar.get_copy()
        bm_collar.colour = [1,.41,.71,.9]
        bm_collar.pattern = "Pattern_1"
        bm_collar.colour_pattern = [.1,.1,.1,.9]
        person.base_outfit.add_accessory(bm_collar)
        return

    SB_fetish_mom_vaginal_crisis = Action("Mom Loves Vaginal Sex", SB_fetish_mom_vaginal_requirement, "SB_fetish_mom_vaginal_label")
    SB_fetish_lily_vaginal_crisis = Action("Lily Loves Vaginal Sex", SB_fetish_lily_vaginal_requirement, "SB_fetish_lily_vaginal_label")
    SB_fetish_vaginal_crisis = Action("Loves Vaginal Sex", SB_fetish_vaginal_requirement, "SB_fetish_vaginal_label")
    SB_fetish_vaginal_event = Action("Vaginal Sex Visit", SB_fetish_vaginal_event_requirement, "SB_fetish_vaginal_event_label")


#SBV1
label SB_fetish_vaginal_label(the_person):
    "*Ding Dong*"
    "You're roused from your bed by a ring on your doorbell."
    "You head to your front door and see [the_person.possessive_title] standing there... outside... in a very provocative outfit."
    $ the_person.apply_outfit(SB_vaginal_outfit)
    $ the_person.draw_person()
    ###Draw the girl###
    "You quickly open the door and invite her inside."
    "To avoid any situations with [mom.possessive_title] or [lily.possessive_title], you quickly invite her to your room."
    "Once you close your door, [the_person.possessive_title] quickly turns and embraces you."
    the_person.char "Oh, [the_person.mc_title], I'm sorry to just come over without asking like this but... I was at home... by myself... and I just..."
    "She stumbles over her words for a second."
    the_person.char "Oh geeze... I just couldn't stop thinking about how good it feels when you fuck me!"
    "You are surprised, [the_person.possessive_title] isn't usually this forward."
    the_person.char "So I thought... surely [the_person.mc_title] has physical needs too... maybe I should just go over there and... maybe we could come to an agreement?"
    the_person.char "I'll take care of your needs whenever you need it... if you do the same for me?"
    "[the_person.possessive_title] looks at you with hopeful eyes."
    menu:
        "Accept":  #This begins the sex scene
            ###Set vaginal skill to 6
            $ the_person.sex_skills["Vaginal"] = 6
            "[the_person.possessive_title] walks over to the windows and looks out of it. You see her hips move side to side for a second and the peaks back at you."
            $ the_person.draw_person(position = "back_peek")
            the_person.char "It so pretty out tonight... Why don't you come over here?"
            "You walk over and stand behind [the_person.possessive_title] as she looks by the window."
            ###Sex Scene, standing variant at window###
            "You put your hands on her hips. She sticks her ass out slightly as you line yourself and then gently push your cock inside her."
            call fuck_person(the_person, start_position = SB_facing_wall, start_object = make_window(), skip_intro = True) from _call_fuck_person_SBV11

            "[the_person.possessive_title] walks over to your bed and lays down on her back and takes off any remaining clothing."
            $ the_person.apply_outfit(SB_vaginal_nude_outfit)
            $ the_person.draw_person(position = "missionary")
            ###If The girl is still wearing any clothing, have her take it off###
            "You join her on the bed. She raises her arm and you lay your head down on her breast."
            "You both catch your breath and just enjoy the warmth of each other's bodies."
            "After a few minutes of cuddling, you reach your hand up and begin to fondle her other breast."
            "[the_person.possessive_title] moans and runs her hands through your hair."
            "You turn your head and begin to lick and suck her nipple."
            ###The girl arousal + 20
            $ the_person.change_arousal(20)
            the_person.char "That feels so good [the_person.mc_title]... are you about ready for round two?"
            "You roll over on top of [the_person.possessive_title]. She wraps her arms around you as you slowly sink your cock into her moist cunt."
            ###Sex scene, missionary###   ###TODO: consider writing a variant of this because the default intro is going to be confusing###
            call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True) from _call_fuck_person_SBV12

            the_person.char "Oh god [the_person.mc_title], tonight has been incredible... excuse me for a second."
            $ the_person.draw_person(position = "walking_away")
            ###The girl walking away draw
            "[the_person.possessive_title] excuses herself to your restroom. After a few minutes she comes back. She sits down on the side of the bed."
            $ the_person.draw_person(position = "sitting")
            ###The girl sitting###
            the_person.char "Why don't... why don't you come sit on the side of the bed? I know you're tired but... I could really go for one more round..."
            "You sit up and move to the side of the bed."
            "[the_person.possessive_title] smiles and gets down on her knees below you."
            ###Draw the girl on knees###
            $ the_person.draw_person(position = "blowjob")
            the_person.char "I'm sorry [the_person.mc_title]... I just can't help it. It feels so good inside of me..."
            "[the_person.possessive_title] reaches down and starts to stroke your mostly soft cock."
            "Her hands feel good but you can tell its going to take a little more to get you aroused again, after cumming twice already."
            ###IF girl has big tits, ask for a tit fuck
            if the_person.has_large_tits():
                mc.name "Why don't you put it between your tits for a while?"
                "[the_person.possessive_title] smiles up at you."
                the_person.char "Anything for you, [the_person.mc_title]"
                "[the_person.possessive_title] looks up at you while she scoots closer to you, until her body is up against yours. She uses her hand to point your cock straight up while she moves it in position between her amazingly soft tits."
                "Once in position, she uses her hands to push her tits together, squashing your prick in her heavenly soft tit-flesh."
                "[the_person.possessive_title] starts to move up and down. Now and then when her tits are at the base of your dick she licks the sensitive tip."
                "The view of [the_person.possessive_title] on her knees before you, happy with you between her tits is extremely arousing. It isn't long until you are fully erect."

            else:
                mc.name "Why don't you put it in your mouth for a while?"
                "[the_person.possessive_title] smiles up at you."
                the_person.char "Anything for you, [the_person.mc_title]."
                "[the_person.possessive_title] looks up at you while she scoots closer to you, then lowers her head down and begins to lick and up down your groin."
                "She moves her head to the tip and slowly moves her head up and down your shaft a few times. She pulls off for a second then looks up at you."
                the_person.char "Mmm, I can taste the remnants of earlier... I can't wait to feel you inside me again..."
                "[the_person.possessive_title] resumes blowing you with vigor."
                "The view of [the_person.possessive_title] on her knees before you, happy with your cock in her mouth is extremely arousing. It isn't long until you are fully erect."


            mc.name "Okay [the_person.title], how do you want it?"
            $ the_person.draw_person(position = "doggy")
            "[the_person.possessive_title] backs up a bit, then turns around on her hands and knees and points her ass at you."
            ###Draw girl doggystyle###
            the_person.char "Come and get it, [the_person.mc_title]... its yours for the taking!"
            "You get down on your knees and get behind [the_person.possessive_title]. You line yourself up with her soaking wet slit and push yourself in."
            ###Sex Doggy Style###
            $ stealth_orgasm = False
            $ stealth_orgasm = False 
            call fuck_person(the_person, start_position = doggy, start_object = make_floor(), skip_intro = True) from _call_fuck_person_SBV13

            "Exhausted from your night with [the_person.possessive_title], you get back up into your bed. [the_person.possessive_title] joins you and you quickly fall asleep, cuddling together."

            "That night, you have many pleasant dreams involving [the_person.possessive_title] and sex in all kinds of crazy positions."
            $ SB_random_fetish_key = get_random_from_list(FETISH_VAGINAL_OPINION_LIST)
            "A couple times in the night, you stir slightly when you hear [the_person.possessive_title] making moaning noises in their sleep, and talking about [SB_random_fetish_key]!"
            $ the_person.sexy_opinions["vaginal sex"] = [FETISH_OPINION_VALUE, True]
            $ the_person.sexy_opinions[SB_random_fetish_key] = [FETISH_OPINION_VALUE, True]

            "She's been under the influence of your serums for a while now... you wonder if she's developed a fetish..."
            $ the_person.special_role.append(vaginal_fetish_role)
            $ add_breed_me_collar_to_base_outfit(the_person)
        "Refuse":       # allow for player to decide if he wants to induce fetish
            mc.name "I'm sorry [the_person.title], I really need to get some sleep."
            $ the_person.change_obedience(-10)
            $ the_person.change_happiness(-10)
            the_person.char "Oh! I'm sorry... Maybe tomorrow then?"
            "[the_person.possessive_title] quickly sulks off."
            return # EXIT
        "Too Tired" if mc.energy < 30:     # not enough energy for the player to induce fetish
            "[the_person.possessive_title] is surprised by your answer."
            $ the_person.change_obedience(-5)
            $ the_person.change_happiness(-5)
            the_person.char "Oh! I'm sorry... I didn't think about that. Maybe tomorrow then?"
            "[the_person.possessive_title] quickly sulks off."
            return  # EXIT

    $ FETISH_VAGINAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()

    call advance_time_enhanced_next_day_no_events() from _SB_overnight_SBV010

    call SB_cowgirl_wakeup_label(the_person) from _SB_cowgirl_wakeup_label_SBV010
    return

#SBV2
label SB_fetish_vaginal_event_label(the_person):
    if the_person == mom:
        "You hear a knock on your door. You hear [the_person.possessive_title]'s sweet and familiar voice from the other side."
        the_person.char "Hey honey, its [the_person.possessive_title]..."
        "You invite [the_person.possessive_title] in. You immediately start to get aroused when you see what she is wearing."
        $ the_person.apply_outfit(SB_vaginal_outfit)
        $ the_person.draw_person()
        the_person.char "Thanks for letting me come spend the night with you. I know you're a grown man with..."
        "Her voice trails off a bit."
        the_person.char "I mean, I know you've been busy with work, and I'm very proud, but sometimes I worry you're not having your needs met."
        "She places a hand on your arm and slides it up to your chest, caressing you with her soft fingers."
        the_person.char "Your physical needs, I mean..."
        menu:
            "Let's fuck!":
                mc.name "Thanks [the_person.title]! Yeah, it has been a pretty long day... It would be great to blow off some steam..."
                "[the_person.possessive_title] gives you a lusty look. She smiles and bounces slightly on your bed."
                $ the_person.change_slut_temp(2)
                the_person.char "Excellent! Now don't think of me as your mom, just think of me as your private, slutty milf. I'll do whatever your cock wants me to do, okay?"
                "You nod and she slides closer to you on the bed."
                $ the_person.add_situational_obedience("crisis_stuff", 25, "I'm doing it for my family.")
                call fuck_person(the_person) from _call_fuck_person_SBV20
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 0:
                    "[the_person.possessive_title] needs a few minutes to lie down when you're finished. Bit by bit her breathing slows down."
                    $ the_person.change_love(5)
                    the_person.char "Oh [the_person.mc_title], that was magical. I've never felt so close to you before..."
                    "After a while, [the_person.possessive_title] gives you a kiss on your forehead and stands up to leave."
                    $ the_person.draw_person(position = "back_peek")
                    the_person.char "Sweet dreams."
                else:
                    "When you're finished [the_person.possessive_title] gives you a kiss on your forehead and stands up to leave."
                    $ the_person.change_love(3)
                    $ the_person.draw_person(position = "back_peek")
                    the_person.char "Sweet dreams."
                $ the_person.clear_situational_obedience("crisis_stuff")
                mc.name "Wait! Hey [the_person.title] why don't you, ya know, sleep in here tonight?"
                the_person.char "Oh? I mean... I suppose that would be okay"
            "Just cuddle.":
                mc.name "Actually, [the_person.title], I'm really worn out. Would you wanna just cuddle for a bit and get some sleep?"
                "[the_person.possessive_title] is surprised by your answer, but happy that you want to be close to her."
                $ the_person.change_happiness(2)
                the_person.char "Oh! Well okay. I mean hey, tomorrow is a new day, and you know I like to be close to you..."
        "[the_person.possessive_title] lays down on your bed. You cuddle up behind her and slowly drift off to sleep."
    elif the_person == lily:
        "There is a quick a knock on your door. You hear [the_person.possessive_title] from the other side of the door."
        the_person.char "Hey [the_person.mc_title], you still up? I hope you're ready for me!"
        "You invite [the_person.possessive_title] in. You immediately start to get aroused when you see what she is wearing."
        $ the_person.apply_outfit(SB_vaginal_lily_outfit)
        $ the_person.draw_person()
        the_person.char "So... do you want a free show tonight? I've been thinking about this all day!"
        menu:
            "Strip Tease":
                mc.name "That sounds good [the_person.title]... why don't you give me a show before we go to bed?"
                "[the_person.possessive_title] smiles at you."
                the_person.char "Aww, does my [the_person.mc_title] wanna see his [the_person.title] get naked for him? What a pervert!" # NOTE: Names wont make sense, but everything else will.
                "[the_person.possessive_title] winks at you before beginning her routine."
                call SB_free_strip_scene(the_person) from _SB_free_strip_scene_2
                mc.name "Damn [the_person.title], you are really getting good at that."
                "[the_person.possessive_title] bites her lip, glancing down at your bulge. Her cheeks are flushed and rosey."
                the_person.char "Hey... if you want to I could... you know... take care of that tent you are sporting there [the_person.mc_title]."
                "You stand up and embrace her, your dick straining against your clothes, eager to begin another incestuous tryst with [the_person.possessive_title]."
                call fuck_person(the_person) from _call_fuck_person_SBV21
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 1:
                    "[the_person.possessive_title] needs a few minutes to lie down when you're finished. Bit by bit her breathing slows down."
                    $ the_person.change_happiness(5)
                    the_person.char "Oh god [the_person.mc_title], your dick is sooooo good..."
                else:
                    the_person.char "Wow, you are done already [the_person.mc_title]? That's... disappointing..."
                    "[the_person.possessive_title] seems disappointed she didn't finish."
                    $ the_person.change_love(-2)
                    $ the_person.change_happiness(-5)
                $ the_person.reset_arousal()
            "Just cuddle.":
                mc.name "Actually, [the_person.title], I'm really worn out. Would you wanna just cuddle for a bit and get some sleep?"
                "[the_person.possessive_title] is surprised by your answer."
                the_person.char "Oh! Well okay. I mean hey, tomorrow is a new day..."
        "[the_person.possessive_title] lays down on your bed. You cuddle up behind her and slowly drift off to sleep."
    else:
        "Your phones rings. Its [the_person.possessive_title]! You quickly pick it up"
        the_person.char "Hey [the_person.mc_title]! I'm here out front!"
        "You head to your front door and see [the_person.possessive_title] standing there... outside... in a very provocative outfit."
        $ the_person.apply_outfit(SB_vaginal_outfit)
        $ the_person.draw_person()
        ###Draw the girl###
        "You quickly open the door and invite her inside."
        "To avoid any situations with [mom.possessive_title] or [lily.possessive_title], you quickly invite her to your room."
        "Once you close your door, [the_person.possessive_title] quickly turns and embraces you."
        "You wrap your arms around her and start to makeout."
        $ the_person.draw_person(position = "kissing")
        "Your hands start exploring her body immediately while you start to kiss. [the_person.possessive_title] breaks off for a second and looks into your eyes."
        the_person.char "Thanks for inviting me over! I've been looking forward to this all day. Did you have anything in particular in mind for tonight?"
        menu:
            "Let's fuck!":
                "You chuckle at her feigned naivety."
                mc.name "You know exactly what I have in mind..."
                "[the_person.possessive_title] gives you a lusty look."
                the_person.char "Yeah... I know. Let's get started! I'm ready to go!"
                call fuck_person(the_person) from _call_fuck_person_SBV22
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 0:
                    the_person.char "Mmmm. I swear you make me cum every time..."
                    $ the_person.change_love(2)
                    $ the_person.change_happiness(5)

                else:
                    the_person.char "Okay... I guess we're done already?"
                    "[the_person.possessive_title] seems disappointed she didn't finish."
                    $ the_person.change_love(-2)
                    $ the_person.change_happiness(-5)
                $ the_person.reset_arousal()
            "Just cuddle.":
                mc.name "Actually, [the_person.title], I'm really sorry about this, but I'm really worn out. Would you wanna just cuddle for a bit and get some sleep?"
                "[the_person.possessive_title] is surprised by your answer, and clearly a little disappointed."
                $ the_person.change_happiness(-2)
                the_person.char "Oh! Well okay. I mean hey, tomorrow is a new day, and you know I like to be close to you..."
        "[the_person.possessive_title] lays down on your bed. You cuddle up behind her and slowly drift off to sleep."


    $ FETISH_VAGINAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()

    call advance_time_enhanced_next_day_no_events() from _SB_overnight_SBV020

    call SB_cowgirl_wakeup_label(the_person) from _SB_cowgirl_wakeup_label_SBV020
    return

#SBV3
label SB_fetish_mom_vaginal_label():
    $ the_person = mom
    "You are just starting to drift off to sleep, when you hear a knock at your door."
    the_person.char "Hey Honey... its [the_person.title]... can I come in?"
    "It is unusual for her to come around this time of night."
    mc.name "Sure thing [the_person.title]."
    $ the_person.apply_outfit(SB_vaginal_outfit)
    $ the_person.draw_person()
    "[the_person.possessive_title] slowly opens your door and walks in. Her outfit makes her body look incredible."
    mc.name "Everything ok [the_person.title]?"
    "[the_person.possessive_title] walks over beside your bed and sits down."
    $ the_person.draw_person(position = "sitting")
    the_person.char "Well... as you know we've been spending a lot of time together lately. We've also been doing all sorts of... other things..."
    "[the_person.possessive_title] stumbles over her words for a second before resuming."
    the_person.char "Now, I'm not gonna say all things we've been doing are okay but... I mean if we're going to do them anyway... Can I sleep in here tonight honey? With you?"
    "You are surprised by the question. It has been a while since you started exposing [the_person.possessive_title] to the serums you've been crafting."
    "While she is still a bit conflicted, it appears she is finally coming to terms with her new found sex drive."
    mc.name "That sounds great [the_person.title]. Come lay down!"
    "You scoot yourself to one side of your bed and let [the_person.possessive_title] lay down next to you."
    $ the_person.draw_person(position = "missionary")
    "[the_person.possessive_title] lays down and you quickly cuddle up with her, enjoying each other's warmth and intimacy."
    the_person.char "Oh [the_person.mc_title]... It has been so nice being close to you lately..."
    "[the_person.possessive_title] begins to rub her hand along your chest. Her touch feels amazing. You reach a hand over and begin to grope one of her breasts in return."
    $ the_person.change_arousal(10)
    the_person.char "[the_person.mc_title]... why can't I stop thinking about you? I know its wrong but I just..."
    "She stops rubbing your chest and her hand slowly drops down to your crotch. She begins to rub your rapidly rising erection through your clothes."
    the_person.char "I just can't stop thinking about your cock... When you put it in me I feel so good."
    "Feeling the moment is right, you move your lips to hers and begin to make out. Your tongues dance around each other in unison."
    $ the_person.change_arousal(10)
    "[the_person.mc_title] begins to pull off your clothes. It isn't long until you are naked, your flesh now against hers."
    the_person.char "[the_person.mc_title]! Please, I need you inside me again. Will you please... make love to me?"
    "You moan into her mouth and quickly prepare yourself to penetrate [the_person.possessive_title]."
    $ the_person.sex_skills["Vaginal"] = 6
    ###Sex scene, missionary###   ###TODO: consider writing a variant of this because the default intro is going to be confusing###
    call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True) from _call_sex_description_SBV30
    #$ the_person.SB_fetish = "vaginal sex"
    $ SB_random_fetish_key = get_random_from_list(FETISH_VAGINAL_OPINION_LIST)
    $ the_person.sexy_opinions["vaginal sex"] = [FETISH_OPINION_VALUE, True]
    $ the_person.sexy_opinions[SB_random_fetish_key] = [FETISH_OPINION_VALUE, True]
    "That night, after fucking [the_person.possessive_title], you share your bed together. As you fall asleep, you consider the implications of what happened. "
    "It is clear that [the_person.possessive_title] is now firmly under the influence of your serums and has developed a fetish for vaginal sex."
    "Her naked flesh soft up against yours gives you many sexy dreams that night."

    $ the_person.special_role.append(vaginal_fetish_role)
    $ add_breed_me_collar_to_base_outfit(the_person)
    $ FETISH_VAGINAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()

    call advance_time_enhanced_next_day_no_events() from _SB_overnight_SBV030

    call SB_cowgirl_wakeup_label(the_person) from _SB_cowgirl_wakeup_label_SBV030

    return

#SBV4
label SB_fetish_lily_vaginal_label():
    $ the_person = lily
    "You are just starting to drift off to sleep, when you hear a knock at your door."
    the_person.char "Hey [the_person.mc_title]... Are you still up? Can I come in for a bit?"
    "[the_person.possessive_title] almost never comes to your room, unless she needs something."
    mc.name "Sure thing [the_person.title]."
    $ the_person.apply_outfit(SB_vaginal_lily_outfit)
    $ the_person.draw_person()
    "[the_person.possessive_title] slowly opens your door and walks in."
    mc.name "Hey [the_person.title], looking great! Are you going out tonight?"
    "[the_person.possessive_title] stutters for a second."
    the_person.char "Well [the_person.mc_title], its been nice having some extra spending money, ya know? With the extra tasks you've been giving me..."
    "[the_person.possessive_title] stumbles over her words for a second before resuming."
    the_person.char "but... I have to admit, I've been having a lot of fun doing some of these different, ya know, tasks for you."
    "You aren't sure where she is going with this conversation."
    mc.name "Do you need more money, [the_person.title]?"
    "She looks at you in surprise."
    the_person.char "No! No its not that. Anyway, I was just wondering if maybe tonight, I could strip for you again, but this time like, not for money but, just for fun?"
    "Wow! You definitely weren't expecting this. Not yet anyway. Your serums must be really effecting her, if she's here to strip for you!"
    mc.name "That sounds great [the_person.title]!"
    "While she is still a bit conflicted, it appears she is finally coming to terms with her new found sex drive."
    "You sit down at the edge of your bed and watch as she begins the show."

    call SB_free_strip_scene(the_person) from _SB_free_strip_scene_1

    "Now completely naked, [the_person.possessive_title] walks over to you and sits on your lap."
    $ the_person.draw_person(position = "sitting")

    the_person.char "[the_person.mc_title]... I love the way you look at me. It makes me feel so good."
    "[the_person.possessive_title] begins to grind herself on your lap. Her breath catches in her throat and she looks at you."
    $ the_person.change_arousal(10)
    the_person.char "[the_person.mc_title]... why do you make me feel so good? I can't stop thinking about you..."
    "She stops grinding up against you and her hands drop down to your crotch. She begins to rub your rapidly rising erection through your clothes."
    the_person.char "...and I just can't stop thinking about your cock! When you put it in me I feel so good."
    "Feeling the moment is right, you move your lips to hers and begin to make out. Your tongues dance around each other in unison."
    $ the_person.change_arousal(10)
    "[the_person.possessive_title] begins to pull off your clothes. It isn't long until you are naked, your flesh now against hers."
    the_person.char "[the_person.mc_title]! Please, I need you inside me again. Fuck me [the_person.mc_title]!!!"
    "You moan into her mouth and quickly prepare yourself to penetrate [the_person.possessive_title]."
    $ the_person.sex_skills["Vaginal"] = 6
    ###Sex scene, missionary###   ###TODO: consider writing a variant of this because the default intro is going to be confusing###
    $ stealth_orgasm = False
    call fuck_person(the_person, start_position = doggy, start_object = make_bed(), skip_intro = True) from _call_sex_description_SBV40
    #$ the_person.SB_fetish = "vaginal sex"
    $ SB_random_fetish_key = get_random_from_list(FETISH_VAGINAL_OPINION_LIST)
    $ the_person.sexy_opinions[SB_random_fetish_key] = [FETISH_OPINION_VALUE, True]
    $ the_person.sexy_opinions["vaginal sex"] = [FETISH_OPINION_VALUE, True]
    the_person.char "Oh... that was so good. [the_person.mc_title]... can I spend the night with you? I don't wanna sleep alone tonight..."
    "That night, after fucking [the_person.possessive_title], you share your bed together. As you fall asleep, you consider the implications of what happened. "
    "It is clear that [the_person.possessive_title] is now firmly under the influence of your serums and has developed a fetish for vaginal sex."
    "Her naked flesh soft up against makes your dreams very pleasant."
    #SBMOD Start hacked wakeup sex code. To be copy/pasted to other similar places#

    $ the_person.special_role.append(vaginal_fetish_role)
    $ add_breed_me_collar_to_base_outfit(the_person)
    $ FETISH_VAGINAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()

    call advance_time_enhanced_next_day_no_events() from _SB_overnight_SBV040
    call SB_cowgirl_wakeup_label(the_person) from _SB_cowgirl_wakeup_label_SBV040
    return



init 1 python:
    def SB_cowgirl_wakeup_requirement():
        if time_of_day == 0:
            return True
        return False

#SBV5
#I'm leaving this code for now, but it should be unused#
label SB_cowgirl_wakeup_label(the_person):
    "All night long, you have sexy dreams centered around [the_person.possessive_title]."
    "She's on her knees, sucking you off expertly. Later, shes on her back while you pin her to the bed. Sometime later, shes on her hands and knees, taking your cock like a pro."

    "When morning comes, you feel a stirring in your loins again as you start to slowly wake up. This time, however, there are some very pleasant sensations coming from your crotch."

    $ the_person.apply_outfit(SB_vaginal_nude_outfit)
    $ the_person.draw_person(position = "cowgirl")
    $ the_person.change_arousal(35)
    $ mc.arousal = 25

    "You slowly open your eyes and discover that [the_person.possessive_title] is on top of you, riding you in the cowgirl position."
    "You reach up and grab her amazing ass cheeks. [the_person.possessive_title] looks in your eyes when she feels your hands on her."
    the_person.char "Good morning [the_person.mc_title]... Sorry but when I woke up I noticed you were hard so... I figured you wouldn't mind if I hopped on for a bit..."
    "[the_person.possessive_title] moans during one slow stroke."
    "You decide to lay back and enjoy the ride"
    call fuck_person(the_person, start_position = cowgirl, skip_intro = True) from _call_sex_description_SBV50
    mc.name "Oh god what a wakeup. I think I'm gonna go back to sleep for a bit. Thanks!"
    if the_person == mom:
        "[the_person.possessive_title] looks at you and smiles."
        the_person.char "Oh, anything for you honey. Well, I'd better go get ready for the day!"
    elif the_person == starbuck:
        "[the_person.possessive_title] giggles for a second then says goodbye."
        the_person.char "Yeah well, just don't tell my other customers about this, I can't make house calls for everyone!"
    else:
        "[the_person.title] looks at you and winks."
        the_person.char "Anytime [the_person.mc_title]! I'd better go get ready!"
    $ the_person.review_outfit(dialogue = False)
    "You fall back asleep. When you wake up, [the_person.possessive_title] has left."
    "Looks like you slept in!"
    $ FETISH_VAGINAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()
    return

init 2 python:
    def SB_fetish_vaginal_recurring_requirement():
        if mc_asleep() and day % 7 is not 4: # not on Friday nights
            if mc.business.get_employee_count() > 0:
                for person in mc.business.get_employee_list():
                    if SB_check_fetish(person, vaginal_fetish_role):
                        return True
            if SB_check_fetish(mom, vaginal_fetish_role):
                return True
        return False

    SB_fetish_vaginal_recurring_crisis = Action("Vaginal Fetish Recurring Crisis",SB_fetish_vaginal_recurring_requirement,"SB_fetish_vaginal_recurring_label")
    crisis_list.append([SB_fetish_vaginal_recurring_crisis, 5])

    def SB_fetish_vaginal_lily_recurring_requirement():
        if mc_asleep() and day % 7 is not 4: # not on Friday nights
            if SB_check_fetish(lily, vaginal_fetish_role):
                return True
        return False

    def get_vaginal_fetish_employee():
        meets_fetish_list = []
        for person in mc.business.get_employee_list():
            if SB_check_fetish(person, vaginal_fetish_role):
                meets_fetish_list.append(person)
        if SB_check_fetish(mom, vaginal_fetish_role):
            meets_fetish_list.append(mom)

        return get_random_from_list(meets_fetish_list)

    SB_fetish_vaginal_lily_recurring_crisis = Action("Vaginal Fetish lily Recurring Crisis",SB_fetish_vaginal_lily_recurring_requirement,"SB_fetish_vaginal_lily_recurring_label")
    crisis_list.append([SB_fetish_vaginal_lily_recurring_crisis, 5])

#SBV6
label SB_fetish_vaginal_recurring_label():
    $ the_person = get_vaginal_fetish_employee()
    if the_person == mom:
        "Before going to bed, you hear a knock on your door. You hear [the_person.possessive_title]'s sweet and familiar voice from the other side."
        the_person.char "Hey honey, its [the_person.title]... I was just wondering if I could come in for a bit?"
        "You invite [the_person.possessive_title] in. You immediately start to get aroused when you see what she is wearing."
        $ the_person.apply_outfit(SB_vaginal_outfit)
        $ the_person.draw_person()
        the_person.char "So... I was wondering... is it okay if I sleep in here with you again tonight?"
        menu:
            "Not tonight":
                mc.name "Sorry [the_person.title]... I had a long day and I'm pretty wore out... maybe tomorrow?"
                "She is clearly disappointed."
                the_person.char "Okay... see you in the morning I guess?"
                "You head for bed, looking forward to a restful night's sleep."
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(-5)
                return
            "Sounds good":
                "You quickly embrace her. Your hands start exploring her body immediately while you start to kiss. [the_person.possessive_title] breaks off for a second and looks into your eyes."
                $ the_person.draw_person(position = "kissing")
                the_person.char "Thanks for letting me come in... I honestly... I just couldn't stop thinking about you tonight."
    else:
        "Before going to bed, you hear a text message on your phone. You pick if up and take a look. It's from [the_person.possessive_title]."
        the_person.char "Hey, can't sleep. Mind if I cum over and spend the night? ;)"
        "You text her back."
        menu:
            "Too tired, sorry :(":
                "She takes a few minutes to respond."
                the_person.char "Okay... see you tomorrow I guess?"
                "You head for bed, looking forward to a restful night's sleep."
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(-5)
                return
            "Cum on over :)":
                "She responds right away."
                the_person.char "Be right there!"
                "You hang out for a few minutes, until you hear the doorbell. You go to your front door and open it."
                $ the_person.apply_outfit(SB_vaginal_outfit)
                $ the_person.draw_person()
                ###Draw the girl###
                "[the_person.possessive_title] is standing there, and she looks amazing."
                "You quickly invite her inside and head up to your room."
                "When you get into your room and close the door, [the_person.possessive_title] immediately throws her arms around you. You wrap your arms around her and start to makeout."
                $ the_person.draw_person(position = "kissing")
                "Your hands start exploring her body immediately while you start to kiss. [the_person.possessive_title] breaks off for a second and looks into your eyes."
                the_person.char "Thanks for letting me come over... I honestly... I just couldn't stop thinking about you tonight."

    if the_person.get_opinion_score("doggy style sex") > 2:
        "[the_person.possessive_title] lets go of you, and starts to slowly back up."
        the_person.char "I don't know what has come over me lately... I can't stop thinking about you fucking me from behind..."
        $ the_person.draw_person(position = "doggy")
        $ the_person.change_arousal(20)
        "[the_person.possessive_title] turns away from you and gets down on her hands and knees. She sticks her ass up in the air and starts to wiggle it back and forth."
        the_person.char "Come fuck me, [the_person.mc_title]. Don't worry, I'm ready for you!"
        "You quickly take your position behind her and slowly sink your cock into her greedy cunt."
        $ stealth_orgasm = False
        call fuck_person(the_person, start_position = doggy, start_object = make_floor(), skip_intro = True) from _call_fuck_person_SBV60
    elif the_person.get_opinion_score("sex standing up") > 2:
        "[the_person.possessive_title] resumes kissing you. You grab her ass with both hands and pick her up. She grinds her crotch into you."
        $ the_person.change_arousal(20)
        the_person.char "I need you so bad, just do me right here, up against the wall!"
        "You quickly pin [the_person.possessive_title] to the wall. She wraps her legs around you and sighs as you sink your cock into her greedy cunt."
        call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True) from _call_fuck_person_SBV61
    elif the_person.get_opinion_score("missionary style sex") > 2:
        "You kiss [the_person.possessive_title] along her neck and ear. She shivers at the sensation and then whispers in your ear."
        $ the_person.change_arousal(20)
        the_person.char "Throw me down on your bed, [the_person.mc_title]. I want to feel your weight on top of me while you fuck my brains out!"
        "You roughly pick up [the_person.possessive_title] and carry her over to the bed. You throw her down and quickly jump on top of her."
        "[the_person.possessive_title] spread her legs wide, giving you easy access. She sighs as you sink your cock into her greedy cunt."
        call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True) from _call_fuck_person_SBV62
    else:
        "[the_person.possessive_title] reaches down and starts to stroke your crotch through your clothes."
        $ the_person.change_arousal(20)
        the_person.char "Mmm... I can't wait to get your cock inside me... how do you want me, [the_person.mc_title]?"
        call fuck_person(the_person) from _call_fuck_person_SB63

    "After you finish your rutting, you and [the_person.possessive_title] get under the covers of your bed."
    "Spooning behind [the_person.possessive_title], you drift off to a wonderful night's sleep. Her body heat and the feeling of her naked skin against yours give you very pleasant dreams."
    $ SB_SET_RANDOM_EVENT_CHANCE(0)
    #SBMOD Start hacked wakeup sex code. To be copy/pasted to other similar places#

    $ FETISH_VAGINAL_EVENT_INUSE = False
    call advance_time_enhanced_next_day_no_events() from _SB_overnight_SBV060
    call SB_cowgirl_wakeup_label(the_person) from _SB_cowgirl_wakeup_label_SBV060
    return

#SBV7
label SB_fetish_vaginal_lily_recurring_label():
    $ the_person = lily

    "Before going to bed, you hear a knock on your door. You hear [the_person.possessive_title] from the other side of the door."
    the_person.char "Hey [the_person.mc_title], you still up? I was just wondering if I could come in for a bit?"
    "You invite Lily in. You immediately start to get aroused when you see what she is wearing."
    $ the_person.apply_outfit(SB_vaginal_lily_outfit)
    $ the_person.draw_person()
    the_person.char "So... I was wondering... is it okay if I sleep in here with you again tonight?"
    menu:
        "Not tonight":
            mc.name "Sorry [the_person.title]... I had a long day and I'm pretty wore out... maybe tomorrow?"
            "She is clearly disappointed."
            the_person.char "Whatever [the_person.mc_title]... see you in the morning I guess?"
            "You head for bed, looking forward to a restful night's sleep."
            $ the_person.change_obedience(-2)
            $ the_person.change_happiness(-5)
            return
        "Strip first":
            mc.name "That sounds good [the_person.title]... why don't you give me a show before we go to bed?"
            "[the_person.possessive_title] smiles at you."
            the_person.char "Aww, does my [the_person.mc_title] wanna see his [the_person.title] get naked for him? What a pervert!"
            "[the_person.possessive_title] winks at you before beginning her routine."
            call SB_free_strip_scene(the_person) from _SB_free_strip_scene_70
            mc.name "Damn [the_person.title], you are really getting good at that."
            "[the_person.possessive_title] bites her lip, glancing down at your bulge. Her cheeks are flushed and rosey."
            the_person.char "Hey... if you want to I could... you know... take care of that tent you are sporting there [the_person.mc_title]."
            "You stand up and embrace her, your dick straining against your clothes, eager to begin another incestuous tryst with [the_person.possessive_title]."

    if  the_person.get_opinion_score("doggy style sex") > 2:
        "[the_person.possessive_title] lets go of you, and starts to slowly back up."
        the_person.char "I don't know what has come over me lately... I can't stop thinking about you fucking me from behind..."
        $ the_person.draw_person(position = "doggy")
        $ the_person.change_arousal(20)
        "[the_person.possessive_title] turns away from you and gets down on her hands and knees. She sticks her ass up in the air and starts to wiggle it back and forth."
        the_person.char "Come fuck me, [the_person.mc_title]. Don't worry, I'm ready for you!"
        "You quickly take your position behind her and slowly sink your cock into her greedy cunt."
        $ stealth_orgasm = False
        call fuck_person(the_person, start_position = doggy, start_object = make_floor(), skip_intro = True) from _call_fuck_person_SBV70
    elif  the_person.get_opinion_score("sex standing up") > 2:
        "[the_person.possessive_title] resumes kissing you. You grab her ass with both hands and pick her up. She grinds her crotch into you."
        $ the_person.change_arousal(20)
        the_person.char "I need you so bad, just do me right here, up against the wall!"
        "You quickly pin your helpless [the_person.title] to the wall. She wraps her legs around you and sighs as you sink your cock into her greedy cunt."
        call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True) from _call_fuck_person_SBV71
    elif  the_person.get_opinion_score("missionary style sex") > 2:
        "You kiss [the_person.possessive_title] along her neck and ear. She shivers at the sensation and then whispers in your ear."
        $ the_person.change_arousal(20)
        the_person.char "Throw me down on your bed, [the_person.mc_title]. I want to feel your weight on top of me while you fuck my brains out!"
        "You roughly pick up [the_person.possessive_title] and carry her over to the bed. You throw her down and quickly jump on top of her."
        "[the_person.possessive_title] spread her legs wide, giving you easy access. She sighs as you sink your cock into her greedy cunt."
        call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True) from _call_fuck_person_SBV72
    else:
        "[the_person.possessive_title] reaches down and starts to stroke your crotch through your clothes."
        $ the_person.change_arousal(20)
        the_person.char "Mmm... I can't wait to get your cock inside me... how do you want me, [the_person.mc_title]?"
        call fuck_person(the_person) from _call_fuck_person_SB73

    "After you finish your rutting, you and [the_person.possessive_title] get under the covers of your bed."
    "Spooning behind [the_person.possessive_title], you drift off to a wonderful night's sleep. Her body heat and the feeling of her naked skin against yours give you very pleasant dreams."
    #SBMOD Start hacked wakeup sex code. To be copy/pasted to other similar places#

    $ FETISH_VAGINAL_EVENT_INUSE = False
    $ SB_CALCULATE_RANDOM_EVENT_RATE()

    call advance_time_enhanced_next_day_no_events() from _SB_overnight_SBV070
    call SB_cowgirl_wakeup_label(the_person) from _SB_cowgirl_wakeup_label_SBV070
    return
