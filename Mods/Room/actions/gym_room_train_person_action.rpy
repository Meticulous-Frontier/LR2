# Gym Studio Mod by Tristimdorion
# The gym session is available in the gym studio for all known characters.

init 3 python:
    def gym_requirement():
        if time_of_day == 4: # Can be removed
            return "Closed for the night"
        elif time_of_day == 0:
            return "Opens in the morning"
        elif mc.business.funds < 40: # $40 per session.
            return "Requires: $40"
        elif mc.energy < 30:
            return "Requires: 30 energy"
        else:
            return True

    # the gym is initialized when the action mod is loaded and also links the gym_shower to the gym
    def gym_initialization(self):
        # add gym shower to active places
        list_of_places.append(gym_shower)
        gym.link_locations_two_way(gym_shower)
        gym.add_action(self)
        return

    def gym_workout_initialization(self):
        gym.add_action(self)
        return

    train_in_gym_action = ActionMod("Schedule Gym Session {image=gui/heart/Time_Advance.png}", gym_requirement, "select_person_for_gym",
        initialization = gym_initialization, menu_tooltip = "Bring a person to the gym to train their body.", category="Mall")

    train_gym_workout_action = ActionMod("Workout in Gym {image=gui/heart/Time_Advance.png}", gym_requirement, "train_gym_workout",
        initialization = gym_workout_initialization, menu_tooltip = "You train in the gym yourself.", category="Mall")

label select_person_for_gym():
    call screen enhanced_main_choice_display(build_menu_items([get_sorted_people_list(known_people_in_the_game([mc]), "Train with", ["Back"])]))
    $ the_person = _return
    if the_person != "Back":
        "You send a text message to [the_person.title] about a gym session."
        "After some time you get a response..."

        call select_person_for_gym_response(the_person) from _call_select_person_for_gym_response # What to do if "Back" was not the choice taken.
        call advance_time from _call_advance_time_gym_training
    return # Go back to main menu


label select_person_for_gym_response(the_person):
    if the_person.happiness < 100 or the_person.obedience < 80:
        $ the_person.draw_person(emotion = "sad")
        the_person.char "I'm not in the mood for gym session, right now."
        $ the_person.change_obedience(-2)
        $ clear_scene()
        return

    if the_person.personality == bimbo_personality:
        the_person.char "Cumming right away, [the_person.mc_title]!"
    elif the_person.obedience > 140:
        the_person.char "Yes, Sir. I am on my way."
    elif the_person.sluttiness > 30:
        the_person.char "Yes, [the_person.mc_title]. I am on my way."
    elif the_person.sluttiness > the_person.obedience:
        the_person.char "Yes, [the_person.mc_title], are you going to train me personally?"
    elif the_person.happiness < 120 and the_person.love > 20:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Thanks for the attention, [the_person.mc_title]."
        $ the_person.change_happiness(+10)
    else:
        the_person.char "Sounds good, I'll be right there [the_person.mc_title]."
        $ the_person.change_happiness(+10)
    # End of responses
    call train_in_gym(the_person) from _call_train_in_gym_person_for_gym
    return

init -2 python:
    gym_session_cost = 40

