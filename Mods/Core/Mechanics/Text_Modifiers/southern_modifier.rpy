init 5 python:
    ####################################################
    # Activate text modifier for person:			   #
    # the_person.text_modifiers.append(southern_belle) #
    ####################################################


    # word replacer (no special chars like - or ')
    southern_dict = {
        "everyone": "y'all",
        "mouth": "gizzard",
        "happy": "tickled pink",
        "stop": "cut",
        "crazy": "ding-dong",
        "suppose": "reckon'",
        "supposed": "reckon'd",
        "get": "git",
        "on": "own",
        "my": "mah",
        "can": "cain",
        "daddy": "diddy",
        "said": "sayd",
        "sweet": "swate",
        "yellow": "yellah",
        "hello": "howdie",
        "i": "aah",
        "you": "yah",
        "it": "aht",
        "nice": "fine",
        "your": "yahr",
        "like": "lac",
        "red": "ray-ed",
        "just": "jis",
        "did": "done",
        "already": "done",
        # "mom": "ma",  DON"T USE THIS SINCE mom IS AN ACTUAL VARIABLE
        "true": "right",
        "cute": "precious",
        "aunt": "ant",
        "children": "chillins",
        "pants": "britches",
        "darn": "dagnabit",
        "himself": "hisself"
    }

    # letter replace (in word)
    southern_replace_dict = {
        "ing": "in'"
    }

    # word group replacer
    southern_word_group_dict = {
        "over there": "over yonder",
        "hold on ": "hold your horses ",
        "be quiet": "hush up",
        "stop talking": "hush up",
        "stop it": "cut that out",
        "give me a kiss": "gimme some sugar",
        "going": "fixing",
        "I think": "I reckon",
        "take it easy": "hold your horses",
        "is not ": "ain't ",
        "am not ": "ain't ",
        "are not ": "ain't ",
        "let me ": "lemme ",
        "very good": "real good"
        "is": "",   # often dropped in southern accent
        "are": "",  # often dropped in southern accent
        "  ": " "   # put at end to replace double spaces with single (for removed words)
    }

    def southern_belle(person, what):
        return word_replace(letter_replacer(word_group_replacer(what, southern_word_group_dict), southern_replace_dict), southern_dict)
