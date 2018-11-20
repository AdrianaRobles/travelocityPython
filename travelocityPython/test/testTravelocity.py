from test import BaseTest
from pages.travelocityPageHome import TravelocityHome
from pages.travelocityPageSelectYourDeparture import TravelocitySelectYourDeparture
from pages import BasePage as bp
import ast
'''
Created on 15/11/2018
Class to do all test on Travelocity page
@author: aldo.villalba
'''
class TestTravelocity(BaseTest):
    
    def test_selectDataPicker(self):
        self.varPage = TravelocityHome(self.driver)
        self.varYourDeparture=self.varPage.findFly()
        varReturn=self.varYourDeparture.verifyAllComponents()
        varAsserBoolean=ast.literal_eval(bp.splitReturn(self,varReturn, 0))
        varReturnFallo = bp.splitReturn(self,varReturn,1)   
        assert varAsserBoolean == True,varReturnFallo
        
        
        
        
        
        