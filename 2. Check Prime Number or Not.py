# Check Prime number or not
def prime_checker(number):
    isprime = True
    for num in range(2, number):
        if number % num == 0:
            isprime = False
    if isprime and num > 1:
        print("it is a prime number")
    else:
        print("not a prime number")
n = int(input("enter number: "))
prime_checker(number = n)


# Output:
Sample - 1
enter number: 29
it is a prime number

Sample - 2
enter number: 67890
not a prime number
