import behave
from selenium.webdriver.common.by import By
from features.steps.pages import Pages


class Authentication:
    @staticmethod
    def log_in(context, login: str, password: str):
        context.driver.get(Pages.get_login_page_address())
        Authentication.submit_credentials(context, login, password)

    @staticmethod
    def submit_credentials(context, login: str, password: str):
        context.login = login
        context.password = password
        context.driver.find_element(By.ID, "id_username").send_keys(login)
        context.driver.find_element(By.ID, "id_password").send_keys(password)
        context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        context.authenticated = context.driver.current_url == Pages.get_index_page_address()

    @staticmethod
    def log_out(context):
        context.driver.get(Pages.get_index_page_address())
        Authentication.click_logout_link(context)

    @staticmethod
    def click_logout_link(context):
        context.driver.find_element(By.XPATH, "//a[text()='Выйти']").click()


# GIVEN

@behave.given('logged in as {login:Text}:{password:Text}')
def step_impl(context, login: str, password: str):
    Authentication.log_in(context, login, password)


# WHEN


@behave.when('I try to log in as {login:Text}:{password:Text}')
def step_impl(context, login: str, password: str):
    Authentication.submit_credentials(context, login, password)


@behave.when('I try to log out')
def step_impl(context):
    Authentication.click_logout_link(context)


# THEN

@behave.then('I verify login is proper')
def step_impl(context):
    actual = context.driver.find_element(By.XPATH, "//label[text()='Логин']/../input").get_attribute("value")
    assert actual == context.login


@behave.then('I verify credentials are rejected')
def step_impl(context):
    assert context.driver.current_url == Pages.get_login_page_address()


@behave.then('I verify I am authenticated')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[text()='Выйти']").is_displayed()


@behave.then('I verify I am not authenticated')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[text()='Войти']").is_displayed()
