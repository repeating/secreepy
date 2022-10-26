from secreepy import Web, utils


class HtmlElement:
    def __init__(self, el):
        if isinstance(el, HtmlElement):
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
        return self.el.attrs[attribute]


class Html(Web):
    def __init__(self, proxies=None):
        super().__init__()
        self.html = None
        self.proxies = proxies

    def get(self, url):
        self.html = None
        self.page_source = None
        response = utils.get_request(url, proxies=self.proxies)
        if response:
            self.html = response.html
            self.page_source = response.text
        self.url = url

    def find_element_by_id(self, _id):
        return self.find_element_by_xpath(f'//*[@id="{_id}"]')

    def find_element_by_xpath(self, xpath):
        return HtmlElement(self.html.xpath(xpath)[0])

    def find_elements_by_xpath(self, xpath):
        return [HtmlElement(el) for el in self.html.xpath(xpath)]

    def find_elements_by_id(self, _id):
        return self.find_elements_by_xpath(f'//*[@id="{_id}"]')

    def find_element_by_name(self, name):
        return self.find_element_by_xpath(f'//*[@name="{name}"]')

    def refresh(self):
        self.get(self.url)

    @property
    def title(self):
        return self.find_element_by_xpath('//title').text

    def quit(self):
        pass
