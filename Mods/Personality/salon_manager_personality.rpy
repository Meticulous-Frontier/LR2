init 1400 python:
    def salon_manager_possessive_titles(person):
        valid_possessive_titles = [wild_titles(person)]
        valid_possessive_titles.append("My stylist")
        if person.sluttiness > 50:
            valid_possessive_titles.append("My intimate stylist")
        return valid_possessive_titles

    salon_manager_personality = Personality("salon_manager", default_prefix = "wild", #Based on wild style personality
        common_likes = ["skirts", "small talk", "the weekend", "the colour purple", "makeup", "hiking", "flirting"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "giving head", "anal sex", "public sex", "skimpy outfits", "anal sex", "showing her tits", "showing her ass", "being submissive", "creampies", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour yellow", "supply work", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["taking control", "bareback sex"],
        titles_function = wild_titles, possessive_titles_function = salon_manager_possessive_titles, player_titles_function = wild_player_titles)

label salon_manager_greetings(the_person):
    $ the_person.draw_person(emotion = "happy")

    if the_person.mc_title == "Stranger":
        "You enter the hair salon. A beautiful young woman walks up to you and introduces herself."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        the_person.char "Hello there sir! Welcome to the Sweet Pixie Salon!"

        # uses parts of the in-game introduction sequence tailored to SB
        if the_person.title is None:
            mc.name "Hey, there."
            $ title_choice = get_random_title(the_person)
            $ formatted_title = the_person.create_formatted_title(title_choice)
            the_person.char "I am [formatted_title], top stylist and owner."
            $ the_person.set_title(title_choice)
            $ the_person.set_possessive_title(get_random_possessive_title(the_person))
            "She holds her hand out to shake yours."
            the_person.char "And how may I call you?"
            $ title_tuple = []
            $ title_choice = None
            python:
                for title in get_player_titles(the_person):
                    title_tuple.append([title,title])

            $ title_choice = renpy.display_menu(title_tuple,True,"Choice")
            mc.name "[title_choice], nice to meet you."
            $ the_person.set_mc_title(title_choice)

        the_person.char "I've just opened, so what can I do for you today? A wash or a trim? A shave perhaps?"
        mc.name "Nothing like that today, I own a company downtown."
        mc.name "My employees need to look perfect and I want to pay for their expenses, is that possible?"
        the_person.char "No problem, just give me your credit card details and I will charge it whenever you sent someone by."
        "You smile at [the_person.name] and hand over your company credit card."
        the_person.char "Perfect! All done."
    else:
        the_person.char "Hey there, [the_person.mc_title]! Its good to see you!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title] smiles playfully."
            the_person.char "I was just thinking about you. Anything I can do for you today?"
        else:
            the_person.char "Is there anything I can help you with?"

    $ renpy.scene("Active")
    return
