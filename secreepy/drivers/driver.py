import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from urllib3.exceptions import MaxRetryError, ProtocolError
from secreepy.config import DRIVER_DECORATOR_TIMEOUT
from secreepy import Web, decorators, Logger


class DriverElement:
    def __init__(self, el):
        if isinstance(el, DriverElement):
            self.el = el.el
        else:
            self.el = el

    @property
    def text(self):
        ret = self.el.text
        while len(ret) and (ret[0] == '\n' or ret[0] == ' '):
            ret = ret[1:]
        while len(ret) and (ret[-1] == '\n' or ret[-1] == ' '):
            ret = ret[: -1]
        return ret

    def get_attribute(self, attribute):
        return self.el.get_attribute(attribute)

    def click(self):
        self.el.click()

    def clear(self):
        self.el.clear()

    def send_keys(self, keys):
        self.el.send_keys(keys)

    @property
    def location(self):
        return self.el.location


class Driver(Web):
    def __init__(self, timeout=DRIVER_DECORATOR_TIMEOUT, headless=False, verbos=0, profile=None, proxy=None, executable_path=None):
        super().__init__()
        self.timeout = timeout
        self.timeout_backup = timeout
        self.headless = headless
        self.profile = profile
        self.proxy = proxy
        self.executable_path = executable_path
        self.wde_counter = 0
        self.logger = Logger(verbos)
        self.driver = self.get_driver()

    def __del__(self):
        try:
            self.driver.quit()
        except:
            pass

    @decorators.timeout(DRIVER_DECORATOR_TIMEOUT, exception=TimeoutException)
    def _get_driver(self):
        pass

    def get_driver(self):
        while True:
            try:
                return self._get_driver()
            except:
                time.sleep(0.1)
                self.logger.log('Getting a driver failed. Trying to get a new driver..')
                self.logger.log(traceback.format_exc(), debug=True)
                self.quit()

    def update_driver(self):
        time.sleep(0.1)
        self.logger.log('Updating driver', debug=True)
        self.quit()
        self.driver = self.get_driver()

    @decorators.timeout(DRIVER_DECORATOR_TIMEOUT, exception=TimeoutException)
    def full_load(self):
        cnt = 0
        while True:
            try:
                if len(self.find_elements_by_xpath('//div')) > 0:
                    break
            except:
                pass
            time.sleep(0.1)
            cnt += 1
            if cnt == 100:
                cnt = 0
                self.logger.log('refreshing..', debug=True)
                self.get(self.url)

    @decorators.timeout(DRIVER_DECORATOR_TIMEOUT, exception=TimeoutException)
    def get(self, url):
        self.url = url
        try:
            self.driver.get(url)
        except TimeoutException:
            self.logger.log(f'{url} timed out', error=True, debug=True)
        except (MaxRetryError, ProtocolError):
            self.logger.log(f'MaxRetry/Protocol error {url}', debug=True)
            time.sleep(1)
            self.get(url)
        except WebDriverException:
            self.logger.log('Web driver exception. Repeating', debug=True)
            time.sleep(1)
            self.wde_counter += 1
            if self.wde_counter == 5:
                self.update_driver()
                self.wde_counter = 0
            self.get(url)
        except Exception as e:
            self.logger.log('You need to take care of this error', error=True)
            self.logger.log(traceback.format_exc())
            raise e
        self.full_load()

    def delete_all_cookies(self):
        self.logger.log('deleting cookies', debug=True)
        self.driver.delete_all_cookies()

    def execute_script(self, script):
        self.logger.log('executing script', script, debug=True)
        self.driver.execute_script(script)

    def find_element_by_id(self, _id):
        return DriverElement(WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.ID, _id))))

    def find_element_by_xpath(self, xpath):
        return DriverElement(WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, xpath))))

    def find_elements_by_xpath(self, xpath):
        return [DriverElement(el) for el in self.driver.find_elements(By.XPATH, xpath)]

    def find_elements_by_id(self, _id):
        return [DriverElement(el) for el in self.driver.find_elements(By.ID, _id)]

    def find_element_by_name(self, name):
        return DriverElement(WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.NAME, name))))

    def click_by_xpath(self, xpath):
        self.find_element_by_xpath(xpath).click()

    def click_by_id(self, _id):
        self.find_element_by_id(_id).click()

    def send_keys_by_id(self, _id, keys):
        element = self.find_element_by_id(_id)
        element.clear()
        element.send_keys(keys)

    def send_keys_by_name(self, name, keys):
        element = self.find_element_by_name(name)
        element.clear()
        element.send_keys(keys)

    def scroll_to_element(self, element):
        x = element.location['x']
        y = element.location['y']
        self.driver.execute_script(f'window.scrollTo({x},{y});')

    def scroll_to_bottom(self, steps=1):
        for i in range(1, 1 + steps):
            self.driver.execute_script(f"window.scrollTo(0, parseInt({i} * document.body.scrollHeight / {steps}));")
            time.sleep(0.05)

    def scroll_down(self, pixels):
        self.driver.execute_script(f'window.scrollBy(0,{pixels})')

    def quit(self):
        try:
            self.driver.quit()
        except:
            pass

    def refresh(self):
        self.driver.refresh()

    def alert(self):
        self.execute_script("alert('Test')")
        while True:
            try:
                self.driver.switch_to.alert.accept()
            except:
                break

    @property
    def current_url(self):
        return self.driver.current_url

    @property
    def title(self):
        return self.driver.title

    @property
    def page_source(self):
        if self.driver:
            return self.driver.page_source
        else:
            return None
