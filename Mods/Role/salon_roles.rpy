# Creates a role for the salon and corresponding actions.
init 2 python:

    # Salon Manager Actions

    # salon_in_business_action = Action() # Opens a salon room in the business itself.

    def cut_hair_requirement(person):
        for role in person.special_role:
            if cut_hair_action in role.actions:
                return True
        else:
            return False

    def ophelia_gets_dumped_requirement(person):
        if day >= ophelia_get_day_met() + 4:
            return True
        return False

    def ophelia_coworker_conversation_overhear_requirement(person):
        if day >= ophelia_get_day_dumped() + 4:
            if person.location() == mall_salon:
                return True
        return False

    def ophelia_learn_chocolate_love_requirement():
        if salon_manager.get_opinion_topic("dark chocolate") == [2, True]:  #Only true if opinion is known
            return True
        return False

    def ophelia_give_chocolate_requirement():
        if ophelia_get_chocolate_gift_unlock():
            if mc.business.funds <= 50:
                return "Not enough money"
            if time_of_day < 1:
                return "Wait for shops to open"
            if time_of_day > 3 or day%7 == 6:
                return "Shops are closed"
            if ophelia_get_day_of_last_gift() == day:
                return "Already gifted today"
            else:
                return True
        return False

    def ophelia_ex_bf_phone_overhear_requirement(person):
        if day >= ophelia_get_day_dumped() + 14: #Wait atleast two weeks after getting dumped
            if person.location() == mall_salon:
                if person.sluttiness >= 20:
                    return True
        return False

    def ophelia_ex_bf_plan_pics_requirement(person):
        # prevent conflict with planned dates
        if mc.business.event_triggers_dict.get("date_scheduled", False) and (day%7 == 1 or day%7 == 4):
            return False
        if person.location() == mall_salon:
            if ophelia_get_ex_pics_planned() < 2:
                if ophelia_get_phone_convo_heard() > 0:
                    return True
        return False

    def ophelia_make_blowjob_pics_requirement():
        # prevent conflict with planned dates
        if mc.business.event_triggers_dict.get("date_scheduled", False) and (day%7 == 1 or day%7 == 4):
            return False
        if not salon_manager.location() == mall_salon:
            return False
        if time_of_day == 3:
            return True
        return False

    def ophelia_blowjob_pics_review_requirement(person):
        if not person.location() == mall_salon:
            return False
        if time_of_day < 4:
            return True
        return False

    def ophelia_revenge_date_plan_requirement(person):
        if person.sluttiness >= 40:
            if person.location() == mall_salon:
                if day >= ophelia_get_day_dumped() + 21:
                    return True
        return False

    def ophelia_revenge_date_requirement():
        if time_of_day == 3:
            if day % 7 == 6:  #Sunday
                return True
        return False

    def ophelia_revenge_aftermath_requirement(person):
        if day % 7 != 6:
            return True

    def ophelia_is_over_her_ex_requirement(person):
        if not ophelia_get_is_over_her_ex() and day >= ophelia_get_day_of_revenge_date() + 7:
            if person.location() == mall_salon:
                return True
        return False

    def ophelia_talk_about_candace_requirement(person):
        if ophelia_get_is_over_her_ex():
            if ophelia_get_can_talk_about_candace():
                if ophelia_get_will_help_candace():
                    return False
                else:
                    return True
        return False

    def ophelia_special_blowjob_requirement(person):
        if person.sluttiness >= 40:
            if person.energy > 60:
                return True
        return False

    def ophelia_increased_service_begin_requirement(person):
        if ophelia_get_is_over_her_ex():
            if person.sluttiness_tier >= 3:
                if person.location() == mall_salon:
                    return True
        return False

    def ophelia_choose_service_test_requirement():
        if mc.business.is_open_for_business():
            if ophelia_get_pubic_style_state() == 1:
                return True
            return "Only during business hours"
        return False

    def ophelia_add_service_full_body_massage_requirement(person):
        return False


    def create_ophelia_date_night_outfit(person):
        outfit = Outfit("Sexy Plum Shirt And Khaki Skirt")
        outfit.add_upper(strappy_bra.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_upper(belted_top.get_copy(),[.41, .16, .38, 0.95])
        outfit.add_lower(strappy_panties.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_lower(belted_skirt.get_copy(),[.77, .7, .56, 0.95], "Pattern_1", [.41, .16, .38, 0.95])
        outfit.add_feet(garter_with_fishnets.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(high_heels.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_accessory(lipstick.get_copy(),[.41, .16, .38, 0.52])
        outfit.add_accessory(heavy_eye_shadow.get_copy(),[.41, .16, .38, 0.52])
        person.apply_outfit(outfit)
        person.wardrobe.add_outfit(outfit)
        return

    def create_candace_date_night_outfit(person):
        outfit = Outfit("Candi Sexy Date Night")
        outfit.add_upper(thin_dress.get_copy(),[1.0, 0.73, 0.85, 0.95])
        outfit.add_upper(corset.get_copy(),[1.0, 0.73, 0.85, 0.95])
        outfit.add_lower(thong.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(garter_with_fishnets.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(pumps.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_accessory(heavy_eye_shadow.get_copy(),[1.0, 0.73, 0.85, 0.95])
        outfit.add_accessory(lipstick.get_copy(),[1.0, 0.73, 0.85, 0.50])
        person.apply_outfit(outfit)
        return

    cut_hair_action = Action("Change hairstyle", cut_hair_requirement, "cut_hair_label", menu_tooltip = "Customize hair style and color")
    ophelia_gets_dumped = Action("Ophelia gets dumped", ophelia_gets_dumped_requirement, "ophelia_gets_dumped_label", menu_tooltip = "Ophelia is back on the market")
    ophelia_coworker_conversation_overhear = Action("Ophelia talks with a co-worker", ophelia_coworker_conversation_overhear_requirement, "ophelia_coworker_conversation_overhear_label", menu_tooltip = "Ophelia vents to a co-worker")
    ophelia_give_chocolate = Action("Buy Ophelia Dark Chocolates", ophelia_give_chocolate_requirement, "ophelia_give_chocolate_label", menu_tooltip = "Buy Ophelia some chocolates. Can use to apply serum")
    ophelia_learn_chocolate_love = Action("Learn Ophelia loves chocolate", ophelia_learn_chocolate_love_requirement, "ophelia_learn_chocolate_love_label")
    ophelia_ex_bf_plan_pics = Action("Ask about Ex", ophelia_ex_bf_plan_pics_requirement, "ophelia_ex_bf_plan_pics_label", menu_tooltip = "See if you can help")
    ophelia_ex_bf_phone_overhear = Action("Overhear a phone conversation", ophelia_ex_bf_phone_overhear_requirement, "ophelia_ex_bf_phone_overhear_label")
    ophelia_make_blowjob_pics = Action("Make blowjob pictures", ophelia_make_blowjob_pics_requirement, "ophelia_make_blowjob_pics_label")
    ophelia_blowjob_pics_review = Action("Review blowjob pictures",  ophelia_blowjob_pics_review_requirement, "ophelia_blowjob_pics_review_label")
    ophelia_revenge_date_plan = Action("Ophelia asks you on a date",  ophelia_revenge_date_plan_requirement, "ophelia_revenge_date_plan_label")
    ophelia_revenge_date =  Action("Date with Ophelia",  ophelia_revenge_date_requirement, "ophelia_revenge_date_label")
    ophelia_revenge_aftermath = Action("Talk about what happened", ophelia_revenge_aftermath_requirement, "ophelia_revenge_aftermath_label")
    ophelia_is_over_her_ex =  Action("Ophelia finally moves on",  ophelia_is_over_her_ex_requirement, "ophelia_is_over_her_ex_label")
    ophelia_talk_about_candace =  Action("Talk about [candace.name]",  ophelia_talk_about_candace_requirement, "ophelia_talk_about_candace_label", menu_tooltip = "Tread carefully, this will be a sore subject")
    ophelia_increased_service_begin = Action("Ophelia increases services",  ophelia_increased_service_begin_requirement, "ophelia_increased_service_begin_label")
    ophelia_choose_service_test = Action("Pick employee for salon visit",ophelia_choose_service_test_requirement ,"ophelia_choose_service_test_label", menu_tooltip = "Select a girl you want to have her hair and pubic hair cut and styled")
    ophelia_add_service_full_body_massage = Action ("Ophelia wants to do massages", ophelia_add_service_full_body_massage_requirement, "ophelia_add_service_full_body_massage_label")

    salon_manager_role = Role("Salon Manager", [cut_hair_action, ophelia_ex_bf_plan_pics, ophelia_talk_about_candace])


label cut_hair_label(the_person):
    python:
        hair_style_check = the_person.hair_style.get_copy()
        pubes_style_check = the_person.pubes_style.get_copy()
    "You ask [the_person.title] if she could change her hairstyle a bit."
    $ the_person.draw_person()
    the_person.char "Sure, [the_person.mc_title], I don't see why not. Let me get my kit."

    call screen hair_creator(the_person, hair_style_check, pubes_style_check)

    $ the_person.draw_person(position = "stand2")
    if hair_style_check != the_person.hair_style or hair_style_check.colour != the_person.hair_style.colour or pubes_style_check != the_person.pubes_style or pubes_style_check.colour != the_person.pubes_style.colour: # Anything was changed
        the_person.char "Better now?"
        $ the_person.draw_person(emotion = "happy")
        mc.name "You look wonderful, [the_person.possessive_title]!"
    else:
        the_person.char "It seems you preferred my old look, [the_person.mc_title]."

    $ clear_scene()
    return

label ophelia_gets_dumped_label(the_person):
    "You walk into the salon. As you do, you can hear a man and a woman arguing. You look over and see [the_person.title] talking with a man you don't recognize."
    the_person.char "I don't understand. You mean... you don't want to see each other anymore?"
    "?????" "That's right. I think we should see other people."
    the_person.char "But... we were gonna move in together? What happened to that?"
    "He sighs and looks annoyed."
    "?????" "Well, obviously that isn't going to happen anymore."
    "It looks like [the_person.title] is struggling to hold back tears."
    the_person.char "I don't... I thought you were the one! 8 months we've been dating... And now... its over?"
    "?????" "I'm sorry. I need to get going. Take care [the_person.name]."
    "The man turns and walks off. [the_person.possessive_title] is in shock."
    $ the_person.change_happiness(-50)
    $ the_person.event_triggers_dict["dump_witnessed"] = 1
    $ the_person.event_triggers_dict["dump_day"] = day
    $ the_person.add_unique_on_room_enter_event(ophelia_coworker_conversation_overhear)
    return

label ophelia_coworker_conversation_overhear_label(the_person):
    $ ex_name = ophelia_get_ex_name()
    "You walk into the salon. You notice [the_person.title] talking to one of her co-workers, probably about her recent breakup."
    the_person.char "I know! But it gets worse! He is still friends with me on Facebook, you know?"
    the_person.char "This morning I got a notification, [ex_name] is now in a relationship. I was like... what the fuck?"
    the_person.char "So I look her up. Its the fucking secretary at his office! They're already planning a vacation together this summer!"
    "?????" "He's dipping his pen in company ink?"
    the_person.char "Exactly. Ugh, you should see her too. She's bimbo looking with tits like..."
    "[the_person.title] motions her hands in a way that makes it clear that this woman her ex is dating is very well endowed."
    "?????" "It's not her fault she's blessed in the chest."
    the_person.char "In her photo history was a pic of her in a bikini... there's absolutely no way they are real."
    "[the_person.title] and her co-worker continue their banter for a bit."
    $ the_person.event_triggers_dict["coworker_overhear"] = 1
    "Maybe you should chat with her for a bit? See if you can learn something about her that would give you an opportunity to cheer her up?"
    "You never know what you might learn with some small talk."
    # Should this just be a python block?
    $ the_person.event_triggers_dict["coworker_overhear"] = 1
    $ mc.business.mandatory_crises_list.append(ophelia_learn_chocolate_love)
    $ the_person.add_unique_on_room_enter_event(ophelia_ex_bf_phone_overhear)
    $ del ex_name
    return

label ophelia_learn_chocolate_love_label():
    $ the_person = salon_manager
    "You consider what you learned about [the_person.title] while talking to her previously."
    "She loves dark chocolate! Slowly a plan starts to form in your mind for how you can cheer her up."
    "You are positive there is a candy store at the mall. You could buy her some, then leave a note saying something tacky, like \'from your Secret Admirer\'."
    "You bet that would help her get her mind off her ex!"
    "... plus... if you have sole control over the chocolates... you could easily add some serum to them if you want..."
    $ the_person.event_triggers_dict["chocolate_gift_unlocked"] = 1
    $ mall.add_action(ophelia_give_chocolate)
    return

label ophelia_give_chocolate_label():
    $ the_person = salon_manager
    "You walk around the mall and find a candy store."
    if ophelia_get_num_chocolates_received() < 3:  #Only done this a couple of times or not at all
        "You look around the store for quite some time, looking for the perfect set of dark chocolates for [the_person.title]"
        "After several minutes, you find the right one. Perfect!"
    elif ophelia_get_num_chocolates_received() < 10:  #Getting to be a regular
        "You go to the section with the dark chocolates. You pick out [the_person.title]'s favorite."
    else:
        "As you walk into the store, the clerk recognizes you and waves."
        "You exchange a few pleasantries as you grab the usual box of dark chocolates that [the_person.title] loves."
    "You take the candy to the counter and purchase it."
    "You consider adding a serum to the candy before you leave it for [the_person.possessive_title]"
    menu:
        "Add a serum":
            "You decide to add a serum to the candy."
            call give_serum(the_person) from _call_ophelia_chocolates_with_serum_01
        "Leave alone":
            "You decide to leave the candy alone."
    "You write a quick note for her."
    if ophelia_get_knows_secret_admirer() and not ophelia_get_is_over_her_ex():
        "\'From your not so secret admirer <3\'"
    elif ophelia_get_is_over_her_ex():
        if not ophelia_get_knows_secret_admirer():
            "You consider for a while what to put down in your note. You decide eventually that it is time to come clean."
            #TODO add new event where next time you see her, Ophelia confronts you about being her secret admirer the whole time.
        "\'From [the_person.mc_title] XOXOXO\'"
    else:
        "\'From your secret admirer <3\'"
    "When you finish, you drop the chocolate in the salon mailbox."
    $ mc.business.change_funds(-50)
    $ the_person.event_triggers_dict["day_of_last_chocolate"] = day
    $ the_person.event_triggers_dict["chocolates_received"] += 1
    $ the_person.change_happiness(5)
    return

label ophelia_ex_bf_phone_overhear_label(the_person):
    "You walk into the salon. You see [the_person.title] with her back to you, conversing on the phone, loudly."
    $ the_person.draw_person(position = "walking_away")
    $ ex_name = ophelia_get_ex_name()
    the_person.char "I know, I know you are seeing someone else now, but its not like she has to know about it!"
    "There's a small pause."
    the_person.char "I'm just going through a dry patch right now and could really use some physical... attention..."
    "Another pause."
    the_person.char "But she won't find out! I promise my lips are sealed..."
    "Hmm, sounds like she is having some problems with an ex..."
    the_person.char "No no, [ex_name] don't go! I can't... Hello? FUCK!"
    "She slams her phone down on the counter."
    the_person.char "UGH! I can't believe him!"
    "Hmm, you wonder if you should talk to her about her boy problems..."
    $ the_person.event_triggers_dict["ex_phone_overhear"] = 1
    $ del ex_name
    return

label ophelia_ex_bf_plan_pics_label(the_person):
    if the_person.happiness < 100:
        mc.name "Sorry, I don't mean to intrude, but..."
        $ the_person.draw_person(emotion = "angry")
        "She snaps back at you."
        the_person.char "Well then you probably shouldn't. What happens between me and my ex is none of your business."
        $ the_person.change_obedience(-2)
        $ the_person.change_love(-2)
        "Yikes! Maybe you should try and find a way to cheer her up some before you talk to her about her ex again..."
        $ the_person.event_triggers_dict["pics_to_ex_plan_made"] = 1
        return
    elif ophelia_get_ex_pics_planned() == 0:
        mc.name "Sorry, I don't mean to intrude, but, I couldn't help overhearing part of your phone conversation."
        the_person.char "Ah jeez, sorry, I was getting pretty fired up there."
        mc.name "Having some problems with someone?"
        "She sighs before she starts to explain."
        the_person.char "Yeah, something like that. My boyfriend dumped me a few weeks ago. I keep trying to convince him we should umm, hang out again sometime, just for fun."
        the_person.char "But apparently he is already dating some slut he met at his job or something."
        the_person.char "I saw a picture of them on Facebook. She has huge tits, but she looks so dumb, I bet she doesn't give blowjobs like I do!"
        $ the_person.event_triggers_dict["pics_to_ex_plan_made"] = 1
    elif ophelia_get_ex_pics_planned() == 1:
        mc.name "Any luck with talking with your ex?"
        the_person.char "No, of course not. He's all HEAD OVER HEELS for the office bimbo he is seeing."
        the_person.char "I mean sure, she's got huge tits, but I bet she doesn't give head like I do!"
    "You carefully consider your response."
    menu:
        "Apologize":  #doesn't accomplish anything.
            mc.name "I'm sorry to hear that."
            the_person.char "Yeah well, what can you do? Anyway, is there something I can help you with?"
            "Hmm, you should think about what to say and talk to her again sometime..."
            return
        "Try making him jealous" if mc.int > 2:
            mc.name "Maybe you could try making him jealous? If you really are that good, do something to remind him what he is missing out on."
            the_person.char "Yeah... you might be right."
            "You lower your voice a bit."
            mc.name "I'm sure if your oral skills are as good as you boast, you'll be able to figure out an way to remind him."

        "Try making him jealous\n{color=#ff0000}{size=18}Requires: More Intelligence{/size}{/color} (disabled)" if mc.int<= 2:
            pass
        "Forget about him" if mc.charisma > 2:
            mc.name "When one door closes, often times another may open."
            the_person.char "Yeah... you might be right."
            "You lower your voice a bit."
            mc.name "I'm sure if your oral skills are as good as you boast, you'll find someone new soon enough, anyway."
        "Forget about him\n{color=#ff0000}{size=18}Requires: More Charisma{/size}{/color} (disabled)" if mc.charisma<= 2:
            pass

        "I don't believe you" if the_person.sluttiness > 40:
            mc.name "I don't know, just about every girl I've ever dated claimed to give the world's best blowjobs. Are you sure yours are so special?"
            the_person.char "Oh? Don't believe me?"
        "I don't believe you\n{color=#ff0000}{size=18}Not slutty enough to fall for this{/size}{/color} (disabled)" if the_person.sluttiness <= 40:
            pass

    "She considers what you said for a bit. Then, a light goes off and her eyes light up."
    the_person.char "Hey... I got an idea!"
    "She looks you over from head to toe before continuing."
    the_person.char "How would you like to help me do something to make him jealous?"
    mc.name "I'm listening."
    the_person.char "Why don't you come back later, after I close up?"
    "She lowers her voice to a whisper."
    the_person.char "I'll get on my knees and pretend like I'm sucking your dick. You can take some pictures, and then I'll accidentally send them to my ex..."
    mc.name "Hmm. That sounds like something that could work... but."
    the_person.char "But?"
    mc.name "What's in it for me?"
    "She groans."
    the_person.char "I don't know... I guess, if you take good pictures, I'll finish you off?"
    mc.name "Hmm... you know, I wasn't doing anything interesting tonight anyway. Okay, I'll swing by."
    the_person.char "Great!"
    "You get the details from her for when she closes up and promise to swing by later."
    the_person.char "See you then!"
    $ the_person.event_triggers_dict["pics_to_ex_plan_made"] = 2
    $ mc.business.mandatory_crises_list.append(ophelia_make_blowjob_pics)
    return

label ophelia_make_blowjob_pics_label():
    $ the_person = salon_manager
    "Remembering your promise to [the_person.title], you head over to the hair salon."
    $ mc.change_location(mall_salon)
    $ mc.location.show_background()
    $ the_person.draw_person()
    "[the_person.title] lets you in, then locks the front door behind her. It seems she is the only employee remaining."
    the_person.char "Hey! Thanks for coming back. So uhh... ready to get started?"
    mc.name "Absolutely."
    the_person.char "Good. To be honest I uhh, well, I've been kinda going through a dry spell, since my ex dumped me. I've been looking forward to this all day!"
    $ the_person.draw_person(position = "blowjob")
    $ the_person.change_arousal(10)
    "She gets down on her knees and reaches for your zipper."
    mc.name "So, am I supposed to be taking pictures?"
    the_person.char "Ah! Right! Here..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] jumps up and walks off. You see her reach into a purse sitting on the counter and pulls out her phone."
    "She comes back and messes with it for a minute."
    $ the_person.draw_person(position = "stand3")
    the_person.char "Here you go! God I can't believe I almost forgot."
    "You take the phone. She already has the camera app up."
    $ the_person.draw_person(position = "blowjob")
    the_person.char "Alright... where was I..."
    "Back on her knees, she reaches to you and eagerly starts opening your zipper. Her hand goes into your trousers and soon she is pulling your semi-erect cock out."
    the_person.char "Mmm, I love it when they are like this and you can feel them getting harder in your mouth..."
    $ the_person.change_arousal(15)
    $ the_person.break_taboo("sucking_cock")
    "Her lips part and you feel a very talented tongue and set of lips, working over the tip of your dick."
    "After teasing the tip for a bit, she opens wide and you feel her lips easily engulf your entire length. Her nose buries itself in your pubic hair."
    mc.name "Holy shit... you weren't lying..."
    "She gives a muffled mmmhmmmmm as her tongue dances along the underside of your now fully erect penis."
    "Phone in hand, you snap several picture of her working over your manhood."
    "For a second she pulls off."
    the_person.char "Hey, put it in video mode and take a quick one of this, my ex used to love it when I did this..."
    mc.name "Okay, one second."
    "You find the button and switch over to video mode. You hit the record button, then give her a nod."
    "She looks up at the phone, making perfect eye contact as she sticks her tongue out, and then easily slides your cock down her throat."
    "While that is impressive enough, her next move is amazing. With your hardness down her throat, she sticks her tongue out and begins to lap at the bottom of your testicles."
    mc.name "Fuck! Holy hell..."
    "She can't smile with her mouth full of meat, but you definitely see a hint of mischief in [the_person.possessive_title]'s eyes."
    $ the_person.change_arousal(15)
    "She keeps it up for several seconds, then slowly pulls off. You stop the recording."
    the_person.char "Did you get it?"
    mc.name "Yes, I definitely did."
    "Even as she talks to you, she continues to stroke you with her hand. She is truly talented at this..."
    the_person.char "Good! I'm surprised you didn't finish! My ex would blow his load pretty much every time I did that."
    the_person.char "But I bet he isn't my ex much longer... when I send him these pics he'll remember how I blew his mind and come around..."
    mc.name "If he doesn't, I'll happily help you make more pictures."
    the_person.char "Ha! I'm sure you would. Want me to do it again?"
    mc.name "Yes. It felt really good when you..."
    "Without waiting for you to finish your sentence, she opens wide, tongue out, and easily throats you. Her tongue is lapping at your heavy sac."
    "You feel a strange session along your length. Is she... is her throat contracting around you? Is that even possible? Where the hell did she learn to do THIS?"
    mc.name "Oh god I'm gonna cum!"
    "She quickly pulls off and starts rapidly stroking you with her hand."
    the_person.char "On my face! Give me your cum all over my face!"
    "You don't have the time to respond. Your body involuntarily begins pumping semen out at a frantic pace."
    $ the_person.cum_on_face()
    $ the_person.change_arousal(20)
    $ the_person.draw_person(position = "blowjob")
    "Spurt after spurt covers [the_person.possessive_title]'s face. You don't think you've ever cum so hard or so fast from a blowjob."
    the_person.char "Mmm, I forgot to tell you... I learned in beauty school that semen is great for your skin! Mmm and its nice and warm too..."
    $ the_person.draw_person()
    "As [the_person.title] stands up, you put your cock away. You see her slowly rubbing your cum into the skin on her face with two fingers..."
    mc.name "Okay, I admit it. You have the best mouth I have ever experienced."
    the_person.char "I told you! I guess years of practicing and being born without a gag reflex will do that though."
    "A hah! There's the secret... to just be born without a gag reflex..."
    "You feel amazing, but this is a bit awkward. You decide to offer to reciprocate."
    mc.name "So uhh, it just so happens I'm not too bad with my tongue, either."
    the_person.char "Is that so?"
    mc.name "I mean, it wouldn't be right for me to be the only one having a good time tonight, maybe I could return the favor?"
    the_person.char "Hmm..."
    if the_person.effective_sluttiness("licking_pussy") < 40 or mc.energy < 50:
        the_person.char "That's tempting but... I mean, I'm doing this to try and get with my ex! It wouldn't feel right to take things any further."
        mc.name "But who knows how long that'll be? Besides, he's off doing..."
        the_person.char "I know what he's doing. But its okay. He'll come back to me eventually. I can be patient."
        "It is clear you aren't going to be able to reason with her."
    else:
        the_person.char "I mean, I'm trying to get back with my ex..."
        mc.name "But who knows how long that'll be? Besides, he's off doing whatever with that other girl. Surely you could let yourself go and get a little relief your self?"
        the_person.char "Oh god, it would be really nice to not have to masturbate tonight."
        "She looks at you for a moment, then down at the ground."
        the_person.char "What did you have in mind, anyway?"
        mc.name "Well, you sucked my cock, why don't you let me lick your pussy?"
        the_person.char "Ok..."
        "She hesitates, but then slowly starts to strip down."
        $ the_person.strip_outfit(exclude_upper = True)
        $ the_person.update_outfit_taboos()
        call fuck_person(the_person, private = True, start_position = cunnilingus, skip_intro = False, position_locked = True) from _call_fuck_ophelia_1
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            the_person.char "Oh my god, I came so hard... you have no idea how bad I needed that!"
            $ the_person.change_love(5)
            $ the_person.change_happiness(10)
        else:
            the_person.char "Errr, I thought you said you were good at that? I didn't even finish..."
            "Her disappointment is obvious."
            the_person.char "Guess I'll just go home and masturbate... again..."
        "You clean yourself up."
    "[the_person.possessive_title] leads you to the front door."
    the_person.char "Thanks for your help tonight. I have a couple more things to do before I head home. Gonna send those pics out..."
    "You say goodbye and then walk out of the salon. You wonder what her ex will think when he gets those pictures..."
    $ the_person.event_triggers_dict["pics_to_ex_plan_made"] = 3
    $ the_person.event_triggers_dict["pics_to_ex_sent"] = 1
    $ the_person.add_unique_on_room_enter_event(ophelia_blowjob_pics_review)
    return

label ophelia_blowjob_pics_review_label(the_person):
    $ ex_name = ophelia_get_ex_name()
    "You walk into the salon. [the_person.title] notices you as you walk in."
    $ the_person.draw_person(emotion = "sad")
    the_person.char "Hello [the_person.mc_title]."
    mc.name "Hey. How'd it go? Get any response?"
    the_person.char "Ugh. See for yourself."
    "She pulls out her phone and shows you the text conversation."
    "It starts with a pic of [the_person.possessive_title] licking the tip of your cock."
    the_person.char "Had so much fun last night baby..."
    "Next is the video you took of her doing that move where she deepthroats and simultaneously licks your balls."
    the_person.char "OH SHIT, sorry, wrong person."
    ex_name "Just happy for you that you found someone."
    the_person.char "Well, he's just a friend. Remember when I used to do that for you?"
    ex_name "[the_person.name]... this isn't funny."
    the_person.char "What? It's nothing serious, you should come over tomorrow, I'll do the same for you."
    ex_name "I'm sorry, this is getting out of control. I'm sorry but I'm blocking you."
    the_person.char "Wow, after everything we've been through together? \n \'message not received\'"
    "...Ouch..."
    mc.name "[the_person.title]... I'm sorry."
    the_person.char "Yeah that's... not what I was hoping for. Oh well."
    the_person.char "I was really thinking that, just maybe."
    if ophelia_get_num_chocolates_received() > 3:
        the_person.char "I've been getting these sweets that someone had been leaving me in the mailbox. They are my favorite dark chocolate! I thought maybe it was him..."
        "Oh jeez, she is really hung up on this guy. Maybe you should be straight with her?"
    else:
        the_person.char "Sometimes guys do weird stuff. You know? I thought surely he'd realize what he has been missing out on."
    mc.name "I guess it just wasn't meant to be."
    the_person.char "Yeah, maybe. Who knows. Anyway if nothing else, I DID have a lot of fun making these pictures."
    mc.name "Yeah, I did too."
    $ the_person.draw_person(emotion = "happy")
    "[the_person.possessive_title] smiles for a moment as she looks at you."
    the_person.char "Yeah. I bet you did!"
    the_person.char "You know, I'm not sure I'm ready to give up on [ex_name] yet, but, in the mean time I suppose that makes me single so... you know..."
    mc.name "I'm not sure I do?"
    the_person.char "It would be nice to be able to blow off a little steam once in a while with someone. Someone like you."
    mc.name "I'm down for anything you want to blow. You were amazing."
    the_person.char "Yeah. It might take some convincing but... I have a feeling you might be able to convince me to do that again."
    "She gives you a wink."
    the_person.char "I'd better get back to work."
    $ the_person.event_triggers_dict["pics_to_ex_sent"] = 2
    $ the_person.event_triggers_dict["special_bj_unlock"] = 1
    $ the_person.add_unique_on_room_enter_event(ophelia_revenge_date_plan)
    $ del ex_name
    return

label ophelia_revenge_date_plan_label(the_person):
    $ ex_name = ophelia_get_ex_name()
    $ the_person.draw_person(emotion = "happy")
    "You step into the salon. No sooner have your eyes adjusted to the light then you see [the_person.title]"
    the_person.char "Ah! [the_person.mc_title]! Just the man I was hoping to see today."
    "A lump forms in your throat. You wander what she is going to rope you into."
    the_person.char "What plans do you have for Sunday night?"
    mc.name "Sunday? Oh, not much I guess..."
    the_person.char "Great! Guess what! I got a reservation at Rafferty's! It's a date, so dress nice! Pick me up at 6 o'clock sharp!"
    "Wow that's a pretty expensive steak house."
    mc.name "Wow, that sounds very nice..."
    "She cuts you off."
    the_person.char "Don't worry about the expenses, it'll be my treat, okay?"
    "Clearly there is something going on that she isn't tell you. Probably involving her ex boyfriend again?"
    mc.name "And... its going to be just me and you there?"
    the_person.char "Of course! What are you implying by that?"
    "She tries to smile sincerely, but she can't pull it off. You raise an eyebrow at her horrible acting."
    the_person.char "God... is it that obvious? [ex_name] is going to be there, on a date with his ho."
    mc.name "And how exactly do you know this?"
    "She groans audibly."
    the_person.char "Well, he sorta left himself signed on to my laptop and I've been reading some of the messages he's been sending Tits-for-Brains..."
    mc.name "That seems like a violation of privacy."
    the_person.char "Whatever, its his fault for not changing his passwords! That's like, break up 101, lock down everything."
    the_person.char "Anyway, I'm sorry, I know I'm kind of using you for this, but I'll pay for the meal and everything!"
    "You aren't really doing anything on Sunday anyway..."
    the_person.char "You'll get to escort me! I'm trying to make my ex jealous... I'll be dressed to impress!"
    "Yup! That seems totally worth it."
    mc.name "Okay, I'll do it. 6 o'clock here, right?"
    the_person.char "You got it! You're the best, [the_person.mc_title]!"
    $ the_person.draw_person(position = "kissing")
    "She steps up and gives you a quick peck on the cheek."
    $ the_person.event_triggers_dict["first_date_planned"] = 1
    $ mc.business.mandatory_crises_list.append(ophelia_revenge_date)
    $ del ex_name
    return

label ophelia_revenge_date_label():
    $ the_person = salon_manager
    $ ex_name = ophelia_get_ex_name()
    # WARNING: Make sure this label is only called once (or we end up with to Candace persons in the game)
    $ candace_mod_initialization()  #Create Candace (Candi), the office bimbo / slut
    #Slutty date outfits
    $ create_ophelia_date_night_outfit(the_person)
    $ create_candace_date_night_outfit(candace)

    if mc.location != mall_salon:
        "It's time for your date with [the_person.title]. You head over to the hair salon."
        $ mc.change_location(mall_salon)
        $ mc.location.show_background()
    else:
        "You hang around at the Salon until it is time for your date with [the_person.title]"
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ scene_manager.add_actor(the_person)
    "When you see her, you can't help but give her body your complete attention."
    mc.name "Wow, you look amazing."
    the_person.char "Thanks! I mean... you'd have to be crazy not to want some of this... right?"
    mc.name "I mean, regardless of what happens with your ex tonight, you don't have to go home alone."
    the_person.char "I appreciate the sentiment, but I'm sure once [ex_name] sees me in this he'll come back to his senses."
    "You have your doubts, but you know better than to voice them right now."
    the_person.char "Alright, let's get going. Don't want to be late!"
    $ mc.change_location(fancy_restaurant)
    $ mc.location.show_background()
    "You arrive at the restaurant. There are a few people in front of you, also waiting on their tables. It seems they are running a little bit behind tonight."
    the_person.char "Hey, I'm just gonna run to the lady's room to check my hair, I'll be right back!"
    mc.name "Sure thing."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    "You continue to wait for a few moments. You hear someone walk up behind you in line. At first, you pay the person no attention, but then you feel a tap on your shoulder."
    "You turn to the person."
    $ scene_manager.add_actor(candace, display_transform = character_left_flipped)
    candace.char "Hi! Sorry, I'm meeting someone here, could you please take me to my table?"
    "At first you just stand there dumbfounded. Jesus this woman is stacked."
    mc.name "I umm, don't work here. I'm waiting for a table also."
    candace.char "Oh! Silly me!"
    "She is giving you an obvious once over..."
    candace.char "You know, you're pretty cute. I'm [candace.title]!"
    mc.name "[candace.mc_title], nice to meet you."
    candace.char "Oh the pleasure is all mine!"
    "She giggles to herself... Wow, she is hot, but definitely not the brightest woman you've ever met."
    "After a moment, you hear a phone ring. It rings multiple times until suddenly she startles."
    candace.char "Oh! That's me!"
    "She picks up her phone. You overhear her half of the conversation."
    candace.char "Yes! HOW DID YOU KNOW I WAS IN LINE?"
    candace.char "You can see me? What? Are you peeping on me boss?"
    candace.char "You're already at the table? What? Look up? Now to the left?... What other left?"
    "This is almost physically painful for you to listen to."
    candace.char "Oh! I see you now! I'll be right there!"
    "She hangs up her phone."
    candace.char "Thank you, Maître d\', but I've found my table!"
    "She still thinks you work here. You mutter a reply."
    mc.name "Of course ma'am... enjoy your meal?"
    $ scene_manager.remove_actor(candace, reset_actor = False)
    $ candace.event_triggers_dict["day_met"] = day
    "Well, that was... interesting..."
    $ scene_manager.add_actor(the_person)
    the_person.char "Hey, I'm back!"
    "Thank god!"
    mc.name "I'm glad you're back. I just met, the dumbest bitch, I have ever met in my life."
    the_person.char "Is that so?"
    "She crinkles her nose."
    the_person.char "Black hair? Huge tits? Dumb as a bag of rocks?"
    mc.name "That's... yes that is completely accurate."
    the_person.char "Good, that means they are here!"
    "They?"
    "As you consider what she said, the last person between you and the host walks towards their table."
    "Host" "Hello there. Reservations?"
    the_person.char "Yes! Under [the_person.name]."
    "Host" "I see. Right this way then."
    "You walk into the restaurant. You get led past several dining guests, eventually to an empty table set for two."
    "You pull out [the_person.title]'s chair. When she sits down you push it in for her."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You sit down across from her. She is looking around the room. After a minute she spots her ex and points him out."
    the_person.char "There they are! Over there..."
    "You look in the direction that [the_person.title] is indicating."
    $ scene_manager.add_actor(candace, display_transform = character_left_flipped(xoffset = .1, yoffset = -.15, zoom = .5), position = "sitting")
    "Sure enough, her ex is sitting across from the woman you ran into earlier."
    "She must be incredible in bed, for him to be with her instead of [the_person.title], with the mental disadvantages she has."
    the_person.char "Alright, let's just play it cool for now. I'm sure he'll notice us eventually."
    "You decide to enjoy this wonderful meal and restaurant for now. You do your best to make conversation with [the_person.title], but you can tell she is a little distracted."
    "You share a nice bottle of wine. The salad is crisp and fresh. Soon your entrées arrive."
    "You steal a glance over at the other table now and then. Once in a while, [candace.title] gives you a wink, but [ex_name] seems to be completely oblivious."
    "[the_person.possessive_title]'s mood seems to be deteriorating by the minute."
    $ scene_manager.update_actor(candace, position = "walking_away")
    "You notice that [candace.title] gets up and goes to the lady's room. You nudge [the_person.title]."
    $ scene_manager.remove_actor(candace, reset_actor = False)
    the_person.char "Okay... I guess it's now or never... I'm gonna go talk to him!"
    "[the_person.title] gets up and walks towards the bathroom, but then stops next to her ex's table, pretending to be surprised to see him."
    $ scene_manager.update_actor(the_person, display_transform = character_left_flipped(xoffset = .1, yoffset = -.15, zoom = .5), position = "walking_away")
    the_person.char "[ex_name]! Oh I just noticed you there..."
    "You zone out a bit. Maybe it is the half a bottle of wine getting to you? Or you decide to just let their conversation be private."
    "Damn, that [candace.title] though. What you wouldn't give to get your hands on those tits..."
    "You spend some time daydreaming... how long? You aren't sure, but are quickly snapped back to attention when [the_person.title] sits down across from you."
    $ scene_manager.update_actor(the_person, display_transform = character_right, position = "sitting", emotion = "angry")
    "From the look on her face, you can guess how the conversation went."
    mc.name "Hey... you okay?"
    "You see a small tear at the corner of her eye."
    the_person.char "He accused me of spying on him... that... I mean yeah I kind of was but, I thought... I thought I could convince him to take me back..."
    "Oh boy."
    the_person.char "He said I just wasn't his type, that we were over, and that I need to just move on."
    "Here we go."
    the_person.char "I tried to reason with him... but I started getting mad! That airhead isn't anyone's type! He's just dating her for the sex..."
    "No shit."
    the_person.char "I don't know... I just can't believe it..."
    $ scene_manager.add_actor(candace, display_transform = character_left_flipped(xoffset = .1, yoffset = -.15, zoom = .5), position = "sitting")
    "You notice the aforementioned airhead return from the restroom. You can see that dessert has just arrived at the other table."
    "You see [ex_name] lean across the table and whisper something into [candace.title]'s ear. She gets a big smile and nods. You wonder what is going on over there..."
    $ scene_manager.update_actor(candace, position = "blowjob", display_transform = character_left_flipped(xoffset = .1, yoffset = -.15, zoom = .5))
    "You watch as [candace.title] gets down on her knees, then lifts the tablecloth up and disappears under it."
    $ scene_manager.remove_actor(candace, reset_actor = False)
    "You can hardly believe it... but you can just barely make out her legs just behind the tablecloth, on her knees, inches over towards [ex_name]."
    "You see [ex_name] pick up his phone and dial someone... a moment later [the_person.possessive_title]'s phone is ringing. Oh boy, you can see where this is going..."
    the_person.char "Hello? Why are you calling me?"
    the_person.char "What do you mean? I would have done anything for you... look at what?"
    "[the_person.title] turns and looks over at the other table. It takes her several moments to process what is going on."
    "When she does, she goes completely silent. She hangs up the phone."
    the_person.char "I umm... I'm not feeling well. I think I need to step outside for a minute..."
    mc.name "Go ahead."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    "[the_person.possessive_title] gets up and excuses herself."
    "While you imagined their previous conversation as a likely outcome of tonight's event, you would not have expected for them to do something so brazenly sexual in public."
    "For a moment, you consider alerting one of the staff to the current situation, but you decide against it. If that were you, you would appreciate the discretion, even if you don't agree with how [ex_name] used it against [the_person.title]."
    $ candace.cum_on_face()
    $ scene_manager.add_actor(candace, display_transform = character_left_flipped(xoffset = .1, yoffset = -.15, zoom = .5), position = "sitting")
    "You ask for the check. You decide to just go ahead and pick it up. As you are waiting, you notice the bimbo return to her seat. It is hard to tell from this distance, but assume the liquid on her face is cum."
    $ mc.business.change_funds(-200)
    $ scene_manager.remove_actor(candace)
    "You pay the tab, then head outside. You look around and eventually notice [the_person.title] around the corner."
    $ scene_manager.add_actor(the_person, emotion = "sad")
    mc.name "[the_person.title]... I'm sorry..."
    the_person.char "No... no... don't be. You've been very nice throughout this whole thing."
    "She takes a deep breath."
    the_person.char "It was so dumb. I just couldn't let go. I don't know why. He is such a jerk sometimes..."
    mc.name "Yeah to be honest that was kind of a dick move."
    the_person.char "Yeah, I guess sometimes it just takes something like this to realize it."
    mc.name "Can I take you home?"
    $ scene_manager.update_actor(the_person, emotion = "happy")
    "She gives you a slight smile. It warms your heart."
    the_person.char "Ah, you did say that, didn't you? That I wouldn't have to go home alone tonight?"
    mc.name "Only if you want."
    the_person.char "I think I would like that. I don't know what is going to happen after this, but, for tonight, I think I don't want to be alone."
    "Instead of answering with words, you just take her hand."
    $ the_person.event_triggers_dict["first_date_finished"] = 1
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    $ the_person.learn_home()
    "Soon, you are walking through her front door."
    the_person.char "Well, this is it! The spoils of a modest hair stylist... its about the best I can afford..."
    "Suddenly, she remembers the date."
    the_person.char "Oh god! I said I would pay for the date tonight."
    mc.name "Don't worry about it."
    the_person.char "I didn't... I couldn't possibly expect you to pay for it, after..."
    mc.name "I tell you what, have anything to drink around here?"
    the_person.char "Umm, I have some gin and some lemons. I love gin sours, so that's usually all I really keep around the house..."
    $ the_person.event_triggers_dict["favorite_drink"] = "gin sour"  #If not already set
    mc.name "That sounds great. Why don't we just have a couple of drinks and relax for a bit? We can call it even."
    the_person.char "Relax, huh? Alright, I suppose I could be convinced to go along with that."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title] disappears for a bit. You take off your shoes and get comfortable on her couch."
    "She returns with a couple of drinks."
    $ scene_manager.update_actor(the_person, position = "stand4")
    the_person.char "Two gin sours!"
    "You take your drink and make a toast."
    mc.name "Safety first! Never drink alone!"
    "You take a sip. Hey this is actually pretty good!"
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You do your best to make conversation, steering clear of the disaster that just happened. Gossip around the salon, you share some stories from your own personal life."
    "Finished with your drinks, you notice her biting her lip now and then, looking at you with a smile, then getting shy and looking away."
    "You stand up. [the_person.possessive_title] quickly stands also."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person.char "Is it time... are you going so soon?"
    mc.name "No, no, I was just stretching my legs for a moment."
    the_person.char "Oh! That's good! I thought..."
    "You stretch your arms up over your head."
    mc.name "Now I'm stretching my arms for a moment."
    "You slowly move towards her, you slowly let your arms come down in front of you. They come down over her shoulders."
    the_person.char "Mmm, I think I need to stretch a bit too!"
    $ scene_manager.update_actor(the_person, position = "kissing")
    "[the_person.title] wraps her arms around you. Your faces close, you lean in and kiss her."
    $ the_person.add_situational_slut("Date", 20, "There's no reason to hold back, he's here to fuck me!")
    "She kisses you back, responding immediately. Her body melts into yours."
    $ the_person.change_arousal(15)
    $ mc.arousal += 10
    "Your hands drops to her ass. You give it a squeeze, testing your limits with [the_person.possessive_title]. She sighs and gives a slight moan. She doesn't resist you at all."
    "You bring your other hand down and grab the other cheek. You pull her toward you and begin to grind your hips against her."
    "She is pressing her body against you."
    the_person.char "Oh god... I haven't... in a while..."
    "Sounds like she wants you! You pick her up and she gives a little yelp. Her nails are digging into your back."
    $ scene_manager.update_actor(the_person, position = "against_wall")
    "You start to walk down the hallway, but you've barely even entered it when you decide the bedroom is way too far away."
    "She moans loudly when you push her up against the hall wall. Her legs are spread now and she is grinding her crotch against yours."
    $ the_person.change_arousal(15)
    the_person.char "Oh god... can you... can you wrap it? I'm sorry I need you to wrap it up!"
    mc.name "Yeah, yeah."
    "You set her down for a second. You grab a condom from your wallet and start to put it on."
    $ scene_manager.strip_actor_outfit(the_person)
    $ mc.condom = True
    "When you finish, you notice [the_person.title] seems to be wearing less clothes..."
    the_person.char "Oh god, I need you so bad. Fuck me [the_person.mc_title]!"
    $ scene_manager.update_actor(the_person, position = "against_wall")
    "You pull her leg up. She is so wet you slide inside of her easily. You feel her salon manicured nails scratching down your back as you fill her up."
    $ the_person.break_taboo("vaginal_sex")
    the_person.char "Yes! Oh god this is so hot, why didn't I let you do this earlier. Oh god."
    call fuck_person(the_person, start_position = against_wall, skip_intro = True, asked_for_condom = True, prohibit_tags = ["Foreplay", "Oral", "Anal"]) from _ophelia_first_date_sex_scene_1
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person.char "Oh my god, I came harder than I ever did with [ex_name]. That was unbelievable!"
        $ the_person.change_love(5)
    else:
        the_person.char "Mmm that was so hot. I can't wait to do that again!"
    "As you both recover from your romp, there is an awkward silence in the room. You notice it is getting very late, and tomorrow is Monday."
    mc.name "I'm really sorry, I wish I could stick around longer, but I have to work in the morning..."
    $ scene_manager.update_actor(the_person, position = "stand3")
    the_person.char "Yeah, yeah, me too. I have to open the salon and all."
    the_person.char "Look... I don't know how we are going to feel about this in the morning, but thank you for tonight."
    the_person.char "You really helped me salvage a rough situation. I appreciate it."
    mc.name "Of course. I had a great time."
    $ the_person.outfit.add_upper(bath_robe.get_copy(), [.80, .26, .04, .7], "Pattern_1", [.15, .15, .15, .95])
    $ scene_manager.draw_scene()
    "You get dressed and she walks you to the door."
    the_person.char "Take care!"
    mc.name "Goodnight!"
    $ scene_manager.remove_actor(the_person)
    $ mc.change_location(downtown)
    $ downtown.show_background()
    "You walk home. As you are walking, you consider the events of the evening."
    "Tonight was a real breakthrough with [the_person.title]. She was a great fuck, hopefully you can get in her pants again soon."
    "The scene at the restaurant was crazy, with that bimbo, [candace.title] and [ex_name]. You'll have to keep an eye out for her. Maybe you'll run into her again?"
    $ the_person.clear_situational_slut("Date")
    $ the_person.add_unique_on_room_enter_event(ophelia_is_over_her_ex)
    $ the_person.add_unique_on_talk_event(ophelia_revenge_aftermath)
    $ del ex_name
    return

label ophelia_revenge_aftermath_label(the_person):
    $ the_person.draw_person()
    "You step up to [the_person.title]"
    mc.name "Hello"
    the_person.char "Hey..."
    "There is a bit of an awkward silence."
    the_person.char "So... I guess you want to talk about the other night..."
    mc.name "Only if you want to."
    the_person.char "I'm going through a lot of... confusing feelings right now."
    the_person.char "I really appreciate you putting up with me through all of this, but I think I just need a little time to myself right now."
    mc.name "I understand. I'll still be around if you need anything though."
    the_person.char "Of course! And feel free to send any of your employees my way. I'll still give them a discount!"
    the_person.char "Is there anything else you wanted to talk about?"
    return


label ophelia_special_blowjob_label(the_person):
    return

label ophelia_is_over_her_ex_label(the_person):
    the_person.char "Hey there! I was hoping I would see you today, [the_person.mc_title]!"
    $ the_person.draw_person(emotion = "happy")
    mc.name "Wow! I like the sound of that! And to what do I owe the pleasure?"
    the_person.char "Oh, not much, I just wanted to chat with you for a minute."
    mc.name "I'll always have a minute for you, [the_person.title]."
    the_person.char "Well, something amazing happened to me this morning."
    mc.name "Oh? What's that?"
    the_person.char "When I woke up, for the first time in a long time, I didn't wake up mad. Or angry. Or Sad. Or Depressed."
    the_person.char "I woke up... happy. And hopeful!"
    if the_person.love > 50:
        the_person.char "When I woke up, I wasn't thinking about my ex... I was thinking about you instead."
    else:
        the_person.char "When I woke up, I wasn't thinking about my ex. I was thinking about... well, just about everything else!"
    the_person.char "For the first time in a long time, I feel like I'm finally moving on. Like I'm finally getting over him."
    mc.name "That is great to hear! It makes me very happy to know that."
    the_person.char "I just want to say thank you for everything you've done! I'm not sure I would have made it through this without you."
    the_person.char "And even if I would have, you certainly made it a lot more fun."
    "She gives you a big wink."
    mc.name "Believe me, the pleasure was... maybe not all, but mostly mine."
    the_person.char "Don't sell yourself short! Anyway, I was thinking about how I could repay you. We are both business owners, and so I thought, maybe we could partner up a bit."
    mc.name "What do you have in mind?"
    the_person.char "Well, I'll give you some referral cards you put up in your business. If any of your employees wants to come get their hair cut or dyed, I'll give them half off!"
    mc.name "I know a few employees who will probably take you up on that."
    the_person.char "I'm also thinking about other ways to expand my business too. I'm sure in the future I'll be able to do more."
    mc.name "That sounds great. I really appreciate it."
    "From now on, hair cuts and styles are half price. Sounds like there may be more business opportunities with [the_person.title] in the future!"
    python:
        salon_style_cost = __builtin__.int(30)
        salon_dye_cost = __builtin__.int(15)

        salon_total_cost = salon_style_cost + salon_dye_cost
        the_person.event_triggers_dict["over_her_ex"] = 1
        the_person.add_unique_on_talk_event(ophelia_increased_service_begin)
    return

label ophelia_talk_about_candace_label(the_person):
    $ ex_name = ophelia_get_ex_name()
    "You take a deep breath. This is a touchy subject, so you need to approach this carefully."
    mc.name "So, I was wondering if I could talk to you for a few minutes about something."
    the_person.char "Sure! You know I always have time for you, [the_person.mc_title]."
    mc.name "Right, well, this might be kind of a sore subject, so please just hear me out before you rush to any judgement."
    the_person.char "I'm listening..."
    mc.name "OK, well, I found out some things about [ex_name], your ex? And they have me a little bit concerned."
    the_person.char "Concerned? Honey, me and him are over, there's no reason for you to be concerned."
    mc.name "For you, sure."
    the_person.char "Then for who? And how did you learn more about [ex_name], anyway?"
    mc.name "Well, you see, I've been talking a little with the girl he is dating, [candace.name]."
    $ the_person.draw_person(emotion = "angry")
    the_person.char "What the fuck? That two timing hussy? What the fuck have you been talking to her for?"
    mc.name "Just hear me out! You know how you said she is, well, dumb as a bag of rocks?"
    the_person.char "Well yeah..."
    mc.name "Well, it turns out, she pretty much is. At first I thought you were exaggerating. After talking to her, I found out that before she worked for your boyfriend, she used to work at a pharmaceutical company."
    the_person.char "What? That sounds crazy. How could someone like her work in that field?"
    mc.name "Well, I did some research into the company, and they went out of business about 6 months ago, after multiple lawsuits were filed."
    mc.name "I think maybe there was some kind of accident there, during research? That stunted her intelligence and made her into a bimbo..."
    the_person.char "Okay... I mean, that is totally not my area of expertise, so I guess I'll trust you when you say its possible."
    the_person.char "But what does that have to do with [ex_name]?"
    mc.name "Well, I think he has been taking advantage of her."
    $ the_person.draw_person(emotion ="sad")
    the_person.char "Taking advantage? Like how?"
    mc.name "Well, I found out, he is crazy controlling in their relationship. He controls everything from how she dresses to where she goes and does for fun."
    the_person.char "That... actually sounds a bit like him. He never did like it that I like to go camping and hiking on my days off by myself. Said I was probably out cheating on him."
    mc.name "Yeah... about that... that is called projection. It turns out he was dating [candace.name] while you two were also still together."
    the_person.char "Yeah. To be honest, I had kind of come to the same conclusion."
    mc.name "I'm sorry."
    the_person.char "Its okay. So, I guess I can understand why you want to help her, what is the plan?"
    mc.name "Well, right now, [ex_name] is paying her basically nothing. Labor laws would say her pay is illegally low."
    the_person.char "Oh god... [ex_name]... what are you doing?"
    mc.name "For the last few weeks, I've been slowly convincing her that she should quit, and if she does, I'll hire her at my company doing basically the same thing she is doing now, but for a fair wage."
    the_person.char "Ok... why are you talking to me about this again? Seems like you've got it all figured out."
    mc.name "[ex_name] has told her that if she quits, he is dumping her. But you and I both know, she isn't smart enough to secure her personal accounts and other things."
    mc.name "Remember when you found his Facebook logged on in your laptop? You said, locking down social media accounts is part of breakup 101!"
    the_person.char "Yeah, that's true."
    mc.name "I can get her job security, but I don't know how to handle [ex_name]. You have more experience with that!"
    the_person.char "So... let me get this straight."
    $ the_person.draw_person(emotion = "happy")
    "She takes a deep breath."
    the_person.char "You want me, to help the woman my ex boyfriend cheated on me with, to dump my ex, block him on social media, and if he comes after her, help blackmail him for breaking labor laws to keep him away from her?"
    mc.name "Yeah, that's pretty much... wait. Blackmail?"
    the_person.char "Yeah, I mean why else would you bring up the wage thing? Isn't that what you had in mind?"
    mc.name "I was just trying to give examples of how he had been taking advantage of her..."
    the_person.char "Alright, its obvious to me that you DO need my help. So fuck yeah, I'm in!"
    the_person.char "Go ahead and talk to her about it, and when you feel like she is ready, have her come visit me here. We'll get it all setup!"
    mc.name "Thanks [the_person.title]! I owe you one."
    the_person.char "Nah, I still owe you a couple of favors. This is just you calling one in."
    "Oh dear. It is a little scary how excited she is getting about this."
    mc.name "Alright, well hopefully it will be soon. I'll let you know!"
    $ the_person.event_triggers_dict["help_candace"] = 1
    $ del ex_name
    return

label ophelia_increased_service_begin_label(the_person):
    $ the_person.draw_person()
    the_person.char "Aha! Just the man I wanted to see."
    mc.name "Last time I heard that, we planned to crash..."
    the_person.char "YEAH, yeah I remember. Don't worry, this doesn't have anything to do with my ex."
    the_person.char "With my spare time, I've really been putting the extra effort into my business, you know?"
    the_person.char "Going the extra mile with every customer, that kind of thing."
    mc.name "Good, I bet that will pay off for you in the long run."
    the_person.char "Yeah... and I've been thinking. There is a place on the other side of town that does a different kind of hairstyling."
    mc.name "Oh?"
    the_person.char "Yeah, but they really only do it one way. It's called waxing, and a lot of girls get their privates done, for a variety of reasons."
    the_person.char "It is so... unimaginative! I've been considering offering a new service by request to do a little extra hair styling, you know, down there."
    the_person.char "I figure I'll call it a full body hair styling. I should probably offer to dye the hair too."
    mc.name "Huh. Having a professional do something like that might be very beneficial for some women."
    the_person.char "The problem is... I'm actually really scared to try it. Like, how would I even ask? Hey can I shave your pubes?"
    mc.name "Yes I can see why that might be an issue."
    the_person.char "So, I figure, you have a lot of female employees, right? I was wondering if you might know anyone who would be willing to try it out?"
    mc.name "I think I can figure something out."
    the_person.char "Great! No rush or anything, but when you think of someone, send them over and I'll take care of everything!"
    "You probably need an employee who is pretty slutty to do something like this... or very obedient? You guess you could just order a few of your employees to do it."
    "When you decide who, you should probably call them to your office first, so you can come over to the salon together."
    $ salon_manager.event_triggers_dict["full_style_state"] = 1
    $ office.actions.append(ophelia_choose_service_test)
    #TODO change variables
    return

label ophelia_choose_service_test_label():
    $ scene_manager = Scene() # make sure we have a clean scene manager

    $ ceo_office.show_background()
    "Sitting down, alone, in your office, you pull up the employee list. Who should you have be the test case for [salon_manager.title]?"
    python:
        able_person_list = []
        for person in mc.business.get_employee_list(): #TODO is there a method that grabs ENTIRE employee list?
            if person.core_sluttiness > 50:
                able_person_list.append(person)
            elif person.sluttiness > 20:
                if person.obedience > 150:
                    able_person_list.append(person)
    if __builtin__.len(able_person_list) == 0:
        "After going through the list, you decide there probably aren't any girls willing to have their pubic hair styled."
        "You should probably work on corrupting some of your employees before you try and send one to [salon_manager.title]."
    #$ able_person_list.insert(0, "Full Body Hairstyle Test")
    #$ able_person_list.append("Back")
    call screen enhanced_main_choice_display(build_menu_items([["Call in"] + able_person_list + ["Changed my mind"]]))
    $ the_person = _return
    $ del able_person_list
    if the_person == "Changed my mind":
        "You decide not to call an employee for the trial run of [salon_manager.possessive_title] full body hair styling right now."
        return
    "You call [the_person.title] down to your office. Soon she walks in your door."
    $ scene_manager.add_actor(the_person)
    the_person.char "Hey [the_person.mc_title], you wanted to see me?"
    mc.name "I have a quick favor to ask."
    mc.name "I have a friend who runs the salon over by the mall. She is considering offering a new service and is looking for someone to trial her service on."
    the_person.char "Oh? At a hair salon? That sounds nice, I'm about due to have it cut. What is the new service she is offering?"
    mc.name "Well, she is calling it a full body hair styling."
    the_person.char "Full body? So like... body hair also?"
    mc.name "Yeah, including the bikini area."
    if the_person.sluttiness > 50:
        the_person.char "Oh! That sounds great! It is such a pain trying to shave down there."
        the_person.char "When can we go?"
    else: #The person is not slutty but is here due to high obedience.
        the_person.char "Oh my... I'm not sure I feel comfortable having another woman cutting my hair down there..."
        mc.name "Well, not usually, I'm sure, but this would be a really big favor for me. Just this once?"
        the_person.char "Oh, well I supposed I could do it. For your sake of course!"
        the_person.char "So... when do we go?"
    mc.name "Let's head over now."
    $ mc.change_location(mall_salon)
    $ mc.location.show_background()
    "You go with [the_person.title] over to the salon."
    $ scene_manager.add_actor(salon_manager, display_transform = character_center_flipped)
    "[salon_manager.title] spots you as you walk in."
    salon_manager.char "Oh hey [salon_manager.mc_title]. What can I do for you?"
    mc.name "I brought you a customer, for that special service we talked about."
    "[salon_manager.title] notices [the_person.title] with you."
    if the_person == candace:
        salon_manager.char "Oh! Hello again. I suppose you would make a good candidate for this..."
        "[the_person.possessive_title] is looking around the salon, completely oblivious to your conversation with [salon_manager.title]"
    else:
        salon_manager.char "Oh! This is perfect! Hi I'm [salon_manager.name]."
        the_person.char "[the_person.name], nice to meet you."
    salon_manager.char "I have a private room all setup for when a girl comes in looking for the full body hair cut style and dye. Let's head back there."
    "You and [the_person.title] follow [salon_manager.possessive_title] to the private room. Its a great setup, with a very comfy looking styling chair."
    salon_manager.char "When I open it, I plan to have wine coolers or mimosas I can offer, along with a hot towel."
    mc.name "Nice, its a salon VIP lounge."
    salon_manager.char "Exactly! Alright dear, go ahead and strip down and we'll get started."
    if the_person.sluttiness > 50:
        the_person.char "This place is amazing..."
    else:
        "[the_person.title] looks to you, unsure about getting naked."
        mc.name "Don't worry she's a professional."
    "[the_person.title] gets naked."
    $ the_person.strip_outfit(exclude_feet = False)
    salon_manager.char "Alright, here's a catalogue with what I can do. Take a look and tell me what you would like!"
    python:
        hair_style_check = the_person.hair_style.get_copy()
        pubes_style_check = the_person.pubes_style.get_copy()
        salon_manager.event_triggers_dict["offers_full_style"] = True
    call screen hair_creator(the_person, hair_style_check, pubes_style_check)
    "You stay and observe as [salon_manager.title] does her work. She does an exceptional job."
    "When she finishes, you check out [the_person.title], while she examines herself in the mirror"
    if the_person == candace:
        the_person.char "Oh. My. God. The carpet even matches the drapes! This is great!"
    elif the_person.sluttiness > 50:
        the_person.char "Wow! Great job! I'm going to have to come here from now on."
    else:
        the_person.char "That was... an interesting experience. My hair looks great though! And everything matches."
        the_person.char "I think... I could get used to this."
    salon_manager.char "Great! Let me get you a card so you can make an appointment when you want to come back."
    $ scene_manager.update_actor(salon_manager, position = "walking_away")
    "As [salon_manager.possessive_title] goes to the other room to get her card, [the_person.title] gets dressed."
    $ the_person.apply_planned_outfit()
    $ scene_manager.update_actor(the_person)
    "Once dressed, she turns to you."
    the_person.char "This was great [the_person.mc_title]. Thanks for asking me to do this!"
    $ the_person.change_stats(happiness = 5, obedience = 5)
    $ scene_manager.update_actor(salon_manager, position = "stand3")
    "[salon_manager.title] returns and hands [the_person.possessive_title] her business card."
    salon_manager.char "Thanks again, both of you, for doing this. I think I'm going to move forward with adding the service to general customers!"
    salon_manager.char "From now on, if the girl wants me to, I'd be glad to give them the same treatment."
    mc.name "That sounds great. I'll definitely keep that in mind."
    "You turn to [the_person.title]"
    mc.name "You can head back to work. I'm not sure if I'm going to head back right away."
    the_person.char "Okay! See you later."
    $ scene_manager.remove_actor(the_person)
    "You say goodbye to [salon_manager.title] as well."
    $ scene_manager.remove_actor(the_person)
    "From now on, if a girl is slutty or obedient enough, when you schedule a haircut, you can also set a pubic hair style."
    $ salon_manager.event_triggers_dict["full_style_state"] = 2
    $ office.actions.remove(ophelia_choose_service_test)
    return # Where to go if you hit "Back".

label ophelia_add_service_full_body_massage_label(the_person):
    $ the_person.draw_person()
    the_person.char "Aha! Just the man I wanted to see."
    mc.name "For some reason everytime I hear that phrase, good things happen. What can I do for you [the_person.title]?"
    "She smiles wide at you."
    the_person.char "I have another idea for how I can expand my business again! I wanted to hear what you think about it again... and maybe provide another 'test subject'."
    mc.name "I'm listening. What's the idea?"
    "She takes a deep breath."
    the_person.char "Well... my full body hair styling has been a great success... especially with some of the girls from your office..."
    the_person.char "I was thinking about what I could do to take the service to the next level, you know. "
    return



##### Story variable python wrappers
#       These are solely to recall story variables

init 2 python:
    def ophelia_get_day_dumped():
        return salon_manager.event_triggers_dict.get("dump_day", 0)

    def ophelia_get_has_been_dumped():
        return salon_manager.event_triggers_dict.get("dump_witnessed", 0)

    def ophelia_get_coworker_overheard():
        return salon_manager.event_triggers_dict.get("coworker_overhear", 0)

    def ophelia_get_num_chocolates_received():
        return salon_manager.event_triggers_dict.get("chocolates_received", 0)

    def ophelia_get_chocolate_gift_unlock():
        return salon_manager.event_triggers_dict.get("chocolate_gift_unlocked", 0)

    def ophelia_get_day_of_last_gift():
        return salon_manager.event_triggers_dict.get("day_of_last_chocolate", 0)

    def ophelia_get_knows_secret_admirer():
        return salon_manager.event_triggers_dict.get("secret_admirer_known", 0)

    def ophelia_get_phone_convo_heard():
        return salon_manager.event_triggers_dict.get("ex_phone_overhear", 0)

    def ophelia_get_ex_pics_planned():
        return salon_manager.event_triggers_dict.get("pics_to_ex_plan_made", 0)

    def ophelia_get_ex_pics_sent():
        return salon_manager.event_triggers_dict.get("pics_to_ex_sent", 0)

    def ophelia_get_first_date_planned():
        return salon_manager.event_triggers_dict.get("first_date_planned", 0)

    def ophelia_get_first_date_finished():
        return salon_manager.event_triggers_dict.get("first_date_finished", 0)

    def ophelia_get_day_met():
        return salon_manager.event_triggers_dict.get("day_met", -1)

    def ophelia_get_ex_name():
        return salon_manager.event_triggers_dict.get("ex_name", "Gary")

    def ophelia_get_salon_and_spa_planned():
        return salon_manager.event_triggers_dict.get("salon_and_spa_planned", 0)

    def ophelia_get_salon_and_spa_finished():
        return salon_manager.event_triggers_dict.get("salon_and_spa_finished", 0)

    def ophelia_get_special_bj_unlocked():
        return salon_manager.event_triggers_dict.get("special_bj_unlock", 0)

    def ophelia_get_is_over_her_ex():
        return salon_manager.event_triggers_dict.get("over_her_ex", 0)

    def ophelia_get_can_talk_about_candace():
        return salon_manager.event_triggers_dict.get("talk_about_candace", 0)

    def ophelia_get_will_help_candace():
        return salon_manager.event_triggers_dict.get("help_candace", 0)

    def ophelia_get_day_of_revenge_date():
        return candace_get_day_met()

    def ophelia_get_pubic_style_state():
        return salon_manager.event_triggers_dict.get("full_style_state", 0)

    def ophelia_get_will_change_pubic_hair(): #Testing
        return salon_manager.event_triggers_dict.get("offers_full_style", False)

    def ophelia_person_wants_pubic_hair_included(person):  #Check for each individual person if they are willing to have their pubic hair styled.
        if person.sluttiness >= 50 or person.obedience >= 150:
            if ophelia_get_will_change_pubic_hair():
                return True

        return False


#TESTING FUNCTIONS#
#I am attempting to creat a unique person only position filter for determining what positions are available and when.

    def ophelia_foreplay_position_filter(foreplay_positions):
        return True

    def ophelia_oral_position_filter(oral_positions):
        if ophelia_get_special_bj_unlocked():
            filter_out = [blowjob, deepthroat, skull_fuck]
            if oral_positions[1] in filter_out:
                return False
            else:
                return True
        return False

    def ophelia_vaginal_position_filter(vaginal_positions):
        if ophelia_get_first_date_finished():
            return True
        return False

    def ophelia_anal_position_filter(anal_positions):
        if ophelia_get_first_date_finished():
            return True
        return False

    def ophelia_unique_sex_positions(person, prohibit_tags = []):
        positions = []
        if ophelia_get_special_bj_unlocked() and "Oral" not in prohibit_tags:
            positions.append([Ophelia_blowjob, 1])

        return positions
