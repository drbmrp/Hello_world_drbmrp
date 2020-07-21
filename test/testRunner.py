import sys
sys.path.append('..')

import unittest
from TemplateGitHub.TemplateGitHub import TemplateGitHub as tg

class DogTestCase(unittest.TestCase):
    def setUp(self):
        self.initialX = 5
        self.tg = tg(self.initialX)
        

    def test_bark(self):
        self.tg.Bark()
        self.assertEqual(self.tg.state, 'barking',
                         'The dog should be barking')

    def test_calm_down(self):
        self.tg.CalmDown()
        self.assertEqual(self.tg.state, 'calmed',
                         'The dog should be calmed')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DogTestCase('test_bark'))
    suite.addTest(DogTestCase('test_calm_down'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
