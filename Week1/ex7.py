# 반복문
var_list = [10,20,30,40,50,60,70,80,90]
var_dict = {
    "title" : 1,
    "img" : ["img1", "img2"]
}
var_str = "hello world"

# 반복
# 이터러블(반복자)한 데이터 특성

# 리스트를 반복문 돌릴 때 (값)
for i in var_list:
    print(i)
    # 처리 로직

# 딕셔너리를 반복문 돌릴 때 (키 값)
for i in var_dict:
    print(i, var_dict[i])

# 문자열을 돌릴 때 (값)
for i in var_str:
    print(i)

print('end')