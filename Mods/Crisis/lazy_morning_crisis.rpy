## Lazy Morning Crisis Mod by Starbuck

init -1 python:
    lazy_morning_mod_weight = 7 #Higher weight since it only occurs on weekends.

init 2 python:
    def lazy_morning_crisis_requirement():
        if mc_at_home() and time_of_day == 0:
            if mc.business.is_weekend():
                return True
        return False

    def lazy_morning_mod_initialization(self):
        pass #???? Do I need something here? TODO
        return
    #
    # lazy_morning_crisis_action = ActionMod("Lazy Morning", lazy_morning_crisis_requirement,"lazy_morning_crisis_action_label", initialization = lazy_morning_mod_initialization,
    #     menu_tooltip = "You sleep in.", category="Home", is_crisis = True, is_morning_crisis = True, crisis_weight = lazy_morning_mod_weight)
        #TODO this is disabled for now.
label lazy_morning_crisis_action_label:

    $ the_person = get_random_from_list(people_in_mc_home()) #Checks all the rooms in player's home

    "Your eyes slowly open when you alarm goes off. It feels like your arms weigh a hundred pounds each when you reach over and turn off your alarm."#TODO change pounds to kilos if metric is active.
    "It's time to get up... but is it really though? It's the weekend. There's probably some things you could get done."
    "But what sounds even better? You roll over and enjoy the comfort of your bed. You know you should get up, do something productive. But wouldn't you be more productive long term, if you got more sleep now?"
    "You finally stop reasoning with yourself and drift back to sleep."

    "You aren't sure how long it is, but you are startled awake when your bedroom door suddenly opens."
    the_person.char "[the_person.mc_title] I have a quick question about... OH!"
    $ the_person.draw_person()

    if the_person == mom:
        the_person.char "I'm sorry honey! I didn't realize you were sleeping in!"
    elif the_person == lily:
        the_person.char "What? You're still sleeping? You know the morning is almost over right?"
    elif the_person == aunt:
        the_person.char "I'm sorry, I didn't realize you weren't up yet!"
    elif the_person == cousin:        #Wow, congrats on getting her so slutty while shes living with you!
        the_person.char "Wow, I can't beieve you're still sleeping. Up late beating off to crazy porn or something, ya perv?."
    else:                           #Someone else someday? A live in girlfriend maybe?
        the_person.char "I'm sorry [the_person.mc_title], I forgot its the weekend!"

    "She looks at you for a minute as she decides what to do."
    if the_person.sluttiness < 20: #Not slutty, she excuses herself.
        mc.name "What do you want?!?"

    elif the_person.sluttiness < 50: #She asks to join you and you wind up dry humping
        pass
    elif the_person.sluttiness < 75: #She asks to join you and you fuck
        pass
    else:    #She jumps you
        pass

    python:
        the_person.reset_arousal()
        the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
        mc.location.show_background()
        renpy.scene("Active")
    return
