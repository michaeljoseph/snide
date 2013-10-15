import re

import markdown2


class Deck(object):

    def __init__(self, title, text, presentation_type=None):
        self.slides = []
        self.title = title
        self.text = text
        self.presentation_type = presentation_type

        for slide in text.split('---'):
            self.slides.append(Slide(slide.lstrip()))

    @property
    def json(self):
        return {
            'title': self.title,
            'slides': [slide.json for slide in self.slides],
        }


class Slide(object):
    text = []
    config = {}
    slide = []
    notes = []

    def __init__(self, text):
        self.text = text.split('\n')
        self.parse_slide()

    @property
    def html(self):
        if self.slide:
            return markdown2.markdown('\n'.join(self.slide))
        else:
            return self.slide

    @property
    def notes_html(self):
        if self.notes:
            return markdown2.markdown('\n'.join(self.notes))
        else:
            return self.notes

    def parse_slide(self):
        # config
        pattern = re.compile("([a-z]+)\s*:\s*([a-z]+)")
        text = []
        for line in self.text:
            if pattern.match(line):
                self.config.update(
                    dict(pattern.findall(line))
                )
            else:
                text.append(line)

        # slide and notes
        self.text = text
        if self.text.count('???'):
            position = self.text.index('???')
            self.slide, self.notes = (
                self.text[0:position],
                self.text[position + 1:len(self.text)]
            )
        else:
            self.slide = self.text

    @property
    def json(self):
        return {
            'config': self.config,
            'text': self.text,
            'slide': self.slide,
            'html': self.html,
            'notes': self.notes,
            'notes_html': self.notes_html,
        }
