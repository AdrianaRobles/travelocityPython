from test import BaseTest
from pages.travelocityPageHome import TravelocityHome
'''
Created on 15/11/2018

@author: aldo.villalba
'''
class TestTravelocity(BaseTest):
    
    def test_selectDataPicker(self):
        self.varPage = TravelocityHome(self.driver)
        self.varPage.findFly()
    
   
        
        
        