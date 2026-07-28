a = 10
print(a)

b = 5 / 2
print(b)

# b = 5 / 0 # ZeroDivisionError: division by zero
# print(b)

c = 5 // 2
print(c)

d = -5 // 2 # 내림
print(d)

e = 4 ** 2 # 제곱
print(e)

# e++ # 없음
# e-- # 없음
e = e + 1
e **= 2
print(e)

print( int(2.4) )
print( int(-2.4) ) # 소수점 버림
print( int('10')+1 )
# print( int('a') )

print(0.12345678901234567890123456789)


print( type(10) )
print( type('10') )

print( 4.3 - 2.7 == 1.6 )


print(4.2 + 5)

print( float(5) )
print( float('5.2') )

a = 10
b = '오백원'

# 전통적인 swap
c = a 
a = b
b = c

a, b = b, a
print(a) # 오백원
print(b) # 10

a = input('입력하세요:')
print(a)

# print( 'a'+ 1 )
print( 'a'+ 'b' )

print(1,2)
print(1, 2, sep=" ")
print(1, 2, sep=",")

print(1, 2, end='', sep=" ")
print(2, end='\n')

x = 4
print(++x)
# print(x++)

print( 1 == 1.0 )
print( 1 is 1.0 ) # === 즉, 타입까지 같다
print( 1 is not 1.0 ) # !==

print(1, False or False and not False)

a = '글씨'
b = a or '쉬는시간'
print( b )

print(3 < 5 < 7)


