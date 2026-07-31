print('문제1')
numbers = [3, 7, 10, 15, 22, 8, 13]
even = []
for num in numbers :
    if num % 2 == 0 :
        even.append(num)
print(even)


even = [num for num in numbers if num % 2 == 0]
print(even)

odd = [num for num in numbers if num % 2 != 0]
print(123, sum(odd))
hap = 0
for num in numbers :
    if (num % 2 != 0) :
        hap += num
print(hap)
print( sum(num for num in numbers if num % 2 != 0) )

print('문제2')
cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}
print( cart['사과']['가격'] )

apple = cart['사과']['가격'] * cart['사과']['개수']
banana = cart['바나나']['가격'] * cart['바나나']['개수']

for a in cart :
    print(a)
b = cart.keys()
for a in b :
    print(a)

total = 0
for fruit in cart :
    total += cart[fruit]['가격'] * cart[fruit]['개수']
print(total)

print('문제3')

import random as r
q3 = r.randint(1, 100)
print('정답', q3)
count = 0

while True :
    # num = int( input('예상은? : ') )
    num = q3
    count += 1

    if not (1 <= num <= 100) :
        print('1~100임')
    else :
        if num == q3 :
            print('정답! 시도 횟수 : ', count)
            break
        elif num < q3 :
            print("UP")
        elif num > q3 :
            print("DOWN")

print('문제4')
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}

id = 'admin'
pw = '1234'
# id = input('id:')
# pw = input('pw:')

# key 없으면 에러
# if users['admin2'] == '1234' :
#     print('로그인 성공')

# print('admin2' in users)
if id in users :
    if users[id] == pw :
        print('로그인 성공')
    else :
        print('비밀번호가 틀립니다')
else :
    print('아이디가 없습니다')

# 매번 출력되느지라 쫌 그래..
# for 아이디, 비번 in users.items() :
#     if 아이디 == id :
#         if 비번 == pw :
#             print('성공')
#         else :
#             print('비번 틀림')
#     else :
#         print('아이디 없음')

if id in users :
    if users[id] == pw :
        print('로그인 성공')
    else :
        print('비밀번호가 틀립니다')
else :
    print('아이디가 없습니다')

# key 없으면 None
if users.get(id) :
    if users.get(id) == pw :
        print('로그인 성공')
    else :
        print('비밀번호가 틀립니다')
else :
    print('아이디가 없습니다')


print('문제5')
a = 0
b = 0
c = 0
import random
for i in range(100):
    vote = random.randint(1,3)
    if vote == 1 :
        a += 1
    elif vote == 2 :
        b += 1
    elif vote == 3 :
        c += 1
print(a,b,c)

후보 = [0,0,0] #a,b,c
import random
for i in range(100):
    vote = random.randint(0, 2)
    후보[vote] += 1
print(후보)

후보 = {
    '후보1': {
        '이름': 'a',
        '득표': 0
    },'후보2': {
        '이름': 'a',
        '득표': 0
    }, '후보3': {
        '이름': 'a',
        '득표': 0
    },
}
후보 = {
    'a':0,
    'b':0,
    'c':0
}

후보 = ['a', 'b', 'c']
득표 = {}

# if 투표 in 득표 :
#     득표[투표] = 득표[투표] + 1
# else :
#     득표[투표] = 1
# print(득표)
for i in range(100):
    투표 = random.choice(후보)

    득표[투표] = 득표.get(투표, 0) + 1
print(득표)

print(max(득표), 득표[max(득표)])


