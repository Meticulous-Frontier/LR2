init -1 python:
    purchasable_room = []
    t1_cost = 10000
    t2_cost = 50000
    t3_cost = 100000

    purchase_rooms_mod_init = False

init 2 python:
    def purchase_rooms_mod_requirement():
        if purchase_rooms_mod_init == False:
            return True
        return False

    purchase_rooms_mod_init_action = Action("Purchase Rooms Enabler", purchase_rooms_mod_requirement, "purchase_rooms_mod_init_label",
        menu_tooltip = "Enables the mod")
    if not purchase_rooms_mod_init_action in mod_list:
        mod_list.append(purchase_rooms_mod_init_action)

label purchase_rooms_mod_init_label():
    python:
        office.actions.append(purchase_rooms)
        purchase_rooms_mod_init = True
    if purchase_rooms_mod_init == True:
        "Purchasable rooms added to office"
    return

# Categorized rooms into tiers for their cost.
# TODO: Show different disabled message if room purchased
init 2 python:

    def purchase_rooms_requirement():
        return True

    purchase_rooms = Action("Purchase Rooms", purchase_rooms_requirement, "purchase_rooms",
        menu_tooltip = "Purchase rooms and facilities")

    def room_tier_1():
        if mc.business.funds >= t1_cost:
            return True
        return "Requires: " + str(t1_cost)

    def room_tier_2():
        if mc.business.funds >= t2_cost:
            return True
        return "Requires: " + str(t2_cost)

    def room_tier_3():
        if mc.business.funds >= t3_cost:
            return True
        return "Requires: " + str(t3_cost)


    # Tier 1 Rooms
    purchase_dungeon_room = Action("Install Dungeon Room {image=gui/heart/Time_Advance.png}", room_tier_1, "purchase_dungeon_room",
        menu_tooltip = "Unlocks the dungeon below the main office") #requirment_args have to be contained in a list.
    purchasable_room.append(purchase_dungeon_room)

    # Tier 2 Rooms
    purchase_security_room = Action("Install Security Room {image=gui/heart/Time_Advance.png}", room_tier_2, "purchase_security_room",
        menu_tooltip = "Opens a new division in the basement, accessed through the lobby elevator") #requirment_args have to be contained in a list.
    purchasable_room.append(purchase_security_room)

    purchase_machinery_room = Action("Install Machinery Room {image=gui/heart/Time_Advance.png}", room_tier_2, "purchase_machinery_room",
        menu_tooltip = "Opens a new division in the basement, accessed through the lobby elevator") #requirment_args have to be contained in a list.
    purchasable_room.append(purchase_machinery_room)

    # Tier 3 Rooms
    purchase_biotech_room = Action("Install Biotech Room {image=gui/heart/Time_Advance.png}", room_tier_3, "purchase_biotech_room",
        menu_tooltip = "Opens a new division in the basement, accessed through the lobby elevator") #requirment_args have to be contained in a list.
    purchasable_room.append(purchase_biotech_room)

label purchase_rooms():

    python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            room_options = []
            for act in purchasable_room:
                room_options.append(act)
            room_options.append("Back")
            act_choice = call_formated_action_choice(room_options)

            if act_choice == "Back":
                renpy.jump("game_loop")
            else:
                act_choice.call_action()

# Tier 1 Rooms
label purchase_dungeon_room(): #Enables the dugneon.
    if office_basement not in mod_rooms_lobby:
        $ mc.business.funds -= t1_cost
        $ mod_rooms_lobby.append(office_basement)
        $ advance_time()
    jump purchase_rooms

# Tier 2 Rooms
label purchase_security_room(): #Enables the security room.
    if m_division_basement not in mod_rooms_lobby:
        $ mc.business.funds -= t2_cost
        $ mod_rooms_lobby.append(m_division_basement)
        $ advance_time()
    jump purchase_rooms

label purchase_machinery_room(): #Enables the machinery room
    if p_division_basement not in mod_rooms_lobby:
        $ mc.business.funds -= t2_cost
        $ mod_rooms_lobby.append(p_division_basement)
        $ advance_time()
    jump purchase_rooms

# Tier 3 Rooms
label purchase_biotech_room(): #Enables the biotech lab
    if rd_division_basement not in mod_rooms_lobby:
        $ mc.business.funds -= t3_cost
        $ mod_rooms_lobby.append(rd_division_basement)
        $ advance_time()
    jump purchase_rooms

#label purchase_dungeon_room(): #Enables the dugneon.
#    if office_basement not in mod_rooms_lobby:
#        $ mod_rooms_lobby.append(office_basement)
#    return
