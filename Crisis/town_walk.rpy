## Town walk Crisis Mod by Tristimdorion
# Based on the Pilotus13 Vanilla extension
init -1 python:
    town_walk_mod_weight = 5

init 2 python:
    def town_walk_crisis_requirement():
        if not mc.business.is_weekend(): # we only take a lunch break on weekdays
            if time_of_day == 2:
                return True
        return False

    town_walk_crisis = ActionMod("Town Walk Crisis",town_walk_crisis_requirement,"town_walk_action_description", 
        menu_tooltip = "On occasion you take an afternoon stroll through town, someone did not close their bedroom curtains.")
    crisis_list.append([town_walk_crisis, town_walk_mod_weight])

label town_walk_action_description:
    call town_walk_crisis_action from _call_town_walk_crisis_action_1
    return
    
label town_walk_crisis_action:
    ## You spy on a neighbour during your town walk activities
    $ exclude_list = [mom, lily, mc] # exclude family and MC
    if mc.business.is_open_for_business() and not mc.business.is_weekend(): # exclude employees working on weekdays
        $ exclude_list.append(mc.business.get_employee_list())

    $ the_person = get_random_person_in_the_game(excluded_people=exclude_list)
    "While walking around the town, you see that the window in [the_person.possessive_title]'s house is open you get closer and peek inside."
    $ change_scene_display(bedroom)
    show screen person_info_ui(the_person)
    $ the_person.draw_person(position = "walking_away")
    "You see [the_person.possessive_title] is standing in front of a mirror, studing herself."
    "There is a glass of water right near the window. This is a good opportunity to test a serum for free."
    menu:
        "Add a dose of serum to [the_person.title]'s drink.":
            call give_serum(the_person) from _call_give_serum_town_walk_1
            "You quickly retreat away from the window."           
        "Keep watching.":
            "You decide not to risk being seen and stay away from her sight"
    the_person.char "I shoud get dresed for lunch. Don't have much time..."
    
    $ random_strip_messages = ["##person_name## takes off her ##clothing## and throws it on the bed.", "##person_name## keeps going and drops her ##clothing##.","##person_name## strips off her ##clothing## and tosses it to the side.", "##person_name## removes her ##clothing## and drops it to the floor.", "##person_name## quickly slides off her ##clothing## and leaves it on the ground."]
    $ the_person.strip_outfit_to_max_sluttiness(narrator_message = random_strip_messages)
   
    if the_person.outfit.vagina_available():
        "You see that [the_person.possessive_title] also studies her pussy."
        if the_person.age <=30:
            the_person.char "Nicely shaven and clean, ready to go."
        else:
            the_person.char "Well, [the_person.name]. Even at [the_person.age] that pussy looks delicious."
        "She moves her hand between her legs, just teasing herself."
        $ arousal_plus = renpy.random.randint (20,50)
        $ the_person.change_arousal (arousal_plus)
    elif the_person.outfit.tits_available():
        "You see that [the_person.possessive_title] is looking at her breasts."
        if the_person.age <=30:
            the_person.char "Darn girl, these puppies look delightful :)"
        else:
            the_person.char "Good to know that even at [the_person.age] my chest is attractive."
        "She plays with her boobs a little, cuping them, and pinching the nipples so they get hard."
        $ arousal_plus = renpy.random.randint (10,40)
        $ the_person.change_arousal (arousal_plus)
    else:
        "[the_person.possessive_title] only took off her top clothes, you just wonder why..."

    if the_person.sluttiness >=50 or the_person.get_opinion_score("masturbating") > 0 or the_person.arousal > 35:
        "[the_person.possessive_title] seems to get turned on by her own image in the mirror."
        $ the_person.draw_person(position = "missionary")
        "She lays down on the bed, spreads her legs and begins to slowly masturbate."
        if the_person.outfit.vagina_available():
            "You notice that she fingering herself with one hand, while the other is caressing the clit."
        else:
            "You notice that with one hand [the_person.possessive_title] squeezes her tits, while shoving the other between her legs."
        while the_person.arousal < 100:
            $ random_mast_descrip = renpy.random.randint(0,3)
            if random_mast_descrip == 0:
                "As she gets more and more turned on, her hand is moving faster and faster."
            elif random_mast_descrip == 1:
                if the_person.outfit.vagina_available():
                    "Her both hands move really fast around her wide-spread pussy."
                else:
                    "[the_person.possessive_title] pinches her nipples and squeezing the other vigorously between her legs."
                the_person.char "Ahh, yes. That's it. Just what I need."
            elif random_mast_descrip == 2:
                if the_person.outfit.vagina_available():
                    "She pushes 3 fingers inside, making a deep gutteral noice."
                    the_person.char "Ahh, yes. Fuck me hard and deep."
                else:
                    "[the_person.possessive_title] keeps rubbing and her moans grow louder."                   
            else:
                the_person.char "Mmm, yes. Keep going..."
            $ arousal_plus = renpy.random.randint (20,35)
            $ the_person.change_arousal (arousal_plus)
        the_person.char "Shit, I'm cumming!"
        $ the_person.draw_person(position = "missionary", emotion = "orgasm")
        "You see [the_person.possessive_title]'s body shiver as she reaches orgasm."
        the_person.char "Wow, that was intense. Need to be quieter or someone might just hear me - the window is still open... I would be so ashamed."
        $ slut_bonus = renpy.random.randint (5,10)
        $ the_person.sluttiness += slut_bonus
        $ the_person.reset_arousal()
        $ arousal_plus = renpy.random.randint (0,60)
        $ the_person.change_arousal (arousal_plus)
    else:
        pass
    menu:
        "Join her." if mc.current_stamina > 0:
            "You decide to use this opportunity and join her."
            mc.name "I was passing by, heard some noise  and decided to investigate. All this robberies, you know..."
            mc.name "And I see that that you indeed require some attention, [the_person.possessive_title]. Should I join?"
            if the_person.sluttiness <= 30 or the_person.arousal < 50:
                $ the_person.draw_person(position = "stand4", emotion = "angry")
                "[the_person.possessive_title] quickly turns around on hearing your voice. You see that she is not glad to see you."
                the_person.char "The fuck are you doing, Mr. [mc.last_name]? You can't just spy on people in their homes! Get out of here or I'll call the police!"
                "You quickly leave the area."
                $ the_person.happiness -= 5
            else:
                $ the_person.draw_person(position = "stand5", emotion = "happy")
                "[the_person.possessive_title] turns around on hearing your voice. You see her smile."
                if (the_person.love) > 30:
                    the_person.char "Come on in [the_person.mc_title]. I could use your help."
                else:
                    the_person.char "Well, that seems to be a good idea, Mr. [mc.last_name]. Come on, get inside."
                "You quickly climb inside through the window."
                call fuck_person(the_person) from _call_fuck_person_P13S2
        "Join her. (disabled)" if not mc.current_stamina > 0:
            pass
        "Walk away":
            "You decide not to disturb her and just walk away."

    hide screen person_info_ui
    $ the_person.reset_arousal()
    $ the_person.reset_outfit() #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return
