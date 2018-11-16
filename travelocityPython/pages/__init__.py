from selenium import webdriver

class BasePage():
    def __init__(self,driver):
        self.driver = driver
            
    
    def getDriver(self):
        return self.driver
    def dispose(self):
        self.driver.close()      
        

        
    