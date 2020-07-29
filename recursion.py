# 1. Write a Python program to calculate the sum of a list of numbers.
def factorial_sum(list_of_nums):
    if len(list_of_nums) == 0:
        return 0
    poped_item = list_of_nums.pop()
    return poped_item + factorial_sum(list_of_nums)

# 4. Write a Python program to get the factorial of a non-negative integer.
def factorial(n):
    if n >= 1:
        if n == 1:
            return 1
        return n * factorial(n - 1)
    else:
        raise Exception("You need to factorial a number that is greater then 0")



# 10. Write a Python program to calculate the value of 'a' to the power 'b'.
def power(n1, n2):
    if n1 >= 1 and n2 >= 1:
        if n2 == 1:
            return n1
        return n1 * power(n1, n2-1)
    else:
        raise Exception("You need to provide numbers that are greater then 0")


print(power(7,1))
