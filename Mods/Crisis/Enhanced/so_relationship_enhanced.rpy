init 2 python:
    config.label_overrides["so_relationship_improve_label"] = "so_relationship_improve_label_enhanced"
    config.label_overrides["so_relationship_worsen_label"] = "so_relationship_worsen_label_enhanced"

    # the relationship will only worsen if the love of the person for the MC is higher than this threshold value
    # so as long as you are not pursuing them, their relationships with their partners will only improve
    relationship_stats = {
        "Married" : 90,
        "Fiancée" : 65,
        "Girlfriend": 40,
        "Single": 25,
    }

    def so_relationship_improve_requirement_enhanced():
        if time_of_day > 0 and time_of_day < 4:
            return not get_so_relationship_improve_person() is None
        return False

    def so_relationship_worsen_requirement_enhanced():
        if time_of_day > 0 and time_of_day < 4:
            return not get_so_relationship_worsen_person() is None
        return False

    def so_relationship_quarrel_requirement(person):
        if quest_director.is_person_blocked(person):
            return False

        if time_of_day > 0 and time_of_day < 4:
            return person.relationship != "Single" and not (person.mc_title == "Stranger" or not person.title)
        return False

    # changed to on-talk event, so it won't light up on the house map
    # she stays mad for two time-slots and if you don't talk to her, she won't break-up
    relation_ship_quarrel = Action("Girl had a fight with her SO", so_relationship_quarrel_requirement, "so_relationship_quarrel_label", event_duration = 2)
    limited_time_event_pool.append([relation_ship_quarrel, 1, "on_talk"])

    # replace action requirement functions with newly defined functions (cPickle resolver)
    so_relationship_improve_crisis.requirement = so_relationship_improve_requirement_enhanced
    so_relationship_worsen_crisis.requirement = so_relationship_worsen_requirement_enhanced

    def get_so_relationship_improve_person():
        potential_people = []
        for person in [x for x in known_people_in_the_game(excluded_people = unique_character_list + quest_director.unavailable_people()) if not x.relationship == "Married" and not x.has_role([girlfriend_role, affair_role])]:
            if person.relationship in relationship_stats and person.love <= relationship_stats[person.relationship] + (person.get_opinion_score("cheating on men") * 5):
                potential_people.append(person)
        return get_random_from_list(potential_people)

    def get_so_relationship_worsen_person():
        potential_people = []
        for person in [x for x in known_people_in_the_game(excluded_people = unique_character_list + quest_director.unavailable_people()) if not x.relationship == "Single" and not x.has_role([affair_role])]:
            if person.relationship in relationship_stats and person.love > relationship_stats[person.relationship] - (person.get_opinion_score("cheating on men") * 5):
                potential_people.append(person)
        return get_random_from_list(potential_people)

label so_relationship_improve_label_enhanced():
    $ the_person = get_so_relationship_improve_person()
    if the_person is None:
        return #Something's changed and there is no longer a valid person

    if the_person.relationship == "Single":
        $ the_person.change_happiness(10)
        "You get a notification on your phone."
        $ guy_name = get_random_male_name()
        "[the_person.title] has just changed her status on social media. She's now in a relationship with someone named [guy_name]."
        $ the_person.relationship = "Girlfriend"
        $ the_person.SO_name = guy_name

    elif the_person.relationship == "Girlfriend":
        $ the_person.change_happiness(20)
        if the_person.love > 30: #You're a good friend.
            $ mc.start_text_convo(the_person)
            the_person "Hey [the_person.mc_title], I have some exciting news!"
            the_person "My boyfriend proposed, me and [the_person.SO_name] are getting married! I'm so excited, I just had to tell you!"
            menu:
                "Congratulate her":
                    mc.name "Congratulations! I'm sure you're the happiest girl in the world."
                    $ the_person.change_love(1)
                    the_person "I am! I've got other people to tell now, talk to you later!"
                "Warn her against it":
                    mc.name "I don't know if that's such a good idea. Do you even know him that well?"
                    "Her response is near instant."
                    the_person "What? What do you even mean by that?"
                    mc.name "I mean, what if he isn't who you think he is? Maybe he isn't the one for you."
                    $ the_person.change_happiness(-10)
                    the_person "I wasn't telling you because I wanted your opinion. If you can't be happy for me, you can at least be quiet."
                    $ the_person.change_love(-5)
                    "She seems pissed, so you take her advice and leave her alone."
            $ mc.end_text_convo()
        else: #You see it on social media
            "You get a notification on your phone."
            "It seems [the_person.title] has gotten engaged to her boyfriend, [the_person.SO_name]. You take a moment to add your own well wishes to her social media pages."
        $ the_person.relationship = "Fiancée"

    elif the_person.relationship == "Fiancée":
        #TODO: Add an event where you're invited to their wedding and fuck the bride.
        "You get a notification on your phone."
        "It seems [the_person.title]'s just had her wedding to her Fiancé, [the_person.SO_name]. You take a moment to add your congratulations to her wedding photo."
        $ the_person.relationship = "Married"

    return


