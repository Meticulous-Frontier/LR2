# Gym Studio Mod by Tristimdorion
# The gym session is available in the gym studio for all known characters.

init 3 python:
    def gym_requirement():
        if time_of_day == 4: # Can be removed
            return "Closed for the night."
        elif time_of_day == 0:
            return "Opens in the morning."
        elif mc.business.funds < 40: # $40 per session.
            return "Requires $40."
        else:
            return True

    # the gym is initialized when the action mod is loaded and also links the gym_shower to the gym
    def gym_initialization(self):
        gym.background_image = room_background_image("Gym_Background.jpg") #As long a there is a mall background for the gym, replace it with our gym background

        # add gym shower to active places
        list_of_places.append(gym_shower)
        gym.link_locations_two_way(gym_shower)
        gym.actions.append(self)
        return

    train_in_gym_action = ActionMod("Schedule Gym Session {image=gui/heart/Time_Advance.png}", gym_requirement, "select_person_for_gym",
        initialization = gym_initialization, menu_tooltip = "Bring a person to the gym to train their body.", category="Mall")

label select_person_for_gym():
    $ people_list = get_sorted_people_list(known_people_in_the_game([mc]), "Train with", ["Back"])

    if "build_menu_items" in globals():
        call screen main_choice_display(build_menu_items([people_list]))
    else:
        call screen main_choice_display([people_list])
    $ person_choice = _return
    $ del people_list

    if person_choice != "Back":
        "You send a text message to [person_choice.title] about a gym session."
        "After some time you get a response..."

        call select_person_for_gym_response(person_choice) from _call_select_person_for_gym_response # What to do if "Back" was not the choice taken.
        call advance_time from _call_advance_time_gym_training

    return # Go back to main menu


label select_person_for_gym_response(person_choice):
    # link the selected person to the_person global object (linked to person info UI)
    $ the_person = person_choice

    if the_person.happiness < 100 or the_person.obedience < 80:
        $ the_person.draw_person(emotion = "sad")
        the_person.char "I'm not in the mood for gym session, right now."
        $ the_person.change_obedience(-2)
        $renpy.scene("Active")
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

init 2 python:
    def set_gym_outfit(person):
        person.apply_outfit(workout_wardrobe.decide_on_outfit2(person))
        person.draw_person(emotion="default")
        return

label train_in_gym(person):
    python:
        gym.show_background()
        set_gym_outfit(person)
        change = renpy.random.random() * 4 # Maximum change is 4 pounds

    if change < 1:
        "You decide to take a yoga class with [person.possessive_title]."
        person.char "This stretching is good my flexibility."
        if person.sluttiness > 20:
            $ person.draw_person(emotion="happy")
            "There is a subtle undertone in that remark that makes you smile."
        $ person.change_max_energy(5)
        "She seems to be building up her endurance"
    elif change < 2.5:
        "You and [person.possessive_title] spend a few hours working out."
        $ person.change_max_energy(10)
        "She seems to be building up her endurance"
    else:
        "You put [person.possessive_title] through a vigorous training session."
        if person.sluttiness > 20:
            $ person.draw_person(emotion = "angry")
            person.char "It seems you have plans with my body, [person.mc_title]."
            "If she only knew what dirty things you have her doing in your mind."
        $ person.change_max_energy(10)
        "She seems to be building up her endurance"

    $ body_changed = person.change_weight(-change, 100)
    $ new_weight = get_person_weight_string(person)

    "After the session [person.possessive_title] weighs [new_weight]."

    if body_changed or person.sluttiness > 50:
        $ person.draw_person()
        $ person.change_stats(happiness = 10, love = 5, arousal = renpy.random.randint(15, 35), slut_temp = 5)
        if person.sluttiness > 20:
            person.char "Wow, these gym sessions make me feel just great, somehow I get turned on too... would you mind?"
            menu:
                "Have Sex":
                    mc.name "Lets go to the shower room."
                    person.char "Lead the way, [person.mc_title]."
                    $ gym_shower.show_background()

                    "As soon as you get into the showers, [person.possessive_title] moves closer and starts kissing you."

                    call fuck_person(person, start_position = kissing, start_object = mc.location.get_object_with_name("floor"), skip_intro = True) from _call_fuck_person_gym_training
                    $ the_report = _return
                    if the_report.get("girl orgasms", 0) > 0:
                        "[person.possessive_title] takes a few minutes to catch her breath, while looking at you getting dressed."

                "Another Time":
                    mc.name "Sorry [person.title], another time."
                    $ person.change_happiness(-5)
        else:
            person.char "Amazing, these gym session are really paying off."
    person.char "Thank you, [person.mc_title]."
    mc.name "Bye [person.title], see you next time."

    $ person.draw_person(position="walking_away")

    $ mc.business.change_funds(-gym_session_cost)
    "You pay for the gym session and $ [gym_session_cost] has been deducted from the company's credit card."

    $ person.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
    $ mc.location.show_background()
    return
