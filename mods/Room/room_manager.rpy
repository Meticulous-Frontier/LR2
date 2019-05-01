# Room management mod by Trollden.
# Use it however you like.

# Requires Mod Core by ParadigmShift

# There are four lists noted below.
# Each list corresponds to the room they are named after e.g mod_rooms_lobby == Room(lobby)
# the mod_rooms list will show the rooms in it regardless of what entry is being used.
# To access the room manager in-game use the "Do something..." menu from the game_loop after having initialized the mod via the Mod Core.
# If you do not have the mod core you can append the elevator_action yourself to the rooms you want it in with Roomname.actions.append(room_manager_action)

# If you want characters other than the main character and defined characters to be able to roam the rooms make sure they are set to public with room.public = True
init 2 python:
    add_label_hijack("normal_start", "activate_room_manager")

init 3 python:
    def mod_room_manager_append(action): # Make sure you input a valid action. e.g sleep_action
        action = action
        for room in mod_rooms_append:
            if action not in room.actions:
                room.actions.append(action)
        return

    room_manager_action = ActionMod("Enter the elevator", room_manager_action_requirement, "room_manager_action_label",
        menu_tooltip = "Visit rooms on different floors", category = "Misc")

        # Room(name,formalName,connections,background_image,objects,people,actions,public,map_pos, tutorial_label = None, visible = True)
    elevator = Room("elevator", "Elevator", [], apartment_background, [],[],[], False,[], None, False) # Create a custom room that can be put to use for generic events and such.

label activate_room_manager(stack):
    $ room_manager_tutorial = False
    # Default mod room lists
    # Player's home.
    $ elevator_entrance_kitchen = False   # These variables are turned to True if for example "mc.location in mod_rooms_mall" when calling the elevator.
    $ mod_rooms_kitchen = []              # This is done in the screen room_manager in the form of: if elevator_entrance_mall == True: -> display rooms in mod_rooms_mall
                                        # They also determine if the rooms belonging to the corresponding list should be displayed or not.

    $ elevator_entrance_mom_bedroom = False # If this variable is True then the list below it will be shown.
    $ mod_rooms_mom_bedroom = []

    $ elevator_entrance_sister_bedroom = False
    $ mod_rooms_sister_bedroom = []

    $ elevator_entrance_player_bedroom = False
    $ mod_rooms_player_bedroom = []

    $ elevator_entrance_hall = False
    $ mod_rooms_hall = []

    # Downtown.
    $ bus_entrance = False
    $ mod_rooms_bus = []

    # Mall.
    $ elevator_entrance_mall = False
    $ mod_rooms_mall = []

    $ elevator_entrance_office_store = False
    $ mod_rooms_office_store = []

    $ elevator_entrance_clothing_store = False
    $ mod_rooms_clothing_store = []

    $ elevator_entrance_sex_store = False
    $ mod_rooms_sex_store = []

    $ elevator_entrance_home_store = False
    $ mod_rooms_home_store = []

    $ elevator_entrance_gym = False
    $ mod_rooms_gym = []

    # Business
    $ elevator_entrance_lobby = False
    $ mod_rooms_lobby = []

    $ elevator_entrance_office = False #This is the same room as the supply division
    $ mod_rooms_office = []

    $ elevator_entrance_rd_division = False
    $ mod_rooms_rd_division = []

    $ elevator_entrance_p_division = False
    $ mod_rooms_p_division = []

    $ elevator_entrance_m_division = False
    $ mod_rooms_m_division = []

    $ mod_rooms = [] #Append to this list with room_mods.append(room_name) to have it show up in any of the elevators

    # Return mod room lists (Copies of default mod room lists).
    #mod_rooms_mall_return = [] # Do not touch these lists. They are checking towards the default mod lists in mod_rooms_return() and are automatically appended.

    $ mod_rooms_append = [] # Rooms appended to this list will have the room_manager_action automatically appended to them so that you can access it via "Do something..."
                          # It updates on first time startup of the mod and whenever an elevator / bus is entered so you can append to it whenever as long as at least ONE location
                          # With access to the screen already exist.
    $ mod_rooms_append.append(mall)
    $ mod_rooms_append.append(downtown)
    $ mod_rooms_append.append(hall)
    $ mod_rooms_append.append(lobby)

    # Enable the action in the custom elevator room.
    $ mod_rooms_append.append(elevator)

    # Have the default hubs always be available from within themselves.
    # Got to append them here as the rooms do not exist on list creation.
    $ mod_rooms_mall.append(mall)
    $ mod_rooms_bus.append(downtown)
    $ mod_rooms_hall.append(hall)
    $ mod_rooms_lobby.append(lobby)
    $ mod_rooms_mom_bedroom.append(mom_bedroom)
    $ mod_rooms_sister_bedroom.append(lily_bedroom)
    $ mod_rooms_player_bedroom.append(bedroom)
    $ mod_rooms_office_store.append(office_store)
    $ mod_rooms_clothing_store.append(clothing_store)
    $ mod_rooms_sex_store.append(sex_store)
    $ mod_rooms_home_store.append(home_store)
    $ mod_rooms_gym.append(gym)
    $ mod_rooms_office.append(office)
    $ mod_rooms_rd_division.append(rd_division)
    $ mod_rooms_p_division.append(p_division)
    $ mod_rooms_m_division.append(m_division)
