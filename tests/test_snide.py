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
        self.slide_text = '# first slide\n\n- and\n- then\n- this'
        self.expected_slide = Slide('# first slide\n\n- and\n- then\n- this')

        self.notes_slide_text = ('# first point\n'
                                 '# second point\n'
                                 '???\n'
                                 '# some notes\n').strip()

        self.config_slide_text = ('class:inverse\n'
                                  'transition:down\n'
                                  '# first point\n'
                                  '# second point\n').strip()

    def test_slide(self):
        self.assertEquals(
            self.expected_slide.json,
            Slide(self.slide_text).json
        )

    def test_slide_config(self):
        self.assertEquals(
            {'class': 'inverse', 'transition': 'down'},
            Slide(self.config_slide_text).config,
        )

    def test_slide_config_removed_from_text(self):
        self.assertEquals(
            ['# first point', '# second point'],
            Slide(self.config_slide_text).text,
        )

    def test_slide_notes(self):
        self.assertEquals(
            ['# some notes'],
            Slide(self.notes_slide_text).notes,
        )
