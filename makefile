SHELL := /usr/bin/env bash

ARTICLES_FILES = $(shell find articles -type f -name '*.html')

STORIES_FILES = $(shell find stories/ -type f -name '*.html')
INLINED_STORIES_FILES = $(patsubst stories/%.html, stories2/%.html, $(STORIES_FILES))

LESS_FILES = $(shell find articles/ -type f -name '*.less')
CSS_FILES = $(patsubst %.less, %.css, $(LESS_FILES))

all: js/src.js stories
inlined_stories: $(INLINED_STORIES_FILES)
css: $(CSS_FILES)


articles/%.css : articles/%.less
	 lessc $< > $@

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
