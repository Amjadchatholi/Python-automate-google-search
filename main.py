# # 1
from selenium import webdriver
import time

import selenium

browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver')

browser.get('https://www.google.com')

time.sleep(2)

search_input = browser.	find_element_by_name ('q')
search_input.send_keys('hello world')

time.sleep(2)

search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()



'''
<input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwi0r7Pjqdb6AhVkU3wKHYHjDkcQ39UDCAQ">
<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" role="button" tabindex="0" type="submit" data-ved="0ahUKEwj2geHc0dr6AhV_zzgGHZYXDRYQ4dUDCAs">

'''
# 2

# from selenium import webdriver

# list= "amjad"

# browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver')

# browser.get('https://www.google.com/search?q=' + list)

# 3

# from selenium import webdriver

# list= input("enter to something:")
# list=list.replace(' ', '+')

# browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver')
# for i in range(1):
#     element= browser.get('https://www.google.com/search?q=' + list + "&start" +str(i))










