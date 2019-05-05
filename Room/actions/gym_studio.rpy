# Gym Studio Mod by Tristimdorion
# Requires ParadigmShift's Mod Core for initialization.
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

    # the gym is initialized by prior to starting a new game, so we need to do this in this initialization function
    def gym_initialization(self):
        gym.background_image = Image("Mods/mods/Room/images/Gym_Background.jpg") #As long a there is a mall background for the gym, replace it with our gym background
        # add gym shower to active places
        list_of_places.append(gym_shower)
        gym.link_locations_two_way(gym_shower)
        gym.actions.append(self)
        return

    train_in_gym_action = ActionMod("Schedule Gym Session {image=gui/heart/Time_Advance.png}", gym_requirement, "select_person_for_gym", 
        initialization = gym_initialization, menu_tooltip = "Bring a person to the gym to train their body.", category="Mall")
       
label select_person_for_gym():
    "Select who the gym session is for"
    python: # First we select which person we want to train with
        tuple_list = format_person_list(all_people_in_the_game([mc]), draw_hearts = True) #The list of people to show. e.g mc.location.people
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

        if person_choice == "Back":
            renpy.jump("game_loop") # Where to go if you hit "Back".
        else:
            renpy.say("","You send a text message to " + person_choice.title + " about a gym session.")
            renpy.say("", "After some time you get a response...")

    call select_person_for_gym_response(person_choice)# What to do if "Back" was not the choice taken.
    jump game_loop # Return to the game_loop or a label that will bring you back to the game loop    
    
    
label select_person_for_gym_response(person_choice):
    $ the_person = person_choice
    
    if the_person.personality == bimbo_personality:
        the_person.char "Cumming right away, [the_person.mc_title]!"
    elif the_person.obedience > 120:
        the_person.char "Yes, Sir. I am on my way."
    elif the_person.sluttiness > 30:
        the_person.char "Yes, [the_person.mc_title]. I am on my way."
    elif the_person.sluttiness > the_person.obedience:
        the_person.char "Yes, [the_person.mc_title], are you going to train me personally?"
    elif the_person.happiness < 100 and the_person.love > 20:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Thanks for the attention, [the_person.mc_title]."
        $ the_person.change_happiness(+10)
    elif the_person.happiness < 100:
        $ the_person.draw_person(emotion = "sad")
        the_person.char "I'm not in the mood for gym session, right now."
        $ the_person.change_obedience(-2)
        $renpy.scene("Active")
        return
    else:
        the_person.char "Sounds good, I'll be right there [the_person.mc_title]."
        $ the_person.change_happiness(+10)
    # End of respones
    call train_in_gym(the_person) from _call_train_in_gym_person_for_gym
    call advance_time from _call_advance_time_gym_training
    