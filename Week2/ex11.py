import requests
import bs4

# 1. requests를 이용하여 json 또는 html을 가져옴
# 2. 만약, html일 때 bs4를 이용하여 원하는 데이터 파싱

res = requests.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&query=멍개")
# ?를 기준으로 뒤가 데이터
# print(res.text) # 문자열 형태의 html을 출력

# 문자열 형태의 html => DOM (객체)

dom = bs4.BeautifulSoup(res.text, 'html.parser')

"""
print(type(dom))
print(type(1))
print(type("1"))
print(type(1.1))
"""

# print(dom.title.text)
# print(dom.head)
# print(dom)

a_tags = dom.select('a.sh_blog_title') # 결과(반환, 리턴) 타입 => bs4 객체 타입의 데이터를 저장하고 있는 리스트

for a_tag in a_tags:
    print(a_tag.text)    