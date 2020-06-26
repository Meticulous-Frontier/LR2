## Town walk Crisis Mod by Tristimdorion
# Based on the Pilotus13 Vanilla extension
init -1 python:
    town_walk_mod_weight = 10   # Due to limited time window we give it a higher probability

init 2 python:
    def town_walk_crisis_requirement():
        if mc.location in get_mall_locations():
            if time_of_day == 1 or time_of_day == 2: # only morning and afternoon
                return True
        return False

    def get_town_walk_person():
        if mc.business.is_weekend():
            return get_random_known_person_in_the_game(excluded_people = [mom, lily, aunt, cousin, mc])
        else:
            return get_random_known_person_in_the_game(excluded_people = [mom, lily, aunt, cousin, mc] + mc.business.get_employee_list())

    town_walk_crisis_action = ActionMod("Town Walk",town_walk_crisis_requirement,"town_walk_crisis_action_label", category = "Mall",
        menu_tooltip = "On occasion you take an afternoon stroll through town, someone did not close their bedroom curtains.", is_crisis = True, crisis_weight = town_walk_mod_weight)

label town_walk_crisis_action_label:
    ## You spy on a neighbor during your town walk activities
    $ the_person = get_town_walk_person()
    if the_person is None: # this could be no one
        return

    # now you know where she lives
    $ the_person.learn_home()

    "While walking around town, you see that the window in [the_person.possessive_title]'s house is open..."
    menu:
        "Get closer and peek inside?":
            pass
        "Ignore it.":
            return

    $ bedroom.show_background()
    $ the_person.draw_person(position = "walking_away")
    "You see [the_person.possessive_title] is standing in front of a mirror, studying herself."
    "There is a glass of water right near the window. This is a good opportunity to test a serum for free."
    menu:
        "Add a dose of serum to [the_person.title]'s drink":
            call give_serum(the_person) from _call_give_serum_town_walk_1
            "You quickly retreat away from the window."
        "Keep watching":
            "You decide not to risk being seen and stay away from her sight"
    the_person.char "I should get dressed for lunch. Don't have much time..."

    if (the_person.strip_outfit_to_max_sluttiness(narrator_messages = [
        "[the_person.possessive_title] takes off her [strip_choice.name] and throws it on the bed.",
        "[the_person.possessive_title] keeps going and drops her [strip_choice.name].",
        "[the_person.possessive_title] strips off her [strip_choice.name] and tosses it to the side.",
        "[the_person.possessive_title] removes her [strip_choice.name] and drops it to the floor.",
        "[the_person.possessive_title] quickly slides off her [strip_choice.name] and leaves it on the ground."
        ], temp_sluttiness_boost = 20)):

        # only show this part of the dialog if she removed clothing
        if the_person.outfit.vagina_available():
            "You see that [the_person.possessive_title] also studies her pussy."
            if the_person.pubes_style is shaved_pubes:
                the_person.char "Nicely shaven and clean, ready to go."
            elif the_person.pubes_style is default_pubes:
                the_person.char "Darn, I should have take some time to trim my pubes."
            else:
                the_person.char "Perfectly trimmed pussy, ready for action."
            "She moves her hand between her legs, just teasing herself."
            $ arousal_plus = renpy.random.randint (20,50)
            $ the_person.change_arousal (arousal_plus)
        elif the_person.outfit.tits_available():
            "You see that [the_person.possessive_title] is looking at her breasts."
            if the_person.age <=30:
                the_person.char "Darn girl, these puppies look delightful :)"
            else:
                the_person.char "Good to know that even at [the_person.age] my chest is attractive."
            "She plays with her boobs a little, cupping them, and pinches the nipples so they get hard."
            $ arousal_plus = renpy.random.randint (10,40)
            $ the_person.change_arousal (arousal_plus)
        else:
            "[the_person.possessive_title] only took off her top clothes, you just wonder why..."

    if the_person.outfit.vagina_available() and (the_person.sluttiness >=50 or the_person.get_opinion_score("masturbating") > 0 or the_person.arousal > 35):
        "[the_person.possessive_title] seems to get turned on by her own image in the mirror."
        $ the_person.draw_person(position = "missionary")
        "She lays down on the bed, spreads her legs and begins to masturbate slowly."
        if the_person.outfit.vagina_available():
            "You notice that she is fingering herself with one hand, while the other is caressing her clit."
        else:
            "You notice that with one hand [the_person.possessive_title] squeezes her tits, while shoving the other between her legs."
        while the_person.arousal < 100:
            $ ran_num = renpy.random.randint(0,3)
            if ran_num == 0:
                "As she gets more and more turned on, her hand moves faster and faster."
            elif ran_num == 1:
                if the_person.outfit.vagina_available():
                    "Both her hands move really fast around her wide-spread pussy."
                else:
                    "[the_person.possessive_title] pinches her nipples and squeezes the other vigorously between her legs."
                the_person.char "Ahh, yes. That's it. Just what I need."
            elif ran_num == 2:
                if the_person.outfit.vagina_available():
                    "She pushes 3 fingers inside, making a deep guttural noise."
                    $ the_person.call_dialogue("sex_responses_foreplay")
                else:
                    "[the_person.possessive_title] keeps rubbing and her moans grow louder."
            else:
                the_person.char "Mmm, yes. Keep going..."
            $ the_person.change_arousal(renpy.random.randint(20,35))
        $ the_person.call_dialogue("climax_responses_foreplay")
        $ the_person.draw_person(position = "missionary", emotion = "orgasm")
        $ mc.change_arousal(25)
        #"You see [the_person.possessive_title]'s body shiver as she reaches orgasm." NOTE: Things like this gets mentioned in the climax_responses
        the_person.char "Wow, that was intense. Need to be quieter or someone might just hear me - the window is still open... I would be so ashamed."
        $ the_person.reset_arousal()
        $ the_person.change_stats(arousal = renpy.random.randint(0,60), slut_temp = renpy.random.randint(5,10))

    menu:
        "Join her":
            "You decide to use this opportunity and join her."
            mc.name "I was passing by, heard some noise  and decided to investigate. All these robberies, you know..."
            mc.name "And I see that that you indeed require some attention, [the_person.title]. Should I join?"
            if the_person.sluttiness > 50 or the_person.arousal > 50:
                $ the_person.draw_person(position = "stand5", emotion = "happy")
                "[the_person.possessive_title] turns around upon hearing your voice. You see her smile."
                if (the_person.love) > 30:
                    the_person.char "Come on in [the_person.mc_title]. I could use your help."
                else:
                    the_person.char "Well, that seems to be a good idea, Mr. [mc.last_name]. Come on, get inside."
                "You quickly climb inside through the window."
                call fuck_person(the_person) from _call_fuck_person_P13S2
            else:
                $ the_person.draw_person(position = "stand4", emotion = "angry")
                "[the_person.possessive_title] quickly turns around upon hearing your voice. You see that she is not glad to see you."
                the_person.char "The fuck are you doing, Mr. [mc.last_name]? You can't just spy on people in their homes! Get out of here or I'll call the police!"
                "You quickly leave the area."
                $ the_person.happiness -= 5
        "Walk away":
            "You decide not to disturb her and just walk away."

    python:
        the_person.apply_planned_outfit()
        mc.location.show_background()
        renpy.scene("Active")
    return
