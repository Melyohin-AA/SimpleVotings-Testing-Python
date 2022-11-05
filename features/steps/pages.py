import behave
from selenium.webdriver.common.by import By


class Pages:
    SERVER_ADDRESS = "http://127.0.0.1:8000"

    @staticmethod
    def get_api_page_address(cmd_name: str):
        return f"{Pages.SERVER_ADDRESS}/testing_api/?cmd={cmd_name}"

    @staticmethod
    def get_index_page_address():
        return f"{Pages.SERVER_ADDRESS}/"

    @staticmethod
    def get_login_page_address():
        return f"{Pages.SERVER_ADDRESS}/login/"

    @staticmethod
    def get_registration_page_address(test: bool):
        if test: return f"{Pages.SERVER_ADDRESS}/registration/?test"
        return f"{Pages.SERVER_ADDRESS}/registration/"

    @staticmethod
    def get_my_profile_page_address():
        return f"{Pages.SERVER_ADDRESS}/my_profile/"


# GIVEN

@behave.given('{url:Page} page is opened')
def step_impl(context, page: str):
    context.driver.get(Pages.SERVER_ADDRESS + page)


@behave.given('index page is opened')
def step_impl(context):
    context.driver.get(Pages.get_index_page_address())


@behave.given('login page is opened')
def step_impl(context):
    context.driver.get(Pages.get_login_page_address())


@behave.given('registration page is opened')
def step_impl(context):
    context.driver.get(Pages.get_registration_page_address(True))


@behave.given('my_profile page is opened')
def step_impl(context):
    context.driver.get(Pages.get_my_profile_page_address())


# WHEN

@behave.when('I navigate to login page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Войти']").click()


@behave.when('I navigate to registration page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Регистрация']").click()


@behave.when('I navigate to my_profile page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Мой профиль']").click()


# THEN

@behave.then('I verify index page is loaded')
def step_impl(context):
    assert context.driver.current_url == Pages.get_index_page_address()


@behave.then('I verify login page is loaded')
def step_impl(context):
    assert context.driver.current_url == Pages.get_login_page_address()


@behave.then('I verify registration page is loaded')
def step_impl(context):
    assert (context.driver.current_url == Pages.get_registration_page_address(False)) or \
           (context.driver.current_url == Pages.get_registration_page_address(True))
