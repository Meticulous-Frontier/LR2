init 2:
    define debug_log_enabled = False
    define last_load_time = 0.0

    style debug_label_text:
        size 14
        italic False
        bold False
        color "#ffffff"
        outlines [(2,"#222222",0,0)]

    screen DebugInfo():
        style_prefix "debug"
        zorder 100

        drag:
            drag_name "DebugInfo"
            xalign .9
            yalign 0
            drag_handle(0.0,0.0, 1.0,1.0)
            frame:
                background "#00000055"
                xmaximum 600
                padding (5,5)
                has vbox
                label "ZipCache memory: {total_size:.2f} MB".format(total_size = system_info.total_zip_size / 1024.0 / 1024.0) xminimum 400
                label "ZipCache items: {count} ({utilization:.1f}%)".format(count = system_info.total_zip_items, utilization = system_info.zip_utilization)
                label "Texture Memory: {total_size:.2f} MB ({num_of_items})".format(total_size = system_info.texture_size / 1024.0 / 1024.0, num_of_items = system_info.texture_count)
                label "Image Cache: {size:.1f} / {max_size:.1f} MB ({utilization:.1f}%)".format(size = 4.0 * system_info.cache_size / 1024.0 / 1024.0, max_size = 4.0 * renpy.display.im.cache.cache_limit / 1024.0 / 1024.0, utilization = system_info.cache_size * 100.0 / renpy.display.im.cache.cache_limit)
                label "Last character load time: {:.3f}".format(last_load_time)
                label ""
                label get_debug_log()


init 2 python:

    class SystemInfo():
        def __init__(self):
            self.total_zip_size = 0
            self.total_zip_items = 0
            self.zip_utilization = 0
            self.texture_size = 0
            self.texture_count = 0
            self.cache_size = 0

        def update(self):
            self.total_zip_size = get_size(zip_manager)
            self.total_zip_items = zip_manager.size()
            self.zip_utilization = zip_manager.utilization()
            self.texture_size, self.texture_count = renpy.exports.get_texture_size()
            self.cache_size = renpy.display.im.cache.get_total_size()


    system_info = SystemInfo()


    def validate_texture_memory():
        while not hasattr(renpy.display.draw, "get_texture_size"):
            time.sleep(2)

        print("Activate texture memory watcher")
        while True:
            # keep texture memory below 1 Gb, even tough the max size is 2 Gb
            if renpy.display.draw.get_texture_size()[0] > (renpy.display.im.cache.cache_limit * 4 * 4):
                renpy.display.im.cache.clear()  # cleanup texture cache

            if debug_log_enabled:
                system_info.update()
            time.sleep(.25)
        return

    debug_log = LRUCacheDict(8, expiration = 0)

    # The preload thread.
    texture_monitor_thread = threading.Thread(target=validate_texture_memory, name="texture_monitor")
    texture_monitor_thread.setDaemon(True)
    texture_monitor_thread.start()

    renpy.config.per_frame_screens.append("DebugInfo")

    def show_debug_log():
        global debug_log_enabled
        debug_log_enabled = True
        renpy.show_screen("DebugInfo")

    def hide_debug_log():
        global debug_log_enabled
        debug_log_enabled = False
        renpy.hide_screen("DebugInfo")

    def add_to_debug_log(message, start_time = time.time()):
        debug_log["T" + str(time.time())] = message.format(total_time = time.time() - start_time)

    def get_debug_log():
        return "\n".join(OrderedDict(sorted(debug_log._LRUCacheDict__values.items(), key=lambda t: t[0], reverse = True)).values())

    def get_persons_size():
        return sum([get_size(x) for x in all_people_in_the_game()])

    def get_size(obj, seen = None):
        size = sys.getsizeof(obj)
        if not seen:
            seen = set()
        if id(obj) in seen:
             return 0
        # Important mark as seen *before* entering recursion to gracefully handle
        # self-referential objects
        seen.add(id(obj))
        try:
            if isinstance(obj, collections.Mapping):
                size += sum([get_size(v, seen) for v in obj.values()])
                size += sum([get_size(k, seen) for k in obj.keys()])
            elif hasattr(obj, '__dict__'):  # sum all object attributes
                size += sum([get_size(getattr(obj, name), seen) for name in obj.__dict__.keys()])
            elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
                size += sum([get_size(i, seen) for i in obj])
            elif isinstance(obj, (str, bytes, bytearray)):
                size += len(obj)
        except:
            pass
        return size
