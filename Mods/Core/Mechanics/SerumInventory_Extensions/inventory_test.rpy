# Enables inventories for Rooms and MainCharacter that enables us to store SerumDesigns in them and play around with effects of that.
# NOTE: Done some extensive testing, re- made screens to support the usecase of Items, stacked SerumDesigns, custom objects etc. and it all works fine,
# but it is better left for later. Had to re- make and "unify" the MC Inventory and serum_trade_ui plus create inventories for Rooms, People and a separate inventory for MC holding active serums.


# init -1 python:
#     list_of_items = [] # Holds items. Items are Pre- made SerumDesigns with SerumTraits (Keep non- suitable traits out of list_of_traits)
#
# init 5 python:
#
#     add_label_hijack("normal_start", "store_inventory_system")
#     add_label_hijack("after_load", "store_inventory_system")
#
#
#
# label store_inventory_system(stack):
# 
#     python:
#         for room in list_of_places: # Setup inventories for Rooms here. Deal with people's when given items since this doesnt cover random created people.
#             if not hasattr(room, "inventory"):
#                 room.inventory = SerumInventory([]) # Items that can be obtained / stored in the room.
#                 room.inventory.name = room.formalName + "'s Inventory"
#
#                 room.active_inventory = SerumInventory([]) # Items in the room that will have an effect on the location
#                 room.active_inventory.name = room.formalName + "'s Active Effects"
#
#         if not hasattr(mc.inventory, "name"):
#             mc.inventory.name = "Your Inventory"
#
#             mc.active_inventory = SerumInventory([]) # Allow the MainCharacter to consume traits / wearables / consumables themselves.
#             mc.active_inventory.name = "Active Effects"
#
#         if not hasattr(mc.business.inventory, "name"):
#             mc.business.inventory.name = mc.business.name + "'s Inventory"
#
#         execute_hijack_call(stack)
#
#
#     return
#
# init 10 python:
#
#     def advance_time_room_run_turn_requirement():
#         return True
#     advance_time_room_run_turn = ActionMod("Run Room Effect(s)", advance_time_room_run_turn_requirement, "advance_time_room_run_turn_label", priority = advance_time_people_to_process_action.priority + 1, menu_tooltip = "Applies the effect of items / serums in the room to people present")
#     advance_time_action_list.append(advance_time_room_run_turn)
#
#     def advance_time_people_inventory_effects_requirement():
#         return True
#
#
# label advance_time_room_run_turn_label():
#
#     "Room Effects" #DEBUG
#     python:
#         for room in list_of_places:
#             for person in room.people:
#                 if person in room.people: # We only spend charges (if any) and run the effects if there's a person in the room at the time.
#                     for serum in room.active_inventory.get_serum_type_list(): # Run the effects of all the serums / items in the location on the people present.
#                         serum.run_on_turn(person) #Run the serum's on_turn funcion if it has one.
#                         if serum.duration_expired(): #Returns true if the serum effect is suppose to expire in this time, otherwise returns false. Always updates duration counter when called.
#                             room.active_inventory.change_serum(serum, - 1) # Decrease the amount in the stack by 1 everytime until none are left, in which case they are removed.
#                             #serum.run_on_remove(person) #NOTE: Get something like this to work? Effects are not attached to the person so doesn't nescessarily make sense.
#                             serum.duration_counter += - serum.duration #Since we are dealing with 1 instance of the serum reset the duration counter every time it hits the limit.
#     return
