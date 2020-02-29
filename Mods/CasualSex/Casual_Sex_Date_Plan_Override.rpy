# Casual Roles will deny going on a date with you. (Original idea by BadRabbit)

init 5 python:
    config.label_overrides["movie_date_plan_label"] = "movie_date_plan_enhanced_label"
    config.label_overrides["dinner_date_plan_label"] = "dinner_date_plan_enhanced_label"

    def add_movie_date_action(person):
        movie_action = Action("Movie date", evening_date_trigger, "movie_date_label", args=person, requirement_args=1) #it happens on a tuesday.
        mc.business.mandatory_crises_list.append(movie_action)
        mc.business.event_triggers_dict["date_scheduled"] = True
        return

    def add_dinner_date_action(person):
        dinner_action = Action("Dinner date", evening_date_trigger, "dinner_date_label", args=person, requirement_args=4) #it happens on a friday, so day%7 == 4
        mc.business.mandatory_crises_list.append(dinner_action)
        mc.business.event_triggers_dict["date_scheduled"] = True
        return

label movie_date_plan_enhanced_label(the_person):
    # She starts to wonder if she should be telling her boyfriend, etc. about this.
    if day%7 == 1 and time_of_day < 3:
        $ is_tuesday = True #It's already Tuesday and early enough that the date would be right about now.
    else:
        $ is_tuesday = False

    if casual_hotwife_role in the_person.special_role:
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        the_person.char "You know my husband won't like that, we agreed on keeping this casual, lets go the bathroom instead and show me how much you like me..."
        return

    elif casual_athlete_role in the_person.special_role:
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        the_person.char "I have no time for that social stuff, but I could use another of your workout exercises..."
        return

    elif casual_FA_role in the_person.special_role:
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        the_person.char "Thanks, but no, this isn't a social thing."
        return

    elif sister_role in the_person.special_role:
        mc.name "Hey, I was wondering if you'd like to see a movie with me some time? You know, spend a little more time together as brother-sister."
        the_person.char "It's been like, a year since I went to the movies with you. I think it was when my date ghosted me and you swept in and saved the night by coming with me."
        the_person.char "I can't quite remember what we saw though..."
        "She seems puzzled for a moment, then shrugs and smiles at you."
        the_person.char "Oh well, it's probably not important. Sure thing [the_person.mc_title], a movie sounds fun!"
        if is_tuesday:
            the_person.char "How about tonight? I think tickets are half price."
        else:
            the_person.char "How about Tuesday night? I tickets are half price."

    elif mother_role in the_person.special_role:
        mc.name "Hey [the_person.title], would you like to come to the movies with me? I want to spend some more time together, mother and son."
        the_person.char "Aww, you're precious [the_person.mc_title]. I would love to go to the movies with you."
        the_person.char "Remember how me and you use to watch movies together every weekend? I felt like our relationship was so close because of that."
        "She seems distracted by the memory for a moment, then snaps back to the conversation."
        if is_tuesday:
            the_person.char "Would you be free tonight?"
        else:
            the_person.char "Would you be free Tuesday night?"

    elif aunt_role in the_person.special_role:
        mc.name "[the_person.title], would you like to come see a movie with me? I think it would just be nice to spend some more time together."
        the_person.char "You know, I haven't been out much since I left my ex, so a movie sounds like a real good time."
        if is_tuesday:
            the_person.char "How about later tonight? I don't have anything going on."
        else:
            the_person.char "How about Tuesday night? I don't have anything going on then."

    elif cousin_role in the_person.special_role:
        mc.name "Hey, do you want to come see a movie with me and spend some time together?"
        the_person.char "Fine, but no telling people we're related, okay? I don't want anyone to think I might be a dweeb like you."
        "She gives you a wink."
        if is_tuesday:
            the_person.char "How about tonight? I didn't have anything going on."
        else:
            the_person.char "How about Tuesday? I don't have anything going on then."

    elif not the_person.relationship == "Single":
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        mc.name "It would give us a chance to spend time together."
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.get_opinion_score("cheating on men") > 0:
            the_person.char "Oh, a movie sounds fun!"
            "She gives you a playful smile."
            the_person.char "Just don't tell my [so_title], okay? He might not like me hanging around with a hot guy like you."
            mc.name "My lips are sealed."
            if the_person.sluttiness > 60:
                if is_tuesday:
                    the_person.char "Treat me right and mine might not be. He's normally out late with work tonight, how does that sound?"
                else:
                    the_person.char "Treat me right and mine might not be. He's normally out late with work on Tuesdays, how does that sound?"
            else:
                if is_tuesday:
                    the_person.char "He's normally out late with work on Tuesdays, so how about would tonight sound for you?"
                else:
                    the_person.char "He's normally out late with work on Tuesdays, how does that sound for you?"

        else:
            the_person.char "Oh, a movie sounds fun! But..."
            mc.name "Is there something wrong?"
            the_person.char "No, I just don't know what my [so_title] would think. He might be a little jealous of you, you know?"
            mc.name "You don't have to tell him that I'll be there, if you don't want to. There's no reason you couldn't go out by yourself if you wanted to."
            "She thinks about it for a moment, then nods and smiles."
            if is_tuesday:
                the_person.char "You're right, of course. He's normally busy with work tonight, so how does that sound for you?"
            else:
                the_person.char "You're right, of course. He's normally busy with work on Tuesdays, how does that sound for you?"

    else:
        mc.name "So [the_person.title], I was wondering if you'd like to come see a movie with me some time this week."
        mc.name "It would give us a chance to spend some time together and get to know each other better."
        if is_tuesday:
            the_person.char "Oh, a movie sounds fun! I don't have anything going on tonight, would that work for you?"
        else:
            the_person.char "Oh, a movie sounds fun! I don't have anything going on Tuesday night, would that work for you?"

    menu:
        "Plan a date for Tuesday night.":
            mc.name "Tuesday would be perfect, I'm already looking forward to it."
            the_person.char "Me too!"

            $ add_movie_date_action(the_person)

        "Maybe some other time.":
            mc.name "I'm busy on Friday unfortunately."
            the_person.char "Well maybe next week then. Let me know, okay?"
            "She gives you a warm smile."

    return "Advance time"

