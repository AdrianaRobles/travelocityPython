from selenium import webdriver

class BasePage():
    def __init__(self,driver):
        self.driver = driver
    
    def getDriver(self):
        return self.driver

    def dispose(self):
        self.driver.close() 
        
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
    
    def splitReturn(self,stringReturn,numParam):
        varArrayString = stringReturn.split("-")
        return varArrayString[numParam]
        
            

        
    