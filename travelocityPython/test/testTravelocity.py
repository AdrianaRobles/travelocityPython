from test import BaseTest
from pages.travelocityPageHome import TravelocityHome
from pages import BasePage as bp
import ast
'''
Created on 15/11/2018
Class to do all test on Travelocity page
@author: aldo.villalba
'''
class TestTravelocity(BaseTest):
    
    def test_selectDataPicker(self):
        self.varPage         = TravelocityHome(self.driver)
        self.varYourDeparture = self.varPage.findFly()
        '''
        This part of code does the steps to verify all components inside of the page
        '''
        varReturn=self.varYourDeparture.verifyAllComponents()
        varAsserBooleanVerifyAllComponents=ast.literal_eval(bp.splitReturn(self,varReturn, 0))
        varReturnFalloVerifyAllComponents = bp.splitReturn(self,varReturn,1)  
        
        '''
        This part of code does the steps to verify all components inside of the page
        ''' 
        varSortbyDuration = self.varYourDeparture.verifybyDuration()
        varAssertBooleanDuration =ast.literal_eval(bp.splitReturn(self, varSortbyDuration, 0))
        varReturnFalloSortbyDuration=bp.splitReturn(self,varSortbyDuration,1)
        
        '''
        This part of code does the steps to verify all details of Trip
        '''
        self.varVerifySummaryComponents = self.varYourDeparture.selectFirstResult()
        varReturnVerifySummaryComponents = self.varVerifySummaryComponents.verifyTripComponents()
        varAssertBooleanSummaryComponents = ast.literal_eval(bp.splitReturn(self, varReturnVerifySummaryComponents, 0))
        varReturnFalloSumaryComponents = bp.splitReturn(self,varReturnVerifySummaryComponents,1)
        '''
        This part of code does the steps to verify all details of who s traveling
        '''
        self.varWhoStraveling =  self.varVerifySummaryComponents.sendToWhoSTraveling()
        varReturnWhoSTraveling=self.varWhoStraveling.verifyPageWhoStraveling()
        varAssertBooleanWhoSTraveling =ast.literal_eval(bp.splitReturn(self,varReturnWhoSTraveling,0))
        varReturnFalloWhoSTraveling = bp.splitReturn(self, varReturnWhoSTraveling, 1)
        try:
            self.assertEqual(varAsserBooleanVerifyAllComponents, True, varReturnFalloVerifyAllComponents)
        except AssertionError:
                print("There is a Error in varAsserBooleanVerifyAllComponents "+str(varAsserBooleanVerifyAllComponents)+">>>"+varReturnFalloVerifyAllComponents)
        try:
            self.assertEqual(varAssertBooleanDuration, True, varReturnFalloSortbyDuration)
        except AssertionError:
                print("There is a Error in varAssertBooleanDuration "+str(varAssertBooleanDuration)+">>>"+varReturnFalloSortbyDuration)
        try:
            self.assertEqual(varAssertBooleanSummaryComponents,True,varReturnFalloSumaryComponents)
        except AssertionError:
                print("There is a Error in varVerifySummaryComponents "+str(varAssertBooleanSummaryComponents)+">>>"+varReturnFalloSumaryComponents)
        try:
            self.assertEqual(varAssertBooleanWhoSTraveling,True,varReturnFalloWhoSTraveling)
        except AssertionError:
                print("There is a Error in Who S traveling "+str(varAssertBooleanWhoSTraveling)+">>>"+varReturnFalloWhoSTraveling)
        
        