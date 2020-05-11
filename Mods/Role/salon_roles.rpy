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

    def ophelia_ex_bf_phone_overhear_requirement(the_person):
        if day >= ophelia_get_day_met() + 4:
            if mc.location == mall_salon:
                return True
        return False

    def ophelia_ex_bf_plan_pics_requirement(the_person):
        if mc.location == mall_salon:
            if ophelia_get_ex_pics_planned() < 2:
                if ophelia_get_phone_convo_heard() > 0:
                    return True
        return "Testing"

    def ophelia_make_blowjob_pics_requirement():
        if time_of_day == 3:
            return True
        return False

    def ophelia_blowjob_pics_review_requirement(): #Disabled for now
        return False


    cut_hair_action = Action("Change hairstyle", cut_hair_requirement, "cut_hair_label", menu_tooltip = "Customize hair style and color")
    ophelia_ex_bf_plan_pics = Action("Ask about Ex", ophelia_ex_bf_plan_pics_requirement, "ophelia_ex_bf_plan_pics_label", menu_tooltip = "See if you can help")
    ophelia_ex_bf_phone_overhear = Action("Overhear a phone conversation", ophelia_ex_bf_phone_overhear_requirement, "ophelia_ex_bf_phone_overhear_label")
    ophelia_make_blowjob_pics = Action("Make blowjob pictures", ophelia_make_blowjob_pics_requirement, "ophelia_make_blowjob_pics_label")

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

label ophelia_ex_bf_phone_overhear_label(the_person):
    "You walk into the salon. You see [the_person.title] with her back to you, conversing on the phone, loudly."
    $ the_person.draw_person(position = "walking_away")
    $ OP_ex_name = ophelia_get_ex_name()
    the_person.char "I know, I know you are seeing someone else now, but its not like she has to know about it!"
    "There's a small pause."
    the_person.char "I'm just going through a dry patch right now and could really use some physical... attention..."
    "Another pause."
    the_person.char "But she won't find out! I promise my lips are sealed..."
    "Hmm, sounds like she is having some problems with an ex..."
    the_person.char "No no, [OP_ex_name] don't go! I can't... Hello? FUCK!"
    "She slams her phone down on the counter."
    the_person.char "UGH! I can't believe him!"
    "Hmm, you wonder if you should talk to her about her boy problems..."
    $ the_person.event_triggers_dict["ex_phone_overhear"] = 1
    $ del OP_ex_name
    return

label ophelia_ex_bf_plan_pics_label(the_person):
    if ophelia_get_ex_pics_planned() == 0:
        mc.name "Sorry, I don't mean to intrude, but, I couldn't help overhearing part of your phone conversation."
        the_person.char "Ah geeze, sorry, I was getting pretty fired up there."
        mc.name "Having some problems with someone?"
        "She sighs before she starts to explain."
        the_person.char "Yeah, something like that. My boyfriend dumped me a couple months ago. I keep trying to convince him we should umm, hang out again sometime, just for fun."
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

        "Try making him jealous\n{size=22}Requires: More Intelligence{/size} (disabled)" if mc.int<= 2:
            pass
        "Forget about him" if mc.charisma > 2:
            mc.name "When one door closes, often times another may open."
            the_person.char "Yeah... you might be right."
            "You lower your voice a bit."
            mc.name "I'm sure if your oral skills are as good as you boast, you'll find someone new soon enough, anyway."
        "Forget about him\n{size=22}Requires: More Charisma{/size} (disabled)" if mc.charisma<= 2:
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
    the_person.char "I'll get on my knees and pretend like I'm sucking your dick. You can take some pictures, and then I'll accidentily send them to my ex..."
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
    "After teasing the tip for a bit, she opens wide and you feel her lips easily engulf your entire lenght. Her nose buries itself in your pubic hair."
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
    the_person.char "Good! I'm surprised you didn't finish! My ex would blow his load pretty much everytime I did that."
    the_person.char "But I bet he isn't my ex much longer... when I send him these pics he'll remember how I blew his mind and come around..."
    mc.name "If he doesn't, I'll happily help you make more pictures."
    the_person.char "Ha! I'm sure you would. Want me to do it again?"
    mc.name "Yes. It felt really good when you..."
    "Without waiting for you to finish your sentence, she opens wide, tongue out, and easily throats you. Her tongue is lapping at your heavy sac."
    "You feel a strange session along your length. Is she... is her throat contracting around you? Is that even possible? Where the hell did she learn to do THIS?"
    mc.name "Oh god I'm gonna cum!"
    "She quickly pulles off and starts rapidly stroking you with her hand."
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
    return

label ophelia_blowjob_pics_review_label():
    pass
    #TODO pick up the story from here!
    return


##### Story variable python wrappers
#       These are solely to recall story variables

init 2 python:
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
