init 1 python:
    def get_wardrobe_file(xml_filename):
        # make sure we don't have an .xml extension on the filename
        wardrobe_name = os.path.splitext(xml_filename)[0]

        file_path = os.path.abspath(os.path.join(config.basedir, "game"))
        file_path = os.path.join(file_path,"wardrobes")
        file_name = os.path.join(file_path, wardrobe_name + ".xml")

        if not os.path.isfile(file_name):
            # try to find the wardrobe in the mods location
            file_path = os.path.abspath(os.path.join(config.basedir, "game"))
            file_path = os.path.join(file_path,"Mods")
            file_path = os.path.join(file_path,"Wardrobes")
            file_name = os.path.join(file_path, wardrobe_name + ".xml")

            if not os.path.isfile(file_name):
                return None
        return file_name

    def get_xml_files_from_path(path_array):
        result = []
        for p in path_array:
            for n in os.listdir(p):
                if n.endswith(".xml"):
                    result.append(n)
        return result

    def wardrobe_from_xml(xml_filename):
        file_name = get_wardrobe_file(xml_filename)
        if file_name is None:
            return Wardrobe("[xml_filename]") #If there is no wardrobe present we return an empty wardrobe with the name of our file.

        wardrobe_tree = ET.parse(file_name)
        tree_root = wardrobe_tree.getroot()

        return_wardrobe = Wardrobe(tree_root.attrib["name"])
        for outfit_element in tree_root.find("FullSets"):
            return_wardrobe.add_outfit(outfit_from_xml(outfit_element))
        for outfit_element in tree_root.find("UnderwearSets"):
            return_wardrobe.add_underwear_set(outfit_from_xml(outfit_element))
        for outfit_element in tree_root.find("OverwearSets"):
            return_wardrobe.add_overwear_set(outfit_from_xml(outfit_element))
        return return_wardrobe

    def import_wardrobe(wardrobe, xml_filename): # This is a rewrite of the wardrobe_from_xml function written by Vren.
                                                 # Wardrobe should be who's / what wardrobe you want to import into. e.g for main character it is mc.designed_wardrobe
        wardrobe = wardrobe

        file_name = get_wardrobe_file(xml_filename)
        if file_name is None:
            return Wardrobe("[xml_filename]") #If there is no wardrobe present we return an empty wardrobe with the name of our file.

        wardrobe_tree = ET.parse(file_name)
        tree_root = wardrobe_tree.getroot()

        return_wardrobe = Wardrobe(tree_root.attrib["name"])
        for outfit_element in tree_root.find("FullSets"):
            wardrobe.add_outfit(outfit_from_xml(outfit_element))

        for outfit_element in tree_root.find("UnderwearSets"):
            wardrobe.add_underwear_set(outfit_from_xml(outfit_element))

        for outfit_element in tree_root.find("OverwearSets"):
            wardrobe.add_overwear_set(outfit_from_xml(outfit_element))

        return return_wardrobe