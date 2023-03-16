init 0 python:
    # Overrides VREN's height function, so we display the height based on the weight property
    # instead of the fixed weight on zoom factor
    # using new VREN calculations (122cm) - (215cm).
    @renpy.pure
    def height_to_string(person_height): #Height is a value between 0.8 and 1.0
        rounded_height = __builtin__.round(person_height,5) #Round height to 5 decimal points.
        height_in_inches = __builtin__.round((rounded_height * 100)/1.5, 3)
        feet = __builtin__.int(math.floor(height_in_inches/12))
        inches = __builtin__.int(height_in_inches % 12)

        if use_imperial_system:
            return "{}' {}\"".format(feet, inches)
        else:
            return "{:.0f} cm".format(height_in_inches * 2.54)

    # override without the 'ERROR' message (just use 'husband' as fallback)
    @renpy.pure
    def SO_relationship_to_title(relationship_string):
        if relationship_string == "Girlfriend":
            return "boyfriend"
        elif relationship_string == "Fiancée":
            return "fiancé"
        return "husband"

    # override without the 'ERROR' message (just use 'wife' as fallback)
    @renpy.pure
    def girl_relationship_to_title(relationship_string):
        if relationship_string == "Girlfriend":
            return "girlfriend"
        elif relationship_string == "Fiancée":
            return "fiancée"
        return "wife"

    @renpy.pure
    def get_color_value_for_fraction(percent):
        color_string = "#43B197"
        if percent < .5:
            color_string = "#e1e113"
        if percent < .2:
            color_string = "#B14365"
        return color_string

    @renpy.pure
    def get_inverted_color_value_for_fraction(percent):
        color_string = "#43B197"
        if percent > .5:
            color_string = "#e1e113"
        if percent > .8:
            color_string = "#B14365"
        return color_string

    @renpy.pure
    def get_energy_string(energy, max_energy):
        percent = energy * 1.0 / (max_energy or 1)
        return "{{color={}}}{:0.0f}%{{/color}} {{image=energy_token_small}}".format(get_color_value_for_fraction(percent), percent * 100)

    @renpy.pure
    def get_arousal_with_token_string(arousal, max_arousal):
        percent = arousal * 1.0 / (max_arousal or 1)
        return "{{color={}}}{:0.0f}%{{/color}} {{image=arousal_token_small}}".format(get_inverted_color_value_for_fraction(percent), percent * 100)

    @renpy.pure
    def get_locked_clarity_with_token_string(locked_clarity):
        return "{} {{image=lust_eye_token_small}}".format(__builtin__.int(locked_clarity))

    @renpy.pure
    def get_attention_string(attention, max_attention):
        percent = attention * 1.0 / (max_attention or 1)
        return "{{color={}}}{:0.0f}%{{/color}}".format(get_inverted_color_value_for_fraction(percent), percent * 100)

    def get_person_weight_string(person):
        kg = person.weight
        # add some weight based on number of days pregnant
        if person.pregnancy_is_visible():
            # calculates a factor for the current day in relation to show day and due day, multiplied by average pregnancy weight of 11.4 kg
            kg += (1 - ((person.get_due_day() - day) / float(person.get_due_day() - person.pregnancy_show_day()))) * 11.4

        if use_imperial_system:
            return "{} lbs".format(__builtin__.round(kg * 2.205, 1))
        return "{} kg".format(__builtin__.round(kg, 1))

    @renpy.pure
    def time_of_day_string(time_of_day):
        return time_names[time_of_day].lower()

    @renpy.pure
    def person_body_shame_string(body_type, pronoun = "girl"):
        if body_type == "curvy_body":
            return "chubby " + pronoun
        elif body_type == "standard_body":
            return "curvy " + pronoun
        elif body_type == "standard_preg_body":
            return "pregnant " + pronoun
        else:
            return "skinny " + pronoun

    # instead of using 'call name' in menus, use the actual person name to avoid confusion
    def format_titles(person):
        person_title = person.name + " " + person.last_name
        if not person.title or person.mc_title == "Stranger":
            return "???"    # we don't know her yet
        return "{{color={}}}{{font={}}}{}{{/font}}{{/color}}".format(person.char.who_args["color"], person.char.what_args["font"], person_title)

    def format_titles_short(person):
        person_title = person.name + " "
        if person.last_name and __builtin__.len(person.last_name) > 0:
            person_title += person.last_name[0] + "."
        if not person.title or person.mc_title == "Stranger":
            return "???"    # we don't know her yet
        return "{{color={}}}{{font={}}}{}{{/font}}{{/color}}".format(person.char.who_args["color"], person.char.what_args["font"], person_title)
