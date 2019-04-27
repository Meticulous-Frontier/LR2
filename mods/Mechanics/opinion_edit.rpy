# Challenge concept:
                  # Baseline should be a 50% success rate as other factors will ALWAYS play in one way or another.
                  # Suggestibility increases success chance by 10% per 10 points. 20 sluttiness = 20% increase
                  # Players charisma increases success chance by 5% per point. 2 Charisma = 10% increase
                   # Targets focus decreases success chance by 10% per point. 2 Focus = 20% decrease
                   # Targets obedience increases success chance by 0.1% per point. 100 obedience = 10% increase.
                   # Being in public adds another 20% decrease in success rate.
# TODO: Make a screen and a room action to develop techniques
      # Make the_person the_person.willpower be affected by choices made through dialogue and not only during final calculation.
      # Create additional actions and labels
      # Create a serum that gives a "Receptive" role. Instead of handing it out to everyone.
# NOTE: Do checks against the_person.willpower and confirm changes in the_person.willpower with calc_will()

init -1 python:

    # Thematic lists NOTE: These lists should be appendable from within the game
    exhib_list = ["naked", "nude", "topless", "underwear"] # Showing off, not nescessary connected to sluttiness
    voyer_list = ["spying"] # Observing lewd acts
    sub_list = ["submissive"] # Submissive behavior
    preg_list = ["pregnant"] # Pregnancy or pregnancy play
    dom_list = ["dominant"] # Domimant behavior
    sadist_list = [] # Sadistic behavior
#    lewd_list = [] # Keywords that are considered sexual, to determine if something is to be thrown into sexy_opinions_list or opinions_list

    def change_willpower(self, amount, add_to_log = True): #Logs change in willpower and shows new total.
        self.willpower += amount
        if self.willpower < 0:
            self.willpower = 0

        log_string = ""
        log_string_total = ""
        if amount > 0:
            log_string = "+" + str(amount) + " Willpower " + "= " + str(person.willpower) + " Total"
        else:
            log_string = str(amount) + " Willpower " + "= " + str(person.willpower) + " Total"

        if add_to_log and amount != 0:
            mc.log_event(person.name + ": " + log_string, "float_text_blue")
        return person.willpower

    # attach to person object
    Person.change_willpower = change_willpower
    #
    def calc_power():
        mc.power = 0

        mc.power += int(mc.charisma*5) # Positive character modifiers
        mc.power += int(mc.current_stamina*1.5)
        return mc.power

    def calc_will(add_to_log = True): # Base calculation. Run this once.

        the_person.willpower = int(the_person.focus * 10 + the_person.happiness * 0.2 - the_person.obedience * 0.1 - the_person.love * 0.2 - the_person.suggestibility * 0.5)

        if the_person.willpower < 0:
            the_person.willpower = 0

        log_string = str(the_person.willpower) + " Willpower"

        if add_to_log:
            mc.log_event(the_person.name + ": " + log_string, "float_text_blue")
        return the_person.willpower

init -1 python:
    pass

label influence_opinion_input_label():
    # Have the player input an opinion then run checks on how the_person reacts to it.
    "Speaker" "Type an opinion e.g 'sculpting garden gnomes' then hit enter to proceed "
    $ opinion = str(renpy.input("Opinion:"))

    if any(srchstr in opinion for srchstr in exhib_list): # This checks any keyword.
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions): # This is limited to exact matches.
            $ the_person.change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in exhib_list"

    if any(srchstr in opinion for srchstr in voyer_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ the_person.change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in voyer_list"

    if any(srchstr in opinion for srchstr in sub_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ the_person.change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in sub_list"

    if any(srchstr in opinion for srchstr in preg_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ the_person.change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in preg_list"

    if any(srchstr in opinion for srchstr in dom_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ the_person.change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in dom_list"

    if any(srchstr in opinion for srchstr in sadist_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ the_person.change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in sadist_list"

    "Speaker" "How do you want [the_person.name] to feel about [opinion]?"
    menu:
        "Hate":
            $ degree = -2
        "Dislike":
            $ degree = -1
        "Neutral": #This will not display, can be used to "remove" an opinion without the need for additional code.
            $ degree = 0
        "Like":
            $ degree = 1
        "Love":
            $ degree = 2
        "Back":
            return

    if not the_person.get_opinion_topic(opinion) is None:
        python:
            score = the_person.get_opinion_score(opinion)
            degrees = [-2,-1,0,1,2]
            change = abs(degrees.index(score) - degrees.index(degree)) # How far is the degree away from current opinion (max 4 steps)
            cur_score = opinion_score_to_string(score) 
            the_person.change_willpower(change * 5)

        if change == 1: # small change
            "Speaker" "[the_person.name] [cur_score] [opinion], so she will put up not much resistance."
        elif change == 2: # medium change
            "Speaker" "[the_person.name] [cur_score] [opinion], so she will put up a little resistance."
        elif change == 3: # large change
            "Speaker" "[the_person.name] [cur_score] [opinion], so she will put up some resistance."
        elif change == 4: # very large change
            "Speaker" "[the_person.name] [cur_score)] [opinion], so she will put up a lot of resistance."


#    "Speaker" "Does the player know about [the_person.name]'s opinion?" NOTE: Might as well assume yes, because the player is determining it.
#
#    menu:
#        "Yes":
#            $ discovered = True
#
#        "No":
#            $ discovered = False
#    $ add_opinion(opinion, degree, discovered)
    $ discovered = True
    call influence_opinion_end_label
