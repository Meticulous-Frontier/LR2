init -1 python:
    # Overrides VREN's height function, so we display the height based on the weight property
    # instead of the fixed weight on zoom factor
    # currently between 60 inch (152.4) - 70 inch (177.8) (based on * 50 + 20).
    def height_to_string(person_height): #Height is a value between 0.8 and 1.0
        total_inches = __builtin__.round((person_height * 50) + 20)
        feet = int(__builtin__.round(total_inches // 12))
        inches = int(__builtin__.round(total_inches % 12))

        if use_imperial_system:
            return str(feet) + "' " + str(inches) + "\""
        else:
            cm = __builtin__.round(total_inches * 2.54, 1)
            return str(cm) + " cm"


    def get_person_weight_string(person):
        if use_imperial_system:
            lbs = person.weight * 2.205
    
            # add some weight based on number of days pregnant
            if person.pregnancy_is_visible():
                # calculates a factor for the current day in relation to show day and due day, multiplied by average pregnancy weight of 25 pounds
                lbs += (1 - ((person.get_due_day() - day) / float(person.get_due_day() - person.pregnancy_show_day()))) * 25

            return str(round(lbs, 1)) + " lbs"
        else:
            kg = person.weight

            # add some weight based on number of days pregnant
            if person.pregnancy_is_visible():
                # calculates a factor for the current day in relation to show day and due day, multiplied by average pregnancy weight of 11.4 kg
                kg += (1 - ((person.get_due_day() - day) / float(person.get_due_day() - person.pregnancy_show_day()))) * 11.4

            return str(round(kg, 1)) + " kg"

    def time_of_day_string():
        return time_names[time_of_day].lower()

    def person_body_shame_string(person, pronoun = "girl"):
        if person.body_type == "curvy_body":
            return "chubby " + pronoun
        elif person.body_type == "standard_body":
            return "curvy " + pronoun
        else:
            return "skinny " + pronoun
