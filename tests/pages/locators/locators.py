from appium.webdriver.common.appiumby import AppiumBy
from utils.generated_data import GeneratedData

class MainPageLoctors:
    ADD_TASK_BUTTON = (AppiumBy.ID, "com.Tasks.Tasks:id/addTaskButton",)
    OPTIONS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "More options")
    NAVIGATION_TAB = (AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer",)
    CLOSING_NAVIGATION_TAB = (AppiumBy.ACCESSIBILITY_ID, "Close navigation drawer")
    TASK_TITLES = (AppiumBy.ID, "android:id/text1")
    
class TaskPageLocators:
    TITLE_FORM = (AppiumBy.ID, "com.Tasks.Tasks:id/taskTitleEditText")
    DESCRIPTION_FORM = (AppiumBy.ID, "com.Tasks.Tasks:id/taskDescriptionEditText")
    SAVE_BUTTON = (AppiumBy.ID, "com.Tasks.Tasks:id/saveTaskButton")
    
class NavigationBarLocators:
    IMPORT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Import")')
    GALLERY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Gallery")')
    SLIDESHOW_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Slideshow")')
    TOOLS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Tools")')
    
    