#Mid game quest. Is available mid game, will help with profitability and seduction.
#Requires tier 2 serums unlocked. Starts with MC witnessing a TV commercial for "Female Viagra"
#AT first, MC blows it off as rediculous, but after considering, realizes that it could be real, considering what his company has made.
#NOTE: doses have a "use by" date, which is how we control the length of this quest.
#Orders 2 doses. First dose it used at the lab with the science leader. If there isn't one, prompt player to make one.
#MC discovers they actually work. Gives to science leader to reverse engineer, offers extra pay to her to do it on the side.
#Wait a few days. Science leader contacts MC and says is ready, swing by the lab after work.
#After work, 3 possible outcomes.
#low sluttiness, leader just gives you details of the serum.
#high sluttiness, low obedience- leader spikes MC drink. MC finds himself painfully aroused. Fucks
#High sluttiness, high obedience- Leader gives MC details, also says they are really fun to take. Offers to take one. If yes, marathon sex session.
#Once complete, adds the female viagra serum trait (Better name?)

# flags
# 1: Quest has been initiated X
# 9: MC has seen infomercial, decided its bullshit (Bad End)
# 11: MC has ordered
# 21: MC has received the pills. Discovered fast use by date.
# 29: MC doesn't use the drug in time. (Bad End)
# 31: Talked to science leader about testing, asking her to stay late.
# 39: HR has been fired. (BAD END)
# 41: Tested drug with science leader. No slutty enough for sex. Asked her to reverse engineer.
# 42: Tested drug with science leader. Had sex. Asked her to reverse engineer.
# 49: Tested drug with science leader. Decided drug is dangerous, do no pursue. (Bad End)
# 51: Science leader contacts MC, lets him know to swing by the lab after work.
# 101: Girl meets with MC, gives details. (Low slutty ending)
# 102: Girl meets with MC, spikes MC drink, sex(low obedience high slutty ending) #TODO this ending. For now only 103 ending
# 103: Girl meets with MC, gives details, offers to take one. said yes, sex marathon.. (high obedience, High slutty, good ending)
# 109: Girl meets with MC, gives details. MC declines having her take one.(neutral ending)
# Any 100 ending adds serum trait.


#TODO don't forget to add the quest to the list of quests in Side_quests_main.rpy

### The next three functions define the quest progress tracker, init requirements, and how we clean up after quest is done.
init 1 python:
    def setup_quest_arousal_serum():
        #Use this function to set quest specific variables.
        quest_arousal_serum.quest_event_dict["start_day"] = 9999
        quest_arousal_serum.quest_event_dict["expiration_day"] = 9999
        quest_arousal_serum.quest_event_dict["ready_day"] = 9999
        quest_arousal_serum.set_quest_flag(1)

        return

    def quest_arousal_serum_tracker():
        if quest_arousal_serum.get_quest_flag() <= 1:
            mc.business.add_unique_mandatory_crisis(quest_arousal_serum_intro)
        elif quest_arousal_serum.get_quest_flag() == 9:  #BAD END
            quest_arousal_serum.quest_complete = True
        elif quest_arousal_serum.get_quest_flag() == 11:
            mc.business.add_unique_mandatory_crisis(quest_arousal_serum_receive_drug)
        elif quest_arousal_serum.get_quest_flag() == 21:
            mc.business.head_researcher.add_unique_on_talk_event(quest_arousal_serum_arrange_test)
            mc.business.add_unique_mandatory_crisis(quest_arousal_serum_pills_expire)
        elif quest_arousal_serum.get_quest_flag() == 29:  #BAD END
            quest_arousal_serum.quest_complete = True
        elif quest_arousal_serum.get_quest_flag() == 31:
            mc.business.add_unique_mandatory_crisis(quest_arousal_serum_test)
            mc.business.add_unique_mandatory_crisis(quest_arousal_serum_fire_HR)
            remove_mandatory_crisis_list_action("quest_arousal_serum_pills_label")
        elif quest_arousal_serum.get_quest_flag() == 41:
            mc.business.add_unique_mandatory_crisis(quest_arousal_serum_researched)
        elif quest_arousal_serum.get_quest_flag() == 42:
            mc.business.add_unique_mandatory_crisis(quest_arousal_serum_researched)
        elif quest_arousal_serum.get_quest_flag() == 49:  #BAD END
            quest_arousal_serum.quest_complete = True
        elif quest_arousal_serum.get_quest_flag() >= 101:  #GOOD END
            quest_arousal_serum.quest_complete = True
        return

    def quest_arousal_serum_start_requirement():
        if mc.business.research_tier >= 2:
            return True
        return False

    def quest_arousal_serum_cleanup():
        remove_mandatory_crisis_list_action("quest_arousal_serum_pills_label")
        remove_mandatory_crisis_list_action("quest_arousal_serum_fire_HR_label")
        remove_mandatory_crisis_list_action("quest_arousal_serum_intro_label")
        remove_mandatory_crisis_list_action("quest_arousal_serum_receive_drug_label")
        remove_mandatory_crisis_list_action("quest_arousal_serum_researched_label")
        remove_mandatory_crisis_list_action("quest_arousal_serum_test_label")

        mc.business.head_researcher.remove_on_talk_event(quest_arousal_serum_arrange_test)
        quest_arousal_serum.quest_event_dict.clear()
        return

