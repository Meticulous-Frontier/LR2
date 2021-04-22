init 5 python:
    config.label_overrides["movie_date_plan_label"] = "movie_date_plan_enhanced_label"
    config.label_overrides["dinner_date_plan_label"] = "dinner_date_plan_enhanced_label"
    config.label_overrides["lunch_date_plan_label"] = "lunch_date_plan_enhanced_label"

    def add_movie_date_action(person):
        movie_action = Action("Movie date", evening_date_trigger, "movie_date_label", args=person, requirement_args=1) #it happens on a tuesday.
        mc.business.add_mandatory_crisis(movie_action)
        mc.business.event_triggers_dict["movie_date_scheduled"] = True
        return

    def add_dinner_date_action(person):
        dinner_action = Action("Dinner date", evening_date_trigger, "dinner_date_label", args=person, requirement_args=4) #it happens on a friday, so day%7 == 4
        mc.business.add_mandatory_crisis(dinner_action)
        mc.business.event_triggers_dict["dinner_date_scheduled"] = True
        return

label movie_date_plan_enhanced_label(the_person):
    if the_person.has_role(casual_hotwife_role):
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        the_person "You know my husband won't like that, we agreed on keeping this casual, lets go the bathroom instead and show me how much you like me..."
        return

    # elif the_person.has_role(casual_athlete_role):
    #     mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
    #     the_person "I have no time for that social stuff, but I could use another of your workout exercises..."
    #     return

    elif the_person.has_role(casual_FA_role):
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        the_person "Thanks, but no, this isn't a social thing."
        return

    # call original label
    $ del config.label_overrides["movie_date_plan_label"]
    call movie_date_plan_label(the_person) from _call_movie_date_plan_label_enhanced
    $ config.label_overrides["movie_date_plan_label"] = "movie_date_plan_enhanced_label"

    return "Advance time"

label dinner_date_plan_enhanced_label(the_person):
    if the_person.has_role(casual_hotwife_role):
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
        the_person "You know my husband won't like that, we agreed on keeping this casual, lets go the bathroom instead and show me how much you like me..."
        return

    # elif the_person.has_role(casual_athlete_role):
    #     mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
    #     the_person "I have no time for that social stuff, but I could use another of your workout exercises..."
    #     return

    elif the_person.has_role(casual_FA_role):
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
        the_person "Thanks, but no, this isn't a social thing."
        return

    # call original label
    $ del config.label_overrides["dinner_date_plan_label"]
    call dinner_date_plan_label(the_person) from _call_dinner_date_plan_label_enhanced
    $ config.label_overrides["dinner_date_plan_label"] = "dinner_date_plan_enhanced_label"
    return

label lunch_date_plan_enhanced_label(the_person):
    if the_person == kaya and the_person.location = downtown:
        mc.name "I was thinking about getting some lunch. Do you have a lunch break?"
        if the_person.love < 40:
            the_person "Sorry, I work a short shift, so I don't get a lunch break."
            the_person "You seem nice though... maybe we could do something after I get off?"
            mc.name "Okay, I'll try to swing by later."
        else:
            the_person "You know I don't get a break! Swing by later, maybe we can get a drink after I get off?"
            mc.name "Okay, I'll try to swing by later."
        return

    $ del config.label_overrides["lunch_date_plan_label"]
    call lunch_date_plan_label(the_person) from _call_lunch_date_plan_label_enhanced
    $ config.label_overrides["lunch_date_plan_label"] = "lunch_date_plan_enhanced_label"
    return
