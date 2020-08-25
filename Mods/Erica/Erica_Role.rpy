

init 2 python:
    erica_workout_wardrobe = wardrobe_from_xml("Erica_Workout_Wardrobe")
    def erica_mod_initialization(): #Add actionmod as argument#

        erica_wardrobe = wardrobe_from_xml("Erica_Workout_Wardrobe")
        erica_base_outfit = Outfit("Erica's base accessories")
        the_eye_shadow = heavy_eye_shadow .get_copy()
        the_eye_shadow.colour = [.18, .54, .34, 0.95]
        the_rings = copper_ring_set.get_copy()   #Change this
        copper_ring_set.colour = [.1,.36,.19,1.0]
        erica_base_outfit.add_accessory(the_eye_shadow)
        erica_base_outfit.add_accessory(the_rings)

        # init erica role
        # erica_role = Role(role_name ="erica", actions =[erica_ask_date_classic_concert, erica_ask_about_porn], hidden = True)

        #global erica_role
        #TODO make most variables identical to Stephanie
        global erica
        erica = make_person(name = "Erica", age = 19, body_type = "thin_body", face_style = "Face_14",  tits="B", height = 0.92, hair_colour="barn red", hair_style = windswept_hair, skin="white" , \
            eyes = "light blue", personality = erica_personality, name_color = "#89CFF0", dial_color = "89CFF0" , starting_wardrobe = erica_wardrobe, \
            stat_array = [2,4,4], skill_array = [4,1,3,3,1], sex_array = [3,2,3,2], start_sluttiness = 3, start_obedience = -18, start_happiness = 119, start_love = 0, \
            title = "Erica", possessive_title = "Your gym girl", mc_title = mc.name, relationship = "Single", kids = 0, force_random = True,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", 2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["doggy style sex", 2, False], ["getting head", 1, False], ["being submissive", 1, False], ["anal creampies", -2, False], ["public sex", -2, False]])



        erica.max_energy = 120
        erica.home = erica.generate_home()
        erica.home.add_person(erica)
        erica.set_schedule([1,3], gym)
        erica.set_schedule([2], university)
        # the_person.schedule[1] = gym
        # the_person.schedule[2] = university
        # the_person.schedule[3] = gym
        erica.event_triggers_dict["reject_position"] = "standing_doggy"
        erica.event_triggers_dict["erica_progress"] = 0
        erica.event_triggers_dict["erica_workout"] = 0
        erica.event_triggers_dict["love_path"] = False
        erica.event_triggers_dict["fwb_path"] = False
        erica.event_triggers_dict["hate_path"] = False
        erica.event_triggers_dict["protein_day"] = 9999



        town_relationships.update_relationship(nora, erica, "Friend")
        town_relationships.update_relationship(lily, erica, "Friend")


        erica.add_role(erica_role)
        erica.add_unique_on_room_enter_event(erica_intro_action)

        #REMARKS: Erica has a few instance specific class overrides. This is my first time testing this type of programming, hopefully it works correctly.
        erica.apply_gym_outfit = erica_apply_gym_outfit

        return


init -2 python:

    def erica_apply_gym_outfit(): #No access to self in object specific override
        if erica_workout_wardrobe:
            erica.apply_outfit(workout_wardrobe.decide_on_outfit2(erica).get_copy())
        return

    def erica_intro_requirement(person):
        if person.location() == gym:
            return True
        return False
    def erica_get_to_know_requirement(person):
        if mc.max_energy >= 110:
            if mc.location == gym:
                return True
            else:
                return "Wait until you see her at the gym"
        else:
            return "Requires: 110 maximum energy"

    def erica_phase_one_requirement(person):
        if person.event_triggers_dict.get("erica_progress", 0) < 1:
            return False
        if person.event_triggers_dict.get("erica_workout", 0) < 1:
            return False
        if time_of_day < 4:
            if mc.max_energy >= 120:
                if person.effective_sluttiness() < 20:
                    return "Requires 20 Sluttiness"
                elif mc.location == gym:
                    return True
                else:
                    return "Only at the gym"
            else:
                return "Requires: 120 maximum energy"
        return False

    def erica_phase_two_requirement(person):
        if person.event_triggers_dict.get("erica_progress", 0) < 2:
            return False
            if person.event_triggers_dict.get("erica_progress", 0) > 3:
                return False
        if person.love > 50:
            return "She is uneasy about falling for you"
        if time_of_day < 4:
            if mc.max_energy >= 140:
                if person.effective_sluttiness() < 40:
                    return "Requires: 40 sluttiness"
                return True
            else:
                return "Requires: 140 maximum energy"
        return False

    def erica_race_crisis_requirement():
        if day % 7 == 5:
            if time_of_day == 1:
                return True
        return False

    def erica_buy_protein_shake_requirement(person):
        if person.event_triggers_dict.get("erica_protein", 0) < 1:
            return False
        if mc.location == gym:
            if day > person.event_triggers_dict.get("protein_day", 9999):
                return True
            else:
                return "Once per Day"
        else:
            return "Only at the Gym"

    def erica_house_call_requirement(person):
        if person.event_triggers_dict.get("erica_progress", 0) == 4:
            if mc.location == person.home:
                return True
        return False

    def erica_ghost_requirement():
        if renpy.random.randint(0,100) < 20:
            return True
        return False

    def add_erica_ghost_action(person): #Hopefully delete this soon
        remove_mandatory_crisis_list_action("erica_ghost_label")
        erica_ghost = Action("Casual Athlete Ghosts you", erica_ghost_requirement, "erica_ghost_label", args = person)
        mc.business.mandatory_crises_list.append(erica_ghost)
        return

    def make_bench():
        the_desk = Object("bench",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)
        return the_desk


#*************Create Casual Athlete Role***********#
init -1 python:
    erica_intro_action =Action("Meet Erica", erica_intro_requirement, "erica_intro_label",
        menu_tooltip = "Meet your new gym girl.")
    erica_get_to_know = Action("Get to know Her {image=gui/heart/Time_Advance.png}", erica_get_to_know_requirement, "erica_get_to_know_label",
        menu_tooltip = "Make an observation about her.")
    erica_phase_one = Action("Workout Together {image=gui/heart/Time_Advance.png}", erica_phase_one_requirement, "erica_phase_one_label",
        menu_tooltip = "Work up a sweat.")
    erica_phase_two = Action("Challenge to Race {image=gui/heart/Time_Advance.png}", erica_phase_two_requirement, "erica_phase_two_label",
        menu_tooltip = "No risk, no reward.")
    erica_protein_shake = Action("Buy Protein Shake ($5)", erica_buy_protein_shake_requirement,"erica_buy_protein_shake_label", menu_tooltip = "Slip some serum in.")
    erica_house_call = Action("Take Charge {image=gui/heart/Time_Advance.png}", erica_house_call_requirement, "erica_house_call_label",
        menu_tooltip = "Pick her up.")
    erica_role = Role(role_name ="College Athlete", actions =[erica_get_to_know , erica_phase_one, erica_phase_two, erica_protein_shake, erica_house_call], hidden = True)


#*************Mandatory Crisis******************#
init 1 python:
    def add_erica_race_crisis(person):
        erica_race_crisis.args = [person]
        mc.business.mandatory_crises_list.append(erica_race_crisis)
        return

    erica_race_crisis = Action("Charity Race", erica_race_crisis_requirement, "erica_race_crisis_label")



###Erica ACTION LABELS###
label erica_intro_label(the_person):
    "As you step into the gym, you glance back and forth, checking out some of the different girls."
    "The gym is a great place to get fit... and enjoy some eye candy at the same time."
    "You get ready to hop onto one of the machines, but one girl in particular stands out to you."
    $ the_person.draw_person()
    "Your eyes are drawn to her. It is clear she takes care of herself. Right now she is in between machines."
    "You decide to introduce yourself. You walk over to her and strike up a conversation."
    $ the_person.event_triggers_dict["erica_progress"] = 1
    mc.name "Hey, you are making short work of these machines."
    the_person.char "Yeah, I come here pretty often."
    mc.name "I can tell. Can you show me how to use this machine? I'm kind of new here."
    the_person.char "Sure! It's not too hard, but you need to make sure you set this..."
    $ the_person.draw_person(position = "standing_doggy")
    "You watch as she bends over and starts setting up some of the weights on the machine."
    "Damn she's got a nice ass."
    "You make sure to keep your eyes up when she starts to stand back up. Don't want to get caught ogling her..."
    $ the_person.draw_person()
    the_person.char "There, now it should be good to go!"
    mc.name "Thanks! That is really helpful. I'm [mc.name]."
    the_person.char "[the_person.name]. Nice to meet you."
    $ the_person.set_title(the_person.name)
    $ the_person.set_possessive_title("your gym girl")
    $ the_person.set_mc_title(mc.name)
    mc.name "Likewise. You come here often?"
    the_person.char "Yeah! You could say that. I'm actually on the state college track and field team!"
    "You aren't surprised, she certainly has the look of an athlete."
    "You talk with her for a while about sports. She has a healthy interest in just about all things physical."
    the_person.char "Well, I need to get going. It was nice talking with you, [the_person.mc_title]!"
    "[the_person.title] seems like an interesting person. You should keep an eye out for her at the gym in the future."
    return


label erica_get_to_know_label(the_person):
    if "erica_progress" not in the_person.event_triggers_dict:
        $ the_person.event_triggers_dict["erica_progress"] = 0
        call erica_intro_label(the_person) from _erica_recall_intro_if_skipped_somehow_01
        #Introduction scene#
    elif the_person.event_triggers_dict.get("erica_progress", 0) == 1:
        "You decide to ask [the_person.title] a bit more about her athletics."
        mc.name "I see you here a lot. Are you getting ready for a race?"
        the_person.char "Yeah! I'm getting ready for a big race soon, so I try to get in here before and after class each day."
        "Wow, going to college, and dedicated to sports. Sounds like she doesn't have much free time."
        mc.name "So, where does that leave you? Any time leftover for a social life? Or a boyfriend?"
        the_person.char "Oh, with everything going on, there is no way I would have time for a boyfriend."
        "[the_person.title] starts to move to the next workout machine."
        the_person.char "So a relationship is not really an option for me right now, or a job for that matter."
        mc.name "Yeah, sounds like an intense schedule."
        if the_person.event_triggers_dict.get("erica_protein", 0) < 1:
            the_person.char "It'd be nice to have a little extra money for some protein powder or something. Money is pretty tight!"
            "You think about it for a bit. You could offer to buy her a protein shake, they serve them here at the gym. That would be a good opportunity to slip some serum in..."
            mc.name "They have protein shakes here. Maybe I could grab you one? It'd be no trouble."
            #Charisma role to unlock the buy protein shake option#
            $ ran_num = renpy.random.randint(0,100)
            $ ran_num += (mc.charisma * 10)
            if ran_num > 50:   #Base line 50:50 chance at charisma = 0. 100% chance at charisma = 5
                the_person.char "That... actually would be nice! You have to be careful accepting drinks from strangers, but you seem genuine enough."
                "You now have the option to buy [the_person.title] a protein shake at the gym."
                $ the_person.event_triggers_dict["erica_protein"] = 1
                $ erica.event_triggers_dict["protein_day"] = 0
            else:
                "[the_person.title] hesitates when you offer."
                the_person.char "I appreciate it, but I'll have to pass. It wouldn't feel right to take freebies like that..."
        else:
            the_person.char "I appreciate you buying me a protein shake now and then. I definitely feel the effects of them. I feel stronger... even sexier since you started doing that!"
        "[the_person.title] moves on to the free weights area of the gym."
        if mc.max_energy >= 110:
            the_person.char "I think I'm going to do some squats..."
            "[the_person.title] looks over at you. She gives you a quick appraisal."
            the_person.char "Hey, you look like you're fairly fit yourself. You should workout with me sometime."
            mc.name "That sounds like a good idea, actually."
            the_person.char "Yeah... you're kinda cute. It'd be nice to have a guy around for a bit. It's been a while since I uhh..."
            "You raise your eyebrow"
            the_person.char "I mean uhh, with school and track, I'm so busy. It'd be nice to spend some time in the company of the opposite sex for a while! Nothing wrong with that, right?"
            $ the_person.event_triggers_dict["erica_workout"] = 1
            "You should consider working out with [the_person.title] sometime. It sounds like she might appreciate some male company!"
        else:
            the_person.char "I think I'm going to do some squats..."
            "[the_person.title] looks over at you. She gives you a quick appraisal."
            the_person.char "Hey, have you ever thought about working out a bit more? It does wonders for your energy..."
            "You consider her statement for a moment."
            the_person.char "Anyway, I'm going to get back to my workout. I'll see you around [the_person.title]!"
            "If you want to get further with her, maybe you should work on increasing your energy!"

        #Had sex in the locker room#
    elif the_person.event_triggers_dict.get("erica_progress", 0) == 2:
        "You notice that [the_person.title] is really pushing herself hard today on the treadmill."
        mc.name "Hey [the_person.title]. You're really going at it! Have an event coming up?"
        "[the_person.title] slows the treadmill down so she can carry on a conversation."
        the_person.char "Yeah! I have a big 10k coming up. I really want to do well for this, with it coming up on track season!"
        "You chit chat with [the_person.title] for a bit about the upcoming race."
        if mc.max_energy >= 140:
            the_person.char "Hey, you seem pretty fit too. You should consider entering! It's for a great cause!"
            mc.name "Okay... I'll consider it. Things are pretty busy at work lately, but I'll get back to you if I have time."
            the_person.char "Just don't be sore about it when I beat you to the finish line. I'm a serious athlete!"
            mc.name "Ohhh, I see! Well, maybe we should make it a race! But what would the stakes be?"
            "[the_person.title] chuckles before responding. She gives you a quick wink."
            the_person.char "I'm sure we could come up with something... be careful though, don't bet anything you aren't willing to lose!"
        else:
            the_person.char "Hey, it has been nice chatting with you, but I need to get back to my workout!"
        "You say goodbye and head on your way."

        #You've challenged her to a race!#
    elif the_person.event_triggers_dict.get("erica_progress", 0) == 3:
        "You try to strike up a conversation with [the_person.title]."
        the_person.char "Hey now, no distractions! Your ass is mine on Saturday!"
        mc.name "Ha! We'll see about that!"


        #You've won the race#
    elif the_person.event_triggers_dict.get("erica_progress", 0) == 4:
        mc.name "Hey [the_person.title]."
        the_person.char "Hey. [the_person.mc_title]!"
        "You catch up with her for a bit with what she's been up to."
        the_person.char "Well, it was good to see you. We should work out again sometime, or... you haven't lost my address have you?"
        mc.name "Of course not!"
        the_person.char "Then swing by some evening, it would be good to get a little time working out some tension!"
        "You tell her you'll look her up soon, say goodbye and head on your way."

    else:
        "Debug: How did you end up here???"

    # $ the_person.review_outfit()
    call advance_time from _call_advance_erica_get_to_know
    return

#CSA10
label erica_phase_one_label(the_person):
    if the_person.event_triggers_dict.get("erica_progress", 0) == 1:
        mc.name "Hey [the_person.title]. I figured I would find you here. Want to workout together?"
        "[the_person.title] is just hopping off the treadmill. You can tell she just finished getting warmed up."
        the_person.char "[the_person.mc_title]! Hey, I was wondering if you would take me up on my offer to workout sometime. That sounds great! I'm going to be doing free weights today."
        mc.name "Sounds good! I'll head to the locker room and get changed and meet you over by the free weights."
        "You quickly get yourself changed into workout clothes and meet [the_person.title]."
        the_person.char "This will be perfect! Today is strength day and with you around to spot me I can really push myself to the limit."
        $ the_person.draw_person( position = "stand4")
        "You begin a workout with [the_person.title]. You start it out with some basic free lifting, taking turns on the equipment. She strikes up a conversation as you work out."
        the_person.char "Alright, time for some curls. Thanks again for doing this. It's been nice having a guy around... a lot of times when I do workouts over here I have a lot of guys hitting on me..."
        "You nod in understanding."
        mc.name "Well, I can't say I blame them, you train hard, and it shows with how good your body looks!"
        "She chuckles."
        the_person.char "Thanks. Honestly, it's not that I don't like the attention, but with everything going on with me right now, I just don't have time for a relationship."
        the_person.char "You've been a good friend though."
        "You finish up your curls with [the_person.title]. You move on to the pull up bar."
        $ the_person.draw_person( position = "stand3")
        "You start to do a few pull-ups."
        mc.name "So, I get that you don't have time for a relationship but... how do you deal with your, you know, needs?"
        the_person.char "Well, I used to have a few friends from class that came with, well, benefits I guess you could say."
        "You grunt as you exert yourself as you finish your set."
        the_person.char "The last few I've had have kind of fizzled though. The last one started getting too attached, wanting to move in with me, and the one before that graduated and moved out of state."
        the_person.char "So, I guess you could say I'm going through a bit of a dry spell right now."
        "You let go of the pull up bar and she steps up to it."
        the_person.char "Hey, could you do me a favor? Could you pull me down a little bit while I do my reps, you know, to give a little resistance?"
        mc.name "Sure, I can do that."
        "[the_person.title] reaches up and grabs the pull up bar. You put your hands on her hips and lightly push down, giving her some extra weight for her pull-ups."
        "As she begins to pull herself up, her hips, waist, and ass are in perfect position, right in front of your face. You check her out while she struggles through her reps."
        "[the_person.title]'s tight, thin body is undeniably sexy and athletic. Your hands on her hips gives you a naughty idea."
        mc.name "I stay busy with my business. I know that feeling, not having time for a relationship, but looking for some casual hookups."
        "[the_person.title] drops down off of the pull up bar. You let your hands linger on her hips a little longer than necessary."
        the_person.char "Exactly! Why can't two adults just have casual sex once in a while?"
        mc.name "Friends with benefits can be great for meeting needs during busy times in your life."
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
        "She racks her weights with a groan, and you quickly retreat. Getting an erection here would be a bit embarrassing"
        the_person.char "Okay... let finish with the bench press."
        "You head over to the bench and start racking some weights on it. You lay down on the bench while [the_person.title] stands by your head."
        "She looks around a bit to see if anybody is watching you before prompting you to begin."
        the_person.char "Ready? It's my turn now..."
        "As you lift the weight up over the bar and begin to bring it down to your chest, [the_person.title] slowly moves forward, maneuvering her legs until her crotch is right above your face."
        "You breathe deep. There is the normal gym smells of weights, rubber, and sweat, but also a smell that is distinctly, sweetly feminine."
        "You lift your head up for a second, making contact with her crotch with your face. She stifles a groan as you finish up your set."
        $ the_person.change_max_energy(5)
        $ the_person.change_arousal(20)
        "[the_person.title] backs off and you quickly get up. She puts a hand on your shoulder and whispers in your ear."
        the_person.char "Do you want to fool around a little?"
        "You nod your head."
        the_person.char "There's a locker room here families can use with a lock on it. Meet me there in three minutes."
        $ the_person.draw_person( position = "walking_away")
        "You watch [the_person.title] walk off, fighting off an erection. Looks like you're about to hookup at the gym!"
        "After three minutes, you follow after [the_person.title]. When you find the family use room, you let yourself in."
        $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True)
        $ the_person.draw_person( position = "stand2")
        "As you enter, you see that [the_person.title] is already naked."
        the_person.char "[the_person.mc_title], I'm so turned on. Can you do what you did a little bit ago again?"
        "She points to a bench sitting along the wall."
        "She looks nervous. You can tell she is just looking for fool around a bit."
        menu:
            "Service Her\n{color=#ff0000}{size=18}Increases Love{/size}{/color}":
                mc.name "I'd love to get a taste..."
                $ the_person.change_love(10)
                the_person.char "Wow, what a gentleman! Over here."
                "She leads you to the bench. You willfully lay back on it. She climbs on top of you."
                $ the_person.draw_person(position = "kneeling1")
                "She slowly climbs up your body until her cunt is inches from your face."
                "You lean forward and run your tongue along her slit. She moans softly as soon as you make contact."
                the_person.char "Oh [the_person.mc_title]..."
                $ the_person.break_taboo("licking_pussy")
                call get_fucked(the_person, the_goal = "get off", private= True, start_position = cowgirl_cunnilingus, start_object = make_bench(), skip_intro = True, ignore_taboo = True, allow_continue = False) from _erica_first_oral_01
                the_person.char "Wow I needed that so bad..."
                "For a bit she just sits on top of you, recovering. Soon, however, you feel her reach back and start to stroke your cock."
                the_person.char "Mmm, it wouldn't be fair for me be the only one getting some relief... I bet you taste good..."
                the_person.char "I want to taste you..."
                "She kisses you on the neck, then starts slowly working her way down your chest."
                "When she reaches your waist, she slowly undoes your pants, then pulls them down and off, revealing your erection."
                the_person.char "Oh [the_person.mc_title]..."
                "[the_person.possessive_title] looks down at your shaft for a moment, giving it a couple strokes. She leans forward and kisses the tip of your dick gingerly."
                "Her mouth opens and you feel the warm, wetness of her gullet envelope your cock. It feels great as she starts to bob her head up and down on it."
                $ the_person.break_taboo("sucking_cock")
                call get_fucked(the_person, the_goal = "oral creampie", private= True, start_position = cowgirl_blowjob, start_object = make_bench(), skip_intro = True, ignore_taboo = True, allow_continue = False) from _erica_first_oral_02
                "You lay back and catch your breath as [the_person.title] gets up."
                $ the_person.draw_person()
                the_person.char "Mmm, that was really nice. I could get used to that."
                the_person.char "I'm gonna shower really quick. We should probably get out of here ASAP."
                mc.name "You're right. I'll join you."
                the_person.char "Okay, but no funny business."
                "You join [the_person.title] in the shower. You splash around a bit and grab her ass once or twice, but go no further."
                $ the_person.apply_planned_outfit()
                the_person.char "Alright, I'm gonna sneak out. Wait a couple minutes, then leave too, okay?"
                "You agree. [the_person.title] slips out of the room, leaving you a long with your thoughts."
                "You know she is young, and not looking for anything serious, but you are really starting to take a liking to this girl."
                "Maybe with a bit more time, more serums, and some mind blowing sex, you can convince her to go steady with you."

            "Exchange Services\n{color=#ff0000}{size=18}Increases sluttiness{/size}{/color} (disabled)": #TODO FWB PATH
                pass
            "Force her to Service You\n{color=#ff0000}{size=18}Increases Obedience and sluttiness\nDecreases Love{/size}{/color} (disabled)": #TODO HATE FUCK PATH
                pass

        $ the_person.event_triggers_dict["erica_progress"] = 2

        # "You walk over to her and quickly strip. You grab [the_person.title] by that ass and pick her up. You carry her to the wall and pin her up against it."
        # $ the_person.draw_person( position = "against_wall")
        # "[the_person.possessive_title] is grinding her hips up against yours. The sweat from your workouts mingles together as you prepare yourself to enter her."
        #
        # $ the_person.add_situational_slut("horny", 20, "She is desperate to be fucked")
        #
        # # NOTE skip intro prevents taboo break from executing
        #
        # call condom_ask(the_person) from _erica_mod_condom_ask_CS010
        #
        # "As you begin to push yourself inside her, she drags her nails across your back."
        # $ the_person.break_taboo("vaginal_sex")
        # if not mc.condom:
        #      $ the_person.break_taboo("condomless_sex")
        # the_person.char "Oh fuck, that's good. Give it to me good, [the_person.mc_title]!"
        # call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, asked_for_condom = True) from _call_casual_sex_mod_CS010
        # $ the_report = _return
        # if the_report.get("girl orgasms", 0) > 0:
        #     "As you slowly let [the_person.title] down from the wall, you can see her trembling, caused by aftershocks from her orgasm."
        #
        # the_person.char "Mmm... that was nice..."
        # "[the_person.title] stutters for a moment."
        # $ the_person.clear_situational_slut("horny")
        # the_person.char "But... you know... I really can't get involved in a serious relationship right now."
        # mc.name "I agree. We need some ground rules. Want to have coffee and figure it out?"
        # the_person.char "That sounds good. But it's not a date, okay? Just need to set boundaries."
        # "You agree. You and [the_person.title] take a quick shower, then get ready and leave the gym."
        #
        # $ the_person.apply_planned_outfit()
        #
        # "You head to a nearby coffee shop. You grab yourself a coffee, letting [the_person.title] pay for her own. You grab a seat at a booth away from any other people."
        # $ renpy.show("restaurant", what = restaraunt_background)
        # $ the_person.draw_person( position = "sitting")
        #
        # the_person.char "So... are you interested in a friends with benefits set up?"
        # "You give a quick nod."
        # the_person.char "Okay, so, some ground rules. First off, if either of us starts to catch feelings for the other person, we break it off. I sure as fuck don't have time for that stuff right now..."
        # mc.name "I agree. We'll keep it physical. No dates or whatever. Just hit me up when you want to fuck around."
        # the_person.char "Right... here, let's exchange numbers. I'll text you and if we're both free, we can screw around, no strings attached."
        # "You agree. You and [the_person.title] finish up with your coffees. You both get up to leave."
        # $ the_person.draw_person(position = "stand3")
        # the_person.char "Well, see you around, stud! I'd better go work on some homework."
        # "You say your goodbyes. This should be interesting. You wonder what kind of crazy sex you'll have with your new friends with benefits."
        #
        # $ the_person.event_triggers_dict["booty_call"] = True
        #
        # "You now have [the_person.title]'s phone number."
        # $ the_person.event_triggers_dict["erica_progress"] = 2

    elif the_person.event_triggers_dict.get("erica_progress", 0) > 1:
        mc.name "Hey [the_person.title]. I figured I would find you here. Want to workout together?"
        the_person.char "That sounds great, [the_person.mc_title]! I always enjoy working up a sweat with you."
        mc.name "Sounds good! I'll head to the locker room and get changed and meet you over by the free weights."
        "You quickly get yourself changed into workout clothes and meet [the_person.title]."
        $ the_person.draw_person( position = "stand4")
        "It is obvious from the beginning of your workout with [the_person.possessive_title] that she intends to get frisky with you when you get done."
        "While doing squats, she gets right behind you, pressing her body against yours as she spots you."
        "You try to be as covert as possible, but a couple of the other guys in the gym shoot you knowing looks as you go about your workout."
        "During the bench press, [the_person.title] stands right above you, her crotch tantalizingly close to your face."
        # $ the_person.change_max_energy(5)
        #TODO change dialogue based on path
        the_person.char "Wow, what a workout! So... are you gonna go hit the showers now?"
        "It is clear from the way she is asking she is curious if you are gonna follow her to the secluded locker room."
        menu:
            "Hit the Shower":
                #TODO some kind of innuendo joke here#

                mc.name "Yeah, I'm pretty sweaty. I'd better get cleaned up!"
                $ the_person.draw_person( emotion = "happy")
                "She gets close to you and whispers in your ear."
                the_person.char "You now where to go... meet me in 5."
                $ the_person.draw_person( position = "walking_away")
                "You watch [the_person.title]'s amazing ass as she walks away. You swear there's a bit of a swagger there."
                "You give her a few minutes, then follow after her."

                #locker room sex scene.
                call erica_locker_room_label(the_person) from _erica_locker_room_transition_01



            "Not Today":  #lol what a tease#
                the_person.char "Oh. Okay, I understand. Well, I'll see you around, [the_person.mc_title]!"
                $ the_person.change_happiness(-3)

    $ the_person.apply_planned_outfit()
    call advance_time from _call_advance_erica_workout
    return

