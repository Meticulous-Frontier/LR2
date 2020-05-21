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
            if mc.business.funds > 50:
                if time_of_day <= 3:
                    if ophelia_get_day_of_last_gift() == day:
                        return "Already gifted today"
                    else:
                        return True
                else:
                    return "Too late to give chocolates"
            else:
                return "Not enough money"
        return False

    def ophelia_ex_bf_phone_overhear_requirement(person):
        if day >= ophelia_get_day_dumped() + 14: #Wait atleast two weeks after getting dumped
            if person.location() is mall_salon:
                if person.sluttiness >= 20:
                    return True
        return False

    def ophelia_ex_bf_plan_pics_requirement(person):
        if person.location() is mall_salon:
            if ophelia_get_ex_pics_planned() < 2:
                if ophelia_get_phone_convo_heard() > 0:
                    return True
        return False

    def ophelia_make_blowjob_pics_requirement():
        if time_of_day == 3:
            return True
        return False

    def ophelia_blowjob_pics_review_requirement(person):
        if time_of_day < 4:
            return True
        return False

    def ophelia_special_blowjob_requirement(person):
        if person.sluttiness >= 40:
            if person.energy > 60:
                return True
        return False


    cut_hair_action = Action("Change hairstyle", cut_hair_requirement, "cut_hair_label", menu_tooltip = "Customize hair style and color")
    ophelia_gets_dumped = Action("Ophelia gets dumped", ophelia_gets_dumped_requirement, "ophelia_gets_dumped_label", menu_tooltip = "Ophelia is back on the market")
    ophelia_coworker_conversation_overhear = Action("Ophelia talks with a coworker", ophelia_coworker_conversation_overhear_requirement, "ophelia_coworker_conversation_overhear_label", menu_tooltip = "Ophelia vents to a coworker")
    ophelia_give_chocolate = Action("Buy Ophelia Dark Chocolates $50", ophelia_give_chocolate_requirement, "ophelia_give_chocolate_label", menu_tooltip = "Buy Ophelia some chocolates. Can use to apply serum")
    ophelia_learn_chocolate_love = Action("Learn Ophelia loves chocolate", ophelia_learn_chocolate_love_requirement, "ophelia_learn_chocolate_love_label")
    ophelia_ex_bf_plan_pics = Action("Ask about Ex", ophelia_ex_bf_plan_pics_requirement, "ophelia_ex_bf_plan_pics_label", menu_tooltip = "See if you can help")
    ophelia_ex_bf_phone_overhear = Action("Overhear a phone conversation", ophelia_ex_bf_phone_overhear_requirement, "ophelia_ex_bf_phone_overhear_label")
    ophelia_make_blowjob_pics = Action("Make blowjob pictures", ophelia_make_blowjob_pics_requirement, "ophelia_make_blowjob_pics_label")
    ophelia_blowjob_pics_review = Action("Review blowjob pictures",  ophelia_blowjob_pics_review_requirement, "ophelia_blowjob_pics_review_label")

    salon_manager_role = Role("Salon Manager", [cut_hair_action, ophelia_ex_bf_plan_pics])


label cut_hair_label(the_person):
    python:
        hair_style_check = the_person.hair_style #If hair_style_check is different than the_person.hair_style it means a "purchase" has been made.
        hair_color_check = the_person.hair_colour
    "You ask [the_person.title] if she could change her hairstyle a bit."
    $ the_person.draw_person()
    the_person.char "Sure, [the_person.mc_title], I don't see why not. Let me get my kit."

    call screen hair_creator(the_person, hair_style_check, hair_color_check)

    $ the_person.draw_person(position = "stand2")
    if hair_style_check != the_person.hair_style or hair_color_check != the_person.hair_colour: # Anything was changed
        the_person.char "Better now?"
        $ the_person.draw_person(emotion = "happy")
        mc.name "You look wonderful, [the_person.possessive_title]!"
    else:
        the_person.char "It seems you preferred my old look, [the_person.mc_title]."

    $ renpy.scene("Active")
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
    $ the_person.on_room_enter_event_list.append(ophelia_coworker_conversation_overhear)
    return

