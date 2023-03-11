# Just a small function so you don't have to write the full path every time you make a room.
# For background images just input bgImage("Background_Name")
init -2 python:
    def darken_background(image):
        return im.MatrixColor(image, im.matrix.saturation(0.9)*im.matrix.tint(.9,.9,.9)*im.matrix.brightness(-0.15))

    def room_background_image(name, darken = True):
        handle = get_file_handle(name)

        return Image(handle)

        # early_morning_background = darken_background(Image(handle))
        # morning_background = Image(handle)
        # afternoon_background = Image(handle)
        # evening_background = Image(handle)
        # night_background = darken_background(Image(handle))

        # return [early_morning_background, morning_background , afternoon_background, evening_background, night_background]

    def prop_image(name):
        return Image(get_file_handle(name))

    def get_file_handle(file_name):
        found = None
        for file in renpy.list_files():
            if file_name in file:
                found = file
                break

        return found
