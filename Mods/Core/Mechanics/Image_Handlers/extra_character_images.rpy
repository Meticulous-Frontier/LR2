init -100 python:
    import threading
    config.search_prefixes = [ "Mods/Core/Images/", "", "images/" ]

init 2 python:
    gui.main_menu_background = "LR2_Title.png"
    gui.game_menu_background = "LR2_Title.png"

init -5 python:
    global supported_positions
    supported_positions = ["stand2","stand3","stand4","stand5","walking_away","kissing","doggy","missionary","blowjob","against_wall","back_peek","sitting","kneeling1","standing_doggy","cowgirl"]

init 2 python:
    # add zip dictionary for MOD character images
    mobile_zip_dict["character_images"] = zipfile.ZipFile(renpy.file(get_file_handle("character_images.zip")), "r") #Cache all of the zip files so we have a single static pointer to them.

    # clothing objects for MOD character images
    secret_mask = Facial_Accessory("Secret Mask", 2, False, False, "Secret_Mask", False, False, 0, display_name = "masks", opacity_adjustment = .5)
    earings_list.append(secret_mask)

    cop_blouse = Clothing("Cop Blouse", 2, True, True, "Cop_Blouse", True, False, 0, supported_patterns = {"Friezes":"Pattern_1"}, tucked = True, whiteness_adjustment = 0.2, display_name = "shirt",
        can_be_half_off = True, half_off_regions = [breast_region], half_off_ignore_regions = [upper_arm_region, lower_arm_region], half_off_gives_access = True, half_off_reveals = True,
        constrain_regions = [torso_region, upper_arm_region, lower_arm_region, stomach_region])
    shirts_list.append(cop_blouse) # excluded from outfit creator / wardrobe builder

    cop_pants = Clothing("Cop Pants", 2, True, True, "Cop_Pants", False, False, 0, whiteness_adjustment = 0.2, supported_patterns = {"Belt":"Pattern_1"}, display_name = "pants",
        can_be_half_off = True, half_off_regions = [pelvis_region], half_off_ignore_regions = [upper_leg_region], half_off_gives_access = True, half_off_reveals = True,
        constrain_regions = [upper_leg_region, lower_leg_region, pelvis_region])
    pants_list.append(cop_pants) # excluded from outfit creator / wardrobe builder

    master_clothing_offset_dict["Secret_Mask"] = {"cowgirl":(266,221), "missionary":(338,93), "kissing":(282,62), "sitting":(387,192), "against_wall":(202,64), "back_peek":(169,103), "blowjob":(227,282), "stand4":(231,111), "stand5":(249,91), "standing_doggy":(146,144), "kneeling1":(248,219), "walking_away":(190,103), "doggy":(319,454), "stand2":(172,115), "stand3":(205,77)}

    master_clothing_offset_dict["Cop_Pants"] = {"cowgirl":(52,543), "missionary":(96,400), "kissing":(216,399), "sitting":(125,518), "against_wall":(109,413), "back_peek":(109,432), "blowjob":(117,560), "stand4":(129,425), "stand5":(131,397), "standing_doggy":(193,301), "kneeling1":(107,563), "walking_away":(127,417), "doggy":(82,484), "stand2":(89,434), "stand3":(72,404)}

    master_clothing_offset_dict["Cop_Blouse"] = {"cowgirl":(148,273), "missionary":(158,192), "kissing":(88,168), "sitting":(238,269), "against_wall":(48,158), "back_peek":(107,190), "blowjob":(98,314), "stand4":(96,186), "stand5":(111,174), "standing_doggy":(75,164), "kneeling1":(156,313), "walking_away":(100,172), "doggy":(135,464), "stand2":(51,204), "stand3":(99,160)}

    #################################################################
    # override image get functions to allow for mod image retrieval #
    #################################################################

    def clothing_get_image(self, body_type, breast_size = "AA" ): #Generates a proper Image object from the file path strings we have stored previously. Prevents object bloat by storing large objects repeatedly for everyone.
        global mobile_zip_dict

        index_string = body_type + "_" + breast_size
        if index_string in self.images and self.images[index_string] in mobile_zip_dict[self.position_name].namelist():
            return ZipContainer(self.position_name, self.images[index_string])

        if self.clothing_name: # check if we have a mod image for the clothing item
            fileName = self.clothing_name + "_" + self.position_name +  "_" + body_type + "_" + breast_size + ".png"
            if fileName in mobile_zip_dict["character_images"].namelist():
                return ZipContainer("character_images", fileName)
        return empty_image

    Clothing_Images.get_image = clothing_get_image

    def facial_accessory_get_image(self, face, emotion, special_modifier = None):
        global mobile_zip_dict
        index_string = face + "_" + emotion
        if special_modifier:
            if self.images[index_string + "_" + special_modifier] in mobile_zip_dict[self.position_name].namelist():
                return ZipContainer(self.position_name, self.images[index_string + "_" + special_modifier])

        if self.images[index_string] in mobile_zip_dict[self.position_name].namelist():
            return ZipContainer(self.position_name, self.images[index_string])

        # check if we have a mod image for the clothing item
        if self.images[index_string] in mobile_zip_dict["character_images"].namelist():
            return ZipContainer("character_images", self.images[index_string])

        return empty_image

    Facial_Accessory_Images.get_image = facial_accessory_get_image

    def expression_generate_emotion_displayable(self,position,emotion, special_modifier = None, eye_colour = None, lighting = None):
        if not emotion in self.emotion_set:
            emotion = "default" #Get our default emotion to show if we get an incorrect one.
        elif special_modifier and special_modifier in self.special_modifiers:
            emotion = emotion + "_" + special_modifier

        if lighting is None:
            lighting = [1,1,1]

        if eye_colour is None:
            eye_colour = [.62, .42, .29, 1.0] #brown by default.

        if not emotion in self.position_dict[position]:
            return Image("character_images/empty_holder.png")

        #renpy.notify("Lighting: {r}, {g}, {b}\nEye Color: {r1}, {g1}, {b1}".format(r=lighting[0], g=lighting[1], b=lighting[2], r1=eye_colour[0], g1=eye_colour[1], b1=eye_colour[2]))

        base_image = ZipContainer(position, self.position_dict[position][emotion])
        mask_image = ZipContainer(position, self.position_dict[position][emotion].replace("_" + self.skin_colour,"_Pattern_1"))

        # correctly lighted
        base_image = im.MatrixColor(base_image, im.matrix.tint(*lighting))

        # grey-scaled with slight brightness boost
        gray_scaled_image = im.MatrixColor(base_image, im.matrix.saturation(0) * im.matrix.brightness(.2))
        # colorized with eye colour
        colorized_image = im.MatrixColor(gray_scaled_image, im.matrix.tint(eye_colour[0], eye_colour[1], eye_colour[2]) * im.matrix.tint(*lighting))
        # only use eyes from colorized gray scale
        shader_image = AlphaMask(colorized_image, mask_image)

        # blend shader pattern into base image (mask location only)
        return Composite((0,0), (0,0), base_image, (0,0), shader_image)

    Expression.generate_emotion_displayable = expression_generate_emotion_displayable

    def expression_generate_raw_image(self, position, emotion, special_modifier = None):
        if not emotion in self.emotion_set:
            emotion = "default" #Get our default emotion to show if we get an incorrect one.
        elif special_modifier and special_modifier in self.special_modifiers:
            emotion = emotion + "_" + special_modifier

        if not emotion in self.position_dict[position]:
            return Image("character_images/empty_holder.png")

        return ZipContainer(position, self.position_dict[position][emotion])

    Expression.generate_raw_image = expression_generate_raw_image

    def clothing_generate_stat_slug(self): #Generates a string of text/tokens representing what layer this clothing item is/covers
        cloth_info = ""
        if self.layer == 4:
            cloth_info += "{image=gui/extra_images/overwear_token.png}"
        if self.layer == 3:
            if self in neckwear_list:
                cloth_info += "{image=gui/extra_images/necklace_token.png}"
            else:
                cloth_info += "{image=gui/extra_images/clothing_token.png}"
        if self.layer == 2:
            if self in shoes_list:
                cloth_info += "{image=gui/extra_images/shoes_token.png}"
            elif self in [light_eye_shadow, heavy_eye_shadow, blush, lipstick]:
                cloth_info += "{image=gui/extra_images/makeup_token.png}"
            else:
                cloth_info += "{image=gui/extra_images/accessory_token.png}"
        if self.layer == 1:
            if self in socks_list:
                cloth_info += "{image=gui/extra_images/stocking_token.png}"
            else:
                cloth_info += "{image=gui/extra_images/underwear_token.png}"
        if self.layer == 0:
            cloth_info += "{image=gui/extra_images/sexy_underwear_token.png}"

        if self.has_extension: #Display a second token if the clothing item is a different part (split coverage into top and bottom?)
            if self.has_extension.layer == 4:
                cloth_info += "|{image=gui/extra_images/overwear_token.png}"
            if self.has_extension.layer == 3:
                if self.has_extension in [neckwear_list]:
                    cloth_info += "|{image=gui/extra_images/accessory_token.png}"
                else:
                    cloth_info += "|{image=gui/extra_images/clothing_token.png}"
            if self.has_extension.layer == 2:
                if self.has_extension == leotard_bottom:
                    cloth_info += "|{image=gui/extra_images/clothing_token.png}"
                elif self.has_extension in shoes_list:
                    cloth_info += "|{image=gui/extra_images/shoes_token.png}"
                else:
                    cloth_info += "|{image=gui/extra_images/accessory_token.png}"
            if self.has_extension.layer == 1:
                cloth_info += "|{image=gui/extra_images/underwear_token.png}"
            if self.has_extension.layer == 0:
                cloth_info += "|{image=gui/extra_images/sexy_underwear_token.png}"

        # Match modifier in `get_total_slut_modifiers_enhanced()` for now
        cloth_info += "+" +str(self.get_slut_value()) + "{image=gui/heart/red_heart.png}"
        return cloth_info

    Clothing.generate_stat_slug = clothing_generate_stat_slug
