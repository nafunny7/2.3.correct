numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(numbers):
    if numbers[a] > 0:
        print(numbers[a])
    elif numbers[a] < 0:
        break

    a += 1
