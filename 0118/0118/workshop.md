### 1. 간단한 N의 약수

```python
N = int(input('N을 입력하시오'))
ls = []
for i in range(1,N + 1):
    if not N%i :
        ls.append(i)

print(*ls)
    
```



### 2. 중간값 찾기



```python
# 리스트에서 최대값 최소값 제거하면서 찾기
numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]
for i in range(len(numbers)//2):
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    
print(*numbers)


# .sort 사용

numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]

numbers.sort()
print(numbers[len(numbers)//2])

```



### 3. 계단 만들기

```python
num = int(input('number를 입력하시오: '))

for i in range(1,num + 1):
    print(*range(1,i+1))
```