# triggered when love for MC grows
label so_relationship_worsen_label_enhanced():
    $ the_person = get_so_relationship_worsen_person()
    if the_person is None:
        return #Something's changed and there is no longer a valid person

    $ so_title = SO_relationship_to_title(the_person.relationship)
    if the_person.has_role(affair_role):
        "You get a call from [the_person.title]. When you pick up she sounds tired, but happy."
        the_person "Hey [the_person.mc_title], I've got some news. Me and my [so_title], [the_person.SO_name], had a fight. We aren't together any more."
        the_person "We don't have to hide what's going on between us any more."
        $ the_person.add_role(girlfriend_role)
        mc.name "That's good news! I'm sure you'll want some rest, so we can talk more later. I love you."
        $ the_person.change_love(5)
        the_person "I love you too. Bye."

    else:
        $ the_person.change_happiness(-20)
        "You get a notification on your phone."
        "It looks like [the_person.title] has left her [so_title] and is single now."

    $ the_person.relationship = "Single"
    $ the_person.SO_name = None
    $ the_person.remove_role(affair_role)   # make sure we don't have a affair
    return

# triggered randomly for a person (fight with her SO)
label so_relationship_quarrel_label(the_person):
    $ so_title = SO_relationship_to_title(the_person.relationship)

    if renpy.random.randint(0, 100) >= 20: # she will only break up 20% of the time
        if renpy.random.randint(0,3) == 1: # 25% change to complain, otherwise go to talk
            the_person "Hey [the_person.mc_title], it's good to see you. Me and my [so_title], [the_person.SO_name], had a fight."
            mc.name "I'm sorry to hear that, are you ok?"
            the_person "Yeah, I'm ok. Sorry to bother you."
            mc.name "That's fine, let me know if I can help."
            the_person "Thanks."
        else:
            "[the_person.title] looks at you as if she's going to say something, but instead just waits for you to talk with her."
        call talk_person(the_person) from _call_talk_person_so_relationship_quarrel
        return

    if the_person.has_role(affair_role):
        the_person "Hey [the_person.mc_title], it's good to see you. Me and my [so_title], [the_person.SO_name], had a fight and we decided to split up."
        the_person "We don't have to hide what's going on between us any more."
        $ the_person.add_role(girlfriend_role)
        mc.name "That's good news! So we don't have to sneak around anymore."
        $ the_person.change_love(5)
        the_person "Indeed, I would love to go out sometime..."
    else:
        $ the_person.change_happiness(-20)
        the_person "Hey [the_person.mc_title], it's good to see you. Me and my [so_title], [the_person.SO_name], had a fight and we decided to split up."
        mc.name "I'm sorry to hear that, [the_person.title], just take it easy and take your time to process it."
        the_person "Thanks, it's appreciated."

    $ the_person.relationship = "Single"
    $ the_person.SO_name = None
    $ the_person.remove_role(affair_role)   # make sure we don't have a affair
    return
