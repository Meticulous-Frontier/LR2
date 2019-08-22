init -2 python:
    import re

    def remove_display_tags(message):
        return re.sub(r"({.*?})", u"", message)