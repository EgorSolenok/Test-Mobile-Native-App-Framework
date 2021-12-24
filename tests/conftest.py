import pytest
import allure
import os
from appium import webdriver

from utils.server_logger import create_logs_file
from config import APPIUM_HOST, APPIUM_PORT
from config import Capabilities


@pytest.fixture(scope='package')
def driver():
    driver = webdriver.Remote(
        command_executor=f"http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub",
        desired_capabilities=Capabilities.APK_TASK_CAPABILITIES
    )
    yield driver
    create_logs_file(driver)
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

