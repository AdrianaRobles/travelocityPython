from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages import BasePage
from pages.travelocityPageWhoSTraveling import TravelocityWhoStraveling
'''
Created on 26/11/2018

@author: aldo.villalba
'''

class TravelocityTripSummary (BasePage):
    
    def __init__(self,driver):
        super().__init__(driver) 
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,TimeoutException])
        self.cssTripTotalPrice ="div [class='tripTotals']>span[class='packagePriceTotal']" 
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div[class*='flex-card flex-tile details OD0']"))) 
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div[class*='flex-card flex-tile details OD1']"))) 
        
        self.cssDepartureTimeFrom = "div[class*='flex-card flex-tile details OD0'] div[class=departure] span[class='time type-500']"
        self.cssDepartureFrom = "div[class*='flex-card flex-tile details OD0'] div[class=departure] div[class='airportCode type-200']"
        self.cssDepartureTimeTo = "div[class*='flex-card flex-tile details OD0'] div[class=arrival] span[class='time type-500']"
        self.cssDepartureTo = "div[class*='flex-card flex-tile details OD0'] div[class=arrival] div[class='airportCode type-200']"
        self.cssReturnTimeFrom = "div[class*='flex-card flex-tile details OD1'] div[class=departure] span[class='time type-500']"
        self.cssReturnFrom = "div[class*='flex-card flex-tile details OD1'] div[class=departure] div[class='airportCode type-200']"
        self.cssReturnTimeTo ="div[class*='flex-card flex-tile details OD1'] div[class=arrival] span[class='time type-500']"
        self.cssReturnTo =  "div[class*='flex-card flex-tile details OD1'] div[class=arrival] div[class='airportCode type-200']"
        
        self.xpathDepartureTimeFrom = "//div[contains(@class,'flex-card flex-tile details OD0')]//div[text()='Las Vegas']/following-sibling::div"
        self.xpathDepartureFrom = "//div[contains(@class,'flex-card flex-tile details OD0')]//div[text()='Las Vegas']"
        self.xpathDepartureTimeTo = "//div[contains(@class,'flex-card flex-tile details OD0')]//div[text()='Los Angeles']/following-sibling::div"
        self.xpathDepartureTo = "//div[contains(@class,'flex-card flex-tile details OD0')]//div[text()='Los Angeles']"
        self.xpathReturnTimeFrom = "//div[contains(@class,'flex-card flex-tile details OD1')]//div[text()='Los Angeles']/following-sibling::div"
        self.xpathReturnFrom = "//div[contains(@class,'flex-card flex-tile details OD1')]//div[text()='Los Angeles']"
        self.xpathReturnTimeTo ="//div[contains(@class,'flex-card flex-tile details OD1')]//div[text()='Las Vegas']/following-sibling::div"
        self.xpathReturnTo =  "//div[contains(@class,'flex-card flex-tile details OD1')]//div[text()='Las Vegas']"
            
        self.cssPriceGuarantee = "div [class='priceGuarantee']"
        self.cssSpanTitle = "span[class='dateDepartureArrival type-500']"
        self.varTotalPrice = False
        self.varDepartureReturnInformation = False
        self.varTextPriceGuarantee = False
        self.varError=""
        
        self.idButtonBooking= "bookButton"
    '''
    Method to verify the parts of the trip
    Trip total price 
    Departureand return information
    Price guarantee
    '''
    def verifyTripComponents(self): 
        
        varError = ""
        try:
            tripTotalPrice = self.driver.find_element_by_css_selector(self.cssTripTotalPrice)
            print("The Total Price is: "+tripTotalPrice.text)
            self.varTotalPrice = True

        except NoSuchElementException as e:
            self.varTotalPrice = False
            varError = "------------There is not total price--------------"
            print(str(self.varTotalPrice)+varError)
            print(e)
        try:
            spanTitletoFindElements = self.driver.find_element_by_css_selector(self.cssSpanTitle)
                
        except NoSuchElementException as e:
            print("we are in a diferent page and its gonna find by css ")
            self.__findTripComponentsByCss()    
        else:
            print("we are in the else and its gonna find by xpath")
            self.__findTripComponetsByXpath()
            
        try:
            priceGuarantee = self.driver.find_element_by_css_selector(self.cssPriceGuarantee)
            print("This is the text>>"+priceGuarantee.text)
            self.varTextPriceGuarantee = True

        except NoSuchElementException as e:
            self.varTextPriceGuarantee = False
            self.varError="--------------There is not price Guarantee Text"
            print(str(self.varTextPriceGuarantee)+varError)
    
        if self.varTotalPrice and self.varDepartureReturnInformation and self.varTextPriceGuarantee:
            return str(True)+"-everything is ok"
        else:
            return str(False)+"-"+self.varError
        
    def __findTripComponetsByXpath(self):
        try:
            departureTimeFrom = self.driver.find_element_by_xpath(self.xpathDepartureTimeFrom)
            departureFrom = self.driver.find_element_by_xpath(self.xpathDepartureFrom)
            departureTimeTo = self.driver.find_element_by_xpath(self.xpathDepartureTimeTo)
            departureTo = self.driver.find_element_by_xpath(self.xpathDepartureTo)
            returnTimeFrom = self.driver.find_element_by_xpath(self.xpathReturnTimeFrom)
            returnFrom = self.driver.find_element_by_xpath(self.xpathReturnFrom)
            returnTimeTo =self.driver.find_element_by_xpath(self.xpathReturnTimeTo)
            returnTo =  self.driver.find_element_by_xpath(self.xpathReturnTo)
            print(departureFrom.text+"----------"+departureTimeFrom.text)
            print(departureTo.text+"---------"+departureTimeTo.text)
            print(returnFrom.text+"------"+returnTimeFrom.text)
            print(returnTo.text+"--------"+returnTimeTo.text)
            self.varDepartureReturnInformation = True
            
        except NoSuchElementException as e:
            self.varDepartureReturnInformation = False
            self.varError = "------------There is not some Information about departure or Return"
            print(str(self.varDepartureReturnInformation)+self.varError)
            print(e)
            
                
    def __findTripComponentsByCss(self):
        try:
            departureTimeFrom = self.driver.find_element_by_css_selector(self.cssDepartureTimeFrom)
            departureFrom = self.driver.find_element_by_css_selector(self.cssDepartureFrom)
            departureTimeTo = self.driver.find_element_by_css_selector(self.cssDepartureTimeTo)
            departureTo = self.driver.find_element_by_css_selector(self.cssDepartureTo)
            returnTimeFrom = self.driver.find_element_by_css_selector(self.cssReturnTimeFrom)
            returnFrom = self.driver.find_element_by_css_selector(self.cssReturnFrom)
            returnTimeTo =self.driver.find_element_by_css_selector(self.cssReturnTimeTo)
            returnTo =  self.driver.find_element_by_css_selector(self.cssReturnTo)
            print(departureFrom.text+"----------"+departureTimeFrom.text)
            print(departureTo.text+"---------"+departureTimeTo.text)
            print(returnFrom.text+"------"+returnTimeFrom.text)
            print(returnTo.text+"--------"+returnTimeTo.text)
            self.varDepartureReturnInformation = True
        
        except NoSuchElementException as e:
            self.varDepartureReturnInformation = False
            self.varError = "------------There is not some Information about departure or Return"
            print(str(self.varDepartureReturnInformation)+self.varError)
            print(e)
    
    def sendToWhoSTraveling(self):
        buttonBooking =self.driver.find_element_by_id(self.idButtonBooking)
        buttonBooking.click()
        
        return TravelocityWhoStraveling(self.driver)
                  
        
        