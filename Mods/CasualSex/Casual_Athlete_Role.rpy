#************* Casual Sex Role: College Athlete  *******************
#Outline
#-College Athlete
 # Looking for casual sex while she focuses on her school and athletic program
# Tends to hang out at the Gym
#  First event: She invites you to work out with her. You work up a sweat together, then sneak into a changing room for sex
#  Second event: She invites you to compete with her in distance race (10k? something similar). Makes a wager if you win she'll let you "do what you want" with her
#  Event Requirements: Advances with sluttiness and player stamina. Stamina takes the place of physical fitness during this storyline
#  Girl requirements: Age <25, skinny body type.
#  Other notes: She calls it off if she "catches feels" (love > 50). Will start warning player at > 40 love

init -2 python:
    def casual_athlete_get_to_know_requirement(the_person):
        return True

    def casual_athlete_phase_one_requirement(the_person):
        if the_person.event_triggers_dict.get("athlete_progress", 0) < 1:
            return False
        if the_person.love > 50:
            return "She is uneasy about falling for you."
        if the_person.event_triggers_dict.get("athlete_workout", 0) < 1:
            return False
        if time_of_day < 4:
            if mc.max_stamina > 2:
                if the_person.sluttiness < 20:
                    return "Requires 20 Sluttiness"
                elif mc.location == gym:
                    return True
                else:
                    return "Not at the gym"
            else:
                return "Requires More Max Stamina"
        return False

    def casual_athlete_phase_two_requirement(the_person):
        if the_person.event_triggers_dict.get("athlete_progress", 0) < 2:
            return False
        if the_person.love > 50:
            return "She is uneasy about falling for you."
        if time_of_day < 4:
            if mc.max_stamina > 4:
                if the_person.sluttiness < 40:
                    return "Requires 40 Sluttiness"
                return True
            else:
                return "Requires More Max Stamina"
        return False

    def casual_athlete_buy_protein_shake_requirement(the_person):
        if the_person.event_triggers_dict.get("athlete_protein", 0) < 1:
            return False
        if mc.location == gym:
            return True
        else:
            return "You need to be at the Gym"


#*************Create Casual Athlete Role***********#
init -1 python:
    casual_athlete_get_to_know = Action("Get to know Her", casual_athlete_get_to_know_requirement, "casual_athlete_get_to_know_label",
        menu_tooltip = "Make an observation about her.")
    casual_athlete_phase_one = Action("Workout Together", casual_athlete_phase_one_requirement, "casual_athlete_phase_one_label",
        menu_tooltip = "Work up a sweat.")
    casual_athlete_phase_two = Action("Challenge to Race", casual_athlete_phase_two_requirement, "casual_athlete_phase_two_label",
        menu_tooltip = "No risk, no reward.")
    casual_athlete_role = Role(role_name ="College Athlete", actions =[casual_athlete_get_to_know , casual_athlete_phase_one, casual_athlete_phase_two])


#*************TODO*****************
#Implement some method of adding this role to random towngirls.



###DEBUG TESTING FUNCTIONS###
label casual_athlete_debug(the_person):
    "attempting to add role to [the_person.title]."
    $ the_person.special_role.append(casual_athlete_role)
    "role added to [the_person.title]."
    return


