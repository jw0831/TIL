# 배열(Array), 큐(Queue)

## 잔재미 코딩 내용 정리:

**배열:** 

- 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
- 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음

- 메모리 공간 기반의 연속 방식 -> 배열 (큐)
- 포인터 기반의 연결 방식 -> 연결 리스트 (스택)

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





이것이 코딩 테스트다 내용 정리:



파이썬 자료구조와 알고리즘 내용 정리:



# LeetCode

### 배열

[1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

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

[1470. Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/)

```python
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

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            result.append(len([j for j in nums if j<i]))
        return result
```

[1. Two Sum](https://leetcode.com/problems/two-sum/submissions/)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 브루트 포스로 계산
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
     ############### ############### ############### ############### ###############
        # in 을 이용한 탐색
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)
 		 ############### ############### ############### ############### ###############
        # 첫 번째 수를 뺀 결과 키 조회
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]
       
     ############### ############### ############### ############### ###############
        # 조회 구조 개선
        # 저장할 필요 없이, 그치만 매번 비교해야 함으로 별차이없는 성능
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
       
        
        """
        # 안되는 case
        # 투 포인터 이용
        # 투 포인터란, 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정하는 방식이다.
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left, right
            
            #nums가 정렬된 상태가 아니라 불가능 그리고 nums.sort()로 정렬을 해도 인덱스가 망가져서 문제이다. 결국 투포인터로는 못한다.
        """
```



[1295.  Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/submissions/)

[1588. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)

[1304. Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)

(파이썬 알고리즘 인터뷰) pg.180  부터

### 큐

