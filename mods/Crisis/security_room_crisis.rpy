# Enables the security room.
# Requirements for it to trigger are hard to achieve, might want to change it so it triggers on a specific day akin to the sister_intro_crisis
# To avoid having to start a new game it might be possible to base it of the current [day] + rand.int().

init -1 python:

    security_room_discovered = False

init 2 python:


    def security_room_introduction_requirments(done): #Runs once.
        day_trigger = 14
        if room_manager_mod_init == True:
            if done == False:
                if day >= day_trigger:
                    if mc.business.is_weekend():
                        return True #If its the weekend and two weeks have passed in the playthrough
        return False

    security_room_introduction_crisis = Action("Opens Security Branch", security_room_introduction_requirments, "security_room_introduction_label", requirement_args = [security_room_discovered]) #requirment_args have to be contained in a list.

    crisis_list.append([security_room_introduction_crisis, 20])

label security_room_introduction_label():
    $ mc.location = lobby # Make sure the player is in the lobby for Room_Manager checks.
    if is_time("Early Morning"): # NOTE: Decide on what variations I want. If switching to it triggering on a specific day this is not nescessary
        "There's not a whole lot to do early on in the weekends so you decide to explore the great elevator of secrets and mystery in the lobby"
    elif is_time("Evening"):
        "Before heading back home for the night you take a peek into the elevator and find stuff, cool"
    else:
        "You take a detour to your company's lobby and lo and behold, magic!"
    $ change_scene_display(elevator)
    "You step up to the door and make an attempt at closing it with the panel buttons"
    "..."
    "Doesn't seem to work..."

    # NOTE: This must be rewritten into something else, anything else, really.
    "You put your hands inbetween the gap of the door and pry it open. Hopefully the panel inside works"
    "Once inside the elevator you look for the 'Close Door' button, should be a simple task, but there are a surprising amount of buttons to press"
    "On the bottom row of buttons there are a couple that stands out to you"
    "Looks like there is a basement in the building..."
    "You boop the snoot on a couple of 'em, nothing happens..."
    "To the leftmost side you notice what could only be perceived as being a biometric scanner."
    "'Sweet, let's give that a go' you think to yourself..."
    "Hey, it's working. 'Overseer Protocol Initiated', amazing..."
    "By the way, this is why I don't bother with writing story elements."

    if mc.location in mod_rooms_lobby:
        $ elevator_entrance_lobby = True

    if m_division_basement not in mod_rooms_lobby:
        $ mod_rooms_lobby.append(m_division_basement) #Enables the security room.

    call screen mod_rooms_manager
    $ new_location = _return
    $ elevator_entrance_lobby = False
    $ security_room_discovered = True
    "Speaker" "[security_room_discovered]" #debug
    call change_location(new_location) # Runs the scene change.

    return
