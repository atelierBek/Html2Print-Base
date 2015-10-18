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
from copy import deepcopy


def valid_xml_char_ordinal(c):
    codepoint = ord(c)
    # conditions ordered by presumed frequency
    return (
        0x20 <= codepoint <= 0xD7FF or
        codepoint in (0x9, 0xA, 0xD) or
        0xE000 <= codepoint <= 0xFFFD or
        0x10000 <= codepoint <= 0x10FFFF
        )


import re, htmlentitydefs

##
# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.

def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


def inline_footnotes(html):
    html = ''.join(c for c in html if valid_xml_char_ordinal(c))

    parser = html5lib.html5parser.HTMLParser(tree=html5lib.getTreeBuilder("lxml"), namespaceHTMLElements=False)
    fragments = parser.parseFragment(html)

    tree = etree.Element("div")
    for f in fragments:
        tree.append(f)

    expression = GenericTranslator().css_to_xpath('a[name$="anc"]')

    for elt in tree.xpath(expression):
        target = elt.attrib['name']
        new_expr = GenericTranslator().css_to_xpath('a[href="#%s"]' % target)
        try:
            fn = tree.xpath(new_expr)[0]
            parent = fn.getparent()
            parent.tag = "span"
            parent.attrib['class'] = "inline-fn"
            elt.addnext(parent)
        except IndexError:
            print("*** Could not get the corresponding footnote""")

    expression = GenericTranslator().css_to_xpath('ol[class="footnotes"]')
    for elt in tree.xpath(expression):
        elt.getparent().remove(elt)

    fragments = [x for x in list(tree)]
    output = u'\n'.join(lxml.html.tostring(x, pretty_print=True) for x in fragments)

    return unescape(output)



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
