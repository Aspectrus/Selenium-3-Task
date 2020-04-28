import numpy
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    IsPrice100 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    if IsPrice100:
        browser.find_element_by_id("book").click()
        x = browser.find_element_by_id("input_value").get_attribute("innerHTML")
        answer = numpy.log(abs(12 * numpy.sin(float(x))))
        print(answer)
        browser.find_element_by_id("answer").send_keys(str(answer))
        browser.find_element_by_id("solve").click()
finally:
    time.sleep(3)
