init -2 python:
    global current_tier
    current_tier = 0

init -1 python:
    purchasable_rooms_list = []
    t1_cost = 5000
    t2_cost = 10000
    t3_cost = 20000

init 3 python:
    def purchase_rooms_requirement():
        return True

    def purchase_rooms_initialization(self):
        office.actions.append(self)

    purchase_rooms = ActionMod("Purchase Rooms", purchase_rooms_requirement, "purchase_rooms", initialization = purchase_rooms_initialization,
        menu_tooltip = "Purchase rooms and facilities", category = "Business")

# Categorized rooms into tiers for their cost.
# TODO: Show different disabled message if room purchased
init 2 python:
    def room_tier_1(roomname):
        if len(filter(lambda x: x.name == roomname, list_of_places)) == 1:
            return "Already owned"
        if time_of_day == 4:    # Force player to go to sleep.
            return "Too late to expand rooms"
        if mc.business.funds >= t1_cost:
            return True
        return "Requires: " + str(t1_cost)

    def room_tier_2(roomname):
        if len(filter(lambda x: x.name == roomname, list_of_places)) == 1:
            return "Already owned"
        if time_of_day == 4:    # Force player to go to sleep.
            return "Too late to expand rooms"
        if current_tier < 1:
            return "Requires Dungeon"
        if mc.business.funds < t2_cost:
            return "Requires: " + str(t2_cost)
        return True

    def room_tier_3(roomname):
        if len(filter(lambda x: x.name == roomname, list_of_places)) == 1:
            return "Already owned"
        if time_of_day == 4:    # Force player to go to sleep.
            return "Too late to expand rooms"
        if current_tier < 2:
            return "Requires Security and Machine Room"
        if mc.business.funds < t3_cost:
            return "Requires: " + str(t3_cost)
        return True

    def can_increase_tier():
        if current_tier == 0 and len(filter(lambda x: x.name == "dungeon", list_of_places)) == 1:
            return True
        if current_tier == 1 and len(filter(lambda x: x.name == "security", list_of_places)) == 1 and len(filter(lambda x: x.name == "machinery", list_of_places)) == 1:
            return True
        return False

    # Tier 1 Rooms
    purchase_dungeon_room_action = Action("Install Private Dungeon {image=gui/heart/Time_Advance.png}\n {size=22}Costs: [t1_cost]{/size}", room_tier_1, "purchase_dungeon_room",
        menu_tooltip = "Unlocks a private Dungeon under the main office...", requirement_args = ["dungeon"])
    purchasable_rooms_list.append(purchase_dungeon_room_action)

    # Tier 2 Rooms
    purchase_security_room_action = Action("Install Security Room {image=gui/heart/Time_Advance.png}\n {size=22}Costs: [t2_cost]{/size}", room_tier_2, "purchase_security_room",
        menu_tooltip = "Unlocks a Security Room for non- nefarious purposes...", requirement_args = ["security"])
    purchasable_rooms_list.append(purchase_security_room_action)

    purchase_machinery_room_action = Action("Install Machinery Room {image=gui/heart/Time_Advance.png}\n {size=22}Costs: [t2_cost]{/size}", room_tier_2, "purchase_machinery_room",
        menu_tooltip = "Unlocks a Machinery for the creation of stuff...", requirement_args = ["machinery"])
    purchasable_rooms_list.append(purchase_machinery_room_action)

    # Tier 3 Rooms
    purchase_biotech_room_action = Action("Install Biotech Lab {image=gui/heart/Time_Advance.png}\n {size=22}Costs: [t3_cost]{/size}", room_tier_3, "purchase_biotech_room",
        menu_tooltip = "Unlocks the Biotech Lab for genetic manipulation...", requirement_args = ["biotech"])
    purchasable_rooms_list.append(purchase_biotech_room_action)

label purchase_rooms():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            room_options = []
            for act in purchasable_rooms_list:
                room_options.append(act)
            room_options.append("Back")
            act_choice = call_formated_action_choice(room_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()

# Tier 1 Rooms
label purchase_dungeon_room(): #Enables the dugneon.
    "[office_basement.formalName] accessable from the elevator in [lobby.formalName]"
    if office_basement in mod_rooms_lobby:
        return  # room already exists exit

    $ mc.business.pay(- t1_cost)

    $ office_basement.actions.append(dungeon_action)
    $ mod_rooms_lobby.append(office_basement)
    $ mod_rooms_append.append(office_basement) # Gives an escape through the elevator

    if office_basement not in list_of_places:
        $ list_of_places.append(office_basement)

    $ update_tier = can_increase_tier()
    if update_tier:
        $ current_tier += 1

    $ advance_time()
    return

# Tier 2 Rooms
label purchase_security_room(): #Enables the security room.
    "[m_division_basement.formalName] accessable from the elevator in [lobby.formalName]"
    if m_division_basement in mod_rooms_lobby:
        return  # room already exists exit

    $ mc.business.pay(- t2_cost)

    $ mod_rooms_lobby.append(m_division_basement)
    $ mod_rooms_append.append(m_division_basement) # Gives an escape through the elevator
    $ m_division_basement.actions.append(security_overview_action)

    $ list_of_places.append(m_division_basement)

    $ update_tier = can_increase_tier()
    if update_tier:
        $ current_tier += 1

    $ advance_time()
    return

label purchase_machinery_room(): #Enables the machinery room
    "[p_division_basement.formalName] accessable from the elevator in [lobby.formalName]"
    if p_division_basement in mod_rooms_lobby:
        return  # room already exists exit

    $ mc.business.pay(- t2_cost)

    $ mod_rooms_lobby.append(p_division_basement)
    $ mod_rooms_append.append(p_division_basement) # Gives an escape through the elevator

    $ list_of_places.append(p_division_basement)

    $ update_tier = can_increase_tier()
    if update_tier:
        $ current_tier += 1

    $ advance_time()
    return

# Tier 3 Rooms
label purchase_biotech_room(): #Enables the biotech lab
    "[rd_division_basement.formalName] accessable from the elevator in [lobby.formalName]"
    if rd_division_basement in mod_rooms_lobby:
        return  # room already exists exit

    $ mc.business.pay(- t3_cost)

    $ rd_division_basement.actions.append(biotech_action)
    $ mod_rooms_lobby.append(rd_division_basement)
    $ mod_rooms_append.append(rd_division_basement) # Gives an escape through the elevator

    $ list_of_places.append(rd_division_basement)

    $ advance_time()
    return

#label purchase_dungeon_room(): #Enables the dugneon.
#    if office_basement not in mod_rooms_lobby:
#        $ mod_rooms_lobby.append(office_basement)
#    return
