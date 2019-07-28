init 2:
    screen show_serum_inventory(the_inventory, extra_inventories = [],inventory_names = []): #You can now pass extra inventories, as well as names for all of the inventories you are passing. Returns nothing, but is used to view inventories.
        add "Science_Menu_Background.png"
        hbox:
            $ count = 0
            xalign 0.05
            yalign 0.05
            spacing 40
            for an_inventory in [the_inventory] + extra_inventories:
                frame:
                    background "#888888"
                    xsize 400
                    vbox:
                        xalign 0.02
                        yalign 0.02
                        frame:
                            background "#000080"
                            xsize 390
                            if len(inventory_names) > 0 and count < len(inventory_names):
                                text inventory_names[count] style "serum_text_style_header"
                            else:
                                text "Serums in Inventory" style "serum_text_style_header"

                        for design in an_inventory.serums_held:
                            textbutton design[0].name + ": " + str(design[1]) + " Doses":
                                xsize 390
                                style "textbutton_style"
                                text_style "serum_text_style"
                                action Show("serum_tooltip",None,design[0])
                                sensitive True
                                hovered Show("serum_tooltip",None,design[0])

                    $ count += 1

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return(), Hide("serum_tooltip")]
            textbutton "Return" align [0.5,0.5] style "return_button_style"
