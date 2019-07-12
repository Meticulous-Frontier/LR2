init -1 python:
   downtown_bar_actions = [] # Actions in a sub-menu
   
   #def update_custom_room_actions(room, action): # Replaces the actions in the room.actions list with the updated version. (Comparison is too exact for this to work at the moment)
    #  for i in range(len(room.actions)):
     #    if room.actions[i] == action:
      #         room.actions[i] = action
      #return

init 2 python: # Downtown Bar Actions Requirements

   def downtown_bar_actions_requirement(): # Enables a buffer menu that builds itself the way Special Role Actions do, can be used if you want branching menus.
      return True

   def downtown_bar_drink_requirement(): # Leave this in
      return True

   downtown_bar_action = Action("Approach the counter.", downtown_bar_actions_requirement, "downtown_bar_actions", menu_tooltip = "More options...")


   downtown_bar_drink_action = Action("Order a drink", downtown_bar_drink_requirement, "downtown_bar_drink_label", menu_tooltip = "Order youself a drink...")
   if downtown_bar_drink_action not in downtown_bar_actions:
      downtown_bar_actions.append(downtown_bar_drink_action)

label downtown_bar_enable_actions(): # Called from tutorial label
   if downtown_bar_action not in downtown_bar.actions:
      $ downtown_bar.actions.append(downtown_bar_action)
   return
   
label downtown_bar_actions():
    while True:
        python: #Generate a list of options from the actions that have their requierement met, plus a back button in case the player wants to take none of them.
            downtown_bar_options = []
            for act in downtown_bar_actions:
               downtown_bar_options.append(act)
            downtown_bar_options.append("Back")
            act_choice = call_formated_action_choice(downtown_bar_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()

label downtown_bar_drink_label():
   "You got yourself a glass of water costing you negative $5. Congratulations."
   $ mc.business.pay(+5)
   
   if time_of_day is not 4:
      "But you spent a couple of hours drinking it. Game balance."  
      call advance_time
   else:
      "Wait, no. It's night time so you ought to pay back those $5, because of reasons."
      $ mc.business.pay(-5)  
   return