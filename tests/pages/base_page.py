class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def lock_screen(self):
        self.driver.lock()
        
    def unlock_screen(self):
        self.driver.unlock()
    
    def swap_to_background(self, time=3):
        self.driver.background_app(time)

        
        
    