###Athlete ACTION LABELS###
label casual_athlete_get_to_know_label(the_person):
    if "athlete_progress" not in the_person.event_triggers_dict:
        $ the_person.event_triggers_dict["athlete_progress"] = 0
    if the_person.event_triggers_dict.get("athlete_progress", 0) < 1:
        "You look up and down [the_person.title]. You can tell she takes care of herself."
        mc.name "You seem like you like to work out."
        the_person.char "Yeah! You could say that. I'm actually on the state college track and field team!"
        "You aren't surprised, she certainly has the look of an athlete."
        "You talk with her for a while about sports. She has a healthy interest in just about all things physical."
        the_person.char "Well, I need to get going. It was nice talking with you, [the_person.mc_title]!"
        $ the_person.event_triggers_dict["athlete_progress"] = 1
    elif the_person.event_triggers_dict.get("athlete_progress", 0) == 1:
        "You decide to ask [the_person.title] a bit more about her athletics."
        mc.name "I see you here a lot. Are you getting ready for a race?"
        the_person.char "Yeah! I'm getting ready for a big race soon, so I try to get in here before and after class each day."
        "Wow, going to college, and dedicated to sports. Sounds like she doesn't have much free time."
        mc.name "So, where does that leave you? Any time leftover for a social life? Or a boyfriend?"
        the_person.char "Oh, with everything going on, there is no way I would have time for a boyfriend."
        "[the_person.title] starts to move to the next workout machine."
        the_person.char "So a relationship is not really an option for me right now, or a job for that matter."
        mc.name "Yeah, sounds like an intense schedule."
        if the_person.event_triggers_dict.get("athlete_protein", 0) < 1:
            the_person.char "It'd be nice to have a little extra money for some protein powder or something. Money is pretty tight!"
            "You think about it for a bit. You could offer to buy her a protein shake, they serve them here at the gym. That would be a good opportunity to slip some serum in..."
            mc.name "They have protein shakes here. Maybe I could grab you one? It'd be no trouble."
            #Charisma role to unlock the buy protein shake option#
            $ random_roll = renpy.random.randint(0,100)
            $ random_roll += (mc.charisma * 10)
            if random_roll > 50:   #Base line 50:50 chance at charisma = 0. 100% chance at charisma = 5
                the_person.char "That... actually would be nice! You have to be careful with guys, but you seem genuine enough."
                "You now have the option to buy [the_person.title] a protein shake at the gym."
                $ the_person.event_triggers_dict["athlete_protein"] = 1
            else:
                "[the_person.title] hesitates when you offer."
                the_person.char "I appreciate it, but I'll have to pass. It wouldn't feel right to take freebies like that..."
        else:
            the_person.char "I appreciate you buying me a protein shake now and then. I definitely feel the effects of them. I feel stronger... even sexier since you started doing that!"
        "[the_person.title] moves on to the free weights area of the gym."
        if mc.max_stamina > 4:
            the_person.char "I think I'm going to do some squats..."
            "[the_person.title] looks over at you. She gives you a quick appraisal."
            the_person.char "Hey, you look like you're fairly fit yourself. You should workout with me sometime."
            mc.name "That sounds like a good idea, actually."
            the_person.char "Yeah... you're kinda cute. It'd be nice to have a guy around for a bit. It's been a while since I uhh..."
            "You raise your eyebrow"
            the_person.char "I mean uhh, with school and track, I'm so busy. It'd be nice to spend some time in the company of the opposite sex for a while! Nothing wrong with that, right?"
            $ the_person.event_triggers_dict["athlete_workout"] = 1
            "You should consider working out with [the_person.title] sometime. It sounds like she might appreciate some male company!"
        else:
            the_person.char "I think I'm going to do some squats..."
            "[the_person.title] looks over at you. She gives you a quick appraisal."
            the_person.char "Hey, have you ever thought about working out a bit more? It does wonders for your stamina..."
            "You consider her statement for a moment."
            the_person.char "Anyway, I'm going to get back to my workout. I'll see you around [the_person.title]!"
            "If you want to get further with her, maybe you should work on increasing your stamina!"
    elif the_person.event_triggers_dict.get("athlete_progress", 0) == 2:
        "TODO: she talks to you about the upcoming marathon"

    elif the_person.event_triggers_dict.get("athlete_progress", 0) == 3:
        "TODO: she hints you should swing by her place for casual sex soon"

    else:
        "Debug: How did you end up here???"


    return

