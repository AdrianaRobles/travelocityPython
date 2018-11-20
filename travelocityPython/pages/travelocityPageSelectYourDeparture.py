from pages import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import ast

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
    '''
    Method to Verify all components in the pages
    Sort
    ButtonSelect
    Duration Fly
    flight detail and baggage fees
    
    '''    
    def verifyAllComponents(self):
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
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//ul[@id='flightModuleList']")))  
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
                    WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,varTextToFind)))
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
                    varDuration = fly.find_element_by_xpath(varTextToDuration)
                    if varDuration.text :
                        varReturn = True
                except NoSuchElementException as e:
                    varReturn = False
                    varFallo="The element li number "+str(numLi)+" has not duration"
                    print("Error has to be that the li number "+str(numLi)+" has not duration ")
                try:
                    varTextToBaggage="//li["+str(numLi)+"]//span[@class='forced-tray-toggle-text']"
                    varBaggage = fly.find_element_by_xpath(varTextToBaggage)
                    if varBaggage == "See fare restrictions and baggage fees":
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
        WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//ul[@id='flightModuleList']"))) 
        varOrderOrigin = self.goThroughList(self.listOfFlies)
        self.sortDurationAsc.click()
        
        self.listOfFliesAfterOrder= self.driver.find_elements_by_xpath("//ul[@id='flightModuleList']/li")
        WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((By.ID,"flightModuleList"))) 
        
        varOrderDurationAsc=self.goThroughList(self.listOfFliesAfterOrder)
        verCorrectOrderBolean=self.comparetSort(varOrderOrigin, varOrderDurationAsc, "desc")
        
        return str(verCorrectOrderBolean)+"-"+varReturnByDuration        
        