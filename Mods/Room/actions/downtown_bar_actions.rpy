init -1 python:
   def downtown_bar_actions_requirement(): # Enables a buffer menu that builds itself the way Special Role Actions do, can be used if you want branching menus.
      return True

   def downtown_bar_drink_requirement(): # Leave this in
      return True

   # leave this function in for now for save game compatibility, can be removed in future version.
   def order_drink_requierement():
      return

   # actions available from entry point action
   downtown_bar_drink_action = Action("Order a drink", downtown_bar_drink_requirement, "downtown_bar_drink_label", menu_tooltip = "Order youself a drink...")
   downtown_bar_actions = [downtown_bar_drink_action] # Actions in a sub-menu

   # entry point action linked to room
   downtown_bar_action = Action("Approach the counter.", downtown_bar_actions_requirement, "downtown_bar_actions", menu_tooltip = "More options...")

   
label downtown_bar_actions():
   python: #Generate a list of options from the actions that have their requierement met, plus a back button in case the player wants to take none of them.
      downtown_bar_options = []
      for act in downtown_bar_actions:
         downtown_bar_options.append(act)
      downtown_bar_options.append("Back")
      act_choice = call_formated_action_choice(downtown_bar_options)

   if act_choice != "Back":
      $ act_choice.call_action()
   return

label downtown_bar_drink_label():
   "You got yourself a glass of water costing you negative $5. Congratulations."
   $ mc.business.pay(+5)
   
   if time_of_day is not 4:
      "But you spent a couple of hours drinking it. Game balance."  
      call advance_time from _call_advance_time_downtown_bar_actions
   else:
      "Wait, no. It's night time so you ought to pay back those $5, because of reasons."
      $ mc.business.pay(-5)  
   return