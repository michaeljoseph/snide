import markdown2


class Deck(object):

    def __init__(self, title, text):
        self.slides = []
        self.title = title
        self.text = text
        print(text.split('---'))
        for slide in text.split('---'):
            self.slides.append(Slide(slide))

    @property
    def json(self):
        return {
            'title': self.title,
            'slides': [slide.json for slide in self.slides],
        }


class Slide(object):

    def __init__(self, text):
        self.markdown = text
        self.config = self.parse_config(text)

    @property
    def html(self):
        return markdown2.markdown(self.markdown)

    def parse_config(self, slide):
        # re of lines: key:value, key=value
        return {

        }

    @property
    def json(self):
        return {
            'text': self.markdown,
            'html': self.html,
            'config': self.config,
        }

