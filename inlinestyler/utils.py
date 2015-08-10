from lxml import etree
from inlinestyler.converter import Conversion

def inline_css(html_message, encoding="UTF-8", copy_style=False):
    """
    Inlines all CSS in an HTML string

    Given an HTML document with CSS declared in the HEAD, inlines it into the
    applicable elements. Used primarily in the preparation of styled emails.

    Arguments:
        html_message -- a string of HTML, including CSS
    """

    document = etree.HTML(html_message)
    converter = Conversion()
    converter.perform(document, html_message, '', encoding=encoding, copy_style=copy_style)
    return converter.convertedHTML
