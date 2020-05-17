#init -100 python:
    # Fix compatibility of save games.

init -2:
    default persistent.high_memory_mode = False # default is low memory mode
    default persistent.use_free_memory = True   # default is clean memory every day

init 5 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_compatibility_fix")
    add_label_hijack("after_load", "update_compatibility_fix")
    add_label_hijack("start", "check_mod_installation")

init -1 python:
    # override some of the default settings to improve performance
    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if renpy.variant("pc"):
        # disables renpy.free_memory() daily cleanup, thus requires enough memory to perform operations
        if persistent.high_memory_mode:
            config.image_cache_size_mb = 1536
        else:
            config.image_cache_size_mb = 512
    else:
        config.image_cache_size_mb = 384 # low memory devices like phones (uses renpy.free_memory() for daily memory clean)

    # allow for more idle objects
    config.automatic_images = None
    config.optimize_texture_bounds = True
    config.predict_statements = 16
    config.rollback_length = 8      # limit rollback to reduce object tracking
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
        return

    def validate_mod_installation_location():
        handle = get_file_handle("mod_icon.png")
        if not handle.startswith("Mods"):
            renpy.say("Warning", "The mod is not installed correctly, make sure the 'Mod' folder is directly in your 'game' folder\nIt should read like '<base>/game/Mods'.")
        return

label check_mod_installation(stack):
    $ validate_mod_installation_location()

    $ execute_hijack_call(stack)
    return

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


