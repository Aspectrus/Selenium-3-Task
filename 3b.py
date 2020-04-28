import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)


class Test(unittest.TestCase):
    def test_run1(self):

        firstname = browser.find_elements(By.XPATH, "//input[@placeholder='Input your first name']")
        lastname = browser.find_elements(By.XPATH, "//input[@placeholder='Input your last name']")
        email = browser.find_elements(By.XPATH, "//input[@placeholder='Input your email']")
        phone = browser.find_elements(By.XPATH, "//input[@placeholder='Input your phone:']")
        adress = browser.find_elements(By.XPATH, "//input[@placeholder='Input your address:']")

        self.assertEqual(len(firstname), 1,"First name input not found")
        if len(firstname):
            firstname[0].send_keys("Rapolas")
        self.assertEqual(len(lastname), 1, "Last name input not found")
        if len(lastname):
            lastname[0].send_keys("Kubaitis")
        self.assertEqual(len(email), 1, "Email input not found")
        if len(email):
            email[0].send_keys("email.com")
        self.assertEqual(len(phone), 1, "Phone input not found")
        if len(phone):
            phone[0].send_keys("123")
        self.assertEqual(len(adress), 1, "Adress input not found")
        if len(adress):
            adress[0].send_keys("home 123")
        browser.find_element_by_class_name("btn").click()


if __name__ == "__main__":
    unittest.main()
