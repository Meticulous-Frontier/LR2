init -2 python:
#    custom_layers = []
    #config.layers.insert(10,"2") # Definitively Infront of "Active" layer
    #config.layers.insert(11,"3")
    #config.layers.insert(12,"4")
    config.layers.insert(10,"5")
    #config.layers.insert(14,"6")
    #config.layers.insert(15,"7")
    config.layers.insert(11,"8")
    #config.layers.insert(17,"9")
    #config.layers.insert(18,"10")

#    custom_layers.append("2")
#    custom_layers.append("3")
#    custom_layers.append("4")
#    custom_layers.append("5")
#    custom_layers.append("6")
#    custom_layers.append("7")
#    custom_layers.append("8")
#    custom_layers.append("9")
#    custom_layers.append("10")

    #config.menu_clear_layers.append("2")
    #config.menu_clear_layers.append("3")
    #config.menu_clear_layers.append("4")
    config.menu_clear_layers.append("5")
    #config.menu_clear_layers.append("6")
    #config.menu_clear_layers.append("7")
    config.menu_clear_layers.append("8")
    #config.menu_clear_layers.append("9")
    #config.menu_clear_layers.append("10")

    #config.context_clear_layers.append("2")
    #config.context_clear_layers.append("3")
    #config.context_clear_layers.append("4")
    config.context_clear_layers.append("5")
    #config.context_clear_layers.append("6")
    #config.context_clear_layers.append("7")
    config.context_clear_layers.append("8")
    #config.context_clear_layers.append("9")
    #config.context_clear_layers.append("10")

    config.layer_clipping["5"] = [1380, 0, 540, 1080] # for menu hover draw
    config.layer_clipping["8"] = [1380, 0, 540, 1080] # for outfit manager mannequin

    #config.menu_clear_layers.append(custom_layers)
    #config.context_clear_layers.append(custom_layers)

init 2 python:

    # NOTE: As long as you are working with the same prop you can move it around without having to hide it first.
    # For testing purposes: draw_object("lollipop", 0.25, "10", place_prop(yalign = 0.225, xalign = 0.907, rotate = 5))
    def draw_object(prop, size, layers = "Active", transform = place_prop): # Input would be draw_object("filename", size, layer, place_prop(args))
        prop = prop_image(prop + ".png")
        size = size
        name = "Prop:" + "[prop]"
        transform = transform
        renpy.show(name, at_list=[transform, scale_person(size)], layer = layers, what = prop)


transform place_prop(yalign = 1.0, xalign = 1.0, xanchor = 1.0, rotate = 0.0):
    yalign  yalign
    xalign  xalign
    xanchor  xanchor
    rotate  rotate
