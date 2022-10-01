from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# By default this env variable is not set.
# In the Dockerfile we set this as True to be able to identify when
# the script is running inside a container.
RUNNING_IN_CONTAINER = os.environ.get('RUNNING_IN_CONTAINER', False)


def main():
    print("Starting app")

    chrome_options = Options()

    if RUNNING_IN_CONTAINER:
        # Only apply these settings when running inside a container
        # It makes for example debugging easier if not run in headless-mode
        print("Running in a container")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)
    driver.get("https://google.com")
    driver.find_element(By.XPATH, "//button[@id='W0wltc']").click() # reject cookies
    for _ in range(5):
        print(driver.find_element(By.XPATH, "//*[@name='q']").get_attribute("title")) # print title of serach button
        time.sleep(3)


if __name__=="__main__":
    main()