#CSA10
label casual_athlete_phase_one_label(the_person):
    if the_person.event_triggers_dict.get("athlete_progress", 0) == 1:
        mc.name "Hey [the_person.title]. I figured I would find you here. Want to workout together?"
        "[the_person.title] is just hopping off the treadmill. You can tell she just finished getting warmed up."
        the_person.char "[the_person.mc_title]! Hey, I was wondering if you would take me up on my offer to workout sometime. That sounds great! I'm going to be doing free weights today."
        mc.name "Sounds good! I'll head to the locker room and get changed and meet you over by the free weights."
        "You quickly get yourself changed into workout clothes and meet [the_person.title]."
        the_person.char "This will be perfect! Today is strength day and with you around to spot me I can really push myself to the limit."
        $ the_person.draw_person( position = "stand4")
        "You begin a workout with [the_person.title]. You start it out with some basic free lifting, taking turns on the equipment. She strikes up a conversation as your work out."
        the_person.char "Alright, time for some curls. Thanks again for doing this. It's been nice having a guy around... a lot of times when I do workouts over here I have a lot of guys hitting on me..."
        "You nod in understanding."
        mc.name "Well, I can't say I blame them, you train hard, and it shows with how good your body looks!"
        "She chuckles."
        the_person.char "Thanks. Honestly, its not that I don't like the attention, but with everything going on with me right now, I just don't have time for a relationship."
        the_person.char "You've been a good friend though. It's nice having a guy be just a friend."
        "You finish up your curls with [the_person.title]. You move on to the pull up bar."
        $ the_person.draw_person( position = "stand3")
        "You start to do a few pullups."
        mc.name "So, I get that you don't have time for a relationship but... how do you deal with your, you know, needs?"
        the_person.char "Well, I used to have a few friends from class that came with, well, benefits I guess you could say."
        "You grunt as you exert yourself as you finish your set."
        the_person.char "The last few I've had have kind of fizzled though. The last one started getting too attached, wanting to move in with me, and the one before that graduated and moved out of state."
        the_person.char "So, I guess you could say I'm going through a bit of a dry spell right now."
        "You let go of the pull up bar and she steps up to it."
        the_person.char "Hey, could you do me a favor? Could you pull me down a little bit while I do my reps, you know, to give a little resistance?"
        mc.name "Sure, I can do that."
        "[the_person.title] reaches up and grabs the pull up bar. You put your hands on her hips and lightly push down, giving her some extra weight for her pullups."
        "As she begins to pull herself up, her hips, waist, and ass are in perfect position, right in front of your face. You check her out while she struggles through her reps."
        "[the_person.title]'s tight, thin body is undeniably sexy and athletic. Your hands on her hips gives you a naughty idea."
        mc.name "I stay busy with my business. I know that feeling, not having time for a relationship, but looking for some casual hookups."
        "[the_person.title] drops down off of the pull up bar. You let your hands linger on her hips a little longer than necessary."
        the_person.char "Exactly! Why can't two adults just have casual sex once in a while?"
        mc.name "Friends with benefits can be great for meeting needs during busy times in your life. I'm looking for something like that right now too."
        "[the_person.title] looks up at you when you finish your sentence. It quickly dawns on her that you are suggesting hooking up."
        the_person.char "Let's keep going, next up are squats."
        $ the_person.draw_person( position = "stand2")
        "[the_person.title] helps you add some weights to the squat bar. You decide to get a little braver."
        mc.name "Add one more weight to the end there, I want to really push myself today."
        "She does as you ask, and you get in position under the bar."
        mc.name "Stay close, I've never done this much weight before."
        "As you get in position, you feel [the_person.title] get in position behind you to spot you. You can feel her a little closer than she needs to be though."
        "With a grunt, you begin your reps. The weight is tough, but you get through your reps without help. When you finish you slowly stand up and turn to her."
        $ the_person.draw_person( position = "stand4")
        if the_person.outfit.tits_available():
            "[the_person.title] has a little extra color in her cheeks than she did a minute ago. You also notice her nipples are a little more prominent."
        else:
            "[the_person.title] has a little extra color in her cheeks than she did a minute ago and it looks like her nipples are poking out a little bit, against the fabric containing them."
        "She must be getting a little bit excited!"
        mc.name "Alright, your turn."
        "You help her reset the weights to something appropriate for her. She gets in position and gets ready to do some squats, and you get behind her, ready to spot for her."
        "As she begins her reps, you get a little bit closer to her. As she stands up with each squat, her lower back starts to brush up against your crotch."
        mc.name "See? Two friends, helping each other out. I take a turn, then you take a turn..."
        "[the_person.title] grunts... or was that a groan? You lean forward just a bit farther. It is now obvious you are using the opportunity to put your body up against hers as she finishes her squats."
        "At the top of her last squat, she lingers a bit before she racks the weight. You feel an ever so slight wiggle of her hips up against you. She's getting turned on!"
        "She racks her weights with a groan, and you quickly retreat. Getting an erection here would be a bit embarassing"
        the_person.char "Okay... let finish with the bench press."
        "You head over to the bench and start racking some weights on it. You lay down on the bench while [the_person.title] stands by your head."
        "She looks around a bit to see if anybody is watching you before prompting you to begin."
        the_person.char "Ready? Its my turn now..."
        "As you lift the weight up over the bar and begin to bring it down to your chest, [the_person.title] slowly moves forward, maneuvering her legs until her crotch is right above your face."
        "You breathe deep. There is the normal gym smells of weights, rubber, and sweat, but also a smell that is distinctly, sweetly feminine."
        "You lift your head up for a second, making contact with her crotch with your face. She stifles a groan as you finish up your set."
        $ the_person.change_arousal(20)
        "[the_person.title] backs off and you quickly get up. She puts a hand on your shoulder and whispers in your ear."
        the_person.char "There's a lockerroom here families can use with a lock on it. Meet me there in three minutes."
        $ the_person.draw_person( position = "walking_away")
        "You watch [the_person.title] walk off, fighting off an erection. Looks like you're about to hookup at the gym!"
        "After three minutes, you follow after [the_person.title]. When you find the family use room, you let yourself in."
        $ CS_nude_outfit = Outfit("Nude")
        $ the_person.outfit = CS_nude_outfit.get_copy()
        $ the_person.draw_person( position = "stand2")
        "As you enter, you see that [the_person.title] is already naked."
        the_person.char "[the_person.mc_title], we can work out the details later... I have been fucked in months!"
        "You walk over to her and quickly strip. You grab [the_person.title] by that ass and pick her up. You carry her to the wall and pin her up against it."
        $ the_person.draw_person( position = "against_wall")
        "[the_person.possessive_title] is grinding her hips up against yours. The sweat from your workouts mingles together as you prepare yourself to enter her."

        ###TODO new version figure out condom stuff here###

        ###TODO situational sluttiness to make sure this position succeeds###

        "As you begin to push yourself inside her, she drags her nails across your back."
        the_person.char "Oh fuck, that's good. Give it to me good, [the_person.mc_title]!"
        call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, girl_in_charge = False, private = True) from _call_casual_sex_mod_CS010

        $ the_person.event_triggers_dict["athlete_progress"] = 2
    elif the_person.event_triggers_dict.get("athlete_progress", 0) == 2:
        "Workout together again, already did this once."
    return

