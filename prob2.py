strings = ["orange", "apple", "pear", "pineapple", "banana"]
sorted_string = sorted(strings, key=lambda string: (len(string), string))
print(sorted_string)