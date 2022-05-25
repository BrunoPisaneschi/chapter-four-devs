from os.path import join, abspath, dirname

from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class FourDevsSelenium:
    def __init__(self, option_events):
        self._base_url = config("BASE_URL")
        self._root_dir = dirname(abspath("driver"))
        self._chrome_path = join(self._root_dir, 'driver', 'chromedriver')
        self._option_events = option_events

    @staticmethod
    def _configure_driver():
        _options = Options()
        _options.add_argument("start-maximized")
        return _options

    def execute(self, _option):
        _chrome_options = self._configure_driver()

        with webdriver.Chrome(service=Service(executable_path=self._chrome_path), options=_chrome_options) as _driver:
            _wait = WebDriverWait(_driver, 10)
            _wait_not = WebDriverWait(_driver, 60)
            _driver.get(f"{self._base_url}{list(self._option_events.items())[_option][1]}")
