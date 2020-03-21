from selenium import webdriver
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager as fox
from webdriver_manager.chrome import ChromeDriverManager as chrome


class FbBot:

    def __init__(self, username, password, pagename, d=None):
        if d == 1:
            self.driver = webdriver.Chrome(
                executable_path=chrome().install())
        else:
            self.driver = webdriver.Firefox(
                executable_path=fox().install())

        self.fblogin(username, password)
        print("Login Done")
        self.latestpostlike(pagename)
        print("latest post liked")

    def fblogin(self, username, password):
        self.driver.get("https://www.facebook.com/")
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="email"]').send_keys(username)
        self.driver.find_element_by_xpath(
            '//*[@id="pass"]').send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@value="Log In"]').click()
        sleep(2)

    def latestpostlike(self, pagename):

        self.driver.find_element_by_xpath(
            "//input[@placeholder='Search']").send_keys(pagename)
        sleep(2)
        self.driver.find_element_by_css_selector("._4w98").click()
        sleep(3)
        self.driver.find_element_by_css_selector("._6xu6").click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 800)")
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div/a").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[29]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/form/div[2]/div/div[2]/div[2]/span[1]/div/div/a").click()


if __name__ == "__main__":
    print("Welcome To Simple fb Bot")
    username = input("Enter the Facebook Username: ")
    password = input("Enter the Facebook Password: ")
    page = input("Enter the Page Name you want to like the latest post: ")
    s = int(input("Choose \n 1.Chrome \n 2. Firefox \n"))
    print("started")
    x = FbBot(username, password, page, s)
    print("Done")
