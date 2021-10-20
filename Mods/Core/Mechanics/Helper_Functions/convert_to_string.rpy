init 0 python:
    # Overrides VREN's height function, so we display the height based on the weight property
    # instead of the fixed weight on zoom factor
    # currently between (147cm) - (197cm).
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
    def SO_relationship_to_title(relationship_string):
        if relationship_string == "Girlfriend":
            return "boyfriend"
        elif relationship_string == "Fiancée":
            return "fiancé"
        return "husband"

    # override without the 'ERROR' message (just use 'wife' as fallback)
    def girl_relationship_to_title(relationship_string):
        if relationship_string == "Girlfriend":
            return "girlfriend"
        elif relationship_string == "Fiancée":
            return "fiancée"
        return "wife"

    def get_energy_string(person):
        percent = person.energy * 1.0 / person.max_energy
        color_string = "{color=#43B197}"
        if percent < .5:
            color_string = "{color=#e1e113}"
        if percent < .2:
            color_string = "{color=#B14365}"

        return color_string + str(__builtin__.int(person.energy)) +"/"+ str(__builtin__.int(person.max_energy)) + "{/color} {image=energy_token_small}"

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

    def time_of_day_string():
        return time_names[time_of_day].lower()

    def person_body_shame_string(person, pronoun = "girl"):
        if person.body_type == "curvy_body":
            return "chubby " + pronoun
        elif person.body_type == "standard_body":
            return "curvy " + pronoun
        elif person.body_type == "standard_preg_body":
            return "pregnant " + pronoun
        else:
            return "skinny " + pronoun