###Declare any requirement functions now
    def quest_arousal_serum_intro_requirement(the_person):
        return True

    def quest_arousal_serum_intro_requirement():
        if time_of_day == 4:
            return True
        return False

    def quest_arousal_serum_receive_drug_requirement():
        if time_of_day == 4:
            if day >= quest_arousal_serum.quest_event_dict.get("start_day", 0) + 2:
                return True
        return False

    def quest_arousal_serum_arrange_test_requirement(the_person):
        if mc.business.is_open_for_business():
            if day%7 == 4:
                return "You aren't evil enough to ask her to stay late on a Friday"
            else:
                return True
        return False

    def quest_arousal_serum_test_requirement():
        if time_of_day == 3:
            return True
        return False

    def quest_arousal_serum_researched_requirement():
        if time_of_day == 3:
            if day >= quest_arousal_serum.quest_event_dict.get("ready_day", 0):
                return True
        return False

    def quest_arousal_serum_pills_expire_requirement():
        if day >= quest_arousal_serum.quest_event_dict.get("expiration_day", 9999):
            return True
        return False

    def quest_arousal_serum_fire_HR_requirement():
        if mc.business.head_researcher == None:
            return True
        return False

###Functions unique to the quest
    def quest_arousal_serum_person_function_thing(the_person):
        return True



###Declare quest actions###
    quest_arousal_serum_intro = Action("Begin Arousal Serum Quest", quest_arousal_serum_intro_requirement, "quest_arousal_serum_intro_label")
    quest_arousal_serum_receive_drug = Action("Pills Arrive", quest_arousal_serum_receive_drug_requirement, "quest_arousal_serum_receive_drug_label")
    quest_arousal_serum_arrange_test = Action("Arrange Drug Test Tonight", quest_arousal_serum_arrange_test_requirement, "quest_arousal_serum_arrange_test_label")
    quest_arousal_serum_test = Action("Test Arousal Drug", quest_arousal_serum_test_requirement, "quest_arousal_serum_test_label")
    quest_arousal_serum_researched = Action("Arousal Drug Researched", quest_arousal_serum_researched_requirement, "quest_arousal_serum_researched_label")
    quest_arousal_serum_pills_expire = Action("Arousal Drug Expires Fail", quest_arousal_serum_pills_expire_requirement, "quest_arousal_serum_pills_expire_label")
    quest_arousal_serum_fire_HR = Action("Arousal Drug No HR Fail", quest_arousal_serum_fire_HR_requirement, "quest_arousal_serum_fire_HR_label")


#Quest Labels. This is the story you want to tell!
label quest_arousal_serum_init_label():
    $ setup_quest_arousal_serum()
    return

label quest_arousal_serum_intro_label():
    "As you are getting ready for bed, you notice [mom.title] sitting on the couch, watching some TV. It is currently a commercial."
    "TV" "Call now for this special offer! Pinkacia is being called the female Viagra by those who have tried it!"
    "TV" "Low libido? Just take this! You'll be grabbing your man and headed for the sack in no time!"
    "Wow, these late night TV commercials are awful. There's no way that stuff is legitimate."
    "... or is it? The work you have been doing is beyond what many people would have considered possible just a few years ago."
    "You decide to look it up. You head to your room and pull up the info on your PC."
    "The site is gaudy. Lots of claimed reviews call it a miracle drug. Taking a look, it is pretty pricey. Two doses for $100."
    menu:
        "Order it ($100)":
            $ mc.business.change_funds(-100)
            "What the hell. In terms of your business finances, $100 isn't that much. And who knows? Maybe it turns out to be legitimate."
            "You place an order with standard two day shipping."
            $ quest_arousal_serum.set_quest_flag(11)
            $ quest_arousal_serum.quest_event_dict["start_day"] = day
            pass
        "Sounds like bullshit":
            "You decide there is absolutely no way this stuff is legitimate. You close your browser and forget about it."
            $ quest_arousal_serum.set_quest_flag(9)
    return

