init 1 python:
    #Role related requirement functions

    # def SB_mom_anal_pay_requirement():
    #     if day%7 == 5: #It is on saturday morning
    #         return True
    #     return False


    # def SB_stephanie_anal_fetish_requirement():
    #     if mc.business.is_open_for_business():
    #         if renpy.random.randint(0,100) < 15:
    #             return True
    #     return False

    def fetish_anal_staylate_requirement(person):
        if mc.is_at_work() and mc.business.is_open_for_business() and person.is_employee():
            if is_fetish_after_hours_available():
                return True
            else:
                return False
        return False

    def fetish_anal_staylate_event_requirement():
        if time_of_day == 3 and mc.business.is_open_for_business():
            return True
        return False

    def add_fuck_doll_collar_to_base_outfit(person):
        person.base_outfit.remove_all_collars()

        fd_collar = fuck_doll_collar.get_copy()
        fd_collar.colour = [.41,.16,.38,.9]
        fd_collar.pattern = "Pattern_1"
        fd_collar.colour_pattern = [.95,.95,.95,.9]
        person.base_outfit.add_accessory(fd_collar)
        return


    # def add_mom_anal_fetish_event():
    #     SB_mom_anal_fetish = Action("Mom Anal Sex", SB_mom_anal_pay_requirement, "SB_mom_anal_pay_label")
    #     mc.business.add_mandatory_morning_crisis(SB_mom_anal_fetish)
    #     return


    def add_fetish_anal_staylate_event(person):
        fetish_anal_staylate_event = Action("Employee stays late", fetish_anal_staylate_event_requirement, "fetish_anal_staylate_event_label", args = person)
        mc.business.add_mandatory_crisis(fetish_anal_staylate_event)
        return

    # def add_mom_weekly_anal_action():
    #     SB_mom_weekly_anal_action = Action("mom saturday anal ", SB_mom_anal_pay_requirement, "SB_mom_weekly_anal_label")
    #     mc.business.add_mandatory_morning_crisis(SB_mom_weekly_anal_action)

    #This is a list of positions that show off a person's ass. Can grab one randomly for when a girl wants to show off ass specifically
    def SB_get_random_ass_position():
        return get_random_from_list(["back_peek", "standing_doggy", "doggy", "walking_away"])

init 2 python:
    fetish_anal_staylate = Action("See me after work", fetish_anal_staylate_requirement, "fetish_anal_staylate_label",
        menu_tooltip = "Ask her to stay after work is over.")

    anal_fetish_role = Role(role_name ="Anal Fetish", actions =[fetish_anal_staylate])



label fetish_anal_staylate_label(the_person):
    mc.name "[the_person.title], I need you to stay after work today."
    the_person.char "Oh, of course sir. I'm not in trouble am I?"
    "You give [the_person.possessive_title] a reassuring smile."
    mc.name "No, of course not, you are a wonderful asset to the company..."
    "You lower your voice and whisper in her ear so others don't overhear."
    mc.name "...but I might have to spank your ass a bit anyway."
    "You look [the_person.possessive_title] in the eyes. Her pupils dilate a bit as she realizes the reasoning behind asking her to stay late."
    the_person.char "Oh! Thank you sir! I'll look forward to it!"
    "You say goodbye to [the_person.possessive_title]."
    $ fetish_after_hours_lock()
    $ add_fetish_anal_staylate_event(the_person)
    return

#SBA2
label fetish_anal_staylate_event_label(the_person):
    $ fetish_after_hours_unlock()
    if not mc.is_at_work():
        "Your phone rings. It's [the_person.possessive_title]. You answer it."
        the_person.char "Hey, are you at work? I can't find you."
        "You forgot! You asked [the_person.possessive_title] to stay after work today."
        mc.name "Sorry, I had something come up and had to leave early."
        "[the_person.possessive_title] tries to mask disappointment in her voice but it is still obvious."
        the_person.char "Oh... okay... well try to let me know next time before I stay late. I thought... anyway, maybe some other time. Bye!"
        $ the_person.change_love(-2)
        $ the_person.change_happiness(-5)
        return

    $ ceo_office.show_background()
    "You finish up with your work for the day and return to your office. You are organizing some papers when [the_person.possessive_title] enters the room."
    $ the_person.apply_outfit(special_fetish_outfit)
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
            "[the_person.possessive_title]'s accommodating ass ripples in shock waves out from where you hand spanks it."
            "You give her hind quarters a few more spanks, giving her few seconds in between."
            $ the_person.change_arousal(20)
            "[the_person.possessive_title] barely stifles a moan as you spank her again. Her cheeks are beginning to glow a rosy red. Her pussy lips are growing puffy with clear signs of arousal."
            "You decide it is time to move on."
        "Fuck Her Ass":
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
            call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True) from _call_fuck_person_SBA20
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title] lays over the desk for a while, recovering from her ass reaming."
                the_person.char "God... that felt so fucking good..."
                $ the_person.change_obedience(5)
                $ the_person.change_happiness(5)

            else:
                the_person.char "Okay... I guess we're done already?"
                "[the_person.possessive_title] seems disappointed she didn't finish."
                $ the_person.change_love(-2)
                $ the_person.change_happiness(-5)

            $ the_person.event_triggers_dict["LastAnalFetish"] = day
            "[the_person.possessive_title] gets up and starts getting ready to go home."
            "You say goodbye to her as she walks out your office door."
            return

    menu:
        "Fuck Her Ass":
            "You firmly grasp one of her ass cheeks in one hand. It is hot to the touch."
            "With two fingers, you start to pull the jewelled plug from her. When only the tip remains, you push it back in."
            "You fuck her for a few moments with the jewelled plug. She loves the penetration and begins to push her hips back against you as you work the plug in and out of her."
            $ the_person.change_arousal(10)
            mc.name "Now, I think it is time for something a bit more substantial than the plug..."
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.get_opinion_score("anal sex") * 5)
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title] tries to push back against you and begins to beg."
            the_person.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]"
            call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True) from _call_fuck_person_SBA21
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title] lays over the desk for a while, recovering from her ass reaming and spanking."
                the_person.char "God... that felt so fucking good..."
                $ the_person.change_stats(happiness = 5, obedience = 5)
            else:
                the_person.char "Okay... I guess we're done already?"
                "[the_person.possessive_title] seems disappointed she didn't finish."
                $ the_person.change_stats(happiness = -5, love = -2)
            $ the_person.event_triggers_dict["LastAnalFetish"] = day

            "[the_person.possessive_title] gets up and starts getting ready to go home."
            "You say goodbye to her as she walks out your office door. She walks a bit funny, clearly uncomfortable after the spanking she received."
        "Send her home":
            mc.name "That's enough for today [the_person.title]."
            "[the_person.possessive_title] looks back at your, clearly surprised that you are sending her away already."
            the_person.char "What? I mean, already? Okay..."
            "She grabs her stuff and quickly makes an exit from your office."
            $ the_person.change_love(-2)
            $ the_person.change_happiness(-5)
            $ the_person.change_obedience(10)
    return



