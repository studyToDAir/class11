# 1~100까지 출력
# 3의 배수는 fizz
# 5의 배수는 buzz
# 3과5 공통 배수(15,30,45...)는 fizzbuzz

# 9는 3의 배수인가?
# 8은 3의 배수인가?

for i in range(1, 101) :
    print(i, end=' ')
    if i % 3 == 0 and i % 5 == 0 :
        print('fizzbuzz', end='')
    elif i % 3 == 0 :
        print('fizz', end='')
    elif i % 5 == 0 :
        print('buzz', end='')
    print()
