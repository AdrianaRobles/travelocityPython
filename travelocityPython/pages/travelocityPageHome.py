from pages import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC 
'''
Created on 15/11/2018

@author: aldo.villalba
'''

class TravelocityHome(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get("https://www.travelocity.com")
        self.botonVuelos=self.driver.find_element_by_id("tab-flight-tab-hp")
        self.selectFrom=self.driver.find_element_by_id("flight-origin-hp-flight")
        self.selectTo = self.driver.find_element_by_id("flight-destination-hp-flight")
        self.calendarFrom = self.driver.find_element_by_id("flight-departing-hp-flight")
        self.calendarTo=self.driver.find_element_by_id("flight-returning-hp-flight")
        
    def findFly(self):
        self.botonVuelos.click()
        self.selectFrom.click()
        self.selectFrom.send_keys("LAS")
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.ID,"typeaheadDataPlain")))  
        lasElementFrom = self.driver.find_element_by_xpath("//ul//li/a[@data-value='Las Vegas, NV (LAS-All Airports)']") 
        lasElementFrom.click()
        self.selectTo.click()
        self.selectTo.send_keys("LAX");
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.ID,"typeaheadDataPlain")))  
        laxElementTo = self.driver.find_element_by_xpath("//ul//li/a[@data-value='Los Angeles, CA (LAX-Los Angeles Intl.)']")
        laxElementTo.click()
        
        self.calendarFrom.click()
        self.selectDayFromAndTo("Feb 2019","14-Feb-2019")
        self.calendarTo.click()
        self.selectDayFromAndTo("Feb 2019","18-Feb-2019")
        
    def selectDayFromAndTo(self,month,choicedDay):
        
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.datepicker-cal button.next")))
        
        while True:
            nameMonth=self.driver.find_element_by_css_selector("caption.datepicker-cal-month-header")
            print(nameMonth.text)
            if nameMonth.text!=month:
                buttonNextMonth=self.driver.find_element_by_css_selector("div.datepicker-cal button.next")
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.datepicker-cal button.next")))
                buttonNextMonth.click()
            elif nameMonth.text==month:
                break
        splitDate=choicedDay.split("-")  
        monthReturn=self.monthToNum(splitDate[1])
        
        stringXpath="//button[@data-year='"+splitDate[2]+"'][@data-month='"+str(monthReturn)+"'][@data-day="+splitDate[0]+"]"
        buttonSinceDay = self.driver.find_element_by_xpath(stringXpath)
        buttonSinceDay.click()
            
        
        