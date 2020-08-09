import requests

response = requests.get('https://crix-api-cdn.upbit.com/v1/crix/candles/days?code=CRIX.UPBIT.KRW-BTC&count=200&ciqrandom=1568240649168')

# 200 : 정상
# 300 : redirection(새로고침)
# 400 : 클라이언트 문제 (EX. 로그인을 하지 않고 요청)
# 500 : 서버 문제

print(response.text) # 문자열(dict + list)
print(response.json()) # 문자열 => dict + list

for item in response.json() :
    print(item)

# json : dict + list => 문자열로 변환