label quest_arousal_serum_receive_drug_label():
    $ mom.draw_person()
    "As you are getting ready for bed, [mom.title] knocks on your door. You open it up."
    mom.char "Hey, you got this in the mail today. At first I thought it was junk, but it has your name on it, so I figured you could figure out what to do with it."
    "She hands you a small manila envelop."
    mc.name "Thanks [mom.title]"
    $ renpy.scene("Active")
    "She turns and walks way, closing your door behind her."
    "You open up the package. Its the two pills you ordered. The highly acclaimed Female Viagra."
    "You note on the package an expiration date. Holy hell, this stuff expires in a week?"
    "Hmm... what to do with this? With two doses, you figure you could test one dose, and if it works, use the second one to try and reverse engineer the drug."
    if mc.business.head_researcher == None:
        "If only you had a head researcher... Well, if you want to this stuff, you should make sure you appoint a new one."
    else:
        "Your head researcher, [mc.business.head_researcher.title], is the obvious choice for who to give it to. And if it turns out to work, she could use the other one to analyze it."

    $ quest_arousal_serum.quest_event_dict["expiration_day"] = day + 7
    $ quest_arousal_serum.set_quest_flag(21)
    return

label quest_arousal_serum_arrange_test_label(the_person):
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. I was wondering if you would be up for a little overtime tonight."
    the_person.char "Oh? Probably. I could use the extra cash. What do you need me to work on?"
    mc.name "I got my hands on a couple of pills that I want to test the effectiveness of."
    the_person.char "Okay. What do they propose to do?"
    mc.name "They function as some sort of blood flow increaser. Working similar to Viagra, but for females, to increase arousal and libido."
    the_person.char "Huh. Sounds interesting. Okay, I can do that. See you tonight?"
    mc.name "See you then."
    #We add the event here because if it happens to already be evening then the event won't proc if we wait for quest tracker to add it.
    $ mc.business.add_unique_mandatory_crisis(quest_arousal_serum_test)
    $ quest_arousal_serum.set_quest_flag(31)
    return

