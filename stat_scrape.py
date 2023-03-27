from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website_stat = "https://www.ultimatetennisstatistics.com/playerProfile?playerId=4920&tab=statistics"
path = "C:\Program Files (x86)\chromedriver"
driver = webdriver.Chrome(path)
driver.get(website_stat)

stat_name = []
stat_info = []

stat_n = driver.find_elements_by_tag_name('td')
stat_i = driver.find_elements_by_tag_name('th')

for name in stat_n:
    stat_name.append(name.text)

for info in stat_i:
    stat_info.append(info.text)

driver.quit()

stat_name = [value for value in stat_name if value != '']
stat_info = [value for value in stat_info if value != '']

stat_info.remove('Serve')
stat_info.remove('Return')
stat_info.remove('Total')

print(stat_name)
print(stat_info)

print(len(stat_name))
print(len(stat_info))