#SBA3






# #SBA40
# label SB_mom_anal_pay_label():
#     python:
#         the_person = mom
#         mc.change_location(bedroom)
#         mc.location.show_background()
#
#     "You're just getting out of bed when [the_person.possessive_title] calls from downstairs."
#     the_person.char "[the_person.mc_title], could we talk for a moment?"
#     mc.name "Sure, down in a second."
#     $ mc.change_location(kitchen)
#     $ mc.location.show_background()
#     $ the_person.draw_person(position = "sitting")
#     "[the_person.possessive_title] is sitting at the kitchen table, a collection of bills laid out in front of her."
#     "She is fidgeting a bit. You can tell she is a little nervous about something."
#     the_person.char "[the_person.mc_title], I'm really sorry about this. Some things have broken around the house that need repaired but I don't have the money to have the work done..."
#     the_person.char "I know that you've been working so hard at your new business and I'm so proud of you, and I'm happy we've been so close lately."
#     the_person.char "I wouldn't feel right about just taking your hard earned money though, so I was hoping we could make a deal..."
#     mc.name "What sort of deal [the_person.title]?"
#     the_person.char "Well, I was thinking... we could make a deal where, instead of just stripping for you, we could do other things too."
#     "You think about her proposal. It has been a while now since you started giving her your serums to test."
#     mc.name "What kind of things do you have in mind, Mom?"
#     "[the_person.possessive_title] stumbles over her words for a second. You can tell this is difficult for her to say, but her urges are getting the better of her."
#     the_person.char "Well, after I get done stripping, I could please you, in whatever way you want..."
#     "[the_person.possessive_title] blushes and looks down at the ground as she finishes her sentence."
#     the_person.char "You could even stick it back there, in my ass the way you like it..."
#     "[the_person.possessive_title] has been exposed to your serums enough, you know that she probably wants it anal too. You decide to push the issue a bit."
#     mc.name "You mean the way you like it?"
#     "[the_person.possessive_title]'s cheeks turn even redder and she looks up at you."
#     the_person.char "I'm sorry honey I just... I can't explain it, but lately I just find myself constantly fantasizing..."
#     "She stops herself before she says too much."
#     the_person.char "The bills are just really starting to pile up. I'm sorry, I know its wrong but, I promise I'll make it good for you!"
#     menu:
#         "Strip and ride me\nPay $1000" if mc.business.funds >= 1000:
#             $ mc.business.change_funds(-1000)
#             "[the_person.possessive_title] smiles wide when you give her the money."
#             the_person.char "Thank you [the_person.mc_title]! Now, are you ready a show?"
#             call free_strip_scene(the_person) from _call_free_strip_scene_SBA40
#             "Now that she is naked, [the_person.possessive_title] quickly grabs your hand and leads you to her bedroom. When you get to her bed, she shoves you down on your back."
#             $ mc.change_location(mom_bedroom)
#             $ mc.location.show_background()
#             the_person.char "Oh god, I need this so bad honey. You just lay back and let momma take care of you now."
#             "[the_person.possessive_title] quickly strips you down. She reaches into her nightstand and grabs some lube. She hands it to you."
#             the_person.char "Here! Can you get me, you know... ready?"
#             $ the_person.draw_person(position = "back_peek")
#             "[the_person.possessive_title] turns away from you. You squirt a liberal amount of lube onto your hand and then reach up between her supple ass cheeks and spread it around her tight asshole."
#             "You start to work one finger into her. She moans and starts to push back against you. When you push a second finger into her she gasps."
#             $ the_person.change_arousal(15)
#             the_person.char "Oh [the_person.mc_title], I've been thinking about this all week... I'm sorry I brought money into this... I won't ask you for money again!"
#             #Cowgirl pose#
#             $ the_person.draw_person(position = "cowgirl")
#             the_person.char "Now, just let [the_person.title] take care of you. I'm gonna stick it into my most intimate hole now..."
#             "[the_person.possessive_title] goes slow, but steadily slides down, impaling her sphincter on your throbbing erection. She bottoms out and moans loudly."
#             $ the_person.break_taboo("anal_sex")
#             # call fuck_person(the_person, start_position = SB_anal_cowgirl, start_object = make_bed(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_SBA41
#             call get_fucked(the_person, the_goal = "anal creampie", private= True, start_position = SB_anal_cowgirl, start_object = make_bed(), skip_intro = True, allow_continue = False) from _call_sex_description_SBA41
#             $ the_report = _return
#             if the_report.get("girl orgasms", 0) > 0:
#                 the_person.char "Oh god, I came so hard..."
#                 "[the_person.possessive_title] collapses onto the bed next to you, exhausted from her anal cowgirl ride."
#             else:
#                 the_person.char "Mmm, that was so good, thank you [the_person.mc_title]..."
#                 "[the_person.possessive_title] rolls off you and lays down on the bed next to you."
#             "You start to get up to go to your room, but [the_person.possessive_title] calls out to you as you start to get up."
#             the_person.char "[the_person.mc_title]? Why don't you just stay in here tonight? [the_person.title] loves you... its okay!"
#             "You slip back into bed next to her."
#             $ the_person.add_role(anal_fetish_role)
#             $ add_fuck_doll_collar_to_base_outfit(the_person)
#             "[the_person.possessive_title] has already fallen asleep. You can hear her murmuring in her dreams about taking stuff in her ass."
#             "It seems your serums have given her an anal fetish!"
#
#             # SINCE THIS IS NOW A MORNING EVENT SKIP SLEEP PART
#             # "You cuddle up behind her and enjoy the heat of her soft flesh as you slowly drift off to sleep."
#
#             # call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_SBA42
#             # $ the_person.apply_outfit(special_fetish_nude_outfit)
#             # "The next morning, you slowly wake up. The bed next to you is cold. You look around and see [the_person.possessive_title] getting ready for the day in the bathroom."
#             # $ mc.change_location(mom_bedroom)
#             # #Position peek back
#             # $ the_person.draw_person(position = "walking_away")
#             # "You walk up behind [the_person.possessive_title] and wrap your arms around her. She arches her back against you as your hands roam across her chest."
#             # the_person.char "Good morning sleepy head..."
#             # "[the_person.possessive_title] starts to tremble at your touch."
#             # the_person.char "Look, about last night... I'm sorry I asked for money in exchange for... the wonderful thing we did afterword. I promise I won't do that again!"
#             # the_person.char "I know that we have this tradition that... every Saturday morning I work on the budget and things have been really tight lately."
#             # the_person.char "I was thinking we should start a new tradition! Every Saturday morning... Why don't we just plan on doing what we did. It will be something to look forward to with the stress of each week."
#             # "[the_person.title] begins to grind her hips up against you, nestling your now quickly hardening dick between her ass cheeks."
#             # the_person.char "Plus... god I just can't stop fantasizing about you... sticking it in me... back there."
#             # "You grab her hips and start to grind against her. Her breathing starts to get a bit heavier."
#             # the_person.char "[the_person.mc_title], last night [the_person.title] took care of you. Do you think this morning, you could take care of me?"
#             # "You smile to yourself."
#             # mc.name "Are you asking me to fuck you in your ass?"
#             # the_person.char "Yes... Please! Please [the_person.mc_title]! I don't know why I keep feeling this way, but I need you in my ass!"
#             # "You pick her up from behind and take her back to the bed. You throw her on the bed. She quickly gets on her hands and knees and starts wiggling her ass at you."
#             # #Draw doggystyle
#             # $ the_person.draw_person(position = "doggy")
#             # "You grab the lube leftover from the night before. You quickly apply another glob to [the_person.title]'s back side. You apply some more to your cock until it is good and slick."
#             # "You get yourself lined up with your mom's back passage. You slowly begin your anal penetration."
#             # the_person.char "That's it [the_person.mc_title]! Fuck me good!"
#             # call fuck_person(the_person, start_position = doggy_anal, start_object = make_bed(), skip_intro = True) from _call_sex_description_SBA43
#             # $ the_report = _return
#             # if the_report.get("girl orgasms", 0) > 0:
#             #     "[the_person.possessive_title] lays there on the bed, speechless from your anal plundering."
#             # else:
#             #     "[the_person.possessive_title] lays there on the bed."
#             # mc.name "So... every Saturday morning? I think I could get used to that..."
#             # "You can see [the_person.possessive_title]'s body quiver slightly at your words."
#             # mc.name "BUT, I am a man. I may have needs more often then that. Be ready for me with that amazing ass of yours anytime."
#             # "[the_person.possessive_title] meekly responds."
#             # the_person.char "Yes [the_person.mc_title]. You know it will be... take my ass, whenever you want. I'll be ready!"
#             $ add_mom_weekly_anal_action()
#         "Strip and ride me\nPay $1000 (disabled)" if mc.business.funds <1000:
#             pass
#         "Not this week":
#             mc.name "Sorry [the_person.title], but I'm tight on cash right now as well. Maybe next week, okay?"
#             "[the_person.possessive_title] nods and turns back to her bills."
#             the_person.char "I understand [the_person.mc_title]. Now don't let me keep you, I'm sure you were up to something important."
#             $ add_mom_anal_fetish_event() # trigger this event again next week
#
#     $ the_person.apply_planned_outfit()
#     $ mc.location.show_background()
#     $ clear_scene()
#     return


