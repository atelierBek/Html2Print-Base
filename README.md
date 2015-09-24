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
$ html2text text-article.html > text-article.md
add makers to your article.md
markdown_py -x extra text-article.md >| text-article.html

copy paste it at the bottom of the of the articles/article.html in between and in the django (?)
    <div id="stories">
        <article id="flow-article" class="type of article like enquete or rubrique...">
			    <header>
					<h1>titre article</h1>
					<p class="authors">auteur</p>
			    </header>
			here! rest-of-the-text-article.html
        </article>
    </div>

in the gabary, on the first page, in the body the first bloc should be for the h1 (header) and therefore have the class="flow-title"
ex
   <div class="body">
       <div class="bloc x1 y0 w8 h3 flow-title"></div>
       <div class="bloc x1 y5 w8 h5 flow-quand-jetais-flamand"></div>
   </div>


