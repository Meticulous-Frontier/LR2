## Lazy Morning Crisis Mod by Starbuck

init 2 python:
    def lazy_morning_crisis_requirement():
        if mc.is_home() and mc.business.is_weekend():
            return True
        return False

    def lazy_morning_mod_initialization(self):
        pass #???? Do I need something here? TODO
        return
    #
    # lazy_morning_crisis_action = ActionMod("Lazy Morning", lazy_morning_crisis_requirement,"lazy_morning_crisis_action_label", initialization = lazy_morning_mod_initialization,
    #     menu_tooltip = "You sleep in.", category="Home", is_crisis = True, is_morning_crisis = True)
        #TODO this is disabled for now.
label lazy_morning_crisis_action_label():

    $ the_person = get_random_from_list(people_in_mc_home()) #Checks all the rooms in player's home
    if the_person is None:
        return

    "Your eyes slowly open when you alarm goes off. It feels like your arms weigh a hundred pounds each when you reach over and turn off your alarm."#TODO change pounds to kilos if metric is active.
    "It's time to get up... but is it really though? It's the weekend. There's probably some things you could get done."
    "But what sounds even better? You roll over and enjoy the comfort of your bed. You know you should get up, do something productive. But wouldn't you be more productive long term, if you got more sleep now?"
    "You finally stop reasoning with yourself and drift back to sleep."

    "You aren't sure how long it is, but you are startled awake when your bedroom door suddenly opens."
    the_person "[the_person.mc_title] I have a quick question about... OH!"
    $ the_person.draw_person()

    if the_person is mom:
        the_person "I'm sorry honey! I didn't realize you were sleeping in!"
    elif the_person is lily:
        the_person "What? You're still sleeping? You know the morning is almost over right?"
    elif the_person is aunt:
        the_person "I'm sorry, I didn't realize you weren't up yet!"
    elif the_person is cousin:
        the_person "Wow, I can't believe you're still sleeping. Up late beating off to crazy porn or something, ya perv?"
    else:
        the_person "I'm sorry [the_person.mc_title], I forgot it's the weekend!"

    "She looks at you for a minute as she decides what to do."
    if the_person.sluttiness < 30: #Not slutty, she excuses herself.
        "She is looking at you pretty intently. You realize you have a crazy morning wood. Your cock is making the blanket tent and she is having trouble taking her eyes off of it."
        mc.name "What do you want?!?"
        the_person "I'm sorry, I wasn't staring... I mean... Ah!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] turns and flees your room, leaving you tired and frustrated. She was totally checking you out a little though..."
        $ the_person.change_slut(2)
        $ mc.change_locked_clarity(10)

    elif the_person.sluttiness < 60: #She asks to join you and you wind up with mutual masturbation
        the_person "You look so comfy... I know this is kind of weird but, can I join you?"
        mc.name "You want to join me... in my bed?"
        "She stammers for a second."
        the_person "I mean, there's nothing wrong with a little cuddling, right? I don't have to I can leave..."
        "You cut her off mid sentence."
        mc.name "No! No come on in, you just surprised me when you walked in and I just woke up. I'd love to cuddle up for a bit."
        "[the_person.possessive_title] walks over to your bed. You lift up the covers and she slides in bed next to you."
        $ the_person.draw_person(position = "missionary")
        "She sighs as she lays on her back. You put your head on her shoulder and wrap one arm beneath her head under the pillow and the other across her stomach."
        $ mc.change_locked_clarity(15)
        if the_person is mom:
            the_person "I remember when it used to be you... climbing in to my bed in the middle of the night, scared from a bad dream."
        elif the_person is lily:
            the_person "God, why is my brother so comfortable?"
        elif the_person is aunt:
            the_person "It's just nice, cuddling up with someone once in a while. My husband hadn't done anything like that in years before I left him..."
        elif the_person is cousin:
            the_person "Keep your hands above the clothing there now."
        else:                           #Someone else someday? A live in girlfriend maybe?
            the_person "Mmm, I love cuddling with you."

        "She sighs as she settles in beside you. Soon, however, you realize your morning wood is right up against her hip. You wonder if she can feel it."
        "You don't have to wonder for long, however."
        if the_person.has_taboo("touching_penis"):
            the_person "I'm sorry... were you having good dreams when I came in? I can feel you poking me."
            mc.name "I don't remember to be honest."
            the_person "Ah... I see."
            "She is silent for a moment."
            the_person "Do you think I could... you know... touch it? It feels so hot and hard!"
            "You are surprised. She's never done anything like this before!"
            mc.name "Yeah, that would be great..."
            "You feel her hand move down your body and then grasps your cock through your underwear. She gives it a few gentle strokes."
            mc.name "That feels great. You should put your hand down my underwear and do that."
            the_person "I'm not sure that's a good idea..."
            mc.name "Please? I want to feel how soft your hands are, it would be so nice..."
            "When she hesitates, you put your hand on hers. She doesn't resist as you move her hand up and then below the waistband on your underwear."
            "She gasps when she takes hold of your cock, her hand stroking your length."
            $ the_person.break_taboo("touching_penis")
        else:
            the_person "Having pleasant dreams when I woke you up?"
            "You feel her hand on your stomach and she starts to move it downwards. When she reaches your underwear, her hand goes between your skin and the band and you gasp when she grasps your cock."
        the_person "God it's so hard..."
        $ mc.change_locked_clarity(30)
        "Her hand stroking your cock feels great, but soon you decide to make the pleasure mutual."
        if the_person.outfit.tits_visible():
            "With one hand, you reach over and start to grope [the_person.possessive_title]'s tits. Her breath catches in her throat when you pinch one of her nipples."
        else:
            "With one hand, you reach over and grope [the_person.possessive_title]'s tits through her clothing. She sighs and you can feel her nipple harden when you pull on it."
        "When you finish with her chest, you run your hand down her stomach. It slows when you reach the top of her hips."
        if the_person.has_taboo("touching_vagina"):
            if the_person.outfit.vagina_visible():
                "When your hand touches her pubic hair, she stops you."
            else:
                "You slide your hand further down, under her clothes. When your hand touches her pubic hair, she stops you."
            $ the_person.call_dialogue("touching_vagina_taboo_break")
            $ the_person.break_taboo("touching_vagina")
            "You move your fingers further down along [the_person.title]'s slit."
        else:
            if the_person.outfit.vagina_visible():
                "[the_person.title] arches her back when your hand reaches her pubic hair."
            else:
                "You slide your hand further down, under her clothes. [the_person.title] arches her back when your hand reaches her pubic hair."
        "You slide a finger between [the_person.possessive_title]'s labia, rubbing all along her slit."
        "She moans quietly as you slide two fingers into her cunt."
        "As your fingers push deep inside of her, she momentarily forgets to stroke you. You remind her by gently thrusting yourself into her hand and she immediately starts stroking you again."
        the_person "Mmmm, I love cuddling..."
        $ mc.change_locked_clarity(30)
        mc.name "I do to... especially this kind of cuddling."
        "[the_person.possessive_title] is getting wetter as you finger her. She is beginning to gasp and moan under hear breath."
        the_person "Oh [the_person.mc_title]..."
        "You feel her legs spread open a little wider, instinctively giving you better access with your fingers. Her soft hand stroking your cock feels great."



    elif the_person.sluttiness < 80: #She asks to join you and you 69
        the_person "That looks so comfortable... can I join you for a while?"
        mc.name "Sure. Always happy to cuddle up with you [the_person.title]!"
        $ the_person.draw_person(position = "kissing")
        "[the_person.possessive_title] lays down on your bed next to you, facing you. She drapes her arm over your body. She runs her hand up and down your chest a few times."

        if the_person is mom:
            the_person "You've been working so hard lately. I'm glad you are getting the chance to catch up on sleep!"
            "As she cuddles with you, her leg moves up and across your body. Soon her thigh is laying across your groin, your morning wood eagerly poking against her leg."
            the_person "Ohh... having pleasant dreams before I woke you up?"
        elif the_person is lily:
            the_person "I swear, you must be the most comfortable person on earth. You're kinda weird, but it's nice to be close to you like this bro..."
            "As she cuddles with you, her leg moves up and across your body. Soon her thigh is laying across your groin, your morning wood eagerly poking against her leg."
            the_person "Oh wow... you must have been having some good dreams when I woke you up!"
        elif the_person is aunt:
            the_person "It's so nice of you to let me come in a cuddle with you like this. You remind me a lot of my ex when we were younger and crazy about each other..."
            "As she cuddles with you, her leg moves up and across your body. Soon her thigh is laying across your groin, your morning wood eagerly poking against her leg."
            the_person "Mmm, he used to be so needy in the morning too. Were you having good dreams when I woke you up?"
        elif the_person is cousin:
            the_person "So, was it pretty good porn? Girls doing all kinds of naughty things?"
            "As she cuddles with you, her leg moves up and across your body. Soon her thigh is laying across your groin, your morning wood eagerly poking against her leg."
            the_person "Damn, you're hard as a rock! Did you dream about it all night too?"
        else:
            the_person "It's so nice to spend a weekend morning just cuddled up like this."
            "As she cuddles with you, her leg moves up and across your body. Soon her thigh is laying across your groin, your morning wood eagerly poking against her leg."
            the_person "Oh wow... you're so hard! Having good dreams when I woke you up [the_person.mc_title]?"
        mc.name "I don't remember to be honest, but having you so close sure isn't helping."
        the_person "Hmm... what do you say we start the day out right?"
        "[the_person.title] moves her leg back and take her arm off you. You feel her rustling around under the covers... removing some clothes?"
        $ the_person.outfit.strip_to_vagina()
        "Her hand comes back to your body, snaking its way down until it's on your cock."
        "She tugs at your shorts and you lift your butt up, letting her pull your clothes off easily. Her hand quickly returns to your morning wood, giving it a couple strokes."
        the_person "Mmm... it's so hard... I want to taste it!"
        mc.name "Why don't you hop on top of me and let me get a taste of you at the same time."
        the_person "Mmm... that sounds nice..."
        $ the_person.draw_person(position = "doggy")
    else:    #She fucks you
        pass

    python:
        the_person.apply_planned_outfit()
        mc.location.show_background()
        clear_scene()
    return