label casual_athlete_phase_two_label(the_person):
    if the_person.event_triggers_dict.get("athlete_progress", 0) == 2:
        "You race her, win, and have sexy times"
        $ the_person.event_triggers_dict["athlete_progress"] = 3
    elif the_person.event_triggers_dict.get("athlete_progress", 0) > 2:
        "You already beat her once!"

    return

label casual_athlete_buy_protein_shake_label(the_person):
    mc.name "Hey [the_person.name], I see you're working pretty hard today! Can I get you a protein shake?"
    "[the_person.possessive_title] looks at you and smiles."
    the_person.char "That sounds great!"
    $ renpy.scene("Active")
    "You head over to the counter where they have the supplements. You order her a protein shake."
    "Before you take it back to her, you have a moment with no one around. You can add a serum to it if you do it quickly!"
    menu:
        "Add a dose of serum to [the_person.title]'s shake.":
            call give_serum(the_person) from _call_give_serum_casual_athlete
            $ the_person.draw_person(emotion = "happy")
            "You mix the serum into [the_person.title]'s protein shake. You take it over to her."
            the_person.char "Thanks [the_person.mc_title]."
            mc.name "No problem at all."
            $ renpy.scene("Active")


        "Leave her drink alone.":
            "You decide not to test a dose of serum out on [the_person.title] and take the shake back to her."
            $ the_person.draw_person(emotion = "happy")
            the_person.char "Thanks [the_person.mc_title]."
            mc.name "No problem at all."
            $ renpy.scene("Active")

    return


#************* Personality****************#
#Override some of her personality functions so that her conversation options makes sense.

