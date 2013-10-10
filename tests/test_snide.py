from . import BaseTestCase

from snide import snide


class TestSnide(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            snide(),
        )
