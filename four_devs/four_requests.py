from requests import get
from decouple import config
from bs4 import BeautifulSoup
from lxml import etree


class FourDevsRequests:
    def __init__(self):
        self._base_url = config("BASE_URL")

    def _access_page(self):
        return get(url=f"{self._base_url}/")

    @staticmethod
    def _find_links_and_names(html_page):
        _soup = BeautifulSoup(html_page, 'html.parser')
        _dom = etree.HTML(str(_soup))
        _xpath = '//div[contains(@class, "main-sidebar")]/ul[@id="top-nav"]/li[@role="menuitem"]/' \
                 'a[contains(@href, "gerador") or contains(@href, "validador")]'
        _elements = _dom.xpath(_xpath)
        return {_element.get("title"): _element.get("href") for _element in _elements}

    def get_options(self):
        response = self._access_page()
        return self._find_links_and_names(html_page=response.text)

    @staticmethod
    def show_options(options):
        for _index, _key, in enumerate(options.keys()):
            print(f"Número: {_index} - Opção: {_key}")
