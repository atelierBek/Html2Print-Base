Quick start
===========

Pre-requisites
--------------

Clone and enter the repository

    git clone git@git.constantvzw.org:medor.numero1.git
    cd medor.numero1

Make sure you have all the system-wide dependencies

    sudo apt-get update
    sudo apt-get install python-virtualenv
    sudo apt-get install npm
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

Using the layout generator
--------------------------

Starts the serveur if it isn't running already

    python2 -m SimpleHTTPServer

Visit the URL:

    http://localhost:8000/grid.html


keeping everything up-to-date
=============================

Updating the stories
--------------------

Enter the virtualenv if it is not yet the case

    source venv/bin/activate

Pull the stories in the stories directory

    make stories

Updating the table of contents
------------------------------

Enter the virtualenv if it is not yet the case

    source venv/bin/activate

Generate the table of contents for HTML2print to work

    make js/src.js


Cookbook
========

Converting from HTML to .docx
-----------------------------

    pandoc -f html -t docx -o destination.docx source.html

Adapt it to your needs if you need to work with other formats
