init -1 python:
    Person._list_of_eyes.append(["emerald", [0.305, 0.643, 0.607, 1.0]])

    found = next((x for x in Person._list_of_eyes if x[0] == 'brown'), None)
    if found:
        found[1] = [.62, .42, .29, 1.0]
