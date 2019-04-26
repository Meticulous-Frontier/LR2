init -1 python:
    # Overrides VREN's height function, so we display the height based on the weight property
    # instead of the fixed weight on zoom factor
    def height_to_string(the_height): #Height is a value between 0.8 and 1.0
        total_inches = __builtin__.round(the_height * 75)
        feet = int(__builtin__.round(total_inches // 12))
        inches = int(__builtin__.round(total_inches % 12))

        return str(feet) + "' " + str(inches) + "\""

    # Check if weight property exists on person, if not, add based on body type
    def check_person_weight_attribute(the_person):
        if not hasattr(the_person, "weight"):
            if (the_person.body_type == "thin_body"):
                setattr(the_person, "weight", 60 * person.height)   # default weight thin body
            elif (the_person.body_type == "standard_body"):
                setattr(the_person, "weight", 75 * person.height)   # default weight standard body
            else:
                setattr(the_person, "weight", 90 * person.height)   # default weight curvy body
        return

    # Returns True when the persons body type has changed; otherwise False
    # chance is probability percentage that weight change for amount will occur (used by serums)
    def change_person_weight(the_person, amount, chance):
        check_person_weight_attribute(the_person)
        if (amount == 0):
            return False

        if renpy.random.randint(0, 100) <= chance:
            the_person.weight += amount
        
        # maximum and minimum weight are dependant on height
        max_weight = the_person.height * 100
        min_weight = the_person.height * 50
        switch_point_low = the_person.height * 68
        switch_point_high = the_person.height * 83

        if (amount > 0):
            if the_person.weight > switch_point_low + 3 and the_person.body_type == "thin_body":
                the_person.body_type = "standard_body"
                return True
            if the_person.weight > switch_point_high + 3 and the_person.body_type == "standard_body":
                the_person.body_type = "curvy_body"
                return True
            if the_person.weight > max_weight: #Maximum weight
                the_person.weight = max_weight
            return False

        if (amount < 0):
            if the_person.weight < min_weight:  #Minimum weight
                the_person.weight = min_weight
                return False
            if the_person.weight < switch_point_low - 3 and the_person.body_type == "standard_body":
                the_person.body_type = "thin_body"        
                return True
            if the_person.weight < switch_point_high - 3 and the_person.body_type == "curvy_body":
                the_person.body_type = "standard_body"
                return True
            return False

    def get_person_weight_string(the_person):
        check_person_weight_attribute(the_person)
        weight = __builtin__.round(the_person.weight * 2.205, 1)
        return str(weight)
