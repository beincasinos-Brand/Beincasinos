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
