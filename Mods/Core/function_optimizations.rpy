# this file contains optimized version for some of the display generation functions
# these need to be reviewed every update
init 5 python:

    def optimized_generate_item_displayable_facial_accessory(self, position, face_type, emotion, special_modifiers = None, lighting = None):
        if not self.is_extension:
            if lighting is None:
                lighting = [1,1,1]

            image_set = self.position_sets.get(position)
            if image_set is None:
                image_set = self.position_sets.get("stand3") #Get a default image set if we are looking at a position we do not have.

            the_image = image_set.get_image(face_type, emotion, special_modifiers)
            if not the_image:
                the_image = image_set.get_image(face_type, emotion) # If we weren't able to get something with the special modifier just use a default to prevent a crash.

            return im.MatrixColor(im.MatrixColor(the_image, im.matrix.opacity(self.opacity_adjustment) * im.matrix.brightness(self.whiteness_adjustment) * im.matrix.contrast(self.contrast_adjustment)), im.matrix.opacity(self.colour[3]) * im.matrix.tint(self.colour[0], self.colour[1], self.colour[2]) * im.matrix.tint(*lighting)) #Now colour the final greyscale image

    Facial_Accessory.generate_item_displayable = optimized_generate_item_displayable_facial_accessory

    def optimized_generate_item_displayable_clothing(self, body_type, tit_size, position, lighting = None, regions_constrained = None):
        if not self.is_extension: #We don't draw extension items, because the image is taken care of in the main object.
            if lighting is None:
                lighting = [1,1,1]

            if not self.body_dependant:
                body_type = "standard_body"

            image_set = self.position_sets.get(position) # The image set we are using should corrispond to the set named "positon".
            if image_set is None:
                image_set = self.position_sets.get("stand3")

            if self.draws_breasts:
                the_image = image_set.get_image(body_type, tit_size)
            else:
                the_image = image_set.get_image(body_type, "AA")

            if regions_constrained is None:
                regions_constrained = []

            if self.pattern is not None:
                pattern_set = self.pattern_sets.get(position+"_"+self.pattern)
                if pattern_set is None:
                    mask_image = None
                elif self.draws_breasts:
                    mask_image = pattern_set.get_image(body_type, tit_size)
                else:
                    mask_image = pattern_set.get_image(body_type, "AA")

                if mask_image is None:
                    self.pattern = None

            #This is the base greyscale image we have
            greyscale_image = im.MatrixColor(the_image, im.matrix.opacity(self.opacity_adjustment) * im.matrix.brightness(self.whiteness_adjustment) * im.matrix.contrast(self.contrast_adjustment)) #Set the image, which will crush all modifiers to 1 (so that future modifiers are applied to a flat image correctly with no unusually large images
            final_image = im.MatrixColor(greyscale_image, im.matrix.opacity(self.colour[3]) * im.matrix.tint(self.colour[0], self.colour[1], self.colour[2]) * im.matrix.tint(*lighting)) #Now colour the final greyscale image

            if self.pattern and mask_image:
                #mask_red_alpha_invert = im.MatrixColor(mask_image, [0,0,0,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,1]) #Inverts the pattern colour so the shader applies properly.
                #shader_image = im.AlphaMask(base,
                #im.composite(
                # shader_red_invert = im.Alpha

                final_image = AlphaBlend(mask_image, final_image, im.MatrixColor(greyscale_image, im.matrix.opacity(self.colour_pattern[3] * self.colour[3]) * im.matrix.tint(self.colour_pattern[0], self.colour_pattern[1], self.colour_pattern[2]) * im.matrix.tint(*lighting)), alpha=False)

            if len(regions_constrained)>0:
                # We want to support clothing "constraining", or masking, lower images. This is done by region.
                # Each constraining region effectively subtracts itself + a blurred border around it, and then the body region is added back in so it appears through clothing.

                composite_list = None
                for region in regions_constrained:
                    #Begin by building a total mask of all constrained regions
                    region_mask = Image(region.generate_item_image_name(body_type, tit_size, position))

                    if composite_list is None:
                        composite_list = [renpy.image_size(region_mask)]
                    composite_list.append((0,0))
                    composite_list.append(region_mask)

                constrained_region_mask = im.MatrixColor(im.Blur(im.Composite(*composite_list), 8), [1,0,0,0,0, 0,1,0,0,0, 0,0,1,0,0, 0,0,0,8,0]) #This is the area to be subracted from the image.
                composite_list.extend([(0,0), Image(all_regions.generate_item_image_name(body_type, tit_size, position))])
                final_image = AlphaBlend(AlphaBlend(constrained_region_mask, Solid("#FFFFFFFF"), im.Composite(*composite_list)), Solid("#00000000"), final_image)

            if self.half_off:
                #NOTE: This actually produces some really good looking effects for water/stuff. We should add these kinds of effects as a general thing, probably on the pattern level.
                #NOTE: Particularly for water/stains, this could work really well (and can use skin-tight region marking, ie. not clothing item dependant).

                composite_list = None
                for region_to_hide in self.half_off_regions: #We first add together all of the region masks so we only operate on a single displayable
                    region_mask = Image(region_to_hide.generate_item_image_name(body_type, tit_size, position))
                    if composite_list is None:
                        composite_list = [renpy.image_size(region_mask)]
                    composite_list.append((0,0))
                    composite_list.append(region_mask)

                transparency_control_image = im.MatrixColor(im.Blur(im.Composite(*composite_list), 12), [1,0,0,0,0, 0,1,0,0,0, 0,0,1,0,0, 0,0,0,7,0]) #...We increase the contribution of alpha from the mask, so a small amount ends up being 100% (this still preserves some gradient at the edge as well)

                if self.half_off_ignore_regions: #Sometimes you want hard edges, or a section of a piece of clothing not to be moved. These regions are not blured/enlarged and are subtracted from the mask generated above.
                    add_composite_list = None
                    for region_to_add in self.half_off_ignore_regions:
                        region_mask = Image(region_to_add.generate_item_image_name(body_type, tit_size, position))
                        if add_composite_list is None:
                            add_composite_list = [renpy.image_size(region_mask)] #We can reuse the size from our first pass building the mask.
                        add_composite_list.append((0,0))
                        add_composite_list.append(region_mask)

                    transparency_control_image = AlphaBlend(im.Composite(*add_composite_list), transparency_control_image, Solid("#00000000"), True) #This alpha blend effectively subtracts the half_off_ignore mask from the half_off region mask

                final_image = AlphaBlend(transparency_control_image, final_image, Solid("#00000000"), True) #Use the final mask to hide parts of the clothing image as appopriate.

            return final_image

    Clothing.generate_item_displayable = optimized_generate_item_displayable_clothing
