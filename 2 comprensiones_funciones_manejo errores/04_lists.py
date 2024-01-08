"""
numbers = []
for element in range(1, 11):
    numbers.append(element)

print(numbers)

#APLICANDO LIST COMPREHENSION
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

"""

numbers = []
for i in range (1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)
print(numbers)