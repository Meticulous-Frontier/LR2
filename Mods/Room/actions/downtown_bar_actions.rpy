init -1 python:
   downtown_bar_actions = [] # These actions are currently linked in business_basement.rpy

init 3 python:

   def order_drink_requierement():
      if time_of_day != 0:
         return True
      return False
   
   order_drink_action = Action("Order a drink", order_drink_requierement, "order_drink_label", menu_tooltip = "Buy yourself something to drink or offer someone else.")
          

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

label order_drink_label():
   "You got yourself a glass of water costing you negative $5. Congratulations."
   $ mc.business.pay(+5)
   return