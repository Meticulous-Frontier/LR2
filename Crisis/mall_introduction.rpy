## Mall Introduction Crisis Mod by Tristimdorion
init -1 python:
    mall_introduction_weight = 5

init 2 python:
    def get_people_with_status():
        strangers = []
        known_people = []
        for loc in [mall, mall_salon, gym, home_store, clothing_store, sex_store]:
            strangers += loc.get_strangers()
            known_people += loc.get_known_people()
        return strangers, known_people

    def mall_introduction_requirement():
        if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
            if mc.location in [mall, mall_salon, gym, home_store, clothing_store, sex_store]:
                strangers, known_people = get_people_with_status()
                if len(strangers) > 0 and len(known_people) > 0:
                    return True
        return False

    mall_introduction_action = ActionMod("Mall Introduction Crisis", mall_introduction_requirement, "mall_introduction_action_label",
        menu_tooltip = "You meet a strange and a friend introduces you.", category = "Mall")
    crisis_list.append([mall_introduction_action, mall_introduction_weight])

label mall_introduction_action_label:
    python:
        strangers, known_people = get_people_with_status()
        # double check that we have at least one stranger and one person we know
        if len(strangers) == 0 or len(known_people) == 0:
            renpy.return_statement()

        # pick a person from each
        known_person = get_random_from_list(known_people)
        stranger = get_random_from_list(strangers)

        known_person.draw_person(position = "stand4", emotion = "happy", character_placement = character_center_flipped)
        stranger.draw_person(position = "stand3", emotion = "default", character_placement = character_right)

    known_person.char "Oh, hello [known_person.mc_title], how nice to see you here."
    mc.name "Hello [known_person.title], nice to see you too."

    # set titles for unknown person
    $ title_choice = get_random_title(stranger)
    $ formatted_title = stranger.create_formatted_title(title_choice)
    $ stranger.set_title(title_choice)
    $ stranger.set_possessive_title(get_random_possessive_title(stranger))

    known_person.char "Let me, introduce my friend [formatted_title]."
    "[formatted_title] holds her hand out to shake yours."

    # sets your title for unknown person
    $ title_choice = get_random_from_list(get_player_titles(stranger))
    $ stranger.set_mc_title(title_choice)

    if known_person.is_employee():
        known_person.char "And this is my boss, [title_choice]."
    else:
        known_person.char "And this is my friend, [title_choice]."

    mc.name "It's a pleasure to meet you, [stranger.title]."
    $ stranger.draw_person(emotion = "happy")
    $ stranger.change_love(5)
    stranger.char "The pleasure is all mine, [stranger.mc_title]."

    # bonus stats when the person knows you more intimately
    if known_person.sluttiness > 20 or known_person.love > 20:
        if known_person.is_employee():
            known_person.char "I promise you [stranger.name], he is a great boss, you should go out with him sometime."
        else:
            known_person.char "I have to tell you [stranger.name], he is a great person to hang out with."

        $ stranger.change_love(5)
        $ stranger.change_happiness(10)

        if stranger.sluttiness > 5:
            stranger.char "I trust your judgement [known_person.name] and he is very cute."
        else:
            stranger.char "I trust your judgement [known_person.name], perhaps we could go out sometime."

    mc.name "It was great meeting you both, until next time."
    
    $ known_person.draw_person(position = "walking_away")
    $ stranger.draw_person(position = "back_peek")

    "[stranger.title] looks back at you smiling."

    $ stranger.clear_scene()
    $ known_person.clear_scene()

    return


    