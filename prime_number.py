number = int(input("Number: "))

if number > 1:
    for x in range(2, int(number/2)):
        if (number % x) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")