init -2 python:
    build.classify("**.rpy", None) # don't include rpy files in build
    build.classify("**.bak", None)
    build.classify('**~', None)
    build.classify('**/#**', None)
    build.classify("**.back", None)
    build.classify("**.txt", None)
    build.classify("**.save", None)
    build.classify("**/game/saves/**.**", None)
    build.classify("**.rpyb", None)
    build.classify("**.code-workspace", None)
    build.classify("game/animation/**.png", None)
    build.classify("game/customizations/**.**", None)
    build.classify("**.", None)
    build.classify("game/OpenGL/DLLS/gle_**", None)
    build.classify("game/wardrobes/Exported_Wardrobe.xml", "all") # make sure exported wardrobe file is included (but not archived)

    build.archive("background_images") #When building all mod background images are placed into an archive.
    build.classify("game/Mods/Room/images/**.jpg", "background_images")
    build.classify("game/Mods/Room/images/**.png", "background_images")
    build.classify("game/Mods/Tutorial/**.png", "background_images")
    build.classify("game/images/**.png", "background_images")
    build.classify("game/images/**.jpg", "background_images")

    build.archive("gui")
    build.classify("game/gui/**.png", "gui")
    build.classify("game/Mods/Core/Images/**.png", "gui")

    build.archive("wardrobes")
    build.classify("game/wardrobes/**.xml", "wardrobes")
    build.classify("game/Mods/Wardrobes/**.xml", "wardrobes")

    build.archive("OpenGL")
    build.classify("game/OpenGL/**.**", "OpenGL")
    build.classify("game/shader/**.**", "OpenGL")

    build.archive("scripts")
    build.classify("game/**.rpyc", "scripts") # put compiled game files into scripts.rpa

    build.archive("fonts")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "fonts")