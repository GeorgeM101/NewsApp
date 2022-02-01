import unittest
from app.models import Sources



class SourceTest(unittest.TestCase):
    """
    Test class to test the behaviour of the news class
    """

    def setUp(self):
        """
        """
        self.new_source = Sources('Test id','Test name','Test description','Test author', 'Test publishedAt', 'Test title')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources)) 

