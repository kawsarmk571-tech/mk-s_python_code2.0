numbers = [12, 7, 19, 24, 5, 18, 30, 11]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print(f"the number of even is: {even_count}")
print(f"the number of odd is: {odd_count}")