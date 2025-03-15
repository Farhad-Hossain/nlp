from selenium import webdriver

class Crowler():
    def __init__(self, url, browser='chrome'):
        self.url = url
        self.browser = browser

        if self.browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=options)
        elif self.browser == 'safari':
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()

        self.driver.set_page_load_timeout(30)  # Set timeout to 30 seconds
        self.driver.implicitly_wait(10)  # Implicit wait for elements to load

        self.driver.get(url)
        self.data = self.driver

    def teardown(self):
        self.driver.quit()
        print('Test Completed')
