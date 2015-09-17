import os
import requests
import json
import codecs
import shutil
import settings

#try:
    #shutil.rmtree('articles')
    ##shutil.rmtree('js')
#except FileNotFoundError:
    #pass


def indent(lines, amount, ch=' '):
    padding = amount * ch
    return padding + ('\n' + padding).join(lines.split('\n'))


if not os.path.isdir("articles"):
    os.mkdir('articles')

hostname = 'https://medor.coop'
path = "/fr/publish/api/article-membership/?issue__id=1"
url = hostname + path

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


request = client.get(url)

src = {}

for membership in request.json():
    order = membership['order']
    slug = membership['article']['slug']
    url = membership['article']['url']

    name = '%02d_%s' % (order, slug)
    os.mkdir('articles/%s' % name)
    src[name] = 'articles/%s/article.html' % name

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



# Creates the src file
js = u"""\
(function(undefined) {
    'use strict';

    var src = %s

    var docs = new HTML2print.Docs;
    docs.initialize(src);
})();
""" % indent(json.dumps(src, sort_keys=True, indent=4), 4)

if not os.path.isdir("js"):
    os.mkdir('js')

f = codecs.open("js/src.js", "w", "utf-8")
f.write(js)
f.close()
