from . import Driver
import undetected_chromedriver as uc


class UndetectedChromeDriver(Driver):
    def _get_driver(self):
        self.timeout = self.timeout_backup
        options = uc.ChromeOptions()
        options.add_argument('--disable-browser-side-navigation')
        if self.headless:
            options.add_argument('--headless')
        if self.executable_path is not None:
            driver = uc.Chrome(use_subprocess=True, user_data_dir=self.profile,
                               options=options, driver_executable_path=self.executable_path)
        else:
            driver = uc.Chrome(use_subprocess=True, user_data_dir=self.profile, options=options)
        driver.set_page_load_timeout(self.timeout)
        driver.set_script_timeout(self.timeout)
        driver.implicitly_wait = self.timeout
        main_page = driver.window_handles[0]
        driver.switch_to.window(main_page)
        driver.maximize_window()
        return driver
