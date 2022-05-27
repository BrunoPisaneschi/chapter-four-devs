from os.path import join, abspath, dirname
from importlib import import_module
from pprint import pprint

from unidecode import unidecode
from decouple import config
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class FourDevsSelenium:
    def __init__(self, option_events):
        self._root_dir = dirname(abspath("driver"))
        self._chrome_path = join(self._root_dir, 'driver', 'chromedriver')
        self._option_events = option_events

    @staticmethod
    def _configure_driver():
        _chrome_options = Options()
        _chrome_options.add_argument("start-maximized")
        return _chrome_options

    def _get_class_by_event(self, _event_option):
        _scrap_module = import_module('four_devs.events.scrap')
        return getattr(_scrap_module, unidecode(list(self._option_events.items())[_event_option][0].replace(" ", "")))

    def _get_partial_link_by_event(self, _event_option):
        return list(self._option_events.items())[_event_option][1]

    def execute(self, _event_option, _response):
        _chrome_options = self._configure_driver()
        with Chrome(service=Service(executable_path=self._chrome_path), options=_chrome_options) as _driver:
            _wait = WebDriverWait(_driver, 10)
            _partial_link = self._get_partial_link_by_event(_event_option=_event_option)
            _selenium_class = self._get_class_by_event(_event_option=_event_option)
            _kwargs = {
                "driver": _driver,
                "base_url": config("BASE_URL"),
                "partial_link": _partial_link,
                "extras": _response
            }
            return _selenium_class(**_kwargs).execute()

