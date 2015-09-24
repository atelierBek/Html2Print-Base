sudo apt-get install npm
sudo npm -global install bower
bower install

- - -

$ virtualenv --no-site-packages venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ cp bin/settings.example.py bin/settings.py
(venv)$ vim bin/settings.py

/* if you need to reload/update the articles html files, you'll have to erase your local artile folder before launching the makedocs.py → you should make a backup of you article folder if you did work in it before the following command
$ rm -fr articles js/src.js */

(venv)$ python bin/makedocs.py
(venv)$ python2 -m SimpleHTTPServer


once you have your article folder and your server runing don't forget to copy paste the good flow for each article
from generated.css to article.html 
for example

"flow-quand-jetais-flamand" from the generated.css will replace the class "recipient" in the body level



-----

html to md to md to html

export you .doc in html
then
$ html2text article.html > article.md
add makers to your article.md
markdown_py -x extra article.md >| article.html


