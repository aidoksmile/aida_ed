numbers = [1,5,2,6,3,4,9]
size = 7
index = 0
while index < size and index < size - 1 - index:
    temp = numbers[index]
    numbers[index] = numbers[size - 1 - index]
    numbers[size - 1 - index] = temp
    index = index + 1
print(numbers)