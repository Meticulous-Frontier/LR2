init 2 python: # Declare variables to use

    # Create the room(s) I want to use.
    gym_shower = Room("gym shower", "Gym Shower", [], standard_gym_shower_backgrounds[:], [], [], [], True, [], None, False, lighting_conditions = standard_indoor_lighting)

init 3 python: # Room creation
    # Create Gym shower and attach to gym
    gym_shower.add_object(make_wall())
    gym_shower.add_object(make_floor())