label ophelia_coworker_conversation_overhear_label(the_person):
    $ ex_name = ophelia_get_ex_name()
    "You walk into the salon. You notice [the_person.title] talking to one of her coworkers, probably about her recent breakup."
    the_person.char "I know! But it gets worse! He is still friends with me on Facebook, you know?"
    the_person.char "This morning I got a notification, [ex_name] is now in a relationship. I was like... what the fuck?"
    the_person.char "So I look her up. Its the fucking secretary at his office! They're already planning a vacation together this summer!"
    "?????" "He's dipping his pen in company ink?"
    the_person.char "Exactly. Ugh, you should see her too. She's bimbo looking with tits like..."
    "[the_person.title] motions her hands in a way that makes it clear that this woman her ex is dating is very well endowed."
    "?????" "It's not her fault she's blessed in the chest."
    the_person.char "In her photo history was a pic of her in a bikini... there's absolutely no way they are real."
    "[the_person.title] and her coworker continue their banter for a bit."
    $ the_person.event_triggers_dict["coworker_overhear"] = 1
    "Maybe you should chat with her for a bit? See if you can learn something about her that would give you an opportunity to cheer her up?"
    "You never know what you might learn with some small talk."
    # Should this just be a python block?
    $ the_person.event_triggers_dict["coworker_overhear"] = 1
    $ mc.business.mandatory_crises_list.append(ophelia_learn_chocolate_love)
    $ the_person.on_room_enter_event_list.append(ophelia_ex_bf_phone_overhear)
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
    $ mall.actions.append(ophelia_give_chocolate)
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

        "Try making him jealous\n{color=#ff0000}{size=22}Requires: More Intelligence{/size}{/color} (disabled)" if mc.int<= 2:
            pass
        "Forget about him" if mc.charisma > 2:
            mc.name "When one door closes, often times another may open."
            the_person.char "Yeah... you might be right."
            "You lower your voice a bit."
            mc.name "I'm sure if your oral skills are as good as you boast, you'll find someone new soon enough, anyway."
        "Forget about him\n{color=#ff0000}{size=22}Requires: More Charisma{/size}{/color} (disabled)" if mc.charisma<= 2:
            pass

        "I don't believe you" if the_person.sluttiness > 40:
            mc.name "I don't know, just about every girl I've ever dated claimed to give the world's best blowjobs. Are you sure yours are so special?"
            the_person.char "Oh? Don't believe me?"
        "I don't believe you\n{size=22}Not slutty enough to fall for this{/size} (disabled)" if the_person.sluttiness <= 40:
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
    the_person.char "Mmm, I forgot to tell you... I learned in beauty school. Semen is great for your skin! Mmm and its nice and warm too..."
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
    $ the_person.on_room_enter_event_list.append(ophelia_blowjob_pics_review)
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
    $ del ex_name
    return

label ophelia_special_blowjob_label(the_person):
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

    def ophelia_get_is_over_her_ex():  #TODO figure out where in the story she is officially over her ex and add the conditions here
        return False

    def ophelia_is_latest_version():
        if salon_manager.event_triggers_dict.get("ophelia_version", -1) < 1:   #Just increment the compare and set value when you have a new version
            salon_manager.event_triggers_dict["ophelia_version"] = 1
            return False
        return True


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
        return False

    def ophelia_anal_position_filter(anal_positions):
        return False

    def ophelia_unique_sex_positions(person, foreplay_positions, oral_positions, vaginal_positions, anal_positions):
        if ophelia_get_special_bj_unlocked():
            willingness = Ophelia_blowjob.build_position_willingness_string(person, ignore_taboo = True).replace("{size=22}", "{size=12}")
            oral_positions.append([willingness, Ophelia_blowjob])


        return [foreplay_positions, oral_positions, vaginal_positions, anal_positions]
