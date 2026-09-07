from typing import List , Tuple

def findKthLargest(nums: List[int],k: int) ->  int:
    nums = sorted(nums, reverse= True)
    return nums[k - 1]

def findMinMax(nums: List[int]) -> Tuple[int ,int]:
    if len(nums) == 1:
        return nums[0] , nums[0]

    mid = len(nums)//2
    min1 , max1 = findMinMax(nums[:mid])
    min2 , max2 = findMinMax(nums[mid:])

    return min(min1 , min2), max(max1 , max2)

#Driver code
nums = list(map(int,input("Enter unsorted intergers: ").split()))
k = int(input("Enter value of k:"))

print(f"{k}-th largest element:",findKthLargest(nums, k))

minimum, maximum = findMinMax(nums)
print("Minmum element:", minimum)
print("Maximum element:", maximum)