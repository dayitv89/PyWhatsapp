###-
###- Web whatsapp python selenium script
###-
###- GauravDS
###- JAMES Whatsapp Module(b)
###-


### configurations
waiting_time = 1
number_of_times = 3
message = 'Hi! are you there?'

### Selenium automation
#- download http://chromedriver.storage.googleapis.com/index.html?path=2.21/
#- details https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
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
	quit()

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	while True:
		time.sleep(1)
		try:
			appLoad = driver.find_element(By.XPATH,"//div[@title='Type a message']")
			if appLoad:
				break
		except NoSuchElementException:
			pass
		finally:
			print('Login Checked')

def sendMessage(msg='Hi!'):
	web_obj = driver.find_element(By.XPATH,"//div[@title='Type a message']")
	web_obj.send_keys(msg)
	web_obj.send_keys(Keys.RETURN)


def send_message_in_loop():
	for i in range(number_of_times):
		sendMessage(message)
		print(str(i+1) + " message sent & waiting for seconds: "+str(waiting_time))
		wait(waiting_time)
	print("Process complete successfully")

### Main Method
if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	name = 'send'
	while name != 'q':
		send_message_in_loop()
		name = input("continue any key, quit press q: ") 
	web_driver_quit()
