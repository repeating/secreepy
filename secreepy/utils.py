import traceback
from time import sleep
from requests_html import HTMLSession
from urllib3.exceptions import MaxRetryError, ConnectionError
from secreepy.logger import Logger
from secreepy.exceptions import StatusCodeException


def get_request(URL, proxies=None, attempt=3):
    def _return(wait_time=1):
        if attempt:
            sleep(wait_time)
            return get_request(URL, proxies, attempt - 1)
        else:
            Logger().log(f'failed to GET request {URL}', error=True)
            print(traceback.format_exc())
            return None

    session = HTMLSession()
    try:
        response = session.get(URL, stream=True, proxies=proxies)
    except (MaxRetryError, ConnectionError):
        return _return()
    except:
        return _return()
    session.close()
    if response.status_code in [404, 500, 502, 503]:
        return _return()
    if response.status_code != 200:
        raise StatusCodeException(f'Requesting URL {URL} returned {response.status_code} response!')
    return response
