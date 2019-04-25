# Gym Studio Mod by Tristimdorion
# Requires ParadigmShift's Mod Core for initialization.
init -1 python:
    gym_training_mod_init = False

init 2 python:
    def gym_training_mod_init_requirement():
        if gym_training_mod_init == False:
            return True
        return False
    
    def gym_requirement():
        if time_of_day == 4: # Can be removed
            return "Closed for the night."
        elif mc.business.funds < 40: # $40 per session.
            return "Not enough money."
        else:
            return True

    gym_training_mod_init_event = Action("Gym Training Mod Initialization Event", gym_training_mod_init_requirement, "gym_training_mod_init_label")

    if gym_training_mod_init_event not in mod_list:
        mod_list.append(gym_training_mod_init_event)
        
label gym_training_mod_init_label:
    python:
        gym.background_image = Image("Mods/mods/Room/images/Gym_Background.jpg") #As long a there is a mall background for the gym, replace it with our gym background

        train_in_gym_action = Action("Schedule a gym session.", gym_requirement, "select_person_for_gym", menu_tooltip = "Bring a person to the gym to train their body.")

        # Always check if the room is somehow already added.
        # I want to enter it from the gym.
        if gym_shower not in mod_rooms_gym:
            mod_rooms_gym.append(gym_shower)

        # I want to enable NPC pathing
        if gym_shower not in list_of_places:
            list_of_places.append(gym_shower)
            
        # Always check if the action is somehow already added.
        # Enables the train_in_gym_action for the gym.
        if train_in_gym_action not in gym.actions:
            gym.actions.append(train_in_gym_action)

        gym_training_mod_init = True           
    return
       
label select_person_for_gym():
    "Select who the gym session is for"
    python: # First we select which person we want to train with
        tuple_list = format_person_list(all_people_in_the_game([mc]), draw_hearts = True) #The list of people to show. e.g mc.location.people
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

        if person_choice == "Back":
            renpy.jump("game_loop") # Where to go if you hit "Back".
        else:
            renpy.say("","You send a text message to " + person_choice.name + " about a gym session.")
            renpy.say("", "After some time you get a response...")

    call select_person_for_gym_response(person_choice)# What to do if "Back" was not the choice taken.
    call advance_time from _call_advance_time_gym_training
    jump game_loop # Return to the game_loop or a label that will bring you back to the game loop    
    
    
label select_person_for_gym_response(person_choice):
    $ the_person = person_choice
    
    if the_person.personality == bimbo_personality:
        the_person.name "Cumming right away, [mc.name]!"
    elif the_person.obedience > 120:
        the_person.name "Yes, Sir. I am on my way."
    elif the_person.sluttiness > 30:
        the_person.name "Yes, [mc.name]. I am on my way."
    elif the_person.sluttiness > the_person.obedience:
        the_person.name "Yes, [mc.name], are you going to train me personally?"
    elif the_person.happiness < 100 and the_person.love > 20:
        $ the_person.draw_person(emotion = "happy")
        the_person.name "Thanks for the attention, [mc.name]."
        $ the_person.change_happiness(+10)
    elif the_person.happiness < 100:
        $ the_person.draw_person(emotion = "sad")
        the_person.name "I'm not in the mood for gym session, right now."
        $ the_person.change_obedience(-2)
        $renpy.scene("Active")
        return
    else:
        the_person.name "Sounds good, I'll be right there [mc.name]."
        $ the_person.change_happiness(+10)
    # End of respones
    call train_in_gym(the_person) from _call_train_in_gym_person_for_gym
    