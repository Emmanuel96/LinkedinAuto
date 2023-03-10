from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

# Use chrome driver to automate browser
driver = webdriver.Chrome(
    r"C:\Users\Wailo\Downloads\chromedriver_win32\chromedriver.exe"
)

# Get url and open it
url = "https://www.linkedin.com/home"
driver.get(url)
# Automate email and password input
email = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")
email.send_keys("xoxxworld@gmail.com")
password.send_keys("@s?XmJ-B5Rpb92u")
# wait
time.sleep(10)
# Submit credentials
submit = driver.find_element(
    By.CLASS_NAME, "sign-in-form__submit-btn--full-width"
).click()

# wait
time.sleep(60)
# Get search bar
search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
# add input
search.send_keys("Python Engineer")
search.send_keys(Keys.ENTER)
time.sleep(10)

primary_filter = driver.find_element(By.ID, "search-reusables__filters-bar")
primary_filter_ul = primary_filter.find_element(By.TAG_NAME, "ul")
primary_filter_li = primary_filter_ul.find_elements(
    By.CLASS_NAME, "search-reusables__primary-filter"
)
people = primary_filter_li[0]
people.click()
time.sleep(10)

all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for job in all_jobs:
    print(job.text)
    job.click()
    time.sleep(10)
    try:
      apply_button = driver.find_element(By.CSS_SELECTOR, ".job-s-apply button")
      apply_button.click()
      time.sleep(5)
      phone = driver.find_element(By.CSS_SELECTOR, "fb-single-line-text__input")
      phone.send_keys("08104394359")
      next = driver.find_element(By.CSS_SELECTOR, "footer button")
      next.click()
      time.sleep(5)
      review = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
      if review.get_attribute("data-control-name") == "continue unify":
          close = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
          close.click()
          time.sleep(5)
          discard = driver.find_elements(
              By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn"
          )[1]
          discard.click()
          print("ooop!!!")
          continue
      else:
          review.click()
          time.sleep(5)
          submitbtn = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
          if submitbtn.get_attribute("data-control-name") == "submit_unify":
              submitbtn.click()
              time.sleep(5)
              close = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
              close.click()
          else:
              close = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
          close.click()
          time.sleep(5)
          discard = driver.find_elements(
              By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn"
          )[1]
          discard.click()
          print("ooop!!!")
          continue
    except NoSuchElementException:
        print("No such element")
        continue
