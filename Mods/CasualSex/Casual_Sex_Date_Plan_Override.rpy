# Casual Roles will deny going on a date with you. (Original idea by BadRabbit)

init 5 python:
    config.label_overrides["movie_date_plan_label"] = "movie_date_plan_rejection_label"
    config.label_overrides["dinner_date_plan_label"] = "dinner_date_plan_rejection_label"

label movie_date_plan_rejection_label(the_person):
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

    call movie_date_plan_label(the_person) from _call_movie_date_plan_rejection_label
    return

label dinner_date_plan_rejection_label(the_person):
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

    call dinner_date_plan_label(the_person) from _call_dinner_date_plan_rejection_label
    return

