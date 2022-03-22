init 0 python:
    # Overrides VREN's height function, so we display the height based on the weight property
    # instead of the fixed weight on zoom factor
    # currently between (147cm) - (197cm).
    @renpy.pure
    def height_to_string(person_height): #Height is a value between 0.8 and 1.0
        total_inches = __builtin__.round(((person_height * 250) - 53) / 2.54)
        feet = __builtin__.int(total_inches // 12)
        inches = __builtin__.int(total_inches % 12)

        if use_imperial_system:
            return str(feet) + "' " + str(inches) + "\""
        else:
            cm = __builtin__.round(total_inches * 2.54, 1)
            return str(cm) + " cm"

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
    def get_energy_string(energy, max_energy):
        percent = energy * 1.0 / max_energy
        color_string = "{color=#43B197}"
        if percent < .5:
            color_string = "{color=#e1e113}"
        if percent < .2:
            color_string = "{color=#B14365}"

        return color_string + str(__builtin__.int(energy)) +"/"+ str(__builtin__.int(max_energy)) + "{/color} {image=energy_token_small}"

    @renpy.pure
    def get_arousal_with_token_string(arousal, max_arousal):
        return str(__builtin__.int(arousal)) + "/"+ str(__builtin__.int(max_arousal)) + " {image=arousal_token_small}"

    @renpy.pure
    def get_locked_clarity_with_token_string(locked_clarity):
        return str(__builtin__.int(locked_clarity)) + " {image=lust_eye_token_small}"

    @renpy.pure
    def get_attention_string(attention, max_attention):
        percent = attention * 1.0 / max_attention
        color_string = "{color=#43B197}"
        if percent > .5:
            color_string = "{color=#e1e113}"
        if percent > .8:
            color_string = "{color=#B14365}"
        return color_string + str(attention) + "/" + str(max_attention) + "{/color}"

    def get_person_weight_string(person):
        if use_imperial_system:
            lbs = person.weight * 2.205

            # add some weight based on number of days pregnant
            if person.pregnancy_is_visible():
                # calculates a factor for the current day in relation to show day and due day, multiplied by average pregnancy weight of 25 pounds
                lbs += (1 - ((person.get_due_day() - day) / float(person.get_due_day() - person.pregnancy_show_day()))) * 25

            return str(__builtin__.round(lbs, 1)) + " lbs"
        else:
            kg = person.weight

            # add some weight based on number of days pregnant
            if person.pregnancy_is_visible():
                # calculates a factor for the current day in relation to show day and due day, multiplied by average pregnancy weight of 11.4 kg
                kg += (1 - ((person.get_due_day() - day) / float(person.get_due_day() - person.pregnancy_show_day()))) * 11.4

            return str(__builtin__.round(kg, 1)) + " kg"

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
        return "{color=" + person.char.who_args["color"] + "}" + "{font=" + person.char.what_args["font"] + "}" + person_title + "{/font}{/color}"

    def format_titles_short(person):
        person_title = person.name + " "
        if person.last_name and __builtin__.len(person.last_name) > 0:
            person.title += person.last_name[0] + "."
        if not person.title or person.mc_title == "Stranger":
            return "???"    # we don't know her yet
        return "{color=" + person.char.who_args["color"] + "}" + "{font=" + person.char.what_args["font"] + "}" + person_title + "{/font}{/color}"
