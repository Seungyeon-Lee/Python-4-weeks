import requests
import bs4

res = requests.post('http://dart.fss.or.kr/corp/searchCorpL.ax', data={
    "currentPage" : "2",
    "searchIndex" : "11"
 })

soup = bs4.BeautifulSoup(res.text, 'html.parser')

items = soup.select('.table_scroll table tbody tr')

for item in items:
    print(item.text)