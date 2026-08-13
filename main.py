import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Botón para solicitar taxi
    taxi_button = (
        By.CSS_SELECTOR,
        'button.button.round')

    # Tarifa Comfort
    comfort_button = (
        By.XPATH,
        '//div[contains(@class, "tcard") '
        'and .//div[normalize-space()="Comfort"]]'
    )

    # Teléfono
    phone_number_button = (
        By.CLASS_NAME,
        'np-button')

    phone_number_field = (
        By.XPATH,
        '//input[@id="phone"]'
    )
    next_button = (
        By.XPATH,
        '(//button[@class="button full"])[1]'
    )
    phone_code_field = (
        By.XPATH,
        '//input[@id="code" and @class="input"]'
    )

    confirm_button = (
        By.XPATH,
        '//button[@class="button full" and normalize-space()="Confirmar"]'
    )

    payment_method_button = (
        By.CLASS_NAME,
        'pp-button'
    )

    add_card_button = (
        By.XPATH,
        '//div[contains(text(), "Agregar tarjeta")]'
    )

    card_number_field = (
        By.ID,
        'number'
    )

    card_code_field = (
        By.CSS_SELECTOR,
        'input#code.card-input'
    )

    link_card_button = (
        By.XPATH,
        '//button[@class="button full" and normalize-space()="Agregar"]'
    )

    close_payment_button = (
        By.CSS_SELECTOR,
        '.payment-picker .close-button'
    )

    #mensaje para el conductor
    message_for_driver_field = (
        By.ID,
        'comment'
    )

    # agrega manta y pañuelos
    blanket_and_handkerchiefs_switch = (
        By.XPATH,
        "//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']"
    )

    blanket_and_handkerchiefs_checkbox = (
        By.XPATH,
        "//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']//input[@class='switch-input']"
    )

    ice_cream_plus_button = (
        By.XPATH,
        '//div[.//*[normalize-space()="Helado"]]'
        '//div[contains(@class, "counter-plus")]'
    )

    ice_cream_counter = (
        By.XPATH,
        '//div[.//*[normalize-space()="Helado"]]'
        '//div[contains(@class, "counter-value")]'
    )

    order_taxi_button = (
        By.XPATH,
        '//button[contains(@class, "smart-button")]'
    )

    order_modal = (
        By.CLASS_NAME,
        'order-body'
    )

    driver_rating = (
        By.CLASS_NAME,
        'order-btn-rating'
    )

    def select_taxi(self):
        taxi_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.taxi_button)
        )
        taxi_button.click()

    def select_comfort(self):
         comfort = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.comfort_button)
         )
         comfort.click()

    def set_phone_number(self, phone_number):
        phone_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.phone_number_button
            )
        )
        phone_button.click()

        phone_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.phone_number_field
            )
        )
        phone_field.send_keys(phone_number)

        next_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.next_button
            )
        )
        next_button.click()

        code = retrieve_phone_code(self.driver)

        code_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.phone_code_field
            )
        )
        code_field.send_keys(code)

        confirm = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.confirm_button
            )
        )
        confirm.click()

    def get_phone_number(self):
        phone_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                self.phone_number_field
            )
        )
        return phone_field.get_property('value')

    def add_card(self, card_number, card_code):
        payment_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.payment_method_button
            )
        )
        payment_button.click()


        add_card = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.add_card_button
            )
        )
        add_card.click()

        number_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.card_number_field
            )
        )
        number_field.send_keys(card_number)

        code_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.card_code_field
            )
        )
        code_field.send_keys(card_code)

        code_field.send_keys(Keys.TAB)

        link_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.link_card_button
            )
        )
        link_button.click()

        # Cerrar la ventana de métodos de pago
        close_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.close_payment_button
            )
        )
        close_button.click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(
                (By.CLASS_NAME, 'overlay')
            )
        )

    def set_message_for_driver(self, message):
        message_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.message_for_driver_field
            )
        )

        message_field.send_keys(message)

    def get_message_for_driver(self):
        message_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.message_for_driver_field
            )
        )

        return message_field.get_property('value')

    def select_blanket_and_handkerchiefs(self):
        switch = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.blanket_and_handkerchiefs_switch
            )
        )
        switch.click()

    def is_blanket_and_handkerchiefs_selected(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                self.blanket_and_handkerchiefs_checkbox
            )
        )

        return checkbox.is_selected()

    def add_two_ice_creams(self):
        plus_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.ice_cream_plus_button
            )
        )

        plus_button.click()
        plus_button.click()

    def get_ice_cream_count(self):
        counter = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.ice_cream_counter
            )
        )

        return counter.text

    def order_taxi(self):
        button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.order_taxi_button
            )
        )
        button.click()

    def is_order_modal_displayed(self):
        modal = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.order_modal
            )
        )

        return modal.is_displayed()

    def wait_for_driver_information(self):
        driver_info = WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(
                self.driver_rating
            )
        )

        return driver_info.is_displayed()

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        from_element = WebDriverWait(self.driver, 10).until(
           expected_conditions.presence_of_element_located(self.from_field)
        )
        from_element.send_keys(from_address)

    def set_to(self, to_address):
        to_element = WebDriverWait(self.driver, 10).until(
           expected_conditions.presence_of_element_located(self.to_field)
        )
        to_element.send_keys(to_address)

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_from(self):
        from_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.from_field)
        )
        return from_element.get_property('value')

    def get_to(self):
        to_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.to_field)
        )
        return to_element.get_property('value')




class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = webdriver.ChromeOptions()
        options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"},
        )
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.select_taxi()
        routes_page.select_comfort()

        assert routes_page.driver.find_element(
            *routes_page.comfort_button
        ).is_displayed()

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_phone_number(data.phone_number)

        assert routes_page.get_phone_number() == data.phone_number

    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.add_card(
            data.card_number,
            data.card_code
        )

    def test_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_message_for_driver(
            data.message_for_driver
        )

        assert (
                routes_page.get_message_for_driver()
                == data.message_for_driver
        )

    def test_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.select_blanket_and_handkerchiefs()

        assert routes_page.is_blanket_and_handkerchiefs_selected()

    def test_two_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.add_two_ice_creams()

        assert routes_page.get_ice_cream_count() == '2'

    def test_order_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.order_taxi()

        assert routes_page.is_order_modal_displayed()

    def test_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)

        assert routes_page.wait_for_driver_information()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
