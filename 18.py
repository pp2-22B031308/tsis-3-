def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'The prime numbers in the list {numbers} are: {filter_prime(numbers)}')

