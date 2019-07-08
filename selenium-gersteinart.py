from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

browser = webdriver.Chrome('/Users/yuvigerstein/Downloads/chromedriver')


class Browse:
    ''' This opens a web browser and performs tests on it by adding items to cart and
    taking screenshots of the website automatically '''

    def __init__(self):
        print("Browser Initialized")

    def open_browser(self):
        browser.get('https://www.gersteinart.com/')

    def search_product(self):
        small_objects = ['armstrong', 'weekend ride', 'heads', 'tulips', 'window', 'champion', 'brush', 'fruit', 'art',
                         'butterfly', 'hadar', 'donkey', 'metal flowers']
        random_piece = random.choice(small_objects) # generate a random piece to search
        searchbar = browser.find_element_by_id("search")  # find the search bar
        searchbar.clear()  # clear search bar before searching
        searchbar.send_keys(random_piece)  # enter a search term to be checked
        searchbar.send_keys(Keys.ENTER)  # simulate pressing enter


    def addtocart_product_page(self):
        addToCart = browser.find_element_by_css_selector('#layer-product-list > div > div.products.'
                                                         'wrapper.grid.columns3.products-grid > ol > li > div >'
                                                         ' div.product.details.product-item-details > '
                                                         'div.product-item-inner > div > div > form > button > span')
        addToCart.click()
        time.sleep(5)
        print("product added")


    def blog(self):
        goToBlog = browser.find_element_by_link_text('Blog')
        goToBlog.click()

    def quit_browser(self):
        browser.quit()


gerstein = Browse() # an instance of gerstein class

gerstein.open_browser()  # Open a Chrome browser
gerstein.search_product()  # search a random product
gerstein.addtocart_product_page()
time.sleep(10)



gerstein.search_product()  # search a random product
gerstein.addtocart_product_page()
time.sleep(10)


gerstein.search_product()  # search a random product
gerstein.addtocart_product_page()
time.sleep(10)

browser.save_screenshot('GersteinART_test.png')  # screenshot save
time.sleep(1)
print("All products have been added to cart successfully")
print("Quiting Browser")

gerstein.quit_browser()  # quit browser