label erica_locker_room_label(the_person): #TODO this will be Erica's sluttiness scaling event. As sluttiness increases, she does crazier stuff in the locker room.
    $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True)
    $ the_person.draw_person( position = "stand2")
    "As you enter, you see that [the_person.title] is already naked."
    if erica_on_love_path():
        mc.name "Oh god, I'll never get tired of seeing your fit body naked."
        if mc.max_energy > 200:
            the_person.char "Me? You have the body of a god. Get those clothes off mister."
            "As you start to undress, she runs her hands up and down your chiseled frame. She clearly enjoys your body."
            $ the_person.change_arousal(20)
        elif mc.max_energy > 160:
            the_person.char "You're pretty fit yourself there mister. Why don't you get those clothes off?"
            "As you start to undress, she runs her hands up and down your chest. She enjoys your body."
            $ the_person.change_arousal(10)
        else:
            the_person.char "Mmm, save your flattery and get naked."
            "You undress and walk over to her."
        the_person.char "So... want to fool around some? If you want I'd be glad to take the lead..."
        menu:
            "Fuck her":
                "You step closer to her. You put your hands on her hips and pull her in."
                $ the_person.draw_person(position = "kissing")
                "You lean in and kiss [the_perosn.possessive_title] hungrily. Her hips are grinding against yours."
                $ the_person.change_arousal(10)
                $ mc.change_arousal(10)
                $ the_person.add_situational_slut("horny", 10, "She submits to you")
                the_person.char "Mmm, I'm ready... do what you want [the_person.mc_title]..."
                call fuck_person(the_person, private = True) from _erica_gets_fucked_by_her_man_in_lockerroom_01
            "Let her take the lead":
                mc.name "I'd like to see how you handle this thing."
                "You give your dick a stroke. She chuckles and leans forward."
                the_person.char "Don't worry, I know just what to do."
                $ the_person.add_situational_slut("horny", 20, "She takes the lead")
                "She is excited to take the lead."
                call get_fucked(the_person, private= True) from _erica_pleases_her_man_in_lockerroom_01
        $ the_report = _return
        $ the_person.draw_person(position = "sitting")
        if the_report.get("girl orgasms", 0) > 0:
            "[the_person.title] sits down on the bench, you can see her trembling, caused by aftershocks from her orgasm."
            the_person.char "Mmm... god I'm glad you know how to use that cock."
        else:
            "[the_person.title] sits down on the brench, catching her breath."
        $ the_person.clear_situational_slut("horny")
        "Without another word, you and [the_person.title] take a quick shower, then get ready and leave the gym."
        "You share a quick kiss before you part ways."
    elif erica_on_hate_path():
        pass

    else:
        if the_person.sluttiness > 50:
            the_person.char "[the_person.mc_title], give me that cock! It's been too long since you fucked me good!"
            "You walk over to her and quickly strip. You grab [the_person.title] by that ass and pick her up. You carry her to the wall and pin her up against it."
            $ the_person.draw_person( position = "against_wall")
            "[the_person.possessive_title] is grinding her hips up against yours. The sweat from your workouts mingles together as you prepare yourself to enter her."

            $ the_person.add_situational_slut("horny", 20, "She is desperate to be fucked")

            call condom_ask(the_person) from _erica_mod_condom_ask_CS011
            "As you begin to push yourself inside her, she drags her nails across your back."
            if not mc.condom:
                $ the_person.break_taboo("condomless_sex")
            the_person.char "Oh fuck, that's good. Give it to me good, [the_person.mc_title]!"
            call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, asked_for_condom = True) from _call_casual_sex_mod_CS011
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "As you slowly let [the_person.title] down from the wall, you can see her trembling, caused by aftershocks from her orgasm."
                the_person.char "Mmm... god I'm glad you know how to use that cock."
            $ the_person.clear_situational_slut("horny")
            "Without another word, you and [the_person.title] take a quick shower, then get ready and leave the gym."
        else:
            the_person.char "[the_person.mc_title], I really need to get off. Can you get naked please?"
            "You walk over to her and quickly strip. She runs her hands along your chest."
            the_person.char "I'm going to do what I want with you... don't worry it will be good for both of us."
            "She is trying to push you back on to the bench. Do you want to let her take the lead?"
            menu:
                "Take Charge":
                    "You decide not to let her take charge. You stop and grab her wrists."
                    mc.name "I don't think so. I'm the man here. Lay down, I'll lick your pussy for a bit first."
                    "She starts to protest, but quickly stops when she realizes you are gonna eat her out."
                    $ the_person.change_happiness(-3)
                    $ the_person.change_obedience(5)
                    $ the_person.add_situational_slut("horny", 10, "She submits to you")
                    $ the_person.draw_person(position = "missionary")
                    call fuck_person(the_person, private = True, start_postion = cunnilingus, start_object = make_bench()) from _erica_gets_fucked_by_her_man_in_lockerroom_02
                "Let her take the lead":
                    "You decide to let her take charge. She gently pushes you back onto the bench."
                    $ the_person.change_happiness(3)
                    $ the_person.change_obedience(-5)
                    the_person.char "Don't worry, I know just what to do."
                    $ the_person.add_situational_slut("horny", 20, "She takes the lead")
                    "She is excited to take the lead."
                    call get_fucked(the_person, private= True) from _erica_pleases_her_man_in_lockerroom_02

            $ the_person.clear_situational_slut("horny")
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.title] sits down on the bench, you can see her trembling, caused by aftershocks from her orgasm."
                the_person.char "Mmm... god I'm glad you know how to make a girl cum so hard."
            else:
                "[the_person.title] sits down on the brench, catching her breath."
            $ the_person.clear_situational_slut("horny")
            "Without another word, you and [the_person.title] take a quick shower, then get ready and leave the gym."
    return

