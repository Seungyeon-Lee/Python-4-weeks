from selenium import webdriver

web = webdriver.Chrome(executable_path= r'/Users/yeon/Downloads/chromedriver')

web.get('https://www.naver.com') # 주소 창에 치는 것을 의미

web.find_element_by_name('id').send_keys('naver_id')
web.find_element_by_name('pw').send_keys('mypassword1234')

web.find_element_by_name('submit').click()