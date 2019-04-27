init -1 python: # Declare variables to use

    # Create the room(s) I want to use.
    gym_shower = Room("shower", "Gym Shower", [], room_background_image("Gym_Shower_Background.jpg"), [], [], [], True, [], None, False)

init 3 python: # Room creation
    # Create Gym shower and attach to gym
    gym_shower.add_object(make_wall())
    gym_shower.add_object(make_floor())

    # Always check if the room or action is somehow added already before proceeding.
    # I want to enter it from the gym.
    if gym_shower not in mod_rooms_gym:
        mod_rooms_gym.append(gym_shower)

