Quick start
===========
Html2Print is a method created by [Open Source Publishing](http://osp.kitchen/tools/html2print/)

Pre-requisites
--------------

Make sure you have all the system-wide dependencies

    sudo apt-get update
    sudo apt-get install python-dev
    sudo apt-get install libffi-dev
    sudo apt-get install python-virtualenv
    sudo apt-get install npm
    sudo apt-get install nodejs-legacy
    sudo npm -global install bower


Install the js and css dependencies (it will create a "vendors" directory)

    bower install

Install the python dependencies

    virtualenv --no-site-packages venv
    source venv/bin/activate
    pip install -r requirements.txt

Copy the exemple settings file and set the credentials for medor.coop. They will
be used to fetch the articles from the plateform

    cp bin/settings.example.py bin/settings.py
    nano bin/settings.py

Pull the stories in the stories directory

    make stories

Generate the table of contents for HTML2print to work

    make js/src.js


Using HTML2print
----------------

Starts the serveur

    python2 -m SimpleHTTPServer

Visit the URL:

    http://localhost:8000

