from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\Reliance\\Downloads\\chromedriver\\chromedriver.exe")
# go to the URL
driver.get("https://www.godaddy.com/")

def test_1():
    # Maximise the window size
    driver.maximize_window()
    # Minimize the window size
    driver.minimize_window()
    # Set the window size to a perticular size
    driver.set_window_size(1920, 1080)
    #fetch the driver size and print
    size = driver.get_window_size()
    print("The current window size is",size)
    # close the  current window
    #driver.close()


