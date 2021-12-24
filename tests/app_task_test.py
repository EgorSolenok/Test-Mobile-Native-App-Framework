import pytest

from tests.pages.main_page import MainPage
from tests.pages.task_page import TaskPage

@pytest.fixture(scope='module')
def main_page(driver):
    main_page = MainPage(driver)
    yield main_page

@pytest.fixture(scope='module')
def task_page(driver):
    task_page = TaskPage(driver)
    yield task_page
    
@pytest.fixture(scope='function')
def app(driver):
    yield
    driver.reset()


class TestGuestActions:
    def test_user_should_see_correct_title_of_created_task(self, driver, app, main_page, task_page):
        main_page.go_to_add_new_task()
        task_page.create_new_task()
        main_page.should_be_correct_last_title_name()
        
    def test_user_should_see_correct_title_of_changed_task(self, driver, app, main_page, task_page):
        main_page.go_to_edit_task()
        task_page.change_task()
        main_page.should_be_correct_first_title_name()
        
    def test_user_should_see_navigation_bar_after_swipe(self, driver, app, main_page):
        main_page.open_navigation_bar()
        main_page.should_be_navigation_bar_items()
        
    def test_user_should_see_correct_titles_after_block_screen(self, driver, app, main_page, task_page):
        main_page.go_to_edit_task()
        task_page.change_task()
        main_page.lock_screen()
        main_page.unlock_screen()
        main_page.should_be_correct_first_title_name()
        
    def test_user_should_see_checked_element_after_swipe(self, driver, app, main_page):
        main_page.open_navigation_bar()
        main_page.check_gallery_in_navbar()
        main_page.wait_for_disappearing_navbar()
        main_page.open_navigation_bar()
        main_page.gallery_should_be_checked()
        
    def test_user_should_see_correct_titles_after_swap_to_background(self, driver, app, main_page, task_page):
        main_page.go_to_add_new_task()
        task_page.create_new_task()
        main_page.swap_to_background()
        main_page.should_be_correct_last_title_name()
