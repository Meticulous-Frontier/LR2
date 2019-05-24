init -1 python: # Declare variables to use

    # Create the room(s) I want to use.
    gym_shower = Room("shower", "Gym Shower", [], room_background_image("Gym_Shower_Background.jpg"), [], [], [], True, [], None, False)

init 3 python: # Room creation
    # Create Gym shower and attach to gym
    gym_shower.add_object(make_wall())
    gym_shower.add_object(make_floor())
