###-
###- Web whatsapp python selenium script
###-
###- GauravDS
###- JAMES Whatsapp Module(b)
###-


### configurations
number_of_times = 10
message = 'Hi! are you there?'



### Selenium automation
#- download http://chromedriver.storage.googleapis.com/index.html?path=2.21/
#- details https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

## Selenium web drivers
driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	driver = webdriver.Chrome()
## quit web driver for selenium
def web_driver_quit():
	driver.quit()

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	wait(5)

def sendMessage(msg='Hi!'):
	web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
	web_obj.send_keys(msg)
	web_obj.send_keys(Keys.RETURN)


### Main Method
if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	wait()
	
	for i in range(number_of_times):
		sendMessage(message)
		wait()
	print("Process complete successfully")

	wait()
	web_driver_quit()