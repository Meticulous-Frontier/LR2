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
                label "ZipCache memory: {total_size:.2f} MB".format(total_size = get_size(zip_manager) / 1024.0 / 1024.0) xminimum 400
                label "ZipCache items: {}".format(zip_manager.size())
                label "Texture Memory: {total_size:.2f} MB ({num_of_items})".format(total_size = renpy.exports.get_texture_size()[0] / 1024.0 / 1024.0, num_of_items = renpy.exports.get_texture_size()[1])
                label "Image Cache: {size:.1f} / {max_size:.1f} MB".format(size = 4.0 * renpy.display.im.cache.get_total_size() / 1024.0 / 1024.0, max_size = 4.0 * renpy.display.im.cache.cache_limit / 1024.0 / 1024.0)
                label "Last character load time: {:.3f}".format(last_load_time)
                label ""
                label get_debug_log()


init 2 python:
    def validate_texture_memory():
        # keep texture memory below 1 Gb, even tough the max size is 2 Gb
        if renpy.exports.get_texture_size()[0] > 1024.0 * 1024.0 * 1024.0:
            renpy.display.im.cache.clear()  # cleanup texture cache
        return

    debug_log = LRUCacheDict(10, expiration = 0)

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
