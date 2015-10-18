SHELL := /usr/bin/env bash

LESS_FILES = $(shell find sample-content/markdown -type f -name '*.md')
ARTICLES_FILES = $(shell find articles -type f -name '*.html')

STORIES_FILES = $(shell find stories/ -type f -name '*.html')
INLINED_STORIES_FILES = $(patsubst stories/%.html, stories2/%.html, $(STORIES_FILES))

all: build/css/main.css js/src.js stories
inlined_stories: $(INLINED_STORIES_FILES)

build/css/main.css : $(LESS_FILE)
	mkdir -p $(@D)
	lessc css/main.less --clean-css $(@)

js/src.js : $(ARTICLES_FILE)
	mkdir -p $(@D)
	python2 bin/makesrc.py $(@)

stories2/%.html : stories/%.html
	mkdir -p $(@D)
	python bin/inline_footnotes.py $< $@

.PHONY: stories
stories:
	mkdir -p $(@)
	python2 bin/pullstories.py $(@)

.PHONY: clean
clean:
	rm -fr stories
	rm -fr build
	rm js/src.js
