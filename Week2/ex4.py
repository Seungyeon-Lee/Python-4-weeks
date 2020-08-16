# 딕셔너리

var_dict = {}

# var_dict 딕셔너리 변수에 a라는 키가 존재하지 않으면 10이라는 값으로 초기화를 하고
# 없으면 그대로 둬라
var_dict['a'] = 10

var_dict.setdefault('a', 100)
var_dict.setdefault('aa', 1000)

print(var_dict)