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
            self.expected_deck.to_json(),
            Deck('foo', self.deck_text).to_json()
        )


class TestSlide(BaseTestCase):

    def test_slide(self):
        pass

    def test_slide_parse(self):
        pass

    def test_slide_render(self):
        pass


