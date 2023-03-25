from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.4.778 Yowser/2.5 Safari/537.36")
# options.add_argument('--headless')

url = 'https://www.isuct.ru/student/schedule'
driver = webdriver.Chrome(executable_path='D:\\DataSatanist\\parser\\chromedriver.exe',
                          options=options)

try:
    print('[+] Connection...')
    driver.get(url=url)
    time.sleep(1)
    print('#' * 20, '\n[+] Apply the group')
    driver.find_element(By.ID, 'edit-type-currentstudentsgroups').click()
    time.sleep(1)
    print('[+] 3')
    driver.find_element(By.ID, 'edit-idgr').send_keys('1/244')
    time.sleep(5)
    print('[+] 2')
    driver.find_element(By.ID, 'edit-idgr').send_keys(Keys.ARROW_DOWN + Keys.ENTER)
    print('[+] 1')
    driver.find_element(By.CLASS_NAME, 'ajax-processed').click()
    time.sleep(1)
    print('[+] Complete...')
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
    schedule = element.find_elements(By.TAG_NAME, 'tr')
    for i in schedule:
        print(i.text)
    time.sleep(10)
    week = element.find_elements(By.CLASS_NAME, 'day')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
