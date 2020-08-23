a = 1
b = 2

aa = "1"
bb = "2"

print(a + b)
print(aa + bb)
# print(aa + a) 데이터 타입이 2개 이상 들어왔기 때문에 모호하다.
print(int(aa) + a)

cc = "13,761,000"
print(float(cc.replace(',','')) + int(cc.replace(',',''))) # type-converting, int type을 float으로 변경하여 연산


