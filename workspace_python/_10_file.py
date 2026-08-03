# w : 수정 가능
file = open('hello.txt', 'w')
file.write('eng\n123\n한글')
file.flush() # 버퍼가 꽉 차지 않아도 내보내기
             # 즉시 반영
file.close()


# 한글 캐릭터셋
# utf-8, euc-kr, cp949
file = open('hello2.txt', 'w', encoding='utf-8')
file.write('eng\n123\n한글')
file.close()

# r : 읽기 전용
file = open('hello.txt', 'r')
s = file.read()
file.close()
print(s)

file = open('hello2.txt', 'r', encoding='utf-8')
s = file.read()
file.close()
print(s)

print('-'*20)
file = open('hello.txt', 'r')
# s = file.read(6)
s = file.read(10)
file.close()
print(s)

print('-'*20)
file = open('hello.txt', 'r', buffering=1)
s = file.read()
file.close()
print(s)

text = ''
file = open('hello.txt', 'r')
while True :
    chunk = file.read(2)
    if not chunk :
        break
    text += chunk
    print(chunk)
file.close()
print(text)



file = open('a.webp', 'rb')
s = file.read()
file.close()
print(s)

file = open('hello.txt', 'r')
s = file.read()
file.close()
print(s)

with open('hello.txt', 'r') as file :
    s = file.read()
    print(s)

a = [1,2,3,4]
with open('array1.txt', 'w') as file :
    # file.write(str(file))
    file.write(str(a))
print(str(a))

with open('array1.txt', 'r') as file :
    b = file.read()
    print( type(b), b )
    c = list(b)
    print( type(c), c )

import pickle

name = 'eng'
age = 20
address = '한글'
arr = [1,2,3,4]
score = {
    'k': 1,
    'k2': 'val'
}

with open('pickle.p', 'wb') as f :
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(arr, f)
    pickle.dump(score, f)

with open('pickle.p', 'rb') as f :
    # dump 순서대로 꺼낸다
    p1 = pickle.load(f)
    print(p1)
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    print(p2['k'])

    # dump한 만큼만 꺼낼 수 있다
    # p2 = pickle.load(f)
    # print(p2, type(p2))

# pickle 보다 대용량에 특화된 라이브러리
# import joblib

# a 이어 쓰기
with open('hello.txt', 'a') as f :
    f.write('123')
    # f.read()

# +
# 쓰기 계열에 붙어있으면 읽기 가능해짐
# 읽기 계열에 붙어있으면 쓰기 가능해짐

# a = 'abc def'

# words.txt를 
# 읽어서
# c가 포함된 단어 찾기
# , . 은 출력하지 않는다

with open('word.txt', 'r') as file :
    txt = file.read()
    print(txt)
    
    # txt = 'Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'
    txt_list = txt.split(' ')
    print(txt_list)
    # for i in range(len(txt_list)) :
    #     print(txt_list[i])

    for word in txt_list :
        # print(word)
        tmp = word.split('c')
        if len(tmp) > 1 :
            a = word.split('.')
            b = ''.join(a)
            c = b.split(',')
            d = ''.join(c)
            print(d)

print('-'*30)
with open('word.txt', 'r') as file :
    txt = file.read()
    print(txt)
    
    # txt = 'Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'
    txt_list = txt.split(' ')
    print(txt_list)
    # for i in range(len(txt_list)) :
    #     print(txt_list[i])

    for word in txt_list :
        # if word.find('c') != -1 :
        # if word.count('c') > 0 :
        # if 'c' in word or 'C' in word :
        if 'c'.lower() in word.lower() :
            a = word.replace(',', '')
            b = a.replace('.', '')
            # b = word.replace(',', '').replace('.', '')
            print(b)

# print([1,2,3].find())
