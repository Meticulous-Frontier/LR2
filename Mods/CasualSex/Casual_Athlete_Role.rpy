#NOTE This entire file is now commented out. I'm hopeful this will reduce the need to completely reinstall the mod directory from scratch, instead of just deleting the file completely.
# With 32.1, please delete this file from the repository.


#************* Casual Sex Role: College Athlete  *******************
#Outline
#-College Athlete
# Looking for casual sex while she focuses on her school and athletic program
# Tends to hang out at the Gym
#  First event: She invites you to work out with her. You work up a sweat together, then sneak into a changing room for sex
#  Second event: She invites you to compete with her in distance race (10k? something similar). Makes a wager if you win she'll let you "do what you want" with her
#  Event Requirements: Advances with sluttiness and player energy. Max energy takes the place of physical fitness during this storyline
#  Girl requirements: Age <25, skinny body type.
#  Other notes: She calls it off if she "catches feels" (love > 50). Will start warning player at > 40 love
#
# init -2 python:
#     def casual_athlete_get_to_know_requirement(person):
#         if mc.max_energy >= 110:
#             if mc.location == gym:
#                 return True
#             else:
#                 return "Wait until you see her at the gym"
#         else:
#             return "Requires: 110 maximum energy"
#
#     def casual_athlete_phase_one_requirement(person):
#         if person.event_triggers_dict.get("athlete_progress", 0) < 1:
#             return False
#         if person.love > 50:
#             return "She is uneasy about falling for you"
#         if person.event_triggers_dict.get("athlete_workout", 0) < 1:
#             return False
#         if time_of_day < 4:
#             if mc.max_energy >= 120:
#                 if person.effective_sluttiness() < 20:
#                     return "Requires 20 Sluttiness"
#                 elif mc.location == gym:
#                     return True
#                 else:
#                     return "Only at the gym"
#             else:
#                 return "Requires: 120 maximum energy"
#         return False
#
#     def casual_athlete_phase_two_requirement(person):
#         if person.event_triggers_dict.get("athlete_progress", 0) < 2:
#             return False
#             if person.event_triggers_dict.get("athlete_progress", 0) > 3:
#                 return False
#         if person.love > 50:
#             return "She is uneasy about falling for you"
#         if time_of_day < 4:
#             if mc.max_energy >= 140:
#                 if person.effective_sluttiness() < 40:
#                     return "Requires: 40 sluttiness"
#                 return True
#             else:
#                 return "Requires: 140 maximum energy"
#         return False
#
#     def casual_athlete_race_crisis_requirement():
#         if day % 7 == 5:
#             if time_of_day == 1:
#                 return True
#         return False
#
#     def casual_athlete_buy_protein_shake_requirement(person):
#         if person.event_triggers_dict.get("athlete_protein", 0) < 1:
#             return False
#         if mc.location == gym:
#             return True
#         else:
#             return "Only at the Gym"
#
#     def casual_athlete_house_call_requirement(person):
#         if person.event_triggers_dict.get("athlete_progress", 0) == 4:
#             if mc.location == person.home:
#                 return True
#         return False
#
#     def casual_athlete_ghost_requirement():
#         if renpy.random.randint(0,100) < 20:
#             return True
#         return False
#
#     def add_casual_athlete_ghost_action(person):
#         mc.business.remove_mandatory_crisis("casual_athlete_ghost_label")
#         casual_athlete_ghost = Action("Casual Athlete Ghosts you", casual_athlete_ghost_requirement, "casual_athlete_ghost_label", args = person)
#         mc.business.add_mandatory_crisis(casual_athlete_ghost)
#         return
#
#
# #*************Create Casual Athlete Role***********#
# init -1 python:
#     casual_athlete_get_to_know = Action("Get to know Her {image=gui/heart/Time_Advance.png}", casual_athlete_get_to_know_requirement, "casual_athlete_get_to_know_label",
#         menu_tooltip = "Make an observation about her.")
#     casual_athlete_phase_one = Action("Workout Together {image=gui/heart/Time_Advance.png}", casual_athlete_phase_one_requirement, "casual_athlete_phase_one_label",
#         menu_tooltip = "Work up a sweat.")
#     casual_athlete_phase_two = Action("Challenge to Race {image=gui/heart/Time_Advance.png}", casual_athlete_phase_two_requirement, "casual_athlete_phase_two_label",
#         menu_tooltip = "No risk, no reward.")
#     casual_athlete_protein_shake = Action("Buy Protein Shake ($5) {image=gui/heart/Time_Advance.png}", casual_athlete_buy_protein_shake_requirement,"casual_athlete_buy_protein_shake_label", menu_tooltip = "Slip some serum in.")
#     casual_athlete_house_call = Action("Take Charge {image=gui/heart/Time_Advance.png}", casual_athlete_house_call_requirement, "casual_athlete_house_call_label",
#         menu_tooltip = "Pick her up.")
#     casual_athlete_role = Role(role_name ="College Athlete", actions =[casual_athlete_get_to_know , casual_athlete_phase_one, casual_athlete_phase_two, casual_athlete_protein_shake, casual_athlete_house_call], hidden = True)
#
#
# #*************Mandatory Crisis******************#
# init 1 python:
#     def add_casual_athlete_race_crisis(person):
#         casual_athlete_race_crisis.args = [person]    # set the current person as action argument
#         mc.business.add_mandatory_crisis(casual_athlete_race_crisis) #Add race crisis    TODO Find out if this breaks if two girls hit this stage a the same point in gameplay
#         return
#
#     casual_athlete_race_crisis = Action("Charity Race", casual_athlete_race_crisis_requirement, "casual_athlete_race_crisis_label")
#
#
#
# ###Athlete ACTION LABELS###
# label casual_athlete_get_to_know_label(the_person):
#     if "athlete_progress" not in the_person.event_triggers_dict:
#         $ the_person.event_triggers_dict["athlete_progress"] = 0
#         #Introduction scene#
#     if the_person.event_triggers_dict.get("athlete_progress", 0) < 1:
#         "You look up and down [the_person.title]. You can tell she takes care of herself."
#         mc.name "You seem like you like to work out."
#         the_person "Yeah! You could say that. I'm actually on the state college track and field team!"
#         "You aren't surprised, she certainly has the look of an athlete."
#         "You talk with her for a while about sports. She has a healthy interest in just about all things physical."
#         the_person "Well, I need to get going. It was nice talking with you, [the_person.mc_title]!"
#         $ the_person.event_triggers_dict["athlete_progress"] = 1
#         #You're introduced but not had sex yet#
#     elif the_person.event_triggers_dict.get("athlete_progress", 0) == 1:
#         "You decide to ask [the_person.title] a bit more about her athletics."
#         mc.name "I see you here a lot. Are you getting ready for a race?"
#         the_person "Yeah! I'm getting ready for a big race soon, so I try to get in here before and after class each day."
#         "Wow, going to college, and dedicated to sports. Sounds like she doesn't have much free time."
#         mc.name "So, where does that leave you? Any time leftover for a social life? Or a boyfriend?"
#         the_person "Oh, with everything going on, there is no way I would have time for a boyfriend."
#         "[the_person.title] starts to move to the next workout machine."
#         the_person "So a relationship is not really an option for me right now, or a job for that matter."
#         mc.name "Yeah, sounds like an intense schedule."
#         if the_person.event_triggers_dict.get("athlete_protein", 0) < 1:
#             the_person "It'd be nice to have a little extra money for some protein powder or something. Money is pretty tight!"
#             "You think about it for a bit. You could offer to buy her a protein shake, they serve them here at the gym. That would be a good opportunity to slip some serum in..."
#             mc.name "They have protein shakes here. Maybe I could grab you one? It'd be no trouble."
#             #Charisma role to unlock the buy protein shake option#
#             $ ran_num = renpy.random.randint(0,100)
#             $ ran_num += (mc.charisma * 10)
#             if ran_num > 50:   #Base line 50:50 chance at charisma = 0. 100% chance at charisma = 5
#                 the_person "That... actually would be nice! You have to be careful with guys, but you seem genuine enough."
#                 "You now have the option to buy [the_person.title] a protein shake at the gym."
#                 $ the_person.event_triggers_dict["athlete_protein"] = 1
#             else:
#                 "[the_person.title] hesitates when you offer."
#                 the_person "I appreciate it, but I'll have to pass. It wouldn't feel right to take freebies like that..."
#         else:
#             the_person "I appreciate you buying me a protein shake now and then. I definitely feel the effects of them. I feel stronger... even sexier since you started doing that!"
#         "[the_person.title] moves on to the free weights area of the gym."
#         if mc.max_energy >= 110:
#             the_person "I think I'm going to do some squats..."
#             "[the_person.title] looks over at you. She gives you a quick appraisal."
#             the_person "Hey, you look like you're fairly fit yourself. You should workout with me sometime."
#             mc.name "That sounds like a good idea, actually."
#             the_person "Yeah... you're kinda cute. It'd be nice to have a guy around for a bit. It's been a while since I uhh..."
#             "You raise your eyebrow"
#             the_person "I mean uhh, with school and track, I'm so busy. It'd be nice to spend some time in the company of the opposite sex for a while! Nothing wrong with that, right?"
#             $ the_person.event_triggers_dict["athlete_workout"] = 1
#             "You should consider working out with [the_person.title] sometime. It sounds like she might appreciate some male company!"
#         else:
#             the_person "I think I'm going to do some squats..."
#             "[the_person.title] looks over at you. She gives you a quick appraisal."
#             the_person "Hey, have you ever thought about working out a bit more? It does wonders for your energy..."
#             "You consider her statement for a moment."
#             the_person "Anyway, I'm going to get back to my workout. I'll see you around [the_person.title]!"
#             "If you want to get further with her, maybe you should work on increasing your energy!"
#
#         #Had sex in the locker room#
#     elif the_person.event_triggers_dict.get("athlete_progress", 0) == 2:
#         "You notice that [the_person.title] is really pushing herself hard today on the treadmill."
#         mc.name "Hey [the_person.title]. You're really going at it! Have an event coming up?"
#         "[the_person.title] slows the treadmill down so she can carry on a conversation."
#         the_person "Yeah! I have a big 10k coming up. I really want to do well for this, with it coming up on track season!"
#         "You chit chat with [the_person.title] for a bit about the upcoming race."
#         if mc.max_energy >= 140:
#             the_person "Hey, you seem pretty fit too. You should consider entering! It's for a great cause!"
#             mc.name "Okay... I'll consider it. Things are pretty busy at work lately, but I'll get back to you if I have time."
#             the_person "Just don't be sore about it when I beat you to the finish line. I'm a serious athlete!"
#             mc.name "Ohhh, I see! Well, maybe we should make it a race! But what would the stakes be?"
#             "[the_person.title] chuckles before responding. She gives you a quick wink."
#             the_person "I'm sure we could come up with something... be careful though, don't bet anything you aren't willing to lose!"
#         else:
#             the_person "Hey, it has been nice chatting with you, but I need to get back to my workout!"
#         "You say goodbye and head on your way."
#
#         #You've challenged her to a race!#
#     elif the_person.event_triggers_dict.get("athlete_progress", 0) == 3:
#         "You try to strike up a conversation with [the_person.title]."
#         the_person "Hey now, no distractions! Your ass is mine on Saturday!"
#         mc.name "Ha! We'll see about that!"
#
#
#         #You've won the race#
#     elif the_person.event_triggers_dict.get("athlete_progress", 0) == 4:
#         mc.name "Hey [the_person.title]."
#         the_person "Hey. [the_person.mc_title]!"
#         "You catch up with her for a bit with what she's been up to."
#         the_person "Well, it was good to see you. We should work out again sometime, or... you haven't lost my address have you?"
#         mc.name "Of course not!"
#         the_person "Then swing by some evening, it would be good to get a little time working out some tension!"
#         "You tell her you'll look her up soon, say goodbye and head on your way."
#
#     else:
#         "Debug: How did you end up here???"
#
#     $ the_person.review_outfit()
#     call advance_time from _call_advance_casual_athlete_get_to_know
#     return
#
# #CSA10
# label casual_athlete_phase_one_label(the_person):
#     if the_person.event_triggers_dict.get("athlete_progress", 0) == 1:
#         mc.name "Hey [the_person.title]. I figured I would find you here. Want to workout together?"
#         "[the_person.title] is just hopping off the treadmill. You can tell she just finished getting warmed up."
#         the_person "[the_person.mc_title]! Hey, I was wondering if you would take me up on my offer to workout sometime. That sounds great! I'm going to be doing free weights today."
#         mc.name "Sounds good! I'll head to the locker room and get changed and meet you over by the free weights."
#         "You quickly get yourself changed into workout clothes and meet [the_person.title]."
#         the_person "This will be perfect! Today is strength day and with you around to spot me I can really push myself to the limit."
#         $ the_person.draw_person( position = "stand4")
#         "You begin a workout with [the_person.title]. You start it out with some basic free lifting, taking turns on the equipment. She strikes up a conversation as your work out."
#         the_person "Alright, time for some curls. Thanks again for doing this. It's been nice having a guy around... a lot of times when I do workouts over here I have a lot of guys hitting on me..."
#         "You nod in understanding."
#         mc.name "Well, I can't say I blame them, you train hard, and it shows with how good your body looks!"
#         "She chuckles."
#         the_person "Thanks. Honestly, it's not that I don't like the attention, but with everything going on with me right now, I just don't have time for a relationship."
#         the_person "You've been a good friend though. It's nice having a guy be just a friend."
#         "You finish up your curls with [the_person.title]. You move on to the pull up bar."
#         $ the_person.draw_person( position = "stand3")
#         "You start to do a few pull-ups."
#         mc.name "So, I get that you don't have time for a relationship but... how do you deal with your, you know, needs?"
#         the_person "Well, I used to have a few friends from class that came with, well, benefits I guess you could say."
#         "You grunt as you exert yourself as you finish your set."
#         the_person "The last few I've had have kind of fizzled though. The last one started getting too attached, wanting to move in with me, and the one before that graduated and moved out of state."
#         the_person "So, I guess you could say I'm going through a bit of a dry spell right now."
#         "You let go of the pull up bar and she steps up to it."
#         the_person "Hey, could you do me a favor? Could you pull me down a little bit while I do my reps, you know, to give a little resistance?"
#         mc.name "Sure, I can do that."
#         "[the_person.title] reaches up and grabs the pull up bar. You put your hands on her hips and lightly push down, giving her some extra weight for her pull-ups."
#         "As she begins to pull herself up, her hips, waist, and ass are in perfect position, right in front of your face. You check her out while she struggles through her reps."
#         "[the_person.title]'s tight, thin body is undeniably sexy and athletic. Your hands on her hips gives you a naughty idea."
#         mc.name "I stay busy with my business. I know that feeling, not having time for a relationship, but looking for some casual hookups."
#         "[the_person.title] drops down off of the pull up bar. You let your hands linger on her hips a little longer than necessary."
#         the_person "Exactly! Why can't two adults just have casual sex once in a while?"
#         mc.name "Friends with benefits can be great for meeting needs during busy times in your life. I'm looking for something like that right now too."
#         "[the_person.title] looks up at you when you finish your sentence. It quickly dawns on her that you are suggesting hooking up."
#         the_person "Let's keep going, next up are squats."
#         $ the_person.draw_person( position = "stand2")
#         "[the_person.title] helps you add some weights to the squat bar. You decide to get a little braver."
#         mc.name "Add one more weight to the end there, I want to really push myself today."
#         "She does as you ask, and you get in position under the bar."
#         mc.name "Stay close, I've never done this much weight before."
#         "As you get in position, you feel [the_person.title] get in position behind you to spot you. You can feel her a little closer than she needs to be though."
#         "With a grunt, you begin your reps. The weight is tough, but you get through your reps without help. When you finish you slowly stand up and turn to her."
#         $ the_person.draw_person( position = "stand4")
#         if the_person.outfit.tits_available():
#             "[the_person.title] has a little extra color in her cheeks than she did a minute ago. You also notice her nipples are a little more prominent."
#         else:
#             "[the_person.title] has a little extra color in her cheeks than she did a minute ago and it looks like her nipples are poking out a little bit, against the fabric containing them."
#         "She must be getting a little bit excited!"
#         mc.name "Alright, your turn."
#         "You help her reset the weights to something appropriate for her. She gets in position and gets ready to do some squats, and you get behind her, ready to spot for her."
#         "As she begins her reps, you get a little bit closer to her. As she stands up with each squat, her lower back starts to brush up against your crotch."
#         mc.name "See? Two friends, helping each other out. I take a turn, then you take a turn..."
#         "[the_person.title] grunts... or was that a groan? You lean forward just a bit farther. It is now obvious you are using the opportunity to put your body up against hers as she finishes her squats."
#         "At the top of her last squat, she lingers a bit before she racks the weight. You feel an ever so slight wiggle of her hips up against you. She's getting turned on!"
#         "She racks her weights with a groan, and you quickly retreat. Getting an erection here would be a bit embarrassing"
#         the_person "Okay... let finish with the bench press."
#         "You head over to the bench and start racking some weights on it. You lay down on the bench while [the_person.title] stands by your head."
#         "She looks around a bit to see if anybody is watching you before prompting you to begin."
#         the_person "Ready? It's my turn now..."
#         "As you lift the weight up over the bar and begin to bring it down to your chest, [the_person.title] slowly moves forward, maneuvering her legs until her crotch is right above your face."
#         "You breathe deep. There is the normal gym smells of weights, rubber, and sweat, but also a smell that is distinctly, sweetly feminine."
#         "You lift your head up for a second, making contact with her crotch with your face. She stifles a groan as you finish up your set."
#         $ the_person.change_max_energy(5)
#         $ the_person.change_arousal(20)
#         "[the_person.title] backs off and you quickly get up. She puts a hand on your shoulder and whispers in your ear."
#         the_person "There's a locker room here families can use with a lock on it. Meet me there in three minutes."
#         $ the_person.draw_person( position = "walking_away")
#         "You watch [the_person.title] walk off, fighting off an erection. Looks like you're about to hookup at the gym!"
#         "After three minutes, you follow after [the_person.title]. When you find the family use room, you let yourself in."
#         $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True)
#         $ the_person.draw_person( position = "stand2")
#         "As you enter, you see that [the_person.title] is already naked."
#         the_person "[the_person.mc_title], we can work out the details later... I haven't been fucked in months!"
#         "You walk over to her and quickly strip. You grab [the_person.title] by that ass and pick her up. You carry her to the wall and pin her up against it."
#         $ the_person.draw_person( position = "against_wall")
#         "[the_person.possessive_title] is grinding her hips up against yours. The sweat from your workouts mingles together as you prepare yourself to enter her."
#
#         $ the_person.add_situational_slut("horny", 20, "She is desperate to be fucked")
#
#         # NOTE skip intro prevents taboo break from executing
#
#         call condom_ask(the_person) from _casual_athlete_mod_condom_ask_CS010
#
#         "As you begin to push yourself inside her, she drags her nails across your back."
#         $ the_person.break_taboo("vaginal_sex")
#         if not mc.condom:
#              $ the_person.break_taboo("condomless_sex")
#         the_person "Oh fuck, that's good. Give it to me good, [the_person.mc_title]!"
#         call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_casual_sex_mod_CS010
#         $ the_report = _return
#         if the_report.get("girl orgasms", 0) > 0:
#             "As you slowly let [the_person.title] down from the wall, you can see her trembling, caused by aftershocks from her orgasm."
#
#         the_person "Mmm... that was nice..."
#         "[the_person.title] stutters for a moment."
#         $ the_person.clear_situational_slut("horny")
#         the_person "But... you know... I really can't get involved in a serious relationship right now."
#         mc.name "I agree. We need some ground rules. Want to have coffee and figure it out?"
#         the_person "That sounds good. But it's not a date, okay? Just need to set boundaries."
#         "You agree. You and [the_person.title] take a quick shower, then get ready and leave the gym."
#
#         $ the_person.apply_planned_outfit()
#
#         "You head to a nearby coffee shop. You grab yourself a coffee, letting [the_person.title] pay for her own. You grab a seat at a booth away from any other people."
#         $ renpy.show("restaurant", what = restaraunt_background, layer = "master")
#         $ the_person.draw_person( position = "sitting")
#
#         the_person "So... are you interested in a friends with benefits set up?"
#         "You give a quick nod."
#         the_person "Okay, so, some ground rules. First off, if either of us starts to catch feelings for the other person, we break it off. I sure as fuck don't have time for that stuff right now..."
#         mc.name "I agree. We'll keep it physical. No dates or whatever. Just hit me up when you want to fuck around."
#         the_person "Right... here, let's exchange numbers. I'll text you and if we're both free, we can screw around, no strings attached."
#         "You agree. You and [the_person.title] finish up with your coffees. You both get up to leave."
#         $ the_person.draw_person(position = "stand3")
#         the_person "Well, see you around, stud! I'd better go work on some homework."
#         "You say your goodbyes. This should be interesting. You wonder what kind of crazy sex you'll have with your new friends with benefits."
#
#         $ the_person.event_triggers_dict["booty_call"] = True
#
#         "You now have [the_person.title]'s phone number."
#         $ the_person.event_triggers_dict["athlete_progress"] = 2
#
#     elif the_person.event_triggers_dict.get("athlete_progress", 0) > 1:
#         mc.name "Hey [the_person.title]. I figured I would find you here. Want to workout together?"
#         the_person "That sounds great, [the_person.mc_title]! I always enjoy working up a sweat with you."
#         mc.name "Sounds good! I'll head to the locker room and get changed and meet you over by the free weights."
#         "You quickly get yourself changed into workout clothes and meet [the_person.title]."
#         $ the_person.draw_person( position = "stand4")
#         "It is obvious from the beginning of your workout with [the_person.possessive_title] that she intends to get frisky with you when you get done."
#         "While doing squats, she gets right behind you, pressing her body against yours as she spots you."
#         "You try to be as covert as possible, but a couple of the other guys in the gym shoot you knowing looks as you go about your workout."
#         "During the bench press, [the_person.title] stands right above you, her crotch tantalizingly close to your face."
#         $ the_person.change_max_energy(5)
#         the_person "Wow, what a workout! So... are you gonna go hit the showers now?"
#         "It is clear from the way she is asking she is curious if you are gonna follow her to the secluded locker room."
#         menu:
#             "Hit the Shower":
#                 #TODO some kind of innuendo joke here#
#                 mc.name "Yeah, I'm pretty sweaty. I'd better get cleaned up!"
#                 $ the_person.draw_person( emotion = "happy")
#                 "She gets close to you and whispers in your ear."
#                 the_person "You now where to go... meet me in 5."
#                 $ the_person.draw_person( position = "walking_away")
#                 "You watch [the_person.title]'s amazing ass as she walks away. You swear there's a bit of a swagger there."
#                 "You give her a few minutes, then follow after her."
#
#                 #locker room sex scene.
#                 $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True)
#                 $ the_person.draw_person( position = "stand2")
#                 "As you enter, you see that [the_person.title] is already naked."
#                 the_person "[the_person.mc_title], give me that cock! It's been too long since you fucked me good!"
#                 "You walk over to her and quickly strip. You grab [the_person.title] by that ass and pick her up. You carry her to the wall and pin her up against it."
#                 $ the_person.draw_person( position = "against_wall")
#                 "[the_person.possessive_title] is grinding her hips up against yours. The sweat from your workouts mingles together as you prepare yourself to enter her."
#
#                 $ the_person.add_situational_slut("horny", 20, "She is desperate to be fucked")
#
#                 # NOTE skip intro prevents taboo break from executing
#
#                 call condom_ask(the_person) from _casual_athlete_mod_condom_ask_CS011
#                 "As you begin to push yourself inside her, she drags her nails across your back."
#                 if not mc.condom:
#                     $ the_person.break_taboo("condomless_sex")
#                 the_person "Oh fuck, that's good. Give it to me good, [the_person.mc_title]!"
#                 call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_casual_sex_mod_CS011
#                 $ the_report = _return
#                 if the_report.get("girl orgasms", 0) > 0:
#                     "As you slowly let [the_person.title] down from the wall, you can see her trembling, caused by aftershocks from her orgasm."
#                     the_person "Mmm... god I'm glad you know how to use that cock."
#                 $ the_person.clear_situational_slut("horny")
#                 "Without another word, you and [the_person.title] take a quick shower, then get ready and leave the gym."
#
#             "Not Today":  #lol what a tease#
#                 the_person "Oh. Okay, I understand. Well, I'll see you around, [the_person.mc_title]!"
#                 $ the_person.change_happiness(-3)
#
#     $ the_person.apply_planned_outfit()
#     call advance_time from _call_advance_casual_athlete_workout
#     return
#
# #CSA20
# label casual_athlete_phase_two_label(the_person):
#     if the_person.event_triggers_dict.get("athlete_progress", 0) == 2:
#         "You see [the_person.title] on the treadmill. She is running hard, and has been training for a race coming up soon. She pauses the treadmill as you walk up to her."
#         the_person "Hey [the_person.mc_title], here for another workout?"
#         mc.name "Not today, [the_person.title]. How goes training? Is that big race coming up soon?"
#         if day % 7 == 4:  #It is friday, the race is tomorrow!
#             the_person "Yeah! As a matter of fact, it's tomorrow!"
#         else:
#             the_person "Yeah! It's coming up quick, on Saturday morning!"
#         "She checks you out for a minute, before continuing."
#         the_person "You know, it's a charity race, with proceeds going to breast cancer! You seem pretty fit, and I know how much you love tits. Maybe you should race too?"
#         "You give her a smile."
#         mc.name "Ah, that sounds like a good cause, but I couldn't. I'd hate for our arrangement to come to an end because we are in the same race and I beat you and you get mad."
#         the_person "Hah! You wish! You seem awfully confident. I tell you what, why don't we make a little bet?"
#         "You are intrigued by where she is going with this."
#         mc.name "Go on."
#         the_person "You come out and race. When the race is over, we go back to my place, and whoever won gets to do anything they want with the loser!"
#         mc.name "Anything?"
#         "She gives you a wink."
#         the_person "That's what I said, isn't it?"
#         mc.name "You've got a deal. Saturday morning downtown. I'll be there."
#         $ the_person.draw_person (position = "stand4")
#         the_person "Yes! Oh my [the_person.mc_title], no backing out now! I'll have to find my handcuffs..."
#         "[the_person.title] seems pretty confident in herself, but you are pretty sure you have good odds in a race."
#         "You wave goodbye to [the_person.title], wondering what you've gotten yourself in to."
#
#         $ add_casual_athlete_race_crisis(the_person)
#
#         $ the_person.event_triggers_dict["athlete_progress"] = 3
#     elif the_person.event_triggers_dict.get("athlete_progress", 0) == 3:
#         mc.name "Hey [the_person.title], I just wanted to verify, the race is this Saturday, right?"
#         the_person "That's right! I can't wait to beat your ass in the race, and then spank it again later at my place!"
#         mc.name "Yeah right, I'll be bending you over before you can even get your front door closed."
#         "[the_person.title] has a spark in her eyes. Whoever wins, you have a feeling the sex is going to be amazing after the race."
#         "You wave goodbye to [the_person.title], wondering what you've gotten yourself in to."
#
#     $ the_person.apply_planned_outfit()
#     call advance_time from _call_advance_casual_athlete_race_challenge
#     return
#
# #CSA30
# label casual_athlete_race_crisis_label(the_person):
#     "It's race day! You make your way downtown, ready for your race with [the_person.title]."
#     $ mc.change_location(downtown)
#     $ mc.location.show_background()
#     "You find where they are organizing the race. It is a 5 kilometer race, which is about three miles long."
#     "You look around and eventually find [the_person.title]."
#     $ the_person.apply_gym_outfit()
#     $ the_person.draw_person(position = "stand3")
#     the_person "Hey, there you are! I was starting to think you had chickened out!"
#     mc.name "Not a chance. I hope you don't have any plans for tomorrow, because when I get done with you tonight you won't be able to get out of bed until Monday at least!"
#     the_person "Oh my, brave words for a brave boy! Let's just see what happens!"
#     "You and [the_person.title] do some stretching and warmups, but soon it is time for the race to begin."
#     "You line up together at the starting line, ready for the race to begin."
#     "*BANG*"
#     $ the_person.draw_person(position = "walking_away")
#     "The official starts the race with a shot from the gun and the race begins! [the_person.title] jumps out in front of you, setting a fast pace."
#     "You are tempted to chase after her, but think better of it. This is a long race, and you need to pace yourself."
#     $ clear_scene()
#     "As you near the first kilometer, you lose sight of [the_person.title] in the crowd of racers, but you are sure you aren't far behind."
#     "You settle into your pace, determined to let your energy carry you through the race, no matter what happens. You pass the second kilometer marker"
#     "You breathe in, you breathe out. You take pace after pace, determined to race with the best of your abilities."
#     "As you approach the third kilometer marker, you can see yourself catching up to a familiar form."
#     $ the_person.draw_person(position = "walking_away")
#     "God she is hot, her ass sways back and forth with each step she takes. You imagine all the things you want to do with those delightfully tight cheeks."
#     "You are breathing hard. It's getting so hard to keep up. She starts to pull away from you."
#     "No! It's time to dig deep! You pump your arms and breath deep."
#     "After a few moments, you catch your second wind. You get a burst of energy and race faster."
#     "You are catching up to her, and you find yourself running with a renewed vigor from the flow of testosterone in your bloodstream, day dreaming about [the_person.possessive_title]."
#     "You pass the marker for the fourth kilometer. This is it, it's now or never!"
#     "You surge forward, and soon you are right beside her. She is gasping for air, she is completely winded!"
#     the_person "[the_person.mc_title]? Oh god..."
#     "She barely gets her words out as you pass her."
#     $ clear_scene()
#     "You keep pushing forward, not daring to turn around."
#     "You round a corner. The finish line! You give it everything you have! Your breathing is heavy and ragged, sucking in every ounce of air you can."
#     "You cross the finish line. You beat her!!!"
#     "You are catching your breath, and turn to see her cross the finish line just a few seconds behind you."
#     $ the_person.draw_person(position = "standing_doggy")
#     "[the_person.title] is breathing hard. She walks up to a table nearby and bends over with her hands on it, trying desperately to catch her breath."
#     "You walk up behind her and put your hands on her back. You are careful not to be too obvious, but you make some contact with her backside with your hips."
#     mc.name "Hey there, [the_person.title]! Nice race! I'm so glad you invited me out here to support such a charitable cause..."
#     $ the_person.draw_person(position = "stand4")
#     "She stands up and turns to face you."
#     the_person "Yeah!... I mean, it's all for a good cause, right?"
#     $ the_person.change_max_energy(10)
#     $ the_person.draw_person(position = "stand4", emotion = "happy")
#     "You think you see a little smirk on the corner of her mouth."
#     "You both take a few minutes to recover, and soon you are ready to go."
#     the_person "Alright, you won the race. I guess it's time to head back to my place?"
#     "You call for an Uber and she gives you here address. Soon you are walking into [the_person.title]'s apartment."
#     $ mc.change_location(the_person.home)
#     $ mc.location.show_background()
#     $ the_person.learn_home()
#     "As soon as you walk in the door, you grab [the_person.title]. You pick her up and push her against the wall."
#     $ the_person.draw_person(position = "against_wall")
#     #TODO add temporary sluttiness to make sure she is up for anything###
#     $ the_person.add_situational_slut("Lost Bet",25,"Be ready for anything!")
#     the_person "Fuck! Mmm, are we gonna start right here? I remember the terms, do what you want to with me..."
#     "You growl into her neck as you grind your hips into hers."
#     mc.name "That's right, you're my sexy bitch for the day."
#     "You back up from the wall, but hold her tight, keeping her feet from reaching the floor. You turn and take her into her bedroom."
#     $ the_person.draw_person(position = "missionary")
#     "You throw her down on her bed."
#     if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
#         "You stop for a second and admire [the_person.title], her body on display in front of you."
#         $ the_person.change_arousal(20)
#         "You notice some moisture building around her slit. She is definitely enjoying your hungry eyes roaming her body."
#     else:
#         "Your mind red with lust, you begin to rip [the_person.title]'s clothes off."
#
#         $ the_person.strip_outfit(position = "missionary")
#         $ the_person.change_arousal(20)
#
#         "[the_person.possessive_title] moans as you strip her down, enjoying your rough treatment of her."
#     "When she is full naked, you grab her hips and flip her over."
#     $ the_person.draw_person(position = "doggy")
#     $ the_person.change_arousal(5)
#     "There it is, the ass that inspired your final push in the race. She lowers her face to the bed and wiggles her hips at you."
#     "In a moment you are naked. You hop up on the bed and get behind her. You grab her hips and roughly pull her back toward you."
#     "You rub her slit up and down with your furious erection, coating it with her juices. You give her ass a rough spank, eliciting a yelp."
#     $ the_person.change_arousal(10)
#     the_person "Oh fuck, please just put it in. I feel like I'm on fire!!!"
#     "You consider for a second putting on a condom first. Nope, not a fucking chance. In one smooth motion you push yourself into her sopping, needy cunt."
#     the_person "Yes!!! Oh god, please fuck me good!"
#     "You have every intention of doing exactly that."
#     call fuck_person(the_person, private=True, start_position = doggy, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_casual_sex_mod_CS030
#     $ the_report = _return
#
#     $ the_person.clear_situational_slut("Lost Bet")
#     "When you finish with her, [the_person.possessive_title] lays down on her bed."
#     $ the_person.draw_person(position = "missionary")
#     if the_report.get("girl orgasms", 0) > 0:
#         the_person "[the_person.mc_title]... I am so sore... My legs from the race... and... you know..."
#         the_person "But that was amazing... Look, I'll be your sexy bitch anytime you want, okay? You have my address now, feel free to stop by. Just promise you'll fuck me like that again."
#         "You laugh."
#     else:
#         the_person "This was really great... Look, I'll be your sexy bitch anytime you want, okay? You know where I live now, so stop by anytime you feel like it."
#
#     mc.name "Sounds good. You have my number, let me know if you wanna hookup sometime, or if you want a rematch!"
#     the_person "Ayup! Don't worry. If it's all the same to you, I think I'm gonna take a nap now..."
#     "You excuse yourself. You grab your clothes and head out. You now know [the_person.title]'s address, with a standing offer to come over and fuck her silly!"
#     $ the_person.event_triggers_dict["athlete_progress"] = 4
#     $ perk_system.add_stat_perk(Stat_Perk(description = "Training for the big race has helped improve your energy level. +20 max energy, +40 energy cap.", energy_bonus = 20, bonus_is_temp = False, energy_cap = 40), "Athlete Energy Bonus")
#     $ perk_system.add_ability_perk(Ability_Perk(description = "You take a few deep breaths and recover a bit of your energy. Use this perk to regain half your max energy, once per day.", toggle = False, usable = True, usable_func = second_wind_func, usable_cd = 1), "Second Wind")
#     "You walk away with a spring in your step. You feel like training for and running the race has given you more energy."
#     "You have gained the second wind ability perk. You can now recover half your max energy, once per day!"
#     return
#
# label casual_athlete_buy_protein_shake_label(the_person):
#     mc.name "Hey [the_person.name], I see you're working pretty hard today! Can I get you a protein shake?"
#     "[the_person.possessive_title] looks at you and smiles."
#     the_person "That sounds great!"
#     $ clear_scene()
#
#     "You head over to the counter where they have the supplements. You order her a protein shake."
#     $ mc.business.change_funds(-5)
#     "Before you take it back to her, you have a moment with no one around. You can add a serum to it if you do it quickly!"
#     menu:
#         "Add a dose of serum to [the_person.title]'s shake":
#             call give_serum(the_person) from _call_give_serum_casual_athlete
#             $ the_person.draw_person(emotion = "happy")
#             "You mix the serum into [the_person.title]'s protein shake. You take it over to her."
#             the_person "Thanks [the_person.mc_title]."
#             mc.name "No problem at all."
#             $ clear_scene()
#
#
#         "Leave her drink alone.":
#             "You decide not to test a dose of serum out on [the_person.title] and take the shake back to her."
#             $ the_person.draw_person(emotion = "happy")
#             the_person "Thanks [the_person.mc_title]."
#             mc.name "No problem at all."
#             $ clear_scene()
#
#     $ the_person.apply_planned_outfit()
#     call advance_time from _call_advance_casual_athlete_smoothie
#     return
#
# #CSA40
# label casual_athlete_house_call_label(the_person):
#     mc.name "Don't worry, I'm not here for business. I'm here for pleasure!"
#     $ the_person.draw_person( position = "against_wall")
#     "You reach around with both hands and grab her ass. You roughly pick her up, holding her tightly against you."
#     the_person "Oh! Yes I was hoping that's why you were here..."
#     "[the_person.possessive_title] wraps her legs around you and you begin to grind your hips together. Heat is quickly building between the two of you."
#     "You carry her to her bedroom. The whole way there she is kissing and nipping at your neck and earlobe."
#     $ the_person.draw_person(position = "missionary")
#     "You throw her down on her bed."
#     if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
#         "You stop for a second and admire [the_person.title], her body on display in front of you."
#         $ the_person.change_arousal(20)
#         "You notice some moisture building around her slit. She is definitely enjoying your hungry eyes roaming her body."
#     else:
#         "Your mind red with lust, you begin to rip [the_person.title]'s clothes off."
#
#         $ the_person.strip_outfit(position = "missionary")
#         $ the_person.change_arousal(20)
#
#         "[the_person.possessive_title] moans as you strip her down, enjoying your rough treatment of her."
#     call fuck_person(the_person) from _call_casual_sex_mod_CSA040
#     $ the_report = _return
#     "After you finish with her, you get up and start to gather your clothes."
#     if the_report.get("girl orgasms", 0) > 0:
#         "[the_person.possessive_title] is in an orgasm fueled daze, enjoying the effects it has on her."
#     the_person "Thanks for stopping by... I think I'm just gonna lay down for a bit..."
#     "Once you finish getting dressed you say goodbye and let yourself out."
#
#     $ mc.change_location(bedroom) # go home
#     call advance_time from _call_advance_casual_athlete_house_call
#     return
#
# label casual_athlete_ghost_label(the_person):
#     "You get a message on your phone. Looks like it is from [the_person.possessive_title]."
#     the_person "Hey, I'm really sorry to have to do this, but I think I'm catching feelings."
#     the_person "We agreed at the beginning we wouldn't let that happen, so I don't think we should see each other anymore."
#     the_person "I'm changing to a different gym, and after I send this, I'm going to block your number. I'm sorry."
#     "Damn. Sounds like you pushed things with her a little too far..."
#     $ the_person.remove_person_from_game()
#     $ casual_sex_create_athlete() #Create a new athlete so MC can try again if they choose.
#     return
# #************* Personality****************#
# #Override some of her personality functions so that her conversation options makes sense.
#
# init 1301 python:              #Because Vren Init personality functions at 1300
#
#     def athlete_titles(person):
#         valid_titles = []
#         valid_titles.append(person.name)
#         if person.effective_sluttiness() > 40:
#             valid_titles.append("College Athlete")
#             valid_titles.append("Cardio Bunny")
#         if person.effective_sluttiness() > 60:
#             valid_titles.append("Slutty Athlete")
#         return valid_titles
#
#     def athlete_possessive_titles(person):
#         valid_possessive_titles = ["Your gym girl",person.title]
#
#         if person.effective_sluttiness() > 60:
#             valid_possessive_titles.append("Your gym slut")
#
#         if person.effective_sluttiness() > 80:
#             valid_possessive_titles.append("The gym cumdump")
#             valid_possessive_titles.append("The gym bicycle")
#         return valid_possessive_titles
#
#     def athlete_player_titles(person):
#         return mc.name
#
#     athlete_personality = Personality("athlete", default_prefix = "introvert",
#     common_likes = ["small talk", "the colour blue", "sports", "taking control"],
#     common_sexy_likes = ["casual sex", "doggy style sex", "giving blowjobs", "showing her ass", "drinking cum"],
#     common_dislikes = ["relationships", "conservative outfits", "makeup", "the colour pink", "dresses", "high heels", "the colour purple"],
#     common_sexy_dislikes = ["lingerie", "being submissive", "skimpy outfits"],
#     titles_function = athlete_titles, possessive_titles_function = athlete_possessive_titles, player_titles_function = athlete_player_titles)
#
# #************* Personality labels***************#
#
#
# label athlete_greetings(the_person):
#     if mc.location == gym:
#         if the_person.love > 50:  #She loves you too much and is going to or already has called things off
#             the_person "Oh... hello, [the_person.mc_title]."
#             $ add_casual_athlete_ghost_action(the_person)
#             return
#         if the_person.event_triggers_dict.get("athlete_progress", 0) >= 2:
#             the_person "Hey there, [the_person.mc_title]."
#             "You see [the_person.title] here at the Gym, in her usual spot on the treadmill."
#             the_person "You want to join me for another workout? I always leave the gym feeling so satisfied when we work out together!"
#         else:
#             the_person "Hey there!"
#     elif mc.location == the_person.home:
#         if the_person.event_triggers_dict.get("athlete_progress", 0) > 3:
#             the_person "Hey there, [the_person.mc_title]! I wasn't expecting you! Are you here for some fun?"
#             "She looks at you hopefully."
#         else:
#             the_person "Hey there, [the_person.mc_title]. I wasn't expecting you, are you sure you should be here?"
#
#     elif the_person.effective_sluttiness() > 60:
#         if the_person.obedience > 130:
#             the_person "Hello, [the_person.mc_title], it's good to see you."
#         else:
#             the_person "Hey there handsome, feeling good?"
#     else:
#         if the_person.obedience > 130:
#             the_person "Hello, [the_person.mc_title]."
#         else:
#             the_person "Hey there!"
#     return
#
# label athlete_sex_responses(the_person):
#     if the_person.effective_sluttiness() > 50:
#         if the_person.obedience > 130:
#             the_person "Oh my, keep doing that please!"
#         else:
#             the_person "Fuck it feels good when you do that. Keep going!"
#     else:
#         "[the_person.title] closes her eyes and moans quietly to herself."
#     return
#
# label athlete_climax_responses_foreplay(the_person):
#     if the_person.effective_sluttiness() > 50:
#         the_person "Oh fuck yes, I'm going to cum! I'm cumming!"
#     else:
#         the_person "Oh fuck, you're going to make me cum! Fuck!"
#         "She goes silent, then lets out a shuddering moan."
#     return
#
# label athlete_climax_responses_oral(the_person):
#     if the_person.effective_sluttiness() > 70:
#         the_person "Fuck yes, I'm going to cum! Make me cum!"
#     else:
#         the_person "Oh my god, you're good at that! I'm going to... I'm going to cum!"
#     return
#
# label athlete_climax_responses_vaginal(the_person):
#     if the_person.effective_sluttiness() > 70:
#         the_person "I'm going to cum! Ah! Make me cum [the_person.mc_title], I want to cum so badly! Ah!"
#         "She closes her eyes and squeals with pleasure."
#     else:
#         the_person "Ah! I'm cumming! Oh fuck! Ah!"
#     the_person "Fuck this feels better than winning a marathon!"
#     return
#
# label athlete_climax_responses_anal(the_person):
#     if the_person.effective_sluttiness() > 70:
#         the_person "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
#         the_person "Ah! Mmhmmm!"
#     else:
#         the_person "Oh fucking shit, I think you're going to make me..."
#         "She barely finishes her sentence before her body is wracked with pleasure."
#         the_person "Cum!"
#     return
#
# label athlete_clothing_accept(the_person):
#     if the_person.obedience > 130:
#         the_person "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
#     else:
#         the_person "Thanks [the_person.mc_title]! I wonder if I could wear this at the gym."
#     return
#
# #label athlete_clothing_reject(the_person):
# #    if the_person.obedience > 130:
# #        the_person "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
# #    else:
# #        if the_person.effective_sluttiness() > 60:
# #            the_person "Wow. I'm usually up for anything but I think that's going too far."
# #        else:
# #            the_person "Wow. It's a little... skimpy. I don't think I could wear that."
# #    return
#
# label athlete_clothing_review(the_person):
#     if mc.location == gym:
#         if the_person.effective_sluttiness() > 40:
#             the_person "I love when you look at me like that, but I don't think the gym staff would appreciate it as much. I'd better clean up a bit."
#         else:
#             the_person "I'd better clean up some before I go to leave the gym..."
#     elif the_person.obedience > 130:
#         the_person "I'm sorry [the_person.mc_title], you shouldn't have to see me like this. I'll go and get cleaned up so I'm presentable again."
#     else:
#         if the_person.effective_sluttiness() > 40:
#             the_person "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
#         else:
#             the_person "My clothes are a mess! I'll be back in a moment, I'm going to go get cleaned up."
#     return
#
# #label athlete_strip_reject(the_person, the_clothing, strip_type = "Full"):
# #    if the_person.obedience > 130:
# #        the_person "I'm sorry, but can we leave that where it is for now?"
# #    elif the_person.obedience < 70:
# #        the_person "Slow down there, I'll decide when that comes off."
# #    else:
# #        the_person "I think that should stay where it is for now."
# #    return
#
# label athlete_sex_accept(the_person):
#     if the_person.effective_sluttiness() > 70:
#         if the_person.obedience < 70:
#             the_person "I was just about to suggest the same thing."
#         else:
#             the_person "Mmm, you have a dirty mind [the_person.mc_title], I like it."
#     else:
#         the_person "Okay, we can give that a try."
#     return
#
# label athlete_sex_obedience_accept(the_person):
#     if the_person.effective_sluttiness() > 70:
#         the_person "Oh god [the_person.mc_title], I should really say no... But you always make me feel so good, I can't say no to you."
#     else:
#         if the_person.obedience > 130:
#             the_person "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
#         else:
#             the_person "I... Okay, if you really want to, lets give it a try."
#     return
#
# label athlete_sex_gentle_reject(the_person):
#     if the_person.effective_sluttiness() > 50:
#         the_person "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
#     else:
#         the_person "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
#     return
#
# label athlete_sex_angry_reject(the_person):
#     if the_person.effective_sluttiness() < 20:
#         the_person "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
#         the_person "Ugh! Get away from me, I don't even want to talk to you after that."
#     else:
#         the_person "What the fuck do you think you're doing, that's disgusting!"
#         the_person "Get the fuck away from me, I don't even want to talk to you after that!"
#     return
#
# label athlete_seduction_response(the_person):
#     if the_person.obedience > 130:
#         if the_person.effective_sluttiness() > 50:
#             the_person "Yes [the_person.mc_title]? Do you need help relieving some stress?"
#         else:
#             the_person "Yes [the_person.mc_title]? Is there something I can help you with?"
#     else:
#         if the_person.effective_sluttiness() > 50:
#             the_person "Mmm, I know that look. Do you want to fool around a little?"
#         elif the_person.effective_sluttiness() > 10:
#             the_person "Oh, do you see something you like?"
#         else:
#             the_person "Oh, I don't really know what to say [the_person.mc_title]..."
#     return
#
# label athlete_seduction_accept_crowded(the_person):
#     if mc.location == gym:
#         if the_person.effective_sluttiness() < 20:
#             the_person "I suppose we could sneak away into the locker room... There's nothing wrong with that, right?"
#         elif the_person.effective_sluttiness() < 70:
#             the_person "Come on, let's sneak into the locker room and do it!"
#         else:
#             the_person "Oh fuck that sounds nice. I'm not sure I can wait until we sneak into the locker room, maybe we should just do it right here!"
#         return
#
#     if the_person.effective_sluttiness() < 20:
#         the_person "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
#     elif the_person.effective_sluttiness() < 50:
#         the_person "Come on, let's go find someplace quiet where we won't be interrupted."
#     else:
#         the_person "No point wasting any time then, right? Let's get to it!"
#     return
#
# label athlete_seduction_accept_alone(the_person):
#     if mc.location == gym:
#         if the_person.effective_sluttiness() < 20:
#             the_person "Well, there's nobody around to see us..."
#         elif the_person.effective_sluttiness() < 50:
#             the_person "I can't believe how empty the gym is right now. Let's do it right here!"
#         else:
#             the_person "Oh [the_person.mc_title], the gym is empty, fuck me now!"
#         return
#     if the_person.effective_sluttiness() < 20:
#         the_person "Well, there's nobody around to stop us..."
#     elif the_person.effective_sluttiness() < 50:
#         the_person "Mmm, that's a fun idea. Come on, let's get to it!"
#     else:
#         the_person "Oh [the_person.mc_title], don't make me wait!"
#     return
#
# #label athlete_seduction_refuse(the_person):
# #    if the_person.effective_sluttiness() < 20:
# #        "[the_person.title] blushes and looks away from you awkwardly."
# #        the_person "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."
# #
# #    elif the_person.effective_sluttiness() < 50:
# #        the_person "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
# #        "[the_person.title] smiles and gives you a wink."
# #
# #    else:
# #        the_person "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
# #    return
#
# label athlete_flirt_response(the_person):
#     if mc.location == gym:
#         if the_person.love > 50:  #She loves you too much and is going to or already has called things off
#             the_person "Didn't your mother ever tell you it's rude to hit on girls at the gym?"
#             return
#         if the_person.event_triggers_dict.get("athlete_progress", 0) >= 2:
#             the_person "Well why don't you workout with me for a bit and we can work up a sweat together?"
#         else:
#             the_person "Hey, maybe if you workout with me first."
#             "[the_person.title] gives you a wink and smiles."
#         return
#
#     if the_person.obedience > 130:
#         if the_person.effective_sluttiness() > 50:
#             the_person "If that's what you want I'm sure I could help with that [the_person.mc_title]."
#         else:
#             the_person "Thank you for the compliment, [the_person.mc_title]."
#     else:
#         if the_person.effective_sluttiness() > 50:
#             the_person "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peek."
#             "[the_person.title] smiles at you and spins around, giving you a full look at her body."
#         else:
#             the_person "Hey, maybe if you buy me dinner first."
#             "[the_person.title] gives you a wink and smiles."
#     return
#
# label athlete_flirt_response_low(the_person):
#     #She's in her own outfit.
#     "[the_person.possessive_title] blushes and smiles."
#     the_person "Thanks. I didn't think anyone even paid attention to what I wear. I mean it's just gym clothes..."
#     mc.name "Yeah, and the way you dress makes it obvious how well you take care of yourself. It's pretty incredible."
#     return
#
# label athlete_flirt_response_mid(the_person):
#
#     if the_person.effective_sluttiness() < 20:
#         the_person "Thanks! I work hard to take care of myself. It's kind of weird to hear, but I'm glad it shows."
#
#     else:
#         the_person "Thanks! One of the benefits of being in shape I guess, you can wear clothing to show off your body."
#         the_person "You want a better look, right? Here, how does it make my ass look?"
#         $ the_person.draw_person(position = "back_peek")
#         the_person "Good?"
#         mc.name "Fantastic. I wish I could get an even better look at it."
#         "[the_person.possessive_title] smiles and turns back to face you."
#         $ the_person.draw_person()
#         the_person "I'm sure you do. Maybe instead of shooting the breeze you should workout with me..."
#     return
#
# label athlete_flirt_response_high(the_person):
#     if the_person.love > 50: #She is going to ghost soon
#         the_person "I feel like you are going a little overboard there with the flattery. Could you please stop?"
#     else:
#         "She looks at you and her eyes narrow."
#         the_person "I appreciate the comment, I really do... but I'm worried you are taking things a little too far."
#         the_person "Remember, we need to keep things CASUAL. Okay?"
#     return
#
#
# label athlete_hookup_rejection(the_person):
#     the_person "Your loss! I've been working out so much lately, and you could have had some of this..."
#     return
#
# label athlete_hookup_accept(the_person):
#     the_person "Meet me at the gym... you know the place!"
#     "You put your phone in your pocket and head to the gym."
#
#     $ mc.change_location(gym)
#     $ mc.location.show_background()
#
#     "A few minutes later, you walk into the gym. You locate the family locker room and discover it to be unlocked. You quietly let yourself in."
#     $ the_person.draw_person(position = "missionary")
#     $ the_person.arousal = 20
#     "You discover [the_person.possessive_title] sitting at one of the sinks, touching herself while waiting for you. Her pussy glistens with arousal."
#     "You quickly lock the door behind you. She notices you walk in but doesn't say a word."
#     "You walk over to her silently, and then get down on your knees in front of her. Her pussy is hanging off the side of the sink, right in front of your face."
#     "You waste no time and dive your tongue straight into her cunt. Her tangy juices greet your tongue."
#     the_person "Mmmm, this is my favorite warm up..."
#     $ the_person.change_arousal( 15 + (mc.sex_skills["Oral"] * 2)) #35 + 2
#     "You quickly lap up the juices available along her labia, then focus your attention on her clitoris with the goal of making more."
#     "You circle your tongue around it several times, teasing her. Just when she thinks you are going to lick it you dart down to her hole."
#     the_person "What a tease! I had a boyfriend once who couldn't find my clit either... here let me help you."
#     $ the_person.change_arousal( 15 + (mc.sex_skills["Oral"] * 2)) #50 + 4
#     "[the_person.title] runs a hand through your hair, then grabs some of it on the back of your head. She begins to gyrate her hips as she grinds into you."
#     "You decide to go with it. You flatten your tongue out and begin to move it across her clitoris in long strokes."
#     "She grinds herself happily against your face. She moans appreciatively at your skilled oral stimulation."
#     $ the_person.change_arousal( 15 + (mc.sex_skills["Oral"] * 2)) #65 + 6
#     if the_person.arousal > 100: #She is surprised how fast you make her cum
#         "Suddenly, you feel her body go stiff and her moans ramp up quickly."
#         the_person "Fuck! I'm gonna... you're gonna make me...!"
#         "[the_person.title] convulses as she orgasms. She is caught completely off guard by how fast you made her cum."
#         "The hand on the back of your head lets go but you continue your assault for several more seconds."
#         $ the_person.change_slut(1)
#         $ the_person.change_happiness(2)
#     else:
#         the_person "Mmm, that's it. Your tongue feels so good. Give it a good workout..."
#         "[the_person.title]'s hand leaves the back of your head but you keep going. You lightly suck on her clit, drawing it into your mouth a few seconds at a time before licking it again."
#         "Her body is responding. Her hips are starting to twitch back and forth on their own as she approaches an orgasm."
#         $ the_person.change_arousal( 15 + (mc.sex_skills["Oral"] * 2)) #80 + 8
#         if the_person.arousal > 100: #She orgasms
#             the_person "Yes! That's it! I'm gonna cum!"
#             "[the_person.title] convulses as she orgasms. She moans and runs her hands through your hair."
#             "You continue your assault for several more seconds."
#         else:   #Not skilled enough to make her orgasm.
#             "You are feverishly working at her pussy, but for some reason you can seem to find the right spot."
#             "Soon, the stimulation gets to be too much for her and she puts her hand on your hand and slowly pushes it back."
#     $ the_person.change_arousal(-30) #50 + 8
#     the_person "Mmm, that was a great warmup. Let me return the favor."
#     "[the_person.possessive_title] hops down from the sink. She quickly helps your undress, then gets down on her knees in front of you."
#     $ the_person.draw_person(position = "blowjob")
#     "She gives your cock a few slow strokes before she begins to lick the tip. Her tongue feels like wet velvet as it circles around your glans."
#     "[the_person.title] opens her mouth and then envelopes the end of your dick with her warm, wet mouth."
#     "[the_person.title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
#     "It feels amazing, you can tell if you let her keep going you will cum quickly."
#     #TODO write blwjob finish scene#
#     mc.name "That feels great, but I don't want to finish in your mouth. Why don't you stand up and turn around..."
#     $ the_person.draw_person( position = "standing_doggy")
#     if the_person.effective_sluttiness() > 40: #She asks if you want to use a condom
#         the_person "Do you want to put on a condom first?"
#         menu:
#             "Put on a condom":
#                 mc.name "Yeah, I'd probably better. I may not be able to resist pulling out."
#                 if the_person.effective_sluttiness() > 60:
#                     the_person "I mean... it's okay with me if you wanted to stick it in for a little bit without one on, you know, just to get started..."
#                     if the_person.effective_sluttiness() > 90:
#                         the_person "...or even just finish inside me. I promise I wouldn't mind at all!"
#                     mc.name "Maybe next time!"
#                 "You get a condom and put it on quickly."
#                 $ mc.condom = True
#             "Fuck her raw":
#                 $ mc.condom = False
#                 mc.name "No way, I want to feel everything."
#                 if the_person.effective_sluttiness() > 60:
#                     the_person "Mmmm, sounds good. I was hoping you would say that!"
#                     if the_person.effective_sluttiness() > 80:
#                         "She wiggles her ass back and forth a little bit."
#                         the_person "You don't need to worry about pulling out. I like it better when I feel the splash anyway..."
#                 else:
#                     the_person "Okay, just make sure to pull out before you finish, okay?"
#     else:
#         the_person "You have a condom right? Make sure you put one on..."
#         mc.name "Right! I'd probably better. I may not be able to resist pulling out."
#         "You get a condom and put it on quickly."
#         $ mc.condom = True
#     "You put your hands on her hips and put your dick at her entrance. She is still soaked from your oral earlier, so you easily slide into her."
#     "Her pussy feels amazing wrapped around your erection. Her legs shake a bit as she gets used to the depth of your penetration."
#     $ the_person.change_arousal(20) #70 + 8
#     the_person "Ohhh, [the_person.mc_title]... That is exactly what I was hoping for when I sent you that text earlier. That feels so good..."
#     "You give her a few tentative thrusts, then quickly pick up the pace and begin fucking her in earnest."
#     "Your hips slap against [the_person.possessive_title]'s ass as you fuck her vigorously."
#     $ the_person.call_dialogue("sex_responses_vaginal")
#     if mc.condom == True:
#         "You grasp her ass with both hands and begin to grope her. You knead her cheeks as your hips slowly work your erection in and out of her."
#         $ the_person.change_arousal(20) #90 + 8
#         if the_person.arousal > 100:
#             "You can feel [the_person.title]'s pussy begin to spasm as she cums. You can see in the mirror that her mouth is hanging open and her eyes are closed."
#             $ the_person.change_slut(1)
#             $ the_person.change_happiness(2)
#         "After the stimulation from hew blowjob earlier, you know you aren't going to last long. You give her ass a loud spank."
#         mc.name "That's it, bitch. I'm about to cum!"
#         if the_person.effective_sluttiness() > 100: #She is so slutty, she begs for your cum.
#             the_person "The condom! Take it off! Please!?! Your cock is so good, I want to feel you dump your load inside me!"
#             "Your brain is getting a little hazy with lust. Surely there's nothing wrong with that, right?"
#             menu:
#                 "Take It Off":
#                     "In one swift you pull out of [the_person.title], pull the condom off, then shove yourself deep back inside her."
#                     "You wad up the condom then throw it on the counter. It lands with splat."
#                     the_person "Yes! Cum for me! I want to feel it!"
#                     $ the_person.change_arousal(20) #110 + 8
#                     "Her excitement is too much. You bottom out and cum, dumping wave after wave of your semen deep inside of her."
#                     the_person  "Yes! Fill me with your cum!"
#                     "You feel her pussy convulsing around your dick as she also starts to orgasm."
#                     $ the_person.change_slut(1)
#                     $ the_person.change_happiness(2)
#                     $ the_person.cum_in_vagina()
#                     "You wait until your orgasm has passed completely, then pull out and stand back. You cum leaks from her well used pussy."
#                     "You take a moment to recover. Then you and [the_person.title] get cleaned up and dress. You quietly sneak out of the locker room."
#                     return
#                 "Leave It On":
#                     mc.name "I can't pull out, even for a second!"
#         "You bottom out and cum, dumping your load into the condom."
#         "You wait until your orgasm has passed completely, then pull out and stand back. Your condom is bulged on the end where it is filled with your seed."
#         if the_person.arousal < 100:
#             the_person "Wow, okay, I guess we are done?"
#             $ the_person.change_happiness(-5)
#             $ the_person.change_obedience(-5)
#             "She is a bit disappointed she didn't finish."
#         else:
#             the_person "That was nice. I'll make sure next time I'm in the mood to hit you up again..."
#         "You take your condom off and throw it in the trash can. You both get dressed before sneaking out of the locker room."
#         return
#     else: #You went in raw
#         "You push yourself in as deep as you can go. [the_person.possessive_title] moans as you fill her completely."
#         "With every thrust, her ass ripples pleasantly. You give her cheek an open handed spank and watch as shockwaves expand from the epicenter."
#         "[the_person.title] moans at your rough treatment."
#         $ the_person.change_arousal(20) #70 + 8
#         if the_person.arousal > 100:
#             "You can feel [the_person.title]'s pussy begin to spasm as she cums. Her silky wetness contracting around you feels amazing."
#             $ the_person.change_slut(1)
#             $ the_person.change_happiness(2)
#     if the_person.effective_sluttiness() > 70:
#         the_person "You should umm, you know, stick a finger in my other hole..."
#         "Wow, it's not every day you have a beautiful woman ask you to finger her ass while you bend her over and fuck her!"
#         "You reach a hand forward and put your index finger in front of her face. She quickly gets the idea and opens her mouth with her tongue out, and begins slathering your finger with saliva."
#         "When satisfied, you bring you fingers back to her tight back passage. You pull your cock almost completely out and stop you hip motion as you begin to press your finger against [the_person.title]'s puckered hole."
#         "She forces her sphincter to relax and your finger begins to slip inside her."
#         the_person "Ohh, yes. You can move your hips, that feels good..."
#         "You give [the_person.possessive_title]'s cunt a few slow thrusts, while simultaneously fingering her other hole."
#         $ the_person.change_arousal(20)#90 + 8
#         if the_person.arousal > 120:
#             the_person "OH! It's so good... fuck I'm gonna cum again!!!"
#             "You get the now familiar feeling of [the_person.title] cumming around your cock, but this time you can also feel the waves around your finger."
#             "You wonder what it would feel like to make her cum again, but with your cock in her ass instead..."
#             menu:
#                 "Stay Vaginal":
#                     "As [the_person.title]'s pussy quivers around you, you decide to just keep doing what you are doing."
#                 "Fuck Her Ass" if the_person.effective_sluttiness() >= 80:
#                     "You pull out of her pussy. Her juices leave a strand attached to you, connecting you to her cunt."
#                     the_person "Mmm, [the_person.mc_title]? Why did you pull out... OH!"
#                     "Her question is swiftly answered when she feels your manhood poking her puckered hole."
#                     if the_person.effective_sluttiness() > 100:
#                         the_person "Yes! Fuck my ass good!"
#                     else:
#                         the_person "Oh my... be careful!"
#                     "With your hands firmly on her hips, you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
#                     the_person "Oh god you make me feel so dirty... I love it!"
#                     "You fuck her hard but at a steady, even pace."
#                     "[the_person.possessive_title] moans, matching each hip movement of yours with movement of her own."
#                     the_person "It feels so deep... I can't... my legs!"
#                     "Her knees give out, but you are too close to stop fucking her. You grab her hips roughly and pick up the pace."
#                     $ the_person.change_arousal(20)#110 + 8
#                     "Her ass begins to spasm. Her buttery smooth back passage squeezes you over and over as her body is racked with yet another orgasm. It feels incredible."
#                     $ the_person.change_slut(2)
#                     $ the_person.change_happiness(5)
#                     mc.name "Get ready, I'm gonna cum!"
#                     "[the_person.title] is incoherent, and doesn't process your words."
#                     "You plunge deep into her ass and hold it there while you cum. She gasps in time with each new shot of hot semen inside of her."
#                     $ the_person.cum_in_ass()
#                     "You stand there for a minute, holding her hips in the air, you dick buried in her bowel as it softens. Eventually she speaks up."
#                     the_person "Wow... okay... I think I can stand now..."
#                     "You slowly let her down. Her legs buckle for a second, but she catches herself."
#                     "You see a faint trace of your semen running down the back of her leg."
#                     the_person "That was SO good. You'll be hearing from me again, I'm sure... I came so many times..."
#                     "You and [the_person.title] get cleaned up and dressed, then sneak out of the locker room."
#                     return
#                 "Fuck Her Ass\n{color=#ff0000}{size=18}Requires 80 sluttiness{/size}{/color} (disabled)" if the_person.effective_sluttiness() < 80:
#                     pass
#     "[the_person.possessive_title]'s creamy cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
#     mc.name "Get ready, I'm gonna cum!"
#     $ the_person.change_arousal(35)
#     if the_person.effective_sluttiness() > 90:
#         "To your surprise [the_person.title] reaches back with both hands and grabs your hips, pulling you deep inside of her."
#         "Her grip is startlingly strong. You don't think you could pull out even if you wanted to!"
#         the_person "That's it, cum with me!"
#         "You cum erupts in a torrent. You seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
#         $ the_person.change_happiness(5)
#         $ the_person.change_slut(1)
#         $ the_person.cum_in_vagina()
#         "You wait until your orgasm has passed completely, then pull out and stand back. You cum leaks from her well used pussy."
#         "You take a moment to recover. Then you and [the_person.title] get cleaned up and dress. You quietly sneak out of the locker room."
#         return
#     elif the_person.effective_sluttiness() > 60:
#         the_person "Oh god... you should probably pull out but... it feels so good..."
#         "You briefly consider pulling out."
#         menu:
#             "Pull Out":
#                 "You pull out of [the_person.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
#                 the_person "Oh! It's so hot on my skin!"
#                 $ the_person.cum_on_ass()
#                 $ the_person.draw_person(position = "standing_doggy")
#                 "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
#                 "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the locker room."
#                 return
#             "Creampie":
#                 "Her pussy feels too good. You bottom out and cum, dumping wave after wave of your semen deep inside of her."
#                 "You seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
#                 $ the_person.change_happiness(5)
#                 $ the_person.change_slut(1)
#                 $ the_person.cum_in_vagina()
#                 "You wait until your orgasm has passed completely, then pull out and stand back. You cum leaks from her well used pussy."
#                 "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the locker room."
#                 return
#     else:
#         "[the_person.title] suddenly moves her hips forward, your cock slides out of her."
#         the_person "Cum on my ass!"
#         "You stroke your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
#         $ the_person.cum_on_ass()
#         $ the_person.draw_person(position = "standing_doggy")
#         "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
#         "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the locker room."
#     return
#
# #label athlete_cum_face(the_person):
# #    if the_person.obedience > 130:
# #        if the_person.effective_sluttiness() > 60:
# #            the_person "Do I look cute covered in your cum, [the_person.mc_title]?"
# #            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
# #        else:
# #            the_person "I hope this means I did a good job."
# #            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
# #    else:
# #        if the_person.effective_sluttiness() > 80:
# #            the_person "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
# #        else:
# #            the_person "Fuck me, you really pumped it out, didn't you?"
# #            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
# #    return
#
# label athlete_cum_mouth(the_person):
#     if mc.location == gym or the_person.has_cum_fetish():
#         if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("drinking cum") > 1:
#             the_person "Your cum tastes great [the_person.mc_title]! Thanks for giving me so much extra protein!"
#             "[the_person.possessive_title] winks at you as she swallows your load."
#         elif the_person.effective_sluttiness() > 50 or the_person.get_opinion_score("drinking cum") > 0:
#             the_person "Thanks [the_person.mc_title]. I could really use the extra protein after that workout!"
#         else:
#             "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
#             the_person "Thank you [the_person.mc_title]. It doesn't taste the best, but I could always use a little extra protein."
#     elif the_person.obedience > 130:
#         if the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
#             the_person "That was very nice [the_person.mc_title], thank you."
#         else:
#             "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
#             the_person "Thank you [the_person.mc_title], I hope you had a good time."
#     else:
#         if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 0:
#             the_person "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
#             "[the_person.title] licks her lips and sighs happily."
#         else:
#             the_person "Bleh, I don't know if I'll ever get used to that."
#     return
#
# #label athlete_surprised_exclaim(the_person):
# #    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
# #    the_person "[rando]"
# #    return
#
# label athlete_talk_busy(the_person):
#     if mc.location == gym:
#         the_person "Hey, I'm really sorry but I need to keep my workout going. Maybe another time?"
#     if the_person.obedience > 120:
#         the_person "Hey, I'm really sorry but I've got some stuff I need to take care of. Could we catch up some other time?"
#     else:
#         the_person "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
#     return
#
# #label athlete_sex_strip(the_person):
# #    if the_person.effective_sluttiness() < 20:
# #        if the_person.arousal < 50:
# #            the_person "Let me get this out of the way..."
# #        else:
# #            the_person "Let me get this out of the way for you..."
# #
# #    elif the_person.effective_sluttiness() < 60:
# #        if the_person.arousal < 50:
# #            the_person "This is just getting in the way..."
# #        else:
# #            the_person "Ah... I need to get this off."
# #
# #    else:
# #        if the_person.arousal < 50:
# #            the_person "Let me get this worthless thing off..."
# #        else:
# #            the_person "Oh god, I need all of this off so badly!"
#
# #    return
#
# label athlete_sex_watch(the_person, the_sex_person, the_position):
#     if the_person.effective_sluttiness() < the_position.slut_requirement - 20:
#         $ the_person.draw_person(emotion = "angry")
#         the_person "Holy shit, are you really doing this in front of everyone?"
#         $ the_person.change_obedience(-2)
#         $ the_person.change_happiness(-1)
#         "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_requirement - 10:
#         $ the_person.draw_person()
#         $ the_person.change_happiness(-1)
#         "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_requirement:
#         $ the_person.draw_person()
#         the_person "Oh my god, you two are just... Wow..."
#         $ change_report = the_person.change_slut(1)
#         "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() > the_position.slut_requirement and the_person.effective_sluttiness() < the_position.slut_cap:
#         $ the_person.draw_person()
#         the_person "Oh my god that's... Wow that looks...Hot."
#         $ change_report = the_person.change_slut(2)
#         "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."
#
#     else:
#         $ the_person.draw_person(emotion = "happy")
#         the_person "Come on [the_person.mc_title], you can give her a little more than that. I'm sure she can handle it."
#         "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
#
#     return
#
# label athlete_being_watched(the_person, the_watcher, the_position):
#     if the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #They agree you should give it to her harder
#         the_person "I can handle it [the_person.mc_title], you can be rough with me."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's super slutty and doesn't care what people think.
#         the_person "Don't listen to [the_watcher.name], I'm having a great time. Look, she can't stop peeking over."
#
#     elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #She's super slutty and encourages the watcher to be slutty.
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #She's into it and encouraged by the slut watching her.
#         the_person "Oh god, having you watch us like this..."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's into it but shamed by the prude watching her.
#         the_person "[the_person.mc_title], maybe we shouldn't be doing this here..."
#         $ the_person.change_arousal(-1)
#         $ the_person.change_slut(-1)
#         "[the_person.title] seems uncomfortable with [the_watcher.name] nearby."
#
#     else: #the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #They're both into it but not fanatical about it.
#         the_person "Oh my god, having you watch us do this feels so dirty. I think I like it!"
#         $ the_person.change_arousal(1)
#         $ the_person.change_slut(1)
#         "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.name] around."
#
#     return
#
# label athlete_work_enter_greeting(the_person):
#     if the_person.happiness < 80:
#         if the_person.obedience > 120:
#             "[the_person.title] gives you a curt nod and then turns back to what she was doing."
#         else:
#             "[the_person.title] glances at you when you enters the room then looks away quickly to avoid starting a conversation."
#
#     elif the_person.happiness > 120:
#         if the_person.effective_sluttiness() > 50:
#             "[the_person.title] looks up from her work when you enter the room."
#             the_person "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
#             "She smiles and winks, then turns back to what she was doing."
#         else:
#             "[the_person.title] turns to you when you enter the room and shoots you a smile."
#             the_person "Hey, good to see you!"
#
#     else:
#         if the_person.obedience < 90:
#             "[the_person.title] glances up from her work."
#             the_person "Hey, how's it going?"
#         else:
#             "[the_person.title] waves at you as you enter the room."
#             the_person "Hey, let me know if you need anything [the_person.mc_title]."
#     return
#
# label athlete_date_seduction(the_person):
#     if the_person.effective_sluttiness() > the_person.love:
#         if the_person.effective_sluttiness() > 40:
#             the_person "I had a great time [the_person.mc_title], but I can think of a few more things we could do together. Want to come back to my place?"
#             # the_person "I had a great night [the_person.mc_title], would you like to come back to my place and let me repay the favour?"
#         else:
#             the_person "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
#             #the_person "I had a great night [the_person.mc_title], but I don't see why it should end here. If you want to come back to my place I can think of a few things we could do."
#     else:
#         if the_person.love > 40:
#             the_person "You're such great company [the_person.mc_title]. Would you like to come back to my place and spend some more time together?"
#         else:
#             the_person "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
#     return
#
# ## Role Specific Section ##
# label athlete_improved_serum_unlock(the_person):
#     mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
#     the_person "Okay, how can I help?"
#     mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
#     "[the_person.title] smiles mischievously."
#     the_person "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is necessary if we want to see rapid results."
#     mc.name "Go on, I'm interested."
#     the_person "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
#     the_person "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
#     return
#
# #</editor-fold>
