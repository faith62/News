import unittest
from app.models import New

class NewTest(unittest.TestCase):
   
    '''
    Test Class to test the behaviour of the New class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_new = New("cnn","Anne Tyler", "Videos show someone tackling Chappelle at the Netflix Is A Joke Festival at the Hollywood Bowl.","https://www.bbc.co.uk/news/entertainment","https://ichef.bbci.co.uk/news/1024/branded_news/","2022-05-04","Dave Chappelle was performing at the Netflix Is A Joke Festival")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_new,New))


if __name__ == '__main__':
    unittest.main()