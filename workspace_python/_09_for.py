for i in range(5) :
    print(i, end=' ')
print()
for i in reversed(range(5)) :
    print(i, end=' ')


print('-'*30)
# 구구단
# j = 2
# for i in range(1, 9+1) :
#     print(f'2x{i}={2*i}')
# j = 3
# for i in range(1, 9+1) :
#     print(f'{j}x{i}={j*i}')

for j in range(2, 9+1) :
    for i in range(1, 9+1) :
        print(f'{j}x{i}={j*i}')


print('-'*30)
# 구구단인데 3단씩 옆으로
'''
2x1=2  3x1=3  4x1=4
...

5x1=5  6x1=6  7x1=7
...

8x1=8  9x1=9
'''

# i = 2, 5, 8
i = 2
j = range(1, 10)
# for j in range(1, 10) :
#     print(f'{i}x{j}={i*j}  {i+1}x{j}={(i+1)*j}  {i+2}x{j}={(i+j)*1}')

# for i in range(2, 10, 3) :
#     for j in range(1, 10) :
#         if i+2 < 10 :
#             print(f'{i}x{j}={i*j}  {i+1}x{j}={(i+1)*j}  {i+2}x{j}={(i+j)*1}')
#         else :
#             print(f'{i}x{j}={i*j}  {i+1}x{j}={(i+1)*j}')

k = 14
for i in range(2, k+1, 3) :
    for j in range(1, 9+1) :
        # print(f'{i}x{j}={i*j}', end='  ') 
        # if i+1 <= k :
        #     print(f'{i+1}x{j}={(i+1)*j}', end='  ')
        # if i+2 <= k :
        #     print(f'{i+2}x{j}={(i+2)*j}', end='  ')
        # print()
        for m in range(3) :
            if i+m <= k :
                print(f'{i+m}x{j}={(i+m)*j}', end='\t') 
        print()
    print()


import random
print( random.random() )
print( random.randint(1, 6) )

print('-'*12)
# 주사위 3이 몇번만에 나오는지 출력
dice = -1
count = 0
while dice != 3 :
    dice = random.randint(1, 6)
    count += 1
    if dice == 3 :
        print(count)


import turtle as t
t.shape('turtle')

# while True :
#     print(1)


a = [  i*10 if i%2 == 0 else i for i in range(10)  ]
for i in range(10) :
    if i%2 == 0:
        a.append(i*10)
    else :
        a.append(i)

a = 20
i = 0
while i < 10 :
    if i == a :
        print('찾음')
        break
    i += 1
else :
    print('못찾음')
# while의 else는 break를 만나지 않고 종료되는 경우 else문 실행 됨

