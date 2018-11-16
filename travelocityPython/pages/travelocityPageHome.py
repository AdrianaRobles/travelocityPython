from pages import BasePage

'''
Created on 15/11/2018

@author: aldo.villalba
'''
from selenium.webdriver.support import expected_conditions


class TravelocityHome(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get("https://www.travelocity.com")
    
    def findFly(self):
        botonVuelos=self.driver.find_element_by_id("tab-flight-tab-hp")
        botonVuelos.click()
        selectFrom=self.driver.find_element_by_id("flight-origin-hp-flight")
        selectFrom.click()
        selectFrom.send_keys("LAS")
        listFrom=self.driver.find_element_by_id("typeaheadDataPlain")
        self.driver.wait().until(expected_conditions.visibility_of_all_elements_located(listFrom))
        
        