init 1301 python:              #Because Vren Init personality functionns at 1300



    def athlete_titles(the_person):
        valid_titles = []
        valid_titles.append(the_person.name)
        if the_person.sluttiness > 20:
            valid_titles.append("Cardio Bunny")
        return valid_titles

    def athlete_possessive_titles(the_person):
        valid_possessive_titles = ["Your gym girl",the_person.title]

        if the_person.sluttiness > 60:
            valid_possessive_titles.append("Your gym slut")

        if the_person.sluttiness > 100:
            valid_possessive_titles.append("The gym cumdump")
            valid_possessive_titles.append("The gym bicycle")
        return valid_possessive_titles
    def athlete_player_titles(the_person):
        return mc.name
    athlete_personality = Personality("athlete", default_prefix = "wild",
    common_likes = [],
    common_sexy_likes = ["casual sex"],
    common_dislikes = ["relationships"],
    common_sexy_dislikes = [],
    titles_function = athlete_titles, possessive_titles_function = athlete_possessive_titles, player_titles_function = athlete_player_titles)

#************* Personality labels***************#


label athlete_greetings(the_person):
    if mc.location == gym:
        if the_person.love > 50:  #She loves you too much and is going to or already has called things off
            the_person.char "Oh... hello [the_person.mc_title]"
            return
        if the_person.event_triggers_dict.get("athlete_progress", 0) >= 2:
            the_person.char "Hey there [the_person.mc_title]"
            "You see [the_person.title] here at the Gym, in her usual spot on the treadmill."
            the_person.char "You want to join me for another workout? I always leave the gym feeling so satisfied when we work out together!"
        else:
            the_person.char "Hey there!"

    elif the_person.sluttiness > 60:
        if the_person.obedience > 130:
            the_person.char "Hello [the_person.mc_title], it's good to see you."
        else:
            the_person.char "Hey there handsome, feeling good?"
    else:
        if the_person.obedience > 130:
            the_person.char "Hello [the_person.mc_title]."
        else:
            the_person.char "Hey there!"
    return

label athlete_sex_responses(the_person):
    if the_person.sluttiness > 50:
        if the_person.obedience > 130:
            the_person.char "Oh my, keep doing that please!"
        else:
            the_person.char "Fuck it feels good when you do that. Keep going!"
    else:
        "[the_person.title] closes her eyes and moans quietly to herself."
    return

label athlete_climax_responses(the_person):
    if the_person.sluttiness > 70:
        the_person.char "I'm going to cum! Ah! Make me cum [the_person.mc_title], I want to cum so badly! Ah!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Ah! I'm cumming! Oh fuck! Ah!"
    the_person.char "Fuck this feels better than winning a marathon!"
    return

label athlete_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
    else:
        the_person.char "Thanks [the_person.mc_title]! I wonder if I could wear this at the gym."
    return

#label athlete_clothing_reject(the_person):
#    if the_person.obedience > 130:
#        the_person.char "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
#    else:
#        if the_person.sluttiness > 60:
#            the_person.char "Wow. I'm usually up for anything but I think that's going too far."
#        else:
#            the_person.char "Wow. It's a little... skimpy. I don't think I could wear that."
#    return

label athlete_clothing_review(the_person):
    if mc.location == gym:
        if the_person.sluttiness > 40:
            the_person.char "I love when you look at me like that, but I don't think the gym staff would appreciate it as much. I'd better clean up a bit."
        else:
            the_person.char "I'd better clean up some before I go to leave the gym..."
    elif the_person.obedience > 130:
        the_person.char "I'm sorry [the_person.mc_title], you shouldn't have to see me like this. I'll go and get cleaned up so I'm presentable again."
    else:
        if the_person.sluttiness > 40:
            the_person.char "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
        else:
            the_person.char "My clothes are a mess! I'll be back in a moment, I'm going to go get cleaned up."
    return

#label athlete_strip_reject(the_person):
#    if the_person.obedience > 130:
#        the_person.char "I'm sorry, but can we leave that where it is for now?"
#    elif the_person.obedience < 70:
#        the_person.char "Slow down there, I'll decide when that comes off."
#    else:
#        the_person.char "I think that should stay where it is for now."
#    return

