from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

def atp_scraper(profile_site, file_name):
    website = profile_site
    path = "C:\Program Files (x86)\chromedriver"
    driver = webdriver.Chrome(path)
    driver.get(website)

    # drivers
    rows = driver.find_elements_by_tag_name('tr')
    prog_bars = driver.find_elements_by_xpath('//div[@class="progress progress-profile"]')

    # storing scraped data in lists
    category = []
    info = []
    player_name = []

    # scraping player name, general info and progress bar --> it will be long data for now 
    name = driver.find_element_by_tag_name('h3').text

    for point in rows:
        try:
            category.append(point.find_element_by_xpath('./th').text)
            info.append(point.find_element_by_xpath('./td').text)
        except:
            pass

    for prog_bar in prog_bars:
        info.insert(-1, prog_bar.text)

    # scraping player statistics 
    website = website[:-7]
    website_stat = website + str("statistics")
    driver.get(website_stat)

    stat_n = driver.find_elements_by_tag_name('td')
    stat_i = driver.find_elements_by_tag_name('th')

    for n in stat_n:
        category.append(n.text)

    for i in stat_i:
        info.append(i.text)

    driver.quit()

    category = [value for value in category if value != '']
    info = [value for value in info if value != '']

    info.remove('Serve')
    info.remove('Return')
    info.remove('Total')

    for i in range((len(category))):
        player_name.append(name)

    df = pd.DataFrame({'Name': player_name, 'Category': category, 'Info': info})
    df.to_csv(file_name, index=False)

    #print(df)

