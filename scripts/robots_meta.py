"""Small HTML robots-meta parser shared by deployment checks and regression tests."""
from html.parser import HTMLParser


class RobotsMetaParser(HTMLParser):
    """Detect a robots meta directive that excludes a page from indexing."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "meta":
            return
        values = {key.lower(): (value or "") for key, value in attrs if key}
        if values.get("name", "").strip().lower() == "robots":
            directives = {
                part.strip().lower()
                for part in values.get("content", "").split(",")
            }
            if "noindex" in directives or "none" in directives:
                self.noindex = True
