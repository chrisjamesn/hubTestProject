#Import the selenium webdriver
require "selenium-webdriver"

#Create the selenium webdriver for the Google Chrome Browser
driver = Selenium::WebDriver.for :chrome

#Navigate to the LOCAL version of "theChrisNutterHub.com" homepage
driver.navigate.to "http://localhost/theChrisNutterHub.com/home.php"

#Wait for 5s
sleep 5

#Navigate to the GitHub Profile
#https://stackoverflow.com/questions/33155454/how-to-find-an-element-by-href-value-using-selenium-python
github_link = driver.find_element(:id, "6")
github_link.click

#Wait for 5s
sleep 5

#Use "driver.current_url" to get the current URL
current_url = driver.current_url

#If the URL is equal to the target URL of the GitHub Profile, print a success statement; otherwise, print the current URL
if current_url == "https://github.com/chrisjamesn"
	puts "Driver navigated to the correct URL successfully!"
else
	puts current_url
end

#Quit the driver
driver.quit