label train_in_gym(the_person):
    python:
        gym.show_background()
        if not the_person in gym.people:
            the_person.location().move_person(the_person, gym)
        ran_num = renpy.random.random() * 4 # Maximum change is 4 pounds
        the_person.draw_person(emotion = "happy")

    if ran_num < 1:
        "You decide to take a yoga class with [the_person.possessive_title]."
        the_person.char "This stretching is good my flexibility."
        if the_person.sluttiness > 20:
            $ the_person.draw_person(emotion="happy")
            "There is a subtle undertone in that remark that makes you smile."
        $ the_person.change_max_energy(5)
        "She seems to be building up her endurance."
    elif ran_num < 2.5:
        "You and [the_person.possessive_title] spend a few hours working out."
        $ the_person.change_max_energy(10)
        "She seems to be building up her endurance."
    else:
        "You put [the_person.possessive_title] through a vigorous training session."
        if the_person.sluttiness > 20:
            $ the_person.draw_person(emotion = "angry")
            the_person.char "It seems you have plans with my body, [the_person.mc_title]."
            "If she only knew what dirty things you have her doing in your mind."
        $ the_person.change_max_energy(10)
        "She seems to be building up her endurance."

    $ mc.change_energy(-30)
    $ body_changed = False
    if not the_person.is_pregnant():
        $ body_changed = the_person.change_weight(-ran_num, 100)
        $ new_weight = get_person_weight_string(the_person)

        "After the session [the_person.possessive_title] weighs [new_weight]."

    else:
        "Since she is pregnant, there is no visible change to her body or weight."

    if body_changed or the_person.sluttiness > 50:
        $ the_person.draw_person()
        $ the_person.change_stats(happiness = 10, love = 5, arousal = renpy.random.randint(15, 35), slut_temp = 5)
        if the_person.sluttiness > 20:
            the_person.char "Wow, these gym sessions make me feel just great, somehow I get turned on too... would you mind?"
            menu:
                "Have Sex":
                    mc.name "Lets go to the shower room."
                    the_person.char "Lead the way, [the_person.mc_title]."
                    $ gym_shower.show_background()

                    "As soon as you get into the showers, [the_person.possessive_title] moves closer and starts kissing you."
                    # intro breaks kissing taboo for the_person
                    $ the_person.break_taboo("kissing")
                    $ old_outfit = the_person.outfit.get_copy() # make a copy we can restore

                    call fuck_person(the_person, start_position = kissing, start_object = mc.location.get_object_with_name("floor"), skip_intro = True) from _call_fuck_person_gym_training
                    $ the_report = _return
                    if the_report.get("girl orgasms", 0) > 0:
                        "[the_person.possessive_title] takes a few minutes to catch her breath, while looking at you getting dressed."
                    $ the_person.apply_outfit(old_outfit) # she puts on her gym clothes
                    $ the_person.draw_person(emotion = "happy")
                    $ del old_outfit

                "Another Time":
                    mc.name "Sorry [the_person.title], another time."
                    $ the_person.change_happiness(-5)
        else:
            the_person.char "Amazing, these gym session are really paying off."
    the_person.char "Thank you, [the_person.mc_title]."
    mc.name "Bye [the_person.title], see you next time."

    $ the_person.draw_person(position="walking_away")

    $ mc.business.change_funds(-gym_session_cost)
    "You pay for the gym session and $ [gym_session_cost] has been deducted from the company's credit card."

    $ mc.location.show_background()
    return


label train_gym_workout():
    menu:
        "Yoga class" if mc.energy >= 30:
            "You do some yoga exercises."
            $ mc.change_energy(-30)
            if mc.max_energy < 150:
                $ mc.change_max_energy(2)
                "You feel a slight improvement from your yoga session."

            if not perk_system.has_stat_perk("Yoga Focus"):
                "You feel more focussed and less stressed."
            else:
                "Doing more yoga helps to maintain your focussed state."

            $ perk_system.add_stat_perk(Stat_Perk(description = "Temporary increase to focus after yoga.", foc_bonus = 2, bonus_is_temp = True, duration = 3), "Yoga Focus")

        "Yoga class\n{color=#ff0000}{size=18}Requires: 30 energy{/size}{/color} (disabled)" if mc.energy < 30:
            pass

        "Cardio" if mc.energy >= 50:
            "You do some cardiovascular exercises."
            $ mc.change_energy(-50)
            if mc.max_energy < 200:
                $ mc.change_max_energy(5)
                "You feel your body strengthen."
            elif mc.max_energy < 250:
                $ mc.change_max_energy(2)
                "You feel a slight improvement from your workout."
                if mc.max_energy > 250:
                    $ mc.max_energy = 250
            else:
                "You have done as much as you can in the gym to improve your fitness. Workouts will no longer give any measurable gains."

        "Cardio\n{color=#ff0000}{size=18}Requires: 50 energy{/size}{/color} (disabled)" if mc.energy < 50:
            pass

        "Nothing":
            return

    $ mc.business.change_funds(-gym_session_cost)

    call advance_time from _call_advance_time_gym_workout
    return
