# 배열(Array), 큐(Queue)

## 잔재미 코딩 내용 정리:

**배열:** 

- 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조

- 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음

#### 왜 필요할까?

- 같은 종류의 데이터를 효율적으로 관리하기 위해 사용

- 같은 종류의 데이터를 순차적으로 저장

- 배열의 장점:
  - 빠른 점근 가능
- 배열의 단점:
  - 추가/삭제가 쉽지 않음
  - 미리 최대 길이를 지정해야 함

#### 파이썬과 C언어의 배열 예제

```c
# C
#include <stdio.h>

int main(int argc, char * argv[])
{
	char country[3] = "US";
	printf("%c%c\n", country[0], country[1]);
	printf("%s\n", country);
	return 0;
}
```

```python
# python
country = 'US'
print(country)

country = country + 'A'
print(country)
```

#### 파이썬과 배열

- 파이썬 리스트 활용

```python
# 1차원 배열: 리스트로 구현시
data = [1,2,3,4,5]
print(data)

# 2차원 배열: 리스트로 구현시
data = [[1,2,3],[4,5,6],[7,8,9]]
print(data[0])
```

배열의 활용: 값 참조하기, 값을 넣거나 빼기

```python
# 2차원 배열 지정
[[0 for col in range(n)] for row in range(n)]
```



### 큐

```python
import queue
data_queue = queue.Queue()
data_queue.put("funcoding")
data_queue.put(1)
data_queue.qsize() 
=2
data_queue.get()
"funcoding"
data_queue.get()
1

#last in first out
data_queue = queue.LifoQueue()
#PriorityQueue()
data_queue = queue.PriorityQueue()
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))
```



파이썬 알고리즘 인터뷰 내용 정리: 

자료구조

- 메모리 공간 기반의 연속 방식 -> 배열 (큐)
- 포인터 기반의 연결 방식 -> 연결 리스트 (스택)









이것이 코딩 테스트다 내용 정리:



이태우 알고리즘 내용 정리:



파이썬 자료구조와 알고리즘 내용 정리:



# LeetCode

```python
# 1470
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = nums
        x = []
        y = []
        temp = []
        for i,j in enumerate(arr):
            if i < n:
                x.append(j)
            if i >= n:
                y.append(j)
        for i in range(n):
            temp.append(x[i])
            temp.append(y[i])
        return temp
```

```
# 1365 How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        return_list = []
        
        for i in range(len(nums)):
            cnt =0 
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[j]<nums[i]:
                    cnt+=1
            return_list.append(cnt)
            
        return return_list
    

"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=[]
        
        for i in range(len(nums)):
            cnt=0
            for j in range(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        cnt+=1
            answer.append(cnt)
        
        return answer
"""
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            result.append(len([j for j in nums if j<i]))
        return result
"""
```

