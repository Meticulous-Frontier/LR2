init -1 python:
    def change_scene_display(the_location): #Switch displayed location and background image
        renpy.scene()
        renpy.show(the_location.name, what=the_location.background_image)
        return