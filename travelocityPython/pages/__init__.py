from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re


class BasePage():
    
    '''
    Method to driver in all pages Objets
    
    '''
    def __init__(self,driver):
        self.driver = driver
    '''
    Method to send driver
    '''
    def getDriver(self):
        return self.driver
    '''
    Method to close the driver
    '''
    def dispose(self):
        self.driver.close() 
    '''
    Method helper to change format date
    '''    
    def monthToNum(self,shortMonth):
        return{
            'Jan' : 1,
            'Feb' : 2,
            'Mar' : 3,
            'Apr' : 4,
            'May' : 5,
            'Jun' : 6,
            'Jul' : 7,
            'Aug' : 8,
            'Sep' : 9, 
            'Oct' : 10,
            'Nov' : 11,
            'Dec' : 12
        }[shortMonth]
    '''
    Method helper to sple
    '''
    def splitReturn(self,stringReturn,numParam):
        varArrayString = stringReturn.split("-")
        return varArrayString[numParam]
    '''
    Method helper to run through the list of flies and
    discriminate all flies that they are not flies 
    '''    
            
    def goThroughList(self,listToRun):
        numLi=0  #var to count li to baggages, duration, flight details
        varListDuration= [None]
        for li in listToRun:
            varClass = li.get_attribute("class")
            numLi=numLi+1
            
            if varClass == "flight-module segment offer-listing":
                try:
                    varTextToDuration="//li["+str(numLi)+"]//span[@class='duration-emphasis'][@data-test-id='duration']"
                    WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,varTextToDuration))) 
                    varDuration = li.find_element_by_xpath(varTextToDuration)
                    
                    if varDuration.text :
                        varListDuration.append(varDuration.text)
                except NoSuchElementException as e:
                    print(e)
                    print(varTextToDuration)
                            
            else:
                #print("The webElement has not to have select because is a promo")
                continue
        varListDuration.pop(0) 
        return varListDuration
    '''
    Method to compare list and verify the sort is correct or not
    '''
    def comparetSort(self,listOrign,listOrderDuration,ascOrDesc):
        if ascOrDesc=="asc":
            
            listOrign=self.returnNumbers(listOrign)
            listOrign.sort(key=int)
            listOrderDuration=self.returnNumbers(listOrderDuration)
            #print(listOrign)
            #print("----------------------------------------------------")
            #print(listOrderDuration)
            if listOrign==listOrderDuration:
                return True
            else:
                return False
        elif ascOrDesc=="desc":
            listOrign=self.returnNumbers(listOrign)
            listOrign.sort(key=int,reverse=True)
            print(listOrign)
            listOrderDuration=self.returnNumbers(listOrderDuration)
            print(listOrderDuration)
            if listOrign==listOrderDuration:
                return True
            else:
                return False
        else:
            print("there is no order for parameter sended")
            return False
    
    def returnNumbers(self,listToTransform):
        listReturnNumbers=[None]
        
        for item in listToTransform:
            if re.findall(" [0-9]m$", item):
                
                item = item.replace("h ","h 0")
            newItem=item.replace("h ","")
            newItem=newItem.replace("m","")
            listReturnNumbers.append(newItem)
        listReturnNumbers.pop(0)
        
        return listReturnNumbers           
        
            
        
        
             