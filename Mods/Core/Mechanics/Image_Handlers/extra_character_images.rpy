init -10 python:
    import threading
    config.search_prefixes = [ "", "images/", "Mods/Core/Images/" ]

init -5 python:
    global supported_positions
    supported_positions = ["stand2","stand3","stand4","stand5","walking_away","kissing","doggy","missionary","blowjob","against_wall","back_peek","sitting","kneeling1","standing_doggy","cowgirl"]

init 2 python:
    # add zip dictionary for MOD character images
    mobile_zip_dict["character_images"] = zipfile.ZipFile(renpy.file(get_file_handle("character_images.zip")), "r") #Cache all of the zip files so we have a single static pointer to them.

    # clothing objects for MOD character images
    secret_mask = Facial_Accessory("Secret Mask", 2, False, False, "Secret_Mask", False, False, 0, display_name = "masks", opacity_adjustment = .5)
    earings_list.append(secret_mask)

    cop_blouse = Clothing("Cop Blouse", 2, True, True, "Cop_Blouse", True, False, 0, supported_patterns = {"Friezes":"Pattern_1"}, tucked = True, whiteness_adjustment = 0.2, display_name = "uniform",
        can_be_half_off = True, half_off_regions = [breast_region], half_off_ignore_regions = [upper_arm_region, lower_arm_region], half_off_gives_access = True, half_off_reveals = True,
        constrain_regions = [torso_region, upper_arm_region, lower_arm_region, stomach_region])
    shirts_list.append(cop_blouse) # excluded from outfit creator / wardrobe builder

    cop_pants = Clothing("Cop Pants", 2, True, True, "Cop_Pants", False, False, 0, whiteness_adjustment = 0.2, supported_patterns = {"Belt":"Pattern_1"}, display_name = "uniform",
        can_be_half_off = True, half_off_regions = [pelvis_region], half_off_ignore_regions = [upper_leg_region], half_off_gives_access = True, half_off_reveals = True,
        constrain_regions = [upper_leg_region, lower_leg_region, pelvis_region])
    pants_list.append(cop_pants) # excluded from outfit creator / wardrobe builder

    master_clothing_offset_dict["Secret_Mask"] = {"cowgirl":(266,221), "missionary":(338,93), "kissing":(282,62), "sitting":(387,192), "against_wall":(202,64), "back_peek":(169,103), "blowjob":(227,282), "stand4":(231,111), "stand5":(249,91), "standing_doggy":(146,144), "kneeling1":(248,219), "walking_away":(190,103), "doggy":(319,454), "stand2":(172,115), "stand3":(205,77)}

    master_clothing_offset_dict["Cop_Pants"] = {"cowgirl":(52,543), "missionary":(96,400), "kissing":(216,399), "sitting":(125,518), "against_wall":(109,413), "back_peek":(109,432), "blowjob":(117,560), "stand4":(129,425), "stand5":(131,397), "standing_doggy":(193,301), "kneeling1":(107,563), "walking_away":(127,417), "doggy":(82,484), "stand2":(89,434), "stand3":(72,404)}

    master_clothing_offset_dict["Cop_Blouse"] = {"cowgirl":(148,273), "missionary":(158,192), "kissing":(88,168), "sitting":(238,269), "against_wall":(48,158), "back_peek":(107,190), "blowjob":(98,314), "stand4":(96,186), "stand5":(111,174), "standing_doggy":(75,164), "kneeling1":(156,313), "walking_away":(100,172), "doggy":(135,464), "stand2":(51,204), "stand3":(99,160)}

    #################################################################
    # override image get functions to allow for mod image retrieval #
    #################################################################

    def can_use_animation():
        return False    # NO ANIMATIONS IN MOD

    def clothing_get_image(self, body_type, breast_size = "AA" ): #Generates a proper Image object from the file path strings we have stored previously. Prevents object bloat by storing large objects repeatedly for everyone.
        global mobile_zip_dict

        index_string = body_type + "_" + breast_size
        if index_string in self.images and self.images[index_string] in mobile_zip_dict[self.position_name].namelist():
            return ZipContainer(self.position_name, self.images[index_string])

        if self.clothing_name: # check if we have a mod image for the clothing item
            fileName = self.clothing_name + "_" + self.position_name +  "_" + body_type + "_" + breast_size + ".png"
            if fileName in mobile_zip_dict["character_images"].namelist():
                return ZipContainer("character_images", fileName)
        return Image("character_images/empty_holder.png")

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

        return Image("character_images/empty_holder.png")

    Facial_Accessory_Images.get_image = facial_accessory_get_image

    def expression_generate_emotion_displayable(self,position,emotion, special_modifier = None, eye_colour = None, lighting = None):
        if not emotion in self.emotion_set:
            emotion = "default" #Get our default emotion to show if we get an incorrect one.
        elif special_modifier and special_modifier in self.special_modifiers:
            emotion = emotion + "_" + special_modifier

        if lighting is None:
            lighting = [1,1,1]

        if eye_colour is None:
            eye_colour = [0.8,0.8,0.8,1] #grey by default.

        if not emotion in self.position_dict[position]:
            return Image("character_images/empty_holder.png")

        base_name = self.position_dict[position][emotion]
        base_image = ZipContainer(position, base_name)

        mask_name = self.position_dict[position][emotion].replace("_" + self.skin_colour,"_Pattern_1")
        mask_image = ZipContainer(position, mask_name)

        base_image = im.MatrixColor(base_image, im.matrix.tint(*lighting)) #To support the lighting of the room we also retint it here.
        return AlphaBlend(mask_image, base_image, im.MatrixColor(base_image, im.matrix.tint(eye_colour[0], eye_colour[1], eye_colour[2]) * im.matrix.tint(*lighting)), alpha=False)

    Expression.generate_emotion_displayable = expression_generate_emotion_displayable
