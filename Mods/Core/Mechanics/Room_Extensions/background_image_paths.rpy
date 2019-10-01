# Just a small function so you don't have to write the full path every time you make a room.
# For background images just input bgImage("Background_Name")
init -2 python:
    def room_background_image(name):

        early_morning_background = Image("Mods/Room/images/" + name)
        morning_background = Image("Mods/Room/images/" + name)
        afternoon_background = Image("Mods/Room/images/" + name)
        evening_background = Image("Mods/Room/images/" + name)
        night_background = Image("Mods/Room/images/" + name)

        room_background_images = [early_morning_background, morning_background , afternoon_background, evening_background, night_background]
        return room_background_images

    def prop_image(name):
        return Image("Mods/Room/images/props/" + name)
