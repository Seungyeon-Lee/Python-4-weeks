# 비교연산자
#   대소비교 (<, >, <=, >=, ==)

a = 10
b = 20
print(a == b)

# 관계연산자
#  여러 개의 True/False를 재조합해서 하나의 True,False를 만들어 줌
#  여러 가지의 상황에 따라 한 가지의 실행유무를 결정

a = True
b = False
c = True
d = False

# and(*), or(+)

print(a and b)
print(a or b) # 0은 False, 0을 제외한 모든 수는 True

# and 연산은 하나라도 False가 있으면 결과는 False
# or 연산은 하나라도 True가 있으면 결과는 True

# 관계 연산자이긴 한데 독립적으로 쓰이는 not 연산자가 있음
print(not a)

# 무언가가 존재하지 않을 때 어떤 코드를 실행해라
is_exist = True
is_exist = False

if not is_exist : ## is_exist == False와 동일
    print('없어서 실행')