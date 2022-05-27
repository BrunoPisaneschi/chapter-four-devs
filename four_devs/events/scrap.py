from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class GeradorOnlinedeContaBancaria:
    def __init__(self, **kwargs):
        self._driver = kwargs.get("driver")
        self._ac = ActionChains(self._driver)
        self._base_url = kwargs.get("base_url")
        self._partial_link = kwargs.get("partial_link")
        self._extras = kwargs.get("extras")

    def _access_page(self):
        self._driver.get(f"{self._base_url}{self._partial_link}")

    def _show_list_bank(self):
        _banks = self._driver.find_elements(By.XPATH, '//select[@id="cc_banco"]/option')
        list(map(lambda _bank: print(f"Número: {_bank.get_attribute('value') or None} - Banco: {_bank.text}"), _banks))

    def _select_bank(self):
        self._show_list_bank()
        _bank = input("\nSelecione o número do banco! Caso seja indiferente, aperte qualquer tecla.\n")
        if _bank:
            _select_bank = Select(self._driver.find_element(By.XPATH, '//select[@id="cc_banco"]'))
            _select_bank.select_by_value(_bank)

    def _show_list_state(self):
        _states = self._driver.find_elements(By.XPATH, '//select[@id="cc_estado"]/option')
        list(map(lambda _state: print(f"Estado: {_state.get_attribute('value')}"), _states))

    def _select_state(self):
        self._show_list_state()
        _state = input("\nSelecione a sigla do estado! Caso seja indiferente, aperte qualquer tecla.\n")
        if _state:
            _select_state = Select(self._driver.find_element(By.XPATH, '//select[@id="cc_estado"]'))
            _select_state.select_by_value(_state.upper())

    def _click_generate(self):
        _button_generate = self._driver.find_element(By.ID, "btn_gerar_conta")
        self._ac.click(_button_generate).perform()

    def _capture_result(self):
        return {
            'conta_corrente': self._driver.find_element(By.XPATH, '//div[@id="conta_corrente"]').text,
            'agencia': self._driver.find_element(By.XPATH, '//div[@id="agencia"]').text,
            'banco': self._driver.find_element(By.XPATH, '//div[@id="banco"]').text,
            'cidade': self._driver.find_element(By.XPATH, '//div[@id="cidade"]').text,
            'estado': self._driver.find_element(By.XPATH, '//div[@id="estado"]').text,
        }

    def _loading(self):
        _attempts = 0
        _flag_generating = False
        _attribute_disabled_after = False
        while _attempts <= 20 and not _flag_generating:
            _button_generate = self._driver.find_element(By.XPATH, '//input[@type="button"]')
            _attribute_disabled = _button_generate.get_attribute("disabled")
            if _attribute_disabled:
                _attribute_disabled_after = True
            if _attribute_disabled_after:
                _flag_generating = True
            sleep(0.5)
            _attempts += 1

    def execute(self):
        self._access_page()
        self._select_bank()
        self._select_state()
        self._click_generate()
        self._loading()
        return self._capture_result()


class ValidadorOnlinedeContaBancaria:
    def __init__(self, **kwargs):
        self._driver = kwargs.get("driver")
        self._ac = ActionChains(self._driver)
        self._base_url = kwargs.get("base_url")
        self._partial_link = kwargs.get("partial_link")
        self._extras = kwargs.get("extras")

    def _access_page(self):
        self._driver.get(f"{self._base_url}{self._partial_link}")

    def _show_list_bank(self):
        _banks = self._driver.find_elements(By.XPATH, '//select[@id="cc_banco"]/option')
        list(map(lambda _bank: print(f"Número: {_bank.get_attribute('value') or None} - Banco: {_bank.text}"), _banks))

    def _select_bank(self):
        _bank = self._extras.get("banco")
        while not _bank:
            self._show_list_bank()
            _bank = input("\nSelecione o número do banco!\n")
        _select_bank = Select(self._driver.find_element(By.XPATH, '//select[@id="cc_banco"]'))
        _select_bank.select_by_visible_text(_bank)

    def _type_agency(self):
        _agency = self._extras.get("agencia")
        if not _agency:
            _agent = input("\nDigite os números da agência:\n")
        self._driver.find_element(By.ID, 'txt_agencia').send_keys(_agency)

    def _type_account_with_digit(self):
        _account = self._extras.get("conta_corrente")
        if not _account:
            _account = input("\nDigite os números da conta com o dígito verificador:\n")
        self._driver.execute_script(f"document.getElementById('txt_conta').value = '{_account}'")

    def _click_validate(self):
        self._driver.execute_script("document.getElementById('btn_gerar_conta').click();")

    def _loading(self):
        _attempts = 0
        _text_area_content = None
        while _attempts <= 20 and not _text_area_content:
            try:
                _text_area_content = self._driver.find_element(By.XPATH, '//textarea[@id="texto_resposta"]').text
            except NoSuchElementException:
                _text_area_content = None
            sleep(0.5)
            _attempts += 1

    def _capture_result(self):
        _text_area_element = self._driver.find_element(By.XPATH, '//textarea[@id="texto_resposta"]').text
        if 'Conta Invalida' not in _text_area_element:
            _bank, _agency, _account, _is_valid = _text_area_element.split(' - ')
            return {
                "banco": _bank,
                "agencia": _agency,
                "conta_corrente": _account,
                "conta_valida": True
            }
        else:
            return {
                "conta_valida": False
            }

    def execute(self):
        self._access_page()
        self._select_bank()
        self._type_agency()
        self._type_account_with_digit()
        self._click_validate()
        self._loading()
        return self._capture_result()
