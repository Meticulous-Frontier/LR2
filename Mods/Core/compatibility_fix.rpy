#init -100 python:
    # Fix compatibility of save games.

init -2:
    if renpy.variant("pc"):
        default persistent.high_memory_mode = True
    else:
        default persistent.high_memory_mode = False        

init 5 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_compatibility_fix")
    add_label_hijack("after_load", "update_compatibility_fix")

init -1 python:
    # override some of the default settings to improve performance
    if renpy.variant("pc"):
        if persistent.high_memory_mode:
            config.image_cache_size = 96
        else:
            config.image_cache_size = 32
    else:
        config.image_cache_size = 8
        # on a PC we should have enough memory to build a full image cache
    config.automatic_images = None
    config.optimize_texture_bounds = True
    config.predict_statements = 8
    #config.image_cache_size_mb = 1024  # this setting does not have the desired effect (always 200 Mb of image_cache memory)
    config.cache_surfaces = False
    config.predict_screens = False

    # for DEBUG only (uncomment when you get a cPickle error)
    # config.use_cpickle = False
    # config.debug_image_cache = True

    def update_pinned_cache():
        # cache all GUI images in memory
        for fn in renpy.list_files():
            if (re.search("gui", fn, re.IGNORECASE) 
                and fn.endswith(".png")):
                renpy.cache_pin(fn)

label activate_compatibility_fix(stack):
    # make sure we store the crisis tracker in the save game
    $ crisis_tracker_dict = {}

    $ update_pinned_cache()

    $ execute_hijack_call(stack)
    return

label update_compatibility_fix(stack):
    if not "crisis_tracker_dict" in globals():
        $ crisis_tracker_dict = {}

    $ update_pinned_cache()

    $ execute_hijack_call(stack)
    return


