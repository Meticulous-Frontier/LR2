init 2:
    screen serum_sell_ui():
        add "Science_Menu_Background.png"
        #use serum_tooltip
        modal True
        hbox:
            spacing 40
            xalign 0.05
            yalign 0.05
            frame:
                background "#1a45a1aa"
                xsize 700 ysize 820
                vbox:
                    hbox:
                        xsize 700
                        text "Serum In Stock" style "menu_text_title_style" size 20 xalign 0.0
                        text "Sell Serum" style "menu_text_title_style" size 20 xalign 0.9 xanchor 1.0
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        vbox:
                            for serum_stock in mc.business.inventory.serums_held:
                                $ the_serum = serum_stock[0]
                                $ serum_amount = serum_stock[1]
                                hbox:
                                    $ serum_dose_value = mc.business.get_serum_base_value(the_serum, round_value = True)
                                    use serum_design_menu_item(the_serum, name_addition = ": " + str(serum_amount) + " Doses, $" + str(serum_dose_value) + "/Dose")
                                    textbutton "1":
                                        ysize 64
                                        xsize 50
                                        text_yalign 0.5
                                        text_xalign 0.5
                                        text_yanchor 0.5
                                        action Function(mc.business.sell_serum, the_serum)
                                        style "textbutton_style" text_style "textbutton_text_style"
                                        sensitive serum_amount >= 1
                                    textbutton "10":
                                        ysize 64
                                        xsize 50
                                        text_yalign 0.5
                                        text_xalign 0.5
                                        text_yanchor 0.5
                                        action Function(mc.business.sell_serum, the_serum, serum_count = 10)
                                        style "textbutton_style" text_style "textbutton_text_style"
                                        sensitive serum_amount >= 10
                                    textbutton "All":
                                        ysize 64
                                        xsize 50
                                        text_yalign 0.5
                                        text_xalign 0.5
                                        text_yanchor 0.5
                                        action Function(mc.business.sell_serum, the_serum, serum_count = serum_amount)
                                        style "textbutton_style" text_style "textbutton_text_style"
                                        sensitive serum_amount > 0


                #TODO: This holds the current serem selections


            vbox:
                spacing 40
                frame:
                    background "#1a45a1aa"
                    xsize 800 ysize 230
                    #TODO: Holds current information about aspect price, attention, market reach
                    vbox:
                        hbox:
                            textbutton "Market Reach:":
                                action VrenNullAction style "textbutton_style" text_style "textbutton_text_style"
                                tooltip "How many people have heard about your business. The larger your market reach the more each serum aspect point is worth."

                            text str(mc.business.market_reach) + " People" style "textbutton_text_style" yalign 0.5

                            null width 50

                            text "Current Funds: {color=#98fb98}$" + str(mc.business.funds) + "{/color}" style "textbutton_text_style" yalign 0.5

                        hbox:
                            textbutton "Attention:":
                                action VrenNullAction style "textbutton_style" text_style "textbutton_text_style"
                                tooltip "How much attention your business has drawn. If this gets too high the authorities will act, outlawing a serum design, leveling a fine, or seizing your inventory."

                            $ attention_info = get_attention_string(mc.business.attention, mc.business.max_attention) + " (-" + str(mc.business.attention_bleed) + "/Day)"
                            text "[attention_info]" style "textbutton_text_style" yalign 0.5

                        null height 8

                        text "Aspect Data" style "menu_text_title_style"
                        frame:
                            background "#00000088"
                            xsize 780
                            grid 6 3:
                                xfill True
                                null

                                text "Mental" style "menu_text_style" color "#387aff"
                                text "Physical" style "menu_text_style" color "#00AA00"
                                text "Sexual" style "menu_text_style" color "#FFC0CB"
                                text "Medical" style "menu_text_style" color "#FFFFFF"
                                text "Flaws" style "menu_text_style" color "#AAAAAA"

                                text ("Values") style "menu_text_style"
                                text "$" + str("%.2f" % mc.business.get_aspect_price("Mental")) style "menu_text_style"
                                text "$" + str("%.2f" % mc.business.get_aspect_price("Physical")) style "menu_text_style"
                                text "$" + str("%.2f" % mc.business.get_aspect_price("Sexual")) style "menu_text_style"
                                text "$" + str("%.2f" % mc.business.get_aspect_price("Medical")) style "menu_text_style"
                                text "-$" + str("%.2f" % -mc.business.get_aspect_price("Flaw")) style "menu_text_style"

                                text ("Desire") style "menu_text_style"
                                text str("%.0f" % (200*mc.business.get_aspect_percent("Mental"))) + "%" style "menu_text_style"
                                text str("%.0f" % (200*mc.business.get_aspect_percent("Physical"))) + "%" style "menu_text_style"
                                text str("%.0f" % (200*mc.business.get_aspect_percent("Sexual"))) + "%" style "menu_text_style"
                                text str("%.0f" % (200*mc.business.get_aspect_percent("Medical"))) + "%" style "menu_text_style"
                                text str("-%.0f" % (200*mc.business.get_aspect_percent("Flaw"))) + "%" style "menu_text_style"

                frame:
                    background "#1a45a1aa"
                    xsize 800 ysize 550
                    vbox:
                        ysize 400
                        text "Active Contracts (" + str(len(mc.business.active_contracts)) + "/" + str(mc.business.max_active_contracts) + " Max)" style "menu_text_title_style"
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            vbox:
                                spacing 20
                                xsize 800
                                for contract in mc.business.active_contracts:
                                    use contract_select_button(contract):
                                        textbutton "Add Serum":
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Show("serum_trade_ui", None, mc.business.inventory, contract.inventory, name_1 = "Stockpile", name_2 = contract.name, trade_requirement = contract.check_serum, hide_instead = True, inventory_2_max = contract.amount_desired)

                                        textbutton "Abandon": #TODO: This should probably require a double click or something.
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Function(mc.business.abandon_contract, contract)

                                        textbutton "Complete":
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Function(mc.business.complete_contract, contract)
                                            sensitive contract.can_finish_contract()


                    textbutton "New Contracts: " + str(len(mc.business.offered_contracts)) + " Available":
                        style "textbutton_style"
                        text_style "textbutton_text_style"
                        yanchor 1.0
                        yalign 1.0
                        xalign 0.5
                        ysize 40
                        action Show("contract_select")


                    #TODO: Holds information about current contracts and lets you transfer serum into and out of them


        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action Return()
            textbutton "Return" align [0.5,0.5] style "return_button_style" text_style "return_button_style"

    screen serum_design_menu_item(the_design, given_x_size = 500, given_y_size = 64, name_addition = ""):
        frame:
            background None

            xsize given_x_size
            ysize given_y_size
            padding (0,0)
            margin (0,0)
            button:
                style "textbutton_style"
                xfill True
                yfill True
                action SetScreenVariable("selected_serum", the_design)
                sensitive True
                hovered [SetScreenVariable("selected_serum", None), Show("serum_tooltip", None, the_design, given_anchor = (1.0,0.0), given_align = (0.95,0.05))]
                unhovered Hide("serum_tooltip")

            vbox:
                yanchor 0.5
                yalign 0.5
                xalign 1.0
                xfill True
                yfill True
                text the_design.name + name_addition style "textbutton_text_style" xoffset 16 yoffset 10
                use aspect_grid(the_design, given_xalign = 0.03, given_xanchor = 0.0)
