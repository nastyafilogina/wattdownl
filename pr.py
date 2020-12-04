from selenium import webdriver
from flask import Flask, request
import time
import os
#from flask import app
#from intro_to_flask import app
#from run import app as application

#if __name__ == '__main__':
#    port = int(os.environ.get('PORT', 5000))
#    app.run(host='0.0.0.0', port=port)




server = Flask(__name__)
if __name__ == '__main__':
#    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.get("https://www.wattpad.com/711036001-silent-reading-%EF%BC%88%E9%BB%98%E8%AF%BB-modu%EF%BC%89-bl-novel-by-priest")

SCROLL_PAUSE_TIME = 1.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
time.sleep(SCROLL_PAUSE_TIME*2)

ch1 = driver.find_elements_by_xpath("//div[@class='col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading']/pre/p")

fr = ""
for i in ch1:
    not_formatted = str(driver.execute_script("""
    arguments[0].removeChild(arguments[0].childNodes[arguments[0].childNodes.length - 1]);
    var fulltext = new String();
    for (let i = 0; i <= arguments[0].childNodes.length - 2; i++) {
        fulltext = fulltext + arguments[0].childNodes[i].textContent;
    }
    return fulltext
    """, i))
    #not_formatted = str(driver.execute_script('return arguments[0].childNodes[0].nodeValue', i))

    #not_formatted = i.text
    formatted = not_formatted.replace('\n', '\n\n')
    fr = fr + '\n\n' + formatted

print(fr)

driver.quit()








#ch1 = driver.find_elements_by_xpath("//div[@class='col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading' and @class='comment-marker on-inline-comments-modal']")
#ch1 = driver.find_elements_by_xpath("//div[@class='col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading' and not(self::span)]")
#ch1 = driver.find_elements_by_xpath("//div[@class='col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading']//span[@class='comment-marker on-inline-comments-modal']")
#ch1 = driver.find_elements_by_xpath("//div[@class='col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading']//*[@class!='comment-marker on-inline-comments-modal']")

#ch1 = driver.find_elements_by_xpath("//div[@class='col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading']//pre//p//*[@class!='comment-marker on-inline-comments-modal' and @class!='comment-marker hide-marker on-inline-comments-modal'")
#ch1 = driver.find_elements_by_xpath("//div[@class='col-xs-10 col-xs-offset-1 col-sm-10 col-sm-offset-1 col-md-7 col-md-offset-1 col-lg-6 col-lg-offset-3 panel panel-reading']/pre//*[not(self::span)]")

