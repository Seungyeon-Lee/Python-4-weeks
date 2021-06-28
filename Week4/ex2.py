# 키보드 입력
# 자바 스크립트 우회
# 클립보드 이용 - 제공이 되는 브라우저가 있고, 되지 않는 브라우저가 있다. (크롬은 되지 않고, 맥 크롬은 되지 않는다)

from seleniumwire import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time, pyperclip

WEB_DRIVE_PATH = "geckodriver"
ID = "id"
PASSWORD = "password"

def copy_input(driver, xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)

    # 윈도우 경우 Keys.COMMAND 대신 Keys.CONTROL 사용
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    # 키보드를 눌렀다가 떼는 동작

driver = webdriver.Firefox(capabilities=None, executable_path=WEB_DRIVE_PATH)
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login?')

copy_input(driver, '//*[@id="id"]', ID)
time.sleep(1.5)
copy_input(driver, '//*[@id="pw"]', PASSWORD)
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()