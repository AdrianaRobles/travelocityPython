from pages import BasePage

'''
Created on 17/11/2018

@author: aldo.villalba
'''
class TravelocitySelectYourDeparture (BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.sortDropdown=self.driver.find_elements_by_id("sortDropdown")
    
    def verifyAllComponets(self):
        varPrice = False
        varDeparture = False
        varArrival = False
        varDuration = False
        varFallo = "All components are ok"
                
        for items in self.sortDropdown:
            if items.text.lower().find("price")!= -1:
                varPrice = True
            elif items.text.lower().find("departure")!= -1:
                varDeparture = True
            elif items.text.lower().find("arrival")!= -1:
                varArrival = True
            elif items.text.lower().find("duration")!= -1:
                varDuration = True
            else:
                varFallo="Sort is not ok"
        
        if varPrice==True and varDeparture == True and varArrival == True and varDuration == True:
            varReturn = True
        else:
            varReturn = False
        
        return str(varReturn)+"-"+varFallo
                
                
                
                