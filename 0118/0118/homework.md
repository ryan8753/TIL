### 1. Mutable & Immutable

​	mutable : Set, Dictionary

​	immutable : Sting, Tuple, Range



### 2. 홀수만 담기



```python
origin_list = list(range(1,51))

sliced_list = origin_list[::2]

print(sliced_list)
```





### 3. Dictionary 만들기

```python
dic = dict(zip(
['김수정'
,'김신철'
,'김창현'
,'김태삼'
,'남성은'
,'문요성'
,'박종민'
,'손보희'
,'신희재'
,'오채명'
,'원민석'
,'유경훈'
,'윤병준'
,'이영주'
,'이지수'
,'이창엽'
,'임상빈'
,'임순우'
,'임지민'
,'장세진'
,'전재권'
,'최윤영'
,'최은우'
,'최희선'
,'한지운'
,'홍제민'
] ,
[
None,
29,
28,
27,
28,
29,
25,
28,
30,
25,
25,
None,
28,
27,
28,
31,
28,
28,
27,
None,
31,
27,
28,
26,
25,
25,
]
))
```



### 4. 반복문으로 네모 출력

```python
n = 5
m = 9

for i in range(m):
    print(f'{"*" * n}')

```



### 5. 조건 표현식

```python
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실가능')
```



### 6. 평균 구하기

```python
scores = [80, 89, 99, 83]

sum = 0
for i in scores :
    sum = sum + i

print(sum/len(scores))
```



