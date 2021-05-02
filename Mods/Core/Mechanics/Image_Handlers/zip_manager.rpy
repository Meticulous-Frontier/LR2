############################################################
# MOD Implementation of ZIP file loading and image caching #
############################################################

init 5 python:
    from lru import LRUCacheDict

    # special class for managing thread locks and cache objects for zipfile loading
    class ZipManager():
        def __init__(self):
            self.Locks = {}
            self.Cache = {}
            self.max_items = 150 if persistent.zip_cache_size == 0 else 300

            for x in supported_positions + ["character_images"]:
                self.Locks[x] = threading.RLock()
                self.Cache[x] = LRUCacheDict(max_size = self.max_items, expiration = 0)    # 300 most used character images per position

        def preload(self):  # load main character images into the zip file cache (about 2700 images)
            for cloth in [white_skin, black_skin, tan_skin]:
                for position in supported_positions:
                    for body in ["standard_body","thin_body","curvy_body"] if cloth.body_dependant else ["standard_body"]:
                        for tits in Clothing_Images.breast_sizes if cloth.draws_breasts else ["AA"]:
                            file = cloth.position_sets[position].get_image(body, tits)
                            if file:
                                file.load()

        def size(self):
            return sum([x.size() for x in self.Cache.values()])

        def utilization(self):
            # result = {}
            # for k, v in self.Cache.iteritems():
            #     result[k] = []
            #     result[k].append(v.size())
            #     result[k].append(v.size() * 100.0 / float(self.max_items))
            # return result
            return (self.size() * 100.0 / (self.max_items * float(len(self.Cache))))

    class ZipContainer(renpy.display.im.ImageBase): #TODO: Move this to a more obvious file. Probably something to do along with a bunch of other refactoring.
        def __init__(self, position, filename, mtime=0, **properties):
            super(ZipContainer, self).__init__(position, filename, mtime, **properties)
            self.position = position
            self.filename = filename

        def load(self):
            try:
                if not self.filename in zip_manager.Cache[self.position]:
                    global mobile_zip_dict
                    with zip_manager.Locks[self.position]:
                        zip_manager.Cache[self.position][self.filename] = mobile_zip_dict[self.position].read(self.filename)

                sio = io.BytesIO(zip_manager.Cache[self.position][self.filename])
                return renpy.display.pgrender.load_image(sio, self.filename)
            except:
                return renpy.display.pgrender.surface((2, 2), True)    # same object als the Renpy image zip returns https://github.com/renpy/renpy/blob/master/renpy/display/im.py

    zip_manager = ZipManager()
    # if not config.debug:    # delays reload time (disable while debugging)
    #     zip_manager.preload()
