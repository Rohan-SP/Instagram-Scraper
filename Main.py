from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstaSpider:

    def __init__(self, Username, Password):

        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

        # To Let Program account for slow internet
        self.driver.implicitly_wait(5)

        # Goes to Instagram site
        self.driver.get("https://www.instagram.com/")
        # Types in username
        self.driver.find_element_by_name("username").send_keys(Username)
        # Types in password
        self.driver.find_element_by_name("password").send_keys(Password)
        # Clicks login
        self.driver.find_element_by_xpath('//button/div[text()="Log In"]').click()
        # Clicks "Not Now"
        self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        # Clicks "Not Now"
        # self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()

    # Goes through the entire OS system looking for the given file name, returns the address of the file to be accessed
    @staticmethod
    def find_file(filename):
        for root, dirs, files in os.walk('/Users/'):
            if filename in files:
                return os.path.join(root, filename)
        return False

    # Searches in user system for the location of chromedriver.exe, returns the path to the file if in the user system
    @staticmethod
    def get_chromedriver_location():
        chrome_location = find_file('chromedriver.exe')

        # if statement, in case there is no chromedriver.exe within system
        if not chrome_location:
            print('No chromdriver.exe installed')
            return False

        return chrome_location

    @staticmethod
    def open_driver(location):
        # first checks if location given is the right location of ChromeDriver.exe
        try:

            func_driver = webdriver.Chrome(executable_path="{}".format(location))
            func_driver.implicitly_wait(5)
            return func_driver

        # location given is invalid (Chromedriver in wrong place or does not exist)
        except selenium.common.exceptions.WebDriverException:
            # checks if there is a ChromeDriver in the system
            location = get_chromedriver_location()

            # If there's no ChromeDriver then returns error
            if not location:
                print("Chrome Driver Not Found")
                return

            # if there is a ChromeDriver in the system then returns a driver object with the right location of file
            else:
                print("Copy loaction path when using open_driver for faster load up time")
                print("Here copy and paste this: {}".format(location))
                func_driver = webdriver.Chrome(executable_path="{}".format(location))
                func_driver.implicitly_wait(5)
                return func_driver

    def go_to_page(self, page_username):
        if self.driver.current_url != 'https://www.instagram.com/{}/'.format(page_username):
            self.driver.get('https://www.instagram.com/{}/'.format(page_username))

        # driver.get("https://www.instagram.com/{}/".format(page_username))
        info = self.driver.find_elements_by_class_name('Y8-fY ')

        # formats info to return onlly the int values
        posts = info[0].text[:info[0].text.find(" ")]
        followers = info[1].text[:info[1].text.find(" ")]
        following = info[2].text[:info[2].text.find(" ")]
        # Returns strings because it could have commas
        return posts, followers, following

    # Made for incase a object needs to be force closed
    def driver_quit(self):
        self.driver.quit()

    # Place holder in case i wanna make a static method
    @staticmethod
    def lol():
        print("lol")

    # Deactivate when fixing bugs with #'s
    def __del__(self):
        self.driver.close()
        print("deleted")
