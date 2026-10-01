def calculate_bill(price, tax=5):
    total = price + tax
    return total
ans1=calculate_bill(500)
print(f"total bill with default tax :{ans1}")

ans2=calculate_bill(200,100)
print(f"total bill with default tax:{ans2}")


