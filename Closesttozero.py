def closest_to_zero(nums):
    closest = float('inf')  # Initialize closest to positive infinity
    largest_closest = float('-inf')  # Initialize largest closest to negative infinity

    for num in nums:
        abs_num = abs(num)
        if abs_num < abs(closest) or (abs_num == abs(closest) and num > closest):
            closest = num
            largest_closest = num
        elif abs_num == abs(closest) and num > largest_closest:
            largest_closest = num

    return largest_closest

# Example usage:
nums = [-4, -2, 1, 4, 8]
result = closest_to_zero(nums)
print("Number closest to 0:", result)
