require "selenium-webdriver"

driver = Selenium::WebDriver.for :chrome

driver.navigate.to "http://www.thechrisnutterhub.com"

driver.quit
