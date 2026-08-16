from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Power Function
def myPow(x: float, n: int) -> float:

    if n == 0:
        return 1.0

    # Handle negative exponents
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    current_product = x

    while n > 0:

        # If exponent is odd
        if n % 2 == 1:
            result *= current_product

        # Square the base
        current_product *= current_product

        # Divide exponent by 2
        n //= 2

    return result


# Testing
nums = [-1, 0, 3, 5, 9, 10]
target = 5

print("Index:", search(nums, target))
print("Power:", myPow(2.0, 9))
print("Power:", myPow(4.0, -2))
