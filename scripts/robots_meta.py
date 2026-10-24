"""Small HTML robots-meta parser shared by deployment checks and regression tests."""
from html.parser import HTMLParser


_CRAWLER_META_NAMES = {
    "robots",
    "bingbot",
    "slurp",
    "duckduckbot",
    "baiduspider",
    "yandex",
}


class RobotsMetaParser(HTMLParser):
    """Detect noindex directives that exclude a page from a search engine."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "meta":
            return
        values = {key.lower(): (value or "") for key, value in attrs if key}
        name = values.get("name", "").strip().lower()
        if not (name in _CRAWLER_META_NAMES or name.startswith("googlebot")):
            return
        directives = {
            part.strip().lower()
            for part in values.get("content", "").split(",")
        }
        if "noindex" in directives or "none" in directives:
            self.noindex = True

class InlineEventHandlerParser(HTMLParser):
    """Collect inline event attributes that violate the same-origin-only CSP."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.handlers = []

    def handle_starttag(self, tag, attrs):
        for attribute, _value in attrs:
            if attribute and attribute.lower().startswith("on"):
                self.handlers.append((tag.lower(), attribute.lower()))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
