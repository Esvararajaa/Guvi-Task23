from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class dragdrop:

    def __init__(self, web_url):
        # get the url
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # use implicit wait
        self.driver.implicitly_wait(10)

    def ddaction(self):
        # get the URL
        self.driver.get(self.url)
        self.driver.maximize_window()
        # switch to required frame
        self.driver.switch_to.frame(0)
        # save the draggable element to a desired variable
        source1 = self.driver.find_element(By.ID, "draggable")
        # save the droppable element to a desired variable
        target1 = self.driver.find_element(By.ID, "droppable")
        # create object for the actionchains
        a = ActionChains(self.driver)
        # perform drag and drop function using action chain object
        a.drag_and_drop(source1, target1).perform()

    def shutdown(self):
        self.driver.close()


url = "https://jqueryui.com/droppable/"
# create object for the class
dd = dragdrop(url)
# call the methods using the object created
dd.ddaction()
dd.shutdown()
