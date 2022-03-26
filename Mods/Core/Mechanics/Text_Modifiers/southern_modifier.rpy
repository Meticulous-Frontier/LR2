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
        "father": "diddy",
        "said": "sayd",
        "sweet": "swate",
        "yellow": "yellah",
        "hello": "howdy",
        #"i": "ah",
        "a": "ah",
        "you": "yah",
        #"it": "aht",
        "to": "tuh",
        #"the": "thu",
        "nice": "fine",
        "your": "yahr",
        "like": "lac",
        "red": "ray-ed",
        "just": "jis",
        "did": "done",
        "already": "done",
        "mom": "mamma",
        "mother": "mamma",
        "true": "right",
        "cute": "precious",
        "aunt": "ant",
        "children": "chillins",
        "pants": "britches",
        "darn": "dagnabit",
        "himself": "hisself",
        "yes": "yessir",
        "something": "sumthing",
        "things": "thangs",
        "because": "cuz",
        "love": "luv",
        "what": "whut",
        "want": "wonna",
        "nothing": "nuthing",
    }

    # letter replace (in word)
    southern_replace_dict = {
        "ing": "in'",
        "some": "sum",
        "other": "uther",
        "irst": "ursd"
    }

    # word group replacer
    southern_word_group_dict = {
        "over there ": "over yonder",
        "hold on ": "hold your horses",
        "be quiet ": "hush up",
        "stop talking ": "hush up",
        "stop it": "cut that out",
        "give me a kiss": "gimme some sugar",
        "going": "fixing",
        "I think": "I reckon",
        "take it easy": "hold your horses",
        " is not ": " ain't ",
        " is all ": " 'sall ",
        "isn't": "ain't",
        " am not ": " ain't ",
        " are not ": " ain't ",
        "aren't": "ain't",
        "you all": "y'all",
        "let me": " lemme",
        "very good": "real good",
        "yes sir": "yes", # replace with yes (word replacer will make it yessir)
        " is ": " ",   # often dropped in southern accent
        " are ": "'re ",  # should result in (those are -> those're)
    }

    def southern_belle(person, what):
        return word_replace(letter_replacer(word_group_replacer(what, southern_word_group_dict), southern_replace_dict), southern_dict)
