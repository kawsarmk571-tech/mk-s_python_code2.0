numbers = [10, 45, 2, 99, 56, 89]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_largest = unique_numbers[-2]
print(f"the unique list is :{numbers}")
print(f"the second largest number is :{second_largest}")