# Print prime numbers
def prime_checker(number):
    for num in range(2, number+1):
        isprime = True
        for i in range(2, num):
            if i*i > num:
                break
            if num %i == 0:
                isprime = False
                break
        if isprime:
            print(num, end=" ")
n = int(input("enter number: "))
prime_checker(number = n)


# Output:
enter number: 90
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 
