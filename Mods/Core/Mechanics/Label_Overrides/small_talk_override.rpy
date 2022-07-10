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

    text_opinion_list = ["I hate", "I don't like", "I have no opinion on", "I like", "I love"]

    def build_opinion_smalltalk_list(opinion_text, opinion_score):
        opinion_list = []
        for menu_score in __builtin__.range(5):
            opinion_string = text_opinion_list[4 - menu_score] + " " + opinion_text
            if opinion_score[1] and opinion_score[0] == 2 - menu_score:
                opinion_string = "{color=00E000}" + opinion_string + "{/color}"
            opinion_list.append([opinion_string, 2 - menu_score])
        opinion_list.insert(0, "Smalltalk")
        return opinion_list

    def get_learned_opinion(person):
        # remove randomness for dark chocolate opinion
        if person.get_opinion_score("dark chocolate") != person.get_known_opinion_score("dark chocolate"):
            opinion_learned = "dark chocolate"
        else:
            opinion_learned = person.get_random_opinion(include_known = True, include_sexy = person.effective_sluttiness() > 50)
            retries = 0
            while opinion_learned == the_person.event_triggers_dict.get("last_opinion_learned", "unknown") and retries < 3:
                opinion_learned = person.get_random_opinion(include_known = True, include_sexy = person.effective_sluttiness() > 50)
                retries += 1

        talk_opinion_text = opinion_learned
        if opinion_learned in opinions_talk_mapping:
            talk_opinion_text = opinions_talk_mapping[opinion_learned]

        return (opinion_learned, talk_opinion_text)



label small_talk_person_enhanced(person, apply_energy_cost = True, is_phone = False):
    python:
        if apply_energy_cost:
            mc.change_energy(-15)
        renpy.say(mc.name, "So [person.title], what's been on your mind recently?")
        person.discover_opinion("small talk")

    # TODO: Add a chance that she wants to talk about someone she knows.
    if not is_phone and person.love > 5 and not person.event_triggers_dict.get("job_known", True):
        if person.job == unemployed_job:
            person "Well, it's hard to make ends meet, but I'll figure it out."
            "She tells you that it is not easy when you have no job."
        elif person in unique_character_list:
            "You chit chat for a while, about life, aspirations and dreams."
        else:
            person "Just having some issues at work, but nothing I can't handle."
            "She tells you about her job and its challenges."
        $ person.event_triggers_dict["job_known"] = True
    elif renpy.random.randint(0,100) < 60 + (person.get_opinion_score("small talk") * 20) + (mc.charisma * 5):
        if is_phone:
            "There's a short pause, then [person.title] texts you back."
        else:
            if person.get_opinion_score("small talk") >= 0:
                $ person.draw_person(emotion = "happy")
                "She seems glad to have a chance to take a break and make small talk with you."
            else:
                "She seems uncomfortable with making small talk, but after a little work you manage to get her talking."

        $ (opinion_learned, talk_opinion_text) = get_learned_opinion(person)
        if not opinion_learned is None:
            $ opinion_state = person.get_opinion_topic(opinion_learned)
            $ opinion_string = opinion_score_to_string(opinion_state[0])
            $ the_person.event_triggers_dict["last_opinion_learned"] = opinion_learned

            if is_phone:
                person "Oh, this and that."
                "The two of you text back and forth between each other for half an hour." #TODO: Either play out that conversation or add some message history to fill it in.
            else:
                "The two of you chat pleasantly for half an hour."

            person "So [person.mc_title], I'm curious what you think about [talk_opinion_text]. Do you have any opinions on it?"

            call screen enhanced_main_choice_display(build_menu_items([build_opinion_smalltalk_list(talk_opinion_text, opinion_state)]))

            if is_phone:
                $ mc_opinion_string = opinion_score_to_string(_return).rstrip('s').replace('has', 'have')
                mc.name "I [mc_opinion_string] [talk_opinion_text]."

            $ prediction_difference = __builtin__.abs(_return - opinion_state[0])
            if prediction_difference == 4: #as wrong as possible
                person "Really? Wow, we really don't agree about [opinion_learned], that's for sure."
            elif prediction_difference == 3:
                person "You really think so? Huh, I guess we'll just have to agree to disagree."
            elif prediction_difference == 2:
                person "I guess I could understand that."
            elif prediction_difference == 1:
                person "Yeah, I'm glad you get it. I feel like we're both on the same wavelength."
            else: #prediction_difference == 0
                person "Exactly! It's so rare that someone feels exactly the same way about [opinion_learned] as me!"

            if opinion_state[1]:
                if is_phone:
                    "[person.possessive_title] sends you a bunch of texts about how she [opinion_string] [opinion_learned]."
                else:
                    "You listen while [person.possessive_title] talks about how she [opinion_string] [opinion_learned]."
            else:
                $ person.discover_opinion(opinion_learned)
                if is_phone:
                    "[person.possessive_title] sends you a bunch of texts, and you learn that she [opinion_string] [opinion_learned]."
                else:
                    "You listen while [person.possessive_title] talks and discover that she [opinion_string] [opinion_learned]."

            $ person.change_love(3 - prediction_difference, max_modified_to = 35)

        else:
            if is_phone:
                person "Oh, this and that. What about you?"
                "You and [person.possessive_title] text back and forth for a while. You've had a fun conversation, but you don't think you've learned anything new."
            else:
                "You and [person.possessive_title] chat for a while. You don't feel like you've learned much about her, but you both enjoyed talking."

        if person.love > 10 and person.has_role(instapic_role) and not person.event_triggers_dict.get("insta_known", False):
            $ person.event_triggers_dict["insta_known"] = True
            person "Hey, are you on InstaPic? You should follow me on there, so you can see what I'm up to."
            if is_phone:
                "She text you her InstaPic profile name. You'll be able to look up her profile now."
            else:
                $ mc.phone.register_number(person)
                "She gives you her InstaPic profile name. You'll be able to look up her profile now."

        $ person.change_happiness(person.get_opinion_score("small talk") + 1)
        if person.get_opinion_score("small talk") >= 0:
            person "It was nice chatting [person.mc_title], we should do it more often!"
        else:
            if is_phone:
                person "I've got to go. Talk to you later."
            else:
                person "So uh... I guess that's all I have to say about that..."
                "[person.possessive_title] trails off awkwardly."
    else:
        if person.get_opinion_score("small talk") < 0:
            person "Oh, not much."
            $ person.change_happiness(person.get_opinion_score("small talk"))
            if is_phone:
                "You try and spark the conversation with a few more messages, but eventually [person.title] just stops responding."
            else:
                "You try and keep the conversation going, but making small talk with [person.title] is like talking to a wall."
        else:
            person "Oh, not much honestly. How about you?"
            $ person.change_happiness(person.get_opinion_score("small talk"))
            if is_phone:
                "You and [person.possessive_title] chat for a while. You don't feel like you've learned much about her, but you both enjoyed talking."
            else:
                "[person.possessive_title] seems happy to chitchat, and you spend half an hour just hanging out."
                "You don't feel like you've learned much about her, but at least she seems to have enjoyed talking."

    if not is_phone:
        $ person.apply_serum_study()
    return
