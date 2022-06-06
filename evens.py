def even_number_of_evens(numbers):
    """
    Should raise a TypeError is a list is not passed into the function
    Error Message: "A list was not passed into the function"
    IF the number of even numbers is odd, return False
    IF the number of even numbers is 0, return False
    IF the number of even numbers is even, return True
    """
    if isinstance(numbers, list):
        # evens = 0

        # for n in numbers:
        #     if n % 2 == 0:
        #         evens += 1
        # Replace For loops with List/Dictionary comprehension

        evens = sum([1 for n in numbers if n % 2 == 0])

        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False
        # It is also possible to use Conditional Expression

        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    print(even_number_of_evens(5))