# #SBA50
# label SB_mom_weekly_anal_label():
#     $ the_person = mom
#     $ bedroom.show_background()
#     "You're just getting out of bed when [the_person.possessive_title] calls out to you."
#     the_person.char "[the_person.mc_title], could we talk for a moment? Can you come to my room?"
#     mc.name "Sure, I'll be there in a second."
#     $ mom_bedroom.show_background()
#     $ the_person.apply_outfit(lingerie_wardrobe.pick_random_outfit())
#     $ the_person.draw_person(position = "stand4")
#     "[the_person.title] is standing next to her bed. You quickly shut her door and lock it."
#     the_person.char "[the_person.mc_title]! Hey, it time for our weekly arrangement! Are you ready for your show and, well you know what comes afterword..."
#     "[the_person.title] smiles wide, waiting for your response."
#     menu:
#         "Strip and ride me":
#             "You sit down on the bed. [the_person.title] walks over to you."
#             the_person.char "Remember, no touching! At least during this part. Now, are you ready a show?"
#             call free_strip_scene(the_person) from _call_free_strip_scene_SBA50
#             "Now that she is naked, [the_person.possessive_title] pushes you over, back on to the bed."
#             "[the_person.possessive_title] quickly strips you down. She reaches into her nightstand and grabs some lube. She hands it to you."
#             the_person.char "Here! Can you get me, you know... ready?"
#             #facing away pose#
#             $ the_person.draw_person(position = "back_peek")
#             "[the_person.title] turns away from you. You squirt a liberal amount of lube onto your hand and then reach up between her supple ass cheeks and spread it around her tight asshole."
#             "You start to work one finger into her. She moans and starts to push back against you. When you push a second finger into her she gasps."
#             $ the_person.change_arousal(15)
#             the_person.char "Oh god, I need this so bad honey. You just lay back and let momma take care of you now."
#             #Cowgirl pose#
#             $ the_person.draw_person(position = "cowgirl")
#             the_person.char "Now, just let [the_person.title] take care of you. I'm gonna stick it into my most intimate hole now..."
#             "[the_person.title] goes slow, but steadily slides down, impaling her sphincter on your throbbing erection. She bottoms out and moans loudly."
#             # call fuck_person(the_person, start_position = SB_anal_cowgirl, start_object = make_bed(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_SBA51
#             call get_fucked(the_person, the_goal = "anal creampie", private= True, start_position = SB_anal_cowgirl, start_object = make_bed(), skip_intro = True, allow_continue = False) from _call_sex_description_SBA51
#             $ the_report = _return
#             if the_report.get("girl orgasms", 0) > 0:
#                 the_person.char "Oh god, I came so hard..."
#                 "[the_person.title] collapses onto the bed next to you, exhausted from her anal cowgirl ride."
#             else:
#                 the_person.char "Mmm, that was so good, thank you [the_person.mc_title]..."
#                 "[the_person.possessive_title] rolls off you and lays down on the bed next to you."
#
#             # SINCE THIS IS NOW A MORNING EVENT, SKIP THE SLEEP PART
#             # "You cuddle up behind her and enjoy the heat of her soft flesh as you slowly drift off to sleep."
#
#             # call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_SBA52
#             # $ the_person.apply_outfit(special_fetish_nude_outfit)
#             # "The next morning, you slowly wake up. The bed next to you is cold. You look around and see [the_person.possessive_title] getting ready for the day in the bathroom."
#             # $ mc.change_location(mom_bedroom)
#             # $ mc.location.show_background()
#             # #Position peek back
#             # $ the_person.draw_person(position = "walking_away")
#             # "You walk up behind [the_person.possessive_title] and wrap your arms around her. She arches her back against you as your hands roam across her chest."
#             # the_person.char "Good morning sleepy head..."
#             # "[the_person.possessive_title] starts to tremble at your touch."
#             # the_person.char "I love being so close to you... and so intimate..."
#             # "[the_person.title] begins to grind her hips up against you, nestling your now quickly hardening dick between her ass cheeks."
#             # the_person.char "I just want you to fuck my ass, all weekend long! Is there really anything wrong with that?"
#             # "You grab her hips and start to grind against her. Her breathing starts to get a bit heavier."
#             # the_person.char "Honey, last night [the_person.title] took care of you. Do you think this morning, you could take care of me?"
#             # "You smile to yourself."
#             # mc.name "Of course [the_person.title]. I'll fuck you in the ass, just the way you like it."
#             # the_person.char "Yes... Please! Please [the_person.mc_title]! Fuck me in the ass!"
#             # "You pick her up from behind and take her back to the bed. You throw her on the bed. She quickly gets on her hands and knees and starts wiggling her ass at you."
#             # #Draw doggy style
#             # $ the_person.draw_person(position = "doggy")
#             # "You grab the lube leftover from the night before. You quickly apply another glob to [the_person.mc_title]'s back side. You apply some more to your cock until it is good and slick."
#             # "You get yourself lined up with [the_person.possessive_title]'s back passage. You slowly begin your anal penetration."
#             # the_person.char "That's it [the_person.mc_title]! Fuck me good!"
#             # call fuck_person(the_person, start_position = doggy_anal, start_object = make_bed(), skip_intro = True) from _call_sex_description_SBA53
#             # $ the_report = _return
#             # if the_report.get("girl orgasms", 0) > 0:
#             #     "[the_person.possessive_title] lays there on the bed, speechless from your anal plundering."
#             # else:
#             #     "[the_person.possessive_title] lays there on the bed"
#             # $ the_person.draw_person(position = "missionary")
#             # mc.name "Mmm, thanks [the_person.title]. That ass is amazing. Next Saturday, right?"
#             # the_person.char "Yes [the_person.mc_title]. But don't feel like you HAVE to wait to take my ass. We can do it whenever you want. I'll be ready!"
#
#         "Not this week":
#             mc.name "Sorry [the_person.title], work was hell and I'm exhausted. Maybe next week, okay?"
#             "[the_person.possessive_title] frowns."
#             the_person.char "I understand [the_person.mc_title]. Now don't let me keep you, I'm sure you were up to something important."
#
#     $ add_mom_weekly_anal_action()  # re-add event for next week
#     $ the_person.apply_planned_outfit()
#     $ mc.location.show_background()
#     $ clear_scene()
#     return


