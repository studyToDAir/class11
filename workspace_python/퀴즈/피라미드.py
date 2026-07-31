'''
피라미드

    *
   ***
  *****
 *******
*********

1. 나는 어떻게 했는가(를 슬로우모션으로 관찰하기)
    빈칸 4개 만들기
    별표 1개 만들기
    엔터

    빈칸 3개 만들기
    별표 3개 만들기
    엔터

    빈칸 2개 만들기
    별표 5개 만들기
2. 어려운 문제는 작은 문제로 쪼개기
3. 하나의 문제를 단순화 한다
'''

print('    *')
print('   ***')
print('  *****')
print(' *******')
print('*********')

# print('-', end='')
# print('-', end='')

for i in range(4) :
    print('-', end='')
# print('*')
for i in range(1) :
    print('*', end='')
print()



for i in range(3) :
    print('-', end='')
# print('***')
for i in range(3) :
    print('*', end='')
print()


for i in range(2) :
    print('-', end='')
# print('***')
for i in range(5) :
    print('*', end='')
print()

# 4~0
for j in range(4,-1,-1):
    # print(j)
    for i in range(j) :
        print('-', end='')

    k = ((4-j)*2) + 1 
    # print(k)
    for i in range(k) :
        print('*', end='')
    print()

m = 5
for j in range(m-1,-1,-1):
    # print(j)
    for i in range(j) :
        print('-', end='')

    k = ((m-1-j)*2) + 1 
    # print(k)
    for i in range(k) :
        print('*', end='')
    print()

print('-'*30)

# # Pyramid_Python(JavaScript ver)
# inputUser = int(input('줄 수 : '))
# for k in range(0,inputUser+1) :
#     result = ''
#     for m in range(0,inputUser-k) :
#         result += ' '
#     for i in range(0,(k+k)-1) :
#         result += '*'
#     for j in range(0,inputUser-k) :
#         result += ' '
#     print(result)

# # Pyramid_Python(Python verFinal)
# inputUser = int(input('줄 수 : '))
# for j in range(1,inputUser+1) :
#     print(' ' * (inputUser-j) ,end='')
#     print('*' * ((j+j)-1),end='')
#     print(' ' * (inputUser-j))


'''
m='*'; s='-';string = '';
for (i = 1; i <= 5; i++) {
    string = '';
    for (j = 5 - i; j >= 1; j--) {
        string += s;
    }
    for (k = 1; k <= i * 2 - 1; k++) {
        string += m;
    }
    for (l = 5 - i; l >= 1; l--) {
        string += s;
    }
    console.log(string);
}


'''

# c = int(input('피라미드 높이: '))

# for a in range(c):
#     for b in range( c - a - 1):
#         print(' ', end='')

#     for b in range(a * 2 + 1):
#         print('*', end='')

#     print()

line = int(input('줄 입력 : '))
m = '*'
s = '-'
for j in range(1, line):
    string = ''
    for i in range(1, line-j):
        string += s
    for i in range(1, j+1):
        string += m
    for i in range(1, j):
        string += m
    for i in range(1, line-j):
        string += s
    print(string)