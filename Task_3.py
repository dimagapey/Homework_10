def shift(list, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            list.append(list.pop(0))
    else:
        for i in range(steps):
            list.insert(0, list.pop())


numbers = [3, 7, 10, 22, 45, 55, 91, 101, 130, 200]
print(numbers)

shift(numbers, -4)
print(numbers)

shift(numbers, 5)
print(numbers)