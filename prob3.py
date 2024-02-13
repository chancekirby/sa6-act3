numbers = [2, 4, 5, 1, 0, 9, 7]

n = len(numbers)
max_num = numbers[0]

find_max = lambda max_num, x: x if x > max_num else max_num

for i in range(1, n):
    max_num = find_max(max_num, numbers[i])

print(max_num)