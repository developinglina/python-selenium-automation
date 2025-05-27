from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

sleep(15)

# Test Case: Users can navigate to SignIn page

# Open https://www.target.com/
driver.get('https://www.target.com/')

# Click Account button
# id="account-sign-in"
driver.find_element(By.ID, 'account-sign-in').click()
sleep(5)

# Click SignIn btn from side navigation
# data-test="accountNav-signIn"
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(15)

# Verify SignIn page opened
expected_text = "Sign in or create account"
text = driver.find_element(By.XPATH, '//h1[text()="Sign in or create account"]').text
sleep(15)
print(text)
assert expected_text in text

print('test case passed')

# Practice with locators.

# Amazon logo :  driver.find_element(By.XPATH, '//i[role="presentation"]')

# Email field :   driver.find_element(By.ID, 'ap_email')

# Continue button : driver.find_element(By.ID, 'continue')

# Conditions of use link :  driver.find_element(By.XPATH, '//a[text()="Conditions of Use"]')

# Privacy Notice link : driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]')

# Need help link : driver.find_element(By.XPATH, '//span[class="a-expander-prompt"]')

# Forgot your password link : driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link : driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button :  driver.find_element(By.ID, 'createAccountSubmit')
