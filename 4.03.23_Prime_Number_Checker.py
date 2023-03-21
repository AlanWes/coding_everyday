divisible = 0
def prime_checker(number):
    count = 1
    while count != number + 1:
        global divisible
        if number % count == 0:
            divisible += 1
            count += 1
        else:
            count += 1
        
n = int(input("Check this number: "))
prime_checker(number=n)

if divisible > 2:
    print("It's not a prime number.")
else:
    print("It's a prime number.")