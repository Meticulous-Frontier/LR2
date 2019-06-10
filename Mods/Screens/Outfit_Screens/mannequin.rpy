init 2 python:
    def show_mannequin(demo_outfit):
        renpy.show_transient_screen("mannequin", demo_outfit)
    def hide_mannequin():
        renpy.hide_screen("mannequin")

    def draw_mannequin(self , outfit, position = None, emotion = None, special_modifier = None): #Draw the person, standing as default if they aren't standing in any other position.
            renpy.scene("Active")
            if position is None:
                position = self.idle_pose #Easiest change is to call this and get a random standing posture instead of a specific idle pose. We redraw fairly frequently so she will change position frequently.
            #self.hair_style.draw_hair_back(self.hair_colour,self.height) #NOTE: Not currently used to see if it's actually needed.

            displayable_list = [] # We will be building up a list of displayables passed to us by the various objects on the person (their body, clothing, etc.)

            if emotion is None:
                emotion = self.get_emotion()

            displayable_list.append(self.body_images.generate_item_displayable(self.body_type,self.tits,position)) #Add the body displayable

            displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier)) #Get the face displayable

            size_render = renpy.render(displayable_list[0], 10, 10, 0, 0) #We need a render object to check the actual size of the body displayable so we can build our composite accordingly.
            the_size = size_render.get_size() # Get the size. Without it our displayable would be stuck in the top left when we changed the size ofthings inside it.
            x_size = __builtin__.int(the_size[0])
            y_size = __builtin__.int(the_size[1])



            displayable_list.extend(outfit.generate_draw_list(self,position,emotion,special_modifier)) #Get the displayables for everything we wear. Note that extnsions do not return anything because they have nothing to show.
            displayable_list.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position)) #Get hair

            #NOTE: default return for the_size is floats, even though it is in exact pixels. Use int here otherwise positional modifiers like xanchor and yalign do not work (no displayable is shown at all!)
            composite_list = [(x_size,y_size)] #Now we build a list of our parameters, done like this so they are arbitrarily long
            for display in displayable_list:
                composite_list.append((0,0)) #Center all displaybles on the top left corner, because of how they are rendered they will all line up.
                composite_list.append(display) #Append the actual displayable

            final_image = Composite(*composite_list) # Create a composite image using all of the displayables

            renpy.show(self.name,at_list=[character_right, scale_person(self.height)],layer="Active",what=final_image,tag=self.name)

    Person.draw_mannequin = draw_mannequin

init 2: # Moved to screen so that it can be refreshed upon changes made in outfit_creator
    screen mannequin(outfit, model = "mannequin"):
        $ renpy.scene("Active")
        zorder 102
        fixed: #TODO: Move this to it's own screen so it can be shown anywhere
            pos (1450,0)

            if model == "mannequin":
                add mannequin_average
                if outfit is not None:
                    for cloth in outfit.generate_draw_list(None,"stand3"):
                        add cloth

            else:

                $ model.draw_mannequin(outfit)
