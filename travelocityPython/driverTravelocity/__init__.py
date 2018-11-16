from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WebDriver():
    
    def __init__(self,browser):
        self.browser=browser
         
        
    def getDriver(self):
        if self.browser == 'Chrome':
            driver = webdriver.Chrome() 
         
        elif self.browser == 'FireFox' :
            driver = webdriver.Chrome()
           
        return driver
    
    
       
        
        