#CSA20
label erica_phase_two_label(the_person):
    if the_person.event_triggers_dict.get("erica_progress", 0) == 2:
        "You see [the_person.title] on the treadmill. She is running hard, and has been training for a race coming up soon. She pauses the treadmill as you walk up to her."
        the_person.char "Hey [the_person.mc_title], here for another workout?"
        mc.name "Not today, [the_person.title]. How goes training? Is that big race coming up soon?"
        if day % 7 == 4:  #It is friday, the race is tomorrow!
            the_person.char "Yeah! As a matter of fact, it's tomorrow!"
        else:
            the_person.char "Yeah! It's coming up quick, on Saturday morning!"
        "She checks you out for a minute, before continuing."
        the_person.char "You know, it's a charity race, with proceeds going to breast cancer! You seem pretty fit, and I know how much you love tits. Maybe you should race too?"
        "You give her a smile."
        mc.name "Ah, that sounds like a good cause, but I couldn't. I'd hate for our arrangement to come to an end because we are in the same race and I beat you and you get mad."
        the_person.char "Hah! You wish! You seem awfully confident. I tell you what, why don't we make a little bet?"
        "You are intrigued by where she is going with this."
        mc.name "Go on."
        the_person.char "You come out and race. When the race is over, we go back to my place, and whoever won gets to do anything they want with the loser!"
        mc.name "Anything?"
        "She gives you a wink."
        the_person.char "That's what I said, isn't it?"
        mc.name "You've got a deal. Saturday morning downtown. I'll be there."
        $ the_person.draw_person (position = "stand4")
        the_person.char "Yes! Oh my [the_person.mc_title], no backing out now! I'll have to find my handcuffs..."
        "[the_person.title] seems pretty confident in herself, but you are pretty sure you have good odds in a race."
        "You wave goodbye to [the_person.title], wondering what you've gotten yourself in to."

        $ add_erica_race_crisis(the_person)
        "Things have been progressing well with [the_person.title], but soon, you might have to make a decision."
        "Is she someone you are interested in dating? Just a friend with benefits? Or do you want to turn her into a mindless fucktoy?"
        "You have a feeling the outcome of your bet could change your relationship with her."

        $ the_person.event_triggers_dict["erica_progress"] = 3
    elif the_person.event_triggers_dict.get("erica_progress", 0) == 3:
        mc.name "Hey [the_person.title], I just wanted to verify, the race is this Saturday, right?"
        the_person.char "That's right! I can't wait to beat your ass in the race, and then spank it again later at my place!"
        mc.name "Yeah right, I'll be bending you over before you can even get your front door closed."
        "[the_person.title] has a spark in her eyes. Whoever wins, you have a feeling the sex is going to be amazing after the race."
        "You wave goodbye to [the_person.title], wondering what you've gotten yourself in to."

    $ the_person.apply_planned_outfit()
    call advance_time from _call_advance_erica_race_challenge
    return



