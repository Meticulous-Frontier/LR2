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
    if the_person.has_role(casual_hotwife_role):
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        the_person.char "You know my husband won't like that, we agreed on keeping this casual, lets go the bathroom instead and show me how much you like me..."
        return

    elif the_person.has_role(casual_athlete_role):
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        the_person.char "I have no time for that social stuff, but I could use another of your workout exercises..."
        return

    elif the_person.has_role(casual_FA_role):
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        the_person.char "Thanks, but no, this isn't a social thing."
        return

    # call original label
    $ del config.label_overrides["movie_date_plan_label"]
    call movie_date_plan_label(the_person) from _call_movie_date_plan_label_enhanced
    $ config.label_overrides["movie_date_plan_label"] = "movie_date_plan_enhanced_label"

    return "Advance time"

label dinner_date_plan_enhanced_label(the_person):
    if the_person.has_role(casual_hotwife_role):
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
        the_person.char "You know my husband won't like that, we agreed on keeping this casual, lets go the bathroom instead and show me how much you like me..."
        return

    elif the_person.has_role(casual_athlete_role):
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
        the_person.char "I have no time for that social stuff, but I could use another of your workout exercises..."
        return

    elif the_person.has_role(casual_FA_role):
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together."
        the_person.char "Thanks, but no, this isn't a social thing."
        return

    # call original label
    $ del config.label_overrides["dinner_date_plan_label"]
    call dinner_date_plan_label(the_person) from _call_dinner_date_plan_label_enhanced
    $ config.label_overrides["dinner_date_plan_label"] = "dinner_date_plan_enhanced_label"
    return
