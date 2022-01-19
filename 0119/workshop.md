### 1. 

```python
def list_sum(args):
   result = 0 
   for i in args:
       result += i
       
   return result
```





###  2. 

```python
def dict_list_sum(args):
    result = 0


    for i in args :
        result = result + i['age']
    
    return result    
```







### 3. 

```python
def all_list_sum(args):
    result = 0

    for i in args:
        for j in i :
            result = result + j
    return result

print(all_list_sum([[1], [2,3], [4,5,6], [7,8,9,10]]))
```



