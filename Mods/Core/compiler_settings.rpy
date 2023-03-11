init -2 python:
    build.script_version = True
    build.classify("**.rpy", None) # don't include rpy files in build
    build.classify("**.bak", None)
    build.classify("**.ref", None)
    build.classify('**~', None)
    build.classify('**/#**', None)
    build.classify("**.back", None)
    build.classify("**.txt", None)
    build.classify("**.save", None)
    build.classify("**.drawio", None)
    build.classify("**/game/saves/**.**", None)
    build.classify("**.rpyb", None)
    build.classify("**.code-workspace", None)
    build.classify("game/animation/**.png", None)
    build.classify("game/customizations/**.**", None)
    build.classify("**.", None)
    build.classify("**.ps1", None)
    build.classify('**.json', None)
    # exclude icon images from build
    build.classify("game/Mods/Core/Images/**.ico", None)
    build.classify("game/Mods/Core/Images/**.icns", None)
    build.classify("game/Mods/Core/Images/**.pdn", None)

    if not renpy.mobile:
        # include existing .rpa files
        build.classify("**.rpa", "renpy")

        build.archive("background_images") #When building all mod background images are placed into an archive.
        build.classify("game/Mods/Room/images/**.jpg", "background_images")
        build.classify("game/Mods/Room/images/**.png", "background_images")

        build.archive("extra_character_images")
        build.classify("game/Mods/Core/Images/character_images/**.png", "extra_character_images")

        build.archive("gui")
        build.classify("game/gui/**.png", "gui")
        build.classify("game/Mods/Core/Images/**.png", "gui")

        build.archive("wardrobes")
        build.classify("game/wardrobes/Exported_Wardrobe.xml", "all") # make sure exported wardrobe file is included (but not archived)
        build.classify("game/wardrobes/**.xml", "wardrobes")
        build.classify("game/Mods/Wardrobes/**.xml", "wardrobes")

        build.archive("OpenGL")
        build.classify("game/OpenGL/**.**", "OpenGL")
        build.classify("game/shader/**.**", "OpenGL")

        build.archive("scripts")
        build.classify("game/**.rpyc", "scripts") # put compiled game files into scripts.rpa
        build.classify("game/Mods/**.py", "scripts")   # put python modules into scripts.rpa

        build.archive("fonts")
        build.classify("game/**.ttf", "fonts")
        build.classify("game/**.otf", "fonts")

        build.archive("tutorial_images")
        build.classify("game/images/**.png", "tutorial_images")
        build.classify("game/images/**.jpg", "tutorial_images")
        build.classify("game/Mods/Tutorial/**.png", "tutorial_images")

        build.archive("unit_tests")
        build.classify("game/unittest/**.**", "unit_tests")
        build.classify("game/integration_tests/**.**", "unit_tests")

init 2 python:
    build.name = "Lab_Rats_2_Mod"
    build.include_old_themes = False
    config.window_icon = get_file_handle("mod_icon.png")
    # disable debugging for release
    config.console = True
    config.debug = False
