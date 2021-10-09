init -1 python:
   def coffee_shop_get_coffee_requirement(): # Leave this in
      if time_of_day == 4: # Can be removed
          return "Closed for the night"
      elif mc.business.funds < 5: # $40 per session.
          return "Requires: $5"
      else:
          return True

   # actions available from entry point action
   coffee_shop_get_coffee_action = Action("Order a coffee", coffee_shop_get_coffee_requirement, "coffee_shop_get_coffee_label", menu_tooltip = "Restore some energy with a hot coffee")

label  coffee_shop_get_coffee_label():
    if kaya.location == coffee_shop:
        $ the_person == kaya
        "You step up to the coffee shop counter. [the_person.possessive_title] is working today."
        $ the_person.draw_person()
        if kaya_can_get_barista_quickie():
            the_person "Oh hey [the_person.mc_title]! Here for coffee? Or something a little more intimate?"
            "She gives you a wink."
            mc.name "Just coffee today, I'm exhausted."
        else:
            the_person "Hello [the_person.mc_title]! What can I get you?"
        "You give her your order and pay. Soon she is handing you a cup of fresh coffee."
        $ mc.business.change_funds(-5)
        menu:
            "Leave a tip":
                "You drop an extra $5 in the tip jar."
                $ mc.business.change_funds(-5)
                the_person "Aww, thank you!"
                $ the_person.change_love(2, 60)
            "No tip":
                pass
        "You sit down at a table an enjoy the fresh brew. The flavor and caffeine perks you up a bit."
        $ mc.change_energy(30)


    else:
        "You step up to the coffee shop counter. You order yourself a coffee."
        "You sit down at a table an enjoy the fresh brew. The flavor and caffeine perks you up a bit."
        $ mc.change_energy(30)
        $ mc.business.change_funds(-5)