#CSA30
label erica_race_crisis_label(the_person):
    "It's race day! You make your way downtown, ready for your race with [the_person.title]."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "You find where they are organizing the race. It is a 5 kilometer race, which is about three miles long."
    "You look around and eventually find [the_person.title]."
    $ the_person.apply_gym_outfit()
    $ the_person.draw_person(position = "stand3")
    the_person.char "Hey, there you are! I was starting to think you had chickened out!"
    mc.name "Not a chance. I hope you don't have any plans for tomorrow, because when I get done with you tonight you won't be able to get out of bed until Monday at least!"
    the_person.char "Oh my, brave words for a brave boy! Let's just see what happens!"
    "You and [the_person.title] do some stretching and warmups, but soon it is time for the race to begin."
    "You line up together at the starting line, ready for the race to begin."
    "*BANG*"
    $ the_person.draw_person(position = "walking_away")
    "The official starts the race with a shot from the gun and the race begins! [the_person.title] jumps out in front of you, setting a fast pace."
    "You are tempted to chase after her, but think better of it. This is a long race, and you need to pace yourself."
    $ clear_scene()
    "As you near the first kilometer, you lose sight of [the_person.title] in the crowd of racers, but you are sure you aren't far behind."
    "You settle into your pace, determined to let your energy carry you through the race, no matter what happens. You pass the second kilometer marker"
    "You breathe in, you breathe out. You take pace after pace, determined to race with the best of your abilities."
    "As you approach the third kilometer marker, you can see yourself catching up to a familiar form."
    $ the_person.draw_person(position = "walking_away")
    "God she is hot, her ass sways back and forth with each step she takes. You imagine all the things you want to do with those delightfully tight cheeks."
    "You are breathing hard. It's getting so hard to keep up. She starts to pull away from you."
    "No! It's time to dig deep! You pump your arms and breath deep."
    "After a few moments, you catch your second wind. You get a burst of energy and race faster."
    "You are catching up to her, and you find yourself running with a renewed vigor from the flow of testosterone in your bloodstream, day dreaming about [the_person.possessive_title]."
    "You pass the marker for the fourth kilometer. This is it, it's now or never!"
    "You surge forward, and soon you are right beside her. She is gasping for air, she is completely winded!"
    the_person.char "[the_person.mc_title]? Oh god..."
    "She barely gets her words out as you pass her."
    $ clear_scene()
    "You keep pushing forward, not daring to turn around."
    "You round a corner. The finish line! You give it everything you have! Your breathing is heavy and ragged, sucking in every ounce of air you can."
    "You cross the finish line. You beat her!!!"
    "You are catching your breath, and turn to see her cross the finish line just a few seconds behind you."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.title] is breathing hard. She walks up to a table nearby and bends over with her hands on it, trying desperately to catch her breath."
    "You walk up behind her and put your hands on her back. You are careful not to be too obvious, but you make some contact with her backside with your hips."
    mc.name "Hey there, [the_person.title]! Nice race! I'm so glad you invited me out here to support such a charitable cause..."
    $ the_person.draw_person(position = "stand4")
    "She stands up and turns to face you."
    the_person.char "Yeah!... I mean, it's all for a good cause, right?"
    $ the_person.change_max_energy(10)
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    "You think you see a little smirk on the corner of her mouth."
    "You both take a few minutes to recover, and soon you are ready to go."
    the_person.char "Alright, you won the race. I guess it's time to head back to my place?"
    "You call for an Uber and she gives you here address. Soon you are walking into [the_person.title]'s apartment."
    "Your mind is racing. She is going to be completely at your mercy. Its now or never, time to make a decision on which direction you want to take things."
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    $ the_person.learn_home()
    "You walk in the door. What do you want to do? WARNING: This decision is permanent."
    menu:
        "Take her ass \n{color=#ff0000}{size=18}Corruption path \n Not yet written{/size}{/color} (disabled)":
            "This path is not yet written"
            pass
        "Fuck her rough \n{color=#ff0000}{size=18}FWB path{/size}{/color}":
            "You decide not to push her for anything serious. She is busy with her athletics, and she's mentioned she doesn't really have time for anything anyway."
            "Your mind is made up. There's nothing wrong with having a friend with benefits!"
            call erica_post_race_fwb_label(the_person) from _erica_fwb_decision_post_race_1
        "Make love \n{color=#ff0000}{size=18}Girlfriend path{/size}{/color}":
            "You watch [the_person.possessive_title] as she walks into her apartment. She is so sexy and fun, you find yourself wanting to spend all your free time with her."
            "You make up your mind. You know she's mentioned she doesn't really have time for something serious right now... but maybe you could find a way to work around that?"
            "You can be patient. And for a girl like [the_person.title], you feel like it might be worth it."
            "Your mind is made up. You are going to ask her out. But first, you need to take advantage of your current situation..."
            call erica_post_race_love_label(the_person) from _erica_love_decision_post_race_1

    return

label erica_post_race_corruption_label(the_person):
    pass
    return

label erica_post_race_fwb_label(the_person):
    "As soon as you walk in the door, you grab [the_person.title]. You pick her up and push her against the wall."
    $ the_person.draw_person(position = "against_wall")
    $ the_person.add_situational_slut("Lost Bet",25,"Be ready for anything!")
    the_person.char "Fuck! Mmm, are we gonna start right here? I remember the terms, do what you want to with me..."
    "You growl into her neck as you grind your hips into hers."
    mc.name "That's right, you're my sexy bitch for the day."
    "You back up from the wall, but hold her tight, keeping her feet from reaching the floor. You turn and take her into her bedroom."
    $ the_person.draw_person(position = "missionary")
    "You throw her down on her bed."
    if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
        "You stop for a second and admire [the_person.title], her body on display in front of you."
        $ the_person.change_arousal(20)
        "You notice some moisture building around her slit. She is definitely enjoying your hungry eyes roaming her body."
    else:
        "Your mind red with lust, you begin to rip [the_person.title]'s clothes off."

        $ the_person.strip_outfit(position = "missionary")
        $ the_person.change_arousal(20)

        "[the_person.possessive_title] moans as you strip her down, enjoying your rough treatment of her."
    "When she is full naked, you grab her hips and flip her over."
    $ the_person.draw_person(position = "doggy")
    $ the_person.change_arousal(5)
    "There it is, the ass that inspired your final push in the race. She lowers her face to the bed and wiggles her hips at you."
    "In a moment you are naked. You hop up on the bed and get behind her. You grab her hips and roughly pull her back toward you."
    "You rub her slit up and down with your furious erection, coating it with her juices. You give her ass a rough spank, eliciting a yelp."
    $ the_person.change_arousal(10)
    the_person.char "Oh fuck, please just put it in. I feel like I'm on fire!!!"
    "You consider for a second putting on a condom first. Nope, not a fucking chance. In one smooth motion you push yourself into her sopping, needy cunt."
    the_person.char "Yes!!! Oh god, please fuck me good!"
    "You have every intention of doing exactly that."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call fuck_person(the_person, private=True, start_position = doggy, start_object = make_bed(), skip_intro = True, asked_for_condom = True) from _call_casual_sex_mod_CS030
    $ the_report = _return

    $ the_person.clear_situational_slut("Lost Bet")
    "When you finish with her, [the_person.possessive_title] lays down on her bed."
    $ the_person.draw_person(position = "missionary")
    if the_report.get("girl orgasms", 0) > 0:
        the_person.char "[the_person.mc_title]... I am so sore... My legs from the race... and... you know..."
        the_person.char "But that was amazing... Look, I'll be your sexy bitch anytime you want, okay? You have my address now, feel free to stop by. Just promise you'll fuck me like that again."
        "You laugh."
    else:
        the_person.char "This was really great... Look, I'll be your sexy bitch anytime you want, okay? You know where I live now, so stop by anytime you feel like it."

    mc.name "Sounds good. You have my number, let me know if you wanna hookup sometime, or if you want a rematch!"
    the_person.char "Ayup! Don't worry. If it's all the same to you, I think I'm gonna take a nap now..."
    "You excuse yourself. You grab your clothes and head out. You now know [the_person.title]'s address, with a standing offer to come over and fuck her silly!"
    $ the_person.event_triggers_dict["erica_progress"] = 4
    $ perk_system.add_stat_perk(Stat_Perk(description = "Training for the big race has helped improve your energy level. +20 max energy, +40 energy cap.", energy_bonus = 20, bonus_is_temp = False, energy_cap = 40), "Athlete Energy Bonus")
    $ perk_system.add_ability_perk(Ability_Perk(description = "You take a few deep breaths and recover a bit of your energy. Use this perk to regain half your max energy, once per day.", toggle = False, usable = True, usable_func = second_wind_func, usable_cd = 1), "Second Wind")
    "You walk away with a spring in your step. You feel like training for and running the race has given you more energy."
    "You have gained the second wind ability perk. You can now recover half your max energy, once per day!"
    $ erica.event_triggers_dict["fwb_path"] = True
    return

