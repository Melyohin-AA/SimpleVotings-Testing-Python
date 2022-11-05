from selenium.webdriver.common.by import By
from features.steps.pages import Pages


class ApiCommand:
    def __init__(self, name: str, args: dict[str, str]):
        self.name = name
        self.args = args

    def execute(self, context) -> int:
        context.driver.get(Pages.get_api_page_address(self.name))
        get_status = context.driver.find_element(By.XPATH, "html/body").text
        if get_status == "400":
            raise RuntimeError(f"Command {self.name}({self.args}) load has failed!")
        for key, value in self.args.items():
            context.driver.find_element(By.XPATH, f"html/body/form/input[@name='{key}']").send_keys(value)
        context.driver.find_element(By.XPATH, "html/body/form/button").click()
        post_status = int(context.driver.find_element(By.XPATH, "html/body").text)
        if post_status == 400:
            raise RuntimeError(f"Command {self.name}({self.args}) execution has failed!")
        return post_status

    @staticmethod
    def del_user(login: str, password: str):
        return ApiCommand("del_user", {
            "login": login,
            "password": password,
        })

    @staticmethod
    def has_user(login: str):
        return ApiCommand("has_user", {
            "login": login,
        })
