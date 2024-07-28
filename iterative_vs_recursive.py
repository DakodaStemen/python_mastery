#iterative approach
def factorial(n):
    the_product = 1

    while n > 0:
        the_product *= n
        n -= 1

    return the_product


print(factorial(5))


#recursive approach
def factorial(n):
    if n == 0:
        return 1

    else:
        return n * factorial(n - 1)


print(factorial(5))

#--------------------------------------------------------------------------------


#iterative approach
def sum_list_iterative(lst):
    total = 0
    for num in lst:
        total += num
    return total


print(sum_list_iterative([1, 2, 3, 4, 5]))


#recursive approach
def sum_list_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])


print(sum_list_recursive([1, 2, 3, 4, 5]))

#--------------------------------------------------------------------------------


#iterative approach
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fibonacci_iterative(10))


#recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(10))

#--------------------------------------------------------------------------------


#iterative approach
def reverse_string_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


print(reverse_string_iterative("hello"))


#recursion approach
def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    return reverse_string_recursive(s[1:]) + s[0]


print(reverse_string_recursive("hello"))

#--------------------------------------------------------------------------------


#iterative approach
def find_max_iterative(lst):
    max_val = float('-inf')
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


print(find_max_iterative([3, 5, 2, 8, 1]))


#recusive approach
def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    max_of_rest = find_max_recursive(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest


print(find_max_recursive([3, 5, 2, 8, 1]))