label erica_post_race_love_label(the_person):
    "As soon as you walk in the door, you grab [the_person.title]. You pick her up and push her against the wall."
    $ the_person.draw_person(position = "against_wall")
    $ the_person.add_situational_slut("Lost Bet",25,"Be ready for anything!")
    the_person.char "Fuck! Mmm, are we gonna start right here? I remember the terms, do what you want to with me..."
    "You whisper into her ear as you grind your hips into hers."
    mc.name "That's right, you're mine for the day!"
    "You back up from the wall, but hold her tight, keeping her feet from reaching the floor. You turn and take her into her bedroom."
    $ the_person.draw_person(position = "missionary")
    "You throw her down on her bed."
    if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
        "You stop for a second and admire [the_person.title], her tight body on display in front of you."
        $ the_person.change_arousal(20)
        "You notice some moisture building around her slit. She is definitely enjoying your hungry eyes roaming her body."
    else:
        "Your mind red with lust, you begin to rip [the_person.title]'s clothes off."

        $ the_person.strip_outfit(position = "missionary")
        $ the_person.change_arousal(20)

        "[the_person.possessive_title] moans as you strip her down, enjoying your rough treatment of her."
    "When she is full naked, you get on top of her."
    $ the_person.change_arousal(5)
    the_person.char "Mmm, you can do anything you want with me, and you go for missionary?"
    mc.name "I thought you were mine for the whole day?"
    the_person.char "Fair enough."
    mc.name "Besides, I want to be able to look you in the eyes the first time I make love to you."
    "She gives you a cheesy grin."
    $ the_person.change_love(3)
    the_person.char "Getting sentimental on me? Look... we can talk about stuff later... right now I just need you inside me..."
    "She reaches down and takes hold of your cock. She points it at her entrance. Her legs wrap around you as she tries to pull you into her."
    mc.name "So needy, are you? Don't worry, I think we can both get what we want."
    "You relax your arms and legs, letting her pull you in. Your cock sinks into her steaming cunt raw."
    the_person.char "Oh!!! Yes that feels so good..."
    "You moan in appreciation. Her eyes are starting into yours as you bottom out inside of her."
    mc.name "Alright [the_person.title]. I didn't take it easy on you at the race, and I'm not about to go easy on you now!"
    the_person.char "Mmmm, prove it!"
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call fuck_person(the_person, private=True, start_position = missionary, start_object = make_bed(), skip_intro = True, asked_for_condom = True) from _call_casual_sex_mod_CS031
    $ the_report = _return
    "When you finish with her, [the_person.possessive_title] lays down on her bed."
    $ the_person.draw_person(position = "missionary")
    if the_report.get("girl orgasms", 0) > 0:
        the_person.char "[the_person.mc_title]... I am so sore... My legs from the race... and... you know..."
        mc.name "Mmm, yeah that was nice. I can't wait to do that again."
        the_person.char "Me too."
    else:
        the_person.char "This was really great... I can't wait to do that again."

    "You lay down next to her, just enjoying the heat of your bodies together. You want to experience this again and again with her."
    "You work up the courage to ask her out."
    mc.name "Look... I know you are busy with school and your athletics. But I love spending time with you, whenever you have free time..."
    the_person.char "Ohh [the_person.mc_title]..."
    mc.name "I'm not asking you to change anything about your life, I'm just asking to be a part of it."
    "She looks at you, thinking for a bit. Then cracks a grin."
    the_person.char "You're very charming, you know that? Before I met you, I was pretty sure I was going to just stay single through my college life..."
    the_person.char "But after getting to know you, I feel the same. I'm going to keep doing what I'm doing, but I want to spend my free time getting to know you better."
    mc.name "So... can I introduce you as my girlfriend?"
    the_person.char "Yeah... I'm not sure if this is going to work out, but I want to give it a try!"
    $ the_person.special_role.append(girlfriend_role)
    $ erica.event_triggers_dict["love_path"] = True
    "You roll over back on top of her and start to kiss her neck."
    $ the_person.change_arousal(10)
    the_person.char "Mmm, you're so fit too... I hope you're thinking what I'm thinking..."
    mc.name "It is definitely time for round two."
    "You feel yourself get a second wind as you start to play with [the_person.possessive_title]. You can see her do the same."
    $ second_wind_func()
    $ the_person.energy = the_person.max_energy
    the_person.char "Oh god you get me so hot... hang on."
    "She pushes you off her for a second. She turns over and gets on her hands and knees, pointing her ass at you."
    $ the_person.draw_person(position = "doggy")
    the_person.char "I want it like this... please! Please take me!"
    $ the_person.change_arousal(15)
    $ the_person.discover_opinion("doggy style sex")
    "Mmm, seems she likes it doggy style... and maybe has a bit of a submissive streak? You aren't sure about the latter yet, but you look forward to finding out."
    call fuck_person(the_person, private=True, start_position = doggy, start_object = make_bed()) from _call_casual_sex_mod_CS033
    "When you finish you are both spent."
    the_person.char "That was amazing... but I need to study, I've got a test on Monday. I love spending time with you, but you ARE a bit distracting..."
    mc.name "I understand. Tell you what, I'll head out, but before I go I'll order some lunch to get delivered, that way you can study without having to worry about making food."
    $ the_person.change_love(5)
    the_person.char "Aww, you don't have to do that. You are such a sweetheart."
    $ the_person.review_outfit()
    "While [the_person.possessive_title] gets cleaned up, you order her a healthy lunch to be deliverd on your phone. You know she is college student, so she probably doesn't have much disposable income."
    $ mc.business.change_funds(-10)
    mc.name "Alright, I got you a Keto special, it should be here soon. Good luck with your studying!"
    the_person.char "Goodbye [the_person.mc_title]. I'll see you soon! And you know where I live now. Feel free to swing by once in a while..."
    "You let yourself out and start to walk away. Wow, what an amazing day! You've managed to convince [the_person.title] to go out with you."
    "You can't wait to explore her tight little body more... but one thing at a time now."
    $ the_person.clear_situational_slut("Lost Bet")
    $ the_person.event_triggers_dict["erica_progress"] = 4
    $ perk_system.add_stat_perk(Stat_Perk(description = "Training for the big race has helped improve your energy level. +20 max energy, +40 energy cap.", energy_bonus = 20, bonus_is_temp = False, energy_cap = 40), "Athlete Energy Bonus")
    $ perk_system.add_ability_perk(Ability_Perk(description = "You take a few deep breaths and recover a bit of your energy. Use this perk to regain half your max energy, once per day.", toggle = False, usable = True, usable_func = second_wind_func, usable_cd = 1), "Second Wind")
    "You walk away with a spring in your step. You feel like training for and running the race has given you more energy."
    "You have gained the second wind ability perk. You can now recover half your max energy, once per day!"
    #call advance_time from _call_advance_erica_love_decision_01
    return

label erica_buy_protein_shake_label(the_person):
    if erica_on_love_path():
        mc.name "Hey [the_person.title], looking good! Can I get you a protein shake babe?"
        "[the_person.possessive_title] looks at you and smiles wide."
        the_person.char "Oh! Hey [the_person.mc_title], that would be great! I skipped the protein this morning..."
        "She lowers her voice."
        the_person.char "Maybe we should workout together... and you could give me another shot of protein when we get done..."
        mc.name "Mmm, that's a tempting offer. Let me get you set up with this for now though."
    elif erica_on_fwb_path():
        mc.name "Hey [the_person.title]. I see you're working hard today, can I get you the usual?"
        the_person.char "Hey! That sounds great! I need all the protein I can get."
        "She lowers her voice."
        the_person.char  "Especially from you... up for a workout today? And... you know..."
        mc.name "Mmm, that's a tempting offer. Let me get you set up with this for now though."
    elif erica_on_hate_path():
        mc.name "Damn, work it [the_person.title]. I'll go get you a protein shake."
        "She gives a wary eye. At this point, she is probably beginning to suspect you are messing with the shakes, but she knows better than to refuse."
        the_person.char "I guess that would be okay."
        mc.name "Good girl. I'll be right back."
    else:
        mc.name "Hey [the_person.name], I see you're working pretty hard today! Can I get you a protein shake?"
        "[the_person.possessive_title] looks at you and smiles."
        the_person.char "That sounds great!"
    $ clear_scene()

    "You head over to the counter where they have the supplements. You order her a protein shake."
    $ mc.business.change_funds(-5)
    $ erica.event_triggers_dict["protein_day"] = day
    "Before you take it back to her, you have a moment with no one around. You can add a serum to it if you do it quickly!"
    menu:
        "Add a dose of serum to [the_person.title]'s shake":
            call give_serum(the_person) from _call_give_serum_erica
            "You mix the serum into [the_person.title]'s protein shake. You take it over to her."

        "Leave her drink alone.":
            "You decide not to test a dose of serum out on [the_person.title] and take the shake back to her."

    if erica_on_love_path():
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Thanks! I really appreciate this. Anything else I can do for you?"
    elif erica_on_fwb_path():
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Thanks! So... you ready to workout?"
    elif erica_on_hate_path():
        "She takes the shake warily. She hesitates to take a sip."
        mc.name "Go on now. Don't worry, its good for you."
        $ the_person.change_obedience(3)
        $ the_person.change_love(-2)
        "She starts to drink it. She waits to see if you need anything else."
    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "I appreciate this. Anything else you wanted to talk about?"
    return

#CSA40
label erica_house_call_label(the_person):
    mc.name "Don't worry, I'm not here for business. I'm here for pleasure!"
    $ the_person.draw_person( position = "against_wall")
    "You reach around with both hands and grab her ass. You roughly pick her up, holding her tightly against you."
    the_person.char "Oh! Yes I was hoping that's why you were here..."
    "[the_person.possessive_title] wraps her legs around you and you begin to grind your hips together. Heat is quickly building between the two of you."
    "You carry her to her bedroom. The whole way there she is kissing and nipping at your neck and earlobe."
    $ the_person.draw_person(position = "missionary")
    "You throw her down on her bed."
    if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
        "You stop for a second and admire [the_person.title], her body on display in front of you."
        $ the_person.change_arousal(20)
        "You notice some moisture building around her slit. She is definitely enjoying your hungry eyes roaming her body."
    else:
        "Your mind red with lust, you begin to rip [the_person.title]'s clothes off."

        $ the_person.strip_outfit(position = "missionary")
        $ the_person.change_arousal(20)

        "[the_person.possessive_title] moans as you strip her down, enjoying your rough treatment of her."
    call fuck_person(the_person) from _call_casual_sex_mod_CSA040
    $ the_report = _return
    "After you finish with her, you get up and start to gather your clothes."
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title] is in an orgasm fueled daze, enjoying the effects it has on her."
    the_person.char "Thanks for stopping by... I think I'm just gonna lay down for a bit..."
    "Once you finish getting dressed you say goodbye and let yourself out. You head home and fall into bed, too tired to do anything else."

    $ mc.change_location(bedroom) # go home
    call advance_time from _call_advance_erica_house_call
    return

