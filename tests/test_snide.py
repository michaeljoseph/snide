from . import BaseTestCase

from snide.models import Deck, Slide 


class TestDeck(BaseTestCase):

    def setUp(self):
        self.deck_text = ('# first slide'
                          '---'
                          '# second slide').strip()

        self.expected_deck = Deck('foo', self.deck_text)
        self.expected_deck.slides = [
            Slide('# first slide'),
            Slide('# second slide')
        ]

    def test_deck(self):
        self.assertEquals(
            self.expected_deck.json,
            Deck('foo', self.deck_text).json
        )


class TestSlide(BaseTestCase):

    def setUp(self):
        self.expected_slide = Slide('# first slide\n\n- and\n- then\n- this')

    def test_slide(self):

        slide_text = '# first slide\n\n- and\n- then\n- this'
        self.assertEquals(
            self.expected_slide.json,
            Slide(self.slide_text).json
        )

        pass

    def test_slide_render(self):
        pass