label quest_arousal_serum_test_label():
    $ the_person = mc.business.head_researcher
    $ the_person.arousal = 0 #Make sure we start at zero arousal for this event.
    if the_person == None: #we fired HR, bad end
        #TODO bad end
        pass
        return
    "After closing up the lab, it is time for you to test the pills with [the_person.title]."
    $ mc.business.r_div.show_background()
    $ the_person.draw_person(position = "stand2")
    mc.name "Hello, are you ready for the test?"
    the_person.char "Yes sir. I've got a camera set up, ready to observe the results. Am I right in assuming I'll be the one taking the drug?"
    mc.name "That is correct."
    if the_person.obedience < 120:
        the_person.char "Okay... since this is on overtime, I'll be getting paid accordingly, right?"
        mc.name "OF course, I'll add an extra $100 to your paycheck."
        $ mc.business.change_funds(-100)
    else:
        the_person.char "Okay, I suppose I'm willing to try it. What's the worst that could happen, right?"
    "You give her the pills. She takes one and puts the other in a sealed container."
    the_person.char "How long is it supposed to take for these to take effect?"
    mc.name "Well, to be honest, the packaging is a little ambiguous."
    the_person.char "... Of course..."
    "You spend some time with [the_person.title]. Not long after taking the pill, you start to notice some abnormal behavior."
    $ the_person.change_arousal(35)
    "Her cheeks are starting to get flushed."
    if the_person.tits_available():
        "You also notice her perky nipples have started to get hard. She is showing classic physical signs of arousal."
    else:
        "You also notice her nipples are hard and starting to show through her top. She is showing classic physical signs of arousal."
    mc.name "How are you doing, do you feel anything?"
    the_person.char "Yeah... actually... I'm feeling really warm."
    the_person.char "But not in a bad way. It's really nice. Actually it feels good..."
    $ the_person.change_arousal(20)
    $ the_person.draw_person(position = "stand4")
    "It seems like her breathing is starting to get kind of shallow and more rapid."
    mc.name "Are you starting to feel aroused?"
    the_person.char "Mmm... yeah... I think I'm starting to get wet!"
    mc.name "Why don't you get up on the desk here and let me examine you?"
    if the_person.vagina_visible():
        $ the_person.draw_person(position = "missionary")
        "[the_person.title] hops up on the table, lays back and spreads her legs."
    else:
        "[the_person.title] hops up on the table."
        the_person.char "Ohh, I'm getting so warm. I need to get this off..."
        $ the_person.strip_outfit()
        $ the_person.draw_person(position = "missionary")
        "She lays back and spreads her legs."
    $ the_person.change_arousal(20)
    "The lips of her vagina are puffy and swollen. Some of her lubrication has started to run down the sides of her legs."
    the_person.char "Oh my god... this is really intense. What is in this stuff?"
    "She starts to try to touch herself but you quickly stop her."
    mc.name "We need to observe the full effect of this."
    the_person.char "Oh god... oh my..."
    $ the_person.change_arousal(20) #This should put her at 95 arousal
    "After another minute, [the_person.title] is panting. She is starting to beg for release."
    the_person.char "Oh my god, please [the_person.mc_title]. PLEASE! Just put something in me. Anything!"
    "After another minute, it appears that the drug has brought her to the edge of climax, but can't quite put her over the top."
    the_person.char "Just a finger... please? I promise I'll do anything you want, just a finger..."
    "You decide that you have seen enough."
    mc.name "Good girl. Okay, let's relieve some of this for you."
    "You easily slide two fingers into her sopping wet cunt."
    $ the_person.change_arousal(20)
    the_person.char "Oh! Yes! Yes yes yes Yes YES YES YES!!!"
    $ mc.listener_system.fire_event("girl_climax", the_person = the_person)
    $ the_person.change_slut_temp(5)
    $ the_person.change_happiness(5)
    "Seconds later her body convulses as she orgasms. She moans a bunch of incomprehensible noises."
    $ the_person.change_arousal(-the_person.arousal/3)
    the_person.char "Oh my god... that felt so good."
    if the_person.sluttiness > 60:
        $ the_person.draw_person(position = "doggy")
        "[the_person.title] turns over onto her hands and knees. She starts to wiggle her ass at you."
        the_person.char "The drug hasn't fully wore off yet though. I could really use a nice, hard cock inside me right now."
        "You decide to do that. Watching her get off like that has got you hard and ready to go."
        call fuck_person(the_person, start_position = doggy, private= True, affair_ask_after = False) from _arousal_serum_fuck_test_1
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            $ the_person.draw_person(position = "missionary")
            "Completely spent, [the_person.title] sprawls out on the table."
            the_person.char "Fuck. I'd say that stuff works. I haven't had sex like that in... I don't know I've had sex that good before..."
        $ the_person.draw_person()
        "[the_person.title] slowly gets up."
        mc.name "Are you okay?"
        the_person.char "Amazing. I'll start working on the other pill... see if I can reverse engineer the effects."
        the_person.char "We might want to consider trying to tone down the effects a bit though. That was pretty excessive!"
        mc.name "Maybe some kind of slower release time frame? Something that would take effect over the course of the day, instead of inside an hour."
        the_person.char "Yeah... something like that. Hey I'm wore out. I'll get back to you about it, okay?"
        mc.name "Thanks."
        $ quest_arousal_serum.set_quest_flag(42)
        $ quest_arousal_serum.quest_event_dict["ready_day"] = day + 3
    else:
        $ the_person.draw_person()
        "[the_person.title] slowly gets up."
        the_person.char "Thanks... wow that stuff really works, doesn't it?"
        mc.name "Are you okay?"
        the_person.char "Yeah. I feel great. Definitely still feeling the effects of it, but I think I can manage now."
        the_person.char "Are you sure you want to me to reverse engineer this? I had fun, but this could be dangerous if it were used in the wrong situation."
        menu:
            "Reverse Engineer":
                mc.name "It's not for us to decide how it should be used. See if you can reverse engineer it."
            "Too Dangerous":
                mc.name "You know, I think you are right. This drug is dangerous. Thanks for testing it, but lets not pursue it anything further."
                the_person "Alright."
                $ quest_arousal_serum.set_quest_flag(49)

        the_person.char "I'll start working on the other pill... see if I can reverse engineer the effects."
        the_person.char "We might want to consider trying to tone down the effects a bit though. That was pretty excessive!"
        mc.name "Maybe some kind of slower release time frame? Something that would take effect over the course of the day, instead of inside an hour."
        the_person.char "Yeah... something like that. Hey I'm wore out. I'll get back to you about it, okay?"
        mc.name "Thanks."
        $ quest_arousal_serum.set_quest_flag(41)
        $ quest_arousal_serum.quest_event_dict["ready_day"] = day + 3
    "You and [the_person.possessive_title] leave the lab and close up for the day."
    return

