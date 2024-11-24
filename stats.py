import statistics

numbers = []
while True:
    value = int(input("Choose a number between 0 to infinty. Type 'done' to end adding numbers. "))
    if value == 'done':
        break
    else:
        numbers.append(value)

mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)

print("The mean is ", mean)
print("The median is ", median)
print("The mode is ", mode)
        