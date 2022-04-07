init -2 python:
    # NOTE: this works different in different versions of Renpy...don't use for now.

    class UpdateWidgetText(ui.Action):
        def __init__(self, screenName, widgetId, value=None):
            self.screenName = screenName
            self.widgetId = widgetId
            self.value = value

        def __call__(self):
            widget = renpy.get_widget(self.screenName, self.widgetId)
            if widget:
                set_method = getattr(widget, "set_text", None)
                if not set_method:
                    set_method = getattr(widget.get_child(), "set_text", None)

                if set_method and callable(set_method):
                    set_method(self.value)
