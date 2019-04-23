init -1 python:

    opinion = None
    degree = None
    discovered = None

label opinion_edit_label(person_choice):
    $ the_person = person_choice

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
# This should show.
    menu:
        "Yes":
            $ discovered = True

        "No":
            $ discovered = False
    $ the_person.opinions[opinion] = [degree, discovered]
    return
