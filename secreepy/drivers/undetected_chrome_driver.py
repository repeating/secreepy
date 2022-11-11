from . import Driver
import seleniumwire.undetected_chromedriver as uc


class UndetectedChromeDriver(Driver):
    def _get_driver(self):
        self.timeout = self.timeout_backup
        options = uc.ChromeOptions()
        options.add_argument('--disable-browser-side-navigation')
        if self.headless:
            options.add_argument('--headless')
        args = {
            'use_subprocess': True,
            'user_data_dir': self.profile,
            'options': options,
        }
        if self.executable_path is not None:
            args['driver_executable_path'] = self.executable_path
        if self.proxy is not None:
            args['seleniumwire_options'] = {
                'proxy': {
                    'http': self.proxy,
                    'https': self.proxy,
                }
            }
        driver = uc.Chrome(**args)
        driver.set_page_load_timeout(self.timeout)
        driver.set_script_timeout(self.timeout)
        driver.implicitly_wait = self.timeout
        main_page = driver.window_handles[0]
        driver.switch_to.window(main_page)
        driver.maximize_window()
        return driver
