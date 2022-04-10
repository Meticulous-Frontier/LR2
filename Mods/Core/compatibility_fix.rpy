#init -100 python:
    # Fix compatibility of save games.

init -4 python:
    # IMPORTED FROM BUGFIX - PREVENT CRASH WHEN BUGFIX NOT INSTALLED.
    # Custom implementation for mapped list, that reference the list_item.identifier instead of the actual object
    # list_func is the function retrieving the original list (we don't want to reference the original list)
    class MappedList():
        def __init__(self, type, list_func, new_list = []):
            self.type = type
            self.list_func = list_func
            if new_list:
                self.mapped_list = new_list
            else:
                self.mapped_list = []

        def __getitem__(self, key):
            if isinstance( key, slice ) :
                #Get the start, stop, and step from the slice
                return [self[ii] for ii in xrange(*key.indices(len(self)))]
            elif isinstance(key, int):
                if key < 0 : #Handle negative indices
                    key += len( self )
                if key < 0 or key >= len( self ) :
                    raise IndexError
                return next((x for x in self.list_func() if x.identifier == self.mapped_list[key]), None)
            raise TypeError

        def __setitem__(self, key, item):
            if not isinstance(key, int):
                raise TypeError
            if isinstance(item, self.type):
                self.mapped_list[key] = item.identifier

        def __delitem__(self, key):
            if not isinstance(key, int):
                raise TypeError
            del self.mapped_list[key]

        def __repr__(self):
            return repr(self())

        def __call__(self):
            return [x for x in self.list_func() if x.identifier in self.mapped_list]

        def __iter__(self):
            item_list = self.list_func()
            for item in self.mapped_list:
                found = next((x for x in item_list if x.identifier == item), None)
                if found:
                    yield found
                else: # item is no longer in main list (remove it from mapping)
                    self.mapped_list.remove(item)

        def __len__(self):
            return len(self.mapped_list)

        def __contains__(self, item):
            if isinstance(item, self.type):
                return any(x for x in self.mapped_list if x == item.identifier)

        def __add__(self, other):
            if isinstance(other, MappedList):
                return MappedList(self.type, self.list_func, self.mapped_list.copy() + other.mapped_list.copy())
            if isinstance(other, list):
                new_list = self.mapped_list.copy()
                new_list.extend([x.identifier for x in other if isinstance(x, self.type)])
                return MappedList(self.type, self.list_func, new_list)

        def __sub__(self, other):
            if isinstance(other, MappedList):
                return MappedList(self.type, self.list_func, list(set(self.mapped_list.copy())-set(other.mapped_list.copy())))
            if isinstance(other, list):
                new_list = self.mapped_list.copy()
                for item in other:
                    if isinstance(item, self.type) and item.identifier in new_list:
                        new_list.remove(item.identifier)
                return MappedList(self.type, self.list_func, new_list)

        def __iadd__(self, other):
            self.append(other)
            return self

        def __isub__(self, other):
            self.remove(other)
            return self

        def append(self, item):
            if isinstance(item, self.type):
                if not item.identifier in self.mapped_list:
                    self.mapped_list.append(item.identifier)

        def remove(self, item):
            if isinstance(item, self.type):
                if item.identifier in self.mapped_list:
                    self.mapped_list.remove(item.identifier)

        def clear(self):
            self.mapped_list.clear()

        def extend(self, other):
            if isinstance(other, MappedList):
                self.mapped_list.extend(other.mapped_list)
            if isinstance(other, list):
                self.mapped_list.extend([x.identifier for x in other])

        def pop(self, index = -1):
            identifier = self.mapped_list.pop(index)
            return next((x for x in self.list_func() if x.identifier == identifier), None)

        def index(self, item):
            if isinstance(item, self.type):
                return self.mapped_list.index(item.identifier)
            raise ValueError

    def parse_version_string(version):
        parts = version.split(".")
        return int(parts[0].strip("v")), int(parts[1]), int(parts[2])

    def get_loaded_version():
        if "game_version" in globals():
            loaded_version = game_version
        else:
            loaded_version = "v0.33.3"
        return loaded_version

init -2:
    default persistent.zip_cache_size = 0 # default is small size
    default persistent.show_ntr = False     # default turn of NTR
    default persistent.keep_patreon_characters = True  # keep VREN original characters from hire process

init python: # place first on the hijack stack
    add_label_hijack("after_load", "check_save_version")

init 5 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_compatibility_fix")
    add_label_hijack("after_load", "update_compatibility_fix")
    add_label_hijack("start", "check_mod_installation")

    hook_label("start", check_bugfix_installed)

init 100 python:
    add_label_hijack("normal_start", "store_game_version")

