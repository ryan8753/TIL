



# 정중앙 문자


# def get_middle_char(abc):
#     # 변수 설정
#     char_len = len(abc)
#     result = 0
    
#     # 문자열 길이별 조건 나누기
#     if char_len %2 :
#         # 중간값 출력
#         result = abc[char_len//2]

#     else : 
#         # 중간값 출력
#         result = abc[char_len//2 - 1 : char_len//2 + 1 ]
    
#     return result


# print(get_middle_char('ssssasfy'))


#--------------------------------------------------------------

# 3. 위치 인자와 키워드 인자

# def ssafy(name, location = '서울'):
#     print(f'{name}의 지역은 {location}입니다.')

# ssafy('허준')
# ssafy(location = '대전', name = '철수')
# ssafy('dudgml', location = 'rhkdwnd')
# ssafy(name = 'rlfehd', 'rnal')    

#------------------------------------------------------------

# 5. 가변인자 리스트


# def my_avg(*args):
    
#     return sum(args)/len(args)

# print(my_avg(77,83,95,80,70))    

# ---------------------------------------------------------------


# 1. LIST 합 구하기

# def list_sum(args):
#    result = 0 
#    for i in args:
#        result += i
       
#    return result

# print(list_sum([1,2,3,4,5]))    

#----------------------------------------------------------------


# 2. 

# def dict_list_sum(args):
#     result = 0


#     for i in args :
#         result = result + i['age']
    
#     return result    

# print(dict_list_sum([{'name' : 'kim', 'age' : 12 }, {'name' : 'lee', 'age' : 4}]))

#----------------------------------------------------------------------------------


# 3. 

def all_list_sum(args):
    result = 0

    for i in args:
        for j in i :
            result = result + j
    return result

print(all_list_sum([[1], [2,3], [4,5,6], [7,8,9,10]]))

