# print("ggggg")
# age = 30
# age = 31
# print("age:", age)

# num = 5.6
# f_n = "r"
# is_true = False
# print("num:", num, ",f_n:", f_n, ",is_true:", is_true)

# name = input("what is your name? ")
# print("hello " + name)

# year = input("year: ")
# age = 2022 - int(year)
# print(age)

# num1 = input("num1: ")
# num2 = input("num2: ")
# sum = float(num1) + float(num2)
# num1 = float(input("num1: "))
# num2 = float(input("num2: "))
# sum = num1 + num2
# print("sum: " + str(sum))


# For the weight converter i use 1kg = 2.2046 lbs
# weight = float(input("Weight: "))
# unit = str(input("(K)g or (L)bs: "))
# if unit == "k" or unit == "K":
#     lbs = weight * 2.2046
#     print("Weight in Lbs: " + str(round(lbs, 2)))
# elif unit == "l" or unit == "L":
#     kg = weight / 2.2046
#     print("Weight in Kg: " + str(round(kg, 2)))

# string = object
# name = "jfasasajd"
# print(name.upper())
# print(name.find('ajd'))
# print(name.replace('ajd', 'DDD'))
# print('ajd' in name)
# print(name)

# print(89/5)
# print(89//5)
# print(8 % 5)
# print(20 * 5)
# print(20 ** 5)

# x = (10 + 3) * 2
# print(x)
# x = 3 > 50
# print(x)


# price = 1000
# print(price > 10 and price < 200)
# print(price < 10 or price < 200)
# print(not price > 10)

# and
# # or
# # not

# # price = 5
# # print(price > 10 and price < 30)  # true true = true
# # print(price > 10 or price < 30)  # true false = true
# # print(not price > 10)  # true false = true


# temp = -7

# if temp >= 30:
#     print("its noy winter")
# elif temp >= 20:
#     print("its almost winter")
# elif temp >= 10:
#     print("its winter")
# else:
#     print("its very winter")
# print("done")

# weight = int(input("weight : "))
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("weight in lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("weight in Kg: " + str(converted))

# i = 1

# while i <= 10:
#     print(i * '*')
#     i = i + 1

# names = ['a', 'v', 'u', 'f', 's', 'x']
# names[0] = 'A'
# print(names[0:3])
# print(names)
# print(names[0])
# print(names[-1])
# print(names[-2])

# nums = [1, 2, 3, 4, 5]
# nums.append(6)
# nums.insert(0, 0)
# nums.remove(3)
# nums.clear()
# print(nums)
# print(1 in nums)
# print(len(nums))

# nums = [1, 2, 3, 4, 5]
# for item in nums:
#     print(item)

nums = range(5, 10, 2)
# print(nums)
for number in nums:
    print(number)
