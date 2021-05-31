init -1:
    $ serum_transfer_amount = 1 # By default transfer 1 at a time, changed by player input. Right clicking by default transfers 10 at a time
    python:
        def serum_transfer_amount_func(new_amount):
            if new_amount is "":
                new_amount = 1
            elif new_amount is "0": #Figure out exactly how this works and then make it work :)
                new_amount = 1
            elif __builtin__.int(new_amount) == 0:
                new_amount = 1
            store.serum_transfer_amount = __builtin__.int(new_amount)

init -2 style serum_text_style: # Cheat Text Style
    text_align 0.5
    size 20
    color "#dddddd"
    outlines [(2,"#222222",0,0)]
    xalign 0.5

init 2:
    screen serum_trade_ui(inventory_1,inventory_2,name_1="Player",name_2="Business"): #Lets you trade serums back and forth between two different inventories. Inventory 1 is assumed to be the players.
        add "Science_Menu_Background.png"

        frame:
            background "#0a142688"
            xalign 0.2
            xanchor 0.5
            yalign 0.5

            vbox:
                xsize 590
                ysize 900
                yalign 0.0
                frame:
                    background "#000080"
                    xsize 590
                    text "Trade Serums Between Inventories" style "menu_text_title_style" xalign 0.5

                frame:
                    background "#0a142688"
                    xalign 0.5

                    viewport:
                        scrollbars "vertical"
                        xsize 650
                        mousewheel True
                        hbox:
                            xalign 0.5
                            vbox:
                                xalign 0.5

                                for serum in set(inventory_1.get_serum_type_list()) | set(inventory_2.get_serum_type_list()): #Gets a unique entry for each serum design that shows up in either list. Doesn't duplicate if it's in both.
                                    # has a few things. 1) name of serum design. 2) count of first inventory, 3) arrows for transfering, 4) count of second inventory.

                                    vbox:
                                        textbutton serum.name:
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 560

                                            action ToggleScreen("serum_tooltip", None, serum, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                            hovered Show("serum_tooltip", None, serum, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                        hbox:
                                            frame:
                                                background "#000080"
                                                xsize 170
                                                # How many serums in inventory_1 (player's)
                                                text name_1 + ": " + str(inventory_1.get_serum_count(serum)) style "serum_text_style"

                                            null width 10

                                            textbutton "|<" action [Function(inventory_1.change_serum,serum,inventory_2.get_serum_count(serum)),Function(inventory_2.change_serum,serum,-inventory_2.get_serum_count(serum))] sensitive (inventory_2.get_serum_count(serum) > 0) style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            textbutton "<<" action [Function(inventory_1.change_serum,serum,10),Function(inventory_2.change_serum,serum,-10)] sensitive (inventory_2.get_serum_count(serum) > 9) style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            textbutton "<" action [Function(inventory_1.change_serum,serum, serum_transfer_amount),Function(inventory_2.change_serum,serum, -serum_transfer_amount)] sensitive (inventory_2.get_serum_count(serum) > serum_transfer_amount - 1) style "textbutton_no_padding_highlight" text_style "serum_text_style"

                                            null width 10
                                            button:
                                                id "serum_transfer_amount"
                                                style "textbutton_style"

                                                action NullAction()
                                                unhovered Function(renpy.restart_interaction) #TODO: Tweak this so it is less annoying  and fix any associated errors

                                                add Input(
                                                    size =  20,
                                                    color = "#dddddd",
                                                    default = serum_transfer_amount,
                                                    changed = serum_transfer_amount_func,
                                                    length = 4,
                                                    button = renpy.get_widget("serum_trade_ui", "serum_transfer_amount"),
                                                    allow = "0123456789"
                                                )

                                            null width 10

                                            textbutton ">" action [Function(inventory_2.change_serum,serum, serum_transfer_amount),Function(inventory_1.change_serum,serum,-serum_transfer_amount)] sensitive (inventory_1.get_serum_count(serum) > serum_transfer_amount - 1) style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            textbutton ">>" action [Function(inventory_2.change_serum,serum,10),Function(inventory_1.change_serum,serum,-10)] sensitive (inventory_1.get_serum_count(serum) > 9) style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            textbutton ">|" action [Function(inventory_2.change_serum,serum,inventory_1.get_serum_count(serum)),Function(inventory_1.change_serum,serum,-inventory_1.get_serum_count(serum))] sensitive (inventory_1.get_serum_count(serum) > 0) style "textbutton_no_padding_highlight" text_style "serum_text_style"

                                            null width 10

                                            frame:
                                                background "#000080"
                                                xsize 170
                                                text name_2 + ": " + str(inventory_2.get_serum_count(serum)) style "serum_text_style"

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
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
