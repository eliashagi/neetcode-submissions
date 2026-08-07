from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    newSum = 0
    for i in nums:
        newSum += i
    return newSum

def get_min(nums: List[int]) -> int:
    smallest = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest

def get_max(nums: List[int]) -> int:
    biggest = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > biggest:
            biggest = nums[i]
    return biggest

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
