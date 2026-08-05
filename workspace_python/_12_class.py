
class Person :

    # __init__
    # 클래스가 생성될 때
    # 자동으로 먼저 실행되는 메소드
    def __init__(self):
        print(1)
        self.hello = '안녕하세요'

    def greeting(self):
        # print('Hello Class')
        print(self.hello)

    def hello(self):
        self.greeting()

print(0)
james = Person()
print(2)
james.greeting()

print(james)
print(type(james))


class Person2 :
    def __init__(self, name, age):
        print('__init__ 실행')
        self.hello = '안녕하세요'
        self.name = name
        self.age = age

    def greeting(self):
        print(f'{self.hello}! 저는 {self.name}이고 나이는 {self.age}입니다')

a = Person2('이름', 20)
a.greeting()
print( a.hello )
print( a.name )

b = Person2('다른이름', 30)
b.greeting()
print( b.name )

b.addr = '천안'
print(b.addr)

# print(a.addr)
b.__init__(1,2) # 실행 됨


class Person3 :
    def __init__(self, money):
        self.hello = '안녕하세요'
        self.__money = money
        self.___money = money

    def pay(self, price):
        self.__money -= price
        print('남은 돈 : ', self.__money)
        self.__study()

    def __study(self):
        print('히히 나 혼자 레벨 업')

a = Person3(10000)
a.pay(3000)
print(a.hello)
# print(a.__money)
a.__money = 99999999 # 이건 변수 추가
a.pay(3000)
# a.__study()

# __붙은 변수나 함수는
# 내부에서는 접근 가능하고
# 외부로 노출되지 않는다
# 캡슐화, 은닉화
# print(a.___money) # __ + _money

class Knotted :

    brand = '노티드-디저트맛집'

    def __init__(self, name, addr) :
        # self.brand = '노티드-디저트맛집'
        self.name = name
        self.addr = addr
    def info(self):
        print(self.name)

k1 = Knotted('천안점', '천안')
k2 = Knotted('아산점', '아산')

print(k1.name, k1.brand)
print(k2.name, k2.brand)

print(k1.name, Knotted.brand)
print(k2.name, Knotted.brand)

class Calc :
    PI = 3.141592

    def __init__(self):
        self.meet = 200

    @staticmethod
    def add(x, y):
        return x + y

    def plus(self, x, y):
        return Calc.add(x, y)

print( Calc.add(1,2) * Calc.PI )

class Person4:
    count = 0

    def __init__(self) :
        Person4.count += 1

    @classmethod
    def print_count(cls) :
        print(f'{cls.count}명 생성 됨')

p1 = Person4()
p2 = Person4()
p3 = Person4()
Person4.print_count()


class Account:
    def __init__(self):
        self.__balance = 0

    def setBalance(self, money):
        self.__balance = money

    def getBalance(self):
        return self.__balance

a1 = Account()
# a1.balance = 99999

'''
문제1
멜론 차트 관리 시스템
모든 곡을 리스트로 관리
한 곡에 해당하는 클래스부터 만들자
- 제목, 가수명, 앨범명, 가사

두 곡 이상 정보를 저장
각 곡의 '제목-가수명'을 출력

문제2
휴먼잡스 계정 관리 시스템
내 계정에는 id, pw, 주소가 있다
모두 접근 제한된 private 변수입니다.

메소드를 이용해서 주소를 변경하거나
주소를 return하는 메소드를 만들기

문제3
디저트 카페 노티드 창업을 위한 클래스
 - 상호, 자본금이 필수 요소

노티드를 두군데에 창업할 것이다.
하나를 창업할 때 필수 요소를 꼭 넣어야 생성되도록 만드세요

'''

class Song :
    # - 제목, 가수명, 앨범명, 가사
    def __init__(self, title, singer, album, lyric):
        self.title = title
        self.singer = singer
        self.album = album
        self.lyric = lyric

s1 = Song('LOVE ATTACK', 'RESCENE (리센느)', 'SCENEDROME', '라부 어택')
s2 = Song('갑자기', '아이오아이 (I.O.I)', 'I.O.I 3rd MINI ALBUM', '써든 어택')

melon = [s1, s2]
for song in melon :
    print(f'{song.title}-{song.singer}')

class HumanJobs :
    def __init__(self):
        self.__id = None
        self.__pw = ''
        self.__addr = ''

    def setAddr(self, addr):
        if addr :
            self.__addr = addr
        else :
            print('주소를 다시 입력하세요')
    def getAddr(self):
        return self.__addr

h1 = HumanJobs()
# print( h1.__id )
h1.setAddr('천안')
h1_addr = h1.getAddr()
print( h1_addr )

class Knotted2 :
    def __init__(self, 상호, 자본금) :
        self.상호 = 상호
        self.자본금 = 자본금

# k1 = Knotted2()
# k1 = Knotted2('천안점')
k1 = Knotted2('천안점', 10000)


class Melon :
    def __init__(self):
        self.songList = []

    def appendSong(self, song):
        self.songList.append(song)
m = Melon()
m.appendSong(s1)




