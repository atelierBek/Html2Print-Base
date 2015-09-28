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


def get_client():
    login_url = 'https://medor.coop/fr/admin/login/'
    client = requests.session()
    # Retrieve the CSRF token first
    client.get(login_url)  # sets cookie
    csrftoken = client.cookies['csrftoken']
    login_data = dict(username=settings.USER, password=settings.PASS, csrfmiddlewaretoken=csrftoken, next='/')
    resp = client.post(login_url, data=login_data, headers=dict(Referer=login_url))

    if resp.status_code != 200:
        print("It didn't work")
        import sys
        sys.exit()

    return client


def other():
    #try:
        #shutil.rmtree('articles')
        ##shutil.rmtree('js')
    #except FileNotFoundError:
        #pass


    if not os.path.isdir("articles"):
        os.mkdir('articles')

    client = get_client()

    hostname = 'https://medor.coop'
    path = "/fr/publish/api/article-membership/?issue__id=1"
    url = hostname + path

    request = client.get(url)

    for membership in request.json():
        order = membership['order']
        slug = membership['article']['slug']
        url = membership['article']['url']

        name = '%02d_%s' % (order, slug)
        os.mkdir('articles/%s' % name)

        # Gets the template
        request = client.get(hostname + "/fr/publish/%s.tpl" % membership['id'])
        f = codecs.open("articles/%s/article.html" % name, "w", "utf-8")
        f.write(request.text)
        f.close()

        # Gets the css
        os.mkdir('articles/%s/css' % name)
        request = client.get(hostname + "/fr/publish/%s.css" % membership['id'])
        f = codecs.open("articles/%s/css/generated.css" % name, "w", "utf-8")
        f.write(request.text)
        f.close()

        # Creates the style file
        f = codecs.open("articles/%s/css/styles.css" % name, "w", "utf-8")
        f.write("/* Styles for %s */" % name)
        f.close()


def make_js():
    from textwrap import dedent


    def indent(lines, amount, ch=' '):
        padding = amount * ch
        return padding + ('\n' + padding).join(lines.split('\n'))

    client = get_client()
    hostname = 'https://medor.coop'
    path = "/fr/publish/api/article-membership/?issue__id=1"
    url = hostname + path

    request = client.get(url)
    src = {}

    for membership in request.json():
        order = membership['order']
        slug = membership['article']['slug']

        name = '%02d_%s' % (order, slug)
        src[name] = 'articles/%s/article.html' % name

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

    if not os.path.isdir("js"):
        os.mkdir('js')

    f = codecs.open("js/src.js", "w", "utf-8")
    f.write(js)
    f.close()


def fetch_stories():
    client = get_client()
    hostname = 'https://medor.coop'
    path = "/fr/publish/api/article-membership/?issue__id=1"
    url = hostname + path

    request = client.get(url)

    os.mkdir('stories')

    for membership in request.json():
        order = membership['order']
        slug = membership['article']['slug']
        url = membership['article']['url']

        name = '%02d_%s' % (order, slug)

        # Gets the template
        request = client.get(hostname + "/fr/publish/%s.html" % membership['id'])
        f = codecs.open("stories/%s.html" % name, "w", "utf-8")
        f.write(request.text)
        f.close()


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('subcommand')
    args = parser.parse_args()

    if args.subcommand == "make_js":
        make_js()
    elif args.subcommand == "fetch_stories":
        fetch_stories()

    sys.exit()
