init -1 python: # Declare variables to use

    # Create the room(s) I want to use.
    gym_shower = Room("shower", "Gym Shower", [], Image("Mods/mods/Room/images/Shower_Background.jpg"), [], [], [], True, [], None, False)
    home_shower = Room("shower", "Home Shower", [], Image("Mods/mods/Room/images/Shower_Background.jpg"), [], [], [], True, [], None, False)

init 2 python: # Room creation
    gym_shower.add_object(make_wall())
    gym_shower.add_object(make_floor())

    home_shower.add_object(make_wall())
    home_shower.add_object(make_floor())

    # Always check if the room or action is somehow added already before proceeding.
    # I want the Elevator to be accessable.
    if home_shower not in mod_rooms_hall:
        mod_rooms_hall.append(home_shower)

    # I want to enter it from the gym.
    if gym_shower not in mod_rooms_gym:
        mod_rooms_gym.append(gym_shower)

