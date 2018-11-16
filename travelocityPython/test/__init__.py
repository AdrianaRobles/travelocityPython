import unittest
from driverTravelocity import WebDriver

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver("Chrome").getDriver()
    
    def tearDown(self):
        self.driver.close()
        
    if __name__ == "__main__":
        unittest.main()

    

