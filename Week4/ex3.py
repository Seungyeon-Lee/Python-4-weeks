# 스크롤을 이용한 크롤러
from selenium import webdriver

web = webdriver.Chrome(executable_path= r'/Users/yeon/Downloads/chromedriver')
web.get('https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&sxsrf=ALeKk01oAFr_v0S4NUKTI8bOISOSLufyIw:1598766662866&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi095L4ncLrAhVD7GEKHdtDAf8Q_AUoAXoECBcQAw&biw=1188&bih=746')

x_pos = 0
step = 100

while True :
    y_pos = y_pos + step
    web.execute_script('window.scrollTo(0, '+ str(y_pos) + ')')