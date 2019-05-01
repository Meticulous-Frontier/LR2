init -1 python: # Declare variables to use

    # Create the room(s) I want to use.
    home_shower = Room("shower", "Home Shower", [], room_background_image("Shower_Background.jpg"), [], [], [], False, [], None, False)

init 3 python: # Room creation
    # Create Home shower and attach to hallway
    home_shower.add_object(make_wall())
    home_shower.add_object(make_floor())

    # Always check if the room or action is somehow added already before proceeding.
    # I want the Elevator to be accessable.
