from tests.pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from utils.generated_data import GeneratedData
from tests.pages.locators.locators import TaskPageLocators

class TaskPage(BasePage):
    def create_new_task(self):
        title_form = BrowserHelper.find_visible_element(self.driver, *TaskPageLocators.TITLE_FORM)
        title_form.send_keys(GeneratedData.get_new_title())
        description_form = BrowserHelper.find_visible_element(self.driver, *TaskPageLocators.DESCRIPTION_FORM)
        description_form.send_keys(GeneratedData.get_new_description())
        save_button = BrowserHelper.find_clickable_element(self.driver, *TaskPageLocators.SAVE_BUTTON)
        save_button.click()
        
    def change_task(self):
        title_form = BrowserHelper.find_visible_element(self.driver, *TaskPageLocators.TITLE_FORM)
        title_form.send_keys(GeneratedData.get_new_title())
        description_form = BrowserHelper.find_visible_element(self.driver, *TaskPageLocators.DESCRIPTION_FORM)
        description_form.send_keys(GeneratedData.get_new_description())
        save_button = BrowserHelper.find_clickable_element(self.driver, *TaskPageLocators.SAVE_BUTTON)
        save_button.click()
    