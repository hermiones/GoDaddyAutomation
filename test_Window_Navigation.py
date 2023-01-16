from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome("C:\\Users\\Reliance\\Downloads\\chromedriver\\chromedriver.exe")
    # go to the URL
    driver.get("https://www.godaddy.com/")

def test_maxWin():
    # Maximise the window size
    driver.maximize_window()

def test_minWin():
    # Minimize the window size
    driver.minimize_window()

def test_WinSize():
    # Set the window size to a perticular size
    driver.set_window_size(1920, 1080)

#fetch the driver size and print
size = driver.get_window_size()
print(size)

# close the  current window
driver.close()

# close the webdriver with all windows
driver.quit()
