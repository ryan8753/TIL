### 1.

```

```



### 2.

```python
def get_middle_char(abc):
    # 변수 설정
    char_len = len(abc)
    result = []
    
    # 문자열 길이별 조건 나누기
    if char_len %2 :
        # 중간값 출력
        result = abc[char_len//2]

    else : 
        # 중간값 출력
        result = abc[char_len//2 - 1 : char_len//2 + 1 ]
    
    return result


print(get_middle_char('coding'))

    
```





### 3 . 

```python
(4)
```





### 4. 

```python
None
```





### 5. 



```python
def my_avg(*args):
    
    return sum(args)/len(args)

```



### 