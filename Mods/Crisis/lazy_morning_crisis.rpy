## Lazy Morning Crisis Mod by Starbuck

init -1 python:
    lazy_morning_mod_weight = 7 #Higher weight since it only occurs on weekends.

init 2 python:
    def lazy_morning_crisis_requirement():
        if mc_at_home() and time_of_day == 0:
            if mc.business.is_weekend():
                return True
        return False

    def lazy_morning_mod_initialization(self):
        pass #???? Do I need something here? TODO
        return
    #
    # lazy_morning_crisis_action = ActionMod("Lazy Morning", lazy_morning_crisis_requirement,"lazy_morning_crisis_action_label", initialization = lazy_morning_mod_initialization,
    #     menu_tooltip = "You sleep in.", category="Home", is_crisis = True, is_morning_crisis = True, crisis_weight = lazy_morning_mod_weight)
        #TODO this is disabled for now.
label lazy_morning_crisis_action_label:

    $ the_person = get_random_from_list(people_in_mc_home()) #Checks all the rooms in player's home
    if the_person is None:
        return

    "Your eyes slowly open when you alarm goes off. It feels like your arms weigh a hundred pounds each when you reach over and turn off your alarm."#TODO change pounds to kilos if metric is active.
    "It's time to get up... but is it really though? It's the weekend. There's probably some things you could get done."
    "But what sounds even better? You roll over and enjoy the comfort of your bed. You know you should get up, do something productive. But wouldn't you be more productive long term, if you got more sleep now?"
    "You finally stop reasoning with yourself and drift back to sleep."

    "You aren't sure how long it is, but you are startled awake when your bedroom door suddenly opens."
    the_person.char "[the_person.mc_title] I have a quick question about... OH!"
    $ the_person.draw_person()

    if the_person is mom:
        the_person.char "I'm sorry honey! I didn't realize you were sleeping in!"
    elif the_person is lily:
        the_person.char "What? You're still sleeping? You know the morning is almost over right?"
    elif the_person is aunt:
        the_person.char "I'm sorry, I didn't realize you weren't up yet!"
    elif the_person is cousin:
        the_person.char "Wow, I can't believe you're still sleeping. Up late beating off to crazy porn or something, ya perv?."
    else:
        the_person.char "I'm sorry [the_person.mc_title], I forgot its the weekend!"

    "She looks at you for a minute as she decides what to do."
    if the_person.sluttiness < 20: #Not slutty, she excuses herself.
        "She is looking at you pretty intently. You realize you have a crazy morning wood. Your cock is making the blanket tent and she is having trouble taking her eyes off of it."
        mc.name "What do you want?!?"
        the_person.char "I'm sorry, I wasn't staring... I mean... Ah!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] turns and flees your room, leaving you tired and frustrated. She was totally checking you out a little though..."
        $ the_person.change_slut_temp(3)

    elif the_person.sluttiness < 50: #She asks to join you and you wind up with mutual masturbation
        the_person.char "You look so comfy... I know this is kind of weird but, can I join you?"
        mc.name "You want to join me... in my bed?"
        "She stammers for a second."
        the_person.char "I mean, theres nothing wrong with a little cuddling, right? I don't have to I can leave..."
        "You cut her off mid sentence."
        mc.name "No! No come on in, you just surprised me when you walked in and I just woke up. I'd love to cuddle up for a bit."
        "[the_person.possessive_title] walks over to your bed. You lift up the covers and she slides in bed next to you."
        $ the_person.draw_person(position = "missionary")
        "She sighs as she lays on her back. You put your head on her shoulder and wrap one arm beneath her head under the pillow and the other across her stomach."
        if the_person is mom:
            the_person.char "I remember when it used to be you... climbing in to my bed in the middle of the night, scared from a bad dream."
        elif the_person is lily:
            the_person.char "God why is my brother so comfortable?"
        elif the_person is aunt:
            the_person.char "Its just nice, cuddling up with someone once in a while. My husband hadn't done anything like that in years before I left him..."
        elif the_person is cousin:
            the_person.char "Keep your hands above the clothing there now."
        else:                           #Someone else someday? A live in girlfriend maybe?
            the_person.char "Mmm, I love cuddling with you."

        "She sighs as she settles in beside you. Soon, however, you realize your morning wood is right up against her hip. You wonder if she can feel it."
        "You don't have to wonder for long, however."
        if the_person.has_taboo("touching_penis"):
            the_person.char "I'm sorry... were you having good dreams when I came in? I can feel you poking me."
            mc.name "I don't remember to be honest."
            the_person.char "Ah... I see."
            "She is silent for a moment."
            the_person.char "Do you think I could... you know... touch it? It feels so hot and hard!"
            "You are surprised. She's never done anything like this before!"
            mc.name "Yeah, that would be great..."
            "You feel her hand move down your body and then grasps your cock through your underwear. She gives it a few gentle strokes."
            mc.name "That feels great. You should put your hand down my underwear and do that."
            the_person.char "I'm not sure that's a good idea..."
            mc.name "Please? I want to feel how soft your hands are, it would be so nice..."
            "When she hesitates, you put your hand on hers. She doesn't resist as you move her hand up and then below the waistband on your underwear."
            "She gasps when she takes hold of your cock, her hand stroking your length."
            $ the_person.break_taboo("touching_penis")
        else:
            the_person.char "Having pleasant dreams when I woke you up?"
            "You feel her hand on your stomach and she starts to move it downwards. When she reaches your underwear, her hand goes between your skin and the band and you gasp when she grasps your cock."
        the_person.char "God its so hard..."
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
        else:
            if the_person.outfit.vagina_visible():
                "[the_person.title] arches her back when your hand reaches her pubic hair."
            else:
                "You slide your hand further down, under her clothes. [the_person.title] arches her back when your hand reaches her pubic hair."
        "You slide a finger between [the_person.possessive_title]'s labia, rubbing all along her slit."
        "She moans quietly as you slide two fingers into her cunt."
        "As your fingers push deep inside of her, she momentarily forgets to stroke you. You remind her by gently thrusting yourself into her hand and she immediately starts stroking you again."
        the_person.char "Mmmm, I love cuddling..."
        #TODO

    elif the_person.sluttiness < 75: #She asks to join you and you fuck
        pass
    else:    #She jumps you
        pass

    python:
        the_person.apply_planned_outfit()
        mc.location.show_background()
        renpy.scene("Active")
    return
