from test import BaseTest
from pages.travelocityPageHome import TravelocityHome
from pages.travelocityPageSelectYourDeparture import TravelocitySelectYourDeparture
import ast
'''
Created on 15/11/2018

@author: aldo.villalba
'''
class TestTravelocity(BaseTest):
    
    def test_selectDataPicker(self):
        self.varPage = TravelocityHome(self.driver)
        self.varYourDeparture=self.varPage.findFly()
        varReturn=self.varYourDeparture.verifyAllComponets()
        varArrayReturn=varReturn.split("-")
        varAsserBoolean=ast.literal_eval(varArrayReturn[0])
        varReturnFallo = varArrayReturn[1]
        print(varReturnFallo)
        print(varAsserBoolean)
        assert varAsserBoolean == True
        
        
        
        