# Challenge concept:
                  # Baseline should be a 50% success rate as other factors will ALWAYS play in one way or another.
                  # Suggestibility increases success chance by 10% per 10 points. 20 sluttiness = 20% increase
                  # Players charisma increases success chance by 5% per point. 2 Charisma = 10% increase
                   # Targets focus decreases success chance by 10% per point. 2 Focus = 20% decrease
                   # Targets obedience increases success chance by 0.1% per point. 100 obedience = 10% increase.
                   # Being in public adds another 20% decrease in success rate.
# TODO: Make a screen and a room action to develop techniques
      # Make the_person will_power be affected by choices made through dialogue and not only during final calculation.
      # Create additional actions and labels
      # Create a serum that gives a "Receptive" role. Instead of handing it out to everyone.

init -1 python:

    # Thematic lists NOTE: These lists should be appendable from within the game
    exhib_list = ["naked", "nude"] # Showing off, not nescessary connected to sluttiness
    voyer_list = ["spying"] # Observing lewd acts
    sub_list = ["submissive"] # Submissive behavior
    preg_list = ["pregnant"] # Pregnancy or pregnancy play
    dom_list = ["dominant"] # Domimant behavior
    sadist_list = [] # Sadistic behavior

    #def suggest_training():
    #    training_progress = training_progress
    #    if training_progress == 10:
    #        return "No more stages"
    #    else:
    #        training_progress += 1
    #        return training_progress

    def mc_suggest():
        suggest_power = 0

        suggest_power += int(mc.charisma*5) # Positive character modifiers
        suggest_power += int(mc.current_stamina*1.5)


        return suggest_power

    def person_will(the_person, approach):
        approach = approach # authority, emotional, accusive
        will_power = 0

        # TODO: This should be cleaned up and completed if possible.
    #    if opinion in the_person.opinions or if opinion in the_person.sexy_opinions:
    #        if the_person.opinions[opinion] <= [-2, True] or the_person.sexy_opinions[opinion] <= [-2, True]:
    #            if degree == 2:
    #                will_power += 20
    #            if degree == 1:
    #                will_power += 15
    #            if degree == 0:
    #                will_power += 10
    #            if degree = -1:
    #                will_power += 5
    #        if the_person.opinions[opinion] >= [-2, False] or the_person.sexy_opinions[opinion] <= [-2, False]:
    #            if degree == 2:
    #                will_power += 20
    #            if degree == 1:
    #                will_power += 15
    #            if degree == 0:
    #                will_power += 10
    #            if degree = -1:
    #                will_power += 5

        if mc.location.public: # If the location is public, check how many people are present and increase difficulty
            will_power += int(len(mc.location.people)*5)

        if approach == "authority":
            will_power += int(the_person.focus * 10)

        elif approach == "emotional":
            pass

        elif approach == "accusive":
            will_power += int(the_person.happiness * 0.2)

        else:
            will_power += int(the_person.focus * 10)
            will_power += int(the_person.happiness * 0.2)

            will_power -= int(the_person.obedience * 0.1)
            will_power -= int(the_person.love * 0.2)
            will_power -= int(the_person.suggestibility * 0.5)



        if any(srchstr in opinion for srchstr in exhib_list): # Check if opinion is in a list
                if the_person in mc.business.get_employee_list(): # Check if the person is employeed
                    if corporate_enforced_nudity_policy.is_owned():
                        will_power -= 10

        # Personality checks

        # Opinion checks

        # Salary check
        if approach == "authority":
            if the_person in mc.business.get_employee_list():
                if the_person.calculate_base_salary() < the_person.salary:
                    will_power -= 2
        return will_power

#$ authority_employees = 65 + (mc.charisma*5) + (the_person.obedience * 0.1) + (the_person.suggestibility * 0.5) - (the_person.focus * 10) # Baseline for employed characters. Will take policies into consideration.
#$ authority = 50 + (mc.charisma*5) + (the_person.obedience * 0.1) + (the_person.suggestibility * 0.5) - (the_person.focus * 10) # Baseline if trying to speak to their obedience, will take personality and likes into consideration.
#$ emotional = 50 + (mc.charisma*5) + (the_person.love * 0.2) + (the_person.suggestibility * 0.5) - (the_person.focus * 10) # Baseline if using "emotional manipulation" aka love stat. Will take personality and likes into consideration.
#$ accusing = 50 + (mc.charisma*5) + (the_person.obedience * 0.1) + (the_person.suggestibility * 0.5) - (the_person.happiness * 0.1) # Baseline if being accusing and trying to "correct" their wrong thinking. Given a bonus if target is "unhappy" / "depressed"

init -1 python:

    opinion = None
    degree = None
    discovered = None

label influence_opinion_label(the_person):
    "Speaker" "Type an opinion e.g 'sculpting garden gnomes' then hit enter to proceed "
    $ opinion = str(renpy.input("Opinion:"))

    "Speaker" "What is [the_person.name]'s thoughts on the opinion?"


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

    "Speaker" "Does the player know about [the_person.name]'s opinion?"

    menu:
        "Yes":
            $ discovered = True

        "No":
            $ discovered = False

    if mc_suggest() > person_will(the_person, "test"):
        "Speaker" "You succeed at making the changes"
        $ the_person.opinions[opinion] = [degree, discovered]

    elif mc_suggest() == person_will(the_person, "test"):
        "Speaker" "You are at a stalemate, try changing your approach"

    elif mc_suggest() < person_will(the_person, "test"):
        "Speaker" "[the_person.name]'s mind rejects your suggestions"
    return
