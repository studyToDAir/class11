
# 딕셔너리 선언
a = {}
a = dict()
print( type(a) )

b = {
    '이름': '호랑이심장',
    '직업': '마법사',
    '직업': '마법사2',
    '스킬': {
        '공격': '고백',
        '방어': '철벽남',
        'javascript': '상'
    }
}
print(b)

c = dict(a=10, b=20)
print(c)

# b.이름
print( b['이름'] )
# print( b['이름2'] )

print( b.get('이름') )
print( b.get('이름2') ) # 없으면 None
print( b.get('이름2', '이름없음') ) # 없으면 두번째 값으로 대체

d = b['스킬']
d['공격']
b['스킬']['공격']
print(b['스킬']['공격'])

print( b.get('스킬').get('공격') )

print( b.get('스킬2', {}).get('공격', 0) )

b['직업'] = '도적'
print( b )

b['직업2'] = '도적2' # 없으면 key 만들어 줌
print( b )

print( '스킬' in b )
print( '공격' in b  )
print( '공격' in b['스킬'] )
print( '공격' not in b['스킬'] )

print( len(b) ) # key의 개수

e = b.keys()
print( e )
f = b.values()
print( f )
print( list(f)[0] )

g = b.items()
print( g )

a = 'hello'
print( list(a) )
print( set(a) ) # {'h', 'e', 'o', 'l'}
# set
#   중복을 제거해서 관리한다
#   순서는 보장하지 않는다


b = {
    '이름': '호랑이심장',
    '직업': '마법사',
    '직업': '마법사2',
    '스킬': {
        '공격': '고백',
        '방어': '철벽남',
        'javascript': '상'
    }
}
b.update(이름='타이거', 직업='강사')
b.update(이름='타이거', 직업='강사', 나이=20)
print(b)
c = b.pop('나이')
print(b)
print(c)
# c = b.pop('나이') # 없으면 에러
c = b.pop('나이', 0) # 없으면 두번째 값을 사용
print(c)
# c = b.pop() # 전달인자 필수
c = b.popitem()
print(c)
print(b)

a = ['a', 'b', 'c']
b = {
    'a':0,
    'b':0,
    'c':0
}
b = {}
b[a[0]] = 0
b[a[1]] = 0

c = dict.fromkeys(a)
print(c)

# key만 나온다
for i in c :
    print(i)
    print(c[i])

for k, v in c.items() :
    print(k, v)


'''
문제1
numbers = [3, 7, 10, 15, 22, 8, 13]
문제1-1 : 짝수만 따로 리스트로 만들어서 출력
문제1-2 : 홀수의 합

문제 2
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
다 샀을 때 가격은?

문제3
UP/DOWN 게임 만들기
단, 맞추면 몇번째에 맞췄는지도 출력

문제4
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}
이런 경우 
id/pw를 입력 받거나 변수에 넣어두고
id/pw가 맞는지 틀리는지 판단해서
"아이디가 없습니다", "비번이 틀립니다", "로그인 성공"


문제5
랜덤 투표 시스템
한번에 a, b, c 대상에 랜덤으로 투표
문제5-1 : 100번의 투표 결과를 출력하시오
문제5-2 : 그 중 가장 득표 많은 사람의 이름과 득표 수 출력

'''


users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}
for i, item in enumerate(users.items()) :
    print(i, item[0], item[1])

