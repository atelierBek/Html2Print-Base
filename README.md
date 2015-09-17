sudo apt-get install npm
sudo npm -global install bower
bower install

- - -

$ virtualenv --no-site-packages venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ cp bin/settings.example.py bin/settings.py
(venv)$ vim bin/settings.py
(venv)$ python bin/makedocs.py
(venv)$ python2 -m SimpleHTTPServer
