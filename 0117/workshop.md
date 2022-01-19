### 1. 세로로 출력하기



```python
num = int(input("number 입력하시오 : "))



for i in range(1,num + 1) : 
    print(i)


```



### 2. 거꾸로 세로로 출력하기

```python
num = int(input("number 입력하시오 : "))

for i in range(num,0,-1) : 
    print(i)

```





### 3. N줄 덧셈(SWEA #2025)

```python
num = int(input("number 입력하시오 : "))

sum = 0

for i in range(1,num + 1) :
    sum = sum + i

print(sum)
```

