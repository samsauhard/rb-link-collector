from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://www.redbubble.com/people/ilustrata/explore?page=1&sortOrder=recent')
x=101
y=1

while(x<172):	
	try:		
		a = driver.find_element_by_css_selector('#app > div > div.ds-theme-find-your-thing.App__dsWrapper--RyVET > main > div > div:nth-child(4) > div > div > div > div > a:nth-child('+str(y)+')')
		print(a.get_attribute('href'))
		y=y+1
	except:
		y=1
		x=x+1
		driver.get('https://www.redbubble.com/people/ilustrata/explore?page=1&sortOrder=recent')
		time.sleep(4)
		driver.find_element_by_css_selector('#app > div > div.ds-theme-find-your-thing.App__dsWrapper--RyVET > main > div > div.styles__box--206r9.ExploreDesignsGrid__masonryGridContainer--ncG3n > div:nth-child(2) > div > div > div:nth-child('+str(x)+')').click()

