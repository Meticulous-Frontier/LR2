init 5 python:
    add_label_hijack("normal_start", "update_stephanie")

# fix stephanie random generation, since the game becomes more difficult
# when has a negative attitude towards certain opinions.
label update_stephanie(stack):
    python:
        stephanie.opinions["research work"] = [2, True]  # she loves research work
        stephanie.opinions["small talk"] = [1, False]  # she likes small talk
        stephanie.opinions["flirting"] = [1, False]  # she likes flirting

        stephanie.sexy_opinions["kissing"] = [1, False]  # she likes kissing
        stephanie.sexy_opinions["vaginal sex"] = [2, False] # she likes having sex

        execute_hijack_call(stack)
    return

