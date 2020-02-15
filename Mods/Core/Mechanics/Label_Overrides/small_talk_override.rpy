# Overrides some of the opinion keys in the dialog with a more sensible dialog topic

init 5 python:
    opinions_talk_mapping = {
        "skirts": "girls in skirts",
        "pants": "girls wearing pants",
        "dresses": "girls in a dress",
        "high heels": "girls in high heels",
        "boots": "girls wearing boots",
        "sports": "working out",
        "hiking": "going hiking",
        "jazz": "jazz music",
        "punk": "punk music",
        "classical": "classical music",
        "pop": "pop music",
        "make up": "girls who wear makeup",
        "giving blowjobs": "getting blowjobs",
        "giving handjobs": "getting handjobs",
        "giving tit fucks": "fucking tits",
        "being fingered": "fingering a girl",
        "showing her tits": "looking at tits",
        "showing her ass": "looking at butts",
        "being submissive": "submissive girls",
        "drinking cum": "cumming in mouths",
        "cum facials": "cumming on faces",
        "being covered in cum": "covering girls in cum",
        "big dicks": "girls who love big cocks",
        "cheating on men": "having affairs",
    }

    config.label_overrides["small_talk_person"] = "small_talk_person_enhanced"


label small_talk_person_enhanced(person):
    python:
        mc.change_energy(-15)
        smalltalk_opinion = person.get_opinion_score("small talk")
        renpy.say(mc.name, "So [person.title], what's been on your mind recently?")
        person.discover_opinion("small talk")
        successful_smalltalk = 60 + (smalltalk_opinion * 20) + (mc.charisma * 5)
        ran_num = renpy.random.randint(0,100)

    # TODO: Add a chance that she wants to talk about someone she knows.
    if ran_num < successful_smalltalk:
        if smalltalk_opinion >= 0:
            $ person.draw_person(emotion = "happy")
            "She seems glad to have a chance to take a break and make small talk with you."

        else:
            "She seems uncomfortable with making small talk, but after a little work you manage to get her talking."

        python:
            casual_sex_talk = person.sluttiness > 50
            opinion_learned = person.get_random_opinion(include_known = True, include_sexy = casual_sex_talk)
            talk_opinion_text = opinion_learned
            if opinion_learned in opinions_talk_mapping:
                talk_opinion_text = opinions_talk_mapping[opinion_learned]


        if not opinion_learned is None:
            $ opinion_state = person.get_opinion_topic(opinion_learned)
            $ opinion_string = opinion_score_to_string(opinion_state[0])

            "The two of you chat pleasantly for half an hour."
            person.char "So [person.mc_title], I'm curious what you think about about [opinion_learned]. Do you have any opinions on it?"
            $ love_gain = 4
            $ prediction = 0
            menu:
                "I love [talk_opinion_text].":
                    $ prediction = 2
                    mc.name "Me? I love [talk_opinion_text]. Absolutely love it."

                "I like [talk_opinion_text].":
                    $ prediction = 1
                    mc.name "I really like [talk_opinion_text]."

                "I don't have any opinion about [talk_opinion_text].":
                    $ prediction = 0
                    mc.name "I don't really have any thoughts on it, I guess I just don't think it's a big deal."

                "I don't like [talk_opinion_text].":
                    $ prediction = -1
                    mc.name "I'm not a fan, that's for sure."

                "I hate [talk_opinion_text].":
                    $ prediction = -2
                    mc.name "I'll be honest, I absolutely hate [talk_opinion_text]. I just can't stand it."

            $ prediction_difference = abs(prediction - opinion_state[0])
            if prediction_difference == 4: #as wrong as possible
                person.char "Really? Wow, we really don't agree about [opinion_learned], that's for sure."
            elif prediction_difference == 3:
                person.char "You really think so? Huh, I guess we'll just have to agree to disagree."
            elif prediction_difference == 2:
                person.char "I guess I could understand that."
            elif prediction_difference == 1:
                person.char "Yeah, I'm glad you get it. I feel like we're both on the same wavelength."
            else: #prediction_difference == 0
                person.char "Exactly! It's so rare that someone feels exactly the same way about [opinion_learned] as me!"


            if opinion_state[1]:
                "You listen while [person.possessive_title] talks about how she [opinion_string] [opinion_learned]."
            else:
                $ person.discover_opinion(opinion_learned)
                "You listen while [person.possessive_title] talks and discover that she [opinion_string] [opinion_learned]."

            $ person.change_love(love_gain - prediction_difference)

        else:
            "You and [person.possessive_title] chat for a while. You don't feel like you've learned much about her, but you both enjoyed talking."

        $ smalltalk_bonus = smalltalk_opinion + 1
        $ person.change_happiness(smalltalk_bonus)
        if smalltalk_opinion >= 0:
            person.char "It was nice chatting [person.mc_title], we should do it more often!"
        else:
            person.char "So uh... I guess that's all I have to say about that..."
            "[person.char] trails off awkwardly."
    else:
        if smalltalk_opinion < 0:
            person.char "Oh, not much."
            $ person.change_happiness(smalltalk_opinion)
            "You try and keep the conversation going, but making small talk with [person.title] is like talking to a wall."
        else:
            person.char "Oh, not much honestly. How about you?"
            $ person.change_happiness(smalltalk_opinion)
            "[person.possessive_title] seems happy to chitchat, and you spend a couple of hours just hanging out."
            "You don't feel like you've learned much about her, but least she seems to have enjoyed talking."

    $ person.apply_serum_study()
    return