#        .append()
#        .append()
#        .append()
#        .append()

    $ mod_room_manager_append(room_manager_action) # Appends the action to any room in the mod_rooms_append list.
                               #This is also done whenever accessing any entry points so a restart of the mod isn't required.
    $ execute_hijack_call(stack)
    return


init 2 python: # Requirement for the elevator action to show in "Do something..." if it has been appended to the room.
    def room_manager_action_requirement():
        return True

label room_manager_action_label(): # What happens when you "Enter the elevator"
    python:
        mod_room_manager_append(room_manager_action) # Adds the action to any new room in the mod_rooms_append list that does not already have it.
    if room_manager_tutorial == False: # Set to True if the player does not wish to see the message (ever) again.
        "Speaker" "This elevator acts as a hub for rooms added to the game via mods"
        "Speaker" "If you want a room to show up in the elevator do mod_rooms.append(room_name)"
        "Speaker" "If you want access to the elevator or bus from your room do mod_rooms_append.append(room_name)"
        "Speaker" "See the elevator.rpy file for more information about different lists that can be used"
        menu:
            "Speaker" "Would you like the message to be repeated?"
            "Yes":
                jump room_manager_action_label
            "No":
                $ room_manager_tutorial = True # Tutorial message will not appear again.

    # Checks where the player is accessing the screen from.
    # If the entrance point is not set to True none of the rooms in the corresponding lists will be shown.
    if mc.location in mod_rooms_kitchen:
        $ elevator_entrance_kitchen = True
    elif mc.location in mod_rooms_mom_bedroom:
        $ elevator_entrance_mom_bedroom = True
    elif mc.location in mod_rooms_sister_bedroom:
        $ elevator_entrance_sister_bedroom = True
    elif mc.location in mod_rooms_player_bedroom:
        $ elevator_entrance_player_bedroom = True
    elif mc.location in mod_rooms_hall:
        $ elevator_entrance_hall = True

    elif mc.location in  mod_rooms_bus:
        $ bus_entrance = True

    elif mc.location in mod_rooms_mall:
        $ elevator_entrance_mall = True
    elif mc.location in mod_rooms_office_store:
        $ elevator_entrance_office_store = True
    elif mc.location in mod_rooms_clothing_store:
        $ elevator_entrance_clothing_store = True
    elif mc.location in mod_rooms_sex_store:
        $ elevator_entrance_sex_store = True
    elif mc.location in mod_rooms_home_store:
        $ elevator_entrance_home_store = True
    elif mc.location in mod_rooms_gym:
        $ elevator_entrance_gym = True

    elif mc.location in mod_rooms_lobby:
        $ elevator_entrance_lobby = True
    elif mc.location in mod_rooms_office:
        $ elevator_entrance_office = True
    elif mc.location in mod_rooms_rd_division:
        $ elevator_entrance_rd_division = True
    elif mc.location in mod_rooms_p_division:
        $ elevator_entrance_p_division = True
    elif mc.location in mod_rooms_m_division:
        $ elevator_entrance_m_division = True


    call screen mod_rooms_manager
    $ new_location = _return

    # Put the check back to a False state to avoid overlaps unless specified elsewhere.
    # This is pushed through after the screen is closed with the "Return" button.

    $ elevator_entrance_kitchen = False
    $ elevator_entrance_mom_bedroom = False
    $ elevator_entrance_sister_bedroom = False
    $ elevator_entrance_player_bedroom = False
    $ elevator_entrance_hall = False

    $ bus_entrance = False

    $ elevator_entrance_mall = False
    $ elevator_entrance_office_store = False
    $ elevator_entrance_clothing_store = False
    $ elevator_entrance_sex_store = False
    $ elevator_entrance_home_store = False
    $ elevator_entrance_gym = False

    $ elevator_entrance_lobby = False
    $ elevator_entrance_office = False
    $ elevator_entrance_rd_division = False
    $ elevator_entrance_p_division = False
    $ elevator_entrance_m_division = False

    call change_location(new_location) # Runs the scene change.

