# Role based around obedience that can be appended to people in the Dungeon.
init 2 python:

    Person.stay_wet = False
    Person.slave_collar = False

init 10 python:

    def stay_wet_requirement(the_person):
        return True

    def advance_time_stay_wet_requirement():
        return stay_wet_action.enabled

    def collar_slave_requirement(the_person):
        if the_person.slave_collar == False:
            return True
        if the_person.slave_collar == True:
            return False

    def uncollar_slave_requirement(the_person):
        return the_person.slave_collar

    def advance_time_collar_person_requirement():
        return collar_slave_action.enabled

    stay_wet_action = ActionMod("Stay wet.", stay_wet_requirement, "stay_wet_label", menu_tooltip = "Have the person stay aroused at all times.", category = "Slave Role")
    advance_time_stay_wet_action = ActionMod("Enable 'stay wet' functionality", advance_time_stay_wet_requirement, "advance_time_stay_wet_label", priority = 20, allow_disable = False, menu_tooltip = "People with 'stay_wet = True' have their minimum arousal set to 50%")
    if advance_time_stay_wet_action not in advance_time_action_list:
        advance_time_action_list.append(advance_time_stay_wet_action)

    collar_slave_action = ActionMod("Place collar on [the_person.title].", collar_slave_requirement, "slave_collar_person_label", menu_tooltip = "Put a collar of ownership on the target, ensure that their obedience stays high.", category = "Slave Role")
    uncollar_slave_action = ActionMod("Remove collar from [the_person.title].", uncollar_slave_requirement, "slave_collar_person_label", menu_tooltip = "Remove the collar, declaring them a free spirit.", category = "Dungeon Actions", allow_disable = False)
    advance_time_collar_person_action = ActionMod("Enable 'collar' functionality", advance_time_collar_person_requirement, "advance_time_collar_person_label", allow_disable = False, priority = 20, menu_tooltip = "Allows the collar_slave_action to do what it is intended to.")
    if advance_time_collar_person_action not in advance_time_action_list:
        advance_time_action_list.append(advance_time_collar_person_action)

    slave_role = Role("Slave", [stay_wet_action, collar_slave_action, uncollar_slave_action], hidden = False)

label stay_wet_label(the_person): # Can expand with dialogue options and degrees of arousal, but just setting up basic actions for now.

    if the_person.stay_wet == False:
        "You order [the_person.possessive_title] to keep herself wet and ready at all times for you."
        if the_person.arousal < 50:
            $ the_person.arousal = 50
        $ the_person.stay_wet = True

    elif the_person.stay_wet == True:
        "You tell [the_person.possessive_title] to calm their tits."
        $ the_person.stay_wet = False

    return

label advance_time_stay_wet_label():

    python:
        for (people, place) in people_to_process:
            if people.stay_wet and people.arousal < 50:
                people.arousal = 50
                if people.sluttiness < 15:
                    people.sluttiness = 15 # Doesn't make sense for them to be "ready" if they cannot be seduced.
    return

label slave_collar_person_label(the_person):

    if the_person.slave_collar:
        $ the_person.slave_collar = False
        "You remove the collar from your [the_person.possessive_title]'s neck"
    else:
        $ the_person.slave_collar = True
        "You put one of the collars you created around your [the_person.possessive_title]'s neck"

    return

label advance_time_collar_person_label():

    python:
        for (people,place) in people_to_process:
            if people.slave_collar and people.obedience < 130: # 130 is the highest value for dialogues and various acts.
                people.obedience = 130
    return