label dinner_date_plan_enhanced_label(the_person):
    if casual_hotwife_role in the_person.special_role:
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
        the_person.char "You know my husband won't like that, we agreed on keeping this casual, lets go the bathroom instead and show me how much you like me..."
        return

    elif casual_athlete_role in the_person.special_role:
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
        the_person.char "I have no time for that social stuff, but I could use another of your workout exercises..."
        return

    elif casual_FA_role in the_person.special_role:
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
        the_person.char "Thanks, but no, this isn't a social thing."
        return

    elif sister_role in the_person.special_role:
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together. Some brother sister bonding time."
        the_person.char "That sounds great [the_person.mc_title]. Would Friday be good?"

    elif mother_role in the_person.special_role:
        mc.name "Mom, I was wondering if I could take you out to dinner, just the two of us. I'd enjoy some mother son bonding time."
        the_person.char "Aww, that's so sweet. How about Friday, after we're both finished with work."

    elif aunt_role in the_person.special_role:
        mc.name "[the_person.title], would you like to go out on a dinner date with me? I think it would be a nice treat for you."
        the_person.char "That sounds like it would be amazing. It's been tough, just me and [cousin.title]. I don't get out much any more."
        "She smiles and gives you a quick hug."
        the_person.char "How about Friday night?"

    elif cousin_role in the_person.special_role:
        mc.name "Hey, I want to take you out to dinner."
        the_person.char "Jesus, at least buy me dinner first. Wait a moment..."
        "She laughs at her own joke."
        the_person.char "Fine, how about Friday?"

    elif not the_person.relationship == "Single":
        mc.name "[the_person.title], I'd love to spend some time together, just the two of us. Would you let me take you out for dinner?"
        $ SO_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "[the_person.mc_title], you know I've got a [SO_title], right? Well..."
        if the_person.get_opinion_score("cheating on men") > 0:
            "She doesn't take very long to make up her mind."
            the_person.char "He won't know about it, right? What he doesn't know can't hurt him. Are you free Friday?"
        else:
            "She thinks about it for a long moment."
            the_person.char "Just this once, and we have to make sure my [SO_title] never finds out. Are you free Friday?"

    else:
        mc.name "[the_person.title], I'd love to get to know you better. Would you let me take you out for dinner?"
        the_person.char "That sounds delightful [the_person.mc_title]. I'm free Friday night, if you would be available."


    menu:
        "Plan a date for Friday night.":
            mc.name "It's a date. I'm already looking forward to it."
            the_person.char "Me too!"

            $ add_dinner_date_action(the_person)

        "Maybe some other time.":
            mc.name "I'm busy on Friday unfortunately."
            the_person.char "Well maybe next week then. Let me know, okay?"
            "She gives you a warm smile."
    return
