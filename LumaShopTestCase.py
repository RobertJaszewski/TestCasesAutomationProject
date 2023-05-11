import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#TEST DATA
email = "automationtester223@gmail.com"
lastName = "Smith"
firstName = "John"

class RegistrationOfNewUser(unittest.TestCase):
    def setUp(self):
        # PRECONDITIONS
        # 1. Browser open
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 2. Main page open
        self.driver.get('https://magento.softwaretestingboard.com/')
        # 3. User is not logged in
        self.driver.implicitly_wait(10)
    def testCaseRegistrationWithEmptyPassword(self):
        # STEPS
        # 1. Click on "Sign In"
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        # 2. Click on "Create an Account" blue button
        self.driver.find_element(By.LINK_TEXT, "Create an Account").click()
        # 4. Enter First Name
        self.driver.find_element(By.ID, "firstname").send_keys(firstName)
        # 5. Enter Last Name
        self.driver.find_element(By.ID, "lastname").send_keys(lastName)
        # 6. Enter Email
        self.driver.find_element(By.ID, 'email_address').send_keys(email)
        # WARNING! Only for negative test case's
        # 7. Click on "Create an Account" blue button
        self.driver.find_element(By.CSS_SELECTOR, 'button[title="Create an Account"]').click()

        # EXPECTED RESULTS
        # The user receives the information: "This is a required field." under the "password" and "confirm password" field
        # 1. Looking for alert "This is a required field." under password field
        alertThisIsARequiredField1 = self.driver.find_element(By.CSS_SELECTOR, 'div#password-error')
        self.assertTrue(alertThisIsARequiredField1.is_displayed())
        print("Assertion 1 correct")
        # 2. Looking for alert "This is a required field." under confirm password field.
        alertThisIsARequiredField2 = self.driver.find_element(By.CSS_SELECTOR, 'div#password-confirmation-error')
        self.assertTrue(alertThisIsARequiredField2.is_displayed())
        print("Assertion 2 correct")
        sleep(5)

    def tearDown(self):
        # End of test
        self.driver.quit()
        # FINAL CONDITIONS
        # 1. Account is not created
