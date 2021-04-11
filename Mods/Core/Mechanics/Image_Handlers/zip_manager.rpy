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

            for x in supported_positions + ["character_images"]:
                self.Locks[x] = threading.RLock()
                self.Cache[x] = LRUCacheDict(max_size = 300, expiration = 0)    # 300 most used character images per position

        def preload(self):  # load main character images into the zip file cache (about 2700 images)
            for cloth in [white_skin, black_skin, tan_skin, breast_region, torso_region, stomach_region, pelvis_region] + hair_styles + pube_styles:
                for position in supported_positions:
                    for body in ["standard_body","thin_body","curvy_body"] if cloth.body_dependant else ["standard_body"]:
                        for tits in Clothing_Images.breast_sizes if cloth.draws_breasts else ["AA"]:
                            file = cloth.position_sets[position].get_image(body, tits)
                            if file:
                                file.load()

        def size(self):
            return sum([x.size() for x in self.Cache.values()])

    class ZipContainer(renpy.display.im.ImageBase): #TODO: Move this to a more obvious file. Probably something to do along with a bunch of other refactoring.
        def __init__(self, position, filename, mtime=0, **properties):
            super(ZipContainer, self).__init__(position, filename, mtime, **properties)
            self.position = position
            self.filename = filename

        def load(self):
            tries = 0
            while tries < 3:
                try:
                    if not self.filename in zip_manager.Cache[self.position]:
                        with zip_manager.Locks[self.position]:
                            zip_manager.Cache[self.position][self.filename] = mobile_zip_dict[self.position].read(self.filename)

                    sio = io.BytesIO(zip_manager.Cache[self.position][self.filename])
                    return renpy.display.pgrender.load_image(sio, self.filename)
                except:
                    tries += 1
                    if tries >= 3:
                        renpy.notify("Unsuccessful Load: " + self.position + " -> " + self.filename)
                        return renpy.display.pgrender.surface((2, 2), True)

                    with zip_manager.Locks[self.position]:
                        mobile_zip_dict[self.position].close()
                        mobile_zip_dict[self.position] = zipfile.ZipFile(renpy.file(get_file_handle(self.position + ".zip")), "r")

    zip_manager = ZipManager()
    # if not config.debug:    # delays reload time (disable while debugging)
    #     zip_manager.preload()
