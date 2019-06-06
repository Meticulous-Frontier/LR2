# init 2:
#     screen trait_tooltip(the_trait,given_xpos=712,given_ypos=580):
#
#         frame:
#             background "#666666"
#
#             xpos given_xpos
#             ypos given_ypos
#             ysize 260
#             xsize 550
#             viewport:
#                 draggable True
#                 xsize 550
#                 ysize 250
#                 mousewheel "vertical"
#                 xalign 0.5
#                 vbox:
#
#                     textbutton "[the_trait.name]":
#                         style "textbutton_style"
#                         text_style "serum_text_style"
#                         xalign 0.5
#                         xsize 500
#                         action NullAction()
#
#                     hbox:
#
#                         vbox:
#
#                             textbutton "{color=#98fb98}[the_trait.positive_slug]{/color}":
#                                 style "textbutton_style"
#                                 text_style "serum_text_style"
#                                 xalign 0.5
#
#                                 xsize 225
#
#                                 action NullAction()
#
#                         vbox:
#
#                             textbutton "{color=#cd5c5c}[the_trait.negative_slug]{/color}":
#                                 style "textbutton_style"
#                                 text_style "serum_text_style"
#                                 xalign 0.5
#
#                                 xsize 225
#
#                                 action NullAction()
#
#                     textbutton "[the_trait.desc]":
#                         style "textbutton_style"
#                         text_style "serum_text_style"
#                         xalign 0.5
#
#                         xsize 500
#
#                         action NullAction()
