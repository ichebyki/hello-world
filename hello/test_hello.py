"""sample test"""
import unittest

from hello import hello,hello2


class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello('world'), 'hello world')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'hello world')

    def test_world_ru(self):
        """sample test with ru text"""
        self.assertEqual(hello2(u'мир'), u'привет мир')



