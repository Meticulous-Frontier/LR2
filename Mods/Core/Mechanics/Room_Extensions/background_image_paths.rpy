# Just a small function so you don't have to write the full path every time you make a room.
# For background images just input bgImage("Background_Name")
init -2 python:
    def darken_background(image):
        return im.MatrixColor(image, im.matrix.saturation(0.9)*im.matrix.tint(.9,.9,.9)*im.matrix.brightness(-0.15))

    def room_background_image(name, darken = True):
        handle = get_file_handle(name)

        if darken:
            early_morning_background = darken_background(Image(handle))
        else:
            early_morning_background = Image(Image(handle))

        morning_background = Image(Image(handle))
        afternoon_background = Image(Image(handle))
        evening_background = Image(Image(handle))

        if darken:
            night_background = darken_background(Image(handle))
        else:
            night_background = Image(Image(handle))

        room_background_images = [early_morning_background, morning_background , afternoon_background, evening_background, night_background]
        return room_background_images

    def prop_image(name):
        return Image(get_file_handle(name))

    def get_file_handle(file_name):
        found = None
        for file in renpy.list_files():
            if file_name in file:
                found = file
                break

        return found
