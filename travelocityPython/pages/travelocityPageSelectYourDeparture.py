from pages import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
'''
Created on 17/11/2018

@author: aldo.villalba
'''
class TravelocitySelectYourDeparture (BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.sortDropdown=self.driver.find_elements_by_id("sortDropdown")
        self.listOfFlies=self.driver.find_elements_by_xpath("//ul[@id='flightModuleList']/li")
        
    def verifyAllComponets(self):
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
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//ul[@id='flightModuleList']")))  
        
        print("There are "+str(len(self.listOfFlies))+" flies to verify select")
        x=0
        for fly in self.listOfFlies:
            
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
                    print(varSelect.text)
                    varReturn = False
                    varFallo="The element number "+str(x)+" has not button select"
                    print("Error has got be The element number "+str(x)+" has not button select")
                    continue
            else:
                #print("The webElement has not to have select because is a promo")
                continue     
        
        return str(varReturn)+"-"+varFallo
                
                
                
                