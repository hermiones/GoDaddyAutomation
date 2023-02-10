from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\Reliance\\Downloads\\chromedriver\\chromedriver.exe")
# go to the URL
driver.get("https://www.godaddy.com/")

def test_1():
    # Maximise the window size
    driver.maximize_window()
    # Minimize the window size 
    driver.minimize_window()
    # Set the window size to a perticular Size
    driver.set_window_size(1920, 1080) 
    #fetch the driver size and Print..
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
    #assert driver.title in driver.page_source

def test_4_MenuLinks():
    driver.maximize_window
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#id-d6f9deab-d554-45df-a52c-8a9ab53948b5").click()
    driver.find_element_by_link_text("Domain Name Search").click()

def test_5_AssertTitle():
    if  ("GoDaddy Domain Search - Buy and Register Available Domain" in driver.title):
        print("PASS")
    else:
        print("Fail")

def test_6_Logo():
    driver.find_element_by_xpath("//header/div[@id='id-c65f43b6-16f4-4542-bb27-3c6a84de0d93']/div[1]/a[1]/*[1]").click()

def test_Final():
    #verifies whether the element is present or not
    search_box_display = driver.find_element_by_xpath("/html[1]/body[1]/section[2]/div[1]/form[1]/div[2]/span[1]/input[1]").is_displayed()
    print(search_box_display)
    #verifies whether the element is displayed or not
    search_box_enable = driver.find_element_by_xpath("/html[1]/body[1]/section[2]/div[1]/form[1]/div[2]/span[1]/input[1]").is_enabled()
    print(search_box_enable)