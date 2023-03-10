from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
  #Use chrome driver to automate browser
driver = webdriver.Chrome(r"C:\Users\Wailo\Downloads\chromedriver_win32\chromedriver.exe")

  # Get url and open it
url  = "https://www.linkedin.com/home"
driver.get(url)
  # Automate email and password input
email = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")
email.send_keys("")
password.send_keys("")
  # wait
time.sleep(10)
  # Submit credentials
submit = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width").click()
  
  # wait
time.sleep(60)
  # Get search bar
search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
  #add input
search.send_keys("Software Engineer")
search.send_keys(Keys.ENTER)
time.sleep(10)

primary_filter = driver.find_element(By.ID, "search-reusables__filters-bar")
primary_filter_ul = primary_filter.find_element(By.TAG_NAME, "ul")
primary_filter_li = primary_filter_ul.find_elements(By.CLASS_NAME, "search-reusables__primary-filter")
people = primary_filter_li[1].click()
time.sleep(10)

# people_ul = driver.find_element(By.TAG_NAME, "ul")
people = driver.find_elements(By.CLASS_NAME, "reusable-search__result-container")

for person in people:
    print(person.text)
    person.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    modal = driver.find_element(By.CLASS_NAME, "artdeco-modal-overlay")
    send = modal.find_element(By.CLASS_NAME, "artdeco-button--primary")
    send.click()

    # person.find_element(By.CLASS_NAME, "artdeco-button__text").click()
    # time.sleep(5)
    # # addnote = driver.find_element(By.CLASS_NAME, "artdeco-button__text")
    # # addnote.click()
    # # time.sleep(2)
    # # message = driver.find_element(By.ID, "custom-message")
    # # message.send_keys("Hi, I will love to connect with you. Thanks!")
    # send = driver.find_element(By.LINK_TEXT, "Send")
    # send.click()
driver.quit()
