numbers = [3, 4, 6, 7, 11, 15, 17, 18, 20]

prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x > 1, numbers))

print(f'Prime numbers: {prime_numbers}')