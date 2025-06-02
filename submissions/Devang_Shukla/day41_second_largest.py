def find_second_largest(nums):
    unique_nums = list(set(nums))  
    if len(unique_nums) < 2:
        return "Array must contain at least two unique numbers."
    
    largest = second = float('-inf')
    
    for num in unique_nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num
    
    return second
input_str = input("Enter numbers: ")
nums = list(map(int, input_str.strip().split()))

result = find_second_largest(nums)
print("Second Largest Number:", result)