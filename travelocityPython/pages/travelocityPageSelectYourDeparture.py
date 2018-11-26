from pages import BasePage
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.travelocityPageTripSummary import TravelocityTripSummary
import ast
import time


'''
Created on 17/11/2018

@author: aldo.villalba
'''
class TravelocitySelectYourDeparture (BasePage):
    '''
    Method to get webElement from the pages
    '''
    def __init__(self,driver):
        super().__init__(driver)
        self.sortDropdown=self.driver.find_elements_by_id("sortDropdown")
        self.listOfFlies=self.driver.find_elements_by_xpath("//ul[@id='flightModuleList']/li")
        self.sortDurationAsc=self.driver.find_element_by_css_selector("#sortDropdown > option[value='duration:asc']")
        self.sortDurationDes=self.driver.find_element_by_css_selector("#sortDropdown > option[value='duration:desc']")
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        self.cssFirtsButton = "#flightModuleList li:nth-child(1) button"
        self.cssFirtsSelectThisFare = "#flightModuleList li:nth-child(1)  #basic-economy-tray-content-1 button"
        self.listOfFliesXpath="//ul[@id='flightModuleList']/li"
        self.listOfFliesCss="#flightModuleList>li"
        self.cssThirtButton ="#flightModuleList li:nth-child(3) button"
        self.ccsThirtSelectThisFare="#flightModuleList li:nth-child(3) #basic-economy-tray-content-3 button"
        self.idNotThanks ="forcedChoiceNoThanks"
        
    '''
    Method to Verify all components in the pages
    Sort
    ButtonSelect
    Duration Fly
    flight detail and baggage fees
    
    '''    
    def verifyAllComponents(self):
        time.sleep(5)
        varVerifyAllComponents="True-AllComponents are ok"
        varReturnVerifySort=self.__verifySort()
        varReturnVerifyButtonSelect=self.__verifyButtonSelect()
        
        if ast.literal_eval(self.splitReturn(varReturnVerifySort, 0))== False:
            varVerifyAllComponents=varReturnVerifySort
        elif ast.literal_eval(self.splitReturn(varReturnVerifyButtonSelect, 0))==False:
            varVerifyAllComponents=varReturnVerifyButtonSelect
        return varVerifyAllComponents
                
    '''
    Method to verify Sort and options of select
    select one allow order by price, Departure, Arrival or duration
    
    '''
    def __verifySort(self):
        varPrice = False
        varDeparture = False
        varArrival = False
        varDuration = False 
        varFallo = "All components are ok"       
        for items in self.sortDropdown:
            
            if items.text.lower().find("price")!= -1:
                varPrice = True
            else:
                varFallo="Sort has not price"
            if items.text.lower().find("departure")!= -1:
                varDeparture = True
            else:
                varFallo="Sort has not departure"    
            if items.text.lower().find("arrival")!= -1:
                varArrival = True
            else:
                varFallo="Sort has not arrival"
            if items.text.lower().find("duration")!= -1:
                varDuration = True
            else:
                varFallo="Sort has not duration"
        if varPrice==True and varDeparture == True and varArrival == True and varDuration == True:
            varReturn = True
        else:
            varReturn = False
        return str(varReturn)+"-"+varFallo
    '''
    Method to verify that in every result 
    there is a button to select
    '''
    def __verifyButtonSelect(self):
        varFallo="All result has button select"
        time.sleep(5)
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//ul[@id='flightModuleList']")))  
        print("There are "+str(len(self.listOfFlies))+" flies to verify select")
       
        x=0  #var to count to select button
        numLi=0  #var to count li to baggages, duration, flight details
        for fly in self.listOfFlies:
            numLi = numLi+1
            varClass = fly.get_attribute("class")
            if varClass == "flight-module segment offer-listing":
                try:
                    x=x+1 
                    varTextToFind="//button//span[text()='Select result "+str(x)+" when sorted by price']"
                    self.wait.until(EC.visibility_of_all_elements_located((By.XPATH,varTextToFind)))
                    varSelect = fly.find_element_by_xpath(varTextToFind)
                    if varSelect.text == "Select result "+str(x)+" when sorted by price":
                        varReturn = True
                except NoSuchElementException as e:
                    varReturn = False
                    varFallo="The element number "+str(x)+" has not button select"
                    print("Error has to be That the element number "+str(x)+" has not button select")
                    continue
                try:
                    varTextToDuration="//li["+str(numLi)+"]//span[@class='duration-emphasis'][@data-test-id='duration']"
                    self.wait.until(EC.visibility_of_all_elements_located((By.XPATH,varTextToDuration)))
                    varDuration = fly.find_element_by_xpath(varTextToDuration)
                    if varDuration.text :
                        varReturn = True
                except NoSuchElementException as e:
                    print(e)
                    varReturn = False
                    varFallo="The element li number "+str(numLi)+" has not duration"
                    print("Error has to be that the li number "+str(numLi)+" has not duration ")
                try:
                    varTextToBaggage="//li["+str(numLi)+"]//span[@class='show-flight-details']"
                    varBaggage = fly.find_element_by_xpath(varTextToBaggage)
                    
                    if varBaggage.text.find("baggage"):
                        varReturn = True
                       
                except NoSuchElementException as e:
                    try:
                        varTextToBaggage = "//li["+str(numLi)+"]//span[@class='forced-tray-toggle-text']"
                        varBaggage = fly.find_element_by_xpath(varTextToBaggage)
                        if varBaggage.text.find("baggage"):
                            varReturn = True
                    except NoSuchElementException as e:
                        varReturn = False
                        varFallo="The element li number "+str(numLi)+" has not baggage"
                        print("Error has to be that the li number "+str(numLi)+" has not baggage")
                    
            else:
                #print("The webElement has not to have select because is a promo")
                continue     
        return str(varReturn)+"-"+varFallo
    
    '''
    Method to verify Sort by duration
    '''
    def verifybyDuration(self):
        
        varReturnByDuration="The order by duration is ok"
        self.wait.until(EC.visibility_of_all_elements_located((By.ID,"flightModuleList"))) 
        varOrderOrigin = self.goThroughList(self.listOfFlies)
        self.sortDurationAsc.click()
        
        self.wait.until(EC.presence_of_all_elements_located((By.ID,"flightModuleList"))) 
        time.sleep(8)
        self.listOfFliesAfterOrder= self.driver.find_elements_by_css_selector(self.listOfFliesCss)
       
        varOrderDurationAsc=self.goThroughList(self.listOfFliesAfterOrder)
        verCorrectOrderBolean=self.comparetSort(varOrderOrigin, varOrderDurationAsc, "asc")
        if verCorrectOrderBolean :
            return str(verCorrectOrderBolean)+"-"+varReturnByDuration  
        else:
            return str(verCorrectOrderBolean)+"-The list is not in order"  
      
    '''
    Method to select el firts button from departure to los
    anteles
    '''
    def selectFirstResult(self):
        
        varReturnSelectFirst="Selecciono el primer boton"
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,self.cssFirtsButton)))
        time.sleep(3)
        self.buttonSelectFirstElement = self.driver.find_element_by_css_selector(self.cssFirtsButton)
        self.buttonSelectFirstElement.click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,self.cssFirtsSelectThisFare)))
        time.sleep(3)
        self.buttonFirtsSelectThisFare = self.driver.find_element_by_css_selector(self.cssFirtsSelectThisFare)
        self.buttonFirtsSelectThisFare.click()
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,self.listOfFliesCss)))
        time.sleep(3)
        self.buttonSelectThirthElement = self.driver.find_element_by_css_selector(self.cssThirtButton)
        self.buttonSelectThirthElement.click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,self.ccsThirtSelectThisFare)))
        time.sleep(3)
        self.buttonThirthSelectThisFare = self.driver.find_element_by_css_selector(self.ccsThirtSelectThisFare)
        self.buttonThirthSelectThisFare.click()
        self.buttonNoThanks = self.driver.find_element_by_id(self.idNotThanks) 
        self.buttonNoThanks.click()
        
        return TravelocityTripSummary(self.driver)
        
        
