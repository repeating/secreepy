import abc


class Web:
    def __init__(self):
        self.url = None
        self.page_source = None

    @abc.abstractmethod
    def get(self, url):
        pass

    @abc.abstractmethod
    def find_element_by_id(self, _id):
        pass

    @abc.abstractmethod
    def find_element_by_xpath(self, xpath):
        pass

    @abc.abstractmethod
    def find_elements_by_xpath(self, xpath):
        pass

    @abc.abstractmethod
    def find_elements_by_id(self, _id):
        pass

    @abc.abstractmethod
    def find_element_by_name(self, name):
        pass

    @abc.abstractmethod
    def refresh(self):
        pass

    @property
    @abc.abstractmethod
    def title(self):
        pass

    @property
    def current_url(self):
        return self.url
