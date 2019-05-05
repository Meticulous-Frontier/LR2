# Just a small function so you don't have to write the full path every time you make a room.
# For background images just input bgImage("Background_Name")
init -2 python:
    def room_background_image(name):
        return Image("Mods/mods/Room/images/" + name)

    def prop_image(name):
        return Image("Mods/mods/Room/images/props/" + name)
