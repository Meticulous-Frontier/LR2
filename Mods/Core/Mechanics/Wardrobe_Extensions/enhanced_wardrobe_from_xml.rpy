init 1 python:
    def get_wardrobe_file(xml_filename):
        file_name = xml_filename + ".xml"
        wardrobe_file = None
        
        for file in renpy.list_files():
            if file_name in file:
                wardrobe_file = renpy.file(file)
                break

        return wardrobe_file

    def get_xml_files_from_path():
        result = []
        files = renpy.list_files()
        for file in files:
            if file.endswith(".xml"):
                base = os.path.basename(file)
                result.append(os.path.splitext(base)[0])
        result.sort()
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