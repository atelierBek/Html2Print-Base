#! /usr/bin/env python2


# Copyright (C) 2015 Alexandre Leray

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Converts Markdown files to HTML
#
# Usage:
#
#     ./generate.py infile.md outfile.html



import lxml
import lxml.html
import lxml.etree as etree
import html5lib
from cssselect import GenericTranslator, SelectorError
import re


def valid_xml_char_ordinal(c):
    codepoint = ord(c)
    # conditions ordered by presumed frequency
    return (
        0x20 <= codepoint <= 0xD7FF or
        codepoint in (0x9, 0xA, 0xD) or
        0xE000 <= codepoint <= 0xFFFD or
        0x10000 <= codepoint <= 0x10FFFF
        )


def inline_footnotes(html):
    html = ''.join(c for c in html if valid_xml_char_ordinal(c))

    #tree = lxml.html.fragment_fromstring(html, create_parent=True)

    parser = html5lib.html5parser.HTMLParser(tree=html5lib.getTreeBuilder("lxml"), namespaceHTMLElements=False)
    fragments = parser.parseFragment(html)
    #fragments = html5lib.parseFragment(html, treebuilder="lxml", container='div')

    tree = etree.Element("root")
    for f in fragments:
        tree.append(f)

    expression = GenericTranslator().css_to_xpath('a[name$="anc"]')

    for elt in tree.xpath(expression):
        target = elt.attrib['name']
        new_expr = GenericTranslator().css_to_xpath('a[href="#%s"]' % target)
        fn = tree.xpath(new_expr)[0]
        parent = fn.getparent()
        parent.tag = "span"
        parent.attrib['class'] = "inline-fn"
        elt.addnext(parent)

    expression = GenericTranslator().css_to_xpath('ol[class="footnotes"]')
    for elt in tree.xpath(expression):
        elt.getparent().remove(elt)

    fragments = [i for i in list(tree)]
    import ipdb; ipdb.set_trace()

    walker = html5lib.getTreeWalker("lxml")
    stream = walker(fragments)

    s = html5lib.serializer.HTMLSerializer(omit_optional_tags=True, quote_attr_values=True)

    output = s.render(stream)
    #output = ""

    return output



if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    content = args.infile.read()
    try:
        unicode_content = content.decode("utf-8")
    except UnicodeDecodeError:
        unicode_content = content.decode("iso8559-1")

    html = inline_footnotes(unicode_content)

    args.outfile.write(html.encode("utf-8"))
