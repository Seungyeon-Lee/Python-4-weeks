# 가위, 보자기, 바위
user1 = '가위'
user2 = '보자기'

if (user1 == '가위' and user2 == '가위') or (user1 == '바위' and user2 == '바위') or (user1 == '보자기' and user2 == '보자기') :
    print('user1과 user2는 비김')
elif (user1 == '바위' and user2 == '가위') or (user1 == '보자기' and user2 == '바위') or (user1 == '가위' and user2 == '보자기') :
    print('user1가 이김')
elif (user1 == '보자기' and user2 == '가위') or (user1 == '가위' and user2 == '바위') or (user1 == '바위' and user2 == '보자기') :
    print('user2가 이김')