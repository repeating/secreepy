from . import Driver
from seleniumwire import webdriver
import os


class FirefoxDriver(Driver):
    def _get_driver(self):
        self.timeout = self.timeout_backup
        options = webdriver.FirefoxOptions()
        options.add_argument('--disable-browser-side-navigation')
        if self.headless:
            options.add_argument('--headless')
        if self.profile is not None:
            os.makedirs(self.profile, exist_ok=True)
            options.add_argument('--profile')
            options.add_argument(self.profile)
        args = {
            'options': options,
        }
        if self.executable_path is not None:
            args['executable_path'] = self.executable_path
        if self.proxy is not None:
            args['seleniumwire_options'] = {
                'proxy': {
                    'http': self.proxy,
                    'https': self.proxy,
                }
            }
        driver = webdriver.Firefox(**args)
        driver.set_page_load_timeout(self.timeout)
        driver.set_script_timeout(self.timeout)
        driver.implicitly_wait = self.timeout
        main_page = driver.window_handles[0]
        driver.switch_to.window(main_page)
        driver.maximize_window()
        return driver
