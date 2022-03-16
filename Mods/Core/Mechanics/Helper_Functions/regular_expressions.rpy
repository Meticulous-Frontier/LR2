init -2 python:
    import re

    def remove_display_tags(message):
        return re.sub(r"([{[[].*?[]}])", u"", message)

    def replace_nth_occurrence(source, find, replacement, nth):
        where = [m.start() for m in re.finditer(find, source)][nth-1]
        before = source[:where]
        after = source[where:]
        after = after.replace(find, replacement, 1)
        return before + after
