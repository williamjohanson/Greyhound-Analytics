# fill_txt_data.py
# Fill the txt file for the days races via web automation.

# Imports.
import datetime
from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
import html2text
import os

def extract_html(meeting, total_races, i, date):
    """ Parse the HTML into text. """
    filename = open('Race Data/M' + str(meeting) + '_' + str(date) + '/file.html', 'r').read()
    
    h = html2text.HTML2Text()
    h.ignore_links = True
    soup = BeautifulSoup(filename, 'html.parser')

    main_text = soup.get_text()

    final_text = BeautifulSoup(main_text, 'html.parser')

    file_a = 'Race Data/M' + str(meeting) + '_' + str(date) + '/Racea' + str(i) + '.txt'
    os.makedirs(os.path.dirname(file_a), exist_ok=True)

    with open(file_a, 'w') as out_txt_f:
        out_txt_f.write(final_text.get_text())
    
    sec_filename = open('Race Data/M' + str(meeting) + '_' + str(date) + '/Racea' + str(i) + '.txt', 'r').read()

    file_b = 'Race Data/M' + str(meeting) + '_' + str(date) + '/Raceb' + str(i) + '.txt'

    os.makedirs(os.path.dirname(file_b), exist_ok=True)

    with open(file_b, 'w') as out_txt_b:
        out_txt_b.write(h.handle(sec_filename))


def web_extract(meeting, total_races):
    """ Fill text files using web extraction - automating fills. """
    current = datetime.datetime.today()
    year = current.year
    month = current.month
    if month < 10: 
        month = '0' + str(month)
    day = current.day
    if day < 10: 
        day = '0' + str(day)
    driver = webdriver.Chrome()

    link_a = "https://new.tab.co.nz/extended-form/"
    date = ("{}-{}-{}".format(year, month, day))

    for i in range(1, total_races + 1):
        url = link_a + date + '-m' + str(meeting) + '-r' + str(i)
        driver.get(url)
        driver.find_element_by_xpath('/html/body/div/div/main/div[2]/div[2]/div[2]/div[1]/span[6]/a').click()
        time.sleep(2)
        #driver.find_element_by_xpath('/html/body/div/div/main/div[2]/div[2]/div[1]/a/div[2]').click() # Don't think this is doing meke.
        
        #time.sleep(5)

        current_URL = driver.current_url
        print(current_URL)
        data = requests.get(current_URL)

        file_html = "Race Data/M" + str(meeting) + "_" + str(date) + "/file.html"
        os.makedirs(os.path.dirname(file_html), exist_ok=True)

        with open(file_html, 'w') as out_html_f:
            out_html_f.write(str(data.text.encode('utf-8')))
        
        extract_html(meeting, total_races, i, date)



