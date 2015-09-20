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


import os
import requests
import json
import codecs
import shutil
import settings
import glob


def make_js():
    from textwrap import dedent

    def indent(lines, amount, ch=' '):
        padding = amount * ch
        return padding + ('\n' + padding).join(lines.split('\n'))

    src = {}

    for path in glob.glob("articles/*/article.html"):
        src[path.split("/")[1]] = path

    # Creates the src file
    js = u"""\
    ;(function(undefined) {
        'use strict';

        var src = %s

        var docs = new HTML2print.Docs;
        docs.initialize(src);
    })();
    """ % indent(json.dumps(src, sort_keys=True, indent=4), 8)
    js = dedent(js)

    return js

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    js = make_js()
    args.outfile.write(js.encode("utf-8"))
