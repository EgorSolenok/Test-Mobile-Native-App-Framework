from appium.webdriver.common.touch_action import TouchAction

from tests.pages.base_page import BasePage
from tests.pages.locators.locators import MainPageLoctors
from tests.pages.locators.locators import NavigationBarLocators
from utils.browser_helper import BrowserHelper
from utils.generated_data import GeneratedData


class MainPage(BasePage):
    def check_gallery_in_navbar(self):
        gallery_button = BrowserHelper.find_visible_element(self.driver, *NavigationBarLocators.GALLERY_BUTTON)
        gallery_button.click()
        
    def wait_for_disappearing_navbar(self):
        navigation_button = BrowserHelper.find_visible_element(self.driver, *MainPageLoctors.NAVIGATION_TAB)
        assert navigation_button, "No navbar button appear"
        
    def go_to_add_new_task(self):
        add_button = BrowserHelper.find_clickable_element(self.driver, *MainPageLoctors.ADD_TASK_BUTTON)
        add_button.click()
    
    def go_to_edit_task(self):
        task_titles = BrowserHelper.find_visible_elements(self.driver, *MainPageLoctors.TASK_TITLES)
        first_title = task_titles[0]
        first_title.click()
        
    def open_navigation_bar(self):
        actions = TouchAction(self.driver)
        actions.long_press(None, 50, 800).move_to(None, 800, 800).release().perform()
        
    def should_be_correct_first_title_name(self):
        task_titles = BrowserHelper.find_visible_elements(self.driver, *MainPageLoctors.TASK_TITLES)
        first_title = task_titles[0]
        assert f"{GeneratedData.GENERATED_TITLE}" in first_title.text, "Incorrect title displayed"
    
    def should_be_correct_last_title_name(self):
        task_titles = BrowserHelper.find_visible_elements(self.driver, *MainPageLoctors.TASK_TITLES)
        last_added_title = task_titles[-1]
        assert f"{GeneratedData.GENERATED_TITLE}" in last_added_title.text, "Incorrect title displayed"
        
    def should_be_navigation_bar_items(self):
        navigation_items = {
            'import_button': BrowserHelper.find_visible_elements(self.driver, *NavigationBarLocators.IMPORT_BUTTON),
            'gellery_button': BrowserHelper.find_visible_elements(self.driver, *NavigationBarLocators.GALLERY_BUTTON),
            'slideshow_button': BrowserHelper.find_visible_elements(self.driver,
                                                                    *NavigationBarLocators.SLIDESHOW_BUTTON),
            'tools_button': BrowserHelper.find_visible_elements(self.driver, *NavigationBarLocators.TOOLS_BUTTON)}
        assert len(navigation_items) == 4, "Not all element of navbar is displayed"
        
    def gallery_should_be_checked(self):
        gallery_button = BrowserHelper.find_visible_element(self.driver, *NavigationBarLocators.GALLERY_BUTTON)
        assert gallery_button.get_attribute("checked") == "true", "The element is not checked"

        


        
    