init 1 python:
    global is64Bit
    is64Bit = sys.maxsize > 2**32

    # override some of the default settings to improve performance
    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if is64Bit:
        config.image_cache_size_mb = 768 # fixed at 768 Mb * 4 bytes per pixel
    else:
        config.image_cache_size_mb = 384 # fixed at 384 Mb * 4 bytes per pixel

    # heart pasties and cincher (move to level 0)
    heart_pasties.layer = 0
    cincher.layer = 0

    # pencil skirt pussy usable to False
    pencil_skirt.anchor_below = True

    # disable gl2 extensions
    if renpy.android or renpy.mobile:
        config.gl2 = False
        persistent.vren_animation = False

    # allow for more idle objects
    config.automatic_images = None
    config.optimize_texture_bounds = True
    config.predict_statements = 64 if is64Bit else 32
    config.rollback_length = 64 if is64Bit else 32      # since refactor we can allow a longer rollback history
    config.cache_surfaces = False
    config.predict_screen_statements = False
    config.predict_screens = False
    config.list_compression_length = 200        # increase list compression length for rollback

    # disable auto save
    config.autosave_on_choice = False
    config.autosave_on_quit = False
    config.autosave_on_input = False
    config.has_autosave = False
    config.has_quicksave = True
    config.autosave_slots = 6
    # config.autosave_frequency = 200 # default: 200

    # for DEBUG only (uncomment when you get a cPickle error)
    # config.use_cpickle = False
    # config.debug_image_cache = True

    # disable sound settings
    config.has_sound = False
    config.has_music = False
    config.has_voice = False

    # extend main_loop_cleanup list from bugfix
    if "common_variable_list" in globals():
        common_variable_list.append("scene_manager");
        common_variable_list.append('HR_employee_list');

    def update_pinned_cache():
        # cache all GUI images in memory
        for fn in renpy.list_files():
            if re.search("[\\/][gG]ui[\\/][a-zA-Z_\\/]*.png", fn, re.IGNORECASE):
                renpy.cache_pin(fn)
            if "empty_holder.png" in fn:
                renpy.cache_pin(fn)
        return

    # remove full outfits / overwear from default wardrobe that have no shoes or no layer 2 clothing items (nude outfits)
    # to prevent messed up outfits to be used by girls in daily life
    def cleanup_default_wardrobe():
        remove = []
        for outfit in default_wardrobe.outfits + default_wardrobe.overwear_sets:
            if not any(x for x in outfit.feet if x.layer == 2):
                remove.append(outfit)
            elif not any(x for x in outfit.upper_body if x.layer == 2 or x.layer == 3):
                remove.append(outfit)
            elif not any(x for x in outfit.upper_body if x.layer == 2 and x.has_extension) and \
                not any(x for x in outfit.lower_body if x.layer == 2):
                remove.append(outfit)

        for outfit in remove:
            # print("Removing: " + outfit.name)
            default_wardrobe.remove_outfit(outfit)
        return

    def validate_mod_installation_location():
        handle = get_file_handle("mod_icon.png")
        if not handle.startswith("Mods"):
            renpy.say("Warning", "The game mod is not installed correctly, make sure the 'Mods' folder is directly in your 'game' folder\nIt should read like '<base>/game/Mods'.")
        return

    def validate_stripclub_stripper_role():
        if not "stripclub_stripper_job" in globals():
            global stripclub_stripper_job
            stripclub_stripper_job = Job("Stripper", stripclub_stripper_role, job_location = strip_club, work_days = [0,1,2,3,4,5,6], work_times = [3,4], hire_function = stripper_hire, quit_function = stripper_quit)
        return

    def check_bugfix_installed(*args, **kwargs): #allow passing of any number of parameters
        if not bugfix_installed:
            renpy.say("Warning", "You are running the game without bugfix installed, the mod no longer works without this bugfix due to the many issues in the base game. Download {a=https://github.com/Tristimdorion/Lab-Rats-2/releases}the correct version here{/a}. The game will now exit.")
            renpy.quit()
        return

    def validate_harem_roles():
        if not "harem_role" in globals():
            global harem_role
            harem_role = Role("Girlfriend in Polyamory", get_harem_role_actions(), role_dates = get_harem_role_dates(), looks_like = girlfriend_role) #Generic specific girlfriend role.
        if not "cousin_girlfriend_role" in globals():
            global cousin_girlfriend_role
            cousin_girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), looks_like = girlfriend_role) #Generic specific girlfriend role.
        if not "aunt_girlfriend_role" in globals():
            global aunt_girlfriend_role
            aunt_girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), looks_like = girlfriend_role) #Generic girlfriend role.
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

    $ validate_harem_roles()

    $ cleanup_default_wardrobe()

    # make beta saves compatible
    if not list_of_jobs or not isinstance(list_of_jobs[0], list):
        call instantiate_jobs() from _call_instantiate_jobs
        call add_extra_room_job_definitions() from _call_add_extra_room_job_definitions

    $ validate_stripclub_stripper_role()

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
        $ renpy.full_restart()
        return
    elif parse_version_string(loaded_version)[1] < parse_version_string(config.version)[1]:
        "Warning" "You are loading an incompatible game version ([loaded_version]). Please start a new game."
        $ renpy.full_restart()
        return
    elif parse_version_string(loaded_version)[2] < parse_version_string(config.version)[2]:
        "Warning" "You are loading a game created by a previous build ([loaded_version]), you might run into errors because of this. Before reporting errors, please start a new modded game and see if the problem persists."
    $ execute_hijack_call(stack)
    return
