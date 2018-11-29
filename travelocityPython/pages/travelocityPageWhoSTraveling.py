from pages import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
'''
Created on 29/11/2018

@author: aldo.villalba
'''

class TravelocityWhoStraveling (BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,TimeoutException])
        self.inputFirstname = "input[id='firstname[0]']"
        self.inputLastName  = "input[id='lastname[0]']"
        self.lisfOfPayment  ="ul[class='payment-tabs '] li"
        self.selectMonthBirth ="select[name*='.dateOfBirth.month']"
        self.selectDayBirth = "select[name*='.dateOfBirth.day']"
        self.selectYearBirth = "select[name*='.dateOfBirth.year']"
        self.varBooleanInputFirsName = False
        self.varBooleanRightPage = False
        self.varBooleanInputLastName = False
        self.varBooleanListPayment = False
        self.varBooleanSelectsBirth = False
        self.varError = ""
        
    def verifyPageWhoStraveling(self):
        varRightPage = "Travelocity: Payment"
          
        #1
        if self.driver.title == varRightPage:
            self.varBooleanRightPage = True
        else:
            self.varError = "The page has other title, maybe we are in other page"
        #2    
        try:
            inputFirstName = self.driver.find_element_by_css_selector(self.inputFirstname) 
            self.varBooleanInputFirsName = True
        
        except NoSuchElementException as e:
            self.varError = "There is a Error. There is no textbox for first name"
            print("there is not textbox for first name"+str(e))
        #3    
        try:  
            inputLastName =  self.driver.find_element_by_css_selector(self.inputLastName) 
            self.varBooleanInputLastName = True
            
        except NoSuchElementException as e:
            self.varError = "There is a Error. There is no textbox for Last name"
            print("there is not textbox for Last name"+str(e))
        #4
        try:
            listOfPayment = self.driver.find_elements_by_css_selector(self.lisfOfPayment)
            if len(listOfPayment)==2:
                self.varBooleanListPayment = True
                
        except NoSuchElementException as e:
            self.varError = "There is a Error. There is not list of payment way"
            print("There is no list of payment way"+str(e))
            
        #5
        try:
            selectMonthBirth =self.driver.find_element_by_css_selector(self.selectMonthBirth)
            selectDayBirth = self.driver.find_element_by_css_selector(self.selectDayBirth)
            selectYearBirth = self.driver.find_element_by_css_selector(self.selectYearBirth)
            self.varBooleanSelectsBirth = True

        except NoSuchElementException as e:   
            self.varError="There is a Error. There is not some of selects for Birth"
            print("There is not some one of selects birth"+str(e))
            
        if self.varBooleanInputFirsName and self.varBooleanRightPage and self.varBooleanInputLastName and self.varBooleanListPayment and self.varBooleanSelectsBirth:
            return str(True)+"-This is the page of Who s Traveling"
        else:
            return str(False)+"-"+self.varError
        
        
                 
            
                
                
              
            