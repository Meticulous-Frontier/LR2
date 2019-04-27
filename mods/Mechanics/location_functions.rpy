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

    def is_day(day_name):
        if dayname in day_names:           
            return day % 7 == day_names.index(dayname)
        return False

    def is_time(time_name):
        if time_name in time_names:
            return time_of_day == time_names.index(time_name)
        return False
