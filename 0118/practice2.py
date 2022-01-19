# # 2. 홀수만 담기

# origin_list = list(range(1,51))

# sliced_list = origin_list[::2]

# print(sliced_list)


# # 3. Dictionary 만들기

# dic = dict(zip(
# ['김수정'
# ,'김신철'
# ,'김창현'
# ,'김태삼'
# ,'남성은'
# ,'문요성'
# ,'박종민'
# ,'손보희'
# ,'신희재'
# ,'오채명'
# ,'원민석'
# ,'유경훈'
# ,'윤병준'
# ,'이영주'
# ,'이지수'
# ,'이창엽'
# ,'임상빈'
# ,'임순우'
# ,'임지민'
# ,'장세진'
# ,'전재권'
# ,'최윤영'
# ,'최은우'
# ,'최희선'
# ,'한지운'
# ,'홍제민'
# ] ,
# [
# None,
# 29,
# 28,
# 27,
# 28,
# 29,
# 25,
# 28,
# 30,
# 25,
# 25,
# None,
# 28,
# 27,
# 28,
# 31,
# 28,
# 28,
# 27,
# None,
# 31,
# 27,
# 28,
# 26,
# 25,
# 25,

# ]))

# print(dic)


# # 4. 반복문 네모

# n = 5
# m = 9

# for i in range(m):
#     print(f'{"*" * n}')

# # 5. 
# temp = 36.5
# print('입실 불가') if temp >= 37.5 else print('입실가능')


# scores = [80, 89, 99, 83]

# sum = 0
# for i in scores :
#     sum = sum + i

# print(sum/len(scores))


##WS-2
##1. 간단한 약수

# N = int(input('N을 입력하시오'))
# ls = []
# for i in range(1,N + 1):
#     if not N%i :
#         ls.append(i)

# print(*ls)



# numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]
# for i in range(len(numbers)//2):
#     numbers.remove(max(numbers))
#     numbers.remove(min(numbers))
    
# print(*numbers)


# numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]

# numbers.sort()
# print(numbers[len(numbers)//2])


num = int(input('number를 입력하시오: '))

for i in range(1,num + 1):
    print(*range(1,i+1))