#    if new_location == Room: # Have something happen if a specific room is entered.
#        $ possible_greetings = []
#        python:
#                        for a_person in new_location.people:
#                            if mc.business.get_employee_title(a_person) != "None":
#                                possible_greetings.append(a_person)
#                    $ the_greeter = get_random_from_list(possible_greetings)
#                    if the_greeter:
#                        $ the_greeter.draw_person()
#                        $ the_greeter.call_dialogue("work_enter_greeting")
#                        $ renpy.scene("Active")

screen mod_rooms_manager(): # This screen is called from room_manager_label and contains the core section of the mod.

    modal True
    zorder 101
    if bus_entrance: # Use a different background if it is supposed to be a "bus ride"
        add "Outside_Background.png"
    else:
        add "Apartment_Lobby.png"
    $ num_of_places = __builtin__.len(mod_rooms)
    $ places_so_far = 0
    $ x_offset_per_place = 0.1

    # Lists all rooms in mod_rooms without any prerequisites
    for place in mod_rooms:
        if not place == mc.location:
            frame:
                background None
                xysize [171,150]
                anchor [0.0,0.0]
                align [0.1+(x_offset_per_place*places_so_far), 0.5]

                imagebutton:
                    anchor [0.5,0.5]
                    auto "gui/LR2_Hex_Button_%s.png"
                    focus_mask "gui/LR2_Hex_Button_idle.png"
                    action Function(mc.change_location,place)
                    sensitive place.accessable
                text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

        else:
            frame:
                background None
                xysize [171,150]
                anchor [0.0,0.0]
                align [0.1+(x_offset_per_place*places_so_far),0.5]

                imagebutton:
                    anchor [0.5,0.5]
                    idle "gui/LR2_Hex_Button_Alt_idle.png"
                    focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                    action Function(mc.change_location,place)
                    sensitive False

                text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
        $ places_so_far += 1

    # Lists all of the rooms in mod_rooms_mall if the player is in the mall.
    if elevator_entrance_mall:

        for place in mod_rooms_mall:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    # Lists all of the rooms in mod_rooms_bus if the player is downtown.
    if bus_entrance:

        for place in mod_rooms_bus:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    # Lists all the locations in mod_rooms_hall if the player is in the main hall
    if elevator_entrance_hall:

        for place in mod_rooms_hall:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    # Lists all the rooms in mod_rooms_lobby if the player is in the business lobby
    if elevator_entrance_lobby:

        for place in mod_rooms_lobby:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_kitchen:

        for place in mod_rooms_kitchen:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_mom_bedroom:

        for place in mod_rooms_mom_bedroom:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_sister_bedroom:

        for place in mod_rooms_sister_bedroom:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_player_bedroom:

        for place in mod_rooms_player_bedroom:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_office_store:

        for place in mod_rooms_office_store:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_clothing_store:

        for place in mod_rooms_clothing_store:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_sex_store:

        for place in mod_rooms_sex_store:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_home_store:

        for place in mod_rooms_home_store:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_gym:

        for place in mod_rooms_gym:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_office:

        for place in mod_rooms_office:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_rd_division:

        for place in mod_rooms_rd_division:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_p_division:

        for place in mod_rooms_p_division:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    if elevator_entrance_m_division:

        for place in mod_rooms_m_division:
            if not place == mc.location:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far), 0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        auto "gui/LR2_Hex_Button_%s.png"
                        focus_mask "gui/LR2_Hex_Button_idle.png"
                        action Function(mc.change_location,place)
                        sensitive place.accessable
                    text place.formalName + "\n(" + str(len(place.people)) +")" anchor [0.5,0.5] style "map_text_style"

            else:
                frame:
                    background None
                    xysize [171,150]
                    anchor [0.0,0.0]
                    align [0.1+(x_offset_per_place*places_so_far),0.5]

                    imagebutton:
                        anchor [0.5,0.5]
                        idle "gui/LR2_Hex_Button_Alt_idle.png"
                        focus_mask "gui/LR2_Hex_Button_Alt_idle.png"
                        action Function(mc.change_location,place)
                        sensitive False

                    text place.formalName + "\n(" + str(len(place.people)) + ")" anchor [0.5,0.5] style "map_text_style"
            $ places_so_far += 1

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]

        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [Hide("elevator"), Return(mc.location)]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"
