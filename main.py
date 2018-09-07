import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import xlsxwriter
import urllib.request

browser = selenium.webdriver.Chrome('path/chromedriver')#Download the Chrome driver and Change the file path
url = 'http://bbcsfx.acropolis.org.uk'
browser.get(url)
workbook = xlsxwriter.Workbook('SFXIndex.xlsx')
worksheet = workbook.add_worksheet()
num = 1

for page in range(1, 642):
    print("page number: " + str(page))

    if page != 1:
        page_link = browser.find_element_by_xpath('//a[@class="paginate_button next"]')
        page_link.click()

    sleep(4)

    html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    html1 = html[html.find('<tbody>'): ]
    html2 = html1[ :html1.find('</tbody>')]

    while True:
        num2 = html2.find('</tr>')
        if num2 == -1:
            break
        name = html2[html2.find('<td tabindex="0">') + 17: html2.find('</td>')]
        link = html2[html2.find('href') + 6 : ]
        link = link[:link.find('aria-label') - 2]
        num3 = html2.find('href')
        html2 = html2[num2 + 5:]

        file = link[link.find('/') + 1:]
        file = file[file.find('/') + 1:]

        worksheet.write('A' + str(num), file)
        worksheet.write('B' + str(num), name)
        num += 1
        print(file)
        print(name)
        '''
        #Downloading
        link = url + link[2:]
        urllib.request.urlretrieve(link, file)
        '''

workbook.close()

    #driver = webdriver.Chrome(executable_path="path/chromedriver.exe",chrome_options=options)



'''
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"D:\TestDownloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
names = browser.find_element_by_xpath("//tr[@role='row']/td").get_attribute("value")
print(names)
'''

