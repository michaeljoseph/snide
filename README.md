# snide

[![Build Status](https://secure.travis-ci.org/michaeljoseph/snide.png)](http://travis-ci.org/michaeljoseph/snide)
[![Stories in Ready](https://badge.waffle.io/michaeljoseph/snide.png?label=ready)](https://waffle.io/michaeljoseph/snide) [![pypi version](https://badge.fury.io/py/snide.png)](http://badge.fury.io/py/snide)
[![# of downloads](https://pypip.in/d/snide/badge.png)](https://crate.io/packages/snide?version=latest)
[![code coverage](https://coveralls.io/repos/michaeljoseph/snide/badge.png?branch=master)](https://coveralls.io/r/michaeljoseph/snide?branch=master)

## Overview

Snide: a remark.js parser in python

* A parser that recognises a slightly modified Markdown slide format parser (todo: ref remarkjs)
    * `---` is a slide boundary
    * arbitrary `key: value` slide configuration
    * `???` for speaker notes

## Usage

Install `snide`:

    pip install snide

Use snide in your code to parse a slide markup document:

```python
from snide.models import Deck

deck = Deck(
    'Application To Platform',
    open('application-to-platform.md').read()
)
print(deck.json)
print(deck.title)

for slide in deck.slides:
    print(slide.html)
```

### CLI

TODO: Minimal cli to parse and display deck statistics and meta information

    snide my_slides.md

## Documentation

[API Documentation](http://snide.rtfd.org)

## Testing

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    nosetests

Lint the project with:

    flake8 changes tests

## API documentation

Generate the documentation with:

    cd docs && PYTHONPATH=.. make singlehtml

To monitor changes to Python files and execute flake8 and nosetests
automatically, execute the following from the root project directory:

    stir
