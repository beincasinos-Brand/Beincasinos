#!/usr/bin/env python3
"""Regression tests for robots meta directives used by sitemap validation."""
import unittest
from scripts.robots_meta import InlineEventHandlerParser, RobotsMetaParser


def parse(html):
    parser = RobotsMetaParser()
    parser.feed(html)
    return parser.noindex


class InlineEventHandlerParserTests(unittest.TestCase):
    def test_inline_click_handler_is_detected(self):
        parser = InlineEventHandlerParser()
        parser.feed('<button onclick="run()">Go</button>')
        self.assertEqual(parser.handlers, [("button", "onclick")])

    def test_mixed_case_handler_and_multiple_elements_are_detected(self):
        parser = InlineEventHandlerParser()
        parser.feed('<IMG ONERROR="bad()"><a onmouseover="bad()">link</a>')
        self.assertEqual(parser.handlers, [("img", "onerror"), ("a", "onmouseover")])

    def test_non_event_attributes_are_allowed(self):
        parser = InlineEventHandlerParser()
        parser.feed('<button class="onclick" data-onclick="x" title="ok">Go</button>')
        self.assertEqual(parser.handlers, [])


class RobotsMetaParserTests(unittest.TestCase):
    def test_noindex_follow_is_detected(self):
        self.assertTrue(parse('<meta name="robots" content="noindex,follow">'))

    def test_none_is_detected(self):
        self.assertTrue(parse('<META NAME="ROBOTS" CONTENT="none">'))

    def test_directive_order_and_whitespace_are_supported(self):
        self.assertTrue(parse('<meta content="index, noindex" name="robots">'))

    def test_googlebot_specific_noindex_is_detected(self):
        self.assertTrue(parse('<meta name="googlebot" content="noindex">'))

    def test_googlebot_variant_noindex_is_detected(self):
        self.assertTrue(parse('<meta name="googlebot-news" content="none">'))

    def test_index_follow_remains_indexable(self):
        self.assertFalse(parse('<meta name="robots" content="index,follow">'))

    def test_other_meta_tags_do_not_trigger_noindex(self):
        self.assertFalse(parse('<meta name="description" content="noindex is a word">'))

    def test_unrelated_meta_tag_is_ignored(self):
        self.assertFalse(parse('<meta name="twitter:card" content="noindex">'))

    def test_absent_robots_tag_is_indexable_by_default(self):
        self.assertFalse(parse('<html><head><title>Test</title></head></html>'))

    def test_multiple_meta_tags_only_crawler_noindex_excludes(self):
        html = (
            '<meta name="description" content="noindex is only explanatory text">'
            '<meta name="twitter:card" content="noindex">'
            '<meta name="bingbot" content="index, noindex, max-image-preview:large">'
        )
        self.assertTrue(parse(html))

    def test_noindexing_word_is_not_noindex_directive(self):
        self.assertFalse(parse('<meta name="robots" content="noindexing,follow">'))

    def test_noindex_in_html_comment_is_ignored(self):
        self.assertFalse(parse('<!-- <meta name="robots" content="noindex"> -->'))

    def test_noindex_with_extra_whitespace_and_mixed_case_is_detected(self):
        self.assertTrue(parse('<meta NAME="GoogleBot-News" CONTENT=" INDEX ,  NOINDEX , max-snippet:0 ">'))

    def test_meta_with_name_and_content_attributes_in_any_order(self):
        self.assertTrue(parse('<meta content="none" charset="utf-8" name="robots">'))


if __name__ == "__main__":
    unittest.main(verbosity=2)
