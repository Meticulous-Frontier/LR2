init -1 python:
    def change_scene_display(the_location): #Switch displayed location and background image
        renpy.scene()
        renpy.show(the_location.name, what=the_location.background_image)
        return


    def is_public():
        if mc.location.public == True:
            return True
        else:
            return False

    def is_accessable():
        if mc.location.accessable == True:
            return True
        else:
            return False

    def is_day(dayname): # Can probably make this better..?

        if str(dayname) == "Monday" and day%7 == 0:
            return True
        if str(dayname) == "Tuesday" and day%7 == 1:
            return True
        if str(dayname) == "Wednesday" and day%7 == 2:
            return True
        if str(dayname) == "Thursday" and day%7 == 3:
            return True
        if str(dayname) == "Friday" and day%7 == 4:
            return True
        if str(dayname) == "Saturday" and day%7 == 5:
            return True
        if str(dayname) == "Sunday" and day%7 == 6:
            return True
        else:
            return False

    def is_time(time_name): # Can probably make this better..?

        if str(time_name) == "Early Morning" and time_of_day == 0:
            return True
        if str(time_name) == "Morning" and time_of_day == 1:
            return True
        if str(time_name) == "Afternoon" and time_of_day == 2:
            return True
        if str(time_name) == "Evening" and time_of_day == 3:
            return True
        if str(time_name) == "Night" and time_of_day == 4:
            return True
        else:
            return False
