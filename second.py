# reversed — перевернуть массив
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
print(list(reversed(arr)))

# булевы значения
x = -2
true_val = True
false_val = False
if (x > 0) == true_val:
    print("true")
else:
    print("false")

# цикл с предусловием
x = 0
while x > 0:
    print(x)
    x = x - 1
else:
    print("ended")

# else работает и для for
for i in range(0, 10):
    if i < 0:
        print("negative")
else:
    print("no negative")

# выход из цикла
#
# continue - переход к следующей итерации
# break - выход из цикла совсем
for i in reversed([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    if i < 5:
        break
    print(i)

# "вечный" цикл
x = 0
while True:
    print("%s hi %s %s" % (x, 10, x * 2))
    x = x + 1
    if x > 10:
        break


# for i in range(0, 10):
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# вывести только четные числа из range(0, 10)
# используя continue и/или break

# функции - переиспользование кода


# не возвращающие значение
def print_odd(times):
    for i in range(0, times):
        print("odd")


print_odd(1)
print("--------")

# возвращающие значения
def even_odd(i):
    if i % 2 == 0:
        return "even"
    else:
        return "odd"


for i in range(0, 10):
    var = even_odd(i)
    print(var)

print(pow(2, 3))


# fizz/buzz classic problem
#
# написать функцию, которая принимает число
# и возвращает
# - "fizz" если число делится на 3
# - "buzz" если число делится на 5
# - "fizzbuzz" если число делится и на 3, и на 5

print("----------- fizzbuzz here ---------------")


def fizz_buzz(i):
    if i % 15 == 0:
        return "fizzbuzz"

    if i % 3 == 0:
        return "fizz"

    if i % 5 == 0:
        return "buzz"

    return "%s" % i


for i in range(1, 25):
    # print(fizz_buzz(i))
    if i % 15 == 0:
        print("fizzbuzz")

    if i % 3 == 0:
        print("fizz")

    if i % 5 == 0:
        print("buzz")
    else:
        print("%s" % i)

# def boil(food):
#   pan = take_pan()
#   pour_water(pan)
#   put_inside(pan, food)
#   put_on_stove(pan)
#   while not is_boiled(food):
#     print("waiting")

#   return(food)
