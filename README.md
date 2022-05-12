# PyWhatsapp
Python Selenium script for fun with web WhatsApp. Thanks [Mak](https://github.com/mayanksaxena) to give this idea.

![status](https://rawgit.com/gauravds/PySelenium/master/imgs/status.svg)
![version](https://rawgit.com/gauravds/PySelenium/master/imgs/version.svg)

##### Uses
-  `Irritate_friend.py` for send a same message(message = Hi! are you there?) n times(number_of_times = 10) on script.

Run this script as `$python src/Irritate_friend.py`
It will open a chrome browser and then open web.WhatsApp.com and then immediate scan your QR code to login, and select friend to irritate. Script has 10 sec for all this process. And then enjoy irritate friend.

### Dependencies
- ![Platform](https://rawgit.com/gauravds/PySelenium/master/imgs/platform.svg)(May work on linux)
- ![Language=Py3.5](https://rawgit.com/gauravds/PySelenium/master/imgs/language.svg)(May work on python 2.7)
- ![Tool=Selenium-2.53.2](https://rawgit.com/gauravds/PySelenium/master/imgs/tool.svg)
- Google Chrome-50.0 browser(It will also work on other browser, need to change drivers)
- chromedriver_mac32.zip web browser driver (Also available for linux)

### Installation
- `$ sudo pip3 install selenium`
  [or Find in resource folder for Selenium-2.53.2]
- copy extracted of chromedriver_mac32.zip and paste into `/usr/local/bin`. [Find in resource]
    - download driver from https://chromedriver.chromium.org/downloads

voila!
