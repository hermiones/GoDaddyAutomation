from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\Reliance\\Downloads\\chromedriver\\chromedriver.exe")

# Open first window and go to the url
driver.get("https://www.google.com")

# Open second window and
driver.execute_script("window.open('');")

# Open second window and go to the url2
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.facebook.com")