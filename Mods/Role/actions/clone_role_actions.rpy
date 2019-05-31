# Labels
label clone_recall(person):
    "You order [person.title] back to [rd_division_basement.name]"

    $ mc.location.move_person(person, rd_division_basement)

    person.char "Okay, [person.mc_title]. I'll head there next."
    return
