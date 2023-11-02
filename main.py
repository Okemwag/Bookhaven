# Simple program to reverse a string
"""
def reverse_string(input_string):
    reversed_string = ""
    
    
    for char in input_string:
        reversed_string = char + reversed_string
        
    return reversed_string

user_input = input("Enter a string to reverse: ")
print("Your reversed string is: " + reverse_string(user_input))
"""
def find_subarray_with_sum(arr, target_sum):
    current_sum = 0
    start = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > target_sum:
            current_sum -= arr[start]
            start += 1

        if current_sum == target_sum:
            return arr[start:end+1]

    return None

# Example usage
a = [4, 2, 1, 1, 3, 4, 5]
target_sum = 5
result = find_subarray_with_sum(a, target_sum)

if result is not None:
    print(f"Subarray with sum {target_sum}: {result}")
else:
    print("No subarray found with the given sum.")
