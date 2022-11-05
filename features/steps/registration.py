import random
import behave
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from features.steps.browser import Browser
from features.steps.api_command import ApiCommand


class Registration:
    @staticmethod
    def generate_unique_login(context, min_length: int, max_length: int, ch_min: int, ch_max: int):
        Browser.new_tab(context)
        while True:
            length = random.randint(min_length, max_length)
            login = "".join((chr(random.randint(ch_min, ch_max)) for _ in range(length)))
            status = ApiCommand.has_user(login).execute(context)
            if status != 200: break
        Browser.close_tab(context)
        return login

    @staticmethod
    def submit_user_registration(context, login: str, pw1: str, pw2: str, name: str):
        context.reg_login = login
        context.reg_password = pw1
        context.driver.find_element(By.ID, "id_login").send_keys(login)
        context.driver.find_element(By.ID, "id_password1").send_keys(pw1)
        context.driver.find_element(By.ID, "id_password2").send_keys(pw2)
        context.driver.find_element(By.ID, "id_name").send_keys(name)
        context.driver.find_element(By.ID, "reg_button").click()

    @staticmethod
    def try_delete(context):
        if hasattr(context, "to_delete_reg") and context.to_delete_reg:
            context.to_delete_reg = False
            status = ApiCommand.del_user(context.reg_login, context.reg_password).execute(context)
            print("Account deletion:", status)


# WHEN

@behave.when('I try register as login={login:Text}, PW1={pw1:Text}, PW2={pw2:Text}, name={name:Text}')
def step_impl(context, login: str, pw1: str, pw2: str, name: str):
    Registration.submit_user_registration(context, login, pw1, pw2, name)


@behave.when('I try register as unique PW1={pw1:Text}, PW2={pw2:Text}, name={name:Text}')
def step_impl(context, pw1: str, pw2: str, name: str):
    login = Registration.generate_unique_login(context, 1, 64, 32, 126)
    Registration.submit_user_registration(context, login, pw1, pw2, name)


# THEN

@behave.then('I verify registration is succeeded')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").is_displayed()
    context.to_delete_reg = True


@behave.then('I verify registration is rejected')
def step_impl(context):
    context.to_delete_reg = True
    try:
        assert context.driver.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").is_displayed()
    except NoSuchElementException: pass
    context.to_delete_reg = False
