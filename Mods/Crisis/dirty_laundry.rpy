## Dirty Laundy crisis by Starbuck!
# Scene: You go to do your laundry before bed, but notice your sister / mom has clean clothes stacked next to the dryer.
# Player has option to masturbate into clean panties and put them back.
# 50% chance mom or sister catches MC in the act. TODO higher chance at higher sluttiness? 50/50? Have cum soaked panties have some kind of effect on the person?
# Zero sluttiness they get angry, gives chance for obedience check?
# Low sluttiness they watch and touch themselves
# Mid sluttiness they give MC a handjob with the panties in their hand
# high sluttiness they put the panties on and have MC cum in the panties while they wear them

init -1 python:
    dirty_laundry_weight = 0  #Disable for now

init 2 python:
    def dirty_laundry_requirement():
        if mc_asleep():
            if mc_at_home():
                return True
        return False
    #
    # dirty_laundry_action = ActionMod("Dirty Laundry", dirty_laundry_requirement, "dirty_laundry_action_label",
    #     menu_tooltip = "Start your laundry before bed.", category = "Home", is_crisis = True, crisis_weight = dirty_laundry_weight)

label dirty_laundry_action_label:

    $ the_person = get_random_from_list(people_in_mc_home())
    $ the_panties = get_random_from_list(people_in_mc_home())

    "You are just drifting off to sleep when you suddenly you remember. You don't have any clean clothes for tomorrow!"
    "You look a the clock. It is already pretty late. You guess that your family is already asleep, so you grab your laundry and take it to the laundry room just wearing your boxers."
    "You throw your laundry in the washing machine, add some detergent and start it up."
    "As you are thinking about what to do for the next 30 minutes while the washer runs and you can move your clothes to the dryer, you notice a laundry basket on the floor filled with clean, folded clothes."
    "It looks like they all belong to [the_panties.title]. Sitting on top of the laundy is a pair of sexy black panties."
    "You feel your cock stir when you think about the ass those panties cover. Maybe while you wait for your laundry you could relieve some tension fantasizing about that..."
    menu:
        "Masturbate with panties":
            #TODO
            pass
        "Find something else to do":
            "You decide to do something else. You head back to room and hop on your PC, doing work related tasks until the washer is done."
            "You go back to swap your laundry to the dryer."
            $ the_panties.draw_person()
            "[the_panties.title] is just coming out of the laundry room with her laundry basket."
            #TODO outfit and text based on her sluttiness.
            "You say goodnight to [the_panties.title] and then swap your clothes from the washer to the dryer. They should be dry in the morning!"
            $ renpy.scene("Active")
            return



    $ renpy.scene("Active")
    $ the_person.review_outfit(show_review_message = False)
    return
