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


def main():
    #try:
        #shutil.rmtree('articles')
        ##shutil.rmtree('js')
    #except FileNotFoundError:
        #pass


    if not os.path.isdir("articles_new"):
        os.mkdir('articles_new')

    client = get_client()

    hostname = 'https://medor.coop'
    path = "/fr/publish/api/article-membership/?issue__id=1"
    url = hostname + path

    request = client.get(url)

    for membership in request.json():
        order = membership['order']
        slug = membership['article']['slug']
        url = membership['article']['url']

        name = slug
        os.mkdir('articles_new/%s' % name)

        # Gets the template
        request = client.get(hostname + "/fr/publish/%s.tpl" % membership['id'])
        f = codecs.open("articles_new/%s/article.html" % name, "w", "utf-8")
        f.write(request.text)
        f.close()

        # Gets the css
        os.mkdir('articles_new/%s/css' % name)
        request = client.get(hostname + "/fr/publish/%s.css" % membership['id'])
        f = codecs.open("articles_new/%s/css/generated.css" % name, "w", "utf-8")
        f.write(request.text)
        f.close()

        # Creates the style file
        f = codecs.open("articles_new/%s/css/styles.css" % name, "w", "utf-8")
        f.write("/* Styles for %s */" % name)
        f.close()


if __name__ == '__main__':
    import argparse
    import sys

    main()

    sys.exit()
