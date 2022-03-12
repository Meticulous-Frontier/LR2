init 2 python:
    def aunt_drunk_cuddle_requirement(day_trigger):
        if day >= day_trigger and time_of_day == 4:
            return True
        return False

    def add_aunt_drunk_cuddle_action(day):
        aunt_drunk_cuddle_action = Action("Aunt Drunken Cuddle", aunt_drunk_cuddle_requirement, "aunt_drunk_cuddle_label", requirement_args = day)
        mc.business.mandatory_crises_list.append(aunt_drunk_cuddle_action)
        return

init 5 python:
    add_label_hijack("normal_start", "aunt_drunk_cuddle_inject")

label aunt_drunk_cuddle_inject(stack):
    python:
        # inject action once on new game start
        # it will wait here until it triggers, after that, it will be removed from the crisis list.
        # aunt moves in at latest at day 30, so trigger somewhere after that
        add_aunt_drunk_cuddle_action(32 + renpy.random.randint(6,12))
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label aunt_drunk_cuddle_label():
    python:
        scene_manager = Scene()
        the_person = aunt
        mc.change_location(kitchen)
        mc.location.show_background()
        scene_manager.add_actor(the_person, position = "sitting")
        scene_manager.add_actor(mom, position = "sitting", emotion = "happy", display_transform = character_center_flipped)

    "Before you go to bed, you come out into the kitchen to get a drink of water. [mom.possessive_title] and [the_person.title] are sitting there, drinking some wine."
    "It is pretty clear from their conversation that they have both had a lot to drink. They are cracking dirty jokes to each other."
    the_person "... So then I said, it's okay my partner is no good, I've got a good hand!"
    "[mom.title] laughs at [the_person.possessive_title]'s joke."
    mom "Ah that's too funny. Oh hi [mom.mc_title], your aunt and I were just having some wine before bed. Would you like some?"
    mc.name "No thanks, I'm just grabbing a glass of water."
    "[mom.possessive_title] looks at the clock and realizes how late it is."
    mom "Oh my. Yeah I'd better get to bed too. Good night!"
    $ scene_manager.update_actor(mom, position = "walking_away")
    the_person "Good night Jen!"
    mc.name "Night Mom."
    $ scene_manager.remove_actor(mom)
    the_person "Hey [the_person.mc_title], would you get me a glass of water too? I've had a LOT of wine and water helps keep you from getting hungover..."
    mc.name "Sure thing."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "You pour two glasses of water and hand one to [the_person.possessive_title]."
    the_person "It has been so nice of your family to let me and Gabrielle stay here for a bit. I hope we haven't been too much of a bother?"
    mc.name "Of course not. You are family, and honestly it is nice having you close by."
    the_person "That's sweet of you to say. Well, goodnight!"
    mc.name "Night."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title] turns and walks out of the kitchen. However, a moment louder you hear a loud yelp and the sound of glass breaking. You run into the living room."
    $ aunt_apartment.show_background()
    $ scene_manager.update_actor(the_person, position = "doggy")
    "[the_person.title] is on the floor on her hands and knees. Her water glass is shattered on the floor next to the couch, and the couch is soaked."
    mc.name "Are you okay?"
    the_person "I'm sorry! I slipped..."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "You quickly help her up."
    the_person "I'm so sorry... oh no the couch is soaked..."
    "She walks over to the couch and starts picking up the pieces of glass."
    the_person "I'll pay for the glass! I didn't mean to..."
    mc.name "It's okay, it's just a glass. I'm glad you aren't hurt."
    "You help [the_person.possessive_title] pick up the glass off the floor and grab a towel you lay down on the couch."
    the_person "Ahh, I guess I'll just be a little wet tonight."
    mc.name "Don't be crazy. You can sleep in my bed tonight."
    the_person "Oh my, I don't want to impose..."
    mc.name "You aren't. It's fine [the_person.title]. You would never get a decent night's sleep out here!"
    the_person "Well... okay... I'll go change into my pajamas..."
    $ scene_manager.remove_actor(the_person)
    "[the_person.title] grabs a couple things out of her suitcase and heads to the bathroom. You head to your room and quickly straighten up a bit."

    $ the_person.add_situational_slut("Drunk", 10, "More than a little tipsy.")
    $ mc.change_location(bedroom)
    $ bedroom.show_background()
    $ set_night_outfit(the_person)
    $ the_person.apply_outfit(the_person.personalize_outfit(the_person.outfit))

    "After a minute, [the_person.possessive_title] knocks on your door, then slowly enters."
    $ scene_manager.add_actor(the_person)
    the_person "I appreciate this [the_person.mc_title]... sometimes I get a little clumsy when I've had a couple drinks..."
    mc.name "It's fine, really!"
    $ scene_manager.update_actor(the_person, position = "missionary")
    "[the_person.title] lays down in your bed and starts to get comfortable."
    mc.name "I'm gonna go check the closet, pretty sure we have a sleeping bag or something in there."
    the_person "Huh? What do you need a sleeping bag for?"
    mc.name "I'll just sleep on the floor, I don't want..."
    the_person "No! Absolutely not. There's more than enough room here for both of us."
    mc.name "I don't want it to be awkward..."
    "[the_person.title] chuckles and shakes her head."
    the_person "[the_person.mc_title], it's just me, your aunt! It'll be fine. It might even be kind of nice... I haven't shared a bed with someone since your uncle..."
    "There is a bit of an awkward silence."
    the_person "It's nonsense. Now get in!"
    mc.name "Okay... it's okay... I usually just sleep in my underwear..."
    the_person "Whatever you need to feel comfortable!"
    "You take your shirt off, then undo your belt and slide your pants down. You can't help but notice [the_person.possessive_title] watching you, her eyes glancing down at your crotch..."
    $ the_person.change_slut(2)
    $ mc.change_locked_clarity(10)
    "You slide into bed next to her. You have to admit, the heat of her body is kind of nice. [the_person.title] rolls over on her side, her back facing you."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    mc.name "Goodnight."
    the_person "Goodnight..."
    "After a few minutes, [the_person.possessive_title] fidget around a bit then asks you."
    the_person "Hey... could you... you know... cuddle up with me?"
    mc.name "You... want me to be your big spoon?"
    the_person "Ahhh, sorry... that's silly..."
    "Before she can say anymore, you decide to do it anyway. You slide over behind her, putting your arm over her and pushing your body up against hers."
    the_person "Ahhh... that's nice. I haven't had a man hold me like this in so long..."
    $ mc.change_locked_clarity(10)
    "You lay there, holding [the_person.possessive_title] close for a while. However, soon the close proximity with her makes your loins start to stir."
    "You try to will it down, but it's no use."
    "Soon, you have a full fledged erection, pressing against [the_person.title]. There's no way she doesn't feel it."
    if the_person.sluttiness < 20:
        "After a while she turns her head back to you."
        the_person "Ahh... I'm sorry, I didn't realize... anyone still thought I was..."
        mc.name "[the_person.title] I'm sorry I didn't mean to it just happened..."
        the_person "It's okay! A young, virile man like you... I shouldn't be surprised."
        "You push your hips against her, grind yourself against her ass for a moment. She gasps, but quickly puts a stop to it."
        the_person "I'm sorry, that's enough for tonight..."
        "You roll on your back. It takes a while for your erection to finally subside, but you finally manage it and fall asleep."
        $ the_person.change_slut(3)
    else:
        "After a while she turns her head back to you."
        the_person "Ahh... I'm sorry, I didn't realize... anyone still thought I was... sexy..."
        "You start to apologize, but to your surprise, you feel her ass push back and start to grind against you."
        the_person "You're such a young... sexy... virile man... it's okay..."
        $ mc.change_locked_clarity(15)
        "You groan and start to grind your hips against hers. The curves of her ass feel amazing, your cock straining against your underwear as you grind against her."
        if the_person.sluttiness < 30:  # she finishes you like this.
            "Despite the clothing in the way, the naughtiness of grinding against your aunt while she grinds against you makes the situation so hot."
            "You grind eagerly against her for a few minutes, and soon you feel yourself getting ready to orgasm."
            $ mc.change_locked_clarity(20)
            mc.name "[the_person.title]... I'm..."
            the_person "Shhh... do it honey... I want you to..."
            "[the_person.possessive_title]'s soothing encouragement pushes you over the edge. You gasp and moan as you dump your load in your underwear against her."
            the_person "Ahhh... that's it baby..."
            "When you finish, you are exhausted. You consider getting up and cleaning up, but it feels to good to be up against [the_person.title]'s body still..."
            $ the_person.change_slut(5)
            $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_person)
            the_person "Goodnight..."
            mc.name "Goodnight..."
        else:
            "Its incredibly sexy to be up against [the_person.possessive_title], but soon the sensation of rubbing against your underwear is more frustrating than pleasurable."
            "[the_person.title] seems to be feeling the same way."
            the_person "Could you... you know... just... take it out? It feels good, but I'm getting a wedgie like this..."
            "You can't believe your ears. You quickly pull your cock out. As you are doing so, you feel [the_person.title] wiggling under the covers..."
            $ scene_manager.strip_to_vagina(person = the_person)
            "When you push up against her again, you realize she was taking her panties off! Your cock is now push up against [the_person.possessive_title]'s naked ass."
            $ mc.change_locked_clarity(20)
            the_person "Oh god... you feel so hard..."
            "She pushes back against you and begins to grind against you again. It feels amazing to push yourself between her soft ass cheeks."
            if the_person.sluttiness < 40:
                "You eagerly grind your crotch against her ass for a few minutes. The heat of her body feels amazing, and every little gasp and moan she makes turns you on."
                "Soon, you feel yourself getting ready to cum."
                $ mc.change_locked_clarity(20)
                mc.name "[the_person.title]... I'm..."
                the_person "Shhh... do it honey... I want you too..."
                "[the_person.possessive_title]'s soothing encouragement pushes you over the edge. You gasp and moan as you dump your load on her ass."
                $ the_person.cum_on_ass()
                $ scene_manager.update_actor(the_person, position = "walking_away")
                $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
                "Your sticky cum coats her ass, but she doesn't seem to mind."
                $ the_person.change_slut(5)
                the_person "Oh [the_person.mc_title]... I didn't know anyone... would feel that way about me..."
                "She grabs your arm and holds you close to her. You consider getting up to try and get cleaned up, but you are so tired..."
                the_person "Goodnight..."
                mc.name "Goodnight..."
            else:
                "You eagerly grind your crotch against her ass. She lets out a quiet gasp."
                the_person "Oh god... [the_person.mc_title]... you make me feel so sexy..."
                "She takes your hand and guides it to her chest. You start to grope her soft tits as you grind up against her."
                $ mc.change_locked_clarity(30)
                the_person "Do you mind if I... if I... get myself off too?"
                mc.name "Of course not! Do you want me...?"
                the_person "No! No it's okay, your hand is great right where it's at..."
                "You feel her shift a bit as she props one leg up a little bit. You can't see under the covers, but she gasps as she begins to touch herself."
                "You resume grinding your hips against her and fondling her tits as she plays with herself. Things really start to get heated."
                $ mc.change_locked_clarity(30)
                "After a few minutes, you feel yourself getting ready to cum."
                mc.name "[the_person.title]... I'm..."
                the_person "Oh god [the_person.mc_title]... me too! Cum for me!"
                "[the_person.possessive_title]'s encouragement pushes you over the edge. You gasp and moan as you dump your load on her ass."
                $ the_person.cum_on_ass()
                $ scene_manager.update_actor(the_person, position = "walking_away")
                $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
                "Your sticky cum coats her ass. Her body goes rigid as she has an orgasm of her own."
                $ the_person.have_orgasm()
                $ the_person.change_slut(5)
                the_person "Oh [the_person.mc_title]... I didn't know anyone... would feel that way about me..."
                "She grabs your arm and holds you close to her. You consider getting up to try and get cleaned up, but you are so tired..."
                the_person "Goodnight..."
                mc.name "Goodnight..."

    "You slowly drift off to sleep with [the_person.possessive_title]."
    $ scene_manager.clear_scene()
    $ the_person.clear_situational_slut("Drunk")

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_aunt_cuddle_01

    "You wake up, but [the_person.possessive_title] isn't there. You slowly get up and walk out of your room and into the kitchen."
    $ mc.change_location(kitchen)
    $ mc.location.show_background()
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(mom, position = "sitting", emotion = "happy", display_transform = character_center_flipped)
    "[mom.title] and [the_person.title] are sitting at the kitchen table, drinking some coffee."
    mom "Good morning!"
    the_person "Ahh, good morning [the_person.mc_title]..."
    mc.name "Good morning."
    "You notice as you walk past them to the coffee pot, your aunt is sneaking looks your way. Her cheeks a little rosey and blushed."
    $ mc.change_locked_clarity(5)
    "You pour yourself a cup and lean against the counter. The two sisters are chatting about plans for a bit, when suddenly [mom.possessive_title] stands up."
    mom "Well, I need to head out. Good luck with the apartment [aunt.name]!"
    the_person "Thank you! I'm sure we'll be out of here soon."
    $ scene_manager.update_actor(mom, position = "walking_away")
    "As [mom.possessive_title] leaves the room, an awkward silence ensues."
    $ scene_manager.remove_actor(mom)
    "You sip your coffee for a while, but finally [the_person.title] stands up and looks at you."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    the_person "[the_person.mc_title]... I appreciate what you did for me last night..."
    the_person "But umm... what happened after we went to bed... that was a one time thing, okay?"
    mc.name "It doesn't have to be."
    if the_person.sluttiness < 30:
        the_person "Yes... yes it does. I was drinking, I wasn't thinking about what I was doing, I just did whatever my body told me to..."
        mc.name "Are you saying you didn't enjoy it?"
        the_person "No, of course not. I definitely enjoyed it, but it can't happen again, okay?"
        mc.name "If that is what you want, [the_person.title]."
        the_person "What I want... right... that's what I want..."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title] slowly walks out of the kitchen, muttering to herself."
    else:
        "You can see her open her mouth to say something, but then she stops. She looks at you, as if searching for something."
        the_person "Are you just teasing me? I don't understand why you are doing this."
        mc.name "[the_person.title], you are a fun, sexy woman. I enjoy spending time with you, and after last night... honestly I want to do that again!"
        "She thinks for a moment, but then shakes her head."
        the_person "I wish we could too... but I'm sorry. You need to find someone else..."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.title] turns and walks out of the kitchen, muttering to herself."
    $ scene_manager.clear_scene()
    "You can't help but feel like you just made a lot of progress in your relationship with her, if you decide to pursue it."
    $ the_person.change_stats(happiness = 5, obedience = 5)
    return

label unit_test_role_aunt_enhanced():
    python:
        the_person = aunt
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 0
        the_person.sluttiness = 0
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
    "Unit test Aunt Cuddle scenario, sluttiness = 0"
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_01

    "Unit test Aunt Cuddle scenario, sluttiness = 10"
    python:
        the_person.situational_sluttiness = {}
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 10
        the_person.sluttiness = 10
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_02

    "Unit test Aunt Cuddle scenario, sluttiness = 20"
    python:
        the_person.situational_sluttiness = {}
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 20
        the_person.sluttiness = 20
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_03

    "Unit test Aunt Cuddle scenario, sluttiness = 30"
    python:
        the_person.situational_sluttiness = {}
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 30
        the_person.sluttiness = 30
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_04

    "Unit test Aunt Cuddle scenario, sluttiness = 40"
    python:
        the_person.situational_sluttiness = {}
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 40
        the_person.sluttiness = 40
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_05

    "Unit test Aunt Cuddle scenario, sluttiness = 50"
    python:
        the_person.situational_sluttiness = {}
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 50
        the_person.sluttiness = 50
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_06

    return