# #SBA90 #Figure out how to do Stephanie's fetishes later
# label SB_stephanie_anal_fetish_label():
#     $ the_person = stephanie
#     $ the_person.event_triggers_dict["LastAnalFetish"] = day
#     if mc.location == mc.business.r_div: #Already in research
#         "Suddenly, [the_person.possessive_title] looks up from her work and and speaks up."
#         the_person.char "Hey [the_person.mc_title], I need to talk to you about something. Can we go somewhere private?"
#     else:
#         "You get a text message from [the_person.possessive_title]."
#         the_person.char "Hey [the_person.mc_title], I need to talk to you about something. Can we meet somewhere private?"
#         "You text her back."
#     mc.name "Sure, meet me in my office."
#     $ mc.change_location(office)
#     $ ceo_office.show_background()
#     $ scene_manager = Scene()
#     $ scene_manager.add_actor(the_person)
#     "[the_person.title] meets you there. You sit down and notice she closes the office door... and then locks it."
#     mc.name "Have a seat. Is there something I can do for you?"
#     "She sits down and immediately starts to talk to you."
#     $ scene_manager.update_actor(the_person, position = "sitting")
#     if the_person.love < 40 and the_person.obedience < 140:
#         the_person.char "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
#         the_person.char "I went along with things for a while because... well I don't know why. I guess I was just really into the science of things."
#         "She shifts uncomfortably in her seat."
#         $ scene_manager.update_actor(the_person, display_transform = character_right)
#         the_person.char "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
#         the_person.char "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
#         the_person.char "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
#         the_person.char "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
#         "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
#         the_person.char "For god's sake, all I can think about is you bending over the fucking desk and sticking it in my ass! That isn't normal!"
#         the_person.char "I'm sorry, but I can't do it anymore. You and I both know there isn't any real way to counter these effects. So, if I'm going to be a butt slut... I might as well enjoy it, right?"
#         mc.name "I suppose so."
#         $ scene_manager.update_actor(the_person, position = "stand4")
#         "[the_person.possessive_title] pulls a serum out of her pocket."
#         the_person.char "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things... might as well enjoy my new life as a butt slut, right?"
#         "This is some dangerous territory. If you let her go through with this, you are sure her sister will be pissed! Do you try to talk her down? Or let her do it?"
#         menu:
#             "Try to talk her down" if mc.charisma > 6:
#                 mc.name "Stop. You don't have to do that?"
#                 "She looks at the serum in her hand. Then back at you."
#                 the_person.char "Ummm, I don't know... I'm pretty sure I do."
#                 mc.name "Don't you want to know more... about the long term effects? Of the serums I mean?"
#                 the_person.char "You hardly need me to test something like that."
#                 mc.name "Who better to do it though? [the_person.title], you've been with me since the beginning. I'll help meet your needs. I know the cravings will be intense, but I promise I'll help!"
#                 "Her resolve is failing. She looks down at the serum again."
#                 mc.name "The science behind these chemicals is incredible. You KNOW you want to keep studying it together. With me!"
#                 the_person.char "[the_person.mc_title]... I want to. I really do. But I'm so scared right now."
#                 "You get up and walk around the desk."
#                 mc.name "It's okay. Sometimes science is a risky business. We can do this. Together. Let me have the serum."
#                 "She hesitates another moment. Then hands you the serum."
#                 the_person.char "Oh god... you better be right about this!"
#                 $ scene_manager.update_actor(the_person, position = "kissing")
#                 "She throws her arms around you, holding you close."
#                 the_person.char "The serums really are incredible. I do want to study them more. But first... I need your dick in my ass! I can't think about anything else right now!"
#                 $ scene_manager.update_actor(the_person, position = "standing_doggy")
#                 "[the_person.possessive_title] turns around and bends over. Your hands immediately get to work."
#                 $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
#                 "She wiggles her ass back and forth in front of you as you pull your dick out of your pants."
#                 the_person.char "Come on [the_person.mc_title], you know what I need!"
#                 "Without any hesitation you slide your cock into her tight hole."
#                 $ the_person.break_taboo("anal_sex")
#                 call fuck_person(the_person, start_position = SB_anal_standing, skip_intro = True, position_locked = True) from _call_fuck_person_SBA090
#                 $ the_person.max_opinion_score("anal sex")
#                 $ the_person.max_opinion_score("anal creampies")
#                 $ the_person.add_role(anal_fetish_role)
#                 $ add_fuck_doll_collar_to_base_outfit(the_person)
#                 $ the_person.update_sex_skill("Anal", 6)
#                 the_person.char "Oh god... It's even better than I dreamed about last night."
#                 "[the_person.possessive_title] takes a minute to recover before standing up."
#                 $ scene_manager.update_actor(the_person, position = "stand2")
#                 the_person.char "Okay... I'm in. I hope you realize the serums also greatly increase libido."
#                 mc.name "Don't worry. I have something that can help with that."
#                 "You reach inside the bottom drawer of your desk. You pull out a pink glass anal plug and hand it to her. Her eyes are transfixed on the plug."
#                 mc.name "If the crazy urges get too strong, and I'm not available to satisfy you, use this."
#                 the_person.char "Oh! Okay! I think I'll try it out now..."
#                 "You see her reach behind herself and easily slide it in, her body still lubed up from your prior fucking."
#                 the_person.char "Ah! Mmm I feel full. That's really nice. Not as good as you, but I guess in a pinch I could use it as a substitute."
#                 $ scene_manager.update_actor(the_person, position = "walking_away")
#                 "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, her plug just peaking out between her rosy ass cheeks."
#                 "Looks like [the_person.title] has an anal fetish now!"
#             "Let her take it":
#                 mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way."
#                 "She looks at you. Her resolve stumbles, but only for a moment."
#                 the_person.char "Don't worry, I'll be a REAL ideal employee for you soon."
#                 "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
#                 $ enhanced_permanent_bimbo_on_apply(the_person, add_to_log = True)
#                 "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
#                 "She looks around a bit, seeming a bit confused about where she is."
#                 the_person.char "That's... we were talking about something... right?"
#                 "She looks at you. Her pupils are dilated and her breathing is calm."
#                 mc.name "We were just about done... with the talking anyway."
#                 the_person.char "That's right! We were going to do something else after though... right? I remember hoping that."
#                 "She begins to walk around the desk toward you."
#                 mc.name "That's right. You were going to bend over my desk for a minute. And if everything goes well, I have a present for you."
#                 the_person.char "Oh! A present! I do love presents! Especially the ones I tend to get when I'm bent over. I wonder what it could be!"
#                 $ scene_manager.update_actor(the_person, position = "standing_doggy")
#                 "[the_person.possessive_title] turns around and bends over. Your hands immediately get to work."
#                 $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
#                 "She wiggles her ass back and forth in front of you as you pull your dick out."
#                 the_person.char "Stick it in [the_person.mc_title]! I want to earn my special present!"
#                 "Without any hesitation you slide your cock into her tight hole."
#                 $ the_person.break_taboo("anal_sex")
#                 call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True, position_locked = True) from _call_fuck_person_SBA091
#                 $ the_person.max_opinion_score("anal sex")
#                 $ the_person.max_opinion_score("anal creampies")
#                 $ the_person.add_role(anal_fetish_role)
#                 $ add_fuck_doll_collar_to_base_outfit(the_person)
#                 $ the_person.update_sex_skill("Anal", 6)
#                 the_person.char "That's it! That's just what I was hoping for."
#                 $ scene_manager.update_actor(the_person, position = "stand2")
#                 the_person.char "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another round. Normally one times is enough but..."
#                 mc.name "Don't worry. I have something that can help with that."
#                 "You reach inside the bottom drawer of your desk. You pull out a pink glass anal plug and hand it to her. Her eyes are transfixed on the plug."
#                 mc.name "This is your present. If you can't find a nice dick to fuck your asshole and you are getting too horny, play with this for a while."
#                 the_person.char "Oh! I thought the present was... but this looks great! Would you do the honors mister?"
#                 $ scene_manager.update_actor(the_person, position = "standing_doggy")
#                 "She bends over and presents her recently used ass to you. You have no problem pushing it in, with her ass being lubed up from your prior fucking."
#                 the_person.char "Ahh! That's the spot! Could you umm... you know... move it in and out a few times? Make sure its reeeaaaallllyyyyy in there good."
#                 "You grab the base and pull it out. You can feel her clenching it as you try to pull on it. When you get it out a few inches, you let it go. Her ass clenches and pulls it back in until its deep again."
#                 the_person.char "Mmmm... that's it. Keep going!"
#                 mc.name "I'm sorry, but I have to get going."
#                 the_person.char "Nnnnoooooo."
#                 $ scene_manager.update_actor(the_person, position = "stand4")
#                 "She stands up and turns to you."
#                 the_person.char "Fine! I'll just go back to... whatever it was I was doing. What do I do here again?"
#                 mc.name "It doesn't matter, you can take the rest of the day off."
#                 the_person.char "Oh? That eager to get rid of me? Guess I'll just go find someone else to play with for a while. Your loss mister!"
#                 $ scene_manager.update_actor(the_person, position = "walking_away")
#                 "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, her plug just peaking out between her rosy ass cheeks."
#                 "Looks like [the_person.title] has an anal fetish now! But she is also a bimbo."
#                 "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"
#
#             "Try to talk her down\n{color=#ff0000}{size=18}Requires High Charisma{/size}{/color} (disabled)" if mc.charisma <= 6:
#                 pass
#
#     elif the_person.love < 70 and not the_person.has_role(girlfriend_role):   #She kinda trusts / loves you, but isn't fully committed and needs some convincing.
#         the_person.char "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
#         the_person.char "I went along with things for a while because I trust you. You've always impressed me with the way you do things."
#         "She shifts uncomfortably in her seat."
#         $ scene_manager.update_actor(the_person, display_transform = character_right)
#         the_person.char "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
#         the_person.char "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
#         the_person.char "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
#         the_person.char "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
#         "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
#         the_person.char "For god's sake, all I can think about is you bending over the fucking desk and sticking it in my ass! That isn't normal!"
#         the_person.char "I'm going to be honest here. I trust you, I'm sure you are just doing this for research or business purposes. But I'm at a tipping point here. I need you to answer this question honestly."
#         mc.name "Okay, go ahead."
#         the_person.char "Are you going to... you know... take responsibility for this? The urges are SO intense! You're the only guy here, I need your word that you'll help me take of these urges!"
#         "From a pocket, she pulls out a serum that it looks like she has concocted."
#         the_person.char "If you can't, I guess I understand. But I don't think I can take it, knowing the serums gave me these urges... I need something to forget, and just move on with my life."
#         the_person.char "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things... Maybe it's time for me to start a new life. I'm sure you could use me over in marketing or something, right?"
#         "This is some dangerous territory. It sounds like she is looking to you to tell her what to do."
#         "Become a bimbo, for real? Or, if you want her to stay the sexy, intelligent research lead, you'll have to help her with her newfound libido?"
#         "If you have her take the serum, her sister will probably get very upset!"
#         menu:
#             "Help her":
#                 pass
#             "Take the Serum":
#                 mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way. I don't think I have the time to commit to something like that."
#                 $ scene_manager.update_actor(the_person, emotion = "sad")
#                 "She looks at you. You think you see a tear coming down from her eye."
#                 the_person.char "It's okay. The science is amazing. And I'm sure I'll enjoy life as... a bimbo butt slut."
#                 "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
#                 $ enhanced_permanent_bimbo_on_apply(the_person, add_to_log = True)
#                 "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
#                 "She looks around a bit, seeming a bit confused about where she is."
#                 the_person.char "That's... we were talking about something... right?"
#                 "She looks at you. Her pupils are dilated and her breathing is calm."
#                 mc.name "We were just about done... with the talking anyway."
#                 the_person.char "That's right! We were going to do something else after though... right? I remember hoping that."
#                 $ scene_manager.update_actor(the_person, position = "stand2")
#                 "She gets up and begins to walk around the desk toward you."
#                 mc.name "That's right. You were going to bend over my desk for a minute. And if everything goes well, I have a present for you."
#                 the_person.char "Oh! A present! I do love presents! Especially the ones I tend to get when I'm bent over. I wonder what it could be!"
#                 $ scene_manager.update_actor(the_person, position = "standing_doggy")
#                 "[the_person.possessive_title] turns around and bends over. Your hands immediately get to work."
#                 $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
#                 "She wiggles her ass back and forth in front of you as you pull your dick out of your pants."
#                 the_person.char "Stick it in [the_person.mc_title]! I want to earn my special present!"
#                 "Without any hesitation you slide your cock into her tight hole."
#                 $ the_person.break_taboo("anal_sex")
#                 call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True, position_locked = True) from _call_fuck_person_SBA092
#                 $ the_person.max_opinion_score("anal sex")
#                 $ the_person.max_opinion_score("anal creampies")
#                 $ the_person.add_role(anal_fetish_role)
#                 $ add_fuck_doll_collar_to_base_outfit(the_person)
#                 $ the_person.update_sex_skill("Anal", 6)
#                 the_person.char "That's it! That's just what I was hoping for."
#                 $ scene_manager.update_actor(the_person, position = "stand2")
#                 the_person.char "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another round. Normally one times is enough but..."
#                 mc.name "Don't worry. I have something that can help with that."
#                 "You reach inside the bottom drawer of your desk. You pull out a pink glass anal plug and hand it to her. Her eyes are transfixed on the plug."
#                 mc.name "This is your present. If you can't find a nice dick to fuck your asshole and you are getting too horny, play with this for a while."
#                 the_person.char "Oh! I thought the present was... but this looks great! Would you do the honors mister?"
#                 $ scene_manager.update_actor(the_person, position = "standing_doggy")
#                 "She bends over and presents her recently used ass to you. You have no problem pushing it in, with her ass being lubed up from your prior fucking."
#                 the_person.char "Ahh! That's the spot! Could you umm... you know... move it in and out a few times? Make sure its reeeaaaallllyyyyy in there good."
#                 "You grab the base and pull it out. You can feel her clenching it as you try to pull on it. When you get it out a few inches, you let it go. Her ass clenches and pulls it back in until its deep again."
#                 the_person.char "Mmmm... that's it. Keep going!"
#                 mc.name "I'm sorry, but I have to get going."
#                 the_person.char "Nnnnoooooo."
#                 $ scene_manager.update_actor(the_person, position = "stand4")
#                 "She stands up and turns to you."
#                 the_person.char "Fine! I'll just go back to... whatever it was I was doing. What do I do here again?"
#                 mc.name "It doesn't matter, you can take the rest of the day off."
#                 the_person.char "Oh? That eager to get rid of me? Guess I'll just go find someone else to play with for a while. Your loss mister!"
#                 $ scene_manager.update_actor(the_person, position = "walking_away")
#                 "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, her plug just peaking out between her rosy ass cheeks."
#                 "Looks like [the_person.title] has an anal fetish now! But she is also a bimbo."
#                 "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"
#                 $ the_person.apply_planned_outfit()
#                 $ clear_scene()
#                 return
#         "She gives a deep sigh of relief."
#         the_person.char "You have NO idea how glad I am to hear that."
#         "[the_person.possessive_title] stands up."
#         $ scene_manager.update_actor(the_person, position = "stand4")
#         if the_person.outfit.tits_available() and the_person.outfit.vagina_available():
#             pass
#         else:
#             "She starts to strip down."
#             $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
#         "She looks at you expectantly."
#         the_person.char "Well? Why are you still wearing clothes? You said you would help!"
#         # call fuck_person(the_person, start_position = SB_anal_cowgirl, start_object = make_desk(), girl_in_charge = True, position_locked = True) from _call_sex_description_SBA093
#         call get_fucked(the_person, the_goal = "anal creampie", start_position = SB_anal_cowgirl, start_object = make_desk(), allow_continue = False) from _call_sex_description_SBA093
#         $ the_person.max_opinion_score("anal sex")
#         $ the_person.max_opinion_score("anal creampies")
#         $ the_person.add_role(anal_fetish_role)
#         $ add_fuck_doll_collar_to_base_outfit(the_person)
#         $ the_person.update_sex_skill("Anal", 6)
#         the_person.char "Oh god... It's even better than I dreamed about last night."
#         "[the_person.possessive_title] takes a minute to recover before standing up."
#         $ scene_manager.update_actor(the_person, position = "stand2")
#         the_person.char "Okay. I hope you realize the serums also greatly increase libido."
#         mc.name "Don't worry. I have something that can help with that."
#         "You reach inside the bottom drawer of your desk. You pull out a pink glass anal plug and hand it to her. Her eyes are transfixed on the plug."
#         mc.name "If the urges get crazy strong, and I'm not available to satisfy you, use this."
#         the_person.char "Oh! Okay! I think I'll try it out now..."
#         "You see her reach behind herself and easily slide it in, her body still lubed up from your prior fucking."
#         the_person.char "Ah! Mmm I feel full. That's really nice. Not as good as you, but I guess in a pinch I could use it as a substitute."
#         $ scene_manager.update_actor(the_person, position = "walking_away")
#         "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, her plug just peaking out between her rosy ass cheeks."
#         "Looks like [the_person.title] has an anal fetish now!"
#     else:
#         the_person.char "Before I get started, I just want to make sure you understand. I support you completely. I'm not mad or anything, just a little concerned."
#         the_person.char "I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
#         the_person.char "I went along with things for a while because I trust you. Maybe even love you. You've always impressed me with the way you do things."
#         the_person.char "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
#         the_person.char "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
#         the_person.char "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
#         the_person.char "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
#         "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
#         the_person.char "For god's sake, all I can think about is you bending over the fucking desk and sticking it in my ass! That isn't normal!"
#         the_person.char "I trust you. It took me a while to realize what is going on, but I understand it now."
#         the_person.char "This is the next step in our relationship. The urges are SO intense! You're the only guy here, I need you to help me take of these urges!"
#         the_person.char "I'm sure that relying on you for this can only bring us closer together."
#         if the_person.relationship != "Single":
#             $ SO_title = SO_relationship_to_title(the_person.relationship)
#             mc.name "Wait, don't you have a [SO_title]?"
#             the_person.char "So? He isn't here at work with me all day is he? He can fuck my ass when I get home, but I need you to do it while I'm here!"
#         "Sounds like she thinks the whole reason you gave her the serums is because... you want to take things to the next level? For now, it is probably better if you just go along with it."
#         mc.name "You're right. I probably should have been more honest about it, but I thought this would help bring us closer together."
#         "She gives a deep sigh of relief."
#         the_person.char "You have NO idea how glad I am to hear that."
#         "[the_person.possessive_title] stands up."
#         $ scene_manager.update_actor(the_person, position = "stand4")
#         if the_person.outfit.tits_available() and the_person.outfit.vagina_available():
#             pass
#         else:
#             "She starts to strip down."
#             $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
#         "She looks at you expectantly."
#         the_person.char "Well? Why are you still wearing clothes? You said you would help!"
#         # call fuck_person(the_person, start_position = SB_anal_cowgirl, start_object = make_desk(), skip_intro = False, girl_in_charge = True, position_locked = True) from _call_sex_description_SBA094
#         call get_fucked(the_person, the_goal = "anal creampie", start_position = SB_anal_cowgirl, start_object = make_desk(), skip_intro = False, allow_continue = False) from _call_sex_description_SBA094
#         $ the_person.max_opinion_score("anal sex")
#         $ the_person.max_opinion_score("anal creampies")
#         $ the_person.add_role(anal_fetish_role)
#         $ add_fuck_doll_collar_to_base_outfit(the_person)
#         $ the_person.update_sex_skill("Anal", 6)
#         the_person.char "Oh god... It's even better than I dreamed about last night."
#         "[the_person.possessive_title] takes a minute to recover before standing up."
#         $ scene_manager.update_actor(the_person, position = "stand2")
#         the_person.char "Okay. I hope you realize the serums also greatly increase libido."
#         mc.name "Don't worry. I have something that can help with that."
#         "You reach inside the bottom drawer of your desk. You pull out a pink glass anal plug and hand it to her. Her eyes are transfixed on the plug."
#         mc.name "If the urges get crazy strong, and I'm not available to satisfy you, use this."
#         the_person.char "Oh! Okay! I think I'll try it out now..."
#         "You see her reach behind herself and easily slide it in, her body still lubed up from your prior fucking."
#         the_person.char "Ah! Mmm I feel full. That's really nice. Not as good as you, but I guess in a pinch I could use it as a substitute."
#         $ scene_manager.update_actor(the_person, position = "walking_away")
#         "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, her plug just peaking out between her rosy ass cheeks."
#         "Looks like [the_person.title] has an anal fetish now!"
#
#     $ scene_manager.clear_scene()
#     $ the_person.apply_planned_outfit()
#     $ clear_scene()
#     return
