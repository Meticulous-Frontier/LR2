init -2 python:
    class UpdateWidgetText(ui.Action):
        def __init__(self, screenName, widgetId, value=None):
            self.screenName = screenName
            self.widgetId = widgetId
            self.value = value

        def __call__(self):
            widget = renpy.get_widget(self.screenName, self.widgetId)
            if widget:
                widget.set_text(self.value)
