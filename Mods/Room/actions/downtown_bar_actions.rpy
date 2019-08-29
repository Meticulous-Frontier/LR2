init -1 python:
   def downtown_bar_actions_requirement(): # Enables a buffer menu that builds itself the way Special Role Actions do, can be used if you want branching menus.
      return True

   def downtown_bar_drink_requirement(): # Leave this in
      return True

   # actions available from entry point action
   downtown_bar_drink_action = Action("Order a drink for... {image=gui/heart/Time_Advance.png}", downtown_bar_drink_requirement, "downtown_bar_drink_label", menu_tooltip = "Treat someone with a drink...")
   downtown_bar_actions = [downtown_bar_drink_action] # Actions in a sub-menu

   # entry point action linked to room
   downtown_bar_action = Action("Approach the counter.", downtown_bar_actions_requirement, "downtown_bar_actions", menu_tooltip = "More options...")


label downtown_bar_actions():
   python: #Generate a list of options from the actions that have their requirements met, plus a back button in case the player wants to take none of them.
      downtown_bar_options = []
      for act in downtown_bar_actions:
         downtown_bar_options.append(act)
      downtown_bar_options.append("Back")
      act_choice = call_formated_action_choice(downtown_bar_options)

   if act_choice != "Back":
      $ act_choice.call_action()
   return

label downtown_bar_drink_label():
    $ new_person = create_random_person(create_home_location = False)

    "[downtown_bar.formalName] is Under Construction - Placeholder Action (Probably will be removed)" # A way to generate new people.

    if not mc.location.people: # No one is in the bar so we create a person.
        "The [downtown_bar.formalName] is a desolate place to be..."

        $ new_person.draw_person()
        "Having seated yourself by the counter with no bartender in sight you hear the entry door open up as a woman walks in."


        $ new_person.draw_person(position = "sitting")
        "She seats herself in the longue area, seemingly puzzled by the lack of attendance at the only bar in town."
        "She sits quietly minding her own business..."

        "Do you wish to introduce yourself, perhaps grace her with a free- of charge drink?"

    $ tuple_list = known_people_at_location(mc.location) + unknown_people_at_location(mc.location) + [new_person, "Back"]

    call screen person_choice(tuple_list, draw_hearts = True)

    $ person_choice = _return

    if person_choice == "Back":
        if new_person.mc_title == "Stranger": # If the player had no interest in interacting with the character we remove it from the game. Assuming a proper "Back" button gets added during first time introduction we can do more with this.
            "Not seeing any reason to stick around she promptly leaves, never to be seen again."

        python: # release variables
            del new_person
            renpy.scene("Active")
            
        return # Where to go if you hit "Back".
    else:
        $ the_person = person_choice

    # add person to game
    python:
        if not new_person in mc.location:
            the_person.create_home_location()
            mc.location.add_person(new_person)  

    if the_person.mc_title == "Stranger": # First time introduction that does not return to talk_person
        call person_introduction(the_person) from _call_person_introduction_downtown_bar_drink

    "Since there's no bartender in town you grab a glass of the finest tap water and treat [the_person.title] to a once- in a lifetime experience."
    $ the_person.change_stats(love = 2, happiness = 2)

    the_person.title "Oh, wow. I literally cannot live without water, this is great. Thanks, [the_person.mc_title]!"

    mc.name "Stay healthy and hydrated, [the_person.title]."

    python: # release variables
        del new_person

    if time_of_day == 4:
        "After a night of drinks you decide to head back home to bed."
        $ mc.change_location(bedroom)

    call advance_time from downtown_bar_drink_1

    $ renpy.scene("Active")
    return
