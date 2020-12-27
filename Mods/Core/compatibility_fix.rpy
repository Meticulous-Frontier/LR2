#init -100 python:
    # Fix compatibility of save games.

init -2:
    default persistent.memory_mode = 0 # default is low memory mode
    default persistent.use_free_memory = True   # default is clean memory every day
    default persistent.show_ntr = False     # default turn of NTR

init 5 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_compatibility_fix")
    add_label_hijack("after_load", "update_compatibility_fix")
    add_label_hijack("start", "check_mod_installation")

init 100 python:
    def parse_version_string(version):
        parts = version.split(".")
        return int(parts[0].strip("v")), int(parts[1]), int(parts[2])

    def get_loaded_version():
        if "game_version" in globals():
            loaded_version = game_version
        else:
            loaded_version = "v0.33.3"
        return loaded_version

    add_label_hijack("normal_start", "store_game_version")
    add_label_hijack("after_load", "check_save_version")

init -1 python:
    # override some of the default settings to improve performance
    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if renpy.variant("pc"):
        # disables renpy.free_memory() daily cleanup, thus requires enough memory to perform operations
        if persistent.memory_mode == 0:
            config.image_cache_size_mb = 256
        elif persistent.memory_mode == 1:
            config.image_cache_size_mb = 512
        else:
            config.image_cache_size_mb = 1536
    else:
        config.image_cache_size_mb = 384 # low memory devices like phones (uses renpy.free_memory() for daily memory clean)

    # allow for more idle objects
    config.automatic_images = None
    config.optimize_texture_bounds = True
    config.predict_statements = 32
    config.rollback_length = 64      # since refactor we can allow a longer rollback history
    config.cache_surfaces = False
    config.predict_screen_statements = False
    config.predict_screens = False

    # disable auto save
    config.autosave_on_choice = False
    config.has_autosave = False
    config.autosave_slots = 6
    # config.autosave_frequency = 200 # default: 200

    # for DEBUG only (uncomment when you get a cPickle error)
    # config.use_cpickle = False
    # config.debug_image_cache = True

    def restore_employees_to_schedules():
        for employee in mc.business.research_team + mc.business.market_team + mc.business.supply_team + mc.business.production_team + mc.business.hr_team:
            if employee.location:
                continue
            # somehow she is lost in limbo
            scheduled_location = employee.get_destination()
            if not scheduled_location: # pick random location
                scheduled_location = get_random_from_list([x for x in list_of_places if x.public])

            if scheduled_location:
                scheduled_location.add_person(employee)
        return

    def update_pinned_cache():
        # cache all GUI images in memory
        for fn in renpy.list_files():
            if (re.search("gui", fn, re.IGNORECASE)
                and fn.endswith(".png")):
                renpy.cache_pin(fn)
        return

    # remove full outfits / overwear from default wardrobe that have no shoes or no layer 2 clothing items (nude outfits)
    # to prevent messed up outfits to be used by girls in daily life
    def cleanup_default_wardrobe():
        remove = []
        for outfit in default_wardrobe.outfits:
            if not any(x for x in outfit.feet if x.layer == 2):
                remove.append(outfit)
            elif not any(x for x in outfit.upper_body if x.layer == 2):
                remove.append(outfit)
            elif not any(x for x in outfit.lower_body if x.layer == 2):
                remove.append(outfit)

        # renpy.say("", "Removing " + str(len(remove)) + " full outfits")
        for outfit in remove:
            default_wardrobe.outfits.remove(outfit)

        remove = []
        for outfit in default_wardrobe.overwear_sets:
            if not any(x for x in outfit.feet if x.layer == 2):
                remove.append(outfit)
            elif not any(x for x in outfit.upper_body if x.layer == 2):
                remove.append(outfit)
            elif not any(x for x in outfit.lower_body if x.layer == 2):
                remove.append(outfit)

        # renpy.say("", "Removing " + str(len(remove)) + " overwear sets")
        for outfit in remove:
            default_wardrobe.overwear_sets.remove(outfit)
        return

    def validate_mod_installation_location():
        handle = get_file_handle("mod_icon.png")
        if not handle.startswith("Mods"):
            renpy.say("Warning", "The game mod is not installed correctly, make sure the 'Mods' folder is directly in your 'game' folder\nIt should read like '<base>/game/Mods'.")
        return

    def check_bugfix_installed():
        if not bugfix_installed:
            renpy.say("Warning", "You are running the game without bugfix installed, this will lead to various issues while playing due to errors in the original game code. Download {a=https://github.com/Tristimdorion/Lab-Rats-2/releases}the correct version here{/a}.")
        return

label check_mod_installation(stack):
    $ validate_mod_installation_location()

    $ execute_hijack_call(stack)
    return

label activate_compatibility_fix(stack):
    # make sure we store the crisis tracker in the save game
    $ crisis_tracker_dict = {}

    $ update_pinned_cache()

    $ cleanup_default_wardrobe()

    $ execute_hijack_call(stack)
    return

label update_compatibility_fix(stack):
    if not "crisis_tracker_dict" in globals():
        $ crisis_tracker_dict = {}

    $ update_pinned_cache()

    $ cleanup_default_wardrobe()

    $ restore_employees_to_schedules()

    $ execute_hijack_call(stack)
    return

label store_game_version(stack):
    $ game_version = config.version
    $ check_bugfix_installed()
    $ execute_hijack_call(stack)
    return

label check_save_version(stack):
    $ loaded_version = get_loaded_version()
    $ check_bugfix_installed()

    if not "game_version" in globals():
        "Warning" "You are loading a save game from an un-modded game. This is not supported, start a new modded game."
    elif parse_version_string(loaded_version)[1] < parse_version_string(config.version)[1]:
        "Warning" "You are loading an incompatible game version ([loaded_version]). Please start a new game."
    elif parse_version_string(loaded_version)[2] < parse_version_string(config.version)[2]:
        "Warning" "You are loading a game created by a previous build ([loaded_version]), you might run into errors because of this. Before reporting errors, please start a new modded game and see if the problem persists."
    $ execute_hijack_call(stack)
    return
