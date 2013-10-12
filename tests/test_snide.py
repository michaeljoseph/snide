from . import BaseTestCase

from snide import Deck, Slide


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
        self.slide_text = (
            '# first slide\n'
            '\n'
            '- and\n'
            '- then\n'
            '- this'
        )
        self.slide = Slide(self.slide_text)

        self.config_slide_text = (
            'class:inverse\n'
            'transition:down\n'
            '# first point\n'
            '# second point\n'
        ).strip()
        self.config_slide = Slide(self.config_slide_text)

        self.notes_slide_text = (
            '# first point\n'
            '# second point\n'
            '???\n'
            '# some notes\n'
        ).strip()
        self.notes_slide = Slide(self.notes_slide_text)

        self.complete_slide_text = (
            'class:inverse\n'
            'transition:down\n'
            '# first point\n'
            '# second point\n'
            '???\n'
            '# some notes\n'
        ).strip()
        self.complete_slide = Slide(self.complete_slide_text)

    def test_slide(self):
        self.assertEquals(
            self.slide.json,
            Slide(self.slide_text).json
        )

    def test_slide_config(self):
        self.assertEquals(
            {'class': 'inverse', 'transition': 'down'},
            self.config_slide.config,
        )

    def test_slide_config_removed_from_text(self):
        self.assertEquals(
            ['# first point', '# second point'],
            self.config_slide.text,
        )

    def test_slide_notes(self):
        self.assertEquals(
            ['# some notes'],
            self.notes_slide.notes,
        )
        self.assertEquals(
            ['# first point', '# second point'],
            self.notes_slide.slide,
        )

    def test_slide_note_marker_removed(self):
        self.assertTrue('???' not in self.notes_slide.config)
        self.assertTrue('???' not in self.notes_slide.slide)
        self.assertTrue('???' not in self.notes_slide.notes)

    def test_slide_notes_html(self):
        self.assertEquals(
            '<h1>some notes</h1>\n',
            self.notes_slide.notes_html,
        )

    def test_complete_slide(self):
        self.assertEquals(
            {'class': 'inverse', 'transition': 'down'},
            self.complete_slide.config,
        )

        self.assertEquals(
            ['# first point', '# second point'],
            self.complete_slide.slide,
        )

        self.assertEquals(
            ['# some notes'],
            self.complete_slide.notes
        )
