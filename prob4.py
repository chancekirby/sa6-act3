lst1 = [1, 21, 13, 10, 9, 11, 34]
lst2 = [2, 10, 18, 34, 19, 5, 6]

intersection = list(filter(lambda x: x in lst1, lst2))

print(intersection)