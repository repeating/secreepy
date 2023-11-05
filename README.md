# Secreepy

Secreepy is a Python library for web scrapping. 
It's crafted to make it easy to parse webpages using web drivers or simple get requests, and smoothly handle
errors that could appear during the scrapping process.

## How to Install

Installing Secreepy is straightforward; you can install it using pip, a package installer for Python.

```bash
pip install secreepy
```

## Getting Started
```python
from secreepy import Html, UndetectedChromeDriver, FirefoxDriver

# Choose the method you want
web = UndetectedChromeDriver(timeout=10, headless=False, verbos=1)
# web = FirefoxDriver(timeout=10, headless=False)
# web = Html()

# get the webpage
web.get('https://simple.wikipedia.org/wiki/List_of_countries')

# find all needed web elements using xpath
xpath = '//div[@class="mw-parser-output"]//p/span/following-sibling::a'
elements = web.find_elements_by_xpath(xpath)

# print all countries from the WikiPedia page
for element in elements:
    print(element.text)
```

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. 

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/repeating/secreepy/blob/main/LICENSE) file for details.