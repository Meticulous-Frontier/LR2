#init -100 python:
    # Fix compatibility of save games.

init -4 python:
    # IMPORTED FROM BUGFIX
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
    default persistent.memory_mode = 1 # default is medium memory mode
    default persistent.use_free_memory = True   # default is clean memory every day
    default persistent.show_ntr = False     # default turn of NTR

init python: # place first on the hijack stack
    add_label_hijack("after_load", "check_save_version")

init 5 python: # add to stack later then other mods
    config.label_overrides["start"] = "alternative_start"

    add_label_hijack("normal_start", "activate_compatibility_fix")
    add_label_hijack("after_load", "update_compatibility_fix")
    add_label_hijack("start", "check_mod_installation")

    if take_animation_screenshot in config.interact_callbacks:
        config.interact_callbacks.remove(take_animation_screenshot)

init 100 python:
    add_label_hijack("normal_start", "store_game_version")

init -1 python:
    # override some of the default settings to improve performance
    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if renpy.variant("pc"):
        # disables renpy.free_memory() daily cleanup, thus requires enough memory to perform operations
        if persistent.memory_mode == 0:
            config.image_cache_size_mb = 384
        elif persistent.memory_mode == 1:
            config.image_cache_size_mb = 768
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

    def check_bugfix_installed():
        if not bugfix_installed:
            renpy.say("Warning", "You are running the game without bugfix installed, the mod no longer works without this bugfix due to the many issues in the base game. Download {a=https://github.com/Tristimdorion/Lab-Rats-2/releases}the correct version here{/a}. The game will now exit.")
            renpy.quit()
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

label alternative_start:
    scene bg paper_menu_background with fade

    $ check_bugfix_installed()

    "Lab Rats 2 contains adult content. If you are not over 18 or your countries equivalent age you should not view this content."
    menu:
        "I am over 18":
            "Excellent, let's continue then."

        "I am not over 18":
            $renpy.full_restart()

    "Vren" "[config.version] represents an early iteration of Lab Rats 2. Expect to run into limited content, unexplained features, and unbalanced game mechanics."
    "Vren" "Would you like to view the FAQ?"
    menu:
        "View the FAQ":
            call faq_loop from _call_faq_loop_alt_start
        "Get on with the game!":
            "You can access the FAQ from your bedroom at any time."

    "Vren" "Lab Rats 2 contains content related to impregnation and pregnancy. These settings may be changed in the menu at any time."
    menu:
        "No pregnancy content\n{size=16}Girls never become pregnant. Most pregnancy content hidden.{/size}":
            $ persistent.pregnancy_pref = 0

        "Predictable pregnancy content\n{size=16}Birth control is 100%% effective. Girls always default to taking birth control.{/size}":
            $ persistent.pregnancy_pref = 1

        "Realistic pregnancy content\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

    $ renpy.block_rollback()
    call screen character_create_screen()
    $ return_arrays = _return #These are the stat, skill, and sex arrays returned from the character creator.
    call create_test_variables(store.name,store.b_name,store.l_name,return_arrays[0],return_arrays[1],return_arrays[2]) from _call_create_test_variables_alt_start ##Moving some of this to an init block (init 1specifically) would let this play better with updates in the future.
    $ renpy.block_rollback()
    menu:
        "Play introduction and tutorial":
            call tutorial_start from _call_tutorial_start_alt_start

        "Skip introduction and tutorial":
            $ mc.business.event_triggers_dict["Tutorial_Section"] = False
    jump normal_start
