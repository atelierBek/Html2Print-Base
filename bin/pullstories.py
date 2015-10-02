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


# Pulls stories from our plateform
#
# Usage:
#
#     ./pullstories.py [where]


import requests
import codecs
import settings
import html5lib
from html5lib.filters import whitespace
from html5lib_typogrify.french.filters import hyphenate, medor



def get_client():
    login_url = 'https://medor.coop/fr/admin/login/'
    client = requests.session()
    # Retrieve the CSRF token first
    client.get(login_url)  # sets cookie
    csrftoken = client.cookies['csrftoken']
    login_data = dict(username=settings.USER, password=settings.PASS, csrfmiddlewaretoken=csrftoken, next='/')
    resp = client.post(login_url, data=login_data, headers=dict(Referer=login_url))

    if resp.status_code != 200:
        import sys
        sys.exit()

    return client


def pull_stories(where="stories"):
    client = get_client()

    hostname = 'https://medor.coop'
    path = "/fr/publish/api/article-membership/?issue__id=1"
    url = hostname + path

    request = client.get(url)

    for membership in request.json():
        order = membership['order']
        slug = membership['article']['slug']

        print("Pulling %s" % slug)

        name = '%02d_%s' % (order, slug)

        # Gets the story
        request = client.get(hostname + "/fr/publish/%s.html" % membership['id'])

        output = request.text

        # Using etree is important here because it /can't/ have adjacent text
        # nodes in its data model (thanks html5lib folks for the tip).
        # See <https://github.com/html5lib/html5lib-python/issues/208>
        dom = html5lib.parseFragment(output, treebuilder="etree")
        walker = html5lib.getTreeWalker("etree")

        stream = walker(dom)
        stream = whitespace.Filter(stream)
        stream = medor.Filter(stream)
        stream = hyphenate.Filter(stream, left=2, right=2)

        s = html5lib.serializer.HTMLSerializer(omit_optional_tags=False)

        output = s.render(stream)

        f = codecs.open("%s/%s.html" % (where, name), "w", "utf-8")
        f.write(output)
        f.close()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('where', default="stories")
    args = parser.parse_args()

    pull_stories(where=args.where)
