from driver import Crowler
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

source = 'https://www.daraz.com.bd/religion-books/'
cr = Crowler(source, 'firefox')

products_html = WebDriverWait(cr.data, 15).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]"))
)

products = products_html.find_elements(by=By.TAG_NAME, value='div')

for product in products:
    img = product.find_element(by=By.TAG_NAME, value='img')
    print(img.get_attribute('src'))

cr.teardown()