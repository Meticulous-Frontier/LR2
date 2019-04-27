init -1 python:
    # Overrides VREN's height function, so we display the height based on the weight property
    # instead of the fixed weight on zoom factor
    def height_to_string(person_height): #Height is a value between 0.8 and 1.0
        total_inches = __builtin__.round(person_height * 75)
        feet = int(__builtin__.round(total_inches // 12))
        inches = int(__builtin__.round(total_inches % 12))

        return str(feet) + "' " + str(inches) + "\""

    # Check if weight property exists on person, if not, add based on body type
    def check_person_weight_attribute(person):
        if not hasattr(person, "weight"):
            if (person.body_type == "thin_body"):
                setattr(person, "weight", 60 * person.height)   # default weight thin body
            elif (person.body_type == "standard_body"):
                setattr(person, "weight", 75 * person.height)   # default weight standard body
            else:
                setattr(person, "weight", 90 * person.height)   # default weight curvy body
        return

    # Returns True when the persons body type has changed; otherwise False
    # chance is probability percentage that weight change for amount will occur (used by serums)
    def change_weight(self, amount, chance):
        check_person_weight_attribute(self)
        if (amount == 0):
            return False

        if renpy.random.randint(0, 100) <= chance:
            self.weight += amount
        
        # maximum and minimum weight are dependant on height
        max_weight = self.height * 100
        min_weight = self.height * 50
        switch_point_low = self.height * 68
        switch_point_high = self.height * 83

        if (amount > 0):
            if self.weight > switch_point_low + 3 and self.body_type == "thin_body":
                self.body_type = "standard_body"
                return True
            if self.weight > switch_point_high + 3 and self.body_type == "standard_body":
                self.body_type = "curvy_body"
                return True
            if self.weight > max_weight: #Maximum weight
                self.weight = max_weight
            return False

        if (amount < 0):
            if self.weight < min_weight:  #Minimum weight
                self.weight = min_weight
                return False
            if self.weight < switch_point_low - 3 and self.body_type == "standard_body":
                self.body_type = "thin_body"        
                return True
            if self.weight < switch_point_high - 3 and self.body_type == "curvy_body":
                self.body_type = "standard_body"
                return True
            return False
    
    # attach change weight function to the Person class
    Person.change_weight = change_weight

    def get_person_weight_string(person):
        check_person_weight_attribute(person)
        weight = __builtin__.round(person.weight * 2.205, 1)
        return str(weight)
