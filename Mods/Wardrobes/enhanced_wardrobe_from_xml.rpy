init 1 python:
    def wardrobe_from_xml(xml_filename):
        file_path = os.path.abspath(os.path.join(config.basedir, "game"))
        file_path = os.path.join(file_path,"wardrobes")
        file_name = os.path.join(file_path, xml_filename + ".xml")

        if not os.path.isfile(file_name):
            # try to find the wardrobe in the mods location
            file_path = os.path.abspath(os.path.join(config.basedir, "game"))
            file_path = os.path.join(file_path,"Mods")
            file_path = os.path.join(file_path,"Wardrobes")
            file_name = os.path.join(file_path, xml_filename + ".xml")

            if not os.path.isfile(file_name):
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