label athlete_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person.char "I was just about to suggest the same thing."
        else:
            the_person.char "Mmm, you have a dirty mind [the_person.mc_title], I like it."
    else:
        the_person.char "Okay, we can give that a try."
    return

label athlete_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god [the_person.mc_title], I should really say no... But you always make me feel so good, I can't say no to you."
    else:
        if the_person.obedience > 130:
            the_person.char "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
        else:
            the_person.char "I... Okay, if you really want to, lets give it a try."
    return

label athlete_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
    else:
        the_person.char "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
    return

label athlete_sex_angry_reject(the_person):
    if the_person.sluttiness < 20:
        the_person.char "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person.char "Ugh! Get away from me, I don't even want to talk to you after that."
    else:
        the_person.char "What the fuck do you think you're doing, that's disgusting!"
        the_person.char "Get the fuck away from me, I don't even want to talk to you after that!"
    return

label athlete_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Yes [the_person.mc_title]? Do you need help relieving some stress?"
        else:
            the_person.char "Yes [the_person.mc_title]? Is there something I can help you with?"
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I know that look. Do you want to fool around a little?"
        elif the_person.sluttiness > 10:
            the_person.char "Oh, do you see something you like?"
        else:
            the_person.char "Oh, I don't really know what to say [the_person.mc_title]..."
    return

label athlete_seduction_accept_crowded(the_person):
    if mc.location == gym:
        if the_person.sluttiness < 20:
            the_person.char "I suppose we could sneak away into the locker room... There's nothing wrong with that, right?"
        elif the_person.sluttiness < 70:
            the_person.char "Come on, let's sneak into the locker room and do it!"
        else:
            the_person.char "Oh fuck that sounds nice. I'm not sure I can wait until we sneak into the locker room, maybe we should just do it right here!"
        return

    if the_person.sluttiness < 20:
        the_person.char "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
    elif the_person.sluttiness < 50:
        the_person.char "Come on, let's go find someplace quiet where we won't be interupted."
    else:
        the_person.char "No point waisting any time then, right? Let's get to it!"
    return

label athlete_seduction_accept_alone(the_person):
    if mc.location == gym:
        if the_person.sluttiness < 20:
            the_person.char "Well, there's nobody around to see us..."
        elif the_person.sluttiness < 50:
            the_person.char "I can't believe how empty the gym is right now. Let's do it right here!"
        else:
            the_person.char "Oh [the_person.mc_title], the gym is empty, fuck me now!"
        return
    if the_person.sluttiness < 20:
        the_person.char "Well, there's nobody around to stop us..."
    elif the_person.sluttiness < 50:
        the_person.char "Mmm, that's a fun idea. Come on, let's get to it!"
    else:
        the_person.char "Oh [the_person.mc_title], don't make me wait!"
    return

#label athlete_seduction_refuse(the_person):
#    if the_person.sluttiness < 20:
#        "[the_person.title] blushes and looks away from you awkwardly."
#        the_person.char "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."
#
#    elif the_person.sluttiness < 50:
#        the_person.char "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
#        "[the_person.title] smiles and gives you a wink."
#
#    else:
#        the_person.char "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
#    return

label athlete_flirt_response(the_person):
    if mc.location == gym:
        if the_person.love > 50:  #She loves you too much and is going to or already has called things off
            the_person.char "Didn't your mother ever tell you its rude to hit on girls at the gym?"
            return
        if the_person.event_triggers_dict.get("athlete_progress", 0) >= 2:
            the_person.char "Well why don't you workout with me for a bit and we can work up a sweat together?"
        else:
            the_person.char "Hey, maybe if you workout with me first."
            "[the_person.title] gives you a wink and smiles."
        return

    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "If that's what you want I'm sure I could help with that [the_person.mc_title]."
        else:
            the_person.char "Thank you for the compliment, [the_person.mc_title]."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peak."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person.char "Hey, maybe if you buy me dinner first."
            "[the_person.title] gives you a wink and smiles."
    return

#label athlete_cum_face(the_person):
#    if the_person.obedience > 130:
#        if the_person.sluttiness > 60:
#            the_person.char "Do I look cute covered in your cum, [the_person.mc_title]?"
#            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
#        else:
#            the_person.char "I hope this means I did a good job."
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    else:
#        if the_person.sluttiness > 80:
#            the_person.char "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
#        else:
#            the_person.char "Fuck me, you really pumped it out, didn't you?"
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    return

