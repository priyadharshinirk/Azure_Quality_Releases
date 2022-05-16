# #!/usr/bin/env python
from lib2to3.pgen2 import driver
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (driver,user, password):
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    time.sleep(10)
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    product_heading=driver.find_element_by_class_name("title").text
    print("product test "+product_heading )
    assert "PRODUCTS" in product_heading
    print("user logged in successfully")


def add_items_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"  
        driver.find_element_by_css_selector(element).click()  
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click()  
        product = driver.find_element_by_css_selector("div[class='inventory_details_name large_size']").text  
        print(product + " added to shopping cart.")  
        driver.find_element_by_id("back-to-products").click()  
    print('{:d} items are all added to shopping cart successfully.'.format(n_items))

def remove_items(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"  
        driver.find_element_by_css_selector(element).click()  
        driver.find_element_by_css_selector("button.btn_small.btn_inventory").click() 
        product = driver.find_element_by_css_selector("div[class='inventory_details_name large_size']").text  
        print(product + " removed from shopping cart.")  
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()  
    print('{:d} items are removed from shopping cart successfully.'.format(n_items))

if __name__ == "__main__":
    print ('Starting the browser...')
    num_items=6
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    # driver=webdriver.Chrome()
    login(driver,'standard_user', 'secret_sauce')
    add_items_cart(driver,num_items)
    remove_items(driver,num_items)


