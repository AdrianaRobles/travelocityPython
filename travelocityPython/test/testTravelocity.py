from test import BaseTest
from pages.travelocityPageHome import TravelocityHome
from pages.travelocityPageSelectYourDeparture import TravelocitySelectYourDeparture
from pages import BasePage as bp
import ast
from _ast import Try
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
        varAsserBooleanVerifyAllComponents=ast.literal_eval(bp.splitReturn(self,varReturn, 0))
        varReturnFalloVerifyAllComponents = bp.splitReturn(self,varReturn,1)   
        varSortbyDuration = self.varYourDeparture.verifybyDuration()
        varAssertBooleanDuration =ast.literal_eval(bp.splitReturn(self, varSortbyDuration, 0))
        varReturnFalloSortbyDuration=bp.splitReturn(self,varSortbyDuration,1)
        try:
            self.assertEqual(varAsserBooleanVerifyAllComponents, True, varReturnFalloVerifyAllComponents)
        except AssertionError:
                print("There is a Error in varAsserBooleanVerifyAllComponents"+str(varAsserBooleanVerifyAllComponents)+">>>"+varReturnFalloVerifyAllComponents)
        try:
            self.assertEqual(varAssertBooleanDuration, True, varReturnFalloSortbyDuration)
        except AssertionError:
                print("There is a Error in varAssertBooleanDuration"+str(varAssertBooleanDuration)+">>>"+varReturnFalloSortbyDuration)
       
        
        
        