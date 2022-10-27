from . import Driver
from selenium import webdriver
import os


class FirefoxDriver(Driver):
    def _get_driver(self):
        self.timeout = self.timeout_backup
        options = webdriver.FirefoxOptions()
        options.add_argument('--disable-browser-side-navigation')
        if self.headless:
            options.add_argument('--headless')
        if self.profile:
            os.makedirs(self.profile, exist_ok=True)
            options.add_argument('--profile')
            options.add_argument(self.profile)
        driver = webdriver.Firefox(options=options)
        driver.set_page_load_timeout(self.timeout)
        driver.set_script_timeout(self.timeout)
        driver.implicitly_wait = self.timeout
        main_page = driver.window_handles[0]
        driver.switch_to.window(main_page)
        driver.maximize_window()
        return driver
