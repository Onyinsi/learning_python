fruits = ["orange", "apples", "Mango", "Pineapples", "banana"]
print(f"the fruit basket currently has {len(fruits)} fruits")

fruits.append("lemon")
print(fruits)
print(f"the fruit basket currently has {len(fruits)} fruits")

fruits.remove('Pineapples')
print(fruits)

fruits.insert(3, "pineapple")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop()
print(fruits)
