# import sys

# num1 = 0.1 * 3
# num2 = 0.3

# result = abs(num1-num2) <= sys.float_info.epsilon

# print(result)


# name = '철수'

# print('안녕, %s야' % name)
# print('안녕, {}야'.format(name))
# print(f'안녕, {name}야')

# str(1)
# int('30')
# int(5)
# bool('50')
# int('3.5')


# n = 5
# print("{:*^n}".format(''))

# print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지.\'')

# a= int(input('a를 입력하세요 :'))
# b= int(input('b를 입력하세요 :'))
# c= int(input('c를 입력하세요 :'))

# result1 = (-b + (b**2 - 4*a*c)**(1/2))/(2 * a)
# result2 = (-b - (b**2 - 4*a*c)**(1/2))/(2 * a)

# print(result1)
# print(result2)

## 4. 네모출력
# n = 5
# m = 9

# line1 = f'{"*" * n}\n'
# print(f'{line1 * m }')



# -----------------------------------------------------------------
#WORKSHOP


# # 1. 세로로 출력하기

# num = int(input("number 입력하시오 : "))

# for i in range(1,num + 1) : 
#     print(i)


# # 2. 거꾸로 세로로 출력하기

# num = int(input("number 입력하시오 : "))

# for i in range(num,0,-1) : 
#     print(i)


# # 3. N줄 덧셈

# num = int(input("number 입력하시오 : "))

# sum = 0

# for i in range(1,num + 1) :
#     sum = sum + i

# print(sum)