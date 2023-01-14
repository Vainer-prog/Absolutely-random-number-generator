import random

start = int(input("From number: "))
end = int(input("To number: "))

num1 = random.randint(start, end)
num2 = random.randint(start, end)
num3 = random.randint(start, end)
num4 = random.randint(start, end)
num5 = random.randint(start, end)
num6 = random.randint(start, end)
num7 = random.randint(start, end)
num8 = random.randint(start, end)
num9 = random.randint(start, end)
num10 = random.randint(start, end)

average = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10) / 10
average = round(average)

print("Random number:", average)
