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
    driver.refresh()
    


def test_2():
    driver.get("https://www.godaddy.com/")
    # print page title
    print("The page title is :: ",driver.title)
    #print current url
    print(driver.current_url)
    
def test_3():
    #Get Title of page and validate it with expected value.
    assert "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy IN" in driver.title
    #Get url of page and validate it with expected value.
    assert "https://www.godaddy.com/en-in" in driver.current_url
    #Get page source of page and validate that title is present
    assert driver.title in driver.page_source