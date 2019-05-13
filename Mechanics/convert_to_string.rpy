init -1 python:
    # Overrides VREN's height function, so we display the height based on the weight property
    # instead of the fixed weight on zoom factor
    def height_to_string(person_height): #Height is a value between 0.8 and 1.0
        total_inches = __builtin__.round(person_height * 75)
        feet = int(__builtin__.round(total_inches // 12))
        inches = int(__builtin__.round(total_inches % 12))

        if use_imperial_system:
            return str(feet) + "' " + str(inches) + "\""
        else:
            cm = __builtin__.round(total_inches * 2.54, 0)
            return str(cm) + " cm"


    def get_person_weight_string(person):
        check_person_weight_attribute(person)
        weight = __builtin__.round(person.weight * 2.205, 1)
        if use_imperial_system:
            return str(weight) + " lbs"
        else:
            kg = __builtin__.round(person.weight, 1)
            return str(kg) + " kg"
