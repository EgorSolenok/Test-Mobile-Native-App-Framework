import os
from datetime import datetime


APPIUM_PORT = '4723'
APPIUM_HOST = 'localhost'

class Capabilities:
    APK_TASK_CAPABILITIES = {
        "platformName": "Android",
        "appium:deviceName": "emulator",
        "app": f"{os.path.abspath(os.path.join(os.getcwd(), os.pardir))}\data\\app1.apk",
        "automationName": "UiAutomator2"
    }

FILE_LOG_NAME = (str(datetime.now())[2:16]).replace(':',' ')