label athlete_cum_mouth(the_person):
    if mc.location == gym:
        if the_person.sluttiness > 80:
            the_person.char "Your cum tastes great [the_person.mc_title]! Thanks for giving me so much extra protein!"
            "[the_person.possessive_title] winks at you as she swallows your load."
        elif the_person.sluttiness > 50:
            the_person.char "Thanks [the_person.mc_title]. I could really use the extra protein after that workout!"
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person.char "Thank you [the_person.mc_title]. It doesn't taste the best, but I could always use a little extra protein."
    elif the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person.char "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person.char "Bleh, I don't know if I'll ever get use to that."
    return

#label athlete_suprised_exclaim(the_person):
#    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
#    the_person.char "[rando]"
#    return

label athlete_talk_busy(the_person):
    if mc.location == gym:
        the_person.char "Hey, I'm really sorry but I need to keep my workout going. Maybe another time?"
    if the_person.obedience > 120:
        the_person.char "Hey, I'm really sorry but I've got some stuff I need to take care of. Could we catch up some other time?"
    else:
        the_person.char "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
    return

#label athlete_sex_strip(the_person):
#    if the_person.sluttiness < 20:
#        if the_person.arousal < 50:
#            the_person.char "Let me get this out of the way..."
#        else:
#            the_person.char "Let me get this out of the way for you..."
#
#    elif the_person.sluttiness < 60:
#        if the_person.arousal < 50:
#            the_person.char "This is just getting in the way..."
#        else:
#            the_person.char "Ah... I need to get this off."
#
#    else:
#        if the_person.arousal < 50:
#            the_person.char "Let me get this worthless thing off..."
#        else:
#            the_person.char "Oh god, I need all of this off so badly!"

#    return

label athlete_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Holy shit, are you really doing this in front of everyone?"
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        $ the_person.change_happiness(-1)
        "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "Oh my god, you two are just... Wow..."
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh my god that's... Wow that looks...Hot."
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Come on [the_person.mc_title], you can give her a little more than that. I'm sure she can handle it."
        "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."

    return

label athlete_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verb]ing you with [the_watcher.title] around."

    return

label athlete_work_enter_greeting(the_person):
    if the_person.happiness < 80:
        if the_person.obedience > 120:
            "[the_person.title] gives you a curt nod and then turns back to what she was doing."
        else:
            "[the_person.title] glances at you when you enters the room then looks away quickly to avoid starting a conversation."

    elif the_person.happiness > 120:
        if the_person.sluttiness > 50:
            "[the_person.title] looks up from her work when you enter the room."
            the_person.char "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
            "She smiles and winks, then turns back to what she was doing."
        else:
            "[the_person.title] turns to you when you enter the room and shoots you a smile."
            the_person.char "Hey, good to see you!"

    else:
        if the_person.obedience < 90:
            "[the_person.title] glances up from her work."
            the_person.char "Hey, how's it going?"
        else:
            "[the_person.title] waves at you as you enter the room."
            the_person.char "Hey, let me know if you need anything [the_person.mc_title]."
    return

label athlete_date_seduction(the_person):
    if the_person.sluttiness > the_person.love:
        if the_person.sluttiness > 40:
            the_person.char "I had a great time [the_person.mc_title], but I can think of a few more things we could do together. Want to come back to my place?"
            # the_person.char "I had a great night [the_person.mc_title], would you like to come back to my place and let me repay the favour?"
        else:
            the_person.char "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
            #the_person.char "I had a great night [the_person.mc_title], but I don't see why it should end here. If you want to come back to my place I can think of a few things we could do."
    else:
        if the_person.love > 40:
            the_person.char "You're such great company [the_person.mc_title]. Would you like to come back to my place and spend some more time together?"
        else:
            the_person.char "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
    return

## Role Specific Section ##
label athlete_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] smiles mischievously."
    the_person.char "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is nessesary if we want to see rapid results."
    mc.name "Go on, I'm interested."
    the_person.char "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
    the_person.char "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
    return

#</editor-fold>