label erica_ghost_label(the_person):
    "You get a message on your phone. Looks like it is from [the_person.possessive_title]."
    the_person.char "Hey, I'm really sorry to have to do this, but I think I'm catching feelings."
    the_person.char "We agreed at the beginning we wouldn't let that happen, so I don't think we should see each other anymore."
    the_person.char "I'm changing to a different gym, and after I send this, I'm going to block your number. I'm sorry."
    "Damn. Sounds like you pushed things with her a little too far..."
    $ the_person.remove_person_from_game()
    $ casual_sex_create_athlete() #Create a new athlete so MC can try again if they choose.
    return
#************* Personality****************#
#Override some of her personality functions so that her conversation options makes sense.
#
# init 1301 python:              #Because Vren Init personality functions at 1300
#
#     def erica_titles(person):
#         valid_titles = []
#         valid_titles.append(person.name)
#         if person.effective_sluttiness() > 40:
#             valid_titles.append("College Athlete")
#             valid_titles.append("Cardio Bunny")
#         if person.effective_sluttiness() > 60:
#             valid_titles.append("Slutty Athlete")
#         return valid_titles
#
#     def erica_possessive_titles(person):
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
#     def erica_player_titles(person):
#         return mc.name
#
#     erica_personality = Personality("athlete", default_prefix = "introvert",
#     common_likes = ["small talk", "the colour blue", "sports", "taking control"],
#     common_sexy_likes = ["casual sex", "doggy style sex", "giving blowjobs", "showing her ass", "drinking cum"],
#     common_dislikes = ["relationships", "conservative outfits", "makeup", "the colour pink", "dresses", "high heels", "the colour purple"],
#     common_sexy_dislikes = ["lingerie", "being submissive", "skimpy outfits"],
#     titles_function = erica_titles, possessive_titles_function = erica_possessive_titles, player_titles_function = erica_player_titles)
#
# #************* Personality labels***************#
#
#
# label erica_greetings(the_person):
#     if mc.location == gym:
#         if the_person.love > 50:  #She loves you too much and is going to or already has called things off
#             the_person.char "Oh... hello, [the_person.mc_title]."
#             $ add_erica_ghost_action(the_person)
#             return
#         if the_person.event_triggers_dict.get("erica_progress", 0) >= 2:
#             the_person.char "Hey there, [the_person.mc_title]."
#             "You see [the_person.title] here at the Gym, in her usual spot on the treadmill."
#             the_person.char "You want to join me for another workout? I always leave the gym feeling so satisfied when we work out together!"
#         else:
#             the_person.char "Hey there!"
#     elif mc.location == the_person.home:
#         if the_person.event_triggers_dict.get("erica_progress", 0) > 3:
#             the_person.char "Hey there, [the_person.mc_title]! I wasn't expecting you! Are you here for some fun?"
#             "She looks at you hopefully."
#         else:
#             the_person.char "Hey there, [the_person.mc_title]. I wasn't expecting you, are you sure you should be here?"
#
#     elif the_person.effective_sluttiness() > 60:
#         if the_person.obedience > 130:
#             the_person.char "Hello, [the_person.mc_title], it's good to see you."
#         else:
#             the_person.char "Hey there handsome, feeling good?"
#     else:
#         if the_person.obedience > 130:
#             the_person.char "Hello, [the_person.mc_title]."
#         else:
#             the_person.char "Hey there!"
#     return
#
# label erica_sex_responses(the_person):
#     if the_person.effective_sluttiness() > 50:
#         if the_person.obedience > 130:
#             the_person.char "Oh my, keep doing that please!"
#         else:
#             the_person.char "Fuck it feels good when you do that. Keep going!"
#     else:
#         "[the_person.title] closes her eyes and moans quietly to herself."
#     return
#
# label erica_climax_responses_foreplay(the_person):
#     if the_person.effective_sluttiness() > 50:
#         the_person.char "Oh fuck yes, I'm going to cum! I'm cumming!"
#     else:
#         the_person.char "Oh fuck, you're going to make me cum! Fuck!"
#         "She goes silent, then lets out a shuddering moan."
#     return
#
# label erica_climax_responses_oral(the_person):
#     if the_person.effective_sluttiness() > 70:
#         the_person.char "Fuck yes, I'm going to cum! Make me cum!"
#     else:
#         the_person.char "Oh my god, you're good at that! I'm going to... I'm going to cum!"
#     return
#
# label erica_climax_responses_vaginal(the_person):
#     if the_person.effective_sluttiness() > 70:
#         the_person.char "I'm going to cum! Ah! Make me cum [the_person.mc_title], I want to cum so badly! Ah!"
#         "She closes her eyes and squeals with pleasure."
#     else:
#         the_person.char "Ah! I'm cumming! Oh fuck! Ah!"
#     the_person.char "Fuck this feels better than winning a marathon!"
#     return
#
# label erica_climax_responses_anal(the_person):
#     if the_person.effective_sluttiness() > 70:
#         the_person.char "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
#         the_person.char "Ah! Mmhmmm!"
#     else:
#         the_person.char "Oh fucking shit, I think you're going to make me..."
#         "She barely finishes her sentence before her body is wracked with pleasure."
#         the_person.char "Cum!"
#     return
#
# label erica_clothing_accept(the_person):
#     if the_person.obedience > 130:
#         the_person.char "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
#     else:
#         the_person.char "Thanks [the_person.mc_title]! I wonder if I could wear this at the gym."
#     return
#
# #label erica_clothing_reject(the_person):
# #    if the_person.obedience > 130:
# #        the_person.char "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
# #    else:
# #        if the_person.effective_sluttiness() > 60:
# #            the_person.char "Wow. I'm usually up for anything but I think that's going too far."
# #        else:
# #            the_person.char "Wow. It's a little... skimpy. I don't think I could wear that."
# #    return
#
# label erica_clothing_review(the_person):
#     if mc.location == gym:
#         if the_person.effective_sluttiness() > 40:
#             the_person.char "I love when you look at me like that, but I don't think the gym staff would appreciate it as much. I'd better clean up a bit."
#         else:
#             the_person.char "I'd better clean up some before I go to leave the gym..."
#     elif the_person.obedience > 130:
#         the_person.char "I'm sorry [the_person.mc_title], you shouldn't have to see me like this. I'll go and get cleaned up so I'm presentable again."
#     else:
#         if the_person.effective_sluttiness() > 40:
#             the_person.char "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
#         else:
#             the_person.char "My clothes are a mess! I'll be back in a moment, I'm going to go get cleaned up."
#     return
#
# #label erica_strip_reject(the_person):
# #    if the_person.obedience > 130:
# #        the_person.char "I'm sorry, but can we leave that where it is for now?"
# #    elif the_person.obedience < 70:
# #        the_person.char "Slow down there, I'll decide when that comes off."
# #    else:
# #        the_person.char "I think that should stay where it is for now."
# #    return
#
# label erica_sex_accept(the_person):
#     if the_person.effective_sluttiness() > 70:
#         if the_person.obedience < 70:
#             the_person.char "I was just about to suggest the same thing."
#         else:
#             the_person.char "Mmm, you have a dirty mind [the_person.mc_title], I like it."
#     else:
#         the_person.char "Okay, we can give that a try."
#     return
#
# label erica_sex_obedience_accept(the_person):
#     if the_person.effective_sluttiness() > 70:
#         the_person.char "Oh god [the_person.mc_title], I should really say no... But you always make me feel so good, I can't say no to you."
#     else:
#         if the_person.obedience > 130:
#             the_person.char "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
#         else:
#             the_person.char "I... Okay, if you really want to, lets give it a try."
#     return
#
# label erica_sex_gentle_reject(the_person):
#     if the_person.effective_sluttiness() > 50:
#         the_person.char "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
#     else:
#         the_person.char "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
#     return
#
# label erica_sex_angry_reject(the_person):
#     if the_person.effective_sluttiness() < 20:
#         the_person.char "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
#         the_person.char "Ugh! Get away from me, I don't even want to talk to you after that."
#     else:
#         the_person.char "What the fuck do you think you're doing, that's disgusting!"
#         the_person.char "Get the fuck away from me, I don't even want to talk to you after that!"
#     return
#
# label erica_seduction_response(the_person):
#     if the_person.obedience > 130:
#         if the_person.effective_sluttiness() > 50:
#             the_person.char "Yes [the_person.mc_title]? Do you need help relieving some stress?"
#         else:
#             the_person.char "Yes [the_person.mc_title]? Is there something I can help you with?"
#     else:
#         if the_person.effective_sluttiness() > 50:
#             the_person.char "Mmm, I know that look. Do you want to fool around a little?"
#         elif the_person.effective_sluttiness() > 10:
#             the_person.char "Oh, do you see something you like?"
#         else:
#             the_person.char "Oh, I don't really know what to say [the_person.mc_title]..."
#     return
#
# label erica_seduction_accept_crowded(the_person):
#     if mc.location == gym:
#         if the_person.effective_sluttiness() < 20:
#             the_person.char "I suppose we could sneak away into the locker room... There's nothing wrong with that, right?"
#         elif the_person.effective_sluttiness() < 70:
#             the_person.char "Come on, let's sneak into the locker room and do it!"
#         else:
#             the_person.char "Oh fuck that sounds nice. I'm not sure I can wait until we sneak into the locker room, maybe we should just do it right here!"
#         return
#
#     if the_person.effective_sluttiness() < 20:
#         the_person.char "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
#     elif the_person.effective_sluttiness() < 50:
#         the_person.char "Come on, let's go find someplace quiet where we won't be interrupted."
#     else:
#         the_person.char "No point waisting any time then, right? Let's get to it!"
#     return
#
# label erica_seduction_accept_alone(the_person):
#     if mc.location == gym:
#         if the_person.effective_sluttiness() < 20:
#             the_person.char "Well, there's nobody around to see us..."
#         elif the_person.effective_sluttiness() < 50:
#             the_person.char "I can't believe how empty the gym is right now. Let's do it right here!"
#         else:
#             the_person.char "Oh [the_person.mc_title], the gym is empty, fuck me now!"
#         return
#     if the_person.effective_sluttiness() < 20:
#         the_person.char "Well, there's nobody around to stop us..."
#     elif the_person.effective_sluttiness() < 50:
#         the_person.char "Mmm, that's a fun idea. Come on, let's get to it!"
#     else:
#         the_person.char "Oh [the_person.mc_title], don't make me wait!"
#     return
#
# #label erica_seduction_refuse(the_person):
# #    if the_person.effective_sluttiness() < 20:
# #        "[the_person.title] blushes and looks away from you awkwardly."
# #        the_person.char "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."
# #
# #    elif the_person.effective_sluttiness() < 50:
# #        the_person.char "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
# #        "[the_person.title] smiles and gives you a wink."
# #
# #    else:
# #        the_person.char "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
# #    return
#
# label erica_flirt_response(the_person):
#     if mc.location == gym:
#         if the_person.love > 50:  #She loves you too much and is going to or already has called things off
#             the_person.char "Didn't your mother ever tell you it's rude to hit on girls at the gym?"
#             return
#         if the_person.event_triggers_dict.get("erica_progress", 0) >= 2:
#             the_person.char "Well why don't you workout with me for a bit and we can work up a sweat together?"
#         else:
#             the_person.char "Hey, maybe if you workout with me first."
#             "[the_person.title] gives you a wink and smiles."
#         return
#
#     if the_person.obedience > 130:
#         if the_person.effective_sluttiness() > 50:
#             the_person.char "If that's what you want I'm sure I could help with that [the_person.mc_title]."
#         else:
#             the_person.char "Thank you for the compliment, [the_person.mc_title]."
#     else:
#         if the_person.effective_sluttiness() > 50:
#             the_person.char "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peak."
#             "[the_person.title] smiles at you and spins around, giving you a full look at her body."
#         else:
#             the_person.char "Hey, maybe if you buy me dinner first."
#             "[the_person.title] gives you a wink and smiles."
#     return
#
# label erica_flirt_response_low(the_person):
#     #She's in her own outfit.
#     "[the_person.possessive_title] blushes and smiles."
#     the_person.char "Thanks. I didn't think anyone even paid attention to what I wear. I mean it's just gym clothes..."
#     mc.name "Yeah, and the way you dress makes it obvious how well you take care of yourself. It's pretty incredible."
#     return
#
# label erica_flirt_response_mid(the_person):
#
#     if the_person.effective_sluttiness() < 20:
#         the_person.char "Thanks! I work hard to take of myself. It's kind of weird to hear, but I'm glad it shows."
#
#     else:
#         the_person.char "Thanks! One of the benefits of being in shape I guess, you can wear clothing to show off your body."
#         the_person.char "You want a better look, right? Here, how does it make my ass look?"
#         $ the_person.draw_person(position = "back_peek")
#         the_person.char "Good?"
#         mc.name "Fantastic. I wish I could get an even better look at it."
#         "[the_person.possessive_title] smiles and turns back to face you."
#         $ the_person.draw_person()
#         the_person.char "I'm sure you do. Maybe instead of shooting the breeze you should workout with me..."
#     return
#
# label erica_flirt_response_high(the_person):
#     if the_person.love > 50: #She is going to ghost soon
#         the_person.char "I feel like you are going a little overboard there with the flattery. Could you please stop?"
#     else:
#         "She looks at you and her eyes narrow."
#         the_person.char "I appreciate the comment, I really do... but I'm worried you are taking things a little too far."
#         the_person.char "Remember, we need to keep things CASUAL. Okay?"
#     return
#
#
# label erica_hookup_rejection(the_person):
#     the_person.char "Your loss! I've been working out so much lately, and you could have had some of this..."
#     return
#
# label erica_hookup_accept(the_person):
#     the_person.char "Meet me at the gym... you know the place!"
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
#     the_person.char "Mmmm, this is my favorite warm up..."
#     $ the_person.change_arousal( 15 + (mc.sex_skills["Oral"] * 2)) #35 + 2
#     "You quickly lap up the juices available along her labia, then focus your attention on her clitoris with the goal of making more."
#     "You circle your tongue around it several times, teasing her. Just when she thinks you are going to lick it you dart down to her hole."
#     the_person.char "What a tease! I had a boyfriend once who couldn't find my clit either... here let me help you."
#     $ the_person.change_arousal( 15 + (mc.sex_skills["Oral"] * 2)) #50 + 4
#     "[the_person.title] runs a hand through your hair, then grabs some of it on the back of your head. She begins to gyrate her hips as she grinds into you."
#     "You decide to go with it. You flatten your tongue out and begin to move it across her clitoris in long strokes."
#     "She grinds herself happily against your face. She moans appreciatively at your skilled oral stimulation."
#     $ the_person.change_arousal( 15 + (mc.sex_skills["Oral"] * 2)) #65 + 6
#     if the_person.arousal > 100: #She is surprised how fast you make her cum
#         "Suddenly, you feel her body go stiff and her moans ramp up quickly."
#         the_person.char "Fuck! I'm gonna... you're gonna make me...!"
#         "[the_person.title] convulses as she orgasms. She is caught completely off guard by how fast you made her cum."
#         "The hand on the back of your head lets go but you continue your assault for several more seconds."
#         $ the_person.change_slut_temp(1)
#         $ the_person.change_happiness(2)
#     else:
#         the_person.char "Mmm, that's it. Your tongue feels so good. Give it a good workout..."
#         "[the_person.title]'s hand leaves the back of your head but you keep going. You lightly suck on her clit, drawing it into your mouth a few seconds at a time before licking it again."
#         "Her body is responding. Her hips are starting to twitch back and forth on their own as she approaches an orgasm."
#         $ the_person.change_arousal( 15 + (mc.sex_skills["Oral"] * 2)) #80 + 8
#         if the_person.arousal > 100: #She orgasms
#             the_person.char "Yes! That's it! I'm gonna cum!"
#             "[the_person.title] convulses as she orgasms. She moans and runs her hands through your hair."
#             "You continue your assault for several more seconds."
#         else:   #Not skilled enough to make her orgasm.
#             "You are feverishly working at her pussy, but for some reason you can seem to find the right spot."
#             "Soon, the stimulation gets to be too much for her and she puts her hand on your hand and slowly pushes it back."
#     $ the_person.change_arousal(-30) #50 + 8
#     the_person.char "Mmm, that was a great warmup. Let me return the favor."
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
#         the_person.char "Do you want to put on a condom first?"
#         menu:
#             "Put on a condom":
#                 mc.name "Yeah, I'd probably better. I may not be able to resist pulling out."
#                 if the_person.effective_sluttiness() > 60:
#                     the_person.char "I mean... it's okay with me if you wanted to stick it in for a little bit without one on, you know, just to get started..."
#                     if the_person.effective_sluttiness() > 90:
#                         the_person.char "...or even just finish inside me. I promise I wouldn't mind at all!"
#                     mc.name "Maybe next time!"
#                 "You get a condom and put it on quickly."
#                 $ mc.condom = True
#             "Fuck her raw":
#                 $ mc.condom = False
#                 mc.name "No way, I want to feel everything."
#                 if the_person.effective_sluttiness() > 60:
#                     the_person.char "Mmmm, sounds good. I was hoping you would say that!"
#                     if the_person.effective_sluttiness() > 80:
#                         "She wiggles her ass back and forth a little bit."
#                         the_person.char "You don't need to worry about pulling out. I like it better when I feel the splash anyway..."
#                 else:
#                     the_person.char "Okay, just make sure to pull out before you finish, okay?"
#     else:
#         the_person.char "You have a condom right? Make sure you put one on..."
#         mc.name "Right! I'd probably better. I may not be able to resist pulling out."
#         "You get a condom and put it on quickly."
#         $ mc.condom = True
#     "You put your hands on her hips and put your dick at her entrance. She is still soaked from your oral earlier, so you easily slide into her."
#     "Her pussy feels amazing wrapped around your erection. Her legs shake a bit as she gets used to the depth of your penetration."
#     $ the_person.change_arousal(20) #70 + 8
#     the_person.char "Ohhh, [the_person.mc_title]... That is exactly what I was hoping for when I sent you that text earlier. That feels so good..."
#     "You give her a few tentative thrusts, then quickly pick up the pace and begin fucking her in earnest."
#     "Your hips slap against [the_person.possessive_title]'s ass as you fuck her vigorously."
#     $ the_person.call_dialogue("sex_responses_vaginal")
#     if mc.condom == True:
#         "You grasp her ass with both hands and begin to grope her. You knead her cheeks as your hips slowly work your erection in and out of her."
#         $ the_person.change_arousal(20) #90 + 8
#         if the_person.arousal > 100:
#             "You can feel [the_person.title]'s pussy begin to spasm as she cums. You can see in the mirror that her mouth is hanging open and her eyes are closed."
#             $ the_person.change_slut_temp(1)
#             $ the_person.change_happiness(2)
#         "After the stimulation from hew blowjob earlier, you know you aren't going to last long. You give her ass a loud spank."
#         mc.name "That's it, bitch. I'm about to cum!"
#         if the_person.effective_sluttiness() > 100: #She is so slutty, she begs for your cum.
#             the_person.char "The condom! Take it off! Please!?! Your cock is so good, I want to feel you dump your load inside me!"
#             "Your brain is getting a little hazy with lust. Surely there's nothing wrong with that, right?"
#             menu:
#                 "Take It Off":
#                     "In one swift you pull out of [the_person.title], pull the condom off, then shove yourself deep back inside her."
#                     "You wad up the condom then throw it on the counter. It lands with splat."
#                     the_person.char "Yes! Cum for me! I want to feel it!"
#                     $ the_person.change_arousal(20) #110 + 8
#                     "Her excitement is too much. You bottom out and cum, dumping wave after wave of your semen deep inside of her."
#                     the_person.char  "Yes! Fill me with your cum!"
#                     "You feel her pussy convulsing around your dick as she also starts to orgasm."
#                     $ the_person.change_slut_temp(1)
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
#             the_person.char "Wow, okay, I guess we are done?"
#             $ the_person.change_happiness(-5)
#             $ the_person.change_obedience(-5)
#             "She is a bit disappointed she didn't finish."
#         else:
#             the_person.char "That was nice. I'll make sure next time I'm in the mood to hit you up again..."
#         "You take your condom off and throw it in the trash can. You both get dressed before sneaking out of the locker room."
#         return
#     else: #You went in raw
#         "You push yourself in as deep as you can go. [the_person.possessive_title] moans as you fill her completely."
#         "With every thrust, her ass ripples pleasantly. You give her cheek an open handed spank and watch as shockwaves expand from the epicenter."
#         "[the_person.title] moans at your rough treatment."
#         $ the_person.change_arousal(20) #70 + 8
#         if the_person.arousal > 100:
#             "You can feel [the_person.title]'s pussy begin to spasm as she cums. Her silky wetness contracting around you feels amazing."
#             $ the_person.change_slut_temp(1)
#             $ the_person.change_happiness(2)
#     if the_person.effective_sluttiness() > 70:
#         the_person.char "You should umm, you know, stick a finger in my other hole..."
#         "Wow, it's not every day you have a beautiful woman ask you to finger her ass while you bend her over and fuck her!"
#         "You reach a hand forward and put your index finger in front of her face. She quickly gets the idea and opens her mouth with her tongue out, and begins slathering your finger with saliva."
#         "When satisfied, you bring you fingers back to her tight back passage. You pull your cock almost completely out and stop you hip motion as you begin to press your finger against [the_person.title]'s puckered hole."
#         "She forces her sphincter to relax and your finger begins to slip inside her."
#         the_person.char "Ohh, yes. You can move your hips, that feels good..."
#         "You give [the_person.possessive_title]'s cunt a few slow thrusts, while simultaneously fingering her other hole."
#         $ the_person.change_arousal(20)#90 + 8
#         if the_person.arousal > 120:
#             the_person.char "OH! It's so good... fuck I'm gonna cum again!!!"
#             "You get the now familiar feeling of [the_person.title] cumming around your cock, but this time you can also feel the waves around your finger."
#             "You wonder what it would feel like to make her cum again, but with your cock in her ass instead..."
#             menu:
#                 "Stay Vaginal":
#                     "As [the_person.title]'s pussy quivers around you, you decide to just keep doing what you are doing."
#                 "Fuck Her Ass" if the_person.effective_sluttiness() >= 80:
#                     "You pull out of her pussy. Her juices leave a strand attached to you, connecting you to her cunt."
#                     the_person.char "Mmm, [the_person.mc_title]? Why did you pull out... OH!"
#                     "Her question is swiftly answered when she feels your manhood poking her puckered hole."
#                     if the_person.effective_sluttiness() > 100:
#                         the_person.char "Yes! Fuck my ass good!"
#                     else:
#                         the_person.char "Oh my... be careful!"
#                     "With your hands firmly on her hips, you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
#                     the_person.char "Oh god you make me feel so dirty... I love it!"
#                     "You fuck her hard but at a steady, even pace."
#                     "[the_person.possessive_title] moans, matching each hip movement of yours with movement of her own."
#                     the_person.char "It feels so deep... I can't... my legs!"
#                     "Her knees give out, but you are too close to stop fucking her. You grab her hips roughly and pick up the pace."
#                     $ the_person.change_arousal(20)#110 + 8
#                     "Her ass begins to spasm. Her buttery smooth back passage squeezes you over and over as her body is racked with yet another orgasm. It feels incredible."
#                     $ the_person.change_slut_temp(2)
#                     $ the_person.change_happiness(5)
#                     mc.name "Get ready, I'm gonna cum!"
#                     "[the_person.title] is incoherent, and doesn't process your words."
#                     "You plunge deep into her ass and hold it there while you cum. She gasps in time with each new shot of hot semen inside of her."
#                     $ the_person.cum_in_ass()
#                     "You stand there for a minute, holding her hips in the air, you dick buried in her bowel as it softens. Eventually she speaks up."
#                     the_person.char "Wow... okay... I think I can stand now..."
#                     "You slowly let her down. Her legs buckle for a second, but she catches herself."
#                     "You see a faint trace of your semen running down the back of her leg."
#                     the_person.char "That was SO good. You'll be hearing from me again, I'm sure... I came so many times..."
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
#         the_person.char "That's it, cum with me!"
#         "You cum erupts in a torrent. You seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
#         $ the_person.change_happiness(5)
#         $ the_person.change_slut_temp(1)
#         $ the_person.cum_in_vagina()
#         "You wait until your orgasm has passed completely, then pull out and stand back. You cum leaks from her well used pussy."
#         "You take a moment to recover. Then you and [the_person.title] get cleaned up and dress. You quietly sneak out of the locker room."
#         return
#     elif the_person.effective_sluttiness() > 60:
#         the_person.char "Oh god... you should probably pull out but... it feels so good..."
#         "You briefly consider pulling out."
#         menu:
#             "Pull Out":
#                 "You pull out of [the_person.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
#                 the_person.char "Oh! It's so hot on my skin!"
#                 $ the_person.cum_on_ass()
#                 $ the_person.draw_person(position = "standing_doggy")
#                 "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
#                 "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the locker room."
#                 return
#             "Creampie":
#                 "Her pussy feels too good. You bottom out and cum, dumping wave after wave of your semen deep inside of her."
#                 "You seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
#                 $ the_person.change_happiness(5)
#                 $ the_person.change_slut_temp(1)
#                 $ the_person.cum_in_vagina()
#                 "You wait until your orgasm has passed completely, then pull out and stand back. You cum leaks from her well used pussy."
#                 "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the locker room."
#                 return
#     else:
#         "[the_person.title] suddenly moves her hips forward, your cock slides out of her."
#         the_person.char "Cum on my ass!"
#         "You stroke your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
#         $ the_person.cum_on_ass()
#         $ the_person.draw_person(position = "standing_doggy")
#         "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
#         "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the locker room."
#     return
#
# #label erica_cum_face(the_person):
# #    if the_person.obedience > 130:
# #        if the_person.effective_sluttiness() > 60:
# #            the_person.char "Do I look cute covered in your cum, [the_person.mc_title]?"
# #            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
# #        else:
# #            the_person.char "I hope this means I did a good job."
# #            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
# #    else:
# #        if the_person.effective_sluttiness() > 80:
# #            the_person.char "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
# #        else:
# #            the_person.char "Fuck me, you really pumped it out, didn't you?"
# #            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
# #    return
#
# label erica_cum_mouth(the_person):
#     if mc.location == gym or the_person.has_role(cum_internal_role):
#         if the_person.has_role(cum_internal_role) or the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("drinking cum") > 1:
#             the_person.char "Your cum tastes great [the_person.mc_title]! Thanks for giving me so much extra protein!"
#             "[the_person.possessive_title] winks at you as she swallows your load."
#         elif the_person.effective_sluttiness() > 50 or the_person.get_opinion_score("drinking cum") > 0:
#             the_person.char "Thanks [the_person.mc_title]. I could really use the extra protein after that workout!"
#         else:
#             "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
#             the_person.char "Thank you [the_person.mc_title]. It doesn't taste the best, but I could always use a little extra protein."
#     elif the_person.obedience > 130:
#         if the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
#             the_person.char "That was very nice [the_person.mc_title], thank you."
#         else:
#             "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
#             the_person.char "Thank you [the_person.mc_title], I hope you had a good time."
#     else:
#         if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 0:
#             the_person.char "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
#             "[the_person.title] licks her lips and sighs happily."
#         else:
#             the_person.char "Bleh, I don't know if I'll ever get used to that."
#     return
#
# #label erica_suprised_exclaim(the_person):
# #    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
# #    the_person.char "[rando]"
# #    return
#
# label erica_talk_busy(the_person):
#     if mc.location == gym:
#         the_person.char "Hey, I'm really sorry but I need to keep my workout going. Maybe another time?"
#     if the_person.obedience > 120:
#         the_person.char "Hey, I'm really sorry but I've got some stuff I need to take care of. Could we catch up some other time?"
#     else:
#         the_person.char "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
#     return
#
# #label erica_sex_strip(the_person):
# #    if the_person.effective_sluttiness() < 20:
# #        if the_person.arousal < 50:
# #            the_person.char "Let me get this out of the way..."
# #        else:
# #            the_person.char "Let me get this out of the way for you..."
# #
# #    elif the_person.effective_sluttiness() < 60:
# #        if the_person.arousal < 50:
# #            the_person.char "This is just getting in the way..."
# #        else:
# #            the_person.char "Ah... I need to get this off."
# #
# #    else:
# #        if the_person.arousal < 50:
# #            the_person.char "Let me get this worthless thing off..."
# #        else:
# #            the_person.char "Oh god, I need all of this off so badly!"
#
# #    return
#
# label erica_sex_watch(the_person, the_sex_person, the_position):
#     if the_person.effective_sluttiness() < the_position.slut_requirement - 20:
#         $ the_person.draw_person(emotion = "angry")
#         the_person.char "Holy shit, are you really doing this in front of everyone?"
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
#         the_person.char "Oh my god, you two are just... Wow..."
#         $ change_report = the_person.change_slut_temp(1)
#         "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() > the_position.slut_requirement and the_person.effective_sluttiness() < the_position.slut_cap:
#         $ the_person.draw_person()
#         the_person.char "Oh my god that's... Wow that looks...Hot."
#         $ change_report = the_person.change_slut_temp(2)
#         "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."
#
#     else:
#         $ the_person.draw_person(emotion = "happy")
#         the_person.char "Come on [the_person.mc_title], you can give her a little more than that. I'm sure she can handle it."
#         "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
#
#     return
#
# label erica_being_watched(the_person, the_watcher, the_position):
#     if the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #They agree you should give it to her harder
#         the_person.char "I can handle it [the_person.mc_title], you can be rough with me."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's super slutty and doesn't care what people think.
#         the_person.char "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."
#
#     elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #She's super slutty and encourages the watcher to be slutty.
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #She's into it and encouraged by the slut watching her.
#         the_person.char "Oh god, having you watch us like this..."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's into it but shamed by the prude watching her.
#         the_person.char "[the_person.mc_title], maybe we shouldn't be doing this here..."
#         $ the_person.change_arousal(-1)
#         $ the_person.change_slut_temp(-1)
#         "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."
#
#     else: #the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #They're both into it but not fanatical about it.
#         the_person.char "Oh my god, having you watch us do this feels so dirty. I think I like it!"
#         $ the_person.change_arousal(1)
#         $ the_person.change_slut_temp(1)
#         "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."
#
#     return
#
# label erica_work_enter_greeting(the_person):
#     if the_person.happiness < 80:
#         if the_person.obedience > 120:
#             "[the_person.title] gives you a curt nod and then turns back to what she was doing."
#         else:
#             "[the_person.title] glances at you when you enters the room then looks away quickly to avoid starting a conversation."
#
#     elif the_person.happiness > 120:
#         if the_person.effective_sluttiness() > 50:
#             "[the_person.title] looks up from her work when you enter the room."
#             the_person.char "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
#             "She smiles and winks, then turns back to what she was doing."
#         else:
#             "[the_person.title] turns to you when you enter the room and shoots you a smile."
#             the_person.char "Hey, good to see you!"
#
#     else:
#         if the_person.obedience < 90:
#             "[the_person.title] glances up from her work."
#             the_person.char "Hey, how's it going?"
#         else:
#             "[the_person.title] waves at you as you enter the room."
#             the_person.char "Hey, let me know if you need anything [the_person.mc_title]."
#     return
#
# label erica_date_seduction(the_person):
#     if the_person.effective_sluttiness() > the_person.love:
#         if the_person.effective_sluttiness() > 40:
#             the_person.char "I had a great time [the_person.mc_title], but I can think of a few more things we could do together. Want to come back to my place?"
#             # the_person.char "I had a great night [the_person.mc_title], would you like to come back to my place and let me repay the favour?"
#         else:
#             the_person.char "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
#             #the_person.char "I had a great night [the_person.mc_title], but I don't see why it should end here. If you want to come back to my place I can think of a few things we could do."
#     else:
#         if the_person.love > 40:
#             the_person.char "You're such great company [the_person.mc_title]. Would you like to come back to my place and spend some more time together?"
#         else:
#             the_person.char "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
#     return
#
# ## Role Specific Section ##
# label erica_improved_serum_unlock(the_person):
#     mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
#     the_person.char "Okay, how can I help?"
#     mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
#     "[the_person.title] smiles mischievously."
#     the_person.char "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is necessary if we want to see rapid results."
#     mc.name "Go on, I'm interested."
#     the_person.char "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
#     the_person.char "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
#     return

#</editor-fold>


init 2 python:
    #Erica specific python wrappers#
    def erica_on_love_path():
        return erica.event_triggers_dict.get("love_path", False)

    def erica_on_fwb_path():
        return erica.event_triggers_dict.get("fwb_path", False)

    def erica_on_hate_path():
        return erica.event_triggers_dict.get("hate_path", False)

    def erica_get_protein_day():
        return erica.event_triggers_dict.get("protein_day", 9999)
