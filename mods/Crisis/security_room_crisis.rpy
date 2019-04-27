init -1 python:

    security_room_discovered = False

init 2 python:


    def security_room_introduction_requirments(done):
        #Want it to run once.: # Room has to exist.
        if room_manager_mod_init == True:
            if done == False:
                if mc.location == lobby and mc.business.is_open_for_business() == False: # Visit lobby during afterhours or weekends.
                    return True
        return False

    security_room_introduction_crisis = Action("Opens Security Branch", security_room_introduction_requirments, "security_room_introduction_label", requirement_args = [security_room_discovered]) #requirment_args have to be contained in a list.

    crisis_list.append([security_room_introduction_crisis, 20])

label security_room_introduction_label():

    if is_time("Early Morning"):
        if  mc.business.is_weekend():
            "There's not a whole lot to do early on in the weekends so you decide to explore the great elevator of secrets and mystery in the lobby"
        else:
            "There's not a whole lot to do before the employees get to work so you decide to explore the great elevator of secrets, mystery, magic and lewdness"
    elif is_time("Evening"):
        if mc.business.is_weekend():
            "Before heading back home for the night you take a peek into the elevator and find stuff, cool"
        else:
            "After the employees have left the building and you are on your way back home through the lobby you notice a draft coming from the slightly ajar elevator door."
    $ change_scene_display(elevator)
    "You step up to the door and make an attempt at closing it with the panel buttons"
    "..."
    "Doesn't seem to work..."

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

    $ mod_rooms_lobby.append(m_division_basement) #Enables the security room.

    call screen mod_rooms_manager
    $ new_location = _return
    $ elevator_entrance_lobby = False
    $ security_room_discovered = True

    "Speaker" "[security_room_discovered]" #debug
    return
