# if suggestability is enabled now depends on the lysergide_n2o_serum
# the serum adds the role action to a person and removes it when
# the serum wears off

init 2 python: # Define actions and requirements for the actual mod here.

    def influence_opinion_requirement(person): # Shows only if person has been affected by suggestibility serum.
        if suggestable_role in person.special_role:
            return True
        else:
            return False

    influence_opinion_action = Action("Influence an opinion", influence_opinion_requirement, "influence_opinion_label",
        menu_tooltip = "Influence a persons opinion regarding a specific topic")

    suggestable_role = Role("Suggestable", [influence_opinion_action])

# Actions for the receptive role in suggestable_role.rpy

label influence_opinion_label(person): #Input a custom opinion, check if they have the opinion or not and base difficulty on how big the change is, or random up to 80 if it's a unrelated opinion

    $ opinion = None
    $ degree = None
    $ discovered = True
    # Pre-check to let the player know base information about the scenario.
    "Speaker" "Type an opinion e.g 'sculpting garden gnomes' then hit enter to proceed "
    $ opinion = str(renpy.input("Opinion:"))

    "Speaker" "How do you want [person.name] to feel about [opinion]?"
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

    python:
        score = person.get_opinion_score(opinion)
        degrees = [-2,-1,0,1,2]
        change = abs(degrees.index(score) - degrees.index(degree)) # How far is the degree away from current opinion (max 4 steps)
        cur_score = opinion_score_to_string(score)

    if score is not 0:
        "Speaker" "[person.possessive_title] [cur_score] [opinion], depending on how drastic the change and how suggestable the person is you might succeed."
    else:
        "Speaker" "[person.possessive_title], currently has no opinion regarding [opinion], depending on how suggestable the person is you might succeed"

    if change == 1: # small change
        $ difficulty = renpy.random.randint(0, 20) # Using ranges so people can get lucky, and it can give different outcomes faking simulation of psychology
    elif change == 2: # medium change
        $ difficulty = renpy.random.randint(20, 40)
    elif change == 3: # large change
        $ difficulty = renpy.random.randint(40, 60)
    elif change == 4: # very large change
        $ difficulty = renpy.random.randint(60, 80)
    else:
        $ difficulty = renpy.random.randint(0, 80) #Anything above 80 should be an auto- success

    if person.suggestibility >= difficulty:
        $ person.add_opinion(opinion, degree, discovered)
        $ new_score = opinion_score_to_string(person.get_opinion_score(opinion))
        "Speaker" "You succeed at influencing [person.possessive_title]'s' opinion to now [new_score] [opinion]"


    else:
        "Speaker" "[person.possessive_title] doesn't seem to agree with your suggestion regarding [opinion]"
        "Speaker" "Making her more suggestable might help you out."

    $ person.special_role.remove(suggestable_role)
    $ mc.log_event((person.title or person.name) + " is no longer suggestable.", "float_text_blue")

    $ renpy.scene("Active")
    return