label quest_arousal_serum_researched_label():
    $ the_person = mc.business.head_researcher
    if the_person == None: #we fired HR, bad end
        #TODO bad end
        pass
        return
    "After you have closed up, you get a text from your head researcher."
    the_person.char "Meet me down in the lab, I have good news."
    $ mc.business.r_div.show_background()
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. What have you got?"
    the_person.char "I've just finished up synthesizing our first batch of the arousal serum. I followed your idea, to make something that takes effect over time."
    the_person.char "The results have been mixed, but overall I think successful. When combined with one of our serums, the drug slowly builds arousal over the course of the day."
    the_person.char "However, due to the extended time it takes to act, often time the tests show that the person is able to calm down to ignore the full effect."
    the_person.char "Once we mixed it with our serums, however, we immediately noticed a pattern. The great the person's suggestability, the greater the arousal we were able to achieve."
    mc.name "Those sound like great results."
    the_person.char "Just let me know, and we can start to integrate it into our serums effective immediately."
    if the_person.sluttiness > 60:
        the_person.char "One question though... The second pill you let me have. I was able to analyze it without dissolving it."
        mc.name "So you still have it?"
        the_person.char "Yep! We had a lot of fun last time... want me to take it?"
        mc.name "Absolutely."
        the_person.char "You got it boss!"
        "She quickly pulls the pill out and takes it."
        the_person.char "Alright, I'm going to start cleaning up my workstation for the night, since it'll take a few minutes to take effect..."
        "[the_person.possessive_title] turns and starts to clean up her desk."
        $ the_person.draw_person(position = "walking_away")
        $ the_person.change_arousal(20)
        "She chats with you a bit as she does so. After a while though, it is beginning to get difficult for her to form complete sentences."
        $ the_person.change_arousal(20)
        the_person.char "Oh god, when this stuff hits you, it happens so fast..."
        $ the_person.change_arousal(20)
        $ the_person.draw_person(position = "standing_doggy")
        "She bends over her desk. You step behind her and grab her hips with your hands."
        mc.name "Are you okay?"
        "She lets out a moan."
        the_person.char "Now that your hands are on my hips I am... oh god..."
        $ the_person.change_arousal(20)
        the_person.char "I need... oh god."
        $ the_person.strip_outfit()
        $ the_person.draw_person(position = "standing_doggy")
        the_person.char "Oh fuck I need you! Fuck me [the_person.mc_title]! I need your cock inside me so bad!"
        call fuck_person(the_person, start_position = SB_doggy_standing, private= True, affair_ask_after = False) from _arousal_serum_fuck_test_2
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            "You fuck some sense back into your head researcher."
        $ the_person.draw_person()
    mc.name "Good work, [the_person.title]."
    "You leave the lab. You have unlocked a new serum trait."
    $ list_of_traits.append(arousal_serum_trait)
    $ quest_arousal_serum.set_quest_flag(101)

label quest_arousal_serum_pills_expire_label():
    if quest_arousal_serum.get_quest_flag() >= 101:
        return
    "The female viagra pills you ordered have expired. You decide the whole thing was probably bullshit anyway, and decide not to pursue it any further."
    $ quest_arousal_serum.set_quest_flag(29)
    return

label quest_arousal_serum_fire_HR_label():
    if quest_arousal_serum.get_quest_flag() >= 101:
        return
    "Unfortunately, since the head researcher position is no longer filled, you doubt you will be able do anything with the female viagra pills you ordered."
    $ quest_arousal_serum.set_quest_flag(39)


init python:
    def arousal_serum_function_on_turn(the_person, add_to_log):
        if the_person.arousal < the_person.suggestibility:
            the_person.change_arousal(__builtin__.min(15, the_person.suggestibility - the_person.arousal),add_to_log = False)
        return



    arousal_serum_trait = SerumTrait(name = "Female Viagra",
            desc = "Reverse engineered from the pills you ordered. Increases arousal over time, maxing out based on suggestability.",
            positive_slug = "+$20 Value, +15 Arousal over time",
            negative_slug = "+20 Serum Research",
            value_added = 20,
            research_added = 20,
    #     slots_added = a_number,
    #     production_added = a_number,
    #     duration_added = a_number,
            base_side_effect_chance = 30,
    #        on_apply = essential_oil_function_on_apply,
    #        on_remove = essential_oil_function_on_remove,
            on_turn = arousal_serum_function_on_turn,
    #     on_day = a_function,
    #     requires = [list_of_other_traits],
            tier = 2,
            start_researched =  True,
            research_needed = 800,
    #     exclude_tags = [list_of_other_tags],
    #     is_side_effect = a_bool)
        )
