import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:
    DRIVER_PATH = os.path.join(__file__[:__file__.find("features")], "drivers", "chromedriver.exe")
    HEADLESS = True

    @staticmethod
    def open(context):
        options = Options()
        if Browser.HEADLESS:
            options.add_argument("--headless")
        context.driver = webdriver.Chrome(Browser.DRIVER_PATH, options=options)
        context.tab_hs = list()

    @staticmethod
    def reset(context):
        context.tab_hs.clear()
        context.driver.delete_all_cookies()
        main_window_h = context.driver.current_window_handle
        for window_h in context.driver.window_handles:
            if window_h != main_window_h:
                context.driver.switch_to.window(window_h)
                context.driver.close()
        context.driver.switch_to.window(main_window_h)

    @staticmethod
    def new_tab(context):
        context.tab_hs.append(context.driver.current_window_handle)
        context.driver.switch_to.new_window("tab")

    @staticmethod
    def close_tab(context):
        context.driver.close()
        context.driver.switch_to.window(context.tab_hs.pop())
