SHELL := /usr/bin/env bash

LESS_FILES = $(shell find sample-content/markdown -type f -name '*.md')
ARTICLES_FILES = $(shell find articles -type f -name '*.html')

all: build/css/main.css js/src.js stories

build/css/main.css : $(LESS_FILE)
	mkdir -p $(@D)
	lessc css/main.less --clean-css $(@)

js/src.js : $(ARTICLES_FILE)
	mkdir -p $(@D)
	python2 bin/makesrc.py $(@)

.PHONY: stories
stories:
	mkdir -p $(@)
	python2 bin/pullstories.py $(@)

.PHONY: clean
clean:
	rm -fr stories
	rm -fr build
	rm js/src.js
