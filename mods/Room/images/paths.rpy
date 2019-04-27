# Just a small function so you don't have to write the full path every time you make a room.
# For background images just input bgImage("Background_Name")
init -2 python:
    def bgImage(imagePath):
        imagePath = Image("Mods/mods/Room/images/" + imagePath + ".jpg")

        return imagePath

    def propImage(imagePath):
        imagePath = Image("Mods/mods/Room/images/props/" + imagePath + ".png")

        return imagePath
