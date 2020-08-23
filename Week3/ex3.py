# 반복문 연습

for i in [1,2,3,4,5,6,7] :
    print(i)

# 구구단
for i in [1,2,3,4,5,6,7,8,9] :
    for j in [1,2,3,4,5,6,7,8,9] :
        print(i, j, i * j)

# range(a, b) => [a, a+1, a+2, ... ,]
# range(1, 11) => [1,2,3,4,5,6,7,8,9,10]

# 피라미드 별 찍기
row = 10
for i in range(1, row + 1):
    star_row = ''
    for space in range(0, row - i) :
        star_row = star_row + ' '
    for star in range(0, i * 2 - 1) :
        star_row = star_row + '*'
    print